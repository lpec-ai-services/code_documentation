<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__blocks__measure.html -->

# Check and Improve geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Building by blocks

## Detailed Description

## Function Documentation

### CheckCompoundOfBlocks()

```python
def CheckCompoundOfBlocks(self, theCompound, theIsUseC1 = False, theAngTolerance = 1.e-12)
```

Check, if the compound of blocks is given.

To be considered as a compound of blocks, the given shape must satisfy the following conditions:

- Each element of the compound should be a Block (6 faces).
- Each face should be a quadrangle, i.e. it should have only 1 wire with 4 edges. If *theIsUseC1* is set to True and there are more than 4 edges in the only wire of a face, this face is considered to be quadrangle if it has 4 bounds (1 or more edge) of C1 continuity.
- A connection between two Blocks should be an entire quadrangle face or an entire edge.
- The compound should be connexe.
- The glue between two quadrangle faces should be applied.

  Parameters
  :   |  |  |
      | --- | --- |
      | theCompound | The compound to check. |
      | theIsUseC1 | Flag to check if there are 4 bounds on a face taking into account C1 continuity. |
      | theAngTolerance | the angular tolerance to check if two neighbor edges are codirectional in the common vertex with this tolerance. This parameter is used only if *theIsUseC1* is set to True. |

  Returns
  :   TRUE, if the given shape is a compound of blocks. If theCompound is not valid, prints all discovered errors.

  [Example 1](../tui_check_compound_of_blocks_page.md)   
  [Example 2](../tui_test_others_page.md#swig_CheckCompoundOfBlocks)

### GetNonBlocks()

```python
def GetNonBlocks(self, theShape, theIsUseC1 = False, theAngTolerance = 1.e-12, theName = None)
```

Retrieve all non blocks solids and faces from *theShape*.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The shape to explore. |
    | theIsUseC1 | Flag to check if there are 4 bounds on a face taking into account C1 continuity. |
    | theAngTolerance | the angular tolerance to check if two neighbor edges are codirectional in the common vertex with this tolerance. This parameter is used only if *theIsUseC1* is set to True. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   A tuple of two GEOM_Objects. The first object is a group of all non block solids (= not 6 faces, or with 6 faces, but with the presence of non-quadrangular faces). The second object is a group of all non quadrangular faces (= faces with more then 1 wire or, if *theIsUseC1* is set to True, faces with 1 wire with not 4 edges that do not form 4 bounds of C1 continuity).

[Example 1](../tui_get_non_blocks_page.md)   
[Example 2](../tui_test_spanner_page.md#swig_GetNonBlocks)

### RemoveExtraEdges()

```python
def RemoveExtraEdges(self, theShape, doUnionFaces = False, theName = None)
```

Remove all seam and degenerated edges from *theShape*.

Unite faces and edges, sharing one surface. It means that this faces must have references to one C++ surface object (handle).

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The compound or single solid to remove irregular edges from. |
    | doUnionFaces | If True, then unite faces. If False (the default value), do not unite faces. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Improved shape.

[Example](../tui_test_others_page.md#swig_RemoveExtraEdges)

### UnionFaces()

```python
def UnionFaces(self, theShape, theName = None)
```

Performs union faces of *theShape* Unite faces sharing one surface.

It means that these faces must have references to one C++ surface object (handle).

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The compound or single solid that contains faces to perform union. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Improved shape.

[Example](../tui_test_others_page.md#swig_UnionFaces)

### CheckAndImprove()

```python
def CheckAndImprove(self, theShape, theName = None)
```

Check, if the given shape is a blocks compound.

Fix all detected errors.

Note
:   Single block can be also fixed by this method.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The compound to check and improve. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Improved compound.

[Example](../tui_test_others_page.md#swig_CheckAndImprove)
