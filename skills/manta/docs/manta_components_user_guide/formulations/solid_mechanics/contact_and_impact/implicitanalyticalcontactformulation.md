<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/contact_and_impact/implicitanalyticalcontactformulation.html -->

# ImplicitAnalyticalContactFormulation

## Introduction

This formulation implements analytical contact for an implicit problem (static or implicit time-integration)

## Example of usage

The following includes are required to use this formulation

```c++
#include "manta/components-modeling/finite_elements/analytical_contact.h"
#include "manta/components-core/linear_system/constraint_set.h"
```

It can be constructed with:

```c++
  auto &contactFormStriker = rm.make<ImplicitAnalyticalContactFormulation>(Uvar, analyticalContactFuncStriker, cubeUp, R);
```

## Parameters

> auto &contactFormStriker =
> :   rm.make<ImplicitAnalyticalContactFormulation>(Uvar, analyticalContactFuncStriker, cubeUp, R);

`ImplicitAnalyticalContactFormulation` has four parameters:

- `Uvar`, the dof variable of the displacement field,
- `analyticalContactFuncStriker`, a function returning `true` when points are in contact,
- `cubeUp`, is the slave surface `MeshSet`,
- `R`, the field linked to the constraint,

The `analyticalContactFuncStriker`, listed in this example, is the master surface defined as a function returning
`true` when the slave point of coordinate `xs` is in contact and
returning `false` otherwise. This function should also fill in the
contact normal `nm` and the master surface speed `vm`. Here is an example of the filling of this lambda functor.

```c++
  auto analyticalContactFuncStriker = [&](bool isAtSurface, ConstRowVectorRef<3> xs, RowVectorRef<3> xm, RowVectorRef<3> nm) {
    const Real r = .5;
    RowVector<3> o;
    o << .5, .5, 1. + r;

    RowVector<3> D = xs - o;
    Real d         = norm(D);

    if (isAtSurface) {
      xm = xs;
      nm = D / d;
      return false;
    }
    else {
      if (d < r) {
        xm = o + D / d * r;
        nm = D / d;
        return true;
      }
      else {
        return false;
      }
    }
  };
```

Finally, two more steps are nescessary to use the formulation, as shown in the following snippet,
definition of the `ConstraintSet` and assignement to the main `LinearSystem`.

```c++
  auto &contactCSetStriker = rm.make<ConstraintSet>(feSystem, "contactCubeStriker");
  rm.assignFormulationToLinearSystem(contactFormStriker, contactCSetStriker);
```

## Description

## List of commented examples and verification tests

- Component verification test: nr/implicit/cube_analytical_contact

Test case location

The test case can be found at:

[<MANTA REPO>/src/components/modeling/tests/e2e/nr/implicit/cube_analytical_contact/](https://gitlab.com/manta-project/manta/-/tree/master/src/components/modeling/tests/e2e/nr/implicit/cube_analytical_contact/)

## Notes

Several formulations aim at modeling contact, and contact with friction,
in an explicit or implicit context such as:

- [AnalyticalContactFormulation](analyticalcontactformulation.md#analytical-contact)
- [AnalyticalContactFrictionFormulation](analytical_contact_friction.md#analytical-contact-friction)
