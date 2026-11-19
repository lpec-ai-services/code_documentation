<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/models/generalities.html -->

# Generalities on models

See also

Further help about available models can be found in the
`Models` section of the online help which is accessible in
python through the manta.info function or through the manta-info
utility (see Section [The manta-info utility](../miscellaneous/tools.md#manta-info-utility)).

PYTHON

```python
manta.info('Models')
```

SH

```sh
manta-info Models
```

## Discretization methods

MANTA supports several discretization methods.

The discretization method can be selected, by order of priority at the
brick level (using the `discretizationMethod` parameter), at the
model level and at the physical level (using in those case the
`defaultDiscretizationMethod` parameter).

By default, the finite element method is used.

By default, models shall not allow to mix bricks using distinct
discretization methods. This can be changed using the parameter
`allowMixingDiscretizationMethods`, which must be set to
`true`.

## Periodic computations support

Periodic computations support requires to:

1. Deal with so-called "periodic boundary conditions".
2. Impose the macroscopic gradients.

### Periodic boundary conditions

Physical models based on solving partial derivative equations (PDEs)
require boundary conditions. If the mesh is periodic (which is usually
automatically detected when loading the mesh), periodic boundary
conditions have to be automatically imposed.

Note

Technically, periodicity is not associated with a specific boundary
condition. Entities on the external boundaries of the mesh are
merged in the connectivity map used to define the degrees of freedom
of the problem, i.e. the same degree of freedom is assigned to
two entities connected by the periodicity condition.

### Macroscopic gradients

Periodic computations requires to define the macroscopic gradients
(macroscopic deformation gradients for finite strain analyses,
macroscopic strain under the infinitesimal perturbation hypothesis,
temperature gradient in heat transfer, etc.). Each brick must define a
way to support the definition of macroscopic gradients, including
user-defined bricks.

This section describes how macroscopic gradients are automatically taken
into account by bricks based on MFront behaviors.

For each component `I` of the gradient `G` of the behavior,
those bricks will look if a loading evolution named
`MacroscopicG[I]` is defined.

For instance, a finite strain behavior has only one gradient named
`DeformationGradient`. The behavior will look if the loading
evolution named `MacroscopicDeformationGradient[0]` is defined and
will do the same for the other components. If this evolution is not
defined, the default value is applied. Note that the components are
stored using [MFront conventions, see](https://thelfer.github.io/tfel/web/tensors.html) for details.

## Linear solver options

The resolution of the underlying linear system can be tuned by users
using the interface described in [this page](../../manta_components_user_guide/main_user_concepts/user_guide_objects/linear_solver_interface.md#linear-solver-interface).
