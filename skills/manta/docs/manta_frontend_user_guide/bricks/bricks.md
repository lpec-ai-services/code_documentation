<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/bricks/bricks.html -->

# Bricks

*Bricks* are the objects that are added to a *Model* (see [Models](../models/models.md#models)) to define
and describe the behavior of materials, structural elements, boundary conditions,
etc.

A *Brick* is generally linked to one or several *Formulations* (see [Catalog : Formulations and Algorithms by theme](../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme))
and implements the equation terms that the model has to represent. They may
cover a wide variety of phenomena, ranging from finite elements (such as Euler beams)
to point-wise behavior or specific flux computations for the finite volume method.

Each *Brick* is compatible with a subset of all the available *Models*: the user
is expected to check that compatibility beforehand.

## Organized by model category

- [Solid mechanics bricks](solid_mechanics/solid_mechanics_bricks.md)
- [Solid heat transfer bricks](solid_heat_transfer/heat_transfer_bricks.md)
- [Point-wise bricks](point_wise/point_wise_bricks.md)
- [Micromorphic damage bricks](micromorphic_damage/micromorphic_damage_bricks.md)

## All bricks

- [The `EulerBeam` brick](solid_mechanics/beams/euler_beam_brick.md)
- [The `ExplicitEulerBeam` brick](solid_mechanics/beams/explicit_euler_beam_brick.md)
- [The `EulerBeamDistributedLoadings` brick](solid_mechanics/beams/euler_beam_distributed_loadings_brick.md)
- [The `ImplicitHeatTransferSolidMaterial` brick](solid_heat_transfer/implicit_heat_transfer_solid_material.md)
- [The `HeatSource` brick](solid_heat_transfer/implicit_heat_transfer_heat_source.md)
- [The `ImplicitHeatLinearConvection` brick](solid_heat_transfer/implicit_heat_transfer_linear_convection.md)
- [The `ImplicitHeatTransferNonlinearConvection` brick](solid_heat_transfer/implicit_heat_transfer_nonlinear_convection.md)
- [The `ImplicitHeatLinearCapacity` brick](solid_heat_transfer/implicit_heat_transfer_linear_capacity.md)
- [The `ImplicitMechanicsSolidMaterial` brick](solid_mechanics/implicit_mechanics_solid_material.md)
- [The `ImplicitMicromorphicDamageSolidMaterialBrick` brick](micromorphic_damage/implicit_micromorphic_damage_brick.md)
- [The `ImposedHeatFlux` brick](solid_heat_transfer/imposed_heat_flux.md)
- [The `ImposedPressure` brick](solid_mechanics/imposed_pressure.md)
- [The `ImposedResultingForce` brick](solid_mechanics/imposed_resulting_force.md)
- [The `ImposedUniformGravityForce` brick](solid_mechanics/imposed_uniform_gravity_force.md)
- [The `IsotropicLinearElasticSolidMaterial` brick](solid_mechanics/isotropic_linear_elastic_material.md)
- [The `MFrontPointWiseModel` model brick](point_wise/mfront_point_wise_model_brick.md)
- [The `NodalMass` brick](solid_mechanics/nodal/nodal_mass_brick.md)
- [The `TimoshenkoBeam` brick (implicit mechanics)](solid_mechanics/beams/timoshenko_beam_brick.md)
- [The `TimoshenkoBeamDistributedLoadings` brick](solid_mechanics/beams/timoshenko_beam_distributed_loadings_brick.md)
