<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/micromorphic_damage/implicit_micromorphic_damage_brick.html -->

# The `ImplicitMicromorphicDamageSolidMaterialBrick` brick

Note

This brick relies on an **external** MFront behavior to work.
Even though this section is self-consistent, the user may want to
read Sections [Generalities on bricks based on MFront behaviors](../../miscellaneous/mfront_behaviors_bricks.md#mfront-behaviors-bricks) and
[Advices on the management of MFront material knowledge](../../miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management) for addtional details
and advices.

This brick computes the stiffnes matrix and the residual associated with
the following variational operator:

\[\int_{\Omega}\left[a_{\chi}\,\var{d_{\chi}}+\v{b}_{\chi}\,\cdot\,\vgradient{\var{d_{\chi}}}\right]\,\d\,V\]

where

- \(\var{d_{\chi}}\) is an kinematically admissible variation of
  \(d_{\chi}\),
- \(a_{\chi}\) and \(\v{b}_{\chi}\) denotes respectively the
  thermodynamic forces associated with \(d_{\chi}\) and
  \(\vgradient{d_{\chi}}\).

The thermodynamic forces \(a_{\chi}\) and \(\v{b}_{\chi}\) must
be computed by a dedicated *behavior*.

Generally, the micromorphic damage behavior will declare the damage as
an internal state variable and handles its evolution using the elastic
energy release rate computed by the mechanical model. See
[[FHS+22](../../../references/references.md#id26), [Sie23](../../../references/references.md#id24)] for details and
description of behaviors associated with some classical phase-field
models.

Note

The *ImplicitMechanicsSolidMaterial* brick deleguates the
computation of the inner forces and stiffness matrices to the
`ImplicitMicromorphicSolidMaterialFormulation` class. This class
can be used directly by advance users.

## About the micromorphic damage behavior

The behaviour must have been generated using MFront' generic
interface. This behaviour must:

- Declare two gradients in that order:

  1. The micromorphic damage \(d_{\chi}\). This variable must be
     named *MicromorphicDamage* and must be a scalar.
  2. The gradient of the micromorphic damage
     \(\vgradient{d_{\chi}}\). This variable must be named
     *MicromorphicDamageGradient* and must be a vector.
- Declare two thermodynamic forces in that order:

  1. The dual of the micromorphic damage \(a_{\chi}\). This variable
     must be named *MicromorphicDamageDualForce* and must be a
     scalar.
  2. The dual of the gradient of the micromorphic damage
     \(\v{b}_{\chi}\). This variable must be named
     *MicromorphicDamageGradientDualForce* and must be a vector.
- Declare two or four tangent operator blocks:

  - when two tangent operator blocks are declared, they must correspond
    respectively to \(\pdfrac{a_{\chi}}{\Delta\,d_{\chi}}\) and
    \(\pdfrac{\v{b}_{\chi}}{\Delta\,\vgradient{d_{\chi}}}\). The
    cross-derivatives
    \(\pdfrac{a_{\chi}}{\Delta\,\vgradient{d_{\chi}}}\) and
    \(\pdfrac{\v{b}_{\chi}}{\Delta\,d_{\chi}}\) are assumed to be
    null.
  - when four tangent operator blocks are declared, they must correspond
    to \(\pdfrac{a_{\chi}}{\Delta\,d_{\chi}}\),
    \(\pdfrac{a_{\chi}}{\Delta\,\vgradient{d_{\chi}}}\),
    \(\pdfrac{\v{b}_{\chi}}{\Delta\,d_{\chi}}\) and
    \(\pdfrac{\v{b}_{\chi}}{\Delta\,\vgradient{d_{\chi}}}\).

The requirements of the behavior, corresponding to its material
properties and external state variables respecively, are automatically
declared by the brick and treated by the dependency management
algorithm. In the case of orthotropic behaviors, a dependency to the
rotation matrix (expressed in the reference configuration) is
automatically declared.

The state variables of the behavior are automatically used to fulfill
dependencies of other models or post-processing by the dependency
management algorithm.

## Main parameters

The main parameters used to initial the brick are:

- *domain* (which must be a string) or *domains* (which must
  be an array of strings). Each of thoses strings are interpreted as
  regular expressions.
- *library* (which must be a string), which indicates in which
  library the MFront behavior must be loaded.
- *behavior* (which must be a string), whih indicates which
  behavior must be loaded in the library.
- *hypothesis* (which must be a string), which indicated which
  structural hypothesis shall be used. This is only useful in 2D under the
  inPlane geometric hypothesis:

  - In 3D, the Tridimensional structural hypothesis is automatically selected.
  - In 2D, the Axisymmetrical structural hypothesis is automatically
    selected if the corresponding geometric hypothesis is set.
  - In 2D, the planeStress and planeStrain hypotheses are equivalent.
- *quadratureOrder* (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.
- *integrationScheme* (which must be a string). This
  parameter is *optional* and defaults to default. It allows to select
  an integration scheme, as an identifier for specific formulation. This
  parameter is only useful when using user-defined formulations
  (see [User-defined extensions](#implicit-micromorphic-damage-user-defined-extensions)).

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *tet4*, *tet10*, *hex8*, *hex20*, *pyr5* |
| *PlaneStrain* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *PlaneStress* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *Axisymmetrical* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |

## Example of usage

The following code adds the an *ImplicitMicromorphicDamageSolidMaterialBrick*
brick to a micromorphic damage model:

```c++
micromorphicDamageResourcesManager->add(ctx,
                             "ImplicitMicromorphicDamageSolidMaterial",
                             {{"domain", "bar"},
                              {"library", lib},
                              {"behavior", "MiehePhaseFieldDamage"},
                              {"hypothesis", "PlaneStrain"},
                              {"quadratureOrder", 1}});
```

## User-defined extensions

User can register variants of the previous built-in formulations by registring new
generators to the `ImplicitMicromorphicDamageSolidMaterialFormulationsFactory` class.

## Compatible models

This brick is compatible with the following models:

- [Implicit micromorphic damage model](../../models/micromorphic_damage/implicit_micromorphic_damage_model.md#implicit-micromorphic-damage-model)
