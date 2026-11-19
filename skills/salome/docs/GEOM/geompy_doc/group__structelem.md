<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__structelem.html -->

# structelem - Structural elements package

## Detailed Description

This package is used to create and visualize structural elements. It contains three modules:

- This module [salome.geom.structelem](group__structelem.md) defines the main classes [StructuralElement](classstructelem_1_1StructuralElement.md) and [StructuralElementManager](classstructelem_1_1StructuralElementManager.md) that can be directly used to build structural elements.
- The module [salome.geom.structelem.parts](group__parts.md) defines the classes corresponding to the different parts (beams, grids, etc.) that make up a structural element. It is used to build the geometric shapes in the structural element.
- The module [salome.geom.structelem.orientation](group__orientation.md) defines the classes that are used to compute the orientation of the structural element parts and to build the corresponding markers.

A structural element is a set of geometric shapes (beams, grids, etc.) that are built semi-automatically along a set of geometric primitives (edges for instance). They are visualized with the same color as their base primitives in the geom viewer.   
Structural elements are generally created by the [StructuralElementManager](classstructelem_1_1StructuralElementManager.md) class, from a list of commands describing the element to create.

Example:

```python
commandList = [('VisuPoutreGenerale', {'Group_Maille': 'Edge_1'}),
               ('VisuBarreCercle', {'R': 30, 'Group_Maille': 'Edge_1', 'EP': 15}),
              ]

structElemManager = StructuralElementManager()
elem = structElemManager.createElement(commandList)
elem.display()
salome.sg.updateObjBrowser()
```
