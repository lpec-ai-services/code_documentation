<!-- source: data_optimization.rst -->

# Data optimization for numerical codes

## Renumbering to improve locality

A mesher (like SMESH) often generates a scattered cell distribution in output unstructured mesh. So a common task for simulation codes is the reordering for a better locality.

medcoupling can do that simply by doing

(example `UG_Optimization_0` not found in UsersGuideExamplesTest.py: broken reference in the upstream docs)

RenumberingFactory method creates a renumbering algorithm of a specified type: either "Boost" or "Metis".

## Partitionning for multi procs

For simulation codes following the SPMD paradigm, the partitionning is a key step. medcoupling can perform this partition. Here is an example of partitioning mesh *m* into 4 parts and retrieving the first part:

(example `UG_Optimization_1` not found in UsersGuideExamplesTest.py: broken reference in the upstream docs)

It's then possible to add a layer or more of cells.

(example `UG_Optimization_2` not found in UsersGuideExamplesTest.py: broken reference in the upstream docs)
