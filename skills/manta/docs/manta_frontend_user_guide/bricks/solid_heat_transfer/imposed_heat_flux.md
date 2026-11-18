<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/imposed_heat_flux.html -->

# The `ImposedHeatFlux` brick

The `ImposedHeatFluxBrick` brick computes the contribution
to the residual of an imposed heat flux.

## Example of usage

The following code adds the an *ImposedHeatFlux*
brick to a mechanical model:

```c++
mechanics_model->add(
    ctx, "ImposedHeatFlux",
    Parameters{{"boundary", "left"},
               {"value", "ImposedHeatFluxValue"}});
```

### Main parameters

The main parameters used to initialize the brick are:

- `boundary` (which must be a string) or `boundaries` (which must
  be an array of strings). Each of those strings are interpreted as
  regular expressions.
- `value` (which must be a string). This parameter gives the name
  of the loading providing the evolution of the heat flux.
- `configurationTime`. This
  parameter is *optional* and by default, the default value is initial.
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.

## Description

orphan:

Imposing a heat flux is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}\phi\,\var{\v{T}} \d\,s\]

where:

- \(\delta\,\Omega_{c}\) is the boundary on which the heat flux is
  applied,
- \(\phi\) is the applied heat flux,
- \(\var{\v{T}}\) is a virtual temperature,

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *Axisymmetrical* | *seg2*, *seg3* |
| *PlaneStrain* | *seg2*, *seg3* |
| *PlaneStress* | *seg2*, *seg3* |

## Notes

The `ImposedHeatFlux` brick is based on the
`ImposedHeatFluxFormulation` described in Section
[Imposed heat flux](../../../manta_components_user_guide/formulations/heat_transfer/boundary_conditions/imposed_heat_flux.md#imposed-heat-flux-formulation).

## Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
