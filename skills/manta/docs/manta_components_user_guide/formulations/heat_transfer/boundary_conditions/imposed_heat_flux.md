<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/heat_transfer/boundary_conditions/imposed_heat_flux.html -->

# Imposed heat flux

This formulation allows to compute the contribution of
a flux imposed on a boundary, in the context of
heat transfer in solid materials.

## Example of usage

The following snippet shows how to create a formulation imposing a
uniform (in space) and constant (in time) heat flux on a *meshset*
named `yside`:

```c++
auto &heat_flux =
    rm.make<ImposedHeatFluxFormulation<h, ShapeId::qua4, const Real>>(
        yside, QuadId::qua4, ConfigurationTime::initial, Tvar, flux);
```

where:

- `h` is the geometric hypothesis,
- `Tvar` is the dof variable of the temperature field,
- `flux` is a floating-point number giving value of imposed the
  heat flux, assumed is thus constant and uniform in this example, as
  expressed by the third template parameter which is `const Real`.

## Parameters

The `ImposedHeatFluxFormulation` has three template parameters:

- the geometric hypothesis,
- the shape identifier,
- the evaluator type for the computation of the imposed heat flux at the
  integration points.

The main constructor of the `ImposedHeatFluxFormulation` class has four
parameters:

- the *meshset* on which the heat flux is imposed,
- the quadrature identifier,
- the configuration time,
- the temperature field,
- the heat flux evaluator.

## Description

orphan:

Imposing a heat flux is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}\phi\,\var{\v{T}} \d\,s\]

where:

- \(\delta\,\Omega_{c}\) is the boundary on which the heat flux is
  applied,
- \(\phi\) is the applied heat flux,
- \(\var{\v{T}}\) is a virtual temperature,

## Preconditions

The user is responsible to check the following pre-conditions:

- The *meshset* must only contain elements of the geometric type
  associated with the shape identifier given in the template parameters.
- The quadrature rule must be compatible with the geometric type of the
  entities of the *meshset*.
- The *meshset* must be included in the support of the
  displacement field.
- If the evaluator of the external heat flux is a reference or contains
  references to external objects, the user is responible for
  managing the lifetime of the referenced objects: those objects
  must outlive the formulation.

## Notes

The `ImposedHeatFluxFormulation` is the basis of the
`ImposedHeatFlux` brick described in Section
[The ImposedHeatFlux brick](../../../../manta_frontend_user_guide/bricks/solid_heat_transfer/imposed_heat_flux.md#imposed-heat-flux-brick).
