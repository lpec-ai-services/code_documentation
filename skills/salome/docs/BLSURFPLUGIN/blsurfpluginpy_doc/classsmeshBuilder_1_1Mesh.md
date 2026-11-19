<!-- source: https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurfpluginpy_doc/classsmeshBuilder_1_1Mesh.html -->

# Mesh Class Reference

This class allows defining and managing a mesh.
[More...](classsmeshBuilder_1_1Mesh.md#details)

## Detailed Description

This class allows defining and managing a mesh.

Note
:   The documentation below does not provide complete description of class **Mesh** from **[smeshBuilder](namespacesmeshBuilder.md)** package. This documentation provides only information about the methods dynamically added to the Mesh class by the BLSURFPlugin plugin For more details on the Mesh class, please refer to the SALOME Mesh module documentation.

## Member Function Documentation

### Triangle()

```python
def Triangle(algo_type, geom_shape = 0)
```

Creates triangle algorithm for faces.

This method is dynamically added to Mesh class by the meshing plug-in(s).

If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh). Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

Parameters
:   |  |  |
    | --- | --- |
    | algo_type | type of algorithm to be created; allowed values are specified by classes implemented by plug-in |
    | geom_shape | if defined, the subshape to be meshed (GEOM_Object) |

Returns
:   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see [BLSURFPluginBuilder.BLSURF_Algorithm](classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md)
