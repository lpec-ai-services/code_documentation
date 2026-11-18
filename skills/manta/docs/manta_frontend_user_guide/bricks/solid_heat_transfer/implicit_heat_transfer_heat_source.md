<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_heat_transfer/implicit_heat_transfer_heat_source.html -->

# The `HeatSource` brick

## Example of usage

The following code adds a *HeatSource*
brick to a mechanical model:

PYTHON

```python
heat_transfer_model.add('HeatSource',
                        material = 'pellet',
                        # or equivalently: domain = 'pellet'
                        value = 'PowerDensity',
                        configuration = 'reference')
```

C++

```c++
heat_transfer_model->add(ctx, "HeatSource",
                         Parameters{{"material", "pellet"},
                                    // or equivalently {"domain", "pellet"}
                                    {"value", "PowerDensity"},
                                    {"configuration", "reference"});
```

## Main parameters

The main parameters used to initialize the brick are:

- `domain` (which must be a string) or `domains` (which must
  be an array of strings). material or materials are also accepted
  as synonymous for domain and domains respectively. Each of those
  strings is interpreted as a regular expression.
- `value` (which must be a string). This parameter gives the name
  of the heat source per unit of volume in the configuration given by
  the `configuration` parameter.
- `configuration` (which must be a string). This parameter gives
  the configuration on which the heat source is computed. Valid values
  are :jarg:'initial' (or equivalently *reference*,
  *Initial* or *Reference*) or *current* (or
  equivalently *Current*).
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.

## Description

The *HeatSource* brick` computes the contribution to the residual
of the following variational operator:

(11)\[-\int_{\Omega_{c}}q_{c}\,\cdot\,\var{T} \d\,v =
-\int_{\Omega_{r}}J\,q_{c}\,\cdot\,\var{T} \d\,V =
-\int_{\Omega_{r}}q_{r}\,\cdot\,\var{T} \d\,V\]

where:

- \(\Omega_{c}\) denotes the current configuration.
- \(\Omega_{r}\) denotes the reference configuration.
- \(J\) is the determinant of the gradient of the transformation (the jacobian of the transformation).
- \(q_{c}\) is the heat source per unit of volume in the current configuration.
- \(q_{r}\) is the heat source per unit of volume in the reference configuration.

Warning

Equation [(11)](#equation-manta-user-guide-heat-source-operator) highlights the fact
that user must be cautious on the definition of the heat source used. In
particular, the heat source can be expressed by unit of volume in the
reference configuration (\(q_{r}\)) or by unit of volume in the
current configuration (\(q_{c}\)).

In most cases, the heat source is defined by loading whose value is known
in the *reference* configuration.

When the heat source is a plastic dissipation term, the user must carefully
take into account on which configuration this plastic dissipation is
defined. If a lagrangian framework is used, the plastic dissipation
is probably defined in the reference configuration. If the plastic
dissipation is naturally computed in an intermediate configuration,
the mechanical behaviour must take care of transporting this dissipation
any of the reference or the current configuration.

To emphasise the fact that the user is responsible for ensuring
the consistency of the definition of the heat source, the
`configuration` parameter described below is always required.

The minus sign in Equation [(11)](#equation-manta-user-guide-heat-source-operator)
comes from the arbitrary convention defining the residual as the difference
bewteen internal heat flux and external heat flux.

Note

The *HeatSource* brick delegates the computation of the heat
flux to the `NonlinearHeatSourceFormulation` class. This class
can be used directly by advanced users. A class named
`LinearHeatSourceFormulation` is also available but computes
the opposite of Equation
[(11)](#equation-manta-user-guide-heat-source-operator).

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *tet4*, *tet10*, *hex8*, *hex20*, *pyr5* |
| *PlaneStrain* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *PlaneStress* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *Axisymmetrical* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |

## Compatible models

This brick is compatible with the following models:

- [Implicit heat transfer](../../models/solid_heat_transfer/implicit_heat_transfer.md#implicit-heat-transfer-model)
