<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_nonlinear_convection.html -->

# The `ImplicitHeatTransferNonlinearConvection` brick

The `ImplicitHeatTransferNonlinearConvection` brick describes
a convection boundary condition where the heat transfer
coefficient depends on the temperature. It relies on
an external MFront behavior to compute the heat transfer
coefficient and its derivative with respect to the temperature.

Note

If the heat transfer coefficient does not depend on temperature,
the `ImplicitHeatTransferLinearConvection` brick can be used,
see [The ImplicitHeatLinearConvection brick](implicit_heat_transfer_linear_convection.md#implicit-heat-linear-convection-brick) for details.

## Example of usage

The following snippet adds a nonlinear convection boundary condition to
an heat transfer model:

```python
m.add('NonlinearConvection', boundary = 'left',
      library = 'src/libBehaviour.so',
      behavior = 'NonlinearHeatTransferCoefficient')
```

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

## Parameters

The following parameters are mandatory:

- `boundaries`: names of boundaries (array of regular expressions),
- `boundary`: name of a boundary (regular expression),
- `behavior`: name of MFront behavior (string)
- `library`: path to the MFront library (string)
- `hypothesis`: structural hypothesis.
  Valid values are: `PlaneStrain`,
  `PlaneStress`, `Tridimensional`, etc.

The following parameters are optional:

- `quadratureOrder`: order of quadrature. If not specified, a
- default quadrature is defined.
- `defaultTangentOperator`: default tangent operator.
  Valid values are: `Elastic`, `Secant`, `Tangent` and
  `ConsistentTangent`. If this option is not used, the
  `ConsistentTangent` value is used by default.

## About the MFront behavior

The following snippet gives a typical skeleton that can be used to
compute a nonlinear heat transfer coefficient:

```c++
@DSL DefaultGenericBehaviour{
  automatic_declaration_of_the_temperature_as_first_external_state_variable: false
};
@Behaviour NonlinearHeatTransferCoefficient;

@Gradient temperature T;
T.setGlossaryName("Temperature");

@Flux real  h;
h.setGlossaryName("HeatTransferCoefficient");

@Integrator{
  // temperature at the end of the time step
  const auto T_ets = T + dT;
  h = ...;
} // end of @Integrator

@TangentOperator {
  dh_ddT = ...;
} // end of @TangentOperator
```

Note

It its highly recommended to set the parameter
`automatic_declaration_of_the_temperature_as_first_external_state_variable`
to `false` in this case.

The previous skeleton suits most cases. However, it shall be emphasized
that one can use arbitrary complex MFront behaviors, including
behaviors introducing state variables: the user can thus use this
feature to model the degradation of the heat transfer coefficient in
time due to corrosion for instance.

## Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
