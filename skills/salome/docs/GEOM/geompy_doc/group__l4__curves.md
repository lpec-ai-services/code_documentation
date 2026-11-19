<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__curves.html -->

# Creating Curves geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Creating Basic Geometric Objects

## Detailed Description

## Function Documentation

### MakeArc()

```python
def MakeArc(self, thePnt1, thePnt2, thePnt3, theName = None)
```

Create an arc of circle, passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Start point of the arc. |
    | thePnt2 | Middle point of the arc. |
    | thePnt3 | End point of the arc. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

[Example](../tui_test_all_page.md#swig_MakeArc)

### MakeArcCenter()

```python
def MakeArcCenter(self, thePnt1, thePnt2, thePnt3, theSense = False, theName = None)
```

Create an arc of circle from a center and 2 points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Center of the arc |
    | thePnt2 | Start point of the arc. (Gives also the radius of the arc) |
    | thePnt3 | End point of the arc (Gives also a direction) |
    | theSense | Orientation of the arc |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

[Example](../tui_test_all_page.md#swig_MakeArc)

### MakeArcOfEllipse()

```python
def MakeArcOfEllipse(self, theCenter, thePnt1, thePnt2, theName = None)
```

Create an arc of ellipse, of center and two points.

Parameters
:   |  |  |
    | --- | --- |
    | theCenter | Center of the arc. |
    | thePnt1 | defines major radius of the arc by distance from Pnt1 to Pnt2. |
    | thePnt2 | defines plane of ellipse and minor radius as distance from Pnt3 to line from Pnt1 to Pnt2. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

[Example](../tui_test_all_page.md#swig_MakeArc)

### MakeCircle()

```python
def MakeCircle(self, thePnt, theVec, theR, theName = None)
```

Create a circle with given center, normal vector and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Circle center. |
    | theVec | Vector, normal to the plane of the circle. |
    | theR | Circle radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

[Example](../tui_basic_geom_objs_page.md#tui_creation_circle)

### MakeCircleR()

```python
def MakeCircleR(self, theR, theName = None)
```

Create a circle with given radius.

Center of the circle will be in the origin of global coordinate system and normal vector will be codirected with Z axis

Parameters
:   |  |  |
    | --- | --- |
    | theR | Circle radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

### MakeCircleThreePnt()

```python
def MakeCircleThreePnt(self, thePnt1, thePnt2, thePnt3, theName = None)
```

Create a circle, passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the circle. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

[Example](../tui_basic_geom_objs_page.md#tui_creation_circle)

### MakeCircleCenter2Pnt()

```python
def MakeCircleCenter2Pnt(self, thePnt1, thePnt2, thePnt3, theName = None)
```

Create a circle, with given point1 as center, passing through the point2 as radius and laying in the plane, defined by all three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the circle. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

[Example](../tui_test_all_page.md#swig_MakeCircle)

### MakeEllipse()

```python
def MakeEllipse(self, thePnt, theVec, theRMajor, theRMinor, theVecMaj = None, theName = None)
```

Create an ellipse with given center, normal vector and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Ellipse center. |
    | theVec | Vector, normal to the plane of the ellipse. |
    | theRMajor | Major ellipse radius. |
    | theRMinor | Minor ellipse radius. |
    | theVecMaj | Vector, direction of the ellipse's main axis. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created ellipse.

[Example](../tui_basic_geom_objs_page.md#tui_creation_ellipse)

### MakeEllipseRR()

```python
def MakeEllipseRR(self, theRMajor, theRMinor, theName = None)
```

Create an ellipse with given radiuses.

Center of the ellipse will be in the origin of global coordinate system and normal vector will be codirected with Z axis

Parameters
:   |  |  |
    | --- | --- |
    | theRMajor | Major ellipse radius. |
    | theRMinor | Minor ellipse radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created ellipse.

### MakePolyline()

```python
def MakePolyline(self, thePoints, theIsClosed = False, theName = None)
```

Create a polyline on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the polyline. |
    | theIsClosed | If True, build a closed wire. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created polyline.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)

### MakeBezier()

```python
def MakeBezier(self, thePoints, theIsClosed = False, theName = None)
```

Create bezier curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the bezier curve. |
    | theIsClosed | If True, build a closed curve. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created bezier curve.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)

### MakeInterpol()

```python
def MakeInterpol(self, thePoints, theIsClosed = False, theDoReordering = False, theName = None)
```

Create B-Spline curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the B-Spline curve. |
    | theIsClosed | If True, build a closed curve. |
    | theDoReordering | If TRUE, the algo does not follow the order of *thePoints* but searches for the closest vertex. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created B-Spline curve.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)

### MakeInterpolWithTangents()

```python
def MakeInterpolWithTangents(self, thePoints, theFirstVec, theLastVec, theName = None)
```

Create B-Spline curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the B-Spline curve. |
    | theFirstVec | Vector object, defining the curve direction at its first point. |
    | theLastVec | Vector object, defining the curve direction at its last point. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created B-Spline curve.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)

### MakeCurveParametric()

```python
def MakeCurveParametric(self, thexExpr, theyExpr, thezExpr, theParamMin, theParamMax, theParamStep, theCurveType, theNewMethod = False, theName = None)
```

Creates a curve using the parametric definition of the basic points.

Parameters
:   |  |  |
    | --- | --- |
    | thexExpr | parametric equation of the coordinates X. |
    | theyExpr | parametric equation of the coordinates Y. |
    | thezExpr | parametric equation of the coordinates Z. |
    | theParamMin | the minimal value of the parameter. |
    | theParamMax | the maximum value of the parameter. |
    | theParamStep | the number of steps if theNewMethod = True, else step value of the parameter. |
    | theCurveType | the type of the curve, one of [GEOM.Polyline](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839ead2644bf3c6a9f629a4ef9748db433513), [GEOM.Bezier](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839ea07611b73b23eebb936a8c018fe2dc80e), [GEOM.Interpolation](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839eaec0e6acb2e6b6dca1c92c50c2a762470). |
    | theNewMethod | flag for switching to the new method if the flag is set to false a deprecated method is used which can lead to a bug. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created curve.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)

### MakeIsoline()

```python
def MakeIsoline(self, theFace, IsUIsoline, theParameter, theName = None)
```

Create an isoline curve on a face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the face for which an isoline is created. |
    | IsUIsoline | True for U-isoline creation; False for V-isoline creation. |
    | theParameter | the U parameter for U-isoline or V parameter for V-isoline. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created isoline edge or a compound of edges.

[Example](../tui_basic_geom_objs_page.md#tui_creation_curve)
