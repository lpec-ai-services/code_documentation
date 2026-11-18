<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/contact_and_impact/analytical_contact_friction.html -->

# AnalyticalContactFrictionFormulation

## Introduction

This formulation implements friction for analytical contact in
an explicit dynamic context.

## Example of usage

The following includes are required to use this formulation

```c++
#include "manta/components-core/core.h"
#include "manta/components-core/linear_system/constraint_set.h"

#include "manta/components-modeling/friction/coulomb_friction.h"
#include "manta/components-modeling/finite_elements/analytical_contact_friction.h"
```

It can be constructed with:

```c++
  auto &formFriction =
      rm.make<AnalyticalContactFrictionFormulation<dim>>(Gvar, analyticalSurface, bottom, V, frictionModel);
```

## Parameters

`AnalyticalContactFrictionFormulation` has one template parameter:

- `dim`, the dimension of the problem,

It calibrates the dimension of all vectors
throughout the internal workings of the formulation.

`AnalyticalContactFrictionFormulation` has five parameters:

- `Gvar`, the dof variable of the acceleration field,
- `analyticalSurface`, a function returning `true` when points are in contact,
- `bottom`, is the slave surface `MeshSet`,
- `V`, the predicted velocity field,
- `frictionModel` , is the friction model, used to compute the friction forces and the determine sliding/sticking.

The following snippet shows how to create the friction model

```c++
  CoulombFriction<dim> frictionModel(system, Gvar, bottom, {contactCSet}, mu_s, mu_d);
```

with the following parameters:

- `system`, the `LinearSystem` solving for `G`,
- `bottom`, the slave `MeshSet`,
- `contactCSet`, the `ConstraintSet` linked with the formulation,
- `mu_s` and `mu_d` are the static and dynamic friction coefficient
  of the Coulomb friction model

The `ConstraintSet` shall be instanciated as follows:

```c++
  ConstraintSet &contactCSet = rm.make<ConstraintSet>(system, "ContactSurface");
```

The `analyticalSurface`, *i.e.* is the master surface defined as a function returning
`true` when the slave point of coordinate `xs` is in contact and
returning `false` otherwise. This function should also fill in the
contact normal `nm` and the master surface speed `vm`.

```c++
  auto analyticalSurface = [&](ConstRowVectorRef<dim> xs, RowVectorRef<dim> nm, RowVectorRef<dim> vm) {
    return false;
  };
```

Other examples of the definition of such a surface can be found in the documentation, tests, and examples related
to the other contact `Formulation`.

Then, two more steps are nescessary to use the formulation, as shown in the following snippet

```c++
  contactCSet.asPrimitive(V, Gvar, dt);
  rm.assignFormulationToLinearSystem(formFriction, contactCSet);
```

Finally note that in an explicit context, it is usually mandatory to use a `TimeIntegrator`.
For this specific contact with friction application one can use the `CentralDifferenceWFrictionTimeIntegrator`
as documented in [in this page about time integrators](../../../algorithms_and_numerics/time_integrators/time_integrators.md#time-integrators).

## Description

The formulation consists in writing a \(\m{C}\) matrix and the corresponding
\(\v{D}\) vector. In dynamic, it is mandatory to use a constraint set with
the option `asPrimitive` in order to write \(\v{D}\) as imposed speed
instead of imposed acceleration.

The friction model is used to determine if a slave node is in a state of
*sliding* or *sticking*

### Coulomb model

Coulomb model is implemented within the `CoulombFriction` class.
Within the scope of this model, when in contact, a point is described
by a friction state. The point is either *sticking* to the master
surface or *sliding* against the master surface.

- In sticking state

  - Apply sitcking to the master surface by enforcing all DOFs in the
    \(\m{C}\) matrix to the speed of the master surface
  - If \(\norm{\v{F}_T} > \mu_s \norm{\v{F}_N}\)
    then state should change to sliding

    - Because sticking is enforced through a kinematic constraint,
      both the normal force \(\v{F}_N\) and the tangential
      force \(\v{F}_T\) are known as the constraint reaction
- In sliding state

  - Apply sliding forces in the main *RHS* as
    \(\v{F}_T = - \mu_d * \norm{\v{F}_N} * \frac{\v{v}_T}{\norm{\v{v}}}\)

    - Because the normale DOF is enforced through a kinematic constraint,
      the normal force \(\v{F}_N\) is known as the constraint reaction
    - The direction of the tangential force is known as the direction of the
      tangential speed
  - If the speed changes sign (becomes zero) in the tangent direction,
    state should change to sticking

The above points are illustrated on the figure below where the tangential force
is plotted against the tangential speed (\(\v{v}_{lim}\) is a normalizing term).

![Figure: Coulomb model](https://manta-project.gitlab.io/manta/_images/CoulombFriction.svg)

## Notes

Several formulations aim at modeling contact, and contact with friction,
in an explicit or implicit context such as:

- [AnalyticalContactFormulation](analyticalcontactformulation.md#analytical-contact)
- [ImplicitAnalyticalContactFormulation](implicitanalyticalcontactformulation.md#implicit-analytical-contact-friction)
