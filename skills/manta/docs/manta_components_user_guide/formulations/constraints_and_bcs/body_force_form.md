<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/body_force_form.html -->

# ImposedBodyForceFormulation

## Introduction

This formulation computed the contribution of body forces in a solid material.
It is a generalized formulation that can be used to model any body force. It is based
on the definition of a `BodyForceEvaluator` that can be designed in a specialized
formulation to model a given body force. For instance, we have created the
`ImposedUniformGravityForceFormulation` that sets the force per unit volume
as the universal gravity constant.

## Example of usage

The following include is required:

```c++
#include "manta/components-modeling/mechanics/imposed_body_force_formulation.h"
```

It can be constructed with:

```c++
ImposedBodyForceFormulation<h, sid, BodyForceEvaluatorType>(ms, qid, ct, Uvar, BodyForceEvaluator)
```

## Parameters

`ImposedBodyForceFormulation` has three template parameters

- `h`, The geometric hypothesis
- `sid`, The shape ID
- `BodyForceEvaluatorType`, type used to evaluate the force fields's contribution per unit volume

`ImposedBodyForceFormulation` has five parameters

- `ms`, the meshSet onto which the formulation is defined
- `qid`, the quadrature used to integrate the formulation
- `ct`, the configuration time
- `Uvar`, the dof variable linked to the primal field
- `BodyForceEvaluator` The BodyForceEvaluator which yields the the force per unit volume

## Description

This formulation is thought to be used as a base class for any body force that could be modeled. Let that be
for uniform or non uniform force fields, as well as uniform or non uniform density (mass density for a self weight body force,
or current density for a magnetic based body force). It computed the contribution of the following variational operator:

(23)\[-\int_{\Omega_{c}}\rho(x)_{c}\,\cdot\,\v{g}(x)_{c}\,\cdot\,\var{u} \d\,v =
-\int_{\Omega_{r}}J\,\rho(x)_{c}\,\cdot\,\v{g}(x)_{c}\,\cdot\,\var{u} \d\,V =
-\int_{\Omega_{r}}\rho(x)_{r}\,\,\cdot\,\v{g}(x)_{r}\,\cdot\,\var{u} \d\,V\]

where:

- \(\Omega_{c}\) denotes the current configuration.
- \(\Omega_{r}\) denotes the reference configuration.
- \(J\) is the determinant of the gradient of the transformation (the jacobian of the transformation).
- \(\rho(x)_{c}\) is mass density in the current configuration (can be non uniform).
- \(\rho(x)_{r}\) is mass density in the reference configuration (can be non uniform).
- \(\v{g(x)}\) is a vector describing the intensity and direction of the force per unit of mass.

Note that the mass density could be seen as a current density if this formulation was to be used for an
electromagnetic based body force.

## Notes

This formulation is not designed to be used as a standalone. It is designed to be a base class,
onto which another formulation is built upon, where the mass density and force field specificities can be
extended.
Interested advanced users can look at the `ImposedUniformGravityForceFormulation` which is the first of
such body force formulation, i.e, that is based on the `ImposedBodyForceFormulation`, and specializes to a given
uniform force field.

In the `ImposedUniformGravityForceFormulation`, a body force is defined, the `ImposedUniformGravityForce`,
that takes in the mass density, and the force per unit of mass, in order to compute the force per unit of volume.
This force per unit of volume is the one that is given to the `ImposedBodyForceFormulation` to compute the contribution
of the body force to the right hand side of the `LinearSystem`.
