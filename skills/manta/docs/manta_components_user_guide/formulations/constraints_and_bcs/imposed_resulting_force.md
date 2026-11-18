<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/imposed_resulting_force.html -->

# Imposed resulting force

## Example of usage

```c++
constexpr Int dim = 3; // 3D
ColVector<dim> F;  // RowVector<dim> may also work
auto &formulation = rm.make<ImposedResultingForceFormulation<dim>>(Uvar, F, meshSet);
```

where:

- `Uvar` is the dof variable of the displacement field
- `F` is vector of the resulting force
- `meshSet` is the a meshSet representing the boundary

## Parameters

`ImposedResultingForceFormulation` has only two template parameters which are
the dimension of the problem (and as such the dimension of the applied force) and
the evaluator type (`const Real &` by default)

The given resulting force is passed by reference to the formulation. This offers
a convenient way to change the loading values throughout the simulation.

## Description

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

## Notes

- The `ImposedResultingForceFormulation` is tested through the MANTA
  front-end within the
  [verification tests](../../../verification_tests/manta_frontend_verification_tests/solid_mechanics/fem_implicit_linear/tridimensional/isotropic_elasticity/isotropic_elastic.md#verification-solidmechanics-isotropic-elasticity).
- The uniform nodal forces are computed in the `assemble` entry point
