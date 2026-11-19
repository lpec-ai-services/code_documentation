<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_test_others_page.html -->

# GEOM_TestOthers.py

## GEOM_TestOthers.py

```python
import os
```

```python
import GEOM
import tempfile

def TestExportImport (geompy, shape):

  print("Test Export/Import ...", end=' ')

  with tempfile.TemporaryDirectory() as tmpDir:
    # Files for Export/Import testing
    fileExportImportBREP = os.path.join(tmpDir, "testExportImportBREP.brep")
    fileExportImportIGES = os.path.join(tmpDir, "testExportImportIGES.iges")
    fileExportImportSTEP = os.path.join(tmpDir, "testExportImportSTEP.step")

    # ExportBREP, ExportIGES, ExportSTEP
 geompy.ExportBREP(shape, fileExportImportBREP)
 geompy.ExportIGES(shape, fileExportImportIGES)
 geompy.ExportSTEP(shape, fileExportImportSTEP)

    # ImportBREP, ImportIGES, ImportSTEP
 ImportBREP = geompy.ImportBREP(fileExportImportBREP)
 ImportIGES = geompy.ImportIGES(fileExportImportIGES)
 ImportSTEP = geompy.ImportSTEP(fileExportImportSTEP)

 geompy.addToStudy(ImportBREP, "ImportBREP")
 geompy.addToStudy(ImportIGES, "ImportIGES")
 geompy.addToStudy(ImportSTEP, "ImportSTEP")

    # GetIGESUnit and GetSTEPUnit
    if geompy.GetIGESUnit(fileExportImportIGES) != "M":
      ImportIGES_scaled = geompy.ImportIGES(fileExportImportIGES, True)
 geompy.addToStudy(ImportIGES_scaled, "ImportIGES_scaled")
      pass

    if geompy.GetSTEPUnit(fileExportImportSTEP) != "M":
      ImportSTEP_scaled = geompy.ImportSTEP(fileExportImportSTEP, True)
 geompy.addToStudy(ImportSTEP_scaled, "ImportSTEP_scaled")
      pass
    pass

  # Test RestoreShape from binary BRep stream
  aStream = shape.GetShapeStream()
  aNewShape = geompy.RestoreShape(aStream)
 geompy.addToStudy(aNewShape, "aNewShape")

  print("OK")
```

```python

def TestOtherOperations (geompy, math):

  # prepare data for further operations
  vx = geompy.MakeVectorDXDYDZ( 1,  0,  0)
  vy = geompy.MakeVectorDXDYDZ( 0,  1,  0)
  vz = geompy.MakeVectorDXDYDZ( 0,  0,  1)

  v_y = geompy.MakeVectorDXDYDZ( 0, -1,  0)

  p11 = geompy.MakeVertex( 0,  0, 0)
  p12 = geompy.MakeVertex(30,  0, 0)
  p13 = geompy.MakeVertex(30, 30, 0)
  p14 = geompy.MakeVertex( 0, 30, 0)

  p21 = geompy.MakeVertex(10, 10, 0)
  p22 = geompy.MakeVertex(20, 10, 0)
  p23 = geompy.MakeVertex(20, 20, 0)
  p24 = geompy.MakeVertex(10, 20, 0)

  e11 = geompy.MakeEdge(p11, p12)
  e12 = geompy.MakeEdge(p12, p13)
  e13 = geompy.MakeEdge(p13, p14)
  e14 = geompy.MakeEdge(p14, p11)

  e21 = geompy.MakeEdge(p21, p22)
  e22 = geompy.MakeEdge(p22, p23)
  e23 = geompy.MakeEdge(p23, p24)
  e24 = geompy.MakeEdge(p24, p21)

  w1 = geompy.MakeWire([e11, e12, e13, e14])
  w2 = geompy.MakeWire([e21, e22, e23, e24])
  w3 = geompy.MakeTranslation(w2, 0, 0, 10)

  id_w1 = geompy.addToStudy(w1, "Outside Wire")
  id_w2 = geompy.addToStudy(w2, "Inside Wire")
  id_w3 = geompy.addToStudy(w3, "Inside Wire, translated along OZ")
```

```python

  # MakeFaces
  f12 = geompy.MakeFaces([w1, w2], 0)
  id_f12 = geompy.addToStudy(f12, "MakeFaces WO + WI")
```

```python

  # Export/Import
  TestExportImport(geompy, f12)
```

```python

  # OrientationChange
  Box = geompy.MakeBoxDXDYDZ(200, 200, 200)
 geompy.addToStudy(Box, "Box")
  Orientation = geompy.OrientationChange(Box)
  id_Orientation = geompy.addToStudy(Orientation, "OrientationChange")
```

```python

  # MakeCommon, MakeCut, MakeFuse, MakeSection
  p1 = geompy.MakeVertex(60, 120, 0)
  p2 = geompy.MakeVertex( 0,  0, 0)
  v = geompy.MakeVector(p1, p2)
  height = 90
  radius1 = 50
  cylinder = geompy.MakeCylinder(p1, v, radius1, height)
  Sphere = geompy.MakeSphereR(100)

  Common1 = geompy.MakeCommon    (Box, Sphere)
  Cut1    = geompy.MakeCut       (Box, Sphere)
  Fuse1   = geompy.MakeFuse      (Box, Sphere)
  Section = geompy.MakeSection   (Box, Sphere)
  Common2 = geompy.MakeCommonList([Box, Sphere, cylinder])
  Cut2    = geompy.MakeCutList   (Box, [Sphere, cylinder])
  Fuse2   = geompy.MakeFuseList  ([Box, Sphere, cylinder])

  id_Common1 = geompy.addToStudy(Common1,  "Common_1")
  id_Cut1    = geompy.addToStudy(Cut1,     "Cut_1")
  id_Fuse1   = geompy.addToStudy(Fuse1,    "Fuse_1")
  id_Section = geompy.addToStudy(Section, "Section")
  id_Common2 = geompy.addToStudy(Common2,  "Common_2")
  id_Cut2    = geompy.addToStudy(Cut2,     "Cut_2")
  id_Fuse2   = geompy.addToStudy(Fuse2,    "Fuse_2")
```

```python

  # Partition
  p100 = geompy.MakeVertex(100, 100, 100)
  p300 = geompy.MakeVertex(300, 300, 300)
  Box1 = geompy.MakeBoxTwoPnt(p100, p300)
 Partition = geompy.Partition([Box], [Box1])
  id_Partition = geompy.addToStudy(Partition, "Partition of Box by Box1")
```

```python

  # MakeMultiRotation1D, MakeMultiRotation2D
  pz = geompy.MakeVertex(0, 0, 100)
  vy = geompy.MakeVectorDXDYDZ(0, 100, 0)

  MultiRot1Dt = geompy.MakeMultiRotation1DNbTimes(f12, vy, pz, 6)
  MultiRot1Ds = geompy.MakeMultiRotation1DByStep(f12, vy, pz, math.pi/5., 6)

  MultiRot2Dt = geompy.MakeMultiRotation2DNbTimes(f12, vy, pz, 5, 30, 3)
  MultiRot2Ds = geompy.MakeMultiRotation2DByStep(f12, vy, pz, math.pi/4., 6, 30, 3)

 geompy.addToStudy(MultiRot1Dt, "MakeMultiRotation1DNbTimes")
 geompy.addToStudy(MultiRot1Ds, "MakeMultiRotation1DByStep")
 geompy.addToStudy(MultiRot2Dt, "MakeMultiRotation2DNbTimes")
  id_MultiRot2D = geompy.addToStudy(MultiRot2Ds, "MakeMultiRotation2DByStep")
```

```python

  # MakeFilletAll
  radius_fillet = 10.
  face5 = geompy.SubShapeSortedCentres(Box, geompy.ShapeType["FACE"], [5])
  f_glob_id = geompy.GetSubShapeID(Box, face5)
  SuppFace = geompy.SuppressFaces(Box, [f_glob_id])

 MakeFilletAll = geompy.MakeFilletAll(SuppFace, radius_fillet)
  id_MakeFilletAll = geompy.addToStudy(MakeFilletAll, "MakeFilletAll")
```

```python

  # MakeChamferAll
  dimension_chamfer = 10.
 MakeChamferAll = geompy.MakeChamferAll(SuppFace, dimension_chamfer)
  id_MakeChamferAll = geompy.addToStudy(MakeChamferAll, "MakeChamferAll")
```

```python

  # MakeChamfer
  d1 = 13.
  d2 = 7.
  box_faces = geompy.SubShapeAllSortedCentres(Box, geompy.ShapeType["FACE"])
  f_ind_1 = geompy.GetSubShapeID(Box, box_faces[0])
  f_ind_2 = geompy.GetSubShapeID(Box, box_faces[1])
  f_ind_3 = geompy.GetSubShapeID(Box, box_faces[2])

 MakeChamfer = geompy.MakeChamfer(Box, d1, d2, geompy.ShapeType["FACE"],
                                   [f_ind_1, f_ind_2, f_ind_3])
  id_MakeChamfer = geompy.addToStudy(MakeChamfer, "MakeChamfer")
```

```python

  # NumberOf
 NumberOfFaces = geompy.NumberOfFaces(Box)
 NumberOfEdges = geompy.NumberOfEdges(Box)
 NumberOfSolids = geompy.NumberOfSolids(Box)
  NumberOfShapes = geompy.NumberOfSubShapes(Box, geompy.ShapeType["SHAPE"])

  assert (NumberOfFaces  ==  6), "Bad number of faces in BOX!"
  assert (NumberOfEdges  == 12), "Bad number of edges in BOX!"
  assert (NumberOfSolids ==  1), "Bad number of solids in BOX!"
  assert (NumberOfShapes == 34), "Bad number of shapes in BOX!"
```

```python

  # MakeBlockExplode
  Compound = geompy.MakeCompound([Box, Sphere])
 MakeBlockExplode = geompy.MakeBlockExplode(Compound, 6, 6)

  id_MakeBlockExplode = geompy.addToStudy(MakeBlockExplode[0], "MakeBlockExplode")
```

```python

  # CheckCompoundOfBlocks
  p1 = geompy.MakeVertex(200, 0, 0)
  p2 = geompy.MakeVertex(400, 200, 200)
  p3 = geompy.MakeVertex(400, 50, 50)
  p4 = geompy.MakeVertex(600, 250, 250)

  Box2 = geompy.MakeBoxTwoPnt(p1, p2)
  Box3 = geompy.MakeBoxTwoPnt(p3, p4)
  Cyl  = geompy.MakeCylinderRH(50, 300)
  Cone = geompy.MakeConeR1R2H(150, 10, 400)

  Compound1 = geompy.MakeCompound([Box, Cyl, Cone, Box3, Box2], "Compound1")

  print("Printing errors of not valid Blocks Compound (EXPECTED):")
  IsValid = geompy.CheckCompoundOfBlocks(Compound1)
 # This Blocks Compound is NOT VALID
  assert (not IsValid)
  (NonBlocks, NonQuads) = geompy.GetNonBlocks(Compound1)
 if NonBlocks is not None:
 geompy.addToStudyInFather(Compound1, NonBlocks, "Group of non-hexahedral solids")
 if NonQuads is not None:
 geompy.addToStudyInFather(Compound1, NonQuads, "Group of non-quadrangular faces")

  IsValid = geompy.CheckCompoundOfBlocks(Box)
  assert (IsValid) # Box is a VALID Blocks Compound
```

```python

  # GetSame
  Cone_ss = geompy.GetSame(Compound1, Cone)
  id_Cone_ss = geompy.addToStudyInFather(Compound1, Cone_ss, "Cone subshape")
```

```python

  # test geometrical groups

  # CreateGroup
 CreateGroup = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])

  id_CreateGroup = geompy.addToStudy(CreateGroup, "CreateGroup")
```

```python

  # AddObject
  f_ind_4 = geompy.GetSubShapeID(Box, box_faces[3])
  f_ind_5 = geompy.GetSubShapeID(Box, box_faces[4])
  f_ind_6 = geompy.GetSubShapeID(Box, box_faces[5])

 geompy.AddObject(CreateGroup, f_ind_6) # box_faces[5]
 geompy.AddObject(CreateGroup, f_ind_1) # box_faces[0]
 geompy.AddObject(CreateGroup, f_ind_4) # box_faces[3]
  # Now contains f_ind_6, f_ind_1, f_ind_4
```

```python

  # UnionList
 geompy.UnionList(CreateGroup, [box_faces[2], box_faces[4], box_faces[5]])
  # Now contains f_ind_6, f_ind_1, f_ind_4, f_ind_3, f_ind_5
```

```python

  # RemoveObject(theGroup, theSubShapeID)
 geompy.RemoveObject(CreateGroup, f_ind_1) # box_faces[0]
  # Now contains f_ind_6, f_ind_4, f_ind_3, f_ind_5
```

```python

  # DifferenceList
 geompy.DifferenceList(CreateGroup, [box_faces[1], box_faces[0], box_faces[3]])
  # Now contains f_ind_6, f_ind_3, f_ind_5
```

```python

  # GetObjectIDs
 GetObjectIDs = geompy.GetObjectIDs(CreateGroup)
  assert (sorted(GetObjectIDs) == sorted([f_ind_6, f_ind_3, f_ind_5]))
```

```python

  # GetMainShape
  BoxCopy = geompy.GetMainShape(CreateGroup)
```

```python

  # DifferenceIDs
 geompy.DifferenceIDs(CreateGroup, [f_ind_3, f_ind_5])
  # Now contains f_ind_6
```

```python

  # UnionIDs
 geompy.UnionIDs(CreateGroup, [f_ind_1, f_ind_2, f_ind_6])
  # Now contains f_ind_6, f_ind_1, f_ind_2

  # Check
 GetObjectIDs = geompy.GetObjectIDs(CreateGroup)
  assert (sorted(GetObjectIDs) == sorted([f_ind_6, f_ind_1, f_ind_2]))
```

```python

  # Boolean Operations on Groups (Union, Intersection, Cut)
  Group_1 = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])
 geompy.UnionIDs(Group_1, [13, 23])
  Group_2 = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])
 geompy.UnionIDs(Group_2, [3, 27])
  Group_3 = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])
 geompy.UnionIDs(Group_3, [33, 23])
  Group_4 = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])
 geompy.UnionIDs(Group_4, [31, 27])

 geompy.addToStudyInFather(Box, Group_1, 'Group_1')
 geompy.addToStudyInFather(Box, Group_2, 'Group_2')
 geompy.addToStudyInFather(Box, Group_3, 'Group_3')
 geompy.addToStudyInFather(Box, Group_4, 'Group_4')

  # union groups
  Group_U_1_2 = geompy.UnionGroups(Group_1, Group_2)
  Group_UL_3_4 = geompy.UnionListOfGroups([Group_3, Group_4])

 geompy.addToStudyInFather(Box, Group_U_1_2, 'Group_U_1_2')
 geompy.addToStudyInFather(Box, Group_UL_3_4, 'Group_UL_3_4')

  # intersect groups
  Group_I_1_3 = geompy.IntersectGroups(Group_1, Group_3)
  Group_IL_1_3 = geompy.IntersectListOfGroups([Group_1, Group_3])

 geompy.addToStudyInFather(Box, Group_I_1_3, 'Group_I_1_3')
 geompy.addToStudyInFather(Box, Group_IL_1_3, 'Group_IL_1_3')

  # cut groups
  Group_C_2_4 = geompy.CutGroups(Group_2, Group_4)
  Group_CL_2_4 = geompy.CutListOfGroups([Group_2], [Group_4])

 geompy.addToStudyInFather(Box, Group_C_2_4, 'Group_C_2_4')
 geompy.addToStudyInFather(Box, Group_CL_2_4, 'Group_CL_2_4')
```

```python

  GroupType = geompy.GetType(CreateGroup)
  assert (GroupType == geompy.ShapeType["FACE"])
```

```python

  # Example of sphere partitioning into hexahedral blocks
  p0 = geompy.MakeVertex(0, 0, 0)
  b0 = geompy.MakeBox(-50, -50, -50, 50, 50, 50)
  s0 = geompy.MakeSphereR(100)

  id_b0 = geompy.addToStudy(b0, "b0")
  id_s0 = geompy.addToStudy(s0, "s0")

  v_0pp = geompy.MakeVectorDXDYDZ( 0,  1,  1)
  v_0np = geompy.MakeVectorDXDYDZ( 0, -1,  1)
  v_p0p = geompy.MakeVectorDXDYDZ( 1,  0,  1)
  v_p0n = geompy.MakeVectorDXDYDZ( 1,  0, -1)
  v_pp0 = geompy.MakeVectorDXDYDZ( 1,  1,  0)
  v_pn0 = geompy.MakeVectorDXDYDZ( 1, -1,  0)

  pln_0pp = geompy.MakePlane(p0, v_0pp, 300)
  pln_0np = geompy.MakePlane(p0, v_0np, 300)
  pln_p0p = geompy.MakePlane(p0, v_p0p, 300)
  pln_p0n = geompy.MakePlane(p0, v_p0n, 300)
  pln_pp0 = geompy.MakePlane(p0, v_pp0, 300)
  pln_pn0 = geompy.MakePlane(p0, v_pn0, 300)

  part_objs = [b0, pln_0pp, pln_0np, pln_p0p, pln_p0n, pln_pp0, pln_pn0]
  part_tool_1 = geompy.MakePartition(part_objs, KeepNonlimitShapes=1)
 geompy.addToStudy(part_tool_1, "part_tool_1")

  pt_pnt_1  = geompy.MakeVertex( 55,   0,  55)
  pt_pnt_2  = geompy.MakeVertex(  0,  55,  55)
  pt_pnt_3  = geompy.MakeVertex(-55,   0,  55)
  pt_pnt_4  = geompy.MakeVertex(  0, -55,  55)
  pt_pnt_5  = geompy.MakeVertex( 55,  55,   0)
  pt_pnt_6  = geompy.MakeVertex( 55, -55,   0)
  pt_pnt_7  = geompy.MakeVertex(-55,  55,   0)
  pt_pnt_8  = geompy.MakeVertex(-55, -55,   0)
  pt_pnt_9  = geompy.MakeVertex( 55,   0, -55)
  pt_pnt_10 = geompy.MakeVertex(  0,  55, -55)
  pt_pnt_11 = geompy.MakeVertex(-55,   0, -55)
  pt_pnt_12 = geompy.MakeVertex(  0, -55, -55)

  pt_face_1  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_1)
  pt_face_2  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_2)
  pt_face_3  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_3)
  pt_face_4  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_4)
  pt_face_5  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_5)
  pt_face_6  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_6)
  pt_face_7  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_7)
  pt_face_8  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_8)
  pt_face_9  = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_9)
  pt_face_10 = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_10)
  pt_face_11 = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_11)
  pt_face_12 = geompy.GetFaceNearPoint(part_tool_1, pt_pnt_12)

  part_tools = [pt_face_1, pt_face_4, pt_face_7, pt_face_10,
                pt_face_2, pt_face_5, pt_face_8, pt_face_11,
                pt_face_3, pt_face_6, pt_face_9, pt_face_12, b0]
  part_tool = geompy.MakeCompound(part_tools)
 geompy.addToStudy(part_tool, "part_tool")
  part = geompy.MakePartition([s0], [part_tool])
 geompy.addToStudy(part, "part")

  # GetFreeFacesIDs
  anIDs = geompy.GetFreeFacesIDs(part)
  freeFaces = geompy.GetSubShape(part, anIDs)

 geompy.addToStudy(freeFaces, "freeFaces")
```

```python

  # Example of hexahedral sphere creation
  # (spherical surface of solid is made of six quasi-quadrangular faces)
  tools = [pln_pp0, pln_pn0, pln_p0p, pln_p0n]
  Partition_1 = geompy.MakePartition([Sphere], tools, [], [], geompy.ShapeType["SOLID"], 0, [])
 geompy.addToStudy(Partition_1, "Partition_1")

  faces = geompy.SubShapeAllSortedCentres(Partition_1, geompy.ShapeType["FACE"])

  Face_1 = faces[0]
  Face_2 = faces[39]
  Face_3 = faces[40]

 geompy.addToStudyInFather(Partition_1, Face_1, "Face_1")
 geompy.addToStudyInFather(Partition_1, Face_2, "Face_2")
 geompy.addToStudyInFather(Partition_1, Face_3, "Face_3")

  Vector_5 = geompy.MakeVectorDXDYDZ(0, 20, 0)
 geompy.addToStudy(Vector_5, "Vector_5")

  Rotation_1 = geompy.MakeRotation(Face_1, Vector_5, 90*math.pi/180.0)
  Rotation_2 = geompy.MakeRotation(Face_1, Vector_5, 180*math.pi/180.0)
  Rotation_3 = geompy.MakeRotation(Face_1, Vector_5, 270*math.pi/180.0)

 geompy.addToStudy(Rotation_1, "Rotation_1")
 geompy.addToStudy(Rotation_2, "Rotation_2")
 geompy.addToStudy(Rotation_3, "Rotation_3")

  Vector_6 = geompy.MakeVectorDXDYDZ(0, 0, 20)
 geompy.addToStudy(Vector_6, "Vector_6")

  Rotation_4 = geompy.MakeRotation(Face_1, Vector_6, 90*math.pi/180.0)
  Rotation_5 = geompy.MakeRotation(Face_1, Vector_6, -90*math.pi/180.0)
 geompy.addToStudy(Rotation_4, "Rotation_4")
 geompy.addToStudy(Rotation_5, "Rotation_5")

  Shell_1 = geompy.MakeShell([Face_1, Rotation_1, Rotation_2, Rotation_3, Rotation_4, Rotation_5])
  Solid_1 = geompy.MakeSolid([Shell_1])
```

```python

  # RemoveExtraEdges with union of all faces, sharing common surfaces
  box10 = geompy.MakeBoxDXDYDZ(10, 10, 10, "box10")
  box11 = geompy.MakeTranslation(box10, 10, 0, 0, "box11")
  FuseB = geompy.MakeFuse(box10, box11, checkSelfInte=False, rmExtraEdges=False, theName="FuseB")
  NoExtraEdges_1 = geompy.RemoveExtraEdges(FuseB, True) # doUnionFaces = True

 geompy.addToStudy(Shell_1, "Shell_1")
 geompy.addToStudy(Solid_1, "Solid_1")
 geompy.addToStudy(NoExtraEdges_1, "NoExtraEdges_1")

  # RemoveExtraEdges (by default, doUnionFaces = False)
  freeFacesWithoutExtra = geompy.RemoveExtraEdges(freeFaces)

 geompy.addToStudy(freeFacesWithoutExtra, "freeFacesWithoutExtra")
```

```python

  # UnionFaces
  unitedFaces = geompy.UnionFaces(freeFaces)

 geompy.addToStudy(unitedFaces, "unitedFaces")
```

```python

  # GetSharedShapes
  sharedFaces = geompy.GetSharedShapes(part, freeFaces,
 geompy.ShapeType["FACE"])
  ind = 1
 for shFace in sharedFaces:
 geompy.addToStudy(shFace, "sharedFace_" + repr(ind))
    ind = ind + 1
    pass

  sharedEdges = geompy.GetSharedShapesMulti([part, freeFaces],
 geompy.ShapeType["EDGE"])
  ind = 1
 for shEdge in sharedEdges:
 geompy.addToStudy(shEdge, "sharedEdge_" + repr(ind))
```

```python
    ind = ind + 1
    pass

  # TransferData
  path = os.getenv("DATA_DIR")
  fileName = path + "/Shapes/Step/black_and_white.step"
  blackWhite = geompy.ImportSTEP(fileName)
  blackWhiteCopy = geompy.MakeCopy(blackWhite[0])
  subBlackWhite = geompy.SubShapeAll(blackWhiteCopy, GEOM.SOLID)
 geompy.TransferData(blackWhite[0], blackWhiteCopy)
 geompy.addToStudy(blackWhite[0], "blackWhite")
 geompy.addToStudy(blackWhiteCopy, "blackWhiteCopy")
 geompy.addToStudyInFather( blackWhiteCopy, subBlackWhite[0], "" )
 geompy.addToStudyInFather( blackWhiteCopy, subBlackWhite[1], "" )
```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
