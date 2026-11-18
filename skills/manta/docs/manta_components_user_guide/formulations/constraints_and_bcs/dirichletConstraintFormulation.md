<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/dirichletConstraintFormulation.html -->

# DirichletConstraintFormulation

## Introduction

This formulation aims at applying a Dirichlet constraint on some degrees of freedom
of the system to be solved.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-fem_tools/constraints/dirichlet_constraint_set.h"
```

Here is the constructor of the formulation:

```c++
    auto &im_bottom_form_impl = rm.make<DirichletConstraintFormulation<nDofsPerNodes, true>>(Uvar, bbottom);
```

## Parameters

`DirichletConstraintFormulation` has two template parameters:

- `nDofsPerNodes`, the number of degrees of freedom per nodes
- `true`, boolean for true if elimination of terms to reduce the size of the system

`DirichletConstraintFormulation` has the following parameters:

- `Uvar`, the constrained field's dof variable as a `DofVar`;
- `bbottom`, a `NodeField` of imposed values

## How to use

A `DirichletConstraintFormulation` requires the construction of a `NodeField`,
which is the support for the imported values, as well as the construction of a
`ConstraintSet` which acts as the contribution of the constraint to the `LinearSystem`.

To summarize, in the previous example those steps were necessary:

- Create a `NodeField` supported by the `Meshset` concerned with boundary condition:

  > ```c++
  >     auto &bbottom = rm.make<NodeField<>>(bottom, "", dim, 1);
  > ```
- Create the formulation (cf. [DirichletConstraintFormulation constructor](#dirich-ctor)).
- Set the formulation:

  > ```c++
  >     auto &im_bottom_impl = rm.make<ConstraintSet>(implicitSystem, "imposedMotions");
  > ```
- Assign the formulation to the `LinearSystem`:

  > ```c++
  >     rm.assignFormulationToLinearSystem(im_bottom_form_impl, im_bottom_impl);
  > ```
- After `rm.init()` is called, set the value of prescribed `NodeField`:

  > ```c++
  >     btop.setValue(0.);                     // option 1: set all dof of btop to a uniform real value
  >     ColVector<3> UImposed;                 // option 2: - create a vector of size = ndofs/node
  >     UImposed << 0., 0., std::nan("");      //           - set the vector ()"nan" is used for "free" dof)
  >     bbottom.setValue(UImposed, bottom);    //           - set bbottom dofs to this vector
  > ```

## Computing reactions

It is possible to keep track of reactions linked to the `ConstraintSet`
of a `LinearSystem`.

```c++
      Bool shallStop = implicitSystem.updateReactionField(ctx, R, Uvar).shallStop();    // R=C^t*\Lambda
```

which requires the construction of a `NodeField` here named `R`.

Users can choose to eliminate dirichlet constraints from the main system or not.
One can also choose to keep track of reactions, and ask to update the reaction field
linked to all or only a limited subsets of dirichlet constraints. More details about
this part of the code can be found in the [developer guide](../../../developer_guide/blueprints/compute_reactions.md#compute-reactions).
