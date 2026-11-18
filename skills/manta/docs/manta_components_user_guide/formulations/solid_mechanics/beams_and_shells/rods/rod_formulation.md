<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/rods/rod_formulation.html -->

# rodStiffnessMatrixFormulation

## Introduction

This formulation is used to compute the rigidity associated to a rod model between
specified degrees of freedom. A rod model is a 1D structure that can only be subjected to
axial strain (tension/compression).

## Example of usage

The following include is required:

```c++
#include "manta/components-modeling/finite_elements/rod_formulation.h"
```

It can be constructed with:

```c++
    auto &rodForm = rm.make<rodStiffnessMatrixFormulation<dim, cellShapeId, cellQuadId>>(beam, Uvar, matp, geop);
```

## Parameters

`rodStiffnessMatrixFormulation` has three template parameters:

- `dim`, is the dimension of the problem,
- `cellShapeId`, is the shape ID,
- `cellQuadId`, is quadrature ID

`rodStiffnessMatrixFormulation` has 4 parameters:

- `beam`, the meshSet onto which the formulation is defined,
- `Uvar`, the dof variable of the primal,
- `matp`, `OMap<std::string,Vector<Real>>` to contain material parameters,
- `geop`, `OMap<std::string,Vector<Real>>` to contain geometrical parameters.

## Material and Geometrical parameters

Two material parameters should be specified in `matp`

- `YoungModulus`, the Young modulus of the rod
- `PoissonRatio`, the Poisson's ratio of the rod

One geometric parameter shall be specified in `geop`

- `SEC`, the cross sectional area

Here is an example of the creation of an `OMap<std::string,Vector<Real>>`
to specify those terms.

```c++
  OMap<std::string, Vector<Real>> matpSteel;
  matpSteel["YoungModulus"] = {E_steel};
  matpSteel["PoissonRatio"] = {nu_steel};
  OMap<std::string, Vector<Real>> geopSteel;
  geopSteel["SEC"] = {sec};
```

## List of commented examples and verification tests

- in the nr/steel_concrete_link tests (used to model steel rods in reinforced concrete)
- in nr/implicit test for the use of a rod model alone
