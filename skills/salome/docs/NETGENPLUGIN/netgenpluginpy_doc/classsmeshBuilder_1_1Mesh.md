<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/classsmeshBuilder_1_1Mesh.html -->

# Mesh Class Reference

This class allows defining and managing a mesh.
[More...](classsmeshBuilder_1_1Mesh.md#details)

## Detailed Description

This class allows defining and managing a mesh.

Note
:   The documentation below does not provide complete description of class **Mesh** from **[smeshBuilder](namespacesmeshBuilder.md)** package. This documentation provides only information about the methods dynamically added to the Mesh class by the NETGENPlugin plugin For more details on the Mesh class, please refer to the SALOME Mesh module documentation.

## Member Function Documentation

### Tetrahedron()

```python
def Tetrahedron(algo_type, geom_shape = 0)
```

Creates tetrahedron 3D algorithm for solids.

This method is dynamically added to Mesh class by the meshing plug-in(s).

If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh). Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

Parameters
:   |  |  |
    | --- | --- |
    | algo_type | type of algorithm to be created; allowed values are specified by classes implemented by plug-in |
    | geom_shape | if defined, the subshape to be meshed (GEOM_Object) |

Returns
:   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see [NETGENPluginBuilder.NETGEN_1D2D3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md), [NETGENPluginBuilder.NETGEN_3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__3D__Algorithm.md), [NETGENPluginBuilder.NETGEN_3D_Remote_Algorithm](classNETGENPluginBuilder_1_1NETGEN__3D__Remote__Algorithm.md)

### Netgen()

```python
def Netgen(algo_type, geom_shape = 0)
```

Deprecated, used only for compatibility! See [Tetrahedron()](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b) method.

This method is dynamically added to Mesh class by the meshing plug-in(s).

If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh). Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

Parameters
:   |  |  |
    | --- | --- |
    | algo_type | type of algorithm to be created; allowed values are specified by classes implemented by plug-in |
    | geom_shape | if defined, the subshape to be meshed (GEOM_Object) |

Returns
:   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see [NETGENPluginBuilder.NETGEN_1D2D3D_Algorithm_2](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm__2.md)

### Triangle()

```python
def Triangle(algo_type, geom_shape = 0)
```

Creates triangle 2D algorithm for faces.

This method is dynamically added to Mesh class by the meshing plug-in(s).

If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh). Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

Parameters
:   |  |  |
    | --- | --- |
    | algo_type | type of algorithm to be created; allowed values are specified by classes implemented by plug-in |
    | geom_shape | if defined, the subshape to be meshed (GEOM_Object) |

Returns
:   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see [NETGENPluginBuilder.NETGEN_1D2D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D__Algorithm.md), [NETGENPluginBuilder.NETGEN_1D2D_Algorithm_2](classNETGENPluginBuilder_1_1NETGEN__1D2D__Algorithm__2.md), [NETGENPluginBuilder.NETGEN_2D_Only_Algorithm](classNETGENPluginBuilder_1_1NETGEN__2D__Only__Algorithm.md), [NETGENPluginBuilder.NETGEN_2D_Remote_Algorithm](classNETGENPluginBuilder_1_1NETGEN__2D__Remote__Algorithm.md)
