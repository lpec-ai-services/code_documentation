<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/mfront_behaviors_bricks.html -->

# Generalities on bricks based on MFront behaviors

Many bricks rely on external MFront behaviors to work:

- `MFrontPointWiseModel`
- `ImplicitMechanicsSolidMaterial`
  (Section [The ImplicitMechanicsSolidMaterial brick](../bricks/solid_mechanics/implicit_mechanics_solid_material.md#implicit-mechanics-solid-material-brick))
- `ImplicitHeatTransferSolidMaterial`
  (Section [The ImplicitHeatTransferSolidMaterial brick](../bricks/solid_heat_transfer/implicit_heat_transfer_solid_material.md#implicit-heat-transfer-solid-material-brick))
- `ImplicitMicromorphicDamageSolidMaterial`
  (Section [The ImplicitMicromorphicDamageSolidMaterialBrick brick](../bricks/micromorphic_damage/implicit_micromorphic_damage_brick.md#implicit-micromorphic-damage-solid-material-brick))

Those bricks inherit from a common class named
`MFrontModelBrickBase`. This section is devoted to provide
an overview of the role of this class.

Note

The usage of those bricks requires the use of MFront generated
libraries, which are **external** to MANTA. Those libraries must be
managed with care, as described in Section
[Advices on the management of MFront material knowledge](mfront_material_knowledge_management.md#mfront-material-knowledge-management).

## About the behavior

The behavior must have been generated using MFront generic
interface.

## Interaction with the dependency management algorithm

The requirements of the behavior, corresponding to its material
properties and external state variables respectively, are automatically
declared by the brick and treated by the dependency management
algorithm. In the case of orthotropic behaviors, a dependency to the
rotation matrix (expressed in the reference configuration) is
automatically declared.

The state variables of the behavior are automatically used to fulfill
dependencies of other models or post-processing by the dependency
management algorithm.

## Common parameters

- `domain` (which must be a string) or `domains` (which must
  be an array of strings). Each of those strings are interpreted as
  regular expressions.
- `library` (which must be a string), which indicates in which
  library the MFront behavior must be loaded. See Section
  [Advices on the management of MFront material knowledge](mfront_material_knowledge_management.md#mfront-material-knowledge-management).
- `behavior` (which must be a string), which indicates which
  behavior must be loaded in the above library.
- `hypothesis` (which must be a string), which indicated which
  structural hypothesis shall be used. This is only useful in 2D under the
  inPlane geometric hypothesis:

  - In 3D, the Tridimensional structural hypothesis is automatically selected.
  - In 2D, the Axisymmetrical structural hypothesis is automatically
    selected if the corresponding geometric hypothesis is set.
- `quadratureOrder` (which must be a positive integer). This
  parameter is *optional* and allows to select the quadrature order.
- `defaultTangentOperator` (which must be a string). This parameter
  is *optional* and defines the default tangent operator. Valid values are:
  `Elastic`, `Secant`, `Tangent` and
  `ConsistentTangent`. If this parameter is not used, the
  `ConsistentTangent` value is used by default.
