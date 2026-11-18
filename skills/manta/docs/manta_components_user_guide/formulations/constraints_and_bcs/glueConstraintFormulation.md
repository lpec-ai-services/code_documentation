<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/glueConstraintFormulation.html -->

# GlueConstraintFormulation

## Introduction

This formulation aims at driving the primal defined on a "slave" `MeshSet`,
by the primal defined on a "master" `MeshSet`. Dofs defined on the nodes of
the slave set are defined as an interpolation of the master set dofs at the position
of the slave nodes.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-fem_tools/constraints/glue_constraint_set.h"
```

Here is the constructor of the formulation:

```c++
  auto &glueForm = rm.make<GlueConstraintFormulation<cellShapeId>>(steel, concrete, Uvar, Uvar, comp1, comp2);
```

## Parameters

`GlueConstraintFormulation` has the following template parameter:

- `cellShapeId`, the shape function used for the discretization of the constrained primals

`GlueConstraintFormulation` has the following parameters:

- `steel`, the "slave" constrained `MeshSet`,
- `concrete`, the "master "`MeshSet` onto which the slave's primal is based,
- `Uvar`, the dof variable of the constrained primal,
- `Uvar`, the dof variable of the "master" primal,
- `comp1`, a `Vector` of `Int` designating the components of the primal to constrain,
- `comp2`, a `Vector` of `Int` designating the components of the primal that constrains,

## How to use

A `GlueConstraintFormulation` requires the construction of a
`ConstraintSet` which acts as the contribution of
the constraint to the `LinearSystem`.

In the previous example those steps were nescessary:

```c++
  auto &glue = rm.make<ConstraintSet>(feSystem, "glue");
  rm.assignFormulationToLinearSystem(glueForm, glue);
```

## List of commented examples and verification tests

- Example : in component tests steel_concrete_link

## Description

Consider two `MeshSets`, `SET1`, the master mesh, and `SET2`, a slave mesh.
As explained above, this formulation enables to compute the contribution of a
constraint where `SET2` would be strongly tied to `SET1`. This constraints means that
the constrained degrees of freedom defined on `SET2`, would be completely driven by the degrees of
freedom defined on `SET1`. Consider the position \(x = (x0, y0, z0)\) of a given entity of `SET2`,
which is located within a given element of `SET1`, \(E_{SET1}\), containing \(k\) nodes. The constraint on a given
degree of freedom (DOF) of `SET2` can be expressed as:

\[\Sigma_i^k \left(N^i(x) \cdot DOF_{`SET1`}^i\right) = DOF_{`SET2`}\]

where \(N^i\) is defined as the shape function interpolating the primal,
at the \(i^{th}\) node of \(E_{SET1}\), the element containing the slave node.
