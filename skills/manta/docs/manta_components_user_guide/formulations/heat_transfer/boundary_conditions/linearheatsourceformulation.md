<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/heat_transfer/boundary_conditions/linearheatsourceformulation.html -->

# LinearHeatSourceFormulation

## Introduction

This formulation is used to describe the contribution of a heat source
on the temperature field in a solid material.

## Example of usage

The following include is required:

```c++
#include "manta/components-fem_heat_transfer/heat_source_formulation.h"
```

It can be constructed with:

```c++
    auto &thermalSourceForm =
        rm.make<LinearHeatSourceFormulation<h, ShapeId::qua8, Real>>(m1, QuadId::qua9, ct, Tvar, thermalSource);
```

## Parameters

`LinearHeatSourceFormulation` has three template parameters

- `h`, is the geometric hypothesis,
- `ShapeId::qua8`, is the shape ID,
- `Real`, is the evaluator type of the source

`LinearHeatSourceFormulation` has 8 parameters

- `m1`, the meshSet onto which the formulation is defined,
- `QuadId::qua9`, the quadrature which is used to integrate on the mesh,
- `ct`, the configuration time onto which everything is integrated,
- `Tvar`, the dof variable of the primal,
- `thermalSource`, evaluator of the source.

## Description

## List of commented examples and verification tests

- in the "thermomeca" test in fem_thermomechanics

## Notes

- A "non-linear" version is created but it has no difference with the linear version, and it is not yet used.
