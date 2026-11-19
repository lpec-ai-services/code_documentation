<!-- source: https://docs.salome-platform.org/latest/gui/HYBRIDPLUGIN/hybridpluginpy_doc/classsmeshBuilder_1_1Mesh.html -->

# Mesh Class Reference

This class allows defining and managing a mesh.
[More...](classsmeshBuilder_1_1Mesh.md#details)

## Detailed Description

This class allows defining and managing a mesh.

Note
:   The documentation below does not provide complete description of class **Mesh** from **[smeshBuilder](namespacesmeshBuilder.md)** package. This documentation provides only information about the methods dynamically added to the Mesh class by the HYBRIDPlugin plugin For more details on the Mesh class, please refer to the SALOME Mesh module documentation.

## Member Function Documentation

### Tetrahedron()

```python
def Tetrahedron(algo_type, geom_shape = 0)
```

Creates tetrahedron 3D algorithm for volumes.

This method is dynamically added to Mesh class by the meshing plug-in(s).

If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh). Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

Parameters
:   |  |  |
    | --- | --- |
    | algo_type | type of algorithm to be created; allowed values are specified by classes implemented by plug-in |
    | geom_shape | if defined, the subshape to be meshed (GEOM_Object) |

Returns
:   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see [HYBRIDPluginBuilder.HYBRID_Algorithm](classHYBRIDPluginBuilder_1_1HYBRID__Algorithm.md)
