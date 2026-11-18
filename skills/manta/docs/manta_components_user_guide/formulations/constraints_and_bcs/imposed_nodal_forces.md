<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/imposed_nodal_forces.html -->

# Imposed nodal forces

## Example of usage

```c++
constexpr Int dim = 3; // 3D
ColVector<dim> F;
auto &formulation = rm.make<ImposedNodalForcesFormulation<dim, ColVector<dim>&>>(Uvar, F, meshSet);
```

```c++
constexpr Int dim = 3; // 3D
auto &field = rm.make<NodeField<dim, 1>>(meshSet, "field");
auto &formulation =
  rm.make<ImposedNodalForcesFormulation<dim, NodeField<dim, 1>&>>(Uvar, field, meshSet);
```

where:

- `Uvar` is the dof variable of the displacement field
- `F` is vector of uniform nodal forces
- `field` is a *NodeField* of nodal forces
- `meshSet` is the a meshSet representing the boundary

## Parameters

`ImposedResultingForceFormulation` has only two template parameters

- The dimension of the problem (and as such the dimension of the applied force).
- The evaluator type which may either be a `NodeField<dim>`
  or a vector `ColVector<dim>` (or again `RowVector<dim>`)

## Description

This formulation directly applies the given nodal force to the residual.

## Notes

- This formulation is used in the *MBM* formulation
