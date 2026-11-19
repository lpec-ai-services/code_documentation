<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/booleanArguments.html -->

# Arguments of Boolean Operations

This section describes the shapes applicable as arguments of Boolean Operations.
First of all, the result of Boolean Operations depends on the dimension of arguments. The following table shows the dimension and corresponding types of shapes.

| Dimension | Shape types |
| --- | --- |
| 0 | VERTEX, COMPOUND |
| 1 | EDGE, WIRE, COMPOUND |
| 2 | FACE, SHELL, COMPOUND |
| 3 | SOLID, COMPSOLID, COMPOUND |

*Note*: COMPOUND may consist of any shape combinations, therefore, it is present is each row.

The next table aligns an operation and the dimensions of its arguments.
Construction planes (mentioned PLANE) can be used in several operations, but not included in the table above due to their infinite nature.

| Operation | Dimension of objects (DO) | Dimension of tools (DT) |
| --- | --- | --- |
| [common.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common.png) [Common](commonFeature.md#featurecommon) | Any | Any (+ PLANE) |
| [cut.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_cut.png) [Cut](cutFeature.md#featurecut) | Any | Not less than **DO** |
| [fuse.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_fuse.png) [Fuse](fuseFeature.md#featurefuse) | Any | Any |
| [inter.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/intersection_btn.png) [Intersection](intersectionFeature.md#featureintersect) | 1 or 2 | — |
| [partition.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/partition_btn.png) [Partition](partitionFeature.md#featurepartition) | Any (+ PLANE) | — |
| [smash.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_smash.png) [Smash](smashFeature.md#featuresmash) | 2 (planar FACE only) or 3 | Equal to **DO** |
| [split.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_split.png) [Split](splitFeature.md#featuresplit) | Any | Any (+ PLANE) |
| [union.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/union_btn.png) [Union](unionFeature.md#featureunion) | 3 (SOLIDs from COMPSOLID) | — |

The optional fuzzy parameter of each boolean operation is used as an additional tolerance to eliminate tiny results.
