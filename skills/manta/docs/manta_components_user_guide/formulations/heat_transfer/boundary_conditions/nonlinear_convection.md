<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/heat_transfer/boundary_conditions/nonlinear_convection.html -->

# Non linear convection formulation

This formulation calculates the contribution of a convection boundary
condition.

Note

If the heat transfer coefficient is assumed to depend on the temperature.
Its evaluation and the evaluation of its derivative with respect
to the temperature is delegated to an external behaviour.

If the heat transfer coefficient does not depend on the temperature,
the linear convection formulation can be used,
see [Linear convection formulation](linear_convection.md#linear-convection-formulation) for details.

## Example of usage

The following example creates a nonlinear convection formulation:

```c++
auto &convectionFormulation =
     rm.make<ImplicitHeatTransferNonlinearConvectionFormulation<h, ShapeId::qua8, MFrontBehavior, Real>>(
        b, QuadId::qua9, T, Tvar, bh, Tinf);
```

where:

- `h` is the geometric hypothesis,
- `b` is the boundary on which the formulation acts,
- `T` is the temperature field, `Tvar` its dof variable,
- `bh` is the behaviour used to calculate
  the heat transfer coefficient and its derivative with
  respect to the temperature,
- `Tinf` is the value of the temperature at infini.

## Parameters

The class `ImplicitHeatTransferNonlinearConvectionFormulation` has
the following template parameters:

- `h`: geometric hypothesis,
- `sid`: identifier of the shape functions,
- `BehaviorType`: type of the behaviour used to calculate
  the heat transfer coefficient
  and its derivative with respect to the temperature,
- `TemperatureAtInfinityEvaluatorType`: evaluator of the temperature at infinity.

The constructor of the
`ImplicitHeatTransferNonlinearConvectionFormulation` class takes the
following arguments:

- the *meshset* of the boundary on which the formulation acts,
- the quadrature used,
- the temperature field,
- the behaviour used to calculate the heat transfer coefficient
  and its derivative with respect to the temperature,
- the evaluator of the temperature at infinity.

## Description

Imposing a convection boundary condition is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}h\left(T\right)\,\cdot\,\left(T-T_{\infty}\right)\,\cdot\,\var{\v{T}} \d\,s\]

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
- If the behavior is a reference or contains references to external objects,
  the user is responsible for managing the lifetime of the referenced objects:
  those objects must outlive the formulation.
- If the evaluator used to evaluate the temperature at infinity is a reference
  or contains references to external objects, the user is responible for
  managing the lifetime of the referenced objects: those objects
  must outlive the formulation.

## Notes

The `ImplicitHeatTransferNonlinearConvectionFormulation` is the basis of the
`NonlinearConvection` brick described in Section
[The ImplicitHeatTransferNonlinearConvection brick](../../../../manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_nonlinear_convection.md#implicit-heat-transfer-nonlinear-convection-brick).
