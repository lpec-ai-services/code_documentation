<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgeomtools_1_1GeomStudyTools.html -->

# GeomStudyTools Class Reference geomtools - Tools to access GEOM engine and objects

This class provides several methods to manipulate geom objects in Salome study.
[More...](classgeomtools_1_1GeomStudyTools.md#details)

## Detailed Description

This class provides several methods to manipulate geom objects in Salome study.

The parameter *studyEditor* defines a **StudyEditor** object used to access the study. If **None**, the method returns a **StudyEditor** object on the current study.

**editor**   
This instance attribute contains the underlying **StudyEditor** object. It can be used to access the study but the attribute itself should not be modified.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, studyEditor = None)
```

## Member Function Documentation

### addShapeToStudy()

```python
def addShapeToStudy(self, shape, shapeName, folderName = None)
```

Add a [GEOM](namespaceGEOM.md) shape in the study.

It returns the associated entry that corresponds to the identifier of the entry in the study. This entry can be used to retrieve an object in the study. A folderName can be specified. In this case, a folder with this name is first created in the Geometry part of the study, and the shape study object is stored in this folder of the study.

Parameters
:   |  |  |
    | --- | --- |
    | shape | ([GEOM](namespaceGEOM.md) object) the [GEOM](namespaceGEOM.md) object defining the shape |
    | shapeName | (string) the name for this shape in the study |
    | folderName | (string) the name of a folder in the [GEOM](namespaceGEOM.md) part of the study |

### removeFromStudy()

```python
def removeFromStudy(self, shapeStudyEntry)
```

This removes the specified entry from the study.

Note that this operation does not destroy the underlying [GEOM](namespaceGEOM.md) object, neither erase the drawing in the viewer. The underlying [GEOM](namespaceGEOM.md) object is returned (so that it can be destroyed)

### displayShapeByName()

```python
def displayShapeByName(self, shapeName, color = None, fit = True)
```

Display the geometrical shape whose name in the study is *shapeName*.

Parameters
:   |  |  |
    | --- | --- |
    | shapeName | (string) name of the geometrical shape |
    | color | (tuple) RGB components of the color of the shape |

Returns
:   True if the shape was found, False otherwise

### displayShapeByEntry()

```python
def displayShapeByEntry(self, shapeStudyEntry, color = None, fit = True)
```

Display the geometrical shape whose entry is given by *entry*.

You should prefer use this function instead of the [displayShapeByName()](classgeomtools_1_1GeomStudyTools.md#aae75f4a41860daa4876bfed859af1eea) which can have an unpredictable behavior in the case where several objects exist with the same name in the study.

### eraseShapeByEntry()

```python
def eraseShapeByEntry(self, shapeStudyEntry)
```

Erase the geometrical shape whose entry is given by *entry*.

Please note that the shape is just erased from the viewer. The associated study object still exists in the study, and the geom object still exists in the [GEOM](namespaceGEOM.md) engine.

### deleteShape()

```python
def deleteShape(self, shapeStudyEntry)
```

This completely deletes a geom shape.

Warning
:   Please be aware that to delete a geom object, you have three operations to perform:

1. erase the shape from the viewers
2. remove the entry from the study
3. destroy the underlying geom object

### getGeomObjectSelected()

```python
def getGeomObjectSelected(self)
```

Returns the [GEOM](namespaceGEOM.md) object currently selected in the objects browser.

### getGeomObjectFromEntry()

```python
def getGeomObjectFromEntry(self, entry)
```

Returns the [GEOM](namespaceGEOM.md) object associated to the specified entry, (the entry is the identifier of an item in the active study)

## Field Documentation

### editor

```python
editor
```
