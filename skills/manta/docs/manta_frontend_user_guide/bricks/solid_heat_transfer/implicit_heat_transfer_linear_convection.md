<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_linear_convection.html -->

# The `ImplicitHeatLinearConvection` brick

The `ImplicitHeatLinearConvection` brick computes the contribution to the residual
of the following variational operator:

(12)\[-\int_{\delta\,\Omega_{h}}h\,\cdot\,\paren{T-T_{\infty}}\,\cdot\,\var{T} \d\,s\]

where:

- \(h\) is the heat transfer coefficient.
- \(T_{\infty}\) is the temperature at infinity.

Note

Linear refers to the fact that this formulation can be adapted
to be usable in linear resolutions. This adaptation ought
to be done in future versions.
This implies that the heat transfer coefficient shall not
depend on the temperature.

If the heat transfer coefficient depends on the temperature, this
formulation can still be used in nonlinear resolutions, but
convergence of implicit resolutions may be degraded.

To avoid this issue, the `ImplicitHeatTransferNonlinearConvection` brick
can be used.

## Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
