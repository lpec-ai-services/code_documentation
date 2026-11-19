<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classstructelem_1_1StructuralElement.html -->

# StructuralElement Class Reference structelem - Structural elements package

This class represents a structural element, i.e.
[More...](classstructelem_1_1StructuralElement.md#details)

## Detailed Description

This class represents a structural element, i.e.

a set of geometrical objects built along geometrical primitives. Structural elements are normally created by the class [StructuralElementManager](classstructelem_1_1StructuralElementManager.md), so this class should not be instantiated directly in the general case.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self)
```

## Member Function Documentation

### _getSObject()

```python
def _getSObject(self) private
```

Find or create the study object corresponding to the structural element.

This object is a Geom Folder named "SE_N" where N is a numerical ID.

### addPart()

```python
def addPart(self, newpart)
```

Add a part to the structural element.

Parameters
:   |  |  |
    | --- | --- |
    | newpart | (StructuralElementPart) the part to add to the structural element. |

### addOrientation()

```python
def addOrientation(self, meshGroup, orientParams)
```

Add orientation information to a part in the structural element.

This information will be used to build the corresponding markers.

Parameters
:   |  |  |
    | --- | --- |
    | meshGroup | (string) the name of a geometrical primitive. The orientation information will apply to the structural element part built along this primitive. |
    | orientParams | (dictionary) parameters defining the orientation of the structural element part. Those parameters are detailed in class [orientation.Orientation1D](classorientation_1_1Orientation1D.md). |

### build()

```python
def build(self)
```

Build the geometric shapes and the markers corresponding to the different parts of the structural element, and add them to the study.

### display()

```python
def display(self)
```

Display the structural element in the geom view.

### showElement()

```python
def showElement(theSObject) static
```

Display the structural element corresponding to the study object **theSObject**.

## Field Documentation

### _counter

```python
int _counter = 1 static private
```

### MAIN_FOLDER_NAME

```python
string MAIN_FOLDER_NAME = "Structural Elements" static
```

### _parts

```python
_parts private
```

### _shapeDict

```python
_shapeDict private
```

### _id

```python
_id private
```

### _studyEditor

```python
_studyEditor private
```

### _SObject

```python
_SObject private
```
