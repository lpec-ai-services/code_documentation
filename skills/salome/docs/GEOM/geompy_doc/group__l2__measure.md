<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l2__measure.html -->

# Using measurement tools geomBuilder Python module » All package methods, grouped by their purpose

## Detailed Description

## Function Documentation

### NumberOfFaces()

```python
def NumberOfFaces(self, theShape)
```

Gives quantity of faces in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count faces of. |

Returns
:   Quantity of faces.

[Example](../tui_test_others_page.md#swig_NumberOf)

### NumberOfEdges()

```python
def NumberOfEdges(self, theShape)
```

Gives quantity of edges in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count edges of. |

Returns
:   Quantity of edges.

[Example](../tui_test_others_page.md#swig_NumberOf)

### NumberOfSubShapes()

```python
def NumberOfSubShapes(self, theShape, theShapeType)
```

Gives quantity of sub-shapes of type theShapeType in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count sub-shapes of. |
    | theShapeType | Type of sub-shapes to count (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |

Returns
:   Quantity of sub-shapes of given type.

[Example](../tui_test_others_page.md#swig_NumberOf)

### NumberOfSolids()

```python
def NumberOfSolids(self, theShape)
```

Gives quantity of solids in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count solids in. |

Returns
:   Quantity of solids.

[Example](../tui_test_others_page.md#swig_NumberOf)

### PointCoordinates()

```python
def PointCoordinates(self, Point)
```

Get point coordinates.

Returns
:   [x, y, z]

[Example](../tui_point_coordinates_page.md)

### VectorCoordinates()

```python
def VectorCoordinates(self, Vector)
```

Get vector coordinates.

Returns
:   [x, y, z]

[Example](../tui_measurement_tools_page.md)

### CrossProduct()

```python
def CrossProduct(self, Vector1, Vector2)
```

Compute cross product.

Returns
:   vector w=u^v

[Example](../tui_measurement_tools_page.md)

### DotProduct()

```python
def DotProduct(self, Vector1, Vector2)
```

Compute cross product.

Returns
:   dot product p=u.v

[Example](../tui_measurement_tools_page.md)

### BasicProperties()

```python
def BasicProperties(self, theShape, theTolerance = 1.e-6)
```

Get summarized length of all wires, area of surface and volume of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to define properties of. |
    | theTolerance | maximal relative error of area and volume computation. |

Returns
:   [theLength, theSurfArea, theVolume]  
    theLength: Summarized length of all wires of the given shape.  
    theSurfArea: Area of surface of the given shape.  
    theVolume: Volume of the given shape.

[Example](../tui_basic_properties_page.md)

### BoundingBox()

```python
def BoundingBox(self, theShape, precise = False)
```

Get parameters of bounding box of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to obtain bounding box of. |
    | precise | TRUE for precise computation; FALSE for fast one. |

Returns
:   [Xmin,Xmax, Ymin,Ymax, Zmin,Zmax] Xmin,Xmax: Limits of shape along OX axis. Ymin,Ymax: Limits of shape along OY axis. Zmin,Zmax: Limits of shape along OZ axis.

[Example](../tui_bounding_box_page.md)

### MakeBoundingBox()

```python
def MakeBoundingBox(self, theShape, precise = False, theName = None)
```

Get bounding box of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to obtain bounding box of. |
    | precise | TRUE for precise computation; FALSE for fast one. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

[Example](../tui_bounding_box_page.md)

### Inertia()

```python
def Inertia(self, theShape)
```

Get inertia matrix and moments of inertia of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to calculate inertia of. |

Returns
:   [I11,I12,I13, I21,I22,I23, I31,I32,I33, Ix,Iy,Iz] I(1-3)(1-3): Components of the inertia matrix of the given shape. Ix,Iy,Iz: Moments of inertia of the given shape.

[Example](../tui_inertia_page.md)

### AreCoordsInside()

```python
def AreCoordsInside(self, theShape, coords, tolerance = 1.e-7)
```

Get if coords are included in the shape (ST_IN or ST_ON)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape |
    | coords | list of points coordinates [x1, y1, z1, x2, y2, z2, ...] |
    | tolerance | to be used (default is 1.0e-7) |

Returns
:   list_of_boolean = [res1, res2, ...]

### MinDistance()

```python
def MinDistance(self, theShape1, theShape2)
```

Get minimal distance between the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find minimal distance between. |

Returns
:   Value of the minimal distance between the given shapes.

[Example](../tui_min_distance_page.md)

### MinDistanceComponents()

```python
def MinDistanceComponents(self, theShape1, theShape2)
```

Get minimal distance between the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find minimal distance between. |

Returns
:   Value of the minimal distance between the given shapes, in form of list [Distance, DX, DY, DZ].

[Example](../tui_min_distance_page.md)

### ClosestPoints()

```python
def ClosestPoints(self, theShape1, theShape2)
```

Get closest points of the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find closest points of. |

Returns
:   The number of found solutions (-1 in case of infinite number of solutions) and a list of (X, Y, Z) coordinates for all couples of points.

[Example](../tui_min_distance_page.md)

### GetAngle()

```python
def GetAngle(self, theShape1, theShape2)
```

Get angle between the given shapes in degrees.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Lines or linear edges to find angle between. |

Note
:   If both arguments are vectors, the angle is computed in accordance with their orientations, otherwise the minimum angle is computed.

Returns
:   Value of the angle between the given shapes in degrees.

[Example](../tui_angle_page.md)

### GetAngleRadians()

```python
def GetAngleRadians(self, theShape1, theShape2)
```

Get angle between the given shapes in radians.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Lines or linear edges to find angle between. |

Note
:   If both arguments are vectors, the angle is computed in accordance with their orientations, otherwise the minimum angle is computed.

Returns
:   Value of the angle between the given shapes in radians.

[Example](../tui_angle_page.md)

### GetAngleVectors()

```python
def GetAngleVectors(self, theShape1, theShape2, theFlag = True)
```

Get angle between the given vectors in degrees.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Vectors to find angle between. |
    | theFlag | If True, the normal vector is defined by the two vectors cross, if False, the opposite vector to the normal vector is used. |

Returns
:   Value of the angle between the given vectors in degrees.

[Example](../tui_angle_page.md)

### GetAngleRadiansVectors()

```python
def GetAngleRadiansVectors(self, theShape1, theShape2, theFlag = True)
```

The same as GetAngleVectors, but the result is in radians.

### CurveCurvatureByParam()

```python
def CurveCurvatureByParam(self, theCurve, theParam)
```

Measure curvature of a curve at a point, set by parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theCurve | a curve. |
    | theParam | parameter. |

Returns
:   radius of curvature of *theCurve*.

Example

### CurveCurvatureByPoint()

```python
def CurveCurvatureByPoint(self, theCurve, thePoint)
```

Measure curvature of a curve at a point.

Parameters
:   |  |  |
    | --- | --- |
    | theCurve | a curve. |
    | thePoint | given point. |

Returns
:   radius of curvature of *theCurve*.

Example

### MaxSurfaceCurvatureByParam()

```python
def MaxSurfaceCurvatureByParam(self, theSurf, theUParam, theVParam)
```

Measure max radius of curvature of surface.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given surface. |
    | theUParam | Value of U-parameter on the referenced surface. |
    | theVParam | Value of V-parameter on the referenced surface. |

Returns
:   max radius of curvature of theSurf.

Example

### MaxSurfaceCurvatureByPoint()

```python
def MaxSurfaceCurvatureByPoint(self, theSurf, thePoint)
```

Measure max radius of curvature of surface in the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given surface. |
    | thePoint | given point. |

Returns
:   max radius of curvature of theSurf.

Example

### MinSurfaceCurvatureByParam()

```python
def MinSurfaceCurvatureByParam(self, theSurf, theUParam, theVParam)
```

Measure min radius of curvature of surface.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given surface. |
    | theUParam | Value of U-parameter on the referenced surface. |
    | theVParam | Value of V-parameter on the referenced surface. |

Returns
:   min radius of curvature of theSurf.

Example

### MinSurfaceCurvatureByPoint()

```python
def MinSurfaceCurvatureByPoint(self, theSurf, thePoint)
```

Measure min radius of curvature of surface in the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given surface. |
    | thePoint | given point. |

Returns
:   min radius of curvature of theSurf.

Example

### CurvatureOnFace()

```python
def CurvatureOnFace(self, theSurf, thePoint, theDirection, theName = None)
```

Measure curvature radius of surface in the given point along the given direction.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given face. |
    | thePoint | given point. |
    | theDirection | given direction. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing vector of curvature of theSurf. The returned vector is codirectional with the normal to the face in the given point in case of positive curvature value and opposite to the normal in case of negative curvature. The normal of the returned vector is equal to the absolute value of the curvature radius. Null shape is returned in case of infinite radius (zero curvature), for example, in case of flat face.

[Example](../tui_test_all_page.md#swig_CurvatureOnFace)

### XYZtoUV()

```python
def XYZtoUV(self, theSurf, theXYZlist, theIsNormalized = True)
```

Convert X,Y,Z points coordinates to UV parameters on the given surface.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given face. It can be also a shell or a compound with one face. |
    | theXYZlist | float list of size 3*N where N is the number of points for which we want their U,V coordinates. If the user enters a list of size not divisible by 3 an exception will be thrown. |
    | theIsNormalized | if True, the returned parameters will be in range [0, 1]. |

Returns
:   list of float of size 2*N.

[Example](../tui_xyz_to_uv_page.md)

### UVtoXYZ()

```python
def UVtoXYZ(self, theSurf, theUVlist, theIsNormalized = True)
```

Convert UV parameters on the given surface to 3D points coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given face. It can be also a shell or a compound with one face. |
    | theUVlist | float list of size 2*N where N is the number of points for which we want their X,Y,Z coordinates. If the user enters a list of non-even size an exception will be thrown. |
    | theIsNormalized | if True, the input parameters are expected to be in range [0, 1]. |

Returns
:   list of float of size 3*N.

[Example](../tui_xyz_to_uv_page.md)

### Tolerance()

```python
def Tolerance(self, theShape)
```

Get min and max tolerances of sub-shapes of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to get tolerances of. |

Returns
:   [FaceMin,FaceMax, EdgeMin,EdgeMax, VertMin,VertMax]  
    FaceMin,FaceMax: Min and max tolerances of the faces.  
    EdgeMin,EdgeMax: Min and max tolerances of the edges.  
    VertMin,VertMax: Min and max tolerances of the vertices.

[Example](../tui_tolerance_page.md)

### WhatIs()

```python
def WhatIs(self, theShape)
```

Obtain description of the given shape (number of sub-shapes of each type)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be described. |

Returns
:   Description of the given shape.

[Example](../tui_whatis_page.md)

### NbShapes()

```python
def NbShapes(self, theShape, theType)
```

Obtain quantity of shapes of the given type in *theShape*.

If *theShape* is of type *theType*, it is also counted.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be described. |
    | theType | the given [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82). |

Returns
:   Quantity of shapes of type *theType* in *theShape*.

[Example](../tui_measurement_tools_page.md)

### ShapeInfo()

```python
def ShapeInfo(self, theShape)
```

Obtain quantity of shapes of each type in *theShape*.

The *theShape* is also counted.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be described. |

Returns
:   Dictionary of [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82) with bound quantities of shapes.

[Example](../tui_measurement_tools_page.md)

### GetCreationInformation()

```python
def GetCreationInformation(self, theShape)
```

### MakeCDG()

```python
def MakeCDG(self, theShape, theName = None)
```

Get a point, situated at the centre of mass of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to define centre of mass of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_center_of_mass_page.md)

### GetVertexByIndex()

```python
def GetVertexByIndex(self, theShape, theIndex, theUseOri = True, theName = None)
```

Get a vertex sub-shape by index.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shape. |
    | theIndex | Index to find vertex by this index (starting from zero) |
    | theUseOri | To consider edge/wire orientation or not |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vertex.

[Example](../tui_measurement_tools_page.md)

### GetFirstVertex()

```python
def GetFirstVertex(self, theShape, theName = None)
```

Get the first vertex of wire/edge depended orientation.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find first vertex. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vertex.

[Example](../tui_measurement_tools_page.md)

### GetLastVertex()

```python
def GetLastVertex(self, theShape, theName = None)
```

Get the last vertex of wire/edge depended orientation.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find last vertex. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vertex.

[Example](../tui_measurement_tools_page.md)

### GetNormal()

```python
def GetNormal(self, theFace, theOptionalPoint = None, theName = None)
```

Get a normale to the given face.

If the point is not given, the normale is calculated at the center of mass.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | Face to define normale of. |
    | theOptionalPoint | Point to compute the normale at. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vector.

Example

### PrintShapeErrors()

```python
def PrintShapeErrors(self, theShape, theShapeErrors, theReturnStatus = 0)
```

Print shape errors obtained from CheckShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape that was checked. |
    | theShapeErrors | the shape errors obtained by CheckShape. |
    | theReturnStatus | If 0 the description of problem is printed. If 1 the description of problem is returned. |

Returns
:   If theReturnStatus is equal to 1 the description is returned. Otherwise doesn't return anything.

[Example](../tui_check_shape_page.md)

### CheckShape()

```python
def CheckShape(self, theShape, theIsCheckGeom = False, theReturnStatus = 0, theIsExact = False)
```

Check a topology of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theIsCheckGeom | If FALSE, only the shape's topology will be checked,   if TRUE, the shape's geometry will be checked also. |
    | theReturnStatus | It can be one of [-1, 0, 1, 2]. Regulates the return value and output of the function. |
    | theIsExact | If TRUE, take into account exact tolerance of edges. It can take more time. Exact tolerance can be greater than the approximate one, which is calculated only in some points of edge. |

Returns
:   (isValid [, Description or ErrorDataList]) where isValid is TRUE, if the shape "seems to be valid". If theReturnStatus is equal to -1, returns IsValid flag only. If theReturnStatus is equal to 0 (default), returns IsValid flag only, but additionally prints a problem description, if theShape is invalid. If theReturnStatus is equal to 1, the description string is returned along with IsValid flag. If theReturnStatus is equal to 2, the list of error data is returned along with IsValid flag.

[Example](../tui_check_shape_page.md)

### CheckSelfIntersections()

```python
def CheckSelfIntersections(self, theShape, theCheckLevel = GEOM.SI_ALL)
```

Detect self-intersections in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check. |
    | theCheckLevel | is the level of self-intersection check. Possible input values are:  - GEOM.SI_V_V(0) - only V/V interferences - GEOM.SI_V_E(1) - V/V and V/E interferences - GEOM.SI_E_E(2) - V/V, V/E and E/E interferences - GEOM.SI_V_F(3) - V/V, V/E, E/E and V/F interferences - GEOM.SI_E_F(4) - V/V, V/E, E/E, V/F and E/F interferences - GEOM.SI_ALL(5) - all interferences. |

Returns
:   TRUE, if the shape contains no self-intersections.

[Example](../tui_check_self_intersections_page.md)

### CheckSelfIntersectionsFast()

```python
def CheckSelfIntersectionsFast(self, theShape, theDeflection = 0.001, theTolerance = 0.0)
```

Detect self-intersections of the given shape with algorithm based on mesh intersections.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check. |
    | theDeflection | Linear deflection coefficient that specifies quality of tessellation:  - if *theDeflection* <= 0, default deflection 0.001 is used |
    | theTolerance | Specifies a distance between sub-shapes used for detecting gaps:  - if *theTolerance* <= 0, algorithm detects intersections (default behavior) - if *theTolerance* > 0, algorithm detects gaps |

Returns
:   TRUE, if the shape contains no self-intersections.

[Example](../tui_check_self_intersections_fast_page.md)

### CheckBOPArguments()

```python
def CheckBOPArguments(self, theShape)
```

Check boolean and partition operations arguments.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the argument of an operation to be checked |

Returns
:   TRUE if the argument is valid for a boolean or partition operation; FALSE otherwise.

### ExtractBOPFailure()

```python
def ExtractBOPFailure(self, theShapes, theTimer = False, theTopo = False, theParallel = False, theExact = False, theVerbose = False, theName = None)
```

Performs general fuse BOP on the given list of shapes and extracts CheckShape information from its invalid result.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | List of shapes for the BOP. |
    | theTimer | If True, the execution time of the operation is measured. |
    | theTopo | If True, only the topological entities will be checked. |
    | theParallel | If True, the operation will be executed in parallel. |
    | theExact | If True, an exact check will be performed. |
    | theVerbose | If True, prints execution errors and resulting shape errors. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   (isValid, shapeResult, listOfErrors), where isValid - a boolean value (whether result shape is valid or not), shapeResult - the result shape itself as GEOM::Object, listOfErrors - the list of [GEOM.GEOM_IMeasureOperations.ShapeError](structGEOM_1_1GEOM__IMeasureOperations_1_1ShapeError.md).

### FastIntersect()

```python
def FastIntersect(self, theShape1, theShape2, theTolerance = 0.0, theDeflection = 0.001)
```

Detect intersections of the given shapes with algorithm based on mesh intersections.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First source object |
    | theShape2 | Second source object |
    | theTolerance | Specifies a distance between shapes used for detecting gaps:  - if *theTolerance* <= 0, algorithm detects intersections (default behavior) - if *theTolerance* > 0, algorithm detects gaps |
    | theDeflection | Linear deflection coefficient that specifies quality of tessellation:  - if *theDeflection* <= 0, default deflection 0.001 is used |

Returns
:   TRUE, if there are intersections (gaps) between source shapes
:   List of sub-shapes IDs from 1st shape that localize intersection.
:   List of sub-shapes IDs from 2nd shape that localize intersection.

[Example](../tui_fast_intersection_page.md)

### GetPosition()

```python
def GetPosition(self, theShape)
```

Get position (LCS) of theShape.

Origin of the LCS is situated at the shape's center of mass. Axes of the LCS are obtained from shape's location or, if the shape is a planar face, from position of its plane.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to calculate position of. |

Returns
:   [Ox,Oy,Oz, Zx,Zy,Zz, Xx,Xy,Xz]. Ox,Oy,Oz: Coordinates of shape's LCS origin. Zx,Zy,Zz: Coordinates of shape's LCS normal(main) direction. Xx,Xy,Xz: Coordinates of shape's LCS X direction.

Example

### KindOfShape()

```python
def KindOfShape(self, theShape)
```

Get kind of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to get a kind of. |

Returns
:   Returns a kind of shape in terms of *[GEOM.GEOM_IKindOfShape.shape_kind](interfaceGEOM_1_1GEOM__IKindOfShape.md#a89b3365676a2806c547d5bc9bf4d9d7c)* enumeration and a list of parameters, describing the shape.

Note
:   Concrete meaning of each value, returned via *theIntegers* or *theDoubles* list depends on the [kind()](group__l1__geomBuilder__auxiliary.md#gaaf25ee7e2306d78c74ec7bc48f092e81) of the shape.

Example

### PatchFace()

```python
def PatchFace(self, theShape)
```

The function takes a single face with holes and returns a list of faces, first of them is the original face without holes, and the other faces are placed on the same surface as the original face but bounded by each hole wire.

If the original face has no holes, it will be returned as an output

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Face to perform operation on. |

Returns
:   [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067), list created faces, where first of them is the original face without holes

### _IsGoodForSolid()

```python
def _IsGoodForSolid(self, theShell) private
```

Returns the string that describes if the shell is good for solid.

This is a support method for MakeSolid.

Parameters
:   |  |  |
    | --- | --- |
    | theShell | the shell to be checked. |

Returns
:   Returns a string that describes the shell validity for solid construction.

### CanonicalRecognition()

```python
def CanonicalRecognition(self)
```

Obtain a canonical recognition interface.

Returns
:   An instance of CanonicalRecognition interface

[Example](../tui_3dsketcher_page.md)
