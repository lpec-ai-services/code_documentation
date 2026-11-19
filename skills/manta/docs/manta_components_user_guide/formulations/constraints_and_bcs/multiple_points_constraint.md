<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/multiple_points_constraint.html -->

# Multiple Point Constraint

## Description

The multiple point constraint formulation enables to enforce constraints between several degrees of freedom of the finite element mesh.
The enforced constraint can be seen as the linear combination between those dofs such that:

\[\Sigma_i^n \left(a_i \cdot DOF_i\right) = RHS_{tot}\]

Note that this formulation enables the construction of constraints on \(n > 1\) meshsets, each composed of \(m\) nodes, with
\(m\) being a constant or 1.

When we consider \(m > 1\), the ordering of nodes becomes of importance. In this case, the user *must* specify the `linkerSeg` parameter
in order to avoid issues of spurious ordering in the constraint. Future features will implement node ordering subroutines that enable users to specify
an ordering based on a geometric criterion.

For the moment, when no `linkerSeg` arguments is given, but when at least one `MeshSet` contains more than one node, an error message stops
the user.

## Example of usage

The following snippet shows how to create a formulation imposing a constraint between two `MeshSets`.
Here, we constrain the opposing edges of a square to be of identical displacement:

```c++
auto &MPC = rm.make<MultiplePointsConstraintFormulation>(constraintData, RHS_tot, &linkerSeg);
```

where:

- `constraintData` holds all information related to the constraint
- `RHS_tot` is a `Real` representative of the right hand side of the constraint ,
- `linkerSeg` is a `MeshSet` of `SEG2` linking the nodes of each constrained `MeshSet`.

Here is an example of the construction of those specific structures, starting with `constraintData`:

```c++
std::tuple<const MeshSet *, const Real, const Int, const DofVar> data1 =
std::make_tuple(&l_left, c1, component1, Uvar);
std::tuple<const MeshSet *, const Real, const Int, const DofVar> data2 =
std::make_tuple(&l_right, c2, component2, Uvar);
Vector<std::tuple<const MeshSet *, const Real, const Int, const DofVar>>
constraintData = {data1, data2};
```

For this example consider the 2D square illustrated below. We want to constrain the sides together. However, since there are 3 nodes per side,
the order with which we constrain the nodes two by two is very important. For this specific example we will enforce that the nodes constrained two by two follow
the geometric order: bottom nodes together, middle nodes together, and top nodes together.

[![figure](https://manta-project.gitlab.io/manta/_images/rela_ex.svg)](https://manta-project.gitlab.io/manta/_images/rela_ex.svg)

Using the nomenclature shown above, with `l_right` and `l_left` are constituted respectively by nodes `ptr`, `pmr`, `pbr`
and `ptl`, `pml`, `pbl`. We can enforce that `ptr`, `ptl`, the top nodes are constrained together,
as well as the mid nodes `pmr` and `pml`, and bottom nodes `pbr` and `pbl` respectively. `linkerSeg` must
then be a `MeshSet` of `SEG2` linking those respective nodes. Here three `SEG2` linking the constrained nodes must be defined.

## Parameters

The main constructor of the `MultiplePointsConstraintFormulation` class has three
parameters:

- the `constraintData` argument which holds all the relevant constraint information,
  it is a Vector of tuple containing: the constrained `MeshSet`, the coefficient linked with those dofs (`Real`),
  an `Int` designating a specific component on the constrainted node, and a `DofVar` linked with the constrained nodes,
- the `RHS_tot`, (*optional*) a Real being the right hand side of the constraint. If it is not specified, it is initialized as 0.
- the `linkerSeg` (*optional*) a structure specifying the order at which we constrain nodes of a given meshset.
  This structure is a `MeshSet` of `SEG2` linking the nodes of each constrained `MeshSet`. If all
  constrained `MeshSets` are composed of one node, it is optional.

## Preconditions

The user (at this layer) is responsible to check the following pre-conditions:

- The `MeshSets` must be composed of \(m\) nodes, with \(m\) being constant or 1.
- The first `MeshSet` given in the parameter `constraintData` must be the largest one (one of them).
- If the user mixes `MeshSet` of one node and \(m > 1\) nodes, the largest must be linked first and the one node `MeshSets` must be linked last,
  by the inputted `SEG2` in `linkerSeg`. See the blueprint of mpc <blueprint_mpc_structure> for more details.

## Notes

In order to ensure correct parsing of nodes during the ordering stage, and later the assembling stage, migration of *ALL* constrained nodes on the root proc
was implemented. This threatens the scalability of the formulation. This migration stage is handled in the `MultiplePointsConstraintManagement` source files.
In the future, an implementation that remigrate ordered node back on diverse procs could be tested to ensure good scalability of the approach.
