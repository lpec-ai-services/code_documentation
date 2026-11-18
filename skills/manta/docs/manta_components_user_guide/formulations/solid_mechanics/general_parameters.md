<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/general_parameters.html -->

# General parameters of solid mechanics formulations

## The structural hypothesis

In solid mechanics formulations, the structural hypothesis is specified with a
template parameter taking a value of type `StructuralHypothesis`.
`StructuralHypothesis` is an enumeration containing the valid structural
hypothesis. They are:

- `StructuralHypothesis::tridimensional`,
- `StructuralHypothesis::planeStress`,
- `StructuralHypothesis::planeStrain`,
- `StructuralHypothesis::axisymmetrical`.

## The kinematic formulation

The kinematic description used for solid mechanics formulations is the total
Lagrangian formulation.

For some formulations (e.g. beam formulations), a corotational formulation
based on the updated Lagrangian description is also available. In those formulations,
kinematics description are specified using a value in the `KinematicDescription`
enumeration:

- `KinematicDescription::lagragian` for the total Lagrangian formulation,
- `KinematicDescription::corotational` for the corotational formulation
  based on a updated Lagrangian description.

The two formulations are described in corresponding theory manual (e.g. for beams
the description can be seen [here](../../../theory_manual/solid_mechanics/beams/beam_theory.md#theory-beam-kinematic-description-formulation)).
