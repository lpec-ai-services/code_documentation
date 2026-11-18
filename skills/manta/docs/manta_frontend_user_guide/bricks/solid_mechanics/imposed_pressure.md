<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/imposed_pressure.html -->

# The `ImposedPressure` brick

The `ImposedPressureBrick` brick computes the contribution
to the residual of an imposed pressure.

## Example of usage

The following code adds the an *ImposedPressure*
brick to a mechanical model:

```c++
mechanics_model->add(
    ctx, "ImposedPressure",
    Parameters{{"boundary", "left"},
               {"value", "ImposedPressureValue"}});
```

### Main parameters

The main parameters used to initialize the brick are:

- `boundary` (which must be a string) or `boundaries` (which must
  be an array of strings). Each of those strings are interpreted as
  regular expressions.
- `value` (which must be a string). This parameter gives the name
  of the loading providing the evolution of the pressure.
- `assumeInfinitesimalPerturbation`, which must be a boolean. If
  this boolean is false, the first (general) variational operator is
  used. If true, the second variational operator is used. This
  parameter is *optional* and by default, the default value is false.
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.

## Description

Imposing a pressure is associated with the following variational operator:

\[-\int_{\delta\,\Omega_{c}}p\,\var{\v{u}}\,\cdot\,\v{n} \d\,s\]

where:

- \(\delta\,\Omega_{c}\) is the boundary in the current
  configuration on which the pressure is applied,
- \(p\) is the applied pressure (positive in compression, negative
  for a compression),
- \(\var{\v{u}}\) is virtual displacement,
- \(\v{n}\) is the outer normal to \(\delta\,\Omega_{c}\).

Under the infinitesimal pertubation hypothesis, imposing a pressure is
associated with the following variational operator:

\[-\int_{\delta\,\Omega_{r}}p\,\var{\v{u}}\,\cdot\,\v{N} \d\,S\]

where:

- \(\delta\,\Omega_{r}\) is the boundary in the reference
  configuration on which the pressure is applied,
- \(\v{N}\) is the outer normal to \(\delta\,\Omega_{r}\).

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

The `ImposedPressure` brick is based on the
`ImposedPressureFormulation` described in Section
[Imposed pressure](../../../manta_components_user_guide/formulations/constraints_and_bcs/imposed_pressure.md#imposed-pressure-formulation).

## Compatible models

This brick is compatible with the following models:

- [The ExplicitMechanics model](../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
- [The ImplicitMechanics model](../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
