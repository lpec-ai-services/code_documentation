<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/general_models/scalarlaplacianformulation.html -->

# ScalarLaplacianFormulation

## Introduction

This formulation aims at solving a scalar laplacian problem, also called
Laplace equation if the right hand side is nil, or Poisson's equation
if the right hand side is a specified given function. This formulation
is to be used in a finite element method framework. It yields the left hand
side of the mentionned equation.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-modeling/finite_elements/scalar_laplacian.h"
```

Here is the constructor of the formulation:

```c++
    auto &scalarLaplacianFormulation = rm.make<ScalarLaplacianFormulation<ShapeId::qua4>>(grid, QuadId::qua4, resultVar);
```

## Parameters

`ScalarLaplacianFormulation` has the following template parameter:

- `ShapeId::qua4`, the shape function used for the discretization of the primal field

`ScalarLaplacianFormulation` has the following parameters:

- `grid`, the mesh set onto which the formulation is defined;
- `QuadId::qua4`, the quadrature used to integrate the field in a given element
- `resultVar`, the dof variable linked with the primal field (result is the primal)

## List of commented examples and verification tests

- Example : in examples/scalar_laplacian, 2D result on a grid mesh
- Component verification tests: in components/modeling.

## Description

This formulation aims at solving the fundamental
scalar laplacian equation, by providing the left hand side equation term:
the Laplace operator.

The problem can be written as:

\[\begin{split}\begin{aligned}
&\text{Find }u\text{ such that:}\\
&\Delta u = f_d
\end{aligned}\end{split}\]

where:

- \(u\) is the scalar primal field
- \(\Delta\) is the laplacian operator
- \(f_d\) is a given right hand side

Note that this right hand side must be defined with another formulation,
(another equation term !). You can look at the scalar_laplacian example for
the definition of the right hand side using a Dirichlet formulation.
