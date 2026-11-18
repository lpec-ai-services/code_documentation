<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/solid_mechanics/implicit_mechanics_solid_material.html -->

# The `ImplicitMechanicsSolidMaterial` brick

The `ImplicitMechanicsSolidMaterial` brick describes a non linear material.
This brick relies on an **external** MFront behavior to work.

Note

Even though this section is self-consistent, the user may want to
read Sections [Generalities on bricks based on MFront behaviors](../../miscellaneous/mfront_behaviors_bricks.md#mfront-behaviors-bricks) and
[Advices on the management of MFront material knowledge](../../miscellaneous/mfront_material_knowledge_management.md#mfront-material-knowledge-management) for addtional details
and advices.

## Example of usage

The following code adds the an *ImplicitMechanicsSolidMaterial*
brick to a mechanical model:

```c++
mechanics_model->add(
    ctx, "ImplicitMechanicsSolidMaterial",
    Parameters{{"domain", "cube"},
               {"library", "./libHyperElasticityBehaviours-generic.so"},
               {"behavior", "SaintVenantKirchhoffElasticity"}});
```

## Main parameters

The main parameters used to initialize the brick are:

- `domain` (which must be a string) or `domains` (which must
  be an array of strings). Each of those strings are interpreted as
  regular expressions.
  - `material` is equivalent to `domain`.
  - `materials` is equivalent to `domains`.
- `library` (which must be a string), which indicates in which
  library the MFront behavior must be loaded.
- `behavior` (which must be a string), which indicates which
  behavior must be loaded in the library.
- `hypothesis` (which must be a string), which indicated which
  structural hypothesis shall be used. This is only useful in 2D under the
  inPlane geometric hypothesis:

  - In 3D, the Tridimensional structural hypothesis is automatically selected.
  - In 2D, the Axisymmetrical structural hypothesis is automatically
    selected if the corresponding geometric hypothesis is set.
- `exportStrain`: boolean stating if the strain shall be exported
  (`true` by default). This parameter is only valid for small
  strain behaviors.
- `exportDeformationGradient`: boolean stating if the deformation
  gradient shall be exported (`true` by default). This parameter is
  only valid for finite strain behaviors.
- `exportStress`: boolean stating if the stress shall be exported
  (`true` by default). This parameter is only valid for small
  strain behaviors.
- `exportFirstPiolaKirchhoffStress`: boolean stating if the first
  Piola-Kirchhoff stress shall be exported (`true` by default).
  This parameter is only valid for finite strain behaviors.
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.
- `integrationScheme` (which must be a string). This
  parameter is *optional* and defaults to default. It allows to select
  an integration scheme, as an identifier for specific formulation. This
  parameter is only useful when using user-defined formulations
  (see [User-defined extensions](#implicit-mechanics-user-defined-extensions)).

## Description

If a behavior written under the infinitesimal perturbation hypothesis is
considered, the *ImplicitMechanicsSolidMaterial* brick` computes
the stiffness matrix and the residual associated with the following
variational operator, which describes the virtual power/work of inner forces:

(7)\[\int_{\Omega_{r}}\tsigma\,\colon\,\tepsilonto\paren{\var{\v{u}}} \d\,V\]

where:

- \(\Omega_{r}\) is the domain on which the brick is defined, in the
  reference configuration,
- \(\var{\v{u}}\) is a kinematically admissible virtual variation of
  the displacement field,
- \(\tsigma\) is the stress tensor, that can be identified to the
  Cauchy stress in the reference configuration for a small strain
  behavior,
- \(\tepsilonto\) is the linearized strain such that:
  \(\tepsilonto\paren{\v{u}} = sym \tGradient{\v{u}} =
  \frac{1}{2}\paren{\tGradient{\v{u}}+\transpose{\tGradient{\v{u}}}}\),
  where \(\tGradient{\v{u}}\) denotes the gradient of \(\v{u}\)
  in the reference configuration.

If a finite strain behavior is considered, the
*ImplicitMechanicsSolidMaterial* brick handles the following
variational operator:

(8)\[\int_{\Omega_{r}}\tPKI\,\colon\,\tGradient{\paren{\var{\v{u}}}} \d\,V\]

where \(\tPKI\) denotes the first Piola-Kirchhoff stress. Note that
this stress tensor is not symmetric.

Note

The choice between the two variational operators
[(7)](#equation-manta-user-guide-implicit-mechanics-small-strain-inner-forces) and
[(8)](#equation-manta-user-guide-implicit-mechanics-finite-strain-inner-forces) is
done automatically by the brick based on the information exported by
the behavior.

Note

By convention, the inner forces are substracted to the residual (right
hand side of the underlying linear system, in MANTA's wording). See
Equation
eq:manta:user_guide:implicit_mechanics:external_and_inner_forces.

Note

The *ImplicitMechanicsSolidMaterial* brick deleguates the
computation of the inner forces and stiffness matrices to the
`ImplicitMechanicsSolidMaterialFormulation` class. This class
can be used directly by advanced users.

### About the behavior

The behaviour must have been generated using MFront generic
interface.

The requirements of the behavior, corresponding to its material
properties and external state variables respecively, are automatically
declared by the brick and treated by the dependency management
algorithm. In the case of orthotropic behaviors, a dependency to the
rotation matrix (expressed in the reference configuration) is
automatically declared.

The state variables of the behavior are automatically used to fulfill
dependencies of other models or post-processing by the dependency
management algorithm.

## Supported structural hypotheses and elements

The following table summarizes the list of supported structural
hypotheses and, for each hypothesis, the list of elements.

| Structural hypothesis | Supported elements |
| --- | --- |
| *Tridimensional* | *tet4*, *tet10*, *hex8*, *hex20*, *pyr5* |
| *PlaneStrain* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *PlaneStress* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |
| *Axisymmetrical* | *tri3*, *tri6*, *tri10*, *qua4*, *qua8* |

## User-defined extensions

User can register variants of the previous built-in formulations by registring new
generators to the cxx:ImplicitMechanicsSolidMaterialFormulationsFactory class.

## Compatible models

This brick is compatible with the following models:

- [The ImplicitMechanics model](../../models/solid_mechanics/implicit_solid_mechanics.md#implicit-mechanics-model)
