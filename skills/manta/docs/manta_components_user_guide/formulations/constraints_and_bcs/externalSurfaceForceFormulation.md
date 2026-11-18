<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/externalSurfaceForceFormulation.html -->

# ExternalSurfaceForceFormulation

## Introduction

This formulation expresses the Neumann's type boundary condition of a force applied on a surface,
in the context of solid mechanics, in a finite element framework.
It is defined using a force vector, and a normal to the surface that is being loaded.

## Example of usage

The following include is required:

```c++
#include "manta/components-modeling/finite_elements/external_surface_force.h"
```

It can be constructed with:

```c++
  auto &extForceForm_concrete = rm.make<ExternalSurfaceForceFormulation<dim, faceShapeId>>(
      right_concrete, faceQuadId, U_concreteVar, pullForce, normalToFirstTangentVector);
```

## Parameters

`ExternalSurfaceForceFormulation` has two template parameters:

- `dim`, the dimension of the problem,
- `faceShapeId`, The shape ID of the face being loaded.

`ExternalSurfaceForceFormulation` has six parameters:

- `right_concrete`, the meshSet onto which the formulation is defined,
- `faceQuadId`, the quadrature used to integrate the formulation,
- `U_concreteVar`, the dof variable linked to the primal,
- `pullForce` , the force expressed as a vector of dimension `dim`,
- `normalToFirstTangentVector`, a vector normal to the first tangent vector of the local frame (3D only).

In the following snippet, we give an example of how to instanciate those last two parameters

```c++
  ColVector<dim> pullForce;
  pullForce << pConcrete, -pConcrete, -pConcrete;
  RowVector<dim> normalToFirstTangentVector;
  normalToFirstTangentVector << 0., 1., 0.;
```

## Description

This formulation enables the computation of the contribution to the residual of
an external surface force applied on a given boundary,
expressed in a local frame of reference (*i.e.*, in the frame of the loaded face in 3D
and edge in 2D).

The inputted force vector is a surfacic force, that is expressed in the current frame of reference.
The current configuration is always assumed in this formulation.

As this formulation is expressed in a local frame, it is nescessary to define its orientation.
In 2D this frame is trivial to define: take the normal to the loaded edge and deduce the tangential
component.
In 3D there is a need to define the first tangent vector to define uniquely this local frame of
reference. For ease of use, users may provide the normal to the first tangent vector (*i.e* any
vector which is normal to the direction that will be used as the first component of the local frame,
and not colinear to the normal to the loaded plane).

## List of commented examples and verification tests

- Component verification test: in steel_concrete_link

Test case location

The test case can be found at:

[<MANTA REPO>/src/components/modeling/tests/e2e/nr/steel_concrete_link/elasticity3d_timoshenko/](https://gitlab.com/manta-project/manta/-/tree/master/src/components/modeling/tests/e2e/nr/steel_concrete_link/elasticity3d_timoshenko/)

## Notes

Several formulations enable to apply such a Neumann condition in the context of solid mechanics.
Those formulations give the choice to users to define their surface force differently,
*e.g*, the [ImposedPressureFormulation](imposed_pressure.md#imposed-pressure-formulation)
or [ImposedNodalForceFormulation](imposed_nodal_forces.md#imposed-nodal-forces-formulation).

The [ImposedPressureFormulation](imposed_pressure.md#imposed-pressure-formulation), is very close to the
presently described formulation: instead of an oriented surfacic force, the user may define a scalar value,
the pressure, which is then applied in the normal direction of the loaded surface.
It can be thought of as the `ExternalSurfaceForceFormulation` where only the first component is non null.

The [ImposedNodalForceFormulation](imposed_nodal_forces.md#imposed-nodal-forces-formulation), simply adds the contribution
of a force to the left-hand side. Contrarily to the presently described formulation,
the [ImposedNodalForceFormulation](imposed_nodal_forces.md#imposed-nodal-forces-formulation) defines a force, and not a
surfacic force. Note also [ImposedResultingForceFormulation](imposed_resulting_force.md#imposed-resulting-force-formulation),
where the inputted force is simply spread across the nodes of a given surface.
