<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__blocks.html -->

# Building by blocks geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### MakeQuad()

```python
def MakeQuad(self, E1, E2, E3, E4, theName = None)
```

Create a quadrangle face from four edges.

Order of Edges is not important. It is not necessary that edges share the same vertex.

Parameters
:   |  |  |
    | --- | --- |
    | E1,E2,E3,E4 | Edges for the face bound. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_building_by_blocks_page.md)

### MakeQuad2Edges()

```python
def MakeQuad2Edges(self, E1, E2, theName = None)
```

Create a quadrangle face on two edges.

The missing edges will be built by creating the shortest ones.

Parameters
:   |  |  |
    | --- | --- |
    | E1,E2 | Two opposite edges for the face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_building_by_blocks_page.md)

### MakeQuad4Vertices()

```python
def MakeQuad4Vertices(self, V1, V2, V3, V4, theName = None)
```

Create a quadrangle face with specified corners.

The missing edges will be built by creating the shortest ones.

Parameters
:   |  |  |
    | --- | --- |
    | V1,V2,V3,V4 | Corner vertices for the face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example 1](../tui_building_by_blocks_page.md)   
[Example 2](../tui_test_spanner_page.md#swig_MakeQuad4Vertices)

### MakeHexa()

```python
def MakeHexa(self, F1, F2, F3, F4, F5, F6, theName = None)
```

Create a hexahedral solid, bounded by the six given faces.

Order of faces is not important. It is not necessary that Faces share the same edge.

Parameters
:   |  |  |
    | --- | --- |
    | F1,F2,F3,F4,F5,F6 | Faces for the hexahedral solid. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

[Example 1](../tui_building_by_blocks_page.md)   
[Example 2](../tui_test_spanner_page.md#swig_MakeHexa)

### MakeHexa2Faces()

```python
def MakeHexa2Faces(self, F1, F2, theName = None)
```

Create a hexahedral solid between two given faces.

The missing faces will be built by creating the smallest ones.

Parameters
:   |  |  |
    | --- | --- |
    | F1,F2 | Two opposite faces for the hexahedral solid. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

[Example 1](../tui_building_by_blocks_page.md)   
[Example 2](../tui_test_spanner_page.md#swig_MakeHexa2Faces)
