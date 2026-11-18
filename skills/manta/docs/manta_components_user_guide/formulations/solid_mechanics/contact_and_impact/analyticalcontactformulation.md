<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/contact_and_impact/analyticalcontactformulation.html -->

# AnalyticalContactFormulation

## Introduction

This formulation implements analytical contact in
an explicit dynamic context.

## Example of usage

The following includes are required to use this formulation

```c++
#include "manta/components-modeling/finite_elements/analytical_contact.h"
#include "manta/components-modeling/time_integrators/central_difference_with_contact.h"
```

It can be constructed with:

```c++
    auto &contactForm = rm.make<AnalyticalContactFormulation>(Gvar, roll, contact, V);
```

## Parameters

auto &contactForm = rm.make<AnalyticalContactFormulation>(Gvar, roll, contact, V);

`AnalyticalContactFormulation` has four parameters:

- `Gvar`, the dof variable of the acceleration field,
- `roll`, a function returning `true` when points are in contact,
- `contact`, is the slave surface `MeshSet`,
- `V`, the predicted velocity field.

The `analyticalSurface` (here `roll`), *i.e.* the master surface defined as a function returning
`true` when the slave point of coordinate `xs` is in contact and
returning `false` otherwise. This function should also fill in the
contact normal `nm` and the master surface speed `vm`. Here is an example
of the definition of this surface. Another example might be fetched in the documentation
of the `ImplicitAnalyticalContactFormulation`.

```c++
    RowVector<2> oRoll;
    oRoll << std::sqrt(2. * e * R - e * e), Ly + R - e;
    auto roll = [&](ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm, RowVectorRef<3> vm) {
      RowVector<2> D = head<2>(xs) - oRoll;
      Real d         = norm(D);

      if (d < R) {
        head<2>(xm) = oRoll + D / d * R;
        xm(2)       = xs(2);
        head<2>(nm) = D / d;
        nm(2)       = 0.;
        setZero(vm);
        return true;
      }
      else {
        return false;
      }
    };
```

The `ConstraintSet` shall be instanciated and associated to the main `LinearSystem` as follows:

```c++
    auto &contactCSet = rm.make<ConstraintSet>(feSystem, "contact");
    contactCSet.asPrimitive(V, Gvar, dt);
    rm.assignFormulationToLinearSystem(contactForm, contactCSet);
```

Finally note that in an explicit context, it is usually mandatory to use a `TimeIntegrator`.
For this specific contact application one can use the `CentralDifferenceWContactTimeIntegrator`
as documented in [in this page about time integrators](../../../algorithms_and_numerics/time_integrators/time_integrators.md#time-integrators).

Here is an example of the instanciation of such a `TimeIntegrator`

```c++
    CentralDifferenceWContactTimeIntegrator timeIntegrator(feSystem, {U, V, G}, Gvar, {contactCSet});
```

## List of commented examples and verification tests

Test case location

The test case can be found at:

[<MANTA REPO>/src/components/modeling/tests/e2e/nr/rolling/](https://gitlab.com/manta-project/manta/-/tree/master/src/components/modeling/tests/e2e/nr/rolling/)

- Note also its usage in the following [commented example of a Charpy test](../../../../demos/components_examples/contact_and_impact/charpy.md#example-3d-charpy)

## Notes

Several formulations aim at modeling contact, and contact with friction,
in an explicit or implicit context such as:

- [ImplicitAnalyticalContactFormulation](implicitanalyticalcontactformulation.md#implicit-analytical-contact-friction)
- [AnalyticalContactFrictionFormulation](analytical_contact_friction.md#analytical-contact-friction)
