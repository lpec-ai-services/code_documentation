<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/user_guide_objects/user_fields.html -->

# User guide for Fields

This page describes the field object in MANTA and describes some common
usage at this c++ layer. Even more details about fields can be found in
[this section of the developer guide](../../../developer_guide/services/details_fields.md#details-fields).

The *fields* are a central data structure in MANTA. A
*field* manages some data attached to the entities of a *meshset*.
In this page, the *mesh set* related
to the considered *field* is called 'support'. Each *entity*
of the support is attached to a set of matrices of real coefficients. Such
a matrix is called a 'value' in this page.

Important

- The number of values attached to the entities of the support
  *mesh set* of a given *field* instance is the same for
  all these entities.
- All the values (*i.e.* a matrix attached to an *entity* of
  the support *mesh set*) of a given *field* instance have
  the same number of rows and columns.

In this page, the 'size' of a *field* refers to the number of
columns and rows of its values.

## The different kinds of *fields*

There are 3 main kinds of *fields*: The *node fields*, the
*element fields* and the *ip fields*. These 3 kinds of
*fields* have a common usage, but some specific functions are
defined for each of them, especially to set values to them.

### *Node field*

A *node field* associates a single value to each node of its support,
*i.e.* the entities that are recovered using the
`MeshSet::getNodes()` member function of the support.

Important

A *node field* does not have to be defined on a *mesh set*
of type 'node'. It can be defined on any *mesh set*.
The entities supporting values are nodes of the *mesh set* which can be obtained
using `MeshSet::getNodes()` and **not**
`MeshSet::getItems()` (note: for a support
*mesh set* of type 'node', these entities are the same).

### *Element field*

An *element field* links some data to each *entity* of its
support, *i.e.* the entities that are recovered using the
`MeshSet::getItems()` member function of the support.
The number of values attached to each *entity* is given as an
argument to the constructor. A default value of 1 is defined for this
argument, so unless differently specified, a single value is attached
to each *entity* of the support.

### *IP field*

An *ip field* is essentially the same as an *element field*
(internally, it derives form an *element field*). The main
difference for the end user is that its constructor requires to specify
a quadrature form so that the number of values attached to each
*entity* is equal to the number of points in the
considered quadrature.

### Construction

Important

Due to the internal [The memory layout](../../../developer_guide/services/details_fields.md#memory-layout):

- Every *field* **must** be constructed through a
  *resources manager*, **before** the call to
  `ResourcesManager::init()`.
- The field values **must not** be handled before the call to
  `ResourcesManager::init()`.

The following snippets illustrate how to construct *fields* with
static sizes through a *resources manager*. Here `rm` is a `ResourcesManager`
instance and `support` is assumed to be a *mesh set* containing
quadrangular cells.

```c++
    auto &ipf = rm.make<IPField<2, 3>>(support, "my 2x3 IP field with static size", QuadId::qua4);        // ①
    auto &nf  = rm.make<NodeField<1, 3>>(support, "my 1x3 node field with static size");                  // ②
    auto &ef  = rm.make<ElementField<4, 2>>(support, "my 4x2 element field with static size", 4);         // ③
```

1. This constructs an *ip field* within the *resources manager* which is defined
   on the *mesh set* `support`, and which attaches 4 values on
   each quadrangle of `support`. The second argument is a string which
   is only used for post-treatment or screen output. The
   `ResourcesManager::make()` function returns a reference to the create
   field, so `auto &` is used (as a field cannot be copied, `auto`
   without the `&` would not have compiled).
2. This constructs a *node field* which is defined on the nodes of
   the *mesh set* `support`.
3. This constructs an *element field* which is defined on the
   *mesh set* `support`, and which attach 4 values on each
   quadrangle of `support`.

The following snippet does exactly the same, but with dynamic sizes:

```c++
    Int nRows, nCols;

    nRows     = 2;
    nCols     = 3;
    auto &ipf = rm.make<IPField<>>(support, "my 2x3 IP field with dynamic size", nRows, nCols, QuadId::qua4);

    nRows    = 1;
    nCols    = 3;
    auto &nf = rm.make<NodeField<dynamic, dynamic>>(support, "my 1x3 node field with dynamic size", nRows, nCols);

    nRows    = 4;
    nCols    = 2;
    auto &ef = rm.make<ElementField<>>(support, "my 4x2 element field with dynamic size", nRows, nCols);
```

Notice that the size must be passed as runtime arguments to the
constructor, and that the `dynamic` value for the template parameters
is the default value and so can be omitted.

### Operations

The fields support some arithmetic operations such as:

```c++
  f2 += (f0 * transpose(f1)) * f1 - 2. * (f2 + f0);
```

where `f0`, `f1` and `f2` are some `2x3` fields. Notice that
`f2` has to be mutable, but `f0` and `f1` can be constant in this
expression.

Note

Lazy evaluation technique is used so that no temporary fields are
created when evaluating arithmetic expressions on fields.

The arithmetic expressions on field are evaluated value-wise. For
example, assuming that `f0`, `f1` and `f2` are
*element fields* or *ip fields*, the above expression amounts to:

```c++
  for (const auto h : f2.getMeshSet()) {
    for (Int iVal = 0; iVal < f2.getNumValsPerEntity(); ++iVal) {
      f2.getValue(h, iVal) += (f0.getValue(h, iVal) * transpose(f1.getValue(h, iVal))) * f1.getValue(h, iVal) - 2. * (f2.getValue(h, iVal) + f0.getValue(h, iVal));
    }
  }
```

The following assignment and compound assignment operators are defined
for mutable fields:

- `=`: assigns t each value of the field the related value defined
  by the rhs expression.
- `+=`: adds t each value of the field the related value defined by
  the rhs expression.
- `-=`: subtracts t each value of the field the related value
  defined by the rhs expression.
- `*=`: multiplies eac value of the field with the related value
  defined by the rhs expression.

  Warning

  This multiplication is the "matrix-multiplication", not a
  coefficient-wise multiplication.

  Note

  The rhs can be a scalar. In this case, the lhs field is "scaled"
  (all the coefficients of all the values are multiplied by the rhs
  scalar).
- `/=`: Only defined for a scalar rhs. Scales the lhs field by the
  inverse of the rhs scalar.

The operators `+`, `-`, `*` `/` are defined with the same
meaning as their compound assignment operator counterpart.

The following unary operators are available:
- `abs(f)`: return a field containing the coefficient-wise absolute values of `f`
- `cwiseInv(f)`: return a field containing the coefficient-wise inverse values of `f`
- `transpose(f)`: return a field containing the transposed values of `f`

The following binary operators are available:
- `cwiseProd(f1, f2)`: return a field containing the coefficient-wise product between values of `f1` and `f2`
- `cwiseDiv(f1, f2)`: return a field containing the coefficient-wise division between values of `f1` and `f2`

## Common usage

### Get a value

All *fields* implement a `getValue` function, which returns a
matrix-like object that can be used to manipulate a value related to an
input *entity*. Let’s consider the following snippet, where `nf`
is a *node field* of size `2x3`:

```c++
  const MeshSet &support              = nf.getMeshSet();           // ①
  const EntityHandle &thirdNode       = support.getNode(2);        // ②
  auto M                              = nf.getValue(thirdNode);    // ③

  Matrix<2, 2> MMt = M * transpose(M);    // ④
  M *= 2.;                                 // ⑤
```

1. this gets the support.
2. this gets the 3rd node of the support. Note that `nf` being a
   *node field*, `getNode` is used and not `getItem`.
3. this gets an object `M` representing the value attached to the
   3rd node of the support. The actual type of `M` is an opaque type
   that is cumbersome to write and that the user does not have to know
   about. So the use of `auto` is strongly advised. What is
   important is that `M` behaves exactly like a
   matrix of size `2x3`(it has the same
   interface). Here `nf` is mutable, so `M` can be read and written
   to. If `nf` was `const`, then `M` could not be written to.
4. this reads the value.
5. this writes to the value.

Note

The `getValue` function returns a type which behaves exactly as a
matrix (it has the same interface) whose size is
related to the number of rows and columns of the considered field.

Here is another example with an *ip field*:

```c++
  for (const auto &cell : ipf.getMeshSet()) {                                   // ①
    for (Int iIP = 0; iIP < Quadrature::getNumPts(ipf.getQuadId()); ++iIP) {    // ②
      auto M = ipf.getValue(cell, iIP);                                         // ③
    }
  }
```

1. loop over the items of the support of the field: the `getMeshSet`
   returns a reference to a constant *meshset*, which can be used
   as a container of entities (and a range-loop can be used). If the
   considered field has been a *node field* instead of an *ip field*,
   then one would have to do:

   ```c++
   for (const auto &node : nf.getMeshSet().getNodes()) {}
   ```

   to iterate over the nodes.
2. loop over the integration points of the quadrature related to the
   considered field.
3. this gets the value attached to the current integration point.

Warning

Querying a field on an *entity* which does not belongs to its
support, or for a value rank which is larger than the number of values
per *entity* of the field, has an undefined behavior (and is likely
to crash) for non-debug build. For a debug build, an error is
triggered.

### Reductions

Various free functions are available to perform reduction across all the values of all the MPI processes.

The `max`, `min` and, `sum` reduction operations are available as free functions, for all type of *fields*.

```c++
  Matrix<3, 3> fieldMax = max(field);
  Matrix<3, 3> fieldMin = min(field);
  Matrix<3, 3> fieldSum = sum(field);
```

For more specific needs, the function `fieldReduction` is available, which allows to
perform the reduction with a custom lambda function.

Warning

`fieldReduction` has some specificity about its usage. For basic
needs, where `max`, `min` and, `sum` are enough to do the
job, prefer use those functions. If the use of `fieldReduction` is
needed, read the doc carefully.

In the following snippet, the coefficient-wise norm-2 of the values of a
`3x3` field is computed:

```c++
  Matrix<3, 3> cwiseNorm2 = fieldReduction(
                 field, // ①
                 [](const auto &a, const auto &b){return square(a) + square(b);} // ②
                 );
  cwiseNorm2 = manta::sqrt(cwiseNorm2);
```

1. The considered *field*.
2. The reduction operator.

   Warning

   This reduction operator **must** be a binary operator, commutative
   and associative. If not commutative or associative, the result is
   undefined.

Note

The result of a reduction is always a matrix of size corresponding to the
field. For example, a temperature field is commonly a `1x1` field and
the result of a reduction over a temperature field would be a `1x1`
matrix that could be transformed into a `Real` value by accessing the
`(0,0)` coefficient.

What follows is another snippet in which the maximum coefficient of all
the values (across all MPI processes) of a `3x3` *field* is
computed. This is a bit trickier as the former one, because it is in
fact a reduction (over the values of the *field*) of a reduction
(over the coefficients of a value).

```c++
  Real fieldReductionMax = maxCoeff(max(field));
```

Note

`fieldReduction` involves a collective MPI communication between
all the MPI processes. So it must be called by all the processes.

A more specific function is available to perform a reduction over one
particular mesh entity (of type depending on the field type). the
following snipet gives an example of its use:

```c++
  auto &entities = field.getEntities();
  auto &entity = entities[0];
  auto result = entityFieldReduction(entity, field, [](const auto &a, const auto &b){return a + b;} );
```

## Specific functions

Some functions specific to a *field* kind (node, element, ip) are
also defined, mainly to set values.

A non-exhaustive list of such functions usages follows.

### Set to each *entity* of an *element field* the average value of a function

This sets to the *entities* (which are quadrangles) of the `1x1`
*element field* `ef` the average value of the distance to a point
`center` on each *entity*:

```c++
  ef.setValue(
      [&center](ConstRowVectorRef<> &x) { // ①
        Matrix<1, 1> M;
        M(0, 0) = std::sqrt(norm(x - center));
        return M;
      },
      QuadId::qua9); // ②
```

1. input functor which has a single argument: the space position. Here a
   lambda which captures the point `center` is used.
2. quadrature to be used to compute the average value on each *entity*.

Note

The use of a single quadrature as argument imposes that all the
*entities* of the support of the considered *field* are of
the same geometrical type.

### Set to each *node* of an *node field* the value of a function

This sets to the nodes of the `2x1` *node field* `nf`, the
position of the node with respect to a point `center`:

```c++
  nf.setValue([&center](ConstRowVectorRef<> &x) {
    Matrix<1, 2> M;
    M = x - center;
    return M;
  });
```

### Set to each *ip* of an *ip field* the value of the finite-element interpolation of a *node field*

This sets to each *ip* of the *ip field* `ipf` the value of
the finite-element interpolation of the *node field* `nf`. The
shape functions that match the geometrical types of the *entities*
of the support of the *ip field* are used.

```c++
  ipf.setValue(nf);
```

Warning

The support and the sizes of the *ip field* and the *node field*
must be the same. Otherwise, it would probably crash…​
