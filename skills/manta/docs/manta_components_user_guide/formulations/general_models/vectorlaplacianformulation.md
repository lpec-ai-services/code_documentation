<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/general_models/vectorlaplacianformulation.html -->

# VectorLaplacianFormulation

## Introduction

This formulation aims at solving a vector laplacian problem, also called
Laplace equation if the right hand side is nil, or Poisson's equation
if the right hand side is a specified given function. This formulation
is to be used in a finite element method framework. It yields the left hand
side of the mentionned equation. It is the same as the scalar laplacian formulation
for a multidimensional primal field.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-modeling/finite_elements/vector_laplacian.h"
```

Here is the constructor of the formulation:

```c++
    auto &vectorLaplacianForm = rm.make<VectorLaplacianFormulation<ShapeId::qua4>>(grid, QuadId::qua4, resultVar);
```

## Parameters

`VectorLaplacianFormulation` has the following template parameter:

- `ShapeId::qua4`, the shape function used for the discretization of the primal field

`VectorLaplacianFormulation` has the following parameters:

- `grid`, the mesh set onto which the formulation is defined;
- `QuadId::qua4`, the quadrature used to integrate the field in a given element
- `resultVar`, the dof variable linked with the primal field (result is the primal)

## List of commented examples and verification tests

- Component non-regression tests: in components/modeling/tests/e2e/nr/vector_laplacian.

## Description

This formulation aims at solving the fundamental
vector laplacian equation, by providing the left hand side equation term:
the Laplace operator.

The problem can be written as:

\[\begin{split}\begin{aligned}
&\text{Find }u\text{ such that:}\\
&\Delta u = f_d
\end{aligned}\end{split}\]

where:

- \(u\) is the vectorial primal field
- \(\Delta\) is the laplacian operator
- \(f_d\) is a given right hand side

Note that this right hand side must be defined with another formulation,
(another equation term !). You can look at the scalar_laplacian example for
the definition of the right hand side using a Dirichlet formulation (in the case of
a scalar formulation).
