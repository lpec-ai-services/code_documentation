<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgsketcher_1_1Polyline2D.html -->

# Polyline2D Class Reference gsketcher - Wrapper to help the creation of simple sketches

An interface to build a 2D polyline step-by-step.
[More...](classgsketcher_1_1Polyline2D.md#details)

## Detailed Description

An interface to build a 2D polyline step-by-step.

The polyline can contain several sections. Each section represents a list of 2d points. As well it has a name, curve type, either polyline or interpolation (BSpline curve) and Closed flag. Use geompy.Polyline2D() method to obtain an instance of this class.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, geompyD)
```

## Member Function Documentation

### addSection()

```python
def addSection(self, theName, theType, theClosed, thePoints = None)
```

Add a new section to the polyline.

Parameters
:   |  |  |
    | --- | --- |
    | theName | the name |
    | theType | the type. It can have either CORBA enumeration type [GEOM.curve_type](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839e) or a value of type long. Possible input values are: GEOM.Polyline(0) and GEOM.Interpolation(2). |
    | theClosed | True for closed section; False otherwise |
    | thePoints | the list of 2D points coordinates in the form: [x1, y1, x2, y2, ..., xN, yN] for N points. |

### addPoints()

```python
def addPoints(self, thePoints)
```

Add a points to the last added section of the polyline.

If there are no sections in the polyline it does nothing.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | the list of 2D points coordinates in the form: [x1, y1, x2, y2, ..., xN, yN] for N points. |

### result()

```python
def result(self, theWorkingPlane = [0, theName = None)
```

Obtain the 2D polyline result as a wire or a compound of wires in case of several sections defined.

Parameters
:   |  |  |
    | --- | --- |
    | theWorkingPlane | - current Working Plane used for this 2D polyline |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created shape.

## Field Documentation

### geompyD

```python
geompyD
```

### myNameList

```python
myNameList
```

### myTypeList

```python
myTypeList
```

### myClosedList

```python
myClosedList
```

### myCoordsList

```python
myCoordsList
```
