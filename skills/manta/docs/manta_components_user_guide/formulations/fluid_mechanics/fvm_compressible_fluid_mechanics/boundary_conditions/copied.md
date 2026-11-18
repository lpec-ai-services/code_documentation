<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/copied.html -->

# `Copied` boundary condition

The `Copied` boundary condition characterizes a supersonic outflow. All
waves are supposed to propagate outside the domain. The outside state is then
copied from the inside state. This boundary condition can be applied for other
boundaries like inflows, but it is assumed that all waves are absorbed.

## Usage

The `CopiedBoundaryCondition` is the default boundary condition, meaning
that every boundary meshSet that is not associated with a boundary condition is
affected with `Copied`. It is then usually not explicitely set by the user.
