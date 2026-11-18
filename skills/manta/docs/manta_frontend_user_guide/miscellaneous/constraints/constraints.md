<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/constraints/constraints.html -->

# Imposing constraints on unknowns

This section describes some general bricks imposing constraints on the
unknowns. Those bricks currently all derive from the ConstraintsSet
brick which manages a set of constraints (See the documentation
[Linear system](../../../developer_guide/pipeline/linear_system.md#linear-system) for in depths details about how constraints are
handled, in particular Section [The constraint sets](../../../developer_guide/pipeline/linear_system.md#constraint-sets)).

See also

Further help about available constraints can be found in the
`Constraints` section of the online help which is accessible in
`python` through the `manta.help` function or through the
`manta-help` utility (see Section [The manta-info utility](../tools.md#manta-help-utility)).

PYTHON

```python
manta.help('Constraints')
```

SH

```sh
manta-help Constraints
```

## Available bricks

[![Link between bricks associated with constraints](https://manta-project.gitlab.io/manta/_images/constraints.svg)](../../../_images/constraints.svg)

### The `ConstraintsSet` brick

The `ConstraintsSet` brick manages a set of constraints. The
constraints available by default are described in Section
[The ImposedTemperature brick](#available-constraints).

Note

The constraints are instanciated through the `ConstraintFactory`
class (See Section [The AbstractConstraint and the ConstraintFactory classes](#abstract-constraint-abstract-factory-classes)).

#### Parameters

The following parameters are allowed:

- `strategy`: selection of the elimination method (string or
  dictionary).

  The following strategies can be defined by a string:

  - `elimination` (default),
  - `LagrangeMultipliers`,
  - `penalty` and
  - `Ainsworth`.

  When using a dictionary, the key selects the strategy. Currently, only
  the `masterSlave` and the `penalty` strategies can be selected by a
  dictionary:

  - The `masterSlave` strategy also requires the `slave`
    key which gives the name of a mesh set used as the slave.
  - The `penalty` strategy also to specify the parameter
    `penalyCoefficient`.
- `constraint`: description of the imposed constraint (dictionary)
- `constraints`: list of imposed constraints (vector of dictionary)

#### Examples of usage

The following example declares one constraint that will be treated by
the `Ainsworth` strategy:

PYTHON

```python
m.add('ConstraintsSet',
      constraint = {'Dirichlet': {'unknown': 'Temperature',
                                  'boundary': 'left',
                                  'value': 'LeftTemperature'}},
      strategy = 'Ainsworth')
```

The following example declares two constraints that will be treated in
by the same constraint set (see Section [The constraint sets](../../../developer_guide/pipeline/linear_system.md#constraint-sets) for
details):

PYTHON

```python
m.add('ConstraintsSet',
      constraints = [{'Dirichlet': {'unknown': 'Temperature',
                                    'boundary': 'left',
                                    'value': 'LeftTemperature'}},
                     {'Dirichlet': {'unknown': 'Temperature',
                                    'boundary': 'right',
                                    'value': 'RightTemperature'}}],
      strategy = 'elimination')
```

See also

The online help for the `ConstraintsSet` brick is accessible as
follows:

PYTHON

```python
manta.help('Model bricks', 'ConstraintsSet')
```

SH

```sh
manta-help "Model bricks":ConstraintsSet
```

### The `DirichletBoundaryCondition` brick

The `DirichletBoundaryCondition` brick is a restriction of the
`ConstraintsSet` brick which manages only one Dirichlet
constraint (see Section [The Dirichlet constraint](#dirichlet-constraint)).

#### Parameters

The parameters of the `DirichletBoundaryCondition` brick combines
the `strategy` parameter of the `ConstraintsSet` brick (see
Section [The ConstraintsSet brick](#constraints-set-brick)) and the parameters of the
`Dirichlet` constraint (see Section [The Dirichlet constraint](#dirichlet-constraint)).

#### Example of usage

In the following example, the temperature is imposed in a thermal problem:

PYTHON

```python
m.add('DirichletBoundaryCondition',
      unknown  = 'Temperature',
      boundary = 'left',
      value    = 'LeftTemperature',
      strategy = 'elimination')
```

In explicit problems, the unknown is the acceleration. One can directly impose
the acceleration of nodes, such as follows, where the acceleration is imposed to zero:

```python
    model.add(
        'DirichletBoundaryCondition', 
        unknown = 'Acceleration', 
        boundary = 'left',
        components = (0, 1, 2),
        strategy = 'lagrangeMultipliers',
    )
```

It is also possible to impose the value of the acceleration or of the displacement,
providing the value of the `primitive` parameter (see parameters description in Section [The Dirichlet constraint](#dirichlet-constraint)).
Note that the unknown must always be the acceleration, as the integration scheme is still explicit.
When using the `primitive` parameter, the constraint is applied on the next time step because of the explicit scheme.

For instance:

```python
    model.add(
        'DirichletBoundaryCondition',
        unknown = 'Acceleration',
        boundary = 'right',
        component = 1,
        strategy = 'lagrangeMultipliers',
        primitive = prim, # if prim= 1,the constraint is imposed on the primitive of the acceleration,
                          # ie on the velocity. If prim = 2 it's imposed on the displacement.
        value = 'ImposedValue' # str to define a time evolution
    )
```

See also

The online help for the `ConstraintsSet` brick is accessible as
follows:

PYTHON

```python
manta.help('Model bricks', 'DirichletBoundaryCondition')
```

SH

```sh
manta-help "Model bricks":DirichletBoundaryCondition
```

### The `ImposedTemperature` brick

The `ImposedTemperature` brick is a specialisation of the
`Dirichlet` brick which imposes the unknown to be the
temperature. The parameters `component` and `components`
are also removed.

### The `ImposedDisplacement` brick

The `ImposedTemperature` brick is a specialisation of the
`Dirichlet` brick which imposes the unknown to be the
displacement.

## Available constraints

This section describes the constraints available in MANTA. The
constraints are not directly usable and must be used through the
ConstraintsSet brick.

### The `Dirichlet` constraint

#### Parameters

The following parameters are allowed:

- `reaction`: name used to export the reaction associated with
  the boundary condition
- `value`: imposed value (Real or string)
- `boundaries`: boundaries on which the boundary condition is
  applied (Vector of strings, interpreted as regular expressions)
- `boundary`: boundary on which the boundary condition is applied
  (String, interpreted as a regular expression)
- `components`: components affected by the boundary condition
  (Vector of integers)
- `component`: component affected by the boundary condition
  (Integer)
- `unknown`: name of the unknown field (String)
- `primitive`: integer (0,1 or 2) to select if the constraint is applied directly on the unknown (0, default)
  or on its primitive (1), or its second primitive (2)

See also

Further help about available constraints can be found in the
`Constraints:Dirichlet` section of the online help:

PYTHON

```python
manta.help('Constraints', 'Dirichlet')
```

SH

```sh
manta-help Constraints:Dirichlet
```

### The `ImposedTemperature` constraint

The `ImposedTemperature` constraint is a specialisation of the
`Dirichlet` constraint which imposes the unknown to be the
temperature. The parameters `component` and `components`
are also removed.

### The `ImposedDisplacement` constraint

The `ImposedDisplacement` constraint is a specialisation of the
`Dirichlet` constraint which imposes the unknown to be the
displacement. This constraint must be used for implicit problems only.

### The `MultiplePoints` constraint

#### LinearRelationsBetweenDegreesOfFreedom

This brick enables the enforcement of constraints between several degrees of freedom of the finite element mesh.
At the moment, only one multiple point constraint is available, the `LinearRelationsBetweenDegreesOfFreedom`.
The enforced constraint can be seen as the linear combination between those dofs such that:

\[\Sigma_i^n \left(a_i \cdot DOF_i\right) = RHS_{tot}\]

Note that this formulation enables the construction of constraints on \(n\) meshsets, each composed of \(m\) nodes, with
\(m\) being a constant or 1.

When we consider \(m > 1\), the ordering of nodes becomes of importance. In this case, the user *must* specify the `linker` parameter
in order to avoid issues of spurious ordering in the constraint. Future features will implement node ordering subroutines that enable users to specify
an ordering based on a geometric criterion.

For the moment, when no *nodesLinkingMethod* arguments is given, but when at least two `MeshSet` contains more than one node, an error message stops
the user.

#### Example of usage

The following code adds a *MultiplePointsConstraint*
brick to a monolithic thermo-mechanical model:

```python
m = manta.Model(...)
m.add('MultiplePointsConstraint',
  constrainedSets=['right','left', 'top'],
  coefficients=[1,1,-2],
  unknowns=['Displacement', 'Temperature', 'Displacement'],
  components=['UX','T','UY'],
  value=1.)
```

It imposes the following relationship between the nodes of `right`, `left` and `top`:

\[1\cdot \text{right}(\text{UX}) + 1\cdot \text{left}(\text{T}) -2\cdot \text{top}(\text{UY}) = 1\]

Therefore linking the displacement dofs of `right` and `top` with the temperature of `left`.

#### Main parameters

The main parameters used to initialize the brick are:

- `type` what type of multiple points constraint shall be used (*optional, only one type at the moment*)
- `constrainedSets` which meshsets are constrained together
- `coefficients` for each meshsets, which coefficient shall be used in the constraint
- `unknowns` for each meshsets, which primal shall be constrained
- `unknown` for each meshsets, which primal shall be constrained (in the case of a single primal)
- `components` for each meshsets, which component of the constrained primal shall be used in the constraint
- `nodesLinkingMethod` indicating the method used to link nodes together (*optional, only one type at the moment*)
- `value` value of the right hand side value. This parameter is optional (*default is 0*).

#### Notes on parameters

Note that the user can specify mismatching fields to constrain together. The argument `unknown` therefore has to be unique (in the case of a unique constrained primal),
or there must be as many specified `unknowns` as there are meshsets. On the other hand, as many `components` and `coefficients` as there are
`constrainedSets` must be specified.

Note that the order in which all of these parameters are specified is very important ! The specified components/coefficient/fields must be given in an order which is consistent
with the order in which the constrainedSets are given.

This constraint brick is only available with an Lagrange Multiplier's elimination strategy. Therefore, it is not useful to specify the strategy.

#### Node Linking method

For meshsets of \(m > 1\) nodes, the order at which we constrain the nodes of each meshsets together becomes relevant.
This is the role of the `linker` parameter: specify the order in which we constrain each nodes of each meshsets.
For a constraint involving \(n\) sets of \(m\) nodes each, one can specify \(m\) sets of \(n\) nodes to
enforce that a specific node of one meshset, mut be constrained with a specific node from another meshset.

For instance consider the example of a 2D square illustrated below. We want to constrain the sides together (`UX` components shall be equal on those sides).
However, since there are 3 nodes per side, the order with which we constrain the nodes two by two is very important.
For this specific example we enforce that the nodes constrained two by two follow
the geometric order: bottom nodes together, middle nodes together, and top nodes together.

[![figure](https://manta-project.gitlab.io/manta/_images/rela_ex1.svg)](../../../_images/rela_ex1.svg)

Using the nomenclature shown above, with `l_right` and `l_left` are constituted respectively by nodes `ptr`, `pmr`, `pbr`
and `ptl`, `pml`, `pbl`. We can enforce that `ptr`, `ptl`, the top nodes are constrained together,
as well as the mid nodes `pmr` and `pml`, and bottom nodes `pbr` and `pbl` respectively.
At the moment, there is only one `nodesLinkingMethod`: `seg2`, which relates nodes two by two throught sets of `SEG2` elements.
In the dictionnary entry `name`, inputted in `nodesLinkingMethod`, one shall indicate the string of the named set of `SEG2` linking those respective nodes.
Here three `SEG2` linking the constrained nodes must be defined.

```python
m = manta.Model(...)
m.add('MultiplePointsConstraint',
 constrainedSets=['l_right','l_left'],
 coefficients=[1,-1],
 unknown=['Displacement'],
 components=['UX','UX'],
 nodesLinkingMethod={'seg2':{'name':'meshSetOfSeg2LinkingNodes'}})
```

## The AbstractConstraint and the ConstraintFactory classes

Constraints derives from the `AbstractConstraint` class. The
`ConstraintFactory` is an abstract factory registring all
constraints available to the `ConstraintsSet` brick (see Section
[Factory functions and abstract factories](../../../developer_guide/dev_guidelines/patterns.md#abstract-factories)).
