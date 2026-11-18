<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/elasticity/linearized_elasticity_finite_element_formulation.html -->

# `LinearizedElasticityFiniteElementFormulation`

## Introduction

This formulation describes isotropic linear elastic solid materials in the context of small
strains. It computes the stiffness matrix, and can also compute internal forces. When a
stress-free expansion handler is supplied, it additionally accounts for stress-free
expansions such as thermal dilation.

## Example of usage

The following include is required:

```c++
#include "manta/components-modeling/mechanics/linearized_elasticity_formulation.h"
```

It is constructed with:

```c++
    auto &elasticityForm = rm.make<LinearizedElasticityFiniteElementFormulation<tridimensional, ShapeId::hex8, Real, Real>>(
        beam, QuadId::hex8, Uvar, E, nu);
```

## Parameters

`LinearizedElasticityFiniteElementFormulation` has up to five template parameters:

- `tridimensional`, the geometric (structural) hypothesis,
- `ShapeId::hex8`, the shape ID,
- `Real`, the type of the Young's modulus evaluator: use `Real` for a uniform,
  constant value, or an evaluator type for a field- or temperature-dependent one,
- `Real`, the type of the Poisson's ratio evaluator,
- `StressFreeExpansionHandlerType` (*optional*), a handler adding stress-free
  expansion (e.g. thermal) contributions; defaults to
  `VoidStressFreeExpansionHandler` (no stress-free expansion).

`LinearizedElasticityFiniteElementFormulation` has five parameters:

- `beam`, the meshSet on which the formulation is defined,
- `QuadId::hex8`, the quadrature rule used to integrate the formulation,
- `Uvar`, the dofVar associated with the unknown (displacement),
- `E`, the Young's modulus (or its evaluator),
- `nu`, the Poisson's ratio (or its evaluator).

When the `StressFreeExpansionHandlerType` template parameter is non-void, a sixth
constructor argument holding the handler is expected.

## Description

This formulation computes the following variational operator:

\[\int_{\Omega_{r}}\left(\tepsilonto\paren{\v{u}}-\sum_{i}\tepsilon^{e}_{(i)}\right):\,\tfour{D}\,\colon\,\tepsilonto\paren{\var{\v{u}}} \d\,V\]

where:

- \(\Omega_{r}\) is the domain on which the formulation is defined, in the reference
  configuration,
- \(\v{u}\) is the displacement field and \(\var{\v{u}}\) a kinematically
  admissible virtual variation of it,
- \(\tepsilonto\) is the linearized strain:

  \[\tepsilonto\paren{\v{u}} = sym \tGradient{\v{u}} =
  \frac{1}{2}\paren{\tGradient{\v{u}}+\transpose{\tGradient{\v{u}}}},\]

  where \(\tGradient{\v{u}}\) denotes the gradient of \(\v{u}\) in the reference
  configuration,
- \(\tepsilon^{e}_{(i)}\) is a list of strains describing stress-free expansions
  (e.g. thermal dilation). This list is empty by default
  (`StressFreeExpansionHandlerType` = `VoidStressFreeExpansionHandler`), and the
  operator then reduces to pure linear elasticity,
- \(\tfour{D}\) is the elastic stiffness tensor:

  \[\tfour{D} = \lambda\,\t{I}\otimes\t{I}+2\,\mu\,\tfour{I},\]

  \(\lambda\), \(\mu\) being respectively the first and second Lamé coefficients
  (the latter is generally referred to as the shear modulus), related to the Young's
  modulus \(E\) and the Poisson's ratio \(\nu\) by

  \[\begin{split}\left\{
  \begin{aligned}
  \lambda &= \frac{\nu\,E}{\paren{1+\nu}\,\paren{1-2\,\nu}}\\
  \mu &= \frac{E}{2\,\paren{1+\nu}}\\
  \end{aligned}
  \right.\end{split}\]

When the stiffness matrix is constant and uniform (both evaluators are `Real`) it is
assembled once and kept.

## Stress-free expansion

Passing a non-void `StressFreeExpansionHandlerType` as the fifth template parameter and
its instance as the sixth constructor argument activates the \(\tepsilon^{e}_{(i)}\)
terms of the operator above.

For thermal dilation the handler is an
`IsotropicThermalExpansionComputer<MeanThermalExpansionCoefficientEvaluatorType, TemperatureEvaluatorType>`
built from a mean thermal expansion coefficient \(\alpha\), the current temperature
field \(T\) and a reference temperature \(T_{0}\), so that

\[\tepsilon^{e} = \alpha\,\paren{T-T_{0}}\,\t{I}.\]

```c++
auto thermalExpansionComputer = IsotropicThermalExpansionComputer<Real, Real>(alpha, T, T0);
auto &form = rm.make<LinearizedElasticityFiniteElementFormulation<planeStrain, ShapeId::qua4,
                                                                  Real, Real,
                                                                  decltype(thermalExpansionComputer)>>(
    cells, QuadId::qua4, Uvar, E, nu, thermalExpansionComputer);
```

The two evaluator types (`Real` above) may be replaced by field- or temperature-dependent
evaluators. Helper routines for stress-free expansions live in
`manta/components-modeling/mechanics/stress_free_expansion.h`.

## List of examples and tests

- the [2D elastic thin plate with hole commented example](../../../../demos/components_examples/elasticity/2D_elastic_thin_plate_with_hole_cpp.md#example-2d-elastic-thin-plate-with-hole-components),
- `src/components/modeling/tests/e2e/nr/implicit/linearized_elasticity` (pure elasticity)
  and `.../linearized_thermoelasticity` (with thermal dilation),
- `examples/implicit/selfWeightBeam` and the reaction verification tests.

## Notes

- This formulation derives from `BaseSolidMechanicsFiniteElementFormulation`.
- It merges the stiffness-matrix and the thermo-elastic use cases into a single class, used
  both in the components and in the frontend.
- The thermal-expansion handler is an `IsotropicThermalExpansionComputer` templated on
  the heat-transfer evaluator types
  `<MeanThermalExpansionCoefficientEvaluatorType, TemperatureEvaluatorType>`; utilities to
  build stress-free expansions are available in `stress_free_expansion.h`.
