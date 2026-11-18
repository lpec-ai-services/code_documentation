<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/imposed_uniform_gravity_force_form.html -->

# ImposedUniformGravityForceFormulation

## Introduction

This formulation computed the contribution of a constant uniform force field.
This can, for instance, be used for the modeling of engineering-scale structures
under the influence of Earth's gravity. It is built upon the generalized
`ImposedBodyForceFormulation`, but imposes that the force field be uniform.
It is therefore defined as a vector, whose direction and intensity can be specified.

## Example of usage

The following include is required:

```c++
#include "manta/components-modeling/mechanics/imposed_uniform_gravity_force_formulation.h"
```

It can be constructed with:

```c++
    RowVector<dim> f;
    f << 0., 0., -g;
    auto &selfweightForm = rm.make<ImposedUniformGravityForceFormulation<h, cellShapeId, Real>>(
        beam, cellQuadId, ConfigurationTime::initial, Uvar, rho, f);
```

## Parameters

`ImposedUniformGravityForceFormulation` has three template parameters:

- `h`, The geometric hypothesis
- `cellShapeId`, The shape ID
- `Real`, type of the mass density (in the example a `Real`)

`ImposedUniformGravityForceFormulation` has five parameters:

- `beam`, the meshSet onto which the formulation is defined
- `cellQuadId`, the quadrature used to integrate the formulation
- `ConfigurationTime`, the configuration time
- `Uvar`, the dof variable linked to the primal
- `rho`, the mass density which has the type defined by the template parameter
- `f`, the force per unit of mass defined as a `RowVector<dim>` (*optional parameter*).

If no `f`, *i.e* no force per unit of mass, is specified, the uniform gravity field will be directed toward the opposite of the last dimension
(-x in 1D, -y in 2D, -z in 3D) with an amplitude of \(g\), Earth's gravity field acceleration, which defaults to \(g=9.80655\) m.s \(^{-2}\) in manta.

## Description

The `ImposedUniformGravityForce` brick computes the contribution to the residual
of the following variational operator:

(24)\[-\int_{\Omega_{c}}\rho_{c}\,\cdot\,\v{g}_{c}\,\cdot\,\var{u} \d\,v =
-\int_{\Omega_{r}}J\,\rho_{c}\,\cdot\,\v{g}_{c}\,\cdot\,\var{u} \d\,V =
-\int_{\Omega_{r}}\rho_{r}\,\,\cdot\,\v{g}_{r}\,\cdot\,\var{u} \d\,V\]

where:

- \(\Omega_{c}\) denotes the current configuration.
- \(\Omega_{r}\) denotes the reference configuration.
- \(J\) is the determinant of the gradient of the transformation (the jacobian of the transformation).
- \(\rho_{c}\) is mass density in the current configuration.
- \(\rho_{r}\) is mass density in the reference configuration.
- \(\v{g}\) is a vector describing the intensity and direction of the force per unit of mass.

## List of commented examples and verification tests

- Component verification test: in components/modeling.

## Notes

This formulation is built upon the `ImposedBodyForceFormulation` which can be used to create any other
body forces formulation.

In this formulation we defined the body force (per unit of volume), expected by the `ImposedBodyForceFormulation`,
as the force per unit of mass (the gravity constant), multiplied by the mass density. This is defined in
the `ImposedUniformGravityForce`. The definition of such a class is mandatory to derive from the
`ImposedBodyForceFormulation`, as the force per unit of volume is the last parameter of this class: the
`BodyForceEvaluator`.
