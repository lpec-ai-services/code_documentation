<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/elasticity/thermalExpansionFormulation.html -->

# ThermalExpansionFormulation

## Introduction

This formulation expresses the expansion of matter due to heat transfer in solid materials.
It is designed to be used with a `LinearizedElasticityFiniteElementFormulation`, in
an implicit, linear, finite element framework for solid mechanics.

## Example of usage

The following include is required:

```c++
#include "manta/components-fem_thermomechanics/thermal_expansion_formulation.h"
```

It can be constructed with:

```c++
    auto &thermalExpansionForm1 = rm.make<ThermalExpansionFormulation<planeStrain, ShapeId::qua8>>(
        m1, Uvar, QuadId::qua9, thermalExpansionCoeff1, youngModulus1, poissonCoeff1, Tref, T);
```

## Parameters

`ThermalExpansionFormulation` has two template parameters:

- `planeStrain`, the structural hypothesis,
- `ShapeId::qua8`, The shape ID of the domain where the formulation is defined,

`ThermalExpansionFormulation` has eight parameters:

- `m1`, the meshSet onto which the formulation is defined,
- `Uvar`, the dof variable of the displacement field,
- `QuadId::qua9`, the quadrature used to integrate the formulation,
- `thermalExpansionCoeff1`, the thermal expansion coefficient,
- `youngModulus1`, the Young's modulis,
- `poissonCoeff1` , the Poisson ratio,
- `Tref`, a `Real`, representing previous temperature.
- `T`, a `NodeField` of the temperature field.

## Description

## List of commented examples and verification tests

- In the thermomeca component verification test.

Test case location

The test case can be found at:

[<MANTA REPO>/src/components/fem_thermomechanics/tests/thermomeca/](https://gitlab.com/manta-project/manta/-/tree/master/src/components/fem_thermomechanics/tests/thermomeca/)
