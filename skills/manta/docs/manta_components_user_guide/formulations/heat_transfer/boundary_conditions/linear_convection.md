<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/heat_transfer/boundary_conditions/linear_convection.html -->

# Linear convection formulation

This formulation calculates the contribution of a convection boundary
condition.

Note

Linear refers to the fact that this formulation can be adapted
to be usable in linear resolutions. This adaptation ought
to be done in future versions. This implies that
the heat transfer coefficient shall not depend on the temperature

If the heat transfer coefficient depends on the temperature, this
formulation can still be used in nonlinear resolutions, but
convergence of implicit resolutions may be degraded.

To avoid this issue, the nonlinear convection formulation can be
used, see [Non linear convection formulation](nonlinear_convection.md#nonlinear-convection-formulation).

## Example of usage

The following example creates a linear convection formulation:

```c++
auto &convectionFormulation =
     rm.make<ImplicitHeatTransferLinearConvectionFormulation<h, ShapeId::qua8, Real, Real>>(
        b, QuadId::qua9, T, Tvar, hv, Tinf);
```

where:

- `h` is the geometric hypothesis,
- `b` is the boundary on which the formulation acts,
- `T` is the temperature field, `Tvar` its dof variable,
- `hv` is the value of the heat transfer coefficient,
- `Tinf` is the value of the temperature at infini.

## Parameters

The class `ImplicitHeatTransferLinearConvectionFormulation` has
the following template parameters:

- `h`: geometric hypothesis,
- `sid`: identifier of the shape functions,
- `HeatTransferCoefficientEvaluatorType`: type of the evaluator of the heat transfer coefficient,
- `TemperatureAtInfinityEvaluatorType`: evaluator of the temperature at infinity.

The constructor of the
`ImplicitHeatTransferLinearConvectionFormulation` class takes the
following arguments:

- the *meshset* of the boundary on which the formulation acts,
- the quadrature used,
- the temperature field,
- the evaluator of the heat transfer coefficient,
- the evaluator of the temperature at infinity.

## Description

Imposing a convection boundary condition is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}h\,\cdot\,\left(T-T_{\infty}\right)\,\cdot\,\var{\v{T}} \d\,s\]

where:

- \(\delta\,\Omega_{c}\) is the boundary on which the convection is
  applied,
- \(h\) is the heat transfer coefficient,
- \(T\) is the temperature,
- \(T_{\infty}\) is the temperature at infinity,
- \(\var{\v{T}}\) is a virtual temperature,

## Preconditions

The user is responsible to check the following pre-conditions:

- The *meshset* must only contain elements of the geometric type
  associated with the shape identifier given in the template parameters.
- The quadrature rule must be compatible with the geometric type of the
  entities of the *meshset*.
- The *meshset* must be included in the support of the
  temperature field.
- If the evaluators used are references or contains
  references to external objects, the user is responsible for
  managing the lifetime of the referenced objects: those objects
  must outlive the formulation.

## Notes

The `ImplicitHeatTransferLinearConvectionFormulation` is the basis of the
`LinearConvection` brick described in Section
[The ImplicitHeatLinearConvection brick](../../../../manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_linear_convection.md#implicit-heat-linear-convection-brick).
