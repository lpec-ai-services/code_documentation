<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/smeshBuilder.html -->

# smeshBuilder module

smeshBuilder.DegreesToRadians(*AngleInDegrees*)
:   Convert an angle from degrees to radians

smeshBuilder.GetName(*obj*)
:   Return a name of an object

    Returns:
    :   object name

smeshBuilder.New(*instance=None*, *instanceGeom=None*)
:   Create a new smeshBuilder instance. The smeshBuilder class provides the Python
    interface to create or load meshes.

    Typical use is:

    ```python
    import salome
    salome.salome_init()
    from salome.smesh import smeshBuilder
    smesh = smeshBuilder.New()
    ```

    Parameters:
    :   - **instance** – CORBA proxy of SMESH Engine. If None, the default Engine is used.
        - **instanceGeom** – CORBA proxy of GEOM Engine. If None, the default Engine is used.

    Returns:
    :   [`smeshBuilder`](#module-smeshBuilder) instance

## smeshBuilder class

*class* smeshBuilder.smeshBuilder(**args*)
:   This class allows to create, load or manipulate meshes.
    It has a set of methods to create, load or copy meshes, to combine several meshes, etc.
    It also has methods to get infos and measure meshes.

    BoundingBox(*objects*)
    :   Get bounding box of the specified object(s)

        Parameters:
        :   **objects** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – single source object or list of source objects

        Returns:
        :   tuple of six values (minX, minY, minZ, maxX, maxY, maxZ)

        See also

        [`GetBoundingBox()`](#smeshBuilder.smeshBuilder.GetBoundingBox)

    ColorToString(*c*)
    :   Convert SALOMEDS.Color to string.
        To be used with filters.

        Parameters:
        :   **c** – color value (SALOMEDS.Color)

        Returns:
        :   a string representation of the color.

    Concatenate(*meshes*, *uniteIdenticalGroups*, *mergeNodesAndElements=False*, *mergeTolerance=1e-05*, *allGroups=False*, *name=''*, *meshToAppendTo=None*)
    :   Concatenate the given meshes into one mesh, optionally to meshToAppendTo.
        All groups of input meshes will be present in the new mesh.

        Parameters:
        :   - **meshes** – [`meshes, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) to combine into one mesh
            - **uniteIdenticalGroups** – if True, groups with same names are united, else they are renamed
            - **mergeNodesAndElements** – if True, equal nodes and elements are merged
            - **mergeTolerance** – tolerance for merging nodes
            - **allGroups** – forces creation of groups corresponding to every input mesh
            - **name** – name of a new mesh
            - **meshToAppendTo** – a mesh to append all given meshes

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh)

        See also

        [`Mesh.Append()`](#smeshBuilder.Mesh.Append)

    CopyMesh(*meshPart*, *meshName*, *toCopyGroups=False*, *toKeepIDs=False*)
    :   Create a mesh by copying a part of another mesh.

        Parameters:
        :   - **meshPart** – a part of mesh to copy, either
              [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
              To copy nodes or elements not forming any mesh object,
              pass result of [`Mesh.GetIDSource()`](#smeshBuilder.Mesh.GetIDSource) as *meshPart*
            - **meshName** – a name of the new mesh
            - **toCopyGroups** – to create in the new mesh groups the copied elements belongs to
            - **toKeepIDs** – to preserve order of the copied elements or not

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh)

    CopyMeshWithGeom(*sourceMesh*, *newGeom*, *meshName=''*, *toCopyGroups=True*, *toReuseHypotheses=True*, *toCopyElements=True*)
    :   Create a mesh by copying a mesh definition (hypotheses and groups) to a new geometry.
        It is supposed that the new geometry is a modified geometry of *sourceMesh*.
        To facilitate and speed up the operation, consider using
        “Set presentation parameters and sub-shapes from arguments” option in
        a dialog of geometrical operation used to create the new geometry.

        Parameters:
        :   - **sourceMesh** – the mesh to copy definition of.
            - **newGeom** – the new geometry.
            - **meshName** – an optional name of the new mesh. If omitted, the mesh name is kept.
            - **toCopyGroups** – to create groups in the new mesh.
            - **toReuseHypotheses** – to reuse hypotheses of the *sourceMesh*.
            - **toCopyElements** – to copy mesh elements present on non-modified sub-shapes of
              *sourceMesh*.

        Returns:
        :   tuple ( ok, newMesh, newGroups, newSubMeshes, newHypotheses, invalidEntries )
            *invalidEntries* are study entries of objects whose
            counterparts are not found in the *newGeom*, followed by entries
            of mesh sub-objects that are invalid because they depend on a not found
            preceding sub-shape

    CreateDualMesh(*mesh*, *meshName*, *adaptToShape*)
    :   Create a dual of a mesh.

        Parameters:
        :   - **mesh** – Tetrahedron mesh
              [`mesh,`](smesh_module.md#SMESH.SMESH_IDSource).
            - **meshName** – a name of the new mesh
            - **adpatToShape** – if true project boundary points on shape

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh)

    CreateHypothesis(*theHType*, *theLibName='libStdMeshersEngine.so'*)
    :   Create hypothesis

        Parameters:
        :   - **theHType** (*string*) – mesh hypothesis type
            - **theLibName** (*string*) – mesh plug-in library name

        Returns:
        :   created hypothesis instance

    CreateMeshesFromCGNS(*theFileName*)
    :   Create Mesh objects importing data from the given CGNS file

        Returns:
        :   a tuple ( list of class [`Mesh`](#smeshBuilder.Mesh) instances, [`SMESH.DriverMED_ReadStatus`](smesh_module.md#SMESH.DriverMED_ReadStatus) )

    CreateMeshesFromGMF(*theFileName*)
    :   Create a Mesh object importing data from the given GMF file.
        GMF files must have .mesh extension for the ASCII format and .meshb for
        the binary format.

        Returns:
        :   ( an instance of class [`Mesh`](#smeshBuilder.Mesh), [`SMESH.ComputeError`](smesh_module.md#SMESH.ComputeError) )

    CreateMeshesFromGMSHIO(*theFileName*, *selectedFilter=''*)
    :   Create a Mesh object(s) importing data from from any file supported by gmsh library.

        Returns:
        :   a tuple ( list of class [`Mesh`](#smeshBuilder.Mesh) instances,
            [`SMESH.DriverMED_ReadStatus`](smesh_module.md#SMESH.DriverMED_ReadStatus) )

    CreateMeshesFromMED(*theFileName*)
    :   Create a Mesh object(s) importing data from the given MED file

        Returns:
        :   a tuple ( list of class [`Mesh`](#smeshBuilder.Mesh) instances,
            [`SMESH.DriverMED_ReadStatus`](smesh_module.md#SMESH.DriverMED_ReadStatus) )

    CreateMeshesFromMESHIO(*theFileName*, *selectedFilter=''*)
    :   Create a Mesh object(s) importing data from from any file supported by meshio library.

        Returns:
        :   a tuple ( list of class [`Mesh`](#smeshBuilder.Mesh) instances,
            [`SMESH.DriverMED_ReadStatus`](smesh_module.md#SMESH.DriverMED_ReadStatus) )

    CreateMeshesFromSTL(*theFileName*)
    :   Create a Mesh object importing data from the given STL file

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh)

    CreateMeshesFromUNV(*theFileName*)
    :   Create a Mesh object importing data from the given UNV file

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh)

    DumpPython(*theStudy*, *theIsPublished=True*, *theIsMultiFile=True*)
    :   Dump component to the Python script.
        This method overrides IDL function to allow default values for the parameters.

    EnumToLong(*theItem*)
    :   Return a long value from enumeration

    GetAngle(*p1*, *p2*, *p3*)
    :   Computes a radian measure of an angle defined by 3 points: <(p1,p2,p3)

        Parameters:
        :   - **p1** – coordinates of 3 points defined by either SMESH.PointStruct
              or list [x,y,z]
            - **p2** – coordinates of 3 points defined by either SMESH.PointStruct
              or list [x,y,z]
            - **p3** – coordinates of 3 points defined by either SMESH.PointStruct
              or list [x,y,z]

        Returns:
        :   Angle in radians

    GetArea(*obj*)
    :   Get sum of areas of all 2D elements in the mesh object.

        Parameters:
        :   **obj** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   sum of areas of all 2D elements

    GetAxisStruct(*theObj*)
    :   Get [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) from a geometrical object

        Parameters:
        :   **theObj** (*GEOM.GEOM_Object*) – line or plane

        Returns:
        :   [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct)

    GetBoundingBox(*objects*)
    :   Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying bounding box data of the specified object(s)

        Parameters:
        :   **objects** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – single source object or list of source objects

        Returns:
        :   [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure

        See also

        [`BoundingBox()`](#smeshBuilder.smeshBuilder.BoundingBox)

    GetCriterion(*elementType*, *CritType*, *Compare=FT_EqualTo*, *Threshold=''*, *UnaryOp=FT_Undefined*, *BinaryOp=FT_Undefined*, *Tolerance=1e-07*)
    :   Create a criterion by the given parameters
        Criterion structures allow to define complex filters by combining them with logical operations (AND / OR) (see example below)

        Parameters:
        :   - **elementType** – the [`type of elements`](smesh_module.md#SMESH.ElementType) (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME)
            - **CritType** – the type of criterion [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) (SMESH.FT_Taper, SMESH.FT_Area, etc.).
              Note that the items starting from FT_LessThan are not suitable for *CritType*.
            - **Compare** – belongs to {SMESH.FT_LessThan, SMESH.FT_MoreThan, SMESH.FT_EqualTo}
            - **Threshold** – the threshold value (range of ids as string, shape, numeric)
            - **UnaryOp** – SMESH.FT_LogicalNOT or SMESH.FT_Undefined
            - **BinaryOp** – a binary logical operation SMESH.FT_LogicalAND, SMESH.FT_LogicalOR or
              SMESH.FT_Undefined
            - **Tolerance** – the tolerance used by SMESH.FT_BelongToGeom, SMESH.FT_BelongToSurface,
              SMESH.FT_LyingOnGeom, SMESH.FT_CoplanarFaces criteria

        Returns:
        :   [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion)

        Example: [How to combine several criteria into a filter?](tui_filters.md#combining-filters)

    GetDirStruct(*theVector*)
    :   Get [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) from vector

        Parameters:
        :   **theVector** (*GEOM.GEOM_Object*) – vector

        Returns:
        :   [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct)

    GetEmptyCriterion()
    :   Create an empty criterion

        Returns:
        :   [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion)

    GetFilter(*elementType*, *CritType=FT_Undefined*, *Compare=FT_EqualTo*, *Threshold=''*, *UnaryOp=FT_Undefined*, *Tolerance=1e-07*, *mesh=None*)
    :   Create a filter with the given parameters

        Parameters:
        :   - **elementType** – the [`type of elements`](smesh_module.md#SMESH.ElementType) (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME)
            - **CritType** – the [`type of criterion`](smesh_module.md#SMESH.FunctorType) (SMESH.FT_Taper, SMESH.FT_Area, etc.).
              Note that the items starting from FT_LessThan are not suitable for CritType.
            - **Compare** – belongs to {SMESH.FT_LessThan, SMESH.FT_MoreThan, SMESH.FT_EqualTo}
            - **Threshold** – the threshold value (range of ids as string, shape, numeric)
            - **UnaryOp** – SMESH.FT_LogicalNOT or SMESH.FT_Undefined
            - **Tolerance** – the tolerance used by SMESH.FT_BelongToGeom, SMESH.FT_BelongToSurface,
              SMESH.FT_LyingOnGeom, SMESH.FT_CoplanarFaces and SMESH.FT_EqualNodes criteria
            - **mesh** – the mesh to initialize the filter with

        Returns:
        :   [`SMESH.Filter`](smesh_module.md#SMESH.Filter)

        Examples

        See [Filters usage examples](tui_filters.md)

    GetFilterFromCriteria(*criteria*, *binOp=FT_LogicalAND*)
    :   Create a filter from criteria

        Parameters:
        :   - **criteria** – a list of [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion)
            - **binOp** – binary operator used when binary operator of criteria is undefined

        Returns:
        :   [`SMESH.Filter`](smesh_module.md#SMESH.Filter)

        Examples

        See [Filters usage examples](tui_filters.md)

    GetFunctor(*theCriterion*)
    :   Create a numerical functor by its type

        Parameters:
        :   **theCriterion** ([*SMESH.FunctorType*](smesh_module.md#SMESH.FunctorType)) – functor type.
            Note that not all items correspond to numerical functors.

        Returns:
        :   [`SMESH.NumericalFunctor`](smesh_module.md#SMESH.NumericalFunctor)

    GetGravityCenter(*obj*)
    :   Get gravity center of all nodes of a mesh object.

        Parameters:
        :   **obj** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   Three components of the gravity center (x,y,z)

        See also

        [`Mesh.BaryCenter()`](#smeshBuilder.Mesh.BaryCenter)

    GetHypothesisParameterValues(*hypType*, *libName*, *mesh*, *shape*, *initParams*)
    :   Create hypothesis initialized according to parameters

        Parameters:
        :   - **hypType** (*string*) – hypothesis type
            - **libName** (*string*) – plug-in library name
            - **mesh** – optional mesh by which a hypotheses can initialize self
            - **shape** – optional geometry by size of which a hypotheses can initialize self
            - **initParams** – structure SMESH.HypInitParams defining how to initialize a hypothesis

        Returns:
        :   created hypothesis instance

    GetLength(*obj*)
    :   Get sum of lengths of all 1D elements in the mesh object.

        Parameters:
        :   **obj** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   sum of lengths of all 1D elements

    GetMeshInfo(*obj*)
    :   Get the mesh statistic.

        Returns:
        :   dictionary { [`SMESH.EntityType`](smesh_module.md#SMESH.EntityType) - “count of elements” }

    GetMinDistance(*src1*, *src2=None*, *id1=0*, *id2=0*, *isElem1=False*, *isElem2=False*)
    :   Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying minimum distance data between two objects

        - If *src2* is None, and *id2* = 0, distance from *src1* / *id1* to the origin is computed.
        - If *src2* is None, and *id2* != 0, it is assumed that both *id1* and *id2* belong to *src1*.

        Parameters:
        :   - **src1** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – first source object
            - **src2** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – second source object
            - **id1** (*int*) – node/element id from the first source
            - **id2** (*int*) – node/element id from the second (or first) source
            - **isElem1** (*boolean*) – *True* if **id1** is element id, *False* if it is node id
            - **isElem2** (*boolean*) – *True* if **id2** is element id, *False* if it is node id

        Returns:
        :   [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure or None if input data is invalid

        See also

        [`MinDistance()`](#smeshBuilder.smeshBuilder.MinDistance)

    GetPattern()
    :   Create a pattern mapper.

        Returns:
        :   an instance of [`SMESH.SMESH_Pattern`](smesh_module.md#SMESH.SMESH_Pattern)

        [Example of Patterns usage](tui_modifying_meshes.md#tui-pattern-mapping)

    GetPointStruct(*theVertex*)
    :   Get [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct) from vertex

        Parameters:
        :   **theVertex** (*GEOM.GEOM_Object*) – vertex

        Returns:
        :   [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)

    GetSubShapesId(*theMainObject*, *theListOfSubObjects*)
    :   Return IDs of sub-shapes

        Parameters:
        :   - **theMainObject** (*GEOM.GEOM_Object*) – a shape
            - **theListOfSubObjects** – sub-shapes (list of GEOM.GEOM_Object)

        Returns:
        :   the list of integer values

    GetVolume(*obj*)
    :   Get sum of volumes of all 3D elements in the mesh object.

        Parameters:
        :   **obj** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   sum of volumes of all 3D elements

    IsEmbeddedMode()
    :   Get the current mode

    MakeDirStruct(*x*, *y*, *z*)
    :   Make [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) from a triplet of floats

        Parameters:
        :   - **x** (*float*) – vector components
            - **y** (*float*) – vector components
            - **z** (*float*) – vector components

        Returns:
        :   [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct)

    Mesh(*obj=0*, *name=0*)
    :   Create a mesh. This mesh can be either

        - an empty mesh not bound to geometry, if *obj* == 0
        - an empty mesh bound to geometry, if *obj* is GEOM.GEOM_Object
        - a mesh wrapping a [`CORBA mesh`](smesh_module.md#SMESH.SMESH_Mesh) given as *obj* parameter.

        Parameters:
        :   - **obj** –

              either

              1. a [`CORBA mesh`](smesh_module.md#SMESH.SMESH_Mesh) got by calling e.g.

                 ```python
                 salome.myStudy.FindObjectID("0:1:2:3").GetObject()
                 ```
              2. a geometrical object for meshing
              3. none.
            - **name** – the name for the new mesh.

        Returns:
        :   an instance of class [`Mesh`](#smeshBuilder.Mesh).

    MinDistance(*src1*, *src2=None*, *id1=0*, *id2=0*, *isElem1=False*, *isElem2=False*)
    :   Get minimum distance between two objects

        - If *src2* is None, and *id2* = 0, distance from *src1* / *id1* to the origin is computed.
        - If *src2* is None, and *id2* != 0, it is assumed that both *id1* and *id2* belong to *src1*.

        Parameters:
        :   - **src1** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – first source object
            - **src2** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – second source object
            - **id1** (*int*) – node/element id from the first source
            - **id2** (*int*) – node/element id from the second (or first) source
            - **isElem1** (*boolean*) – *True* if *id1* is element id, *False* if it is node id
            - **isElem2** (*boolean*) – *True* if *id2* is element id, *False* if it is node id

        Returns:
        :   minimum distance value

        See also

        [`GetMinDistance()`](#smeshBuilder.smeshBuilder.GetMinDistance)

    ParallelMesh(*obj*, *name=0*, *split_geom=True*)
    :   Create a parallel mesh.

        Parameters:
        :   - **obj** – geometrical object for meshing
            - **name** – the name for the new mesh.
            - **split_geom** – If True split the geometry and create the associated
            - **meshes** (*sub*) –

        Returns:
        :   an instance of class [`ParallelMesh`](#smeshBuilder.smeshBuilder.ParallelMesh).

    ReloadMeshFromFile(*theMesh*)
    :   Desc for method,

    RemoveMesh(*mesh*)
    :   Delete a mesh

    SetBoundaryBoxSegmentation(*nbSegments*)
    :   Set number of segments per diagonal of boundary box of geometry, by which
        default segment length of appropriate 1D hypotheses is defined in GUI.
        Default value is 10.

    SetDumpPythonHistorical(*isHistorical*)
    :   Set mode of DumpPython(), *historical* or *snapshot*.
        In the *historical* mode, the Python Dump script includes all commands
        performed by SMESH engine. In the *snapshot* mode, commands
        relating to objects removed from the Study are excluded from the script
        as well as commands not influencing the current state of meshes

    SetEmbeddedMode(*theMode*)
    :   Set the current mode

    SetEnablePublish(*theIsEnablePublish*)
    :   Set enable publishing in the study. Calling SetEnablePublish( False ) allows to
        switch **off** publishing in the Study of mesh objects.

    SetName(*obj*, *name*)
    :   Set the given name to an object

        Parameters:
        :   - **obj** – the object to rename
            - **name** – a new object name

    UpdateStudy(*geompyD=None*)
    :   Update the current study. Calling UpdateStudy() allows to
        update meshes at switching GEOM->SMESH

    init_smesh(*geompyD=None*)
    :   Set Geometry component

## Mesh class

*class* smeshBuilder.Mesh(*smeshpyD*, *geompyD*, *obj=0*, *name=0*, *parallel=False*)
:   This class allows defining and managing a mesh.
    It has a set of methods to build a mesh on the given geometry, including the definition of sub-meshes.
    It also has methods to define groups of mesh elements, to modify a mesh (by addition of
    new nodes and elements and by changing the existing entities), to get information
    about a mesh and to export a mesh in different formats.

    Add0DElement(*IDOfNode*, *DuplicateElements=True*)
    :   Create a 0D element on a node with given number.

        Parameters:
        :   - **IDOfNode** – the ID of node for creation of the element.
            - **DuplicateElements** – to add one more 0D element to a node or not

        Returns:
        :   ID of the new 0D element

    Add0DElementsToAllNodes(*theObject*, *theGroupName=''*, *DuplicateElements=False*)
    :   Create 0D elements on all nodes of the given elements except those
        nodes on which a 0D element already exists.

        Parameters:
        :   - **theObject** – an object on whose nodes 0D elements will be created.
              It can be list of element IDs, [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **theGroupName** – optional name of a group to add 0D elements created
              and/or found on nodes of *theObject*.
            - **DuplicateElements** – to add one more 0D element to a node or not

        Returns:
        :   an object (a new group or a temporary [`SMESH.SMESH_IDSource`](smesh_module.md#SMESH.SMESH_IDSource)) holding
            IDs of new and/or found 0D elements. IDs of 0D elements
            can be retrieved from the returned object by
            calling [`GetIDs()`](smesh_module.md#SMESH.SMESH_IDSource.GetIDs)

    AddBall(*IDOfNode*, *diameter*)
    :   Create a ball element on a node with given ID.

        Parameters:
        :   - **IDOfNode** – the ID of node for creation of the element.
            - **diameter** – the bal diameter.

        Returns:
        :   ID of the new ball element

    AddEdge(*IDsOfNodes*)
    :   Create a linear or quadratic edge (this is determined
        by the number of given nodes).

        Parameters:
        :   **IDsOfNodes** – list of node IDs for creation of the element.
            The order of nodes in this list should correspond to
            the [connectivity convention](connectivity.md#connectivity-page).

        Returns:
        :   ID of the new edge

    AddFace(*IDsOfNodes*)
    :   Create a linear or quadratic face (this is determined
        by the number of given nodes).

        Parameters:
        :   **IDsOfNodes** – list of node IDs for creation of the element.
            The order of nodes in this list should correspond to
            the [connectivity convention](connectivity.md#connectivity-page).

        Returns:
        :   ID of the new face

    AddHypothesis(*hyp*, *geom=0*)
    :   Assign a hypothesis

        Parameters:
        :   - **hyp** – a hypothesis to assign
            - **geom** – a subhape of mesh geometry

        Returns:
        :   [`SMESH.Hypothesis_Status`](smesh_module.md#SMESH.Hypothesis_Status)

    AddNode(*x*, *y*, *z*)
    :   Add a node to the mesh by coordinates

        Returns:
        :   ID of the new node

    AddNodeOnFace(*face*, *x*, *y*, *z*)
    :   Split a face into triangles by adding a new node onto the face
        and connecting the new node with face nodes

        Parameters:
        :   - **face** – ID of the face
            - **x** – coordinates of the new node
            - **y** – coordinates of the new node
            - **z** – coordinates of the new node

    AddNodeOnSegment(*Node1*, *Node2*, *position=0.5*)
    :   Replace each triangle bound by Node1-Node2 segment with
        two triangles by connecting a node made on the link with a node
        opposite to the link.

        Parameters:
        :   - **Node1** – ID of the first node
            - **Node2** – ID of the second node
            - **position** – location [0,1] of the new node on the segment

    AddPolygonalFace(*IdsOfNodes*)
    :   Add a polygonal face defined by a list of node IDs

        Parameters:
        :   **IdsOfNodes** – the list of node IDs for creation of the element.

        Returns:
        :   ID of the new face

    AddPolyhedralVolume(*IdsOfNodes*, *Quantities*)
    :   Create a volume of many faces, giving nodes for each face.

        Parameters:
        :   - **IdsOfNodes** – list of node IDs for volume creation, face by face.
            - **Quantities** – list of integer values, Quantities[i]
              gives the quantity of nodes in face number i.

        Returns:
        :   ID of the new volumic element

    AddPolyhedralVolumeByFaces(*IdsOfFaces*)
    :   Create a volume of many faces, giving the IDs of the existing faces.

        Note

        The created volume will refer only to the nodes
        of the given faces, not to the faces themselves.

        Parameters:
        :   **IdsOfFaces** – the list of face IDs for volume creation.

        Returns:
        :   ID of the new volumic element

    AddQuadPolygonalFace(*IdsOfNodes*)
    :   Add a quadratic polygonal face defined by a list of node IDs

        Parameters:
        :   **IdsOfNodes** – the list of node IDs for creation of the element;
            corner nodes follow first.

        Returns:
        :   ID of the new face

    AddVolume(*IDsOfNodes*)
    :   Create both simple and quadratic volume (this is determined
        by the number of given nodes).

        Parameters:
        :   **IDsOfNodes** – list of node IDs for creation of the element.
            The order of nodes in this list should correspond to
            the [connectivity convention](connectivity.md#connectivity-page).

        Returns:
        :   ID of the new volumic element

    AdvancedExtrusion(*IDsOfElements*, *StepVector*, *NbOfSteps*, *ExtrFlags*, *SewTolerance*, *MakeGroups=False*)
    :   Generate new elements by extrusion of the elements with given ids

        Parameters:
        :   - **IDsOfElements** – is ids of elements
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **ExtrFlags** – sets flags for extrusion
            - **SewTolerance** – uses for comparing locations of nodes if flag
              EXTRUSION_FLAG_SEW is set
            - **MakeGroups** – forces the generation of new groups from existing ones

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    AffectedElemGroupsInRegion(*theElems*, *theNodesNot*, *theShape*)
    :   Identify the elements that will be affected by node duplication (actual duplication is not performed).
        This method is the first step of [`DoubleNodeElemGroupsInRegion()`](#smeshBuilder.Mesh.DoubleNodeElemGroupsInRegion).

        Parameters:
        :   - **theElems** – list of groups of nodes or elements (edges or faces) to replicate
            - **theNodesNot** – list of groups of nodes NOT to replicate
            - **theShape** – shape to detect affected elements (element which geometric center
              located on or inside shape).
              The replicated nodes should be associated to affected elements

        Returns:
        :   volumes, faces, edges

        Return type:
        :   groups of affected elements in order

    Append(*meshes*, *uniteIdenticalGroups=True*, *mergeNodesAndElements=False*, *mergeTolerance=1e-05*, *allGroups=False*)
    :   Append given meshes into this mesh.
        All groups of input meshes will be created in this mesh.

        Parameters:
        :   - **meshes** – [`meshes, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) to append
            - **uniteIdenticalGroups** – if True, groups with same names are united, else they are renamed
            - **mergeNodesAndElements** – if True, equal nodes and elements are merged
            - **mergeTolerance** – tolerance for merging nodes
            - **allGroups** – forces creation of groups corresponding to every input mesh

    AutomaticHexahedralization(*fineness=0*)
    :   Compute an hexahedral mesh using AutomaticLength + Quadrangle + Hexahedron

        Parameters:
        :   **fineness** – [0.0, 1.0] defines mesh fineness

        Returns:
        :   True or False

    AutomaticTetrahedralization(*fineness=0*)
    :   Compute a tetrahedral mesh using AutomaticLength + Triangle + Tetrahedron

        Parameters:
        :   **fineness** – [0.0,1.0] defines mesh fineness

        Returns:
        :   True or False

    BaryCenter(*id*)
    :   Return XYZ coordinates of the barycenter of the given element.
        If there is no element for the given ID - return an empty list

        Returns:
        :   a list of three double values

        See also

        [`smeshBuilder.GetGravityCenter()`](#smeshBuilder.smeshBuilder.GetGravityCenter)

    BestSplit(*IDOfQuad*, *theCriterion*)
    :   Find a better splitting of the given quadrangle.

        Parameters:
        :   - **IDOfQuad** – the ID of the quadrangle to be split.
            - **theCriterion** – is a numerical functor, in terms of enum [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType), used to
              choose a diagonal for splitting.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.

        Returns:
        :   - 1 if 1-3 diagonal is better,
            - 2 if 2-4 diagonal is better,
            - 0 if error occurs.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    BodyFitted(*geom_shape=0*)
    :   Create Body Fitting 3D algorithm for volumes

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Cartesian_3D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Cartesian_3D)

    BoundingBox(*objects=None*, *isElem=False*)
    :   Get bounding box of the specified object(s)

        Parameters:
        :   - **objects** – single [`source object`](smesh_module.md#SMESH.SMESH_IDSource) or list of source objects or list of nodes/elements IDs
            - **isElem** – if *objects* is a list of IDs, *True* value in this parameters specifies that *objects* are elements,
              *False* specifies that *objects* are nodes

        Returns:
        :   tuple of six values (minX, minY, minZ, maxX, maxY, maxZ)

        See also

        [`GetBoundingBox()`](#smeshBuilder.Mesh.GetBoundingBox)

    ChangeElemNodes(*ide*, *newIDs*)
    :   Set new nodes for the given element. Number of nodes should be kept.

        Parameters:
        :   - **ide** – the element ID
            - **newIDs** – nodes IDs

        Returns:
        :   False if the number of nodes does not correspond to the type of element

    CheckCompute()
    :   Check if the mesh was properly compute

    Clear(*refresh=False*)
    :   Remove all nodes and elements generated on geometry. Imported elements remain.

        Parameters:
        :   **refresh** – if *True*, Object browser is automatically updated (when running in GUI)

    ClearLastCreated()
    :   Forget what nodes and elements were created by the last mesh edition operation

    ClearLog()
    :   Clear the log of nodes and elements added or removed since the previous
        clear. Must be used immediately after [`GetLog()`](#smeshBuilder.Mesh.GetLog) if clearAfterGet is false.

    ClearSubMesh(*geomId*, *refresh=False*)
    :   Remove all nodes and elements of indicated shape

        Parameters:
        :   - **geomId** – the ID of a sub-shape to remove elements on
            - **refresh** – if *True*, Object browser is automatically updated (when running in GUI)

    Compute(*geom=0*, *discardModifs=False*, *refresh=False*)
    :   Compute the mesh and return the status of the computation

        Parameters:
        :   - **geom** – geomtrical shape on which mesh data should be computed
            - **discardModifs** – if True and the mesh has been edited since
              a last total re-compute and that may prevent successful partial re-compute,
              then the mesh is cleaned before Compute()
            - **refresh** – if *True*, Object Browser is automatically updated (when running in GUI)

        Returns:
        :   True or False

    ConvertFromQuadratic(*theSubMesh=None*)
    :   Convert the mesh from quadratic to ordinary,
        deletes old quadratic elements,
        replacing them with ordinary mesh elements with the same id.

        Parameters:
        :   **theSubMesh** – a [`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource) to convert

        Warning

        If *theSubMesh* is provided, the mesh can become non-conformal

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    ConvertToQuadratic(*theForce3d=False*, *theSubMesh=None*, *theToBiQuad=False*)
    :   Convert the mesh to quadratic or bi-quadratic, deletes old elements, replacing
        them with quadratic with the same id.

        Parameters:
        :   - **theForce3d** –

              method of new node creation:

              - False - the medium node lies at the geometrical entity from which the mesh element is built
              - True - the medium node lies at the middle of the line segments connecting two nodes of a mesh element
            - **theSubMesh** – a [`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource) to convert
            - **theToBiQuad** – If True, converts the mesh to bi-quadratic

        Returns:
        :   [`SMESH.ComputeError`](smesh_module.md#SMESH.ComputeError) which can hold a warning

        Warning

        If *theSubMesh* is provided, the mesh can become non-conformal

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    ConvertToStandalone(*group*)
    :   Convert group on geom into standalone group

    CreateDimGroup(*groups*, *elemType*, *name*, *nbCommonNodes=ALL_NODES*, *underlyingOnly=True*)
    :   Create a standalone group of entities basing on nodes of other groups.

        Parameters:
        :   - **groups** – list of [`sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource), of any type.
            - **elemType** – a type of elements to include to the new group; either of
              (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME).
            - **name** – a name of the new group.
            - **nbCommonNodes** –

              a criterion of inclusion of an element to the new group
              basing on number of element nodes common with reference *groups*.
              Meaning of possible values are:

              > - SMESH.ALL_NODES - include if all nodes are common,
              > - SMESH.MAIN - include if all corner nodes are common (meaningful for a quadratic mesh),
              > - SMESH.AT_LEAST_ONE - include if one or more node is common,
              > - SMEHS.MAJORITY - include if half of nodes or more are common.
            - **underlyingOnly** – if *True* (default), an element is included to the
              new group provided that it is based on nodes of an element of *groups*;
              in this case the reference *groups* are supposed to be of higher dimension
              than *elemType*, which can be useful for example to get all faces lying on
              volumes of the reference *groups*.

        Returns:
        :   an instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    CreateEmptyGroup(*elementType*, *name*)
    :   Create an empty standalone mesh group

        Parameters:
        :   - **elementType** – the [`type`](smesh_module.md#SMESH.ElementType) of elements in the group;
              either of (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME)
            - **name** – the name of the mesh group

        Returns:
        :   [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    CreateFlatElementsOnFacesGroups(*theGroupsOfFaces*)
    :   Double nodes on some external faces and create flat elements.
        Flat elements are mainly used by some types of mechanic calculations.

        Each group of the list must be constituted of faces.
        Triangles are transformed in prisms, and quadrangles in hexahedrons.

        Parameters:
        :   **theGroupsOfFaces** – list of groups of faces

        Returns:
        :   True if operation has been completed successfully, False otherwise

    CreateHoleSkin(*radius*, *theShape*, *groupName*, *theNodesCoords*)
    :   Identify all the elements around a geom shape, get the faces delimiting the hole

    CutGroups(*main_group*, *tool_group*, *name*)
    :   Produce a cut of two groups.
        A new group is created. All mesh elements that are present in
        the main group but are not present in the tool group are added to the new one

        Parameters:
        :   - **main_group** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – a group to cut from
            - **tool_group** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – a group to cut by

        Returns:
        :   an instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    CutListOfGroups(*main_groups*, *tool_groups*, *name*)
    :   Produce a cut of groups.
        A new group is created. All mesh elements that are present in main groups
        but do not present in tool groups are added to the new one

        Parameters:
        :   - **main_group** – groups to cut from (list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase))
            - **tool_group** – groups to cut by (list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase))

        Returns:
        :   an instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    DeleteDiag(*NodeID1*, *NodeID2*)
    :   Replace two neighbour triangles sharing *Node1-Node2* link
        with a quadrangle built on the same 4 nodes.

        Parameters:
        :   - **NodeID1** – ID of the first node
            - **NodeID2** – ID of the second node

        Returns:
        :   False if proper faces were not found

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    DoubleElements(*theElements*, *theGroupName=''*)
    :   Create duplicates of given elements, i.e. create new elements based on the
        same nodes as the given ones.

        Parameters:
        :   - **theElements** – container of elements to duplicate. It can be a
              [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource)
              or a list of element IDs. If *theElements* is
              a [`Mesh`](#smeshBuilder.Mesh), elements of highest dimension are duplicated
            - **theGroupName** – a name of group to contain the generated elements.
              If a group with such a name already exists, the new elements
              are added to the existing group, else a new group is created.
              If *theGroupName* is empty, new elements are not added
              in any group.

        Returns:
        :   a [`group`](smesh_module.md#SMESH.SMESH_Group) where the new elements are added.
            None if *theGroupName* == “”.

    DoubleNode(*theNodeId*, *theModifiedElems*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theNodeId** – IDs of node to double
            - **theModifiedElems** – IDs of elements to update

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodeElem(*theElems*, *theNodesNot*, *theAffectedElems*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements

        Parameters:
        :   - **theElems** – the list of elements (edges or faces) to replicate.
              The nodes for duplication could be found from these elements
            - **theNodesNot** – list of nodes NOT to replicate
            - **theAffectedElems** – the list of elements (cells and edges) to which the
              replicated nodes should be associated to

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodeElemGroup(*theElems*, *theNodesNot*, *theAffectedElems*, *theMakeGroup=False*, *theMakeNodeGroup=False*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theElems** – group of of elements (edges or faces) to replicate.
            - **theNodesNot** – group of nodes NOT to replicate.
            - **theAffectedElems** – group of elements to which the replicated nodes
              should be associated to.
            - **theMakeGroup** – forces the generation of a group containing new elements.
            - **theMakeNodeGroup** – forces the generation of a group containing new nodes.

        Returns:
        :   True or created groups (one or two) if operation has been completed successfully,
            False or None otherwise

    DoubleNodeElemGroupInRegion(*theElems*, *theNodesNot*, *theShape*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theElems** – group of of elements (edges or faces) to replicate
            - **theNodesNot** – group of nodes not to replicate
            - **theShape** – shape to detect affected elements (element which geometric center
              located on or inside shape).
              The replicated nodes should be associated to affected elements

    DoubleNodeElemGroups(*theElems*, *theNodesNot*, *theAffectedElems*, *theMakeGroup=False*, *theMakeNodeGroup=False*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theElems** – list of groups of elements (edges or faces) to replicate
            - **theNodesNot** – list of groups of nodes NOT to replicate
            - **theAffectedElems** – group of elements to which the replicated nodes
              should be associated to
            - **theMakeGroup** – forces generation of a group containing new elements.
            - **theMakeNodeGroup** – forces generation of a group containing new nodes

        Returns:
        :   True or created groups (one or two) if operation has been completed successfully,
            False or None otherwise

    DoubleNodeElemGroupsInRegion(*theElems*, *theNodesNot*, *theShape*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theElems** – list of groups of elements (edges or faces) to replicate
            - **theNodesNot** – list of groups of nodes NOT to replicate
            - **theShape** – shape to detect affected elements (element which geometric center
              located on or inside shape).
              The replicated nodes should be associated to affected elements

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodeElemInRegion(*theElems*, *theNodesNot*, *theShape*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements

        Parameters:
        :   - **theElems** – the list of elements (edges or faces) to replicate.
              The nodes for duplication could be found from these elements
            - **theNodesNot** – list of nodes NOT to replicate
            - **theShape** – shape to detect affected elements (element which geometric center
              located on or inside shape).
              The replicated nodes should be associated to affected elements.

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodeGroup(*theNodes*, *theModifiedElems*, *theMakeGroup=False*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theNodes** – group of nodes to double.
            - **theModifiedElems** – group of elements to update.
            - **theMakeGroup** – forces the generation of a group containing new nodes.

        Returns:
        :   True or a created group if operation has been completed successfully,
            False or None otherwise

    DoubleNodeGroups(*theNodes*, *theModifiedElems*, *theMakeGroup=False*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements.
        This method provided for convenience works as [`DoubleNodes()`](#smeshBuilder.Mesh.DoubleNodes).

        Parameters:
        :   - **theNodes** – list of groups of nodes to double.
            - **theModifiedElems** – list of groups of elements to update.
            - **theMakeGroup** – forces the generation of a group containing new nodes.

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodes(*theNodes*, *theModifiedElems*)
    :   Create a hole in a mesh by doubling the nodes of some particular elements

        Parameters:
        :   - **theNodes** – IDs of nodes to be doubled
            - **theModifiedElems** – IDs of elements to be updated by the new (doubled)
              nodes. If list of element identifiers is empty then nodes are doubled but
              they not assigned to elements

        Returns:
        :   True if operation has been completed successfully, False otherwise

    DoubleNodesOnGroupBoundaries(*theDomains*, *createJointElems*, *onAllBoundaries=False*)
    :   Double nodes on shared faces between groups of volumes and create flat elements on demand.
        The list of groups must describe a partition of the mesh volumes.
        The nodes of the internal faces at the boundaries of the groups are doubled.
        In option, the internal faces are replaced by flat elements.
        Triangles are transformed to prisms, and quadrangles to hexahedrons.

        Parameters:
        :   - **theDomains** – list of groups of volumes
            - **createJointElems** – if True, create the elements
            - **onAllBoundaries** – if True, the nodes and elements are also created on
              the boundary between *theDomains* and the rest mesh

        Returns:
        :   True if operation has been completed successfully, False otherwise

    Dump()
    :   Get the mesh description

        Returns:
        :   string value

    ElemNbEdges(*id*)
    :   Return the number of edges for the given element

    ElemNbFaces(*id*)
    :   Return the number of faces for the given element

    Evaluate(*geom=0*)
    :   Evaluate size of prospective mesh on a shape

        Returns:
        :   a list where i-th element is a number of elements of i-th [`SMESH.EntityType`](smesh_module.md#SMESH.EntityType).
            To know predicted number of e.g. edges, inquire it this way:

            ```python
            Evaluate()[ smesh.EnumToLong( SMESH.Entity_Edge )]
            ```

    ExportCGNS(*f*, *overwrite=1*, *meshPart=None*, *groupElemsByType=False*)
    :   Export the mesh in a file in CGNS format

        Parameters:
        :   - **f** – is the file name
            - **overwrite** – boolean parameter for overwriting/not overwriting the file
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh
            - **groupElemsByType** – if True all elements of same entity type are exported at ones,
              else elements are exported in order of their IDs which can cause creation
              of multiple cgns sections

    ExportDAT(*f*, *meshPart=None*, *renumber=True*)
    :   Export the mesh in a file in DAT format

        Parameters:
        :   - **f** – the file name
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh
            - **renumber** (*boolean*) – enable renumbering nodes and cells in order to eliminate holes in numbering

    ExportGMF(*f*, *meshPart=None*)
    :   Export the mesh in a file in GMF format.
        GMF files must have .mesh extension for the ASCII format and .meshb for
        the bynary format. Other extensions are not allowed.

        Parameters:
        :   - **f** – is the file name
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh

    ExportGMSHIO(*fileName*, *selectedFilter*, *meshPart*)
    :   Exports a part of mesh to a file with gmsh library
        through an intermediate MED file.

        Parameters described below are the same as for ExportMED() method.
        However, we know that _pyMesh::Process(const Handle(_pyCommand)& theCommand) method
        change a position of meshPart argument when dump to a Python script for whatever reason
        this way:
        - to 5th place for ExportMED command
        - to last place for the rest commands

        So, for this method meshPart moved to the end of the args.
        Look at src/SMESH_I/SMESH_2smeshpy.cxx for related source code.

        The same note is for the name of the method that was dumped as ExportPartToMESHIO(),
        but then processing just removes PartTo from the middle of the name as it was done
        for all export methods.

        Parameters:
        :   - **fileName** – is the file name
            - **selectedFilter** – filter string selected by user in a file dialog
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
              to export instead of the mesh

    ExportMED(**args*, ***kwargs*)
    :   Export the mesh in a file in MED format
        allowing to overwrite the file if it exists or add the exported data to its contents

        Parameters:
        :   - **fileName** – is the file name
            - **auto_groups** (*boolean*) – parameter for creating/not creating
              the groups Group_On_All_Nodes, Group_On_All_Faces, … ;
              the typical use is auto_groups=False.
            - **version** (*int*) – define the version (xy, where version is x.y.z) of MED file format.
              For instance med 3.2.1 is coded 3*10+2 = 32, med 4.0.0 is coded 4*10+0 = 40.
              The rules of compatibility to write a mesh in an older version than
              the current version depend on the current version. For instance,
              with med 4.0 it is possible to write/append med files in 4.0.0 (default)
              or 3.2.1 or 3.3.1 formats.
              If the version is equal to -1, the version is not changed (default).
            - **overwrite** (*boolean*) – parameter for overwriting/not overwriting the file
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
              to export instead of the mesh
            - **autoDimension** –

              if *True* (default), a space dimension of a MED mesh can be either

              - 1D if all mesh nodes lie on OX coordinate axis, or
              - 2D if all mesh nodes lie on XOY coordinate plane, or
              - 3D in the rest cases.

              If *autoDimension* is *False*, the space dimension is always 3.
            - **fields** – list of GEOM fields defined on the shape to mesh.
            - **geomAssocFields** –

              each character of this string means a need to export a
              corresponding field; correspondence between fields and characters
              is following:

              - ’v’ stands for “_vertices_” field;
              - ’e’ stands for “_edges_” field;
              - ’f’ stands for “_faces_” field;
              - ’s’ stands for “_solids_” field.
            - **zTolerance** (*float*) – tolerance in Z direction. If Z coordinate of a node is
              close to zero within a given tolerance, the coordinate is set to zero.
              If *ZTolerance* is negative (default), the node coordinates are kept as is.
            - **saveNumbers** (*boolean*) – enable saving numbers of nodes and cells.

    ExportMEDCoupling(**args*, ***kwargs*)
    :   Export the mesh in a memory representation.

        Parameters:
        :   - **auto_groups** (*boolean*) – parameter for creating/not creating
              the groups Group_On_All_Nodes, Group_On_All_Faces, … ;
              the typical use is auto_groups=False.
            - **overwrite** (*boolean*) – parameter for overwriting/not overwriting the file
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
              to export instead of the mesh
            - **autoDimension** –

              if *True* (default), a space dimension of a MED mesh can be either

              - 1D if all mesh nodes lie on OX coordinate axis, or
              - 2D if all mesh nodes lie on XOY coordinate plane, or
              - 3D in the rest cases.

              If *autoDimension* is *False*, the space dimension is always 3.
            - **fields** – list of GEOM fields defined on the shape to mesh.
            - **geomAssocFields** –

              each character of this string means a need to export a
              corresponding field; correspondence between fields and characters
              is following:

              - ’v’ stands for “_vertices_” field;
              - ’e’ stands for “_edges_” field;
              - ’f’ stands for “_faces_” field;
              - ’s’ stands for “_solids_” field.
            - **zTolerance** (*float*) – tolerance in Z direction. If Z coordinate of a node is
              close to zero within a given tolerance, the coordinate is set to zero.
              If *ZTolerance* is negative (default), the node coordinates are kept as is.
            - **saveNumbers** (*boolean*) – enable saving numbers of nodes and cells.

    ExportMESHIO(*fileName*, *selectedFilter*, *meshPart*)
    :   Exports a part of mesh to a file with meshio library
        through an intermediate MED file.

        Parameters described below are the same as for ExportMED() method.
        However, we know that _pyMesh::Process(const Handle(_pyCommand)& theCommand) method
        change a position of meshPart argument when dump to a Python script for whatever reason
        this way:
        - to 5th place for ExportMED command
        - to last place for the rest commands

        So, for this method meshPart moved to the end of the args.
        Look at src/SMESH_I/SMESH_2smeshpy.cxx for related source code.

        The same note is for the name of the method that was dumped as ExportPartToMESHIO(),
        but then processing just removes PartTo from the middle of the name as it was done
        for all export methods.

        Parameters:
        :   - **fileName** – is the file name
            - **selectedFilter** – filter string selected by user in a file dialog
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
              to export instead of the mesh

    ExportSTL(*f*, *ascii=1*, *meshPart=None*)
    :   Export the mesh in a file in STL format

        Parameters:
        :   - **f** – the file name
            - **ascii** – defines the file encoding
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh

    ExportStructuredCGNS(*f*, *overwrite=1*, *meshPart=None*)
    :   Export the mesh in a file in Structured CGNS format

        Parameters:
        :   - **f** – is the file name
            - **overwrite** – boolean parameter for overwriting/not overwriting the file
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh

    ExportToMED(**args*, ***kwargs*)
    :   Deprecated, used only for compatibility! Please, use [`ExportMED()`](#smeshBuilder.Mesh.ExportMED) method instead.
        Export the mesh in a file in MED format
        allowing to overwrite the file if it exists or add the exported data to its contents

        Parameters:
        :   - **fileName** – the file name
            - **opt** (*boolean*) – parameter for creating/not creating
              the groups Group_On_All_Nodes, Group_On_All_Faces, …
            - **overwrite** – boolean parameter for overwriting/not overwriting the file
            - **autoDimension** –

              if *True* (default), a space dimension of a MED mesh can be either

              - 1D if all mesh nodes lie on OX coordinate axis, or
              - 2D if all mesh nodes lie on XOY coordinate plane, or
              - 3D in the rest cases.

              If **autoDimension** is *False*, the space dimension is always 3.

    ExportToMEDX(**args*, ***kwargs*)
    :   Deprecated, used only for compatibility! Please, use ExportMED() method instead.
        Export the mesh in a file in MED format

        Parameters:
        :   - **fileName** – the file name
            - **opt** (*boolean*) – parameter for creating/not creating
              the groups Group_On_All_Nodes, Group_On_All_Faces, …
            - **overwrite** – boolean parameter for overwriting/not overwriting the file
            - **autoDimension** –

              if *True* (default), a space dimension of a MED mesh can be either

              - 1D if all mesh nodes lie on OX coordinate axis, or
              - 2D if all mesh nodes lie on XOY coordinate plane, or
              - 3D in the rest cases.

              If **autoDimension** is *False*, the space dimension is always 3.

    ExportUNV(*f*, *meshPart=None*, *renumber=True*)
    :   Export the mesh in a file in UNV format

        Parameters:
        :   - **f** – the file name
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to export instead of the mesh
            - **renumber** (*boolean*) – enable renumbering nodes and cells in order to eliminate holes in numbering

    ExtrusionAlongPath(*IDsOfElements*, *PathMesh*, *PathShape*, *NodeStart*, *HasAngles=False*, *Angles=[]*, *HasRefPoint=False*, *RefPoint=[]*, *MakeGroups=False*, *LinearVariation=False*)
    :   Generate new elements by extrusion of the given elements.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **IDsOfElements** – ids of elements
            - **PathMesh** – mesh containing a 1D sub-mesh on the edge, along which proceeds the extrusion
            - **PathShape** – shape (edge) defines the sub-mesh for the path
            - **NodeStart** – the first or the last node on the edge. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – the reference point around which the shape is rotated (the mass center of the shape by default).
              The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error)
            if *MakeGroups* == True, only [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) otherwise

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionAlongPathObject(*theObject*, *PathMesh*, *PathShape*, *NodeStart*, *HasAngles=False*, *Angles=[]*, *HasRefPoint=False*, *RefPoint=[]*, *MakeGroups=False*, *LinearVariation=False*)
    :   Generate new elements by extrusion of the elements which belong to the object.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **theObject** – the object whose elements should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **PathMesh** – mesh containing a 1D sub-mesh on the edge, along which the extrusion proceeds
            - **PathShape** – shape (edge) defines the sub-mesh for the path
            - **NodeStart** – the first or the last node on the edge. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – the reference point around which the shape is rotated (the mass center of the shape by default).
              The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) if *MakeGroups* == True,
            only [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) otherwise

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionAlongPathObject1D(*theObject*, *PathMesh*, *PathShape*, *NodeStart*, *HasAngles=False*, *Angles=[]*, *HasRefPoint=False*, *RefPoint=[]*, *MakeGroups=False*, *LinearVariation=False*)
    :   Generate new elements by extrusion of mesh segments which belong to the object.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **theObject** – the object whose 1D elements should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **PathMesh** – mesh containing a 1D sub-mesh on the edge, along which the extrusion proceeds
            - **PathShape** – shape (edge) defines the sub-mesh for the path
            - **NodeStart** – the first or the last node on the edge. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – the reference point around which the shape is rotated (the mass center of the shape by default).
              The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) if *MakeGroups* == True,
            only [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) otherwise

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionAlongPathObject2D(*theObject*, *PathMesh*, *PathShape*, *NodeStart*, *HasAngles=False*, *Angles=[]*, *HasRefPoint=False*, *RefPoint=[]*, *MakeGroups=False*, *LinearVariation=False*)
    :   Generate new elements by extrusion of faces which belong to the object.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **theObject** – the object whose 2D elements should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **PathMesh** – mesh containing a 1D sub-mesh on the edge, along which the extrusion proceeds
            - **PathShape** – shape (edge) defines the sub-mesh for the path
            - **NodeStart** – the first or the last node on the edge. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – the reference point around which the shape is rotated (the mass center of the shape by default).
              The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) if *MakeGroups* == True,
            only [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error) otherwise

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionAlongPathObjects(*Nodes*, *Edges*, *Faces*, *PathObject*, *PathShape=None*, *NodeStart=1*, *HasAngles=False*, *Angles=[]*, *LinearVariation=False*, *HasRefPoint=False*, *RefPoint=[0, 0, 0]*, *MakeGroups=False*, *ScaleFactors=[]*, *ScalesVariation=False*)
    :   Generate new elements by extrusion of the given elements and nodes along the path.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **Nodes** – nodes to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Edges** – edges to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Faces** – faces to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **PathObject** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource) containing edges along which proceeds the extrusion
            - **PathShape** – optional shape (edge or wire) which defines the sub-mesh of the mesh defined by *PathObject* if the mesh contains not only path segments, else it can be None
            - **NodeStart** – the first or the last node on the path. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – optional scaling and rotation center (mass center of the extruded
              elements by default). The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **ScaleFactors** – optional scale factors to apply during extrusion
            - **ScalesVariation** – if *True*, *scaleFactors* are spread over all *NbOfSteps*,
              else *scaleFactors* [i] is applied to nodes at the i-th extrusion step

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error)

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionAlongPathX(*Base*, *Path*, *NodeStart*, *HasAngles=False*, *Angles=[]*, *LinearVariation=False*, *HasRefPoint=False*, *RefPoint=[0, 0, 0]*, *MakeGroups=False*, *ElemType=FACE*)
    :   Generate new elements by extrusion of the given elements.
        The path of extrusion must be a meshed edge.

        Parameters:
        :   - **Base** – [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource), or list of ids of elements for extrusion
            - **Path** – 1D mesh or 1D sub-mesh, along which proceeds the extrusion
            - **NodeStart** – the start node from Path. Defines the direction of extrusion
            - **HasAngles** – not used obsolete
            - **Angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **LinearVariation** – forces the computation of rotation angles as linear
              variation of the given Angles along path steps
            - **HasRefPoint** – allows using the reference point
            - **RefPoint** – the reference point around which the elements are rotated (the mass
              center of the elements by default).
              The User can specify any point as the Reference Point.
              *RefPoint* can be either GEOM Vertex, [x,y,z] or [`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **ElemType** – type of elements for extrusion (if param Base is a mesh)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) and
            [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error)
            if *MakeGroups* == True, only [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Extrusion_Error)
            otherwise

        Example: [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path)

    ExtrusionByNormal(*Elements*, *StepSize*, *NbOfSteps*, *ByAverageNormal=False*, *UseInputElemsOnly=True*, *MakeGroups=False*, *Dim=2*)
    :   Generate new elements by extrusion along the normal to a discretized surface or wire

        Parameters:
        :   - **Elements** – elements to extrude - a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource).
              Only faces can be extruded so far. A sub-mesh should be a sub-mesh on geom faces.
            - **StepSize** – length of one extrusion step (the total extrusion
              length will be *NbOfSteps* *StepSize*).
            - **NbOfSteps** – number of extrusion steps.
            - **ByAverageNormal** – if True each node is translated by *StepSize*
              along the average of the normal vectors to the faces sharing the node;
              else each node is translated along the same average normal till
              intersection with the plane got by translation of the face sharing
              the node along its own normal by *StepSize*.
            - **UseInputElemsOnly** – to use only *Elements* when computing extrusion direction
              for every node of *Elements*.
            - **MakeGroups** – forces generation of new groups from existing ones.
            - **Dim** – dimension of elements to extrude: 2 - faces or 1 - edges. Extrusion of edges
              is not yet implemented. This parameter is used if *Elements* contains
              both faces and edges, i.e. *Elements* is a Mesh.

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True,
            empty list otherwise.

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    ExtrusionSweep(*IDsOfElements*, *StepVector*, *NbOfSteps*, *MakeGroups=False*, *IsNodes=False*)
    :   Generate new elements by extrusion of the elements with given ids

        Parameters:
        :   - **IDsOfElements** – the list of ids of elements or nodes for extrusion
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **IsNodes** – is True if elements with given ids are nodes

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    ExtrusionSweepObject(*theObject*, *StepVector*, *NbOfSteps*, *MakeGroups=False*, *IsNodes=False*)
    :   Generate new elements by extrusion of the elements or nodes which belong to the object

        Parameters:
        :   - **theObject** – the object whose elements or nodes should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **IsNodes** – is True if elements to extrude are nodes

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    ExtrusionSweepObject1D(*theObject*, *StepVector*, *NbOfSteps*, *MakeGroups=False*)
    :   Generate new elements by extrusion of edges which belong to the object

        Parameters:
        :   - **theObject** – object whose 1D elements should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **MakeGroups** – to generate new groups from existing ones

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    ExtrusionSweepObject2D(*theObject*, *StepVector*, *NbOfSteps*, *MakeGroups=False*)
    :   Generate new elements by extrusion of faces which belong to the object

        Parameters:
        :   - **theObject** – object whose 2D elements should be processed.
              It can be a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource).
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **MakeGroups** – forces the generation of new groups from existing ones

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    ExtrusionSweepObjects(*nodes*, *edges*, *faces*, *StepVector*, *NbOfSteps*, *MakeGroups=False*, *scaleFactors=[]*, *linearVariation=False*, *basePoint=[]*, *angles=[]*, *anglesVariation=False*)
    :   Generate new elements by extrusion of the given elements and nodes

        Parameters:
        :   - **nodes** – nodes to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **edges** – edges to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **faces** – faces to extrude: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **StepVector** – vector or [`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or 3 vector components, defining
              the direction and value of extrusion for one step (the total extrusion
              length will be NbOfSteps * ||StepVector||)
            - **NbOfSteps** – the number of steps
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **scaleFactors** – optional scale factors to apply during extrusion
            - **linearVariation** – if *True*, *scaleFactors* are spread over all *NbOfSteps*,
              else *scaleFactors* [i] is applied to nodes at the i-th extrusion step
            - **basePoint** –

              optional scaling and rotation center; if not provided, a gravity center of
              nodes and elements being extruded is used as the scaling center.
              It can be either

              > - a list of tree components of the point or
              > - a node ID or
              > - a GEOM point
            - **angles** – list of angles in radians. Nodes at each extrusion step are rotated
              around *basePoint*, additionally to previous steps.
            - **anglesVariation** – forces the computation of rotation angles as linear
              variation of the given *angles* along path steps

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

        Example: [Extrusion](tui_modifying_meshes.md#tui-extrusion)

    FaceGroupsSeparatedByEdges(*sharpAngle*, *createEdges=False*, *useExistingEdges=False*)
    :   Distribute all faces of the mesh among groups using sharp edges and optionally
        existing 1D elements as group boundaries.

        Parameters:
        :   - **sharpAngle** – edge is considered sharp if an angle between normals of
              adjacent faces is more than  sharpAngle in degrees.
            - **createEdges** (*boolean*) – to create 1D elements for detected sharp edges.
            - **useExistingEdges** (*boolean*) – to use existing edges as group boundaries

        Returns:
        :   ListOfGroups - the created [`groups`](smesh_module.md#SMESH.SMESH_Group)

    FillHole(*holeNodes*, *groupName=''*)
    :   Fill with 2D elements a hole defined by a SMESH.FreeBorder.

        Parameters:
        :   - **holeNodes** – either a SMESH.FreeBorder or a list on node IDs. These nodes
              must describe all sequential nodes of the hole border. The first and the last
              nodes must be the same. Use [`FindFreeBorders()`](#smeshBuilder.Mesh.FindFreeBorders) to get nodes of holes.
            - **groupName** (*string*) – name of a group to add new faces

        Returns:
        :   a [`group`](smesh_module.md#SMESH.SMESH_GroupBase) containing the new faces; or `None` if groupName == “”

    FindCoincidentFreeBorders(*tolerance=0.0*)
    :   Return groups of FreeBorder’s coincident within the given tolerance.

        Parameters:
        :   **tolerance** – the tolerance. If the tolerance <= 0.0 then one tenth of an average
            size of elements adjacent to free borders being compared is used.

        Returns:
        :   SMESH.CoincidentFreeBorders structure

    FindCoincidentNodes(*Tolerance*, *SeparateCornerAndMediumNodes=False*)
    :   Find groups of adjacent nodes within Tolerance.

        Parameters:
        :   - **Tolerance** (*float*) – the value of tolerance
            - **SeparateCornerAndMediumNodes** (*boolean*) – if *True*, in quadratic mesh puts
              corner and medium nodes in separate groups thus preventing
              their further merge.

        Returns:
        :   the list of groups of nodes IDs (e.g. [[1,12,13],[4,25]])

    FindCoincidentNodesOnPart(*SubMeshOrGroup*, *Tolerance*, *exceptNodes=[]*, *SeparateCornerAndMediumNodes=False*)
    :   Find groups of adjacent nodes within Tolerance.

        Parameters:
        :   - **Tolerance** – the value of tolerance
            - **SubMeshOrGroup** – list of [`sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) or of node IDs
            - **exceptNodes** – list of either SubMeshes, Groups or node IDs to exclude from search
            - **SeparateCornerAndMediumNodes** – if *True*, in quadratic mesh puts
              corner and medium nodes in separate groups thus preventing
              their further merge.

        Returns:
        :   the list of groups of nodes IDs (e.g. [[1,12,13],[4,25]])

    FindElementByNodes(*nodes*)
    :   Return an element based on all given nodes.

    FindElementsByPoint(*x*, *y*, *z*, *elementType=ALL*, *meshPart=None*)
    :   Find the elements where a point lays IN or ON

        Parameters:
        :   - **x** (*float*) – coordinates of the point
            - **y** (*float*) – coordinates of the point
            - **z** (*float*) – coordinates of the point
            - **elementType** ([*SMESH.ElementType*](smesh_module.md#SMESH.ElementType)) – type of elements to find; SMESH.ALL type
              means elements of any type excluding nodes, discrete and 0D elements.
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to search within

        Returns:
        :   list of IDs of found elements

    FindEqualElements(*MeshOrSubMeshOrGroup=None*, *exceptElements=[]*)
    :   Find the elements built on the same nodes.

        Parameters:
        :   - **MeshOrSubMeshOrGroup** – [`mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) or element IDs to check for equal elements
            - **exceptElements** – list of either SubMeshes, Groups or elements IDs to exclude from search

        Returns:
        :   the list of groups of equal elements IDs (e.g. [[1,12,13],[4,25]])

    FindFreeBorders(*ClosedOnly=True*)
    :   Returns all or only closed free borders

        Returns:
        :   list of SMESH.FreeBorder’s

    FindNodeClosestTo(*x*, *y*, *z*)
    :   Find the node closest to a point

        Parameters:
        :   - **x** – the X coordinate of a point
            - **y** – the Y coordinate of a point
            - **z** – the Z coordinate of a point

        Returns:
        :   the ID of a node

    FindSharpEdges(*angle*, *addExisting=False*)
    :   Return sharp edges of faces and non-manifold ones.
        Optionally add existing edges.

        Parameters:
        :   - **angle** – angle (in degrees) between normals of adjacent faces to detect sharp edges
            - **addExisting** – to return existing edges (1D elements) as well

        Returns:
        :   list of FaceEdge structures

    FunctorValue(*funcType*, *elemId*, *isElem=True*)
    :   Return value of a functor for a given element

        Parameters:
        :   - **funcType** – an item of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) enum.
            - **elemId** – element or node ID
            - **isElem** – *elemId* is ID of element or node

        Returns:
        :   the functor value or zero in case of invalid arguments

    Get1DBranches(*edges*, *startNode=0*)
    :   Partition given 1D elements into groups of contiguous edges.
        A node where number of meeting edges != 2 is a group end.
        An optional startNode is used to orient groups it belongs to.

        Returns:
        :   A list of edge groups and a list of corresponding node groups,
            where the group is a list of IDs of edges or nodes, like follows
            [[[branch_edges_1],[branch_edges_2]], [[branch_nodes_1],[branch_nodes_2]]].
            If a group is closed, the first and last nodes of the group are same.

    GetAlgoState(*theSubObject*)
    :   Return errors of hypotheses definition.
        The list of errors is empty if everything is OK.

        Parameters:
        :   **theSubObject** – a sub-shape of a mesh shape

        Returns:
        :   a list of errors

    GetAngle(*node1*, *node2*, *node3*)
    :   Computes a radian measure of an angle defined by 3 nodes: <(node1,node2,node3)

        Parameters:
        :   - **node1** – IDs of the three nodes
            - **node2** – IDs of the three nodes
            - **node3** – IDs of the three nodes

        Returns:
        :   Angle in radians [0,PI]. -1 if failure case.

    GetArea(*elemId=None*)
    :   Get area of given 2D elements or of all 2D mesh elements

        Parameters:
        :   **elemId** – either a mesh element ID or a list of IDs or [`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource). By default sum area of all 2D elements will be calculated.

        Returns:
        :   Area of given element’s if *elemId* is specified or sum of all 2D mesh elements’ areas otherwise

    GetAspectRatio(*elemId*)
    :   Get aspect ratio of 2D or 3D element.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s aspect ratio value

    GetAutoColor()
    :   Get flag of object auto color mode.

        Returns:
        :   True or False

    GetBallDiameter(*id*)
    :   Return diameter of a ball discrete element or zero in case of an invalid *id*

    GetBoundingBox(*objects=None*, *isElem=False*)
    :   Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying bounding box data of the specified object(s)

        Parameters:
        :   - **objects** – single [`source object`](smesh_module.md#SMESH.SMESH_IDSource) or list of source objects or list of nodes/elements IDs
            - **isElem** – if *objects* is a list of IDs, True means that *objects* are elements,
              False means that *objects* are nodes

        Returns:
        :   [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure

        See also

        [`BoundingBox()`](#smeshBuilder.Mesh.BoundingBox)

    GetComputeErrors(*shape=0*)
    :   Return a list of error messages ([`SMESH.ComputeError`](smesh_module.md#SMESH.ComputeError)) of the last [`Compute()`](#smeshBuilder.Mesh.Compute)

    GetElemFaceNodes(*elemId*, *faceIndex*)
    :   Return nodes of given face (counted from zero) for given volumic element.

    GetElemNbNodes(*id*)
    :   Return the number of nodes of the given element

        Returns:
        :   an integer value > 0 or -1 if there is no element for the given ID

    GetElemNode(*id*, *index*)
    :   Return the node ID the given (zero based) index for the given element.

        - If there is no element for the given ID - return -1.
        - If there is no node for the given index - return -2.

        Parameters:
        :   - **id** (*int*) – element ID
            - **index** (*int*) – node index within the element

        Returns:
        :   an integer value (ID)

        See also

        [`GetElemNodes()`](#smeshBuilder.Mesh.GetElemNodes)

    GetElemNodes(*id*)
    :   Return the IDs of nodes of the given element

        Returns:
        :   a list of integer values

    GetElementGeomType(*id*)
    :   Return the geometric type of mesh element

        Returns:
        :   the value from [`SMESH.EntityType`](smesh_module.md#SMESH.EntityType) enumeration.

    GetElementPosition(*ElemID*)
    :   Return the position of an element on the shape

        Returns:
        :   [`SMESH.ElementPosition`](smesh_module.md#SMESH.ElementPosition)

    GetElementShape(*id*)
    :   Return the shape type of mesh element

        Returns:
        :   the value from [`SMESH.GeometryType`](smesh_module.md#SMESH.GeometryType) enumeration.

    GetElementType(*id*, *iselem=True*)
    :   Return the type of mesh element or node

        Returns:
        :   the value from [`SMESH.ElementType`](smesh_module.md#SMESH.ElementType) enumeration.
            Return SMESH.ALL if element or node with the given ID does not exist

    GetElementsByNodes(*nodes*, *elemType=ALL*)
    :   Return elements including all given nodes.

    GetElementsByType(*elementType*)
    :   Return the list of IDs of mesh elements with the given type

        Parameters:
        :   **elementType** ([*SMESH.ElementType*](smesh_module.md#SMESH.ElementType)) – the required type of elements

        Returns:
        :   list of integer values

    GetElementsId()
    :   Return the list of all mesh elements IDs

        Returns:
        :   the list of integer values

        See also

        [`GetElementsByType()`](#smeshBuilder.Mesh.GetElementsByType)

    GetEngine()
    :   Return a smeshBuilder instance created this mesh

    GetFaceNormal(*faceId*, *normalized=False*)
    :   Return three components of normal of given mesh face
        (or an empty array in KO case)

    GetFailedShapes(*publish=False*)
    :   Return a list of sub-shapes meshing of which failed, grouped into GEOM groups by
        error of an algorithm

        Parameters:
        :   **publish** – if *True*, the returned groups will be published in the study

        Returns:
        :   a list of GEOM groups each named after a failed algorithm

    GetFreeBorders()
    :   Verify whether a 2D mesh element has free edges (edges connected to one face only).
        Return a list of special structures (borders).

        Returns:
        :   a list of [`SMESH.FreeEdges.Border`](smesh_module.md#SMESH.FreeEdges.Border)

    GetFunctor(*funcType*)
    :   Return a cached numerical functor by its type.

        Parameters:
        :   **funcType** – functor type: an item of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) enumeration.
            Note that not all items correspond to numerical functors.

        Returns:
        :   [`SMESH.NumericalFunctor`](smesh_module.md#SMESH.NumericalFunctor). The functor is already initialized with a mesh

    GetGeomEngine()
    :   Return a geomBuilder instance

    GetGeometryByMeshElement(*theElementID*, *theGeomName*)
    :   Return a geometrical object on which the given element was built.
        The returned geometrical object, if not nil, is either found in the
        study or published by this method with the given name

        Parameters:
        :   - **theElementID** – the id of the mesh element
            - **theGeomName** – the user-defined name of the geometrical object

        Returns:
        :   GEOM.GEOM_Object instance

    GetGroupByName(*name*, *elemType=None*)
    :   Find groups by name and type

        Parameters:
        :   - **name** (*string*) – name of the group of interest
            - **elemType** ([*SMESH.ElementType*](smesh_module.md#SMESH.ElementType)) – type of elements the groups contain;
              by default one group of any type is returned;
              if elemType == SMESH.ALL then all groups of any type are returned

        Returns:
        :   a list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase)

    GetGroupNames()
    :   Get the list of names of groups existing in the mesh

        Returns:
        :   list of strings

    GetGroups(*elemType=ALL*)
    :   Get the list of groups existing in the mesh in the order of creation
        (starting from the oldest one)

        Parameters:
        :   **elemType** ([*SMESH.ElementType*](smesh_module.md#SMESH.ElementType)) – type of elements the groups contain;
            by default groups of elements of all types are returned

        Returns:
        :   a list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase)

    GetHypothesisList(*geom*)
    :   Get the list of hypotheses added on a geometry

        Parameters:
        :   **geom** (*GEOM.GEOM_Object*) – a sub-shape of mesh geometry

        Returns:
        :   the sequence of [`SMESH.SMESH_Hypothesis`](smesh_module.md#SMESH.SMESH_Hypothesis)

    GetIDSource(*ids*, *elemType=ALL*)
    :   Wrap a list of IDs of elements or nodes into [`SMESH.SMESH_IDSource`](smesh_module.md#SMESH.SMESH_IDSource) which
        can be passed as argument to a method accepting [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Parameters:
        :   - **ids** – list of IDs
            - **elemType** – type of elements; this parameter is used to distinguish
              IDs of nodes from IDs of elements; by default ids are treated as
              IDs of elements; use SMESH.NODE if ids are IDs of nodes.

        Returns:
        :   an instance of [`SMESH.SMESH_IDSource`](smesh_module.md#SMESH.SMESH_IDSource)

        Warning

        call UnRegister() for the returned object as soon as it is no more useful:

        ```python
        idSrc = mesh.GetIDSource( [1,3,5], SMESH.NODE )
        mesh.DoSomething( idSrc )
        idSrc.UnRegister()
        ```

    GetId()
    :   Get the internal ID

        Returns:
        :   integer value, which is the internal Id of the mesh

    GetIdsFromFilter(*filter*, *meshParts=[]*)
    :   Pass mesh elements through the given filter and return IDs of fitting elements

        Parameters:
        :   - **filter** – [`SMESH.Filter`](smesh_module.md#SMESH.Filter)
            - **meshParts** – list of mesh parts ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to filter

        Returns:
        :   a list of ids

        See also

        [`SMESH.Filter.GetIDs()`](smesh_module.md#SMESH.Filter.GetIDs)
        `SMESH.Filter.GetElementsIdFromParts()`

    GetLastCreatedElems()
    :   If during the last operation of [`SMESH.SMESH_MeshEditor`](smesh_module.md#SMESH.SMESH_MeshEditor) some elements were
        created this method return the list of their IDs.
        If new elements were not created - return empty list

        Returns:
        :   the list of integer values (can be empty)

    GetLastCreatedNodes()
    :   If during the last operation of [`SMESH.SMESH_MeshEditor`](smesh_module.md#SMESH.SMESH_MeshEditor) some nodes were
        created, this method return the list of their IDs.
        If new nodes were not created - return empty list

        Returns:
        :   the list of integer values (can be empty)

    GetLength(*elemId=None*)
    :   Get length of given 1D elements or of all 1D mesh elements

        Parameters:
        :   **elemId** – either a mesh element ID or a list of IDs or [`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource). By default sum length of all 1D elements will be calculated.

        Returns:
        :   Sum of lengths of given elements

    GetLog(*clearAfterGet*)
    :   Return the log of nodes and elements added or removed
        since the previous clear of the log.

        Parameters:
        :   **clearAfterGet** – log is emptied after Get (safe if concurrents access)

        Returns:
        :   list of SMESH.log_block structures { commandType, number, coords, indexes }

    GetMaxElementLength(*elemId*)
    :   Get maximum element length.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s maximum length value

    GetMesh()
    :   Return the mesh, that is an encapsulated instance of [`SMESH.SMESH_Mesh`](smesh_module.md#SMESH.SMESH_Mesh) interface

        Returns:
        :   a [`SMESH.SMESH_Mesh`](smesh_module.md#SMESH.SMESH_Mesh) object

    GetMeshEditor()
    :   Obtain the mesh editor tool

        Returns:
        :   an instance of [`SMESH.SMESH_MeshEditor`](smesh_module.md#SMESH.SMESH_MeshEditor)

    GetMeshInfo(*obj=None*)
    :   Get the mesh statistic.

        Returns:
        :   dictionary { [`SMESH.EntityType`](smesh_module.md#SMESH.EntityType) - “count of elements” }

    GetMeshOrder()
    :   Return sub-mesh objects list in meshing order

        Returns:
        :   list of lists of [`sub-meshes`](smesh_module.md#SMESH.SMESH_subMesh)

    GetMinDistance(*id1*, *id2=0*, *isElem1=False*, *isElem2=False*)
    :   Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying minimum distance data between two objects

        Parameters:
        :   - **id1** – first node/element id
            - **id2** – second node/element id (if 0, distance from *id1* to the origin is computed)
            - **isElem1** – *True* if *id1* is element id, *False* if it is node id
            - **isElem2** – *True* if *id2* is element id, *False* if it is node id

        Returns:
        :   [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure

        See also

        [`MinDistance()`](#smeshBuilder.Mesh.MinDistance)

    GetMinMax(*funType*, *meshPart=None*)
    :   Return minimal and maximal value of a given functor.

        Parameters:
        :   - **funType** ([*SMESH.FunctorType*](smesh_module.md#SMESH.FunctorType)) – a functor type.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.
            - **meshPart** – a part of mesh ([`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) to treat

        Returns:
        :   tuple (min,max)

    GetMinimumAngle(*elemId*)
    :   Get minimum angle of 2D element.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s minimum angle value

    GetName()
    :   Get the name of the mesh

        Returns:
        :   the name of the mesh as a string

    GetNodeInverseElements(*id*, *elemType=ALL*)
    :   Return list of IDs of inverse elements for the given node.
        If there is no node for the given ID - return an empty list

        Parameters:
        :   - **id** – node ID
            - **elementType** – [`type of elements`](smesh_module.md#SMESH.ElementType) (SMESH.EDGE, SMESH.FACE, SMESH.VOLUME, etc.)

        Returns:
        :   list of integer values

    GetNodePosition(*NodeID*)
    :   Return the position of a node on the shape

        Returns:
        :   [`SMESH.NodePosition`](smesh_module.md#SMESH.NodePosition)

    GetNodeXYZ(*id*)
    :   Get XYZ coordinates of a node.
        If there is no node for the given ID - return an empty list

        Returns:
        :   list of float values

    GetNodesId()
    :   Return the list of mesh nodes IDs

        Returns:
        :   the list of integer values

    GetPointState(*x*, *y*, *z*)
    :   Return point state in a closed 2D mesh in terms of TopAbs_State enumeration:
        smesh.TopAbs_IN, smesh.TopAbs_OUT, smesh.TopAbs_ON and smesh.TopAbs_UNKNOWN.
        UNKNOWN state means that either mesh is wrong or the analysis fails.

    GetScaledJacobian(*elemId*)
    :   Get the scaled jacobian of 3D element id

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   the scaled jacobian

    GetShape()
    :   Return the shape associated to the mesh

        Returns:
        :   a GEOM_Object

    GetShapeID(*id*)
    :   Return the ID of the shape, on which the given node was generated.

        Returns:
        :   an integer value > 0 or -1 if there is no node for the given
            ID or the node is not assigned to any geometry

    GetShapeIDForElem(*id*)
    :   Return the ID of the shape, on which the given element was generated.

        Returns:
        :   an integer value > 0 or -1 if there is no element for the given
            ID or the element is not assigned to any geometry

    GetSkew(*elemId*)
    :   Get skew of 2D element.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s skew value

    GetSubMesh(*geom*, *name*)
    :   Get a sub-mesh object associated to a *geom* geometrical object.

        Parameters:
        :   - **geom** – a geometrical object (shape)
            - **name** – a name for the sub-mesh in the Object Browser

        Returns:
        :   an object of type [`SMESH.SMESH_subMesh`](smesh_module.md#SMESH.SMESH_subMesh), representing a part of mesh,
            which lies on the given shape

        Note

        A sub-mesh is implicitly created when a sub-shape is specified at
        creating an algorithm, for example:

        ```python
        algo1D = mesh.Segment(geom=Edge_1)
        ```

        create a sub-mesh on *Edge_1* and assign Wire Discretization algorithm to it.
        The created sub-mesh can be retrieved from the algorithm:

        ```python
        submesh = algo1D.GetSubMesh()
        ```

    GetSubMeshElementType(*Shape*)
    :   Return type of elements on given shape

        Parameters:
        :   **Shape** – a geom object (sub-shape).
            *Shape* must be a sub-shape of a ShapeToMesh()

        Returns:
        :   [`SMESH.ElementType`](smesh_module.md#SMESH.ElementType)

    GetSubMeshElementsId(*Shape*)
    :   Return the list of sub-mesh elements IDs

        Parameters:
        :   **Shape** (*GEOM.GEOM_Object*) – a geom object (sub-shape).
            *Shape* must be the sub-shape of the [`main shape`](#smeshBuilder.Mesh.GetShape)

        Returns:
        :   list of integer values

    GetSubMeshNodesId(*Shape*, *all*)
    :   Return the list of sub-mesh nodes IDs

        Parameters:
        :   - **Shape** – a geom object (sub-shape).
              *Shape* must be the sub-shape of a [`GetShape()`](#smeshBuilder.Mesh.GetShape)
            - **all** – If True, gives all nodes of sub-mesh elements, otherwise gives only sub-mesh nodes

        Returns:
        :   list of integer values

    GetSubShapeName(*subShapeID*)
    :   Return a name of a sub-shape by its ID.
        Possible variants (for *subShapeID* == 3):

        > - **“Face_12”** - published sub-shape
        > - **FACE #3** - not published sub-shape
        > - **sub-shape #3** - invalid sub-shape ID
        > - **#3** - error in this function

        Parameters:
        :   **subShapeID** – a unique ID of a sub-shape

        Returns:
        :   a string describing the sub-shape

    GetTaper(*elemId*)
    :   Get taper of 2D element.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s taper value

    GetVolume(*elemId=None*)
    :   Get volume of given 3D elements or of all 3D mesh elements

        Parameters:
        :   **elemId** – either a mesh element ID or a list of IDs or [`sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource). By default sum volume of all 3D elements will be calculated.

        Returns:
        :   Sum element’s volume value if *elemId* is specified or sum of all 3D mesh elements’ volumes otherwise

    GetWarping(*elemId*)
    :   Get warping angle of 2D element.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s warping angle value

    GetWarping3D(*elemId*)
    :   Get warping angle of faces element of 3D elements.

        Parameters:
        :   **elemId** – mesh element ID

        Returns:
        :   element’s warping angle value

    Group(*grp*, *name=''*)
    :   Create a mesh group based on the geometric object *grp*
        and give it a *name*.
        If *name* is not defined the name of the geometric group is used

        Note

        Works like [`GroupOnGeom()`](#smeshBuilder.Mesh.GroupOnGeom).

        Parameters:
        :   - **grp** – a geometric group, a vertex, an edge, a face or a solid
            - **name** – the name of the mesh group

        Returns:
        :   [`SMESH.SMESH_GroupOnGeom`](smesh_module.md#SMESH.SMESH_GroupOnGeom)

    GroupOnFilter(*typ*, *name*, *filter*)
    :   Create a mesh group with given *name* based on the *filter*.
        It is a special type of group dynamically updating it’s contents during
        mesh modification

        Parameters:
        :   - **typ** – the type of elements in the group; either of
              (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME).
            - **name** – the name of the mesh group
            - **filter** ([*SMESH.Filter*](smesh_module.md#SMESH.Filter)) – the filter defining group contents

        Returns:
        :   [`SMESH.SMESH_GroupOnFilter`](smesh_module.md#SMESH.SMESH_GroupOnFilter)

    GroupOnGeom(*grp*, *name=''*, *typ=None*)
    :   Create a mesh group based on the geometrical object *grp*
        and give it a *name*.
        if *name* is not defined the name of the geometric group is used

        Parameters:
        :   - **grp** – a geometrical group, a vertex, an edge, a face or a solid
            - **name** – the name of the mesh group
            - **typ** – the type of elements in the group; either of
              (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME). If not set, it is
              automatically detected by the type of the geometry

        Returns:
        :   [`SMESH.SMESH_GroupOnGeom`](smesh_module.md#SMESH.SMESH_GroupOnGeom)

    HasDuplicatedGroupNamesMED()
    :   Check the group names for duplications.
        Consider the maximum group name length stored in MED file.

        Returns:
        :   True or False

    HasShapeToMesh()
    :   Return `True` if this mesh is based on geometry

    Hexahedron(*geom_shape=0*)
    :   Create hexahedron 3D algorithm for volumes

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Hexahedron`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Hexahedron)

    IntersectGroups(*group1*, *group2*, *name*)
    :   Prodice an intersection of two groups.
        A new group is created. All mesh elements that are common
        for the two initial groups are added to the new one.

        Parameters:
        :   - **group1** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – a group
            - **group2** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – another group

        Returns:
        :   instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    IntersectListOfGroups(*groups*, *name*)
    :   Produce an intersection of groups.
        New group is created. All mesh elements that are present in all
        initial groups simultaneously are added to the new one

        Parameters:
        :   **groups** – a list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase)

        Returns:
        :   instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    InverseDiag(*NodeID1*, *NodeID2*)
    :   Replace two neighbour triangles sharing Node1-Node2 link
        with the triangles built on the same 4 nodes but having other common link.

        Parameters:
        :   - **NodeID1** – the ID of the first node
            - **NodeID2** – the ID of the second node

        Returns:
        :   False if proper faces were not found

    IsCoherentOrientation2D()
    :   Check if orientation of 2D elements is coherent

    IsManifold()
    :   Check if a 2D mesh is manifold

    IsMediumNode(*elementID*, *nodeID*)
    :   Return true if the given node is the medium node in the given quadratic element

    IsMediumNodeOfAnyElem(*nodeID*, *elementType=ALL*)
    :   Return true if the given node is the medium node in one of quadratic elements

        Parameters:
        :   - **nodeID** – ID of the node
            - **elementType** – the type of elements to check a state of the node, either of
              (SMESH.ALL, SMESH.NODE, SMESH.EDGE, SMESH.FACE or SMESH.VOLUME)

    IsPoly(*id*)
    :   Return true if the given element is a polygon

    IsQuadratic(*id*)
    :   Return true if the given element is quadratic

    IsReadyToCompute(*theSubObject*)
    :   Return true if the hypotheses are defined well

        Parameters:
        :   **theSubObject** – a sub-shape of a mesh shape

        Returns:
        :   True or False

    IsUsedHypothesis(*hyp*, *geom*)
    :   Return True if an algorithm or hypothesis is assigned to a given shape

        Parameters:
        :   - **hyp** – an algorithm or hypothesis to check
            - **geom** – a subhape of mesh geometry

        Returns:
        :   True of False

    Load()
    :   Load mesh from the study after opening the study

    Make2DMeshFrom3D()
    :   Create 2D mesh as skin on boundary faces of a 3D mesh

        Returns:
        :   True if operation has been completed successfully, False otherwise

    MakeBoundaryElements(*dimension=BND_2DFROM3D*, *groupName=''*, *meshName=''*, *toCopyAll=False*, *groups=[]*)
    :   Create missing boundary elements around either the whole mesh or
        groups of elements

        Parameters:
        :   - **dimension** – defines type of boundary elements to create, either of
              { SMESH.BND_2DFROM3D, SMESH.BND_1DFROM3D, SMESH.BND_1DFROM2D }
            - **groupName** – a name of group to store all boundary elements in,
              “” means not to create the group
            - **meshName** – a name of a new mesh, which is a copy of the initial
              mesh + created boundary elements; “” means not to create the new mesh
            - **toCopyAll** – if True, the whole initial mesh will be copied into
              the new mesh else only boundary elements will be copied into the new mesh
            - **groups** – list of [`sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) of elements to make boundary around

        Returns:
        :   tuple( long, mesh, group )
            :   - long - number of added boundary elements
                - mesh - the [`Mesh`](#smeshBuilder.Mesh) where elements were added to
                - group - the [`group`](smesh_module.md#SMESH.SMESH_Group) of boundary elements or None

    MakeBoundaryMesh(*elements*, *dimension=BND_2DFROM3D*, *groupName=''*, *meshName=''*, *toCopyElements=False*, *toCopyExistingBondary=False*)
    :   Create missing boundary elements

        Parameters:
        :   - **elements** – elements whose boundary is to be checked:
              [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) or list of elements.
              If *elements* is mesh, it must be the mesh whose MakeBoundaryMesh() is called
            - **dimension** – defines type of boundary elements to create, either of
              { SMESH.BND_2DFROM3D, SMESH.BND_1DFROM3D, SMESH.BND_1DFROM2D }.
              SMESH.BND_1DFROM3D create mesh edges on all borders of free facets of 3D cells
            - **groupName** – a name of group to store created boundary elements in,
              “” means not to create the group
            - **meshName** – a name of new mesh to store created boundary elements in,
              “” means not to create the new mesh
            - **toCopyElements** – if True, the checked elements will be copied into
              the new mesh else only boundary elements will be copied into the new mesh
            - **toCopyExistingBondary** – if True, not only new but also pre-existing
              boundary elements will be copied into the new mesh

        Returns:
        :   tuple ([`Mesh`](#smeshBuilder.Mesh), [`group`](smesh_module.md#SMESH.SMESH_Group)) where boundary elements were added to

    MakeBoundaryOfEachElement(*groupName=''*, *meshName=''*, *toCopyAll=False*, *groups=[]*)
    :   Create boundary elements around the whole mesh or groups of elements

        Parameters:
        :   - **groupName** – a name of group to store all boundary elements in,
              “” means not to create the group
            - **meshName** – a name of a new mesh, which is a copy of the initial
              mesh + created boundary elements; “” means not to create the new mesh
            - **toCopyAll** – if True, the whole initial mesh will be copied into
              the new mesh else only boundary elements will be copied into the new mesh
            - **groups** – list of [`sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource) of elements to make boundary around

        Returns:
        :   tuple( long, mesh, group )
            :   - long - number of added boundary elements
                - mesh - the [`Mesh`](#smeshBuilder.Mesh) where elements were added to
                - group - the [`group`](smesh_module.md#SMESH.SMESH_Group) of boundary elements or None

    MakeGroup(*groupName*, *elementType*, *CritType=FT_Undefined*, *Compare=FT_EqualTo*, *Threshold=''*, *UnaryOp=FT_Undefined*, *Tolerance=1e-07*)
    :   Create a mesh group by the given conditions

        Parameters:
        :   - **groupName** – the name of the mesh group
            - **elementType** ([*SMESH.ElementType*](smesh_module.md#SMESH.ElementType)) – the type of elements (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME)
            - **CritType** ([*SMESH.FunctorType*](smesh_module.md#SMESH.FunctorType)) – the type of criterion (SMESH.FT_Taper, SMESH.FT_Area, etc.).
              Note that the items starting from FT_LessThan are not suitable for CritType.
            - **Compare** ([*SMESH.FunctorType*](smesh_module.md#SMESH.FunctorType)) – belongs to {SMESH.FT_LessThan, SMESH.FT_MoreThan, SMESH.FT_EqualTo}
            - **Threshold** – the threshold value (range of ids as string, shape, numeric, depending on *CritType*)
            - **UnaryOp** ([*SMESH.FunctorType*](smesh_module.md#SMESH.FunctorType)) – SMESH.FT_LogicalNOT or SMESH.FT_Undefined
            - **Tolerance** (*float*) – the tolerance used by SMESH.FT_BelongToGeom, SMESH.FT_BelongToSurface,
              SMESH.FT_LyingOnGeom, SMESH.FT_CoplanarFaces criteria

        Returns:
        :   [`SMESH.SMESH_GroupOnFilter`](smesh_module.md#SMESH.SMESH_GroupOnFilter)

    MakeGroupByCriteria(*groupName*, *theCriteria*, *binOp=FT_LogicalAND*)
    :   Create a mesh group by the given criteria (list of [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion))

        Parameters:
        :   - **groupName** – the name of the mesh group
            - **theCriteria** – the list of [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion)
            - **binOp** – binary operator (SMESH.FT_LogicalAND or SMESH.FT_LogicalOR ) used when binary operator of criteria is undefined

        Returns:
        :   [`SMESH.SMESH_GroupOnFilter`](smesh_module.md#SMESH.SMESH_GroupOnFilter)

        See also

        [`smeshBuilder.GetCriterion()`](#smeshBuilder.smeshBuilder.GetCriterion)

    MakeGroupByCriterion(*groupName*, *Criterion*)
    :   Create a mesh group by the given criterion

        Parameters:
        :   - **groupName** – the name of the mesh group
            - **Criterion** – the instance of [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion) class

        Returns:
        :   [`SMESH.SMESH_GroupOnFilter`](smesh_module.md#SMESH.SMESH_GroupOnFilter)

        See also

        [`smeshBuilder.GetCriterion()`](#smeshBuilder.smeshBuilder.GetCriterion)

    MakeGroupByFilter(*groupName*, *theFilter*)
    :   Create a mesh group by the given filter

        Parameters:
        :   - **groupName** (*string*) – the name of the mesh group
            - **theFilter** ([*SMESH.Filter*](smesh_module.md#SMESH.Filter)) – the filter

        Returns:
        :   [`SMESH.SMESH_GroupOnFilter`](smesh_module.md#SMESH.SMESH_GroupOnFilter)

        See also

        [`smeshBuilder.GetFilter()`](#smeshBuilder.smeshBuilder.GetFilter)

    MakeGroupByIds(*groupName*, *elementType*, *elemIDs*)
    :   Create a mesh group by the given ids of elements

        Parameters:
        :   - **groupName** – the name of the mesh group
            - **elementType** – the type of elements in the group; either of
              (SMESH.NODE, SMESH.EDGE, SMESH.FACE, SMESH.VOLUME).
            - **elemIDs** – either the list of ids, [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    MakePolyLine(*segments*, *groupName=''*, *isPreview=False*)
    :   Create a polyline consisting of 1D mesh elements each lying on a 2D element of
        the initial triangle mesh. Positions of new nodes are found by cutting the mesh by the
        plane passing through pairs of points specified by each [`SMESH.PolySegment`](smesh_module.md#SMESH.PolySegment) structure.
        If there are several paths connecting a pair of points, the shortest path is
        selected by the module. Position of the cutting plane is defined by the two
        points and an optional vector lying on the plane specified by a PolySegment.
        By default the vector is defined by Mesh module as following. A middle point
        of the two given points is computed. The middle point is projected to the mesh.
        The vector goes from the middle point to the projection point. In case of planar
        mesh, the vector is normal to the mesh.

        In preview mode, *segments* [i].vector returns the used vector which goes from the middle point to its projection.

        Parameters:
        :   - **segments** – list of [`SMESH.PolySegment`](smesh_module.md#SMESH.PolySegment) defining positions of cutting planes.
            - **groupName** – optional name of a group where created mesh segments will be added.

    MakeSlot(*segmentGroup*, *width*)
    :   Create a slot of given width around given 1D elements lying on a triangle mesh.
        The slot is constructed by cutting faces by cylindrical surfaces made
        around each segment. Segments are expected to be created by MakePolyLine().

        Returns:
        :   FaceEdge’s located at the slot boundary

    MergeElements(*GroupsOfElementsID*, *ElementsToKeep=[]*)
    :   Merge elements in each given group.

        Parameters:
        :   - **GroupsOfElementsID** – a list of groups (lists) of elements IDs for merging
              (e.g. [[1,12,13],[25,4]] means that elements 12, 13 and 4 will be removed and
              replaced in all mesh groups by elements 1 and 25)
            - **ElementsToKeep** – elements to keep in the mesh: a list of groups, sub-meshes or node IDs.
              If *ElementsToKeep* does not include an element to keep for some group to merge,
              then the first element in the group is kept.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    MergeEqualElements()
    :   Leave one element and remove all other elements built on the same nodes.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    MergeNodes(*GroupsOfNodes*, *NodesToKeep=[]*, *AvoidMakingHoles=False*)
    :   Merge nodes

        Parameters:
        :   - **GroupsOfNodes** – a list of groups of nodes IDs for merging.
              E.g. [[1,12,13],[25,4]] means that nodes 12, 13 and 4 will be removed and replaced
              in all elements and mesh groups by nodes 1 and 25 correspondingly
            - **NodesToKeep** – nodes to keep in the mesh: a list of groups, sub-meshes or node IDs.
              If *NodesToKeep* does not include a node to keep for some group to merge,
              then the first node in the group is kept.
            - **AvoidMakingHoles** – prevent merging nodes which cause removal of elements becoming
              invalid

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    MeshDimension()
    :   Return the mesh dimension depending on the dimension of the underlying shape
        or, if the mesh is not based on any shape, basing on deimension of elements

        Returns:
        :   mesh dimension as an integer value [0,3]

    MeshToPassThroughAPoint(*x*, *y*, *z*)
    :   Find the node closest to a point and moves it to a point location

        Parameters:
        :   - **x** – the X coordinate of a point
            - **y** – the Y coordinate of a point
            - **z** – the Z coordinate of a point

        Returns:
        :   the ID of a moved node

    MinDistance(*id1*, *id2=0*, *isElem1=False*, *isElem2=False*)
    :   Get minimum distance between two nodes, elements or distance to the origin

        Parameters:
        :   - **id1** – first node/element id
            - **id2** – second node/element id (if 0, distance from *id1* to the origin is computed)
            - **isElem1** – *True* if *id1* is element id, *False* if it is node id
            - **isElem2** – *True* if *id2* is element id, *False* if it is node id

        Returns:
        :   minimum distance value

        See also

        [`GetMinDistance()`](#smeshBuilder.Mesh.GetMinDistance)

    Mirror(*IDsOfElements*, *Mirror*, *theMirrorType=None*, *Copy=0*, *MakeGroups=False*)
    :   Create a symmetrical copy of mesh elements

        Parameters:
        :   - **IDsOfElements** – list of elements ids
            - **Mirror** – is [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom object (point, line, plane)
            - **theMirrorType** – smesh.POINT, smesh.AXIS or smesh.PLANE.
              If the *Mirror* is a geom object this parameter is unnecessary
            - **Copy** – allows to copy element (Copy is 1) or to replace with its mirroring (Copy is 0)
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    MirrorMakeMesh(*IDsOfElements*, *Mirror*, *theMirrorType=0*, *MakeGroups=0*, *NewMeshName=''*)
    :   Create a new mesh by a symmetrical copy of mesh elements

        Parameters:
        :   - **IDsOfElements** – the list of elements ids
            - **Mirror** – is [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom object (point, line, plane)
            - **theMirrorType** – smesh.POINT, smesh.AXIS or smesh.PLANE.
              If the *Mirror* is a geom object this parameter is unnecessary
            - **MakeGroups** – to generate new groups from existing ones
            - **NewMeshName** – a name of the new mesh to create

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    MirrorObject(*theObject*, *Mirror*, *theMirrorType=None*, *Copy=0*, *MakeGroups=False*)
    :   Create a symmetrical copy of the object

        Parameters:
        :   - **theObject** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Mirror** – [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom object (point, line, plane)
            - **theMirrorType** – smesh.POINT, smesh.AXIS or smesh.PLANE.
              If the *Mirror* is a geom object this parameter is unnecessary
            - **Copy** – allows copying the element (Copy==True) or replacing it with its mirror (Copy==False)
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    MirrorObjectMakeMesh(*theObject*, *Mirror*, *theMirrorType=0*, *MakeGroups=0*, *NewMeshName=''*)
    :   Create a new mesh by a symmetrical copy of the object

        Parameters:
        :   - **theObject** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Mirror** – [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom object (point, line, plane)
            - **theMirrorType** – smesh.POINT, smesh.AXIS or smesh.PLANE.
              If the *Mirror* is a geom object this parameter is unnecessary
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the new mesh to create

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    MoveClosestNodeToPoint(*x*, *y*, *z*, *NodeID*)
    :   Find the node closest to a point and moves it to a point location

        Parameters:
        :   - **x** – the X coordinate of a point
            - **y** – the Y coordinate of a point
            - **z** – the Z coordinate of a point
            - **NodeID** – if specified (>0), the node with this ID is moved,
              otherwise, the node closest to point (*x*, *y*, *z*) is moved

        Returns:
        :   the ID of a moved node

    MoveNode(*NodeID*, *x*, *y*, *z*)
    :   Move the node with the given id

        Parameters:
        :   - **NodeID** – the id of the node
            - **x** – a new X coordinate
            - **y** – a new Y coordinate
            - **z** – a new Z coordinate

        Returns:
        :   True if succeed else False

    Nb0DElements()
    :   Return the number of 0d elements in the mesh

        Returns:
        :   an integer value

    NbBalls()
    :   Return the number of ball discrete elements in the mesh

        Returns:
        :   an integer value

    NbBiQuadQuadrangles()
    :   Return the number of biquadratic quadrangles in the mesh

        Returns:
        :   an integer value

    NbBiQuadTriangles()
    :   Return the number of biquadratic triangles in the mesh

        Returns:
        :   an integer value

    NbEdges()
    :   Return the number of edges in the mesh

        Returns:
        :   an integer value

    NbEdgesOfOrder(*elementOrder*)
    :   Return the number of edges with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbElements()
    :   Return the number of elements in the mesh

        Returns:
        :   an integer value

    NbFaces()
    :   Return the number of faces in the mesh

        Returns:
        :   an integer value

    NbFacesOfOrder(*elementOrder*)
    :   Return the number of faces with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbGroups()
    :   Get the number of groups existing in the mesh

        Returns:
        :   the quantity of groups as an integer value

    NbHexagonalPrisms()
    :   Return the number of hexagonal prisms in the mesh

        Returns:
        :   an integer value

    NbHexas()
    :   Return the number of hexahedrons in the mesh

        Returns:
        :   an integer value

    NbHexasOfOrder(*elementOrder*)
    :   Return the number of hexahedrons with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbNodes()
    :   Return the number of nodes in the mesh

        Returns:
        :   an integer value

    NbPolygons(*elementOrder=ORDER_ANY*)
    :   Return the number of polygons of given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbPolyhedrons()
    :   Return the number of polyhedrons in the mesh

        Returns:
        :   an integer value

    NbPrisms()
    :   Return the number of prisms in the mesh

        Returns:
        :   an integer value

    NbPrismsOfOrder(*elementOrder*)
    :   Return the number of prisms with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbPyramids()
    :   Return the number of pyramids in the mesh

        Returns:
        :   an integer value

    NbPyramidsOfOrder(*elementOrder*)
    :   Return the number of pyramids with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbQuadrangles()
    :   Return the number of quadrangles in the mesh

        Returns:
        :   an integer value

    NbQuadranglesOfOrder(*elementOrder*)
    :   Return the number of quadrangles with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbSubMesh()
    :   Return the number of submeshes in the mesh

        Returns:
        :   an integer value

    NbTetras()
    :   Return the number of tetrahedrons in the mesh

        Returns:
        :   an integer value

    NbTetrasOfOrder(*elementOrder*)
    :   Return the number of tetrahedrons with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbTriQuadraticHexas()
    :   Return the number of triquadratic hexahedrons in the mesh

        Returns:
        :   an integer value

    NbTriangles()
    :   Return the number of triangles in the mesh

        Returns:
        :   an integer value

    NbTrianglesOfOrder(*elementOrder*)
    :   Return the number of triangles with the given order in the mesh

        Parameters:
        :   **elementOrder** – is the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    NbVolumes()
    :   Return the number of volumes in the mesh

        Returns:
        :   an integer value

    NbVolumesOfOrder(*elementOrder*)
    :   Return the number of volumes with the given order in the mesh

        Parameters:
        :   **elementOrder** – the order of elements
            (SMESH.ORDER_ANY, SMESH.ORDER_LINEAR or SMESH.ORDER_QUADRATIC)

        Returns:
        :   an integer value

    Offset(*theObject*, *Value*, *MakeGroups=False*, *CopyElements=False*, *NewMeshName=''*)
    :   Create an offset mesh from the given 2D object

        Parameters:
        :   - **theObject** ([*SMESH.SMESH_IDSource*](smesh_module.md#SMESH.SMESH_IDSource)) – the source object (mesh, sub-mesh, group or filter)
            - **theValue** (*float*) – signed offset size
            - **MakeGroups** (*boolean*) – forces the generation of new groups from existing ones
            - **CopyElements** (*boolean*) – if *NewMeshName* is empty, True means to keep original elements,
              False means to remove original elements.
            - **NewMeshName** (*string*) – the name of a mesh to create. If empty, offset elements are added to this mesh

        Returns:
        :   A tuple ([`Mesh`](#smeshBuilder.Mesh), list of [`groups`](smesh_module.md#SMESH.SMESH_Group))

    Polygon(*geom_shape=0*)
    :   Create polygon 2D algorithm for faces

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_PolygonPerFace`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_PolygonPerFace)

    Polyhedron(*geom_shape=0*)
    :   Create polyhedron 3D algorithm for solids

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_PolyhedronPerSolid`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_PolyhedronPerSolid)

    Prism(*geom_shape=0*)
    :   Create prism 3D algorithm for volumes

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Prism3D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Prism3D), [`StdMeshersBuilder_RadialPrism3D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_RadialPrism3D)

    ProjectPoint(*x*, *y*, *z*, *elementType*, *meshObject=None*)
    :   Project a point to a mesh object.
        Return ID of an element of given type where the given point is projected
        and coordinates of the projection point.
        In the case if nothing found, return -1 and []

    Projection1D(*geom_shape=0*)
    :   Create projection 1D algorithm for edges

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Projection1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Projection1D)

    Projection1D2D(*geom_shape=0*)
    :   Create projection 1D-2D algorithm for faces

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Projection1D2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Projection1D2D)

    Projection2D(*geom_shape=0*)
    :   Create projection 2D algorithm for faces

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Projection2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Projection2D)

    Projection3D(*geom_shape=0*)
    :   Create projection 3D algorithm for volumes

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_Projection3D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Projection3D)

    QuadTo4Tri(*theElements=[]*)
    :   Split each of given quadrangles into 4 triangles. A node is added at the center of
        a quadrangle.

        Parameters:
        :   **theElements** – the faces to be split. This can be either
            [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource)
            or a list of face IDs. By default all quadrangles are split

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    QuadToTri(*IDsOfElements*, *theCriterion=None*)
    :   Split quadrangles into triangles.

        Parameters:
        :   - **IDsOfElements** – the faces to be split.
            - **theCriterion** – is a numerical functor, in terms of enum [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType), used to
              choose a diagonal for splitting. If *theCriterion* is None, which is a default
              value, then quadrangles will be split by the smallest diagonal.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    QuadToTriObject(*theObject*, *theCriterion=None*)
    :   Split quadrangles into triangles.

        Parameters:
        :   - **theObject** – the object from which the list of elements is taken,
              this is [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **theCriterion** – is a numerical functor, in terms of enum [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType), used to
              choose a diagonal for splitting. If *theCriterion* is None, which is a default
              value, then quadrangles will be split by the smallest diagonal.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    Quadrangle(*geom_shape=0*)
    :   Create quadrangle 1D-2D algorithm for faces

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_QuadMA_1D2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_QuadMA_1D2D), [`StdMeshersBuilder_Quadrangle`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle), [`StdMeshersBuilder_RadialQuadrangle1D2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_RadialQuadrangle1D2D)

    RemoveElements(*IDsOfElements*)
    :   Remove the elements from the mesh by ids

        Parameters:
        :   **IDsOfElements** – is a list of ids of elements to remove

        Returns:
        :   True or False

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    RemoveGlobalHypotheses()
    :   Remove all global hypotheses

    RemoveGroup(*group*)
    :   Remove a group

        Parameters:
        :   **group** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – group to remove

    RemoveGroupWithContents(*group*)
    :   Remove a group with its contents

        Parameters:
        :   **group** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – group to remove

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    RemoveHypothesis(*hyp*, *geom=0*)
    :   Unassign a hypothesis

        Parameters:
        :   - **hyp** ([*SMESH.SMESH_Hypothesis*](smesh_module.md#SMESH.SMESH_Hypothesis)) – a hypothesis to unassign
            - **geom** (*GEOM.GEOM_Object*) – a sub-shape of mesh geometry

        Returns:
        :   [`SMESH.Hypothesis_Status`](smesh_module.md#SMESH.Hypothesis_Status)

    RemoveNodeWithReconnection(*nodeID*)
    :   Remove a node along with changing surrounding faces to cover a hole.

        Parameters:
        :   **nodeID** – ID of node to remove

    RemoveNodes(*IDsOfNodes*)
    :   Remove nodes from mesh by ids

        Parameters:
        :   **IDsOfNodes** – is a list of ids of nodes to remove

        Returns:
        :   True or False

        Note

        This operation can create gaps in numeration of nodes.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    RemoveOrphanNodes()
    :   Remove all orphan (free) nodes from mesh

        Returns:
        :   number of the removed nodes

        Note

        This operation can create gaps in numeration of nodes.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    RenumberElements()
    :   Renumber mesh elements to remove unused element IDs

    RenumberNodes()
    :   Renumber mesh nodes to remove unused node IDs

    Reorient(*IDsOfElements=None*)
    :   Reorient elements by ids

        Parameters:
        :   **IDsOfElements** – if undefined reorients all mesh elements

        Returns:
        :   True if succeed else False

    Reorient2D(*the2DObject*, *theDirection*, *theFaceOrPoint*)
    :   Reorient faces contained in *the2DObject*.

        Parameters:
        :   - **the2DObject** – a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource) or list of IDs of 2D elements
            - **theDirection** – a desired direction of normal of *theFace*.
              It can be either a GEOM vector or a list of coordinates [x,y,z].
            - **theFaceOrPoint** – defines a face of *the2DObject* whose normal will be
              compared with theDirection. It can be either ID of face or a point
              by which the face will be found. The point can be given as either
              a GEOM vertex or a list of point coordinates.

        Returns:
        :   number of reoriented faces

    Reorient2DBy3D(*the2DObject*, *the3DObject*, *theOutsideNormal=True*)
    :   Reorient faces according to adjacent volumes.

        Parameters:
        :   - **the2DObject** – is a [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) or list of
              either IDs of faces or face groups.
            - **the3DObject** – is a [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) or list of IDs of volumes.
            - **theOutsideNormal** – to orient faces to have their normals
              pointing either *outside* or *inside* the adjacent volumes.

        Returns:
        :   number of reoriented faces.

    Reorient2DByNeighbours(*objectFaces*, *referenceFaces=[]*)
    :   Reorient faces contained in a list of *objectFaces*
        equally to faces contained in a list of *referenceFaces*.

        Parameters:
        :   - **objectFaces** – list of [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) holding faces to reorient.
            - **referenceFaces** – list of [`sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) holding reference faces. It can be empty, then any face in *objectFaces* is used as the reference.

        Returns:
        :   number of reoriented faces.

    ReorientObject(*theObject*)
    :   Reorient all elements of the object

        Parameters:
        :   **theObject** – [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)

        Returns:
        :   True if succeed else False

    Rotate(*IDsOfElements*, *Axis*, *AngleInRadians*, *Copy*, *MakeGroups=False*)
    :   Rotate the elements

        Parameters:
        :   - **IDsOfElements** – list of elements ids
            - **Axis** – the axis of rotation ([`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom line)
            - **AngleInRadians** – the angle of rotation (in radians) or a name of variable which defines angle in degrees
            - **Copy** – allows copying the rotated elements
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    RotateMakeMesh(*IDsOfElements*, *Axis*, *AngleInRadians*, *MakeGroups=0*, *NewMeshName=''*)
    :   Create a new mesh of rotated elements

        Parameters:
        :   - **IDsOfElements** – list of element ids
            - **Axis** – the axis of rotation ([`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom line)
            - **AngleInRadians** – the angle of rotation (in radians) or a name of variable which defines angle in degrees
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the newly created mesh

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    RotateObject(*theObject*, *Axis*, *AngleInRadians*, *Copy*, *MakeGroups=False*)
    :   Rotate the object

        Parameters:
        :   - **theObject** – the object to rotate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **Axis** – the axis of rotation ([`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom line)
            - **AngleInRadians** – the angle of rotation (in radians) or a name of variable which defines angle in degrees
            - **Copy** – allows copying the rotated elements
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if MakeGroups==True, empty list otherwise

    RotateObjectMakeMesh(*theObject*, *Axis*, *AngleInRadians*, *MakeGroups=0*, *NewMeshName=''*)
    :   Create a new mesh from the rotated object

        Parameters:
        :   - **theObject** – the object to rotate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **Axis** – the axis of rotation ([`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or geom line)
            - **AngleInRadians** – the angle of rotation (in radians) or a name of variable which defines angle in degrees
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the newly created mesh

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    RotationSweep(*IDsOfElements*, *Axis*, *AngleInRadians*, *NbOfSteps*, *Tolerance*, *MakeGroups=False*, *TotalAngle=False*)
    :   Generate new elements by rotation of the elements around the axis

        Parameters:
        :   - **IDsOfElements** – the list of ids of elements to sweep
            - **Axis** – the axis of rotation, [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or line(geom object)
            - **AngleInRadians** – the angle of Rotation (in radians) or a name of variable which defines angle in degrees
            - **NbOfSteps** – the number of steps
            - **Tolerance** – tolerance
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **TotalAngle** – gives meaning of AngleInRadians: if True then it is an angular size
              of all steps, else - size of each step

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    RotationSweepObject(*theObject*, *Axis*, *AngleInRadians*, *NbOfSteps*, *Tolerance*, *MakeGroups=False*, *TotalAngle=False*)
    :   Generate new elements by rotation of the elements of object around the axis
        theObject object which elements should be sweeped.
        It can be a mesh, a sub mesh or a group.

        Parameters:
        :   - **Axis** – the axis of rotation, [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or line(geom object)
            - **AngleInRadians** – the angle of Rotation
            - **NbOfSteps** – number of steps
            - **Tolerance** – tolerance
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **TotalAngle** – gives meaning of AngleInRadians: if True then it is an angular size
              of all steps, else - size of each step

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    RotationSweepObject1D(*theObject*, *Axis*, *AngleInRadians*, *NbOfSteps*, *Tolerance*, *MakeGroups=False*, *TotalAngle=False*)
    :   Generate new elements by rotation of the elements of object around the axis
        theObject object which elements should be sweeped.
        It can be a mesh, a sub mesh or a group.

        Parameters:
        :   - **Axis** – the axis of rotation, [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or line(geom object)
            - **AngleInRadians** – the angle of Rotation
            - **NbOfSteps** – number of steps
            - **Tolerance** – tolerance
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **TotalAngle** – gives meaning of AngleInRadians: if True then it is an angular size
              of all steps, else - size of each step

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True,
            empty list otherwise

    RotationSweepObject2D(*theObject*, *Axis*, *AngleInRadians*, *NbOfSteps*, *Tolerance*, *MakeGroups=False*, *TotalAngle=False*)
    :   Generate new elements by rotation of the elements of object around the axis
        theObject object which elements should be sweeped.
        It can be a mesh, a sub mesh or a group.

        Parameters:
        :   - **Axis** – the axis of rotation, [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct) or line(geom object)
            - **AngleInRadians** – the angle of Rotation
            - **NbOfSteps** – number of steps
            - **Tolerance** – tolerance
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **TotalAngle** – gives meaning of AngleInRadians: if True then it is an angular size
              of all steps, else - size of each step

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    RotationSweepObjects(*nodes*, *edges*, *faces*, *Axis*, *AngleInRadians*, *NbOfSteps*, *Tolerance*, *MakeGroups=False*, *TotalAngle=False*)
    :   Generate new elements by rotation of the given elements and nodes around the axis

        Parameters:
        :   - **nodes** – nodes to revolve: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **edges** – edges to revolve: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **faces** – faces to revolve: a list including ids, [`a mesh, sub-meshes, groups or filters`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Axis** – the axis of rotation: [`SMESH.AxisStruct`](smesh_module.md#SMESH.AxisStruct), line (geom object) or [x,y,z,dx,dy,dz]
            - **AngleInRadians** – the angle of Rotation (in radians) or a name of variable
              which defines angle in degrees
            - **NbOfSteps** – the number of steps
            - **Tolerance** – tolerance
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **TotalAngle** – gives meaning of AngleInRadians: if True then it is an angular size
              of all steps, else - size of each step

        Returns:
        :   the list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    Scale(*theObject*, *thePoint*, *theScaleFact*, *Copy*, *MakeGroups=False*)
    :   Scale the object

        Parameters:
        :   - **theObject** – the object to translate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **thePoint** – base point for scale ([`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct) or list of 3 coordinates)
            - **theScaleFact** – list of 1-3 scale factors for axes
            - **Copy** – allows copying the translated elements
            - **MakeGroups** – forces the generation of new groups from existing
              ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True,
            empty list otherwise

    ScaleMakeMesh(*theObject*, *thePoint*, *theScaleFact*, *MakeGroups=False*, *NewMeshName=''*)
    :   Create a new mesh from the translated object

        Parameters:
        :   - **theObject** – the object to translate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **thePoint** – base point for scale ([`SMESH.PointStruct`](smesh_module.md#SMESH.PointStruct) or list of 3 coordinates)
            - **theScaleFact** – list of 1-3 scale factors for axes
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the newly created mesh

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    Segment(*geom_shape=0*)
    :   Create segment 1D algorithm for edges

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_CompositeSegment`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_CompositeSegment), [`StdMeshersBuilder_Segment`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment), [`StdMeshersBuilder_Segment_Python`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment_Python)

    SetAutoColor(*theAutoColor*)
    :   Toggle auto color mode on the object.
        If switched on, a default color of a new group in Create Group dialog is chosen randomly.

        Parameters:
        :   **theAutoColor** (*boolean*) – the flag which toggles auto color mode.

    SetMesh(*theMesh*)
    :   Initialize the Mesh object from an instance of [`SMESH.SMESH_Mesh`](smesh_module.md#SMESH.SMESH_Mesh) interface

        Parameters:
        :   **theMesh** – a [`SMESH.SMESH_Mesh`](smesh_module.md#SMESH.SMESH_Mesh) object

    SetMeshElementOnShape(*ElementID*, *Shape*)
    :   Bind an element to a shape

        Parameters:
        :   - **ElementID** – an element ID
            - **Shape** – a shape (GEOM.GEOM_Object) or shape ID

        Returns:
        :   True if succeed else raises an exception

    SetMeshOrder(*submeshes*)
    :   Set priority of sub-meshes. It works in two ways:

        - For sub-meshes with assigned algorithms of same dimension generating mesh of
          *several dimensions*, it sets the order in which the sub-meshes are computed.
        - For the rest sub-meshes, it sets the order in which the sub-meshes are checked
          when looking for meshing parameters to apply to a sub-shape. To impose the
          order in which sub-meshes with uni-dimensional algorithms are computed,
          call **submesh.Compute()** in a desired order.

        Parameters:
        :   **submeshes** – list of lists of [`sub-meshes`](smesh_module.md#SMESH.SMESH_subMesh)

        Warning: the method is for setting the order for all sub-meshes at once:
        :   SetMeshOrder( [ [sm1, sm2, sm3], [sm4, sm5] ] )

    SetName(*name*)
    :   Set a name to the mesh

        Parameters:
        :   **name** – a new name of the mesh

    SetNodeInVolume(*NodeID*, *Solid*)
    :   Bind a node to a solid

        Parameters:
        :   - **NodeID** – a node ID
            - **Solid** – a solid (GEOM.GEOM_Object) or solid ID

        Returns:
        :   True if succeed else raises an exception

    SetNodeOnEdge(*NodeID*, *Edge*, *paramOnEdge*)
    :   Store the node position on an edge

        Parameters:
        :   - **NodeID** – a node ID
            - **Edge** – an edge (GEOM.GEOM_Object) or edge ID
            - **paramOnEdge** – a parameter on the edge where the node is located

        Returns:
        :   True if succeed else raises an exception

    SetNodeOnFace(*NodeID*, *Face*, *u*, *v*)
    :   Store node position on a face

        Parameters:
        :   - **NodeID** – a node ID
            - **Face** – a face (GEOM.GEOM_Object) or face ID
            - **u** – U parameter on the face where the node is located
            - **v** – V parameter on the face where the node is located

        Returns:
        :   True if succeed else raises an exception

    SetNodeOnVertex(*NodeID*, *Vertex*)
    :   Bind a node to a vertex

        Parameters:
        :   - **NodeID** – a node ID
            - **Vertex** – a vertex (GEOM.GEOM_Object) or vertex ID

        Returns:
        :   True if succeed else raises an exception

    SetShape(*geom*)
    :   Associate the given shape to the mesh (entails the recreation of the mesh)

        Parameters:
        :   **geom** – the shape to be meshed (GEOM_Object)

    SewBorderToSide(*FirstNodeIDOnFreeBorder*, *SecondNodeIDOnFreeBorder*, *LastNodeIDOnFreeBorder*, *FirstNodeIDOnSide*, *LastNodeIDOnSide*, *CreatePolygons*, *CreatePolyedrs*)
    :   Sew border to side

        Returns:
        :   [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Sew_Error)

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SewCoincidentFreeBorders(*freeBorders*, *createPolygons=False*, *createPolyhedra=False*)
    :   Sew FreeBorder’s of each group

        Parameters:
        :   - **freeBorders** – either a SMESH.CoincidentFreeBorders structure or a list of lists
              where each enclosed list contains node IDs of a group of coincident free
              borders such that each consequent triple of IDs within a group describes
              a free border in a usual way: n1, n2, nLast - i.e. 1st node, 2nd node and
              last node of a border.
              For example [[1, 2, 10, 20, 21, 40], [11, 12, 15, 55, 54, 41]] describes two
              groups of coincident free borders, each group including two borders.
            - **createPolygons** – if `True` faces adjacent to free borders are converted to
              polygons if a node of opposite border falls on a face edge, else such
              faces are split into several ones.
            - **createPolyhedra** – if `True` volumes adjacent to free borders are converted to
              polyhedra if a node of opposite border falls on a volume edge, else such
              volumes, if any, remain intact and the mesh becomes non-conformal.

        Returns:
        :   a number of successfully sewed groups

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SewConformFreeBorders(*FirstNodeID1*, *SecondNodeID1*, *LastNodeID1*, *FirstNodeID2*, *SecondNodeID2*)
    :   Sew conform free borders

        Returns:
        :   [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Sew_Error)

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SewFreeBorders(*FirstNodeID1*, *SecondNodeID1*, *LastNodeID1*, *FirstNodeID2*, *SecondNodeID2*, *LastNodeID2*, *CreatePolygons*, *CreatePolyedrs*)
    :   Sew free borders

        Returns:
        :   [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Sew_Error)

        Note

        This operation can create gaps in numeration of nodes or elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SewSideElements(*IDsOfSide1Elements*, *IDsOfSide2Elements*, *NodeID1OfSide1ToMerge*, *NodeID1OfSide2ToMerge*, *NodeID2OfSide1ToMerge*, *NodeID2OfSide2ToMerge*)
    :   Sew two sides of a mesh. The nodes belonging to Side1 are
        merged with the nodes of elements of Side2.
        The number of elements in theSide1 and in theSide2 must be
        equal and they should have similar nodal connectivity.
        The nodes to merge should belong to side borders and
        the first node should be linked to the second.

        Returns:
        :   [`error code`](smesh_module.md#SMESH.SMESH_MeshEditor.Sew_Error)

        Note

        This operation can create gaps in numeration of nodes.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    Smooth(*IDsOfElements*, *IDsOfFixedNodes*, *MaxNbOfIterations*, *MaxAspectRatio*, *Method*)
    :   Smooth elements

        Parameters:
        :   - **IDsOfElements** – the list if ids of elements to smooth
            - **IDsOfFixedNodes** – the list of ids of fixed nodes.
              Note that nodes built on edges and boundary nodes are always fixed.
            - **MaxNbOfIterations** – the maximum number of iterations
            - **MaxAspectRatio** – varies in range [1.0, inf]
            - **Method** – is either Laplacian (smesh.LAPLACIAN_SMOOTH)
              or Centroidal (smesh.CENTROIDAL_SMOOTH)

        Returns:
        :   True in case of success, False otherwise.

    SmoothObject(*theObject*, *IDsOfFixedNodes*, *MaxNbOfIterations*, *MaxAspectRatio*, *Method*)
    :   Smooth elements which belong to the given object

        Parameters:
        :   - **theObject** – the object to smooth
            - **IDsOfFixedNodes** – the list of ids of fixed nodes.
              Note that nodes built on edges and boundary nodes are always fixed.
            - **MaxNbOfIterations** – the maximum number of iterations
            - **MaxAspectRatio** – varies in range [1.0, inf]
            - **Method** – is either Laplacian (smesh.LAPLACIAN_SMOOTH)
              or Centroidal (smesh.CENTROIDAL_SMOOTH)

        Returns:
        :   True in case of success, False otherwise.

    SmoothParametric(*IDsOfElements*, *IDsOfFixedNodes*, *MaxNbOfIterations*, *MaxAspectRatio*, *Method*)
    :   Parametrically smooth the given elements

        Parameters:
        :   - **IDsOfElements** – the list if ids of elements to smooth
            - **IDsOfFixedNodes** – the list of ids of fixed nodes.
              Note that nodes built on edges and boundary nodes are always fixed.
            - **MaxNbOfIterations** – the maximum number of iterations
            - **MaxAspectRatio** – varies in range [1.0, inf]
            - **Method** – is either Laplacian (smesh.LAPLACIAN_SMOOTH)
              or Centroidal (smesh.CENTROIDAL_SMOOTH)

        Returns:
        :   True in case of success, False otherwise.

    SmoothParametricObject(*theObject*, *IDsOfFixedNodes*, *MaxNbOfIterations*, *MaxAspectRatio*, *Method*)
    :   Parametrically smooth the elements which belong to the given object

        Parameters:
        :   - **theObject** – the object to smooth
            - **IDsOfFixedNodes** – the list of ids of fixed nodes.
              Note that nodes built on edges and boundary nodes are always fixed.
            - **MaxNbOfIterations** – the maximum number of iterations
            - **MaxAspectRatio** – varies in range [1.0, inf]
            - **Method** – is either Laplacian (smesh.LAPLACIAN_SMOOTH)
              or Centroidal (smesh.CENTROIDAL_SMOOTH)

        Returns:
        :   True in case of success, False otherwise.

    SplitBiQuadraticIntoLinear(*elems=None*)
    :   Split bi-quadratic elements into linear ones without creation of additional nodes:

        > - bi-quadratic triangle will be split into 3 linear quadrangles;
        > - bi-quadratic quadrangle will be split into 4 linear quadrangles;
        > - tri-quadratic hexahedron will be split into 8 linear hexahedra.

        Quadratic elements of lower dimension adjacent to the split bi-quadratic element
        will be split in order to keep the mesh conformal.

        Parameters:
        :   **elems** – elements to split: [`mesh, sub-mesh, group, filter`](smesh_module.md#SMESH.SMESH_IDSource) or element IDs;
            if None (default), all bi-quadratic elements will be split

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitHexaToPrisms(*theObject*, *theNode000*, *theNode001*)
    :   Split hexahedrons into prisms.

        Uses the [Pattern mapping](pattern_mapping.md) functionality for splitting.

        Parameters:
        :   - **theObject** – the object ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)) from where the list of hexahedrons is taken;
            - **theNode000** – (within the range [0,7]) gives the orientation of the
              pattern relatively each hexahedron: keypoint (0,0,0) of the pattern
              will be mapped into the *theNode000* -th node of each volume, keypoint (0,0,1)
              will be mapped into the *theNode001* -th node of each volume.
              Edge (0,0,0)-(0,0,1) of used pattern connects two not split corners.
            - **theNode001** – (within the range [0,7]) gives the orientation of the
              pattern relatively each hexahedron: keypoint (0,0,0) of the pattern
              will be mapped into the *theNode000* -th node of each volume, keypoint (0,0,1)
              will be mapped into the *theNode001* -th node of each volume.
              Edge (0,0,0)-(0,0,1) of used pattern connects two not split corners.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitHexaToTetras(*theObject*, *theNode000*, *theNode001*)
    :   Split hexahedrons into tetrahedrons.

        This operation uses [Pattern mapping](pattern_mapping.md) functionality for splitting.

        Parameters:
        :   - **theObject** – the object from which the list of hexahedrons is taken;
              this is [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **theNode000** – within the range [0,7]; gives the orientation of the
              pattern relatively each hexahedron: the (0,0,0) key-point of the pattern
              will be mapped into *theNode000*-th node of each volume, the (0,0,1)
              key-point will be mapped into *theNode001*-th node of each volume.
              The (0,0,0) key-point of the used pattern corresponds to a non-split corner.
            - **theNode001** – within the range [0,7]; gives the orientation of the
              pattern relatively each hexahedron: the (0,0,0) key-point of the pattern
              will be mapped into *theNode000*-th node of each volume, the (0,0,1)
              key-point will be mapped into *theNode001*-th node of each volume.
              The (0,0,0) key-point of the used pattern corresponds to a non-split corner.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitHexahedraIntoPrisms(*elems*, *startHexPoint*, *facetNormal*, *method=1*, *allDomains=False*)
    :   Split hexahedra into prisms

        Parameters:
        :   - **elems** – either a list of elements or a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **startHexPoint** – a point used to find a hexahedron for which *facetNormal*
              gives a normal vector defining facets to split into triangles.
              *startHexPoint* can be either a triple of coordinates or a vertex.
            - **facetNormal** – a normal to a facet to split into triangles of a
              hexahedron found by *startHexPoint*.
              *facetNormal* can be either a triple of coordinates or an edge.
            - **method** – flags passing splitting method: smesh.Hex_2Prisms, smesh.Hex_4Prisms.
              smesh.Hex_2Prisms - to split the hexahedron into 2 prisms, etc.
            - **allDomains** – if `False`, only hexahedra adjacent to one closest
              to *startHexPoint* are split, else *startHexPoint*
              is used to find the facet to split in all domains present in *elems*.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitQuad(*IDsOfElements*, *Diag13*)
    :   Split quadrangles into triangles.

        Parameters:
        :   - **IDsOfElements** – the faces to be split
            - **Diag13** (*boolean*) – is used to choose a diagonal for splitting.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitQuadObject(*theObject*, *Diag13*)
    :   Split quadrangles into triangles.

        Parameters:
        :   - **theObject** – the object from which the list of elements is taken,
              this is [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **Diag13** (*boolean*) – is used to choose a diagonal for splitting.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitQuadsNearTriangularFacets()
    :   Split quadrangle faces near triangular facets of volumes

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    SplitVolumesIntoTetra(*elems*, *method=1*, *avoidOverConstrainedVolumes=False*)
    :   Split volumic elements into tetrahedrons

        Parameters:
        :   - **elems** – either a list of elements or a [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **method** – flags passing splitting method:
              smesh.Hex_5Tet, smesh.Hex_6Tet, smesh.Hex_24Tet.
              smesh.Hex_5Tet - to split the hexahedron into 5 tetrahedrons, etc.
            - **avoidOverConstrainedVolume** – if True, choose variants that comply with no over-constrained volumes

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    Translate(*IDsOfElements*, *Vector*, *Copy*, *MakeGroups=False*)
    :   Translate the elements

        Parameters:
        :   - **IDsOfElements** – list of elements ids
            - **Vector** – the direction of translation ([`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or vector or 3 vector components)
            - **Copy** – allows copying the translated elements
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    TranslateMakeMesh(*IDsOfElements*, *Vector*, *MakeGroups=False*, *NewMeshName=''*)
    :   Create a new mesh of translated elements

        Parameters:
        :   - **IDsOfElements** – list of elements ids
            - **Vector** – the direction of translation ([`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or vector or 3 vector components)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the newly created mesh

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    TranslateObject(*theObject*, *Vector*, *Copy*, *MakeGroups=False*)
    :   Translate the object

        Parameters:
        :   - **theObject** – the object to translate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **Vector** – direction of translation ([`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or geom vector or 3 vector components)
            - **Copy** – allows copying the translated elements
            - **MakeGroups** – forces the generation of new groups from existing ones (if Copy)

        Returns:
        :   list of created [`groups`](smesh_module.md#SMESH.SMESH_GroupBase) if *MakeGroups* == True, empty list otherwise

    TranslateObjectMakeMesh(*theObject*, *Vector*, *MakeGroups=False*, *NewMeshName=''*)
    :   Create a new mesh from the translated object

        Parameters:
        :   - **theObject** – the object to translate ([`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource))
            - **Vector** – the direction of translation ([`SMESH.DirStruct`](smesh_module.md#SMESH.DirStruct) or geom vector or 3 vector components)
            - **MakeGroups** – forces the generation of new groups from existing ones
            - **NewMeshName** – the name of the newly created mesh

        Returns:
        :   instance of class [`Mesh`](#smeshBuilder.Mesh)

    TriToQuad(*IDsOfElements*, *theCriterion*, *MaxAngle*)
    :   Fuse the neighbouring triangles into quadrangles.

        Parameters:
        :   - **IDsOfElements** – The triangles to be fused.
            - **theCriterion** – a numerical functor, in terms of enum [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType), used to
              applied to possible quadrangles to choose a neighbour to fuse with.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.
            - **MaxAngle** – is the maximum angle between element normals at which the fusion
              is still performed; theMaxAngle is measured in radians.
              Also it could be a name of variable which defines angle in degrees.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    TriToQuadObject(*theObject*, *theCriterion*, *MaxAngle*)
    :   Fuse the neighbouring triangles of the object into quadrangles

        Parameters:
        :   - **theObject** – is [`mesh, sub-mesh, group or filter`](smesh_module.md#SMESH.SMESH_IDSource)
            - **theCriterion** – is a numerical functor, in terms of enum [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType),
              applied to possible quadrangles to choose a neighbour to fuse with.
              Note that not all items of [`SMESH.FunctorType`](smesh_module.md#SMESH.FunctorType) corresponds
              to numerical functors.
            - **MaxAngle** – a max angle between element normals at which the fusion
              is still performed; theMaxAngle is measured in radians.

        Returns:
        :   True in case of success, False otherwise.

        Note

        This operation can create gaps in numeration of elements.
        Call [`RenumberElements()`](#smeshBuilder.Mesh.RenumberElements) to remove the gaps.

    UnionGroups(*group1*, *group2*, *name*)
    :   Produce a union of two groups.
        A new group is created. All mesh elements that are
        present in the initial groups are added to the new one

        Parameters:
        :   - **group1** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – a group
            - **group2** ([*SMESH.SMESH_GroupBase*](smesh_module.md#SMESH.SMESH_GroupBase)) – another group

        Returns:
        :   instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    UnionListOfGroups(*groups*, *name*)
    :   Produce a union list of groups.
        New group is created. All mesh elements that are present in
        initial groups are added to the new one

        Parameters:
        :   **groups** – list of [`SMESH.SMESH_GroupBase`](smesh_module.md#SMESH.SMESH_GroupBase)

        Returns:
        :   instance of [`SMESH.SMESH_Group`](smesh_module.md#SMESH.SMESH_Group)

    UseExisting1DElements(*geom_shape=0*)
    :   Create 1D algorithm for edges with reusing of existing mesh elements

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_UseExistingElements_1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_UseExistingElements_1D)

    UseExisting2DElements(*geom_shape=0*)
    :   Create 1D-2D algorithm for faces with reusing of existing mesh elements

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_UseExistingElements_1D2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_UseExistingElements_1D2D)

    UseExistingFaces(*geom_shape=0*)
    :   Create 2D algorithm allowing batch meshing of faces

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_UseExisting_2D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_UseExisting_2D)

    UseExistingSegments(*geom_shape=0*)
    :   Create 1D algorithm allowing batch meshing of edges

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_UseExisting_1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_UseExisting_1D)

    ViscousLayerBuilder(*geom_shape=0*)
    :   Viscous layer builder for 2D and 3D geometries

        This method is dynamically added to [`Mesh`](#smeshBuilder.Mesh) class by the meshing plug-in(s).

        If the optional *geom_shape* parameter is not set, this algorithm is global (applied to whole mesh).
        Otherwise, this algorithm defines a submesh based on *geom_shape* subshape.

        Parameters:
        :   - **algo_type** – type of algorithm to be created; allowed values are specified by classes implemented by plug-in
            - **geom_shape** (*GEOM_Object*) – if defined, the subshape to be meshed

        Returns:
        :   An instance of Mesh_Algorithm sub-class according to the specified *algo_type*, see
            [`StdMeshersBuilder_ViscousLayer`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_ViscousLayer)
