<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_linear_capacity.html -->

# The `ImplicitHeatLinearCapacity` brick

The `ImplicitHeatLinearCapacity` brick computes the contribution to the residual
of the following variational operator:

(13)\[-\int_{\delta\,\Omega_{c}}\rho_{c}\,C_{p}\,\frac{T-\bts{T}}{\Delta\, t}\,\cdot\,\var{T} \d\,v =
-\int_{\delta\,\Omega_{r}}\rho_{r}\,C_{p}\,\frac{T-\bts{T}}{\Delta\, t}\,\cdot\,\var{T} \d\,V =\]

where:

- \(C_{v}\) is the volumic heat capacity, with \(C_{v}_{x}\) = \(rho_{x} C_{p}\).
- \(C_{p}\) is the specific heat capacity (invariant to configuration change).
- \(rho\) i the volumic mass.
- \(\bts{T}\) is the temperature at the beginning of the time step.
- \(\Delta\, t\) is the time increment.

## Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
