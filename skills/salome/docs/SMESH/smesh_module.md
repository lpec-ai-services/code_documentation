<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/smesh_module.html -->

# SMESH module

## DriverMED_ReadStatus

*class* SMESH.DriverMED_ReadStatus
:   Enumeration for mesh read status

    DRS_OK
    :   Ok

    DRS_EMPTY
    :   a file contains no mesh with the given name

    DRS_WARN_RENUMBER
    :   a MED file has overlapped ranges of element numbers,
        so the numbers from the file are ignored

    DRS_WARN_SKIP_ELEM
    :   some elements were skipped due to incorrect file data

    DRS_WARN_DESCENDING
    :   some elements were skipped due to descending connectivity

    DRS_FAIL
    :   general failure (exception etc.)

## ComputeErrorName

*class* SMESH.ComputeErrorName
:   Enumeration of computation errors

    COMPERR_OK
    :   Ok

    COMPERR_BAD_INPUT_MESH
    :   wrong mesh of lower sub-mesh

    COMPERR_STD_EXCEPTION
    :   some std exception raised

    COMPERR_OCC_EXCEPTION
    :   OCC exception raised

    COMPERR_SLM_EXCEPTION
    :   SALOME exception raised

    COMPERR_EXCEPTION
    :   other exception raised

    COMPERR_MEMORY_PB
    :   memory allocation problem

    COMPERR_ALGO_FAILED
    :   computation failed

    COMPERR_BAD_SHAPE
    :   bad geometry

    COMPERR_WARNING
    :   algo reports error but sub-mesh is computed anyway

    COMPERR_CANCELED
    :   compute canceled

    COMPERR_NO_MESH_ON_SHAPE
    :   no mesh elements assigned to sub-mesh

    COMPERR_BAD_PARMETERS
    :   incorrect hypotheses parameters

## ComputeError

*class* SMESH.ComputeError
:   Error details

    code
    :   `int` - [`ComputeErrorName`](#SMESH.ComputeErrorName) or, if negative, algo specific code

    comment
    :   `str` - textual problem description

    algoName
    :   `str`

    subShapeID
    :   `int` - id of sub-shape of a shape to mesh

    hasBadMesh
    :   `boolean` - there are elements preventing computation available for visualization

## Measure

*class* SMESH.Measure
:   Data returned by measure operations

    minX, minY, minZ
    :   `double` - coordinates of one point

    maxX, maxY, maxZ
    :   `double` - coordinates of another point

    node1, node2
    :   `long` - IDs of two nodes

    elem1, elem2
    :   `long` - IDs of two elements

    value
    :   `double` - distance

## NodePosition

*class* SMESH.NodePosition
:   Node location on a shape

    shapeID
    :   `long` - ID of a shape

    shapeType
    :   `GEOM.shape_type` - type of shape

    params
    :   `list of float` -

        > - [U] on EDGE,
        > - [U,V] on FACE,
        > - [] on the rest shapes

## ElementPosition

*class* SMESH.ElementPosition
:   Element location on a shape

    shapeID
    :   `long` - ID of a shape

    shapeType
    :   `GEOM.shape_type` - type of shape

## PolySegment

*class* SMESH.PolySegment
:   Define a cutting plane passing through two points.
    Used in [`MakePolyLine()`](smeshBuilder.md#smeshBuilder.Mesh.MakePolyLine)

    node1ID1, node1ID2
    :   `int,int` - *point 1*: if *node1ID2* > 0, then the point is in the middle of a face edge defined
        :   by two nodes, else it is at *node1ID1*

    node2ID1, node2ID2
    :   `int,int` - *point 2*: if *node2ID2* > 0, then the point is in the middle of a face edge defined
        :   by two nodes, else it is at *node2ID1*

    vector
    :   `SMESH.DirStruct` - vector on the plane; to use a default plane set vector = (0,0,0)

## ElementType

*class* SMESH.ElementType
:   Enumeration for element type, like in SMDS

    ALL

    NODE

    EDGE

    FACE

    VOLUME

    ELEM0D

    BALL

    NB_ELEMENT_TYPES

## EntityType

*class* SMESH.EntityType
:   Enumeration of entity type

    Entity_Node

    Entity_0D

    Entity_Edge

    Entity_Quad_Edge

    Entity_Triangle

    Entity_Quad_Triangle

    Entity_BiQuad_Triangle

    Entity_Quadrangle

    Entity_Quad_Quadrangle

    Entity_BiQuad_Quadrangle

    Entity_Polygon

    Entity_Quad_Polygon

    Entity_Tetra

    Entity_Quad_Tetra

    Entity_Pyramid

    Entity_Quad_Pyramid

    Entity_Hexa

    Entity_Quad_Hexa

    Entity_TriQuad_Hexa

    Entity_Penta

    Entity_Quad_Penta

    Entity_BiQuad_Penta

    Entity_Hexagonal_Prism

    Entity_Polyhedra

    Entity_Quad_Polyhedra

    Entity_Ball

    Entity_Last

## GeometryType

*class* SMESH.GeometryType
:   Enumeration of element geometry type

    Geom_POINT

    Geom_EDGE

    Geom_TRIANGLE

    Geom_QUADRANGLE

    Geom_POLYGON

    Geom_TETRA

    Geom_PYRAMID

    Geom_HEXA

    Geom_PENTA

    Geom_HEXAGONAL_PRISM

    Geom_POLYHEDRA

    Geom_BALL

    Geom_LAST

## Hypothesis_Status

*class* SMESH.Hypothesis_Status
:   Enumeration of result of hypothesis addition/removal

    HYP_OK
    :   Ok

    HYP_MISSING
    :   algo misses a hypothesis

    HYP_CONCURRENT
    :   several applicable hypotheses

    HYP_BAD_PARAMETER
    :   hypothesis has a bad parameter value

    HYP_HIDDEN_ALGO
    :   an algo is hidden by an upper dim algo generating all-dim elements

    HYP_HIDING_ALGO
    :   an algo hides lower dim algos by generating all-dim elements

    HYP_UNKNOWN_FATAL
    :   all statuses below should be considered as fatal for Add/RemoveHypothesis operations

    HYP_INCOMPATIBLE
    :   hypothesis does not fit algorithm

    HYP_NOTCONFORM
    :   not conform mesh is produced applying a hypothesis

    HYP_ALREADY_EXIST
    :   such hypothesis already exist

    HYP_BAD_DIM
    :   bad dimension

    HYP_BAD_SUBSHAPE
    :   shape is neither the main one, nor its sub-shape, nor a group

    HYP_BAD_GEOMETRY
    :   geometry mismatches algorithm’s expectation

    HYP_NEED_SHAPE
    :   algorithm can work on shape only

    HYP_INCOMPAT_HYPS
    :   several additional hypotheses are incompatible one with other

## FunctorType

*class* SMESH.FunctorType
:   Enumeration of functor types

    FT_AspectRatio

    FT_AspectRatio3D

    FT_Warping

    FT_MinimumAngle

    FT_Taper

    FT_Skew

    FT_Area

    FT_Volume3D

    FT_MaxElementLength2D

    FT_MaxElementLength3D

    FT_FreeBorders

    FT_FreeEdges

    FT_FreeNodes

    FT_FreeFaces

    FT_EqualNodes

    FT_EqualEdges

    FT_EqualFaces

    FT_EqualVolumes

    FT_MultiConnection

    FT_MultiConnection2D

    FT_Length

    FT_Length2D

    FT_Deflection2D

    FT_NodeConnectivityNumber

    FT_BelongToMeshGroup

    FT_BelongToGeom

    FT_BelongToPlane

    FT_BelongToCylinder

    FT_BelongToGenSurface

    FT_LyingOnGeom

    FT_RangeOfIds

    FT_BadOrientedVolume

    FT_BareBorderVolume

    FT_BareBorderFace

    FT_OverConstrainedVolume

    FT_OverConstrainedFace

    FT_LinearOrQuadratic

    FT_GroupColor

    FT_ElemGeomType

    FT_EntityType

    FT_CoplanarFaces

    FT_BallDiameter

    FT_ConnectedElements

    FT_LessThan

    FT_MoreThan

    FT_EqualTo

    FT_LogicalNOT

    FT_LogicalAND

    FT_LogicalOR

    FT_Undefined

## Filter.Criterion

*class* SMESH.Filter.Criterion
:   Structure containing information of a criterion

    Type
    :   `long` - value of item of [`SMESH.FunctorType`](#SMESH.FunctorType)

    Compare
    :   `long` - value of item of [`SMESH.FunctorType`](#SMESH.FunctorType) in ( FT_LessThan, FT_MoreThan, FT_EqualTo )

    Threshold
    :   `double` - threshold value

    ThresholdStr
    :   `string` - Threshold value defined as string. Used for:
        :   1. Diapason of identifiers. Example: “1,2,3,5-10,12,27-29”.
            2. Storing name of shape.
            3. Storing group color “0.2;0;0.5”.
            4. Storing point coordinates.

    ThresholdID
    :   `string` - One more threshold value defined as string. Used for storing id of shape

    UnaryOp
    :   `long` - unary logical operation: FT_LogicalNOT or FT_Undefined

    BinaryOp
    :   `long` - binary logical operation FT_LogicalAND, FT_LogicalOR etc.

    Tolerance
    :   `double` - Tolerance is used for
        :   1. Comparison of real values.
            2. Detection of geometrical coincidence.

    TypeOfElement
    :   `ElementType` - type of element [`SMESH.ElementType`](#SMESH.ElementType) (SMESH.NODE, SMESH.FACE etc.)

    Precision
    :   `long` - Precision of numerical functors

## FreeEdges.Border

*class* FreeEdges.Border
:   Free edge: edge connected to one face only

    myElemId
    :   `long` - ID of a face

    myPnt1,myPnt2
    :   `long` - IDs of two nodes

## PointStruct

*class* SMESH.PointStruct
:   3D point.

    Use [`GetPointStruct()`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetPointStruct)
    to convert a vertex (GEOM.GEOM_Object) to PointStruct

    x,y,z
    :   `double` - point coordinates

## DirStruct

*class* SMESH.DirStruct
:   3D vector.

    Use [`GetDirStruct()`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetDirStruct)
    to convert a vector (GEOM.GEOM_Object) to DirStruct

    PS
    :   [`PointStruct`](#SMESH.PointStruct) - vector components

## AxisStruct

*class* SMESH.AxisStruct
:   Axis defined by its origin and its vector.

    Use [`GetAxisStruct()`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetAxisStruct)
    to convert a line or plane (GEOM.GEOM_Object) to AxisStruct

    x,y,z
    :   `double` - coordinates of the origin

    vx,vy,vz
    :   `double` - components of the vector

## Filter

*class* SMESH.Filter
:   Filter of mesh entities

    GetElementsId(*mesh*)
    :   Return satisfying elements

        Parameters:
        :   **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – the mesh;
            it can be obtained via [`GetMesh()`](smeshBuilder.md#smeshBuilder.Mesh.GetMesh)

        Returns:
        :   list of IDs

    GetIDs()
    :   Return satisfying elements.
        A mesh to filter must be already set, either via [`SetMesh()`](#SMESH.Filter.SetMesh) method
        or via `mesh` argument of [`GetFilter()`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetFilter)

        Returns:
        :   list of IDs

    SetMesh(*mesh*)
    :   Set mesh to filter

        Parameters:
        :   **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – the mesh;
            it can be obtained via [`GetMesh()`](smeshBuilder.md#smeshBuilder.Mesh.GetMesh)

    SetCriteria(*criteria*)
    :   Define filtering criteria

        Parameters:
        :   **criteria** – list of [`SMESH.Filter.Criterion`](#SMESH.Filter.Criterion)

## NumericalFunctor

*class* SMESH.NumericalFunctor
:   Calculate value by ID of mesh entity. Base class of various functors

    GetValue(*elementID*)
    :   Compute a value

        Parameters:
        :   **elementID** – ID of element or node

        Returns:
        :   floating value

## SMESH_Mesh

*class* SMESH.SMESH_Mesh
:   Mesh. It is a Python wrap over a CORBA interface of mesh.

    All its methods are exposed via [`smeshBuilder.Mesh`](smeshBuilder.md#smeshBuilder.Mesh) class that you can obtain by calling:

    ```python
    smeshBuilder_mesh = smesh.Mesh( smesh_mesh )
    ```

## SMESH_MeshEditor

*class* SMESH.SMESH_MeshEditor
:   Mesh editor. It is a Python wrap over a CORBA SMESH_MeshEditor interface.
    All its methods are exposed via [`smeshBuilder.Mesh`](smeshBuilder.md#smeshBuilder.Mesh) class.

    *class* Extrusion_Error
    :   Enumeration of errors of [`ExtrusionAlongPathObjects()`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathObjects)

        EXTR_OK

        EXTR_NO_ELEMENTS

        EXTR_PATH_NOT_EDGE

        EXTR_BAD_PATH_SHAPE

        EXTR_BAD_STARTING_NODE

        EXTR_BAD_ANGLES_NUMBER

        EXTR_CANT_GET_TANGENT

*class* SMESH_MeshEditor.Sew_Error
:   Enumeration of errors of SMESH_MeshEditor.Sewing… methods

    SEW_OK

    SEW_BORDER1_NOT_FOUND

    SEW_BORDER2_NOT_FOUND

    SEW_BOTH_BORDERS_NOT_FOUND

    SEW_BAD_SIDE_NODES

    SEW_VOLUMES_TO_SPLIT

    SEW_DIFF_NB_OF_ELEMENTS

    SEW_TOPO_DIFF_SETS_OF_ELEMENTS

    SEW_BAD_SIDE1_NODES

    SEW_BAD_SIDE2_NODES

    SEW_INTERNAL_ERROR

## SMESH_Pattern

*class* SMESH.SMESH_Pattern
:   Pattern mapper. Use a pattern defined by user for

    > - creating mesh elements on geometry, faces or blocks
    > - refining existing mesh elements, faces or hexahedra

    The pattern is defined by a string as explained [here](pattern_mapping.md).

    Usage work-flow is:

    > - Define a pattern via Load… method
    > - Compute future positions of nodes via Apply… method
    > - Create nodes and elements in a mesh via [`MakeMesh()`](#SMESH.SMESH_Pattern.MakeMesh) method

    LoadFromFile(*patternFileContents*)
    :   Load a pattern from the string *patternFileContents*

        Parameters:
        :   **patternFileContents** (*str*) – string defining a pattern

        Returns:
        :   True if succeeded

    LoadFromFace(*mesh*, *geomFace*, *toProject*)
    :   Create a 2D pattern from the mesh built on *geomFace*.

        Parameters:
        :   - **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – source mesh
            - **geomFace** (*GEOM.GEOM_Object*) – geometrical face whose mesh forms a pattern
            - **toProject** (*boolean*) – if True makes override nodes positions
              on *geomFace* computed by mesher

        Returns:
        :   True if succeeded

    LoadFrom3DBlock(*mesh*, *geomBlock*)
    :   Create a 3D pattern from the mesh built on *geomBlock*

        Parameters:
        :   - **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – source mesh
            - **geomBlock** (*GEOM.GEOM_Object*) – geometrical block whose mesh forms a pattern

        Returns:
        :   True if succeeded

    ApplyToFace(*geomFace*, *vertexOnKeyPoint1*, *toReverse*)
    :   Compute nodes coordinates by applying
        the loaded pattern to *geomFace*. The first key-point
        will be mapped into *vertexOnKeyPoint1*, which must
        be in the outer wire of *geomFace*

        Parameters:
        :   - **geomFace** (*GEOM.GEOM_Object*) – the geometrical face to generate faces on
            - **vertexOnKeyPoint1** (*GEOM.GEOM_Object*) – the vertex to be at the 1st key-point
            - **toReverse** (*boolean*) – to reverse order of key-points

        Returns:
        :   list of [`SMESH.PointStruct`](#SMESH.PointStruct) - computed coordinates of points of the pattern

    ApplyTo3DBlock(*geomBlock*, *vertex000*, *vertex001*)
    :   Compute nodes coordinates by applying
        the loaded pattern to *geomBlock*. The (0,0,0) key-point
        will be mapped into *vertex000*. The (0,0,1)
        key-point will be mapped into *vertex001*.

        Parameters:
        :   - **geomBlock** (*GEOM.GEOM_Object*) – the geometrical block to generate volume elements on
            - **vertex000** (*GEOM.GEOM_Object*) – the vertex to superpose (0,0,0) key-point of pattern
            - **vertex001** (*GEOM.GEOM_Object*) – the vertex to superpose (0,0,1) key-point of pattern

        Returns:
        :   list of [`SMESH.PointStruct`](#SMESH.PointStruct) - computed coordinates of points of the pattern

    ApplyToMeshFaces(*mesh*, *facesIDs*, *nodeIndexOnKeyPoint1*, *toReverse*)
    :   Compute nodes coordinates by applying
        the loaded pattern to mesh faces. The first key-point
        will be mapped into *nodeIndexOnKeyPoint1* -th node of each mesh face

        Parameters:
        :   - **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – the mesh where to refine faces
            - **facesIDs** (*list_of_ids*) – IDs of faces to refine
            - **nodeIndexOnKeyPoint1** (*int*) – index of a face node to be at 1-st key-point of pattern
            - **toReverse** (*boolean*) – to reverse order of key-points

        Returns:
        :   list of [`SMESH.PointStruct`](#SMESH.PointStruct) - computed coordinates of points of the pattern

    ApplyToHexahedrons(*mesh*, *volumesIDs*, *node000Index*, *node001Index*)
    :   Compute nodes coordinates by applying
        the loaded pattern to hexahedra. The (0,0,0) key-point
        will be mapped into *Node000Index* -th node of each volume.
        The (0,0,1) key-point will be mapped into *node001Index* -th
        node of each volume.

        Parameters:
        :   - **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – the mesh where to refine hexahedra
            - **volumesIDs** (*list_of_ids*) – IDs of volumes to refine
            - **node000Index** (*long*) – index of a volume node to be at (0,0,0) key-point of pattern
            - **node001Index** (*long*) – index of a volume node to be at (0,0,1) key-point of pattern

        Returns:
        :   list of [`SMESH.PointStruct`](#SMESH.PointStruct) - computed coordinates of points of the pattern

    MakeMesh(*mesh*, *createPolygons*, *createPolyedrs*)
    :   Create nodes and elements in *mesh* using nodes
        coordinates computed by either of Apply…() methods.
        If *createPolygons* is True, replace adjacent faces by polygons
        to keep mesh conformity.
        If *createPolyedrs* is True, replace adjacent volumes by polyedrs
        to keep mesh conformity.

        Parameters:
        :   - **mesh** ([*SMESH.SMESH_Mesh*](#SMESH.SMESH_Mesh)) – the mesh to create nodes and elements in
            - **createPolygons** (*boolean*) – to create polygons to to keep mesh conformity
            - **createPolyedrs** (*boolean*) – to create polyherda to to keep mesh conformity

        Returns:
        :   True if succeeded

## SMESH_subMesh

*class* SMESH.SMESH_subMesh
:   [Sub-mesh](constructing_submeshes.md)

    GetNumberOfElements()
    :   Return number of elements in the sub-mesh

    GetNumberOfNodes(*all*)
    :   Return number of nodes in the sub-mesh

        Parameters:
        :   **all** (*boolean*) – if True, also return nodes assigned to boundary sub-meshes

    GetElementsId()
    :   Return IDs of elements in the sub-mesh

    GetNodesId()
    :   Return IDs of nodes in the sub-mesh

    GetSubShape()
    :   Return `geom shape` the sub-mesh is dedicated to

    GetId()
    :   Return ID of the `geom shape` the sub-mesh is dedicated to

    GetMeshInfo()
    :   Return number of mesh elements of each [`SMESH.EntityType`](#SMESH.EntityType).
        Use [`EnumToLong()`](smeshBuilder.md#smeshBuilder.smeshBuilder.EnumToLong) to get an integer from
        an item of [`SMESH.EntityType`](#SMESH.EntityType).

        Returns:
        :   array of number of elements per [`SMESH.EntityType`](#SMESH.EntityType)

    GetMesh()
    :   Return the [`SMESH.SMESH_Mesh`](#SMESH.SMESH_Mesh)

## SMESH_GroupBase

*class* SMESH.SMESH_GroupBase
:   [Mesh group](grouping_elements.md).
    Base class of [`standalone group`](#SMESH.SMESH_Group),
    [`group on geometry`](#SMESH.SMESH_GroupOnGeom) and
    [`group on filter`](#SMESH.SMESH_GroupOnFilter).
    Inherit all methods from [`SMESH_IDSource`](#SMESH.SMESH_IDSource).

    SetName(*name*)
    :   Set group name

    GetName()
    :   Return group name

    GetType()
    :   Return [`group type`](#SMESH.ElementType) (type of elements in the group)

    Size()
    :   Return the number of elements in the group

    IsEmpty()
    :   Return True if the group does not contain any elements

    Contains(*elem_id*)
    :   Return True if the group contains an element with ID == *elem_id*

    GetID(*elem_index*)
    :   Return ID of an element at position *elem_index* counted from 1

    GetNumberOfNodes()
    :   Return the number of nodes of cells included to the group.
        For a nodal group return the same value as Size() function

    GetNodeIDs()
    :   Return IDs of nodes of cells included to the group.
        For a nodal group return result of GetListOfID() function

    SetColor(*color*)
    :   Set group color

        Parameters:
        :   **color** (*SALOMEDS.Color*) – color

    GetColor()
    :   Return group color

        Returns:
        :   SALOMEDS.Color

## SMESH_Group

*class* SMESH.SMESH_Group
:   [Standalone mesh group](grouping_elements.md). Inherits all methods of [`SMESH.SMESH_GroupBase`](#SMESH.SMESH_GroupBase)

    Clear()
    :   Clears the group’s contents

    Add(*elem_ids*)
    :   Adds elements or nodes with specified identifiers to the group

        Parameters:
        :   **elem_ids** (*list_of_ids*) – IDs to add

    AddFrom(*idSource*)
    :   Add all elements or nodes from the specified source to the group

        Parameters:
        :   **idSource** ([*SMESH.SMESH_IDSource*](#SMESH.SMESH_IDSource)) – an object to retrieve IDs from

    Remove(*elem_ids*)
    :   Removes elements or nodes with specified identifiers from the group

        Parameters:
        :   **elem_ids** (*list_of_ids*) – IDs to remove

## SMESH_GroupOnGeom

*class* SMESH.SMESH_GroupOnGeom
:   Group linked to geometry. Inherits all methods of [`SMESH.SMESH_GroupBase`](#SMESH.SMESH_GroupBase)

    GetShape()
    :   Return an associated geometry

        Returns:
        :   GEOM.GEOM_Object

## SMESH_GroupOnFilter

*class* SMESH.SMESH_GroupOnFilter
:   Group defined by filter. Inherits all methods of [`SMESH.SMESH_GroupBase`](#SMESH.SMESH_GroupBase)

    SetFilter(*filter*)
    :   Set the [`filter`](#SMESH.Filter)

    GetFilter()
    :   Return the [`filter`](#SMESH.Filter)

## SMESH_IDSource

*class* SMESH.SMESH_IDSource
:   Base class for classes able to return IDs of mesh entities. These classes are:

    - [`SMESH.SMESH_Mesh`](#SMESH.SMESH_Mesh)
    - [`SMESH.SMESH_subMesh`](#SMESH.SMESH_subMesh)
    - [`SMESH.SMESH_GroupBase`](#SMESH.SMESH_GroupBase)
    - [`SMESH.Filter`](#SMESH.Filter)
    - temporal ID source created by [`GetIDSource()`](smeshBuilder.md#smeshBuilder.Mesh.GetIDSource)

    GetIDs()
    :   Return a sequence of all element IDs

    GetMeshInfo()
    :   Return number of mesh elements of each [`SMESH.EntityType`](#SMESH.EntityType).
        Use [`EnumToLong()`](smeshBuilder.md#smeshBuilder.smeshBuilder.EnumToLong) to get an integer from
        an item of [`SMESH.EntityType`](#SMESH.EntityType).

    GetNbElementsByType()
    :   Return number of mesh elements of each [`SMESH.ElementType`](#SMESH.ElementType).
        Use [`EnumToLong()`](smeshBuilder.md#smeshBuilder.smeshBuilder.EnumToLong) to get an integer from
        an item of [`SMESH.ElementType`](#SMESH.ElementType).

    GetTypes()
    :   Return types of elements it contains.
        It’s empty if the object contains no IDs

        Returns:
        :   list of [`SMESH.ElementType`](#SMESH.ElementType)

    GetMesh()
    :   Return the [`SMESH.SMESH_Mesh`](#SMESH.SMESH_Mesh)

## SMESH_Hypothesis

*class* SMESH.SMESH_Hypothesis
:   Base class of all [hypotheses](about_hypo.md)

    GetName()
    :   Return string of hypothesis type name, something like “Regular_1D”

    GetLibName()
    :   Return string of plugin library name
