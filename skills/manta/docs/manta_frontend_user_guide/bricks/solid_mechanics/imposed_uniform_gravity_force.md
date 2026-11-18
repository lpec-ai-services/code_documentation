<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/imposed_uniform_gravity_force.html -->

# The `ImposedUniformGravityForce` brick

This brick considers a constant uniform force field modeling engineering-scale structures under the influence
of Earth's gravity. Other types of volumic forces could be considered with a similar brick, (*e.g.*
the influence of an electromagnetic field on a charged particle via the density of charge
and the intensity of the field).

## Example of usage

The following code adds a *ImposedUniformGravityForce*
brick to a mechanical model:

PYTHON

```python
ps.add('ImposedUniformGravityForce',
                        material = 'pellet',
                        # or equivalently: domain = 'pellet'
                        gravityPull = [0.0, 0.0, -9.81],
                        # mass density can be specified, here we use the one defined
                        # under the name MassDensity
                        massDensity = 'MassDensity',
                        # considering Earth's attraction in a usual frame
                        configuration = 'reference')
```

C++

```c++
ps->add(ctx, "ImposedUniformGravityForce",
                         Parameters{{"material", "pellet"},
                                    // or equivalently {"domain", "pellet"}
                                    {"gravityPull", {0.0, 0.0, -9.81}},
                                    // mass density can be specified, here we use the one defined
                                    // under the name MassDensity
                                    {"massDensity", "MassDensity"},
                                    // considering Earth's attraction in a usual frame
                                    {"configuration", "reference"}});
```

## Main parameters

The main parameters used to initialize the brick are:

- `domain` (which must be a string) or `domains` (which must
  be an array of strings). material or materials are also accepted
  as synonymous for domain and domains respectively. Each of those
  strings is interpreted as a regular expression.
- `gravityPull` (which must be a list of reals). This *optional* parameter initializes
  force vector describing the constant uniform field of force per unit mass. This force is multiplied to the mass density.
  If this parameter is not given, the brick uses a vector modeling Earth's attraction (if 1D then F=(-g), if 2D then F=(0,-g), if 3D then F=(0,0,-g))
  Note that the default pull in manta is \(g=9.80655\) m.s \(^{-2}\).
- `MassDensity` (which must be a string). This *optional* parameter is a string specifying the mass density that shall be considered in computations
  By default 'MassDensity' is chosen.
- `configuration` (which must be a string). This parameter gives
  the configuration on which the density and force are computed. Valid values
  are *initial`* (or equivalently *reference*,
  *Initial* or *Reference*) or *current* (or
  equivalently *Current*).
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.

## Physical description

The `ImposedUniformGravityForce` brick computes the contribution to the residual
of the following variational operator:

(9)\[-\int_{\Omega_{c}}\rho_{c}\,\cdot\,\v{g}_{c}\,\cdot\,\var{u} \d\,v =
-\int_{\Omega_{r}}J\,\rho_{c}\,\cdot\,\v{g}_{c}\,\cdot\,\var{u} \d\,V =
-\int_{\Omega_{r}}\rho_{r}\,\,\cdot\,\v{g}_{r}\,\cdot\,\var{u} \d\,V\]

where:

- \(\Omega_{c}\) denotes the current configuration.
- \(\Omega_{r}\) denotes the reference configuration.
- \(J\) is the determinant of the gradient of the transformation (the jacobian of the transformation).
- \(\rho_{c}\) is mass density in the current configuration.
- \(\rho_{r}\) is mass density in the reference configuration.
- \(\v{g}\) is a vector describing the intensity and direction of the force per unit of mass.

Warning

As explained in Section [The HeatSource brick](../solid_heat_transfer/implicit_heat_transfer_heat_source.md#implicit-heat-transfer-heat-source-brick), Equation
[(9)](#equation-manta-user-guide-gravity-force-operator) highlights the fact
that the user must be cautious on the definition of the mass density, as it can be expressed
in two different configurations. The configuration onto which everything is defined and computed is thus a parameter of the brick.
See the referenced section for more details.

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

- [The ExplicitMechanics model](../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
- [The ImplicitMechanics model](../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
