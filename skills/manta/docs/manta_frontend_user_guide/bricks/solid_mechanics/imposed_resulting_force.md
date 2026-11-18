<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/imposed_resulting_force.html -->

# The `ImposedResultingForce` brick

This brick applies a resulting force on the prescribed boundary.

## Examples of usage

The following code adds a *ImposedResultingForce*
brick to a mechanical model:

```python
m = manta.Model(...)
m.add('ImposedResultingForce', boundary='right', force=[1,0,0])
```

A complete example can be found in the
[verification tests](../../../verification_tests/manta_frontend_verification_tests/solid_mechanics/fem_implicit_linear/tridimensional/isotropic_elasticity/isotropic_elastic.md#verification-solidmechanics-isotropic-elasticity).

The following code adds a time-dependent *ImposedResultingForce*
brick to a mechanical model:

```python
m = manta.Model(...)
ps.addLoadingEvolution('LOAD_Y', lambda t: -100.0 * t)
m.add('ImposedResultingForce', boundary='right', force=[0, 'LOAD_Y', 0])
```

## Main parameters

The main parameters used to initialize the brick are:

- `boundary` on which the resulting force shall be applied
- `force` to give an amplitude and direction to the resulting force. Must be a vector of the
  same dimension as the `domain`, containing floating-point numbers or names of time-dependent evolutions via `addLoadingEvolution`.

## Physical description

The *ImposedResultingForce* implements the following boundary
condition:

\[\int_{\partial \Omega} \m{\sigma} \cdot \v{e}_n \ \mathrm{d}S = \v{F}\]

with \(\v{F}\) the applied resulting force and \(\v{e}_n\) the
outward normal to boundary \(\partial \Omega\).

In practice, such boundary condition is enforced through a uniform nodal force
on each node of the boundary:

\[\v{F}_N = \frac{\v{F}}{N}\]

with \(N\) the total number of
nodes constituting the discretization of the boundary.

## Compatible models

This brick is compatible with the following models:

- [The ExplicitMechanics model](../../models/solid_mechanics/explicit_solid_mechanics.md#explicit-mechanics-model)
- [The ImplicitMechanics model](../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
