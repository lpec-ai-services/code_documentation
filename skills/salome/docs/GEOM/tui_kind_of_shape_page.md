<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_kind_of_shape_page.html -->

# Get information about a shape

```python
# Sample: KindOfShape method for Edges

import salome
from inspect import getfile
from os.path import abspath, dirname, join
salome.salome_init_without_session()
import GEOM

from salome.geom import geomBuilder
geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(50, 100, 0)
Vertex_3 = geompy.MakeVertex(-10, 60, 0)
Vertex_4 = geompy.MakeVertex(0, 100, 0)
Vertex_5 = geompy.MakeVertex(-100, 100, 0)
Vertex_6 = geompy.MakeVertex(-100, 0, 0)
Vertex_7 = geompy.MakeVertex(-200, 0, 0)
Vertex_8 = geompy.MakeVertex(-200, 100, 0)

# create some curves
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Circle_1 = geompy.MakeCircle(Vertex_2, OZ, 50)
Ellipse_1 = geompy.MakeEllipse(Vertex_1, OZ, 200, 100, Line_1)
Arc_1 = geompy.MakeArc(Vertex_2, Vertex_3, Vertex_1)
Curve_1 = geompy.MakeCurveParametric("t", "50*sin(t)", "0", 0, 360, 30, GEOM.Interpolation, True)
Curve_2 = geompy.MakeCurveParametric("-t", "50*cos(t)", "t", 0, 360, 14, GEOM.Bezier, True)
Curve_5 = geompy.MakeInterpol([Vertex_1, Vertex_4, Vertex_5, Vertex_6, Vertex_7, Vertex_8], False, False)
Curve_7 = geompy.MakeBezier([Vertex_5, Vertex_6, Vertex_7, Vertex_8], True)
Curve_8 = geompy.MakeBezier([Vertex_5, Vertex_6, Vertex_1, Vertex_4], False)

# show information for all curves
props = geompy.KindOfShape(Line_1)
print("KindOfShape(Line_1): ", props)
# [SEGMENT, 0.,0.,0., 50.,100.,0.]
props = geompy.KindOfShape(Circle_1)
print("KindOfShape(Circle_1): ", props)
# [CIRCLE, 50.,100.,0., 0.,0.,1., 50.]
props = geompy.KindOfShape(Ellipse_1)
print("KindOfShape(Ellipse_1): ", props)
# [ELLIPSE, 0.,0.,0., 0.,0.,1., 200., 100., 0.44721,0.89443,0., 0.44721,0.89443,0.]
props = geompy.KindOfShape(Arc_1)
print("KindOfShape(Arc_1): ", props)
# [ARC_CIRCLE, 47.5,38.75,0., 0.,0.,1., 61.301, 50.,100.,0., 0.,0.,0.]
props = geompy.KindOfShape(Curve_1)
print("KindOfShape(Curve_1): ", props)
# [CRV_BSPLINE, 0, 3, 33, 31, 0, 31, 0.,0.,0.,..., 4,1,...,1,4]
props = geompy.KindOfShape(Curve_2)
print("KindOfShape(Curve_2): ", props)
# [CRV_BEZIER, 15, 0, 0.,50.,0.,...,-360.,-14.18455,360.]
props = geompy.KindOfShape(Curve_5)
print("KindOfShape(Curve_5): ", props)
# [CRV_BSPLINE, 0, 3, 8, 6, 0, 6, 0.,0.,0.,..., 100.,0.,0.,100.,200.,300.,400.,500., 4,1,1,1,1,4]
props = geompy.KindOfShape(Curve_7)
print("KindOfShape(Curve_7): ", props)
# [CRV_BEZIER, 5, 0, -100.,100.,0., -100.,0.,0., -200.,0.,0., -200.,100.,0., -100.,100.,0.]
props = geompy.KindOfShape(Curve_8)
print("KindOfShape(Curve_8): ", props)
# [CRV_BEZIER, 4, 0, -100.,100.,0., -100.,0.,0., 0.,0.,0., 0.,100.,0.]
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/kind_of_shape.py)

```python
# Sample: KindOfShape method for faces, which are results of partitioning of a conical surface with a prism with complex base.
# Faces of the prism are not perpendicular to cone axis, therefore contour-wires of resulting cone fragments are composed of lines and 2-order curves.

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

def approximatelyEqual(a, b, epsilon = 1e-5):
 return abs(a - b) <= ((abs(b) if (abs(a) < abs(b)) else abs(a)) * epsilon)

def assertShapeKindEquals(iShapeInfo, iKind):
 assert (len(iShapeInfo) > 0), "Yielded data array is empty."
 assert (iShapeInfo[0] == iKind), f"Expected shape kind is {iKind}, but yielded kind is {iShapeInfo[0]}."

def assertConePropsEqual(iShapeName, iShapeInfo, iExpectedShapeInfo):
   assertShapeKindEquals(iShapeInfo, geompy.kind.CONE2D)
 assert (len(iShapeInfo) == len(iExpectedShapeInfo)), f"{iShapeName}: Yielded data array is of unexpected length."
 for idx in range(1, len(iShapeInfo)):
 assert (approximatelyEqual(iShapeInfo[idx], iExpectedShapeInfo[idx])), f"{iShapeName}: Yielded data array element is not equal to the expected value."

def assertConeInfoEquals(iFace, iExpectedShapeInfo, iAddRestoredConeToStudy = False):
  ShapeInfo = geompy.KindOfShape(iFace)
  print("ShapeInfo of " + iFace.GetName() + " = ", end = "")
  print(ShapeInfo, ', ')
  assertConePropsEqual(iFace.GetName(), ShapeInfo, iExpectedShapeInfo)

 if (iAddRestoredConeToStudy):
    BottomLidCenter = geompy.MakeVertex(ShapeInfo[1], ShapeInfo[2], ShapeInfo[3])
    AxisAuxPnt = geompy.MakeVertex(ShapeInfo[1] + ShapeInfo[4], ShapeInfo[2] + ShapeInfo[5], ShapeInfo[3] + ShapeInfo[6])
    Axis = geompy.MakeVector(BottomLidCenter, AxisAuxPnt)
    R1 = ShapeInfo[7] # Bottom lid radius.
    R2 = ShapeInfo[8] # Top lid radius.
    H = ShapeInfo[9]
    RestoredCone = geompy.MakeCone(BottomLidCenter, Axis, R1, R2, H)
    geompy.addToStudy(RestoredCone, iFace.GetName() + '__RestoredCone')

# iExpectedConeFragmentShapeInfos is a dictionary of [IndexOfFace, ExpectedShapeInfoOfFace]. IndexOfFace is zero-based index, not one-based one as in Shaper GUI!
def partitionConeAndAssertShapeInfosEqual(iCone, iPartitioningShape, iExpectedConeFragmentShapeInfos, iAddResultsToStudy):
  PartitionedCone = geompy.MakePartition([iCone], [iPartitioningShape], [], [], geompy.ShapeType["FACE"], 0, [], 0)
 if (iAddResultsToStudy):
    geompy.addToStudy(PartitionedCone, "Partitioned" + iCone.GetName())

  ConeFragments = geompy.ExtractShapes(PartitionedCone, geompy.ShapeType["FACE"], True)
  ConeFragmentsIdxs = iExpectedConeFragmentShapeInfos.keys()
 for ConeFragmentIdx in ConeFragmentsIdxs:
 assert (ConeFragmentIdx < len(ConeFragments)), f"Num of faces, {iCone.GetName()} is partitioned into, <= {ConeFragmentIdx} (zero-based index)."
    ConeFragment = ConeFragments[ConeFragmentIdx]
    ConeFragmentName = f"Partitioned{iCone.GetName()}_Face_{ConeFragmentIdx+1}" # Add index to a name as Shaper GUI does.

 if (iAddResultsToStudy):
      geompy.addToStudyInFather(PartitionedCone, ConeFragment, ConeFragmentName)
 else:
      ConeFragment.SetName(ConeFragmentName)

    assertConeInfoEquals(ConeFragment, iExpectedConeFragmentShapeInfos[ConeFragmentIdx], iAddResultsToStudy)

geompy = geomBuilder.New()

OriginalConeBaseCenter = geompy.MakeVertex(100, 130, -60)
OriginalConeAxisAuxPnt = geompy.MakeVertex(100, 230, 40)
OriginalConeAxis = geompy.MakeVector(OriginalConeBaseCenter, OriginalConeAxisAuxPnt)
OriginalCone = geompy.MakeCone(OriginalConeBaseCenter, OriginalConeAxis, 100, 50, 300)
PrismSubstrateCenter = geompy.MakeVertex(100, 1000, 50)
PrismDirAuxPnt = geompy.MakeVertex(100, 950, 50)
PrismDir = geompy.MakeVector(PrismSubstrateCenter, PrismDirAuxPnt)
PrismSubstrate = geompy.MakeDiskPntVecR(PrismSubstrateCenter, PrismDir, 100)
sk = geompy.Sketcher2D()
sk.addPoint(0.395986, 43.346713)
sk.addSegmentAbsolute(66.321537, 41.733575)
sk.addSegmentAbsolute(80.619408, -2.852314)
sk.addSegmentAbsolute(67.641539, -38.565150)
sk.addSegmentAbsolute(22.193602, -56.632163)
sk.addSegmentAbsolute(-19.060136, -51.084351)
sk.addSegmentAbsolute(-60.823572, 34.825751)
sk.addSegmentAbsolute(-13.047004, 55.727527)
sk.close()
PrismBase = sk.wire(PrismSubstrate)
Prism = geompy.MakePrismVecH(PrismBase, PrismDir, 1400)
geompy.addToStudy( OriginalConeBaseCenter, 'OriginalConeBaseCenter' )
geompy.addToStudy( OriginalConeAxisAuxPnt, 'OriginalConeAxisAuxPnt' )
geompy.addToStudy( OriginalConeAxis, 'OriginalConeAxis' )
geompy.addToStudy( OriginalCone, 'OriginalCone' )
geompy.addToStudy( PrismSubstrateCenter, 'PrismSubstrateCenter' )
geompy.addToStudy( PrismDirAuxPnt, 'PrismDirAuxPnt' )
geompy.addToStudy( PrismDir, 'PrismDir' )
geompy.addToStudy( PrismSubstrate, 'PrismSubstrate' )
geompy.addToStudy( PrismBase, 'PrismBase' )
geompy.addToStudy( Prism, 'Prism' )

# Test on the original cone
ExpectedOriginalConeFragmentsShapeInfos = {
  3: ["CONE2D", 100.0, 215.76160602318674, 25.761606023186744, 0.0, 0.7071067811865475, 0.7071067811865475, 79.7857956051852, 54.62305376134459, 150.9764510630437],
  5: ["CONE2D", 100.0, 129.99999999999753, -60.000000000002466, 0.0, 0.7071067811865475, 0.7071067811865475, 100.00000000000058, 69.82277418813575, 181.06335487118898],
  11: ["CONE2D", 100.0, 216.57653245407857, 26.57653245407856, 0.0, 0.7071067811865475, 0.7071067811865475, 79.59371560336794, 52.95933239773038, 159.80629923382543]
}
partitionConeAndAssertShapeInfosEqual(OriginalCone, Prism, ExpectedOriginalConeFragmentsShapeInfos, True)

# Test on isotropically scaled cone. Non-isotropical scaling does not preserve shape kind - it is desired behavior.
ScaledCone = geompy.MakeScaleTransform(OriginalCone, OriginalConeAxisAuxPnt, 2)
ScaledCone.SetName('ScaledCone')
ExpectedScaledConeFragmentsShapeInfos = {
  4: ["CONE2D", 100.0, 29.9999999999999, -160.00000000000009, 0.0, 0.7071067811865475, 0.7071067811865475, 200.00000000000003, 162.64508449690112, 224.1294930185934],
  6: ["CONE2D", 100.0, 262.09898500769475, 72.09898500769472, 0.0, 0.7071067811865475, 0.7071067811865475, 145.2937445981814, 120.13428858458612, 150.95673608157182],
  12: ["CONE2D", 100.0, 262.8999708414969, 72.8999708414969, 0.0, 0.7071067811865475, 0.7071067811865475, 145.10495042660943, 117.46838914559419, 165.8193676860916]
}
partitionConeAndAssertShapeInfosEqual(ScaledCone, Prism, ExpectedScaledConeFragmentsShapeInfos, False)

# Test on a cone, mirrored relative to a point.
PntMirroredCone = geompy.MakeMirrorByPoint(OriginalCone, OriginalConeAxisAuxPnt)
PntMirroredCone.SetName('PntMirroredCone')
ExpectedPntMirroredConeFragmentsShapeInfos = {
  2: ["CONE2D", 100.0, 229.8712015945071, 39.87120159450711, -0.0, -0.7071067811865475, -0.7071067811865475, 76.39941588513841, 51.25530645152799, 150.8646566016625],
  7: ["CONE2D", 100.0, 330.0, 140.0, -0.0, -0.7071067811865475, -0.7071067811865475, 100.0, 71.73019727352477, 169.61881635885143],
  10: ["CONE2D", 100.0, 249.15532313133338, 59.15532313133339, -0.0, -0.7071067811865475, -0.7071067811865475, 80.9447269211102, 51.428754043115056, 177.09583726797095]
}
partitionConeAndAssertShapeInfosEqual(PntMirroredCone, Prism, ExpectedPntMirroredConeFragmentsShapeInfos, False)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/kind_of_shape_cone.py)
