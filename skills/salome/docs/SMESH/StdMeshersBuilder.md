<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/StdMeshersBuilder.html -->

# smesh_algorithm module

*class* smesh_algorithm.Mesh_Algorithm
:   The base class to define meshing algorithms

    Note

    This class should not be used directly, it is supposed to be sub-classed
    for implementing Python API for specific meshing algorithms

    For each meshing algorithm, a python class inheriting from class *Mesh_Algorithm*
    should be defined. This descendant class should have two attributes defining the way
    it is created by class [`Mesh`](smeshBuilder.md#smeshBuilder.Mesh) (see e.g. class [`StdMeshersBuilder_Segment`](#StdMeshersBuilder.StdMeshersBuilder_Segment)):

    - `meshMethod` attribute defines name of method of class [`Mesh`](smeshBuilder.md#smeshBuilder.Mesh) by calling which the
      python class of algorithm is created; this method is dynamically added to the [`Mesh`](smeshBuilder.md#smeshBuilder.Mesh) class
      in runtime. For example, if in `class MyPlugin_Algorithm` this attribute is defined as:

      ```python
      meshMethod = "MyAlgorithm"
      ```

      then an instance of `MyPlugin_Algorithm` can be created by the direct invocation of the function
      of [`Mesh`](smeshBuilder.md#smeshBuilder.Mesh) class:

      ```python
      my_algo = mesh.MyAlgorithm()
      ```
    - `algoType` defines type of algorithm and is used mostly to discriminate
      algorithms that are created by the same method of class [`Mesh`](smeshBuilder.md#smeshBuilder.Mesh). For example, if this attribute
      is specified in `MyPlugin_Algorithm` class as:

      ```python
      algoType = "MyPLUGIN"
      ```

      then it’s creation code can be:

      ```python
      my_algo = mesh.MyAlgorithm(algo="MyPLUGIN")
      ```

    Assign(*algo*, *mesh*, *geom*)
    :   Private method

    Create(*mesh*, *geom*, *hypo*, *so='libStdMeshersEngine.so'*)
    :   Private method.

    FindAlgorithm(*algoname*, *smeshpyD*)
    :   Finds the algorithm in the study by its type name.
        Finds only the algorithms, which have been created in smeshBuilder engine.

        Returns:
        :   SMESH.SMESH_Algo

    FindHypothesis(*hypname*, *args*, *CompareMethod*, *smeshpyD*)
    :   Finds a hypothesis in the study by its type name and parameters.
        Finds only the hypotheses created in smeshBuilder engine.

        Returns:
        :   [`SMESH_Hypothesis`](smesh_module.md#SMESH.SMESH_Hypothesis)

    GetAlgorithm()
    :   Returns the wrapped mesher.

    GetCompatibleHypothesis()
    :   Gets the list of hypothesis that can be used with this algorithm

    GetId()
    :   Gets the id of the algorithm

    GetName()
    :   Gets the name of the algorithm

    GetSubMesh()
    :   If the algorithm is global, returns 0;
        else returns the [`SMESH_subMesh`](smesh_module.md#SMESH.SMESH_subMesh) associated to this algorithm.

    Hypothesis(*hyp*, *args=[]*, *so='libStdMeshersEngine.so'*, *UseExisting=0*, *CompareMethod=''*, *toAdd=True*)
    :   Private method

    MainShapeEntry()
    :   Returns entry of the shape to mesh in the study

    ReversedEdgeIndices(*reverseList*)
    :   Transform a list of either edges or tuples (edge, 1st_vertex_of_edge)
        into a list acceptable to SetReversedEdges() of some 1D hypotheses

    SetName(*name*)
    :   Sets the name to the algorithm

    ViscousLayers(*thickness*, *numberOfLayers*, *stretchFactor*, *faces=[]*, *isFacesToIgnore=True*, *extrMethod=SURF_OFFSET_SMOOTH*, *groupName=''*)
    :   Defines “ViscousLayers” hypothesis to give parameters of layers of prisms to build
        near mesh boundary. This hypothesis can be used by several 3D algorithms:
        NETGEN 3D, MG-Tetra, Hexahedron(i,j,k)

        Parameters:
        :   - **thickness** – total thickness of layers of prisms
            - **numberOfLayers** – number of layers of prisms
            - **stretchFactor** – factor (>1.0) of growth of layer thickness towards inside of mesh
            - **faces** – list of geometrical faces (or their ids).
              Viscous layers are either generated on these faces or not, depending on
              the value of **isFacesToIgnore** parameter.
            - **isFacesToIgnore** – if *True*, the Viscous layers are not generated on the
              faces specified by the previous parameter (**faces**).
            - **extrMethod** –

              extrusion method defines how position of new nodes are found during
              prism construction and how creation of distorted and intersecting prisms is
              prevented. Possible values are:

              - StdMeshers.SURF_OFFSET_SMOOTH (default) method extrudes nodes along normal
                :   to underlying geometrical surface. Smoothing of internal surface of
                    element layers can be used to avoid creation of invalid prisms.
              - StdMeshers.FACE_OFFSET method extrudes nodes along average normal of
                :   surrounding mesh faces till intersection with a neighbor mesh face
                    translated along its own normal by the layers thickness. Thickness
                    of layers can be limited to avoid creation of invalid prisms.
              - StdMeshers.NODE_OFFSET method extrudes nodes along average normal of
                :   surrounding mesh faces by the layers thickness. Thickness of
                    layers can be limited to avoid creation of invalid prisms.
            - **groupName** –

              name of a group to contain elements of layers. If not provided,
              no group is created. The group is created upon mesh generation.
              It can be retrieved by calling

              ```python
              group = mesh.GetGroupByName( groupName, SMESH.VOLUME )[0]
              ```

        Returns:
        :   StdMeshers.StdMeshers_ViscousLayers hypothesis

    ViscousLayers2D(*thickness*, *numberOfLayers*, *stretchFactor*, *edges=[]*, *isEdgesToIgnore=True*, *groupName=''*)
    :   Defines “ViscousLayers2D” hypothesis to give parameters of layers of quadrilateral
        elements to build near mesh boundary. This hypothesis can be used by several 2D algorithms:
        NETGEN 2D, NETGEN 1D-2D, Quadrangle (mapping), MG-CADSurf

        Parameters:
        :   - **thickness** – total thickness of layers of quadrilaterals
            - **numberOfLayers** – number of layers
            - **stretchFactor** – factor (>1.0) of growth of layer thickness towards inside of mesh
            - **edges** – list of geometrical edges (or their ids).
              Viscous layers are either generated on these edges or not, depending on
              the value of **isEdgesToIgnore** parameter.
            - **isEdgesToIgnore** – if *True*, the Viscous layers are not generated on the
              edges specified by the previous parameter (**edges**).
            - **groupName** –

              name of a group to contain elements of layers. If not provided,
              no group is created. The group is created upon mesh generation.
              It can be retrieved by calling

              ```python
              group = mesh.GetGroupByName( groupName, SMESH.FACE )[0]
              ```

        Returns:
        :   StdMeshers.StdMeshers_ViscousLayers2D hypothesis

# StdMeshersBuilder module

Python API for the standard meshing plug-in module.

StdMeshersBuilder.COMPOSITE *= 'CompositeSegment_1D'*
:   Composite segment 1D algorithm, see [`StdMeshersBuilder_CompositeSegment`](#StdMeshersBuilder.StdMeshersBuilder_CompositeSegment)

    Type:
    :   Algorithm type

StdMeshersBuilder.Hexa *= 'Hexa_3D'*
:   Hexahedron 3D (i-j-k) algorithm, see [`StdMeshersBuilder_Hexahedron`](#StdMeshersBuilder.StdMeshersBuilder_Hexahedron)

    Type:
    :   Algorithm type

StdMeshersBuilder.POLYGON *= 'PolygonPerFace_2D'*
:   Polygon Per Face 2D algorithm, see [`StdMeshersBuilder_PolygonPerFace`](#StdMeshersBuilder.StdMeshersBuilder_PolygonPerFace)

    Type:
    :   Algorithm type

StdMeshersBuilder.POLYHEDRON *= 'PolyhedronPerSolid_3D'*
:   Polyhedron Per Solid 3D algorithm, see [`StdMeshersBuilder_PolyhedronPerSolid`](#StdMeshersBuilder.StdMeshersBuilder_PolyhedronPerSolid)

    Type:
    :   Algorithm type

StdMeshersBuilder.PYTHON *= 'Python_1D'*
:   Python 1D algorithm, see [`StdMeshersBuilder_Segment_Python`](#StdMeshersBuilder.StdMeshersBuilder_Segment_Python)

    Type:
    :   Algorithm type

StdMeshersBuilder.QUADRANGLE *= 'Quadrangle_2D'*
:   Quadrangle 2D algorithm, see [`StdMeshersBuilder_Quadrangle`](#StdMeshersBuilder.StdMeshersBuilder_Quadrangle)

    Type:
    :   Algorithm type

StdMeshersBuilder.QUAD_MA_PROJ *= 'QuadFromMedialAxis_1D2D'*
:   Quadrangle (Medial Axis Projection) 1D-2D algorithm, see [`StdMeshersBuilder_QuadMA_1D2D`](#StdMeshersBuilder.StdMeshersBuilder_QuadMA_1D2D)

    Type:
    :   Algorithm type

StdMeshersBuilder.RADIAL_QUAD *= 'RadialQuadrangle_1D2D'*
:   Radial Quadrangle 1D-2D algorithm, see [`StdMeshersBuilder_RadialQuadrangle1D2D`](#StdMeshersBuilder.StdMeshersBuilder_RadialQuadrangle1D2D)

    Type:
    :   Algorithm type

StdMeshersBuilder.REGULAR *= 'Regular_1D'*
:   Regular 1D algorithm, see [`StdMeshersBuilder_Segment`](#StdMeshersBuilder.StdMeshersBuilder_Segment)

    Type:
    :   Algorithm type

*class* StdMeshersBuilder.StdMeshersBuilder_Cartesian_3D(*mesh*, *geom=0*)
:   Defines a Body Fitting 3D algorithm.

    It is created by calling smeshBuilder.Mesh.BodyFitted(geom=0)

    SetAxesDirs(*xAxis*, *yAxis*, *zAxis*)
    :   Defines custom directions of axes of the grid

        Parameters:
        :   - **xAxis** – either SMESH.DirStruct or a vector, or 3 vector components
            - **yAxis** – either SMESH.DirStruct or a vector, or 3 vector components
            - **zAxis** – either SMESH.DirStruct or a vector, or 3 vector components

    SetFixedPoint(*p*, *toUnset=False*)
    :   Sets/unsets a fixed point. The algorithm makes a plane of the grid pass
        :   through the fixed point in each direction at which the grid is defined
            by spacing

        Parameters:
        :   - **p** – coordinates of the fixed point. Either SMESH.PointStruct or
              a vertex or 3 components of coordinates.
            - **toUnset** – defines whether the fixed point is defined or removed.

    SetGrid(*xGridDef*, *yGridDef*, *zGridDef*, *sizeThreshold=4.0*, *implEdges=False*)
    :   Defines “Body Fitting parameters” hypothesis

        Parameters:
        :   **xGridDef** –

            is definition of the grid along the X asix.
            It can be in either of two following forms:

            > - Explicit coordinates of nodes, e.g. [-1.5, 0.0, 3.1] or range( -100,200,10)
            > - Functions f(t) defining grid spacing at each point on grid axis. If there are
            >   :   several functions, they must be accompanied by relative coordinates of
            >       points dividing the whole shape into ranges where the functions apply; points
            >       coordinates should vary within (0.0, 1.0) range. Parameter *t* of the spacing
            >       function f(t) varies from 0.0 to 1.0 within a shape range.

        Note

        The actual grid spacing can slightly differ from the defined one. This is done for the
        best fitting of polyhedrons and for a better mesh quality on the interval boundaries.
        For example, if a constant **Spacing** is defined along an axis, the actual grid will
        fill the shape’s dimension L along this axis with round number of equal cells:
        Spacing_actual = L / round( L / Spacing_defined ).

        Examples

        “10.5” - defines a grid with a constant spacing
        [[“1”, “1+10*t”, “11”] [0.1, 0.6]] - defines different spacing in 3 ranges.

        Parameters:
        :   - **yGridDef** – defines the grid along the Y asix the same way as *xGridDef* does.
            - **zGridDef** – defines the grid along the Z asix the same way as *xGridDef* does.
            - **sizeThreshold** – (> 1.0) defines a minimal size of a polyhedron so that
              a polyhedron of size less than hexSize/sizeThreshold is not created.
            - **implEdges** – enables implementation of geometrical edges into the mesh.

    SetOptimalAxesDirs(*isOrthogonal=True*)
    :   Automatically defines directions of axes of the grid at which
        :   a number of generated hexahedra is maximal

        Parameters:
        :   **isOrthogonal** – defines whether the axes mush be orthogonal

    algoType *= 'Cartesian_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create Body Fitting 3D algorithm for volumes'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'BodyFitted'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_CompositeSegment(*mesh*, *geom=0*)
:   Segment 1D algorithm for discretization of a set of adjacent edges as one edge.

    It is created by calling smeshBuilder.Mesh.Segment(smeshBuilder.COMPOSITE,geom=0)

    algoType *= 'CompositeSegment_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create segment 1D algorithm for edges'*
    :   doc string of the method

    isDefault *= False*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Segment'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Hexahedron(*mesh*, *geom=0*)
:   Defines a hexahedron 3D algorithm.
    It is created by calling smeshBuilder.Mesh.Hexahedron(geom=0)

    algoType *= 'Hexa_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create hexahedron 3D algorithm for volumes'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Hexahedron'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_PolygonPerFace(*mesh*, *geom=0*)
:   Defines a Polygon Per Face 2D algorithm.
    It is created by calling smeshBuilder.Mesh.Polygon(geom=0)

    algoType *= 'PolygonPerFace_2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create polygon 2D algorithm for faces'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Polygon'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_PolyhedronPerSolid(*mesh*, *geom=0*)
:   Defines a Polyhedron Per Solid 3D algorithm.
    It is created by calling smeshBuilder.Mesh.Polyhedron(geom=0)

    algoType *= 'PolyhedronPerSolid_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create polyhedron 3D algorithm for solids'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Polyhedron'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Prism3D(*mesh*, *geom=0*)
:   Defines a Prism 3D algorithm, which is either “Extrusion 3D” or “Radial Prism” depending on geometry.
    It is created by calling smeshBuilder.Mesh.Prism(geom=0)

    Arithmetic1D(*start*, *end*)
    :   Defines “Arithmetic1D” hypothesis, specifying the distribution of segments
        :   to build between the inner and the outer shells with a length that changes
            in arithmetic progression

        Parameters:
        :   - **start** – the length of the first segment
            - **end** – the length of the last segment

    AutomaticLength(*fineness=0*)
    :   Defines “AutomaticLength” hypothesis, specifying the number of segments
        :   to build between the inner and outer shells

        Parameters:
        :   **fineness** – defines the quality of the mesh within the range [0-1]

    GeometricProgression(*start*, *ratio*)
    :   Defines “GeometricProgression” hypothesis, specifying the distribution of segments
        :   to build between the inner and the outer shells with a length that changes
            in Geometric progression

        Parameters:
        :   - **start** – the length of the first segment
            - **ratio** – the common ratio of the geometric progression

    Get3DHypothesis()
    :   Returns:
        :   3D hypothesis holding the 1D one

    LocalLength(*l*, *p=1e-07*)
    :   Defines “LocalLength” hypothesis, specifying the segment length
        :   to build between the inner and the outer shells

        Parameters:
        :   - **l** – the length of segments
            - **p** – the precision of rounding

    NumberOfLayers(*n*, *UseExisting=0*)
    :   Defines “NumberOfLayers” hypothesis, specifying the number of layers of
        :   prisms to build between the inner and outer shells

        Parameters:
        :   - **n** – number of layers
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    NumberOfSegments(*n*, *s=[]*)
    :   Defines “NumberOfSegments” hypothesis, specifying the number of layers of
        :   prisms to build between the inner and the outer shells.

        Parameters:
        :   - **n** – the number of layers
            - **s** – the scale factor (optional)

    OwnHypothesis(*hypType*, *args=[]*, *so='libStdMeshersEngine.so'*)
    :   Private method creating a 1D hypothesis and storing it in the LayerDistribution
        :   hypothesis.

        Returns:
        :   the created hypothesis

    StartEndLength(*start*, *end*)
    :   Defines “StartEndLength” hypothesis, specifying distribution of segments
        :   to build between the inner and the outer shells as geometric length increasing

        Parameters:
        :   **start** – for the length of the first segment

        end: for the length of the last segment

    algoType *= 'Prism_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create prism 3D algorithm for volumes'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Prism'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Projection1D(*mesh*, *geom=0*)
:   Defines a projection 1D algorithm.
    It is created by calling smeshBuilder.Mesh.Projection1D(geom=0)

    SourceEdge(*edge*, *mesh=None*, *srcV=None*, *tgtV=None*, *UseExisting=0*)
    :   Defines “Source Edge” hypothesis, specifying a meshed edge, from where
        :   a mesh pattern is taken, and, optionally, the association of vertices
            between the source edge and a target edge (to which a hypothesis is assigned)

        Parameters:
        :   - **edge** – from which nodes distribution is taken
            - **mesh** – from which nodes distribution is taken (optional)
            - **srcV** – a vertex of *edge* to associate with *tgtV* (optional)
            - **tgtV** – a vertex of *the edge* to which the algorithm is assigned, to associate with *srcV* (optional)
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    algoType *= 'Projection_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create projection 1D algorithm for edges'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Projection1D'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Projection1D2D(*mesh*, *geom=0*)
:   Defines a projection 1D-2D algorithm.
    It is created by calling smeshBuilder.Mesh.Projection1D2D(geom=0)

    algoType *= 'Projection_1D2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create projection 1D-2D algorithm for faces'*
    :   doc string of the method

    meshMethod *= 'Projection1D2D'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Projection2D(*mesh*, *geom=0*)
:   Defines a projection 2D algorithm.
    It is created by calling smeshBuilder.Mesh.Projection2D(geom=0)

    SourceFace(*face*, *mesh=None*, *srcV1=None*, *tgtV1=None*, *srcV2=None*, *tgtV2=None*, *UseExisting=0*)
    :   Defines “Source Face” hypothesis, specifying a meshed face, from where
        :   a mesh pattern is taken, and, optionally, the association of vertices
            between the source face and the target face (to which a hypothesis is assigned)

        Parameters:
        :   - **face** – from which the mesh pattern is taken
            - **mesh** – from which the mesh pattern is taken (optional)
            - **srcV1** – a vertex of *face* to associate with *tgtV1* (optional)
            - **tgtV1** – a vertex of *the face* to which the algorithm is assigned, to associate with *srcV1* (optional)
            - **srcV2** – a vertex of *face* to associate with *tgtV1* (optional)
            - **tgtV2** – a vertex of *the face* to which the algorithm is assigned, to associate with *srcV2* (optional)
            - **UseExisting** – if ==true - forces the search for the existing hypothesis created with
              he same parameters, else (default) - forces the creation a new one

        Note

        all association vertices must belong to one edge of a face

    algoType *= 'Projection_2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create projection 2D algorithm for faces'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Projection2D'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Projection3D(*mesh*, *geom=0*)
:   Defines a projection 3D algorithm.
    It is created by calling smeshBuilder.Mesh.Projection3D(geom=0)

    SourceShape3D(*solid*, *mesh=0*, *srcV1=0*, *tgtV1=0*, *srcV2=0*, *tgtV2=0*, *UseExisting=0*)
    :   Defines the “Source Shape 3D” hypothesis, specifying a meshed solid, from where
        :   the mesh pattern is taken, and, optionally, the association of vertices
            between the source and the target solid (to which a hypothesis is assigned)

        Parameters:
        :   - **solid** – from where the mesh pattern is taken
            - **mesh** – from where the mesh pattern is taken (optional)
            - **srcV1** – a vertex of *solid* to associate with *tgtV1* (optional)
            - **tgtV1** – a vertex of *the solid* where the algorithm is assigned, to associate with *srcV1* (optional)
            - **srcV2** – a vertex of *solid* to associate with *tgtV1* (optional)
            - **tgtV2** – a vertex of *the solid* to which the algorithm is assigned,to associate with *srcV2* (optional)
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Note

        association vertices must belong to one edge of a solid

    algoType *= 'Projection_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create projection 3D algorithm for volumes'*
    :   doc string of the method

    meshMethod *= 'Projection3D'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_QuadMA_1D2D(*mesh*, *geom=0*)
:   Defines a Quadrangle (Medial Axis Projection) 1D-2D algorithm .
    It is created by calling smeshBuilder.Mesh.Quadrangle(smeshBuilder.QUAD_MA_PROJ,geom=0)

    algoType *= 'QuadFromMedialAxis_1D2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create quadrangle 1D-2D algorithm for faces'*
    :   doc string of the method

    meshMethod *= 'Quadrangle'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Quadrangle(*mesh*, *geom=0*)
:   Defines a quadrangle 2D algorithm.
    It is created by calling smeshBuilder.Mesh.Quadrangle(geom=0)

    QuadrangleParameters(*quadType=QUAD_STANDARD*, *triangleVertex=0*, *enfVertices=[]*, *enfPoints=[]*, *corners=[]*, *UseExisting=0*)
    :   Defines “QuadrangleParameters” hypothesis
        :   quadType defines the algorithm of transition between differently descretized
            sides of a geometrical face:

            - QUAD_STANDARD - both triangles and quadrangles are possible in the transition
              :   area along the finer meshed sides.
            - QUAD_TRIANGLE_PREF - only triangles are built in the transition area along the
              :   finer meshed sides.
            - QUAD_QUADRANGLE_PREF - only quadrangles are built in the transition area along
              :   the finer meshed sides, iff the total quantity of segments on
                  all four sides of the face is even (divisible by 2).
            - QUAD_QUADRANGLE_PREF_REVERSED - same as QUAD_QUADRANGLE_PREF but the transition
              :   area is located along the coarser meshed sides.
            - QUAD_REDUCED - only quadrangles are built and the transition between the sides
              :   is made gradually, layer by layer. This type has a limitation on
                  the number of segments: one pair of opposite sides must have the
                  same number of segments, the other pair must have an even difference
                  between the numbers of segments on the sides.

        Parameters:
        :   - **triangleVertex** – vertex of a trilateral geometrical face, around which triangles
              will be created while other elements will be quadrangles.
              Vertex can be either a GEOM_Object or a vertex ID within the
              shape to mesh
            - **enfVertices** – list of shapes defining positions where nodes (enforced nodes)
              must be created by the mesher. Shapes can be of any type,
              vertices of given shapes define positions of enforced nodes.
              Only vertices successfully projected to the face are used.
            - **enfPoints** – list of points giving positions of enforced nodes.
              Point can be defined either as SMESH.PointStruct’s
              ([SMESH.PointStruct(x1,y1,z1), SMESH.PointStruct(x2,y2,z2),…])
              or triples of values ([[x1,y1,z1], [x2,y2,z2], …]).
              In the case if the defined QuadrangleParameters() refer to a sole face,
              all given points must lie on this face, else the mesher fails.
            - **corners** – list of vertices that should be used as quadrangle corners.
              The parameter can be useful for faces with more than four vertices,
              since in some cases Quadrangle Mapping algorithm chooses corner vertices
              differently than it is desired.
              A hypothesis can be global and define corners for all CAD faces that
              require it, but be sure that each specified vertex is a corner in all
              faces the hypothesis will be applied to.
            - **UseExisting** – if *True* - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    QuadranglePreference(*reversed=False*, *UseExisting=0*)
    :   Defines “QuadrangleParams” hypothesis with a type of quadrangulation that only
        :   quadrangles are built in the transition area along the finer meshed sides,
            if the total quantity of segments on all four sides of the face is even.

        Parameters:
        :   **reversed** – if True, transition area is located along the coarser meshed sides.

        UseExisting: if ==true - searches for the existing hypothesis created with
        :   the same parameters, else (default) - Create a new one

    Reduced(*UseExisting=0*)
    :   Defines “QuadrangleParams” hypothesis with a type of quadrangulation that only
        :   quadrangles are built and the transition between the sides is made gradually,
            layer by layer. This type has a limitation on the number of segments: one pair
            of opposite sides must have the same number of segments, the other pair must
            have an even difference between the numbers of segments on the sides.

        Parameters:
        :   **UseExisting** – if ==true - searches for the existing hypothesis created with
            the same parameters, else (default) - Create a new one

    TrianglePreference(*UseExisting=0*)
    :   Defines “QuadrangleParams” hypothesis with a type of quadrangulation that only
        :   triangles are built in the transition area along the finer meshed sides.

        Parameters:
        :   **UseExisting** – if ==true - searches for the existing hypothesis created with
            the same parameters, else (default) - Create a new one

    TriangleVertex(*vertex*, *UseExisting=0*)
    :   Defines “QuadrangleParams” hypothesis with QUAD_STANDARD type of quadrangulation

        Parameters:
        :   **vertex** –

            vertex of a trilateral geometrical face, around which triangles
            :   will be created while other elements will be quadrangles.
                Vertex can be either a GEOM_Object or a vertex ID within the
                shape to mesh

            UseExisting: if ==true - searches for the existing hypothesis created with
            :   the same parameters, else (default) - Create a new one

    algoType *= 'Quadrangle_2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create quadrangle 2D algorithm for faces'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Quadrangle'*
    :   name of the dynamic method in smeshBuilder.Mesh class

    params *= 0*
    :   hypothesis associated with algorithm

*class* StdMeshersBuilder.StdMeshersBuilder_RadialAlgorithm
:   Base class for algorithms supporting radial distribution hypotheses

    Arithmetic1D(*start*, *end*)
    :   Defines “Arithmetic1D” hypothesis, specifying the distribution of segments
        :   with a length that changes in arithmetic progression

        Parameters:
        :   - **start** – the length of the first segment
            - **end** – the length of the last segment

    AutomaticLength(*fineness=0*)
    :   Defines “AutomaticLength” hypothesis, specifying the number of segments

        Parameters:
        :   **fineness** – defines the quality of the mesh within the range [0-1]

    GeometricProgression(*start*, *ratio*)
    :   Defines “GeometricProgression” hypothesis, specifying the distribution of segments
        :   with a length that changes in Geometric progression

        Parameters:
        :   - **start** – the length of the first segment
            - **ratio** – the common ratio of the geometric progression

    Get2DHypothesis()
    :   Returns:
        :   2D hypothesis holding the 1D one

    LocalLength(*l*, *p=1e-07*)
    :   Defines “LocalLength” hypothesis, specifying the segment length

        Parameters:
        :   - **l** – the length of segments
            - **p** – the precision of rounding

    NumberOfLayers(*n*, *UseExisting=0*)
    :   Defines “NumberOfLayers” hypothesis, specifying the number of layers

        Parameters:
        :   - **n** – number of layers
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    NumberOfSegments(*n*, *s=[]*)
    :   Defines “NumberOfSegments” hypothesis, specifying the number of layers

        Parameters:
        :   - **n** – the number of layers
            - **s** – the scale factor (optional)

    OwnHypothesis(*hypType*, *args=[]*, *so='libStdMeshersEngine.so'*)
    :   Private method creating a 1D hypothesis and storing it in the LayerDistribution
        :   hypothesis.

        Returns:
        :   the created hypothesis

    StartEndLength(*start*, *end*)
    :   Defines “StartEndLength” hypothesis, specifying distribution of segments
        :   as geometric length increasing

        Parameters:
        :   - **start** – for the length of the first segment
            - **end** – for the length of the last segment

*class* StdMeshersBuilder.StdMeshersBuilder_RadialPrism3D(*mesh*, *geom=0*)
:   Defines Radial Prism 3D algorithm.
    It is created by calling smeshBuilder.Mesh.Prism(geom=0).
    See [`StdMeshersBuilder_Prism3D`](#StdMeshersBuilder.StdMeshersBuilder_Prism3D) for methods defining distribution of mesh layers
    build between the inner and outer shells.

    algoType *= 'RadialPrism_3D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create Raial Prism 3D algorithm for volumes'*
    :   doc string of the method

    meshMethod *= 'Prism'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_RadialQuadrangle1D2D(*mesh*, *geom=0*)
:   Defines a Radial Quadrangle 1D-2D algorithm.
    It is created by calling smeshBuilder.Mesh.Quadrangle(smeshBuilder.RADIAL_QUAD,geom=0)

    algoType *= 'RadialQuadrangle_1D2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create quadrangle 1D-2D algorithm for faces having a shape of disk or a disk segment'*
    :   doc string of the method

    meshMethod *= 'Quadrangle'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Segment(*mesh*, *geom=0*)
:   Defines segment 1D algorithm for edges discretization.

    It can be created by calling smeshBuilder.Mesh.Segment(geom=0)

    Adaptive(*minSize*, *maxSize*, *deflection*, *UseExisting=False*)
    :   Defines “Adaptive” hypothesis to cut an edge into segments keeping segment size
        within the given range and considering (1) deflection of segments from the edge
        and (2) distance from segments to closest edges and faces to have segment length
        not longer than two times shortest distances to edges and faces.

        Parameters:
        :   - **minSize** – defines the minimal allowed segment length
            - **maxSize** – defines the maximal allowed segment length
            - **deflection** – defines the maximal allowed distance from a segment to an edge
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_Adaptive1D hypothesis

    Arithmetic1D(*start*, *end*, *reversedEdges=[]*, *UseExisting=0*)
    :   Defines “Arithmetic1D” hypothesis to cut an edge in several segments with a length
        :   that changes in arithmetic progression

        Parameters:
        :   - **start** – defines the length of the first segment
            - **end** – defines the length of the last segment
            - **reversedEdges** – is a list of edges to mesh using reversed orientation.
              A list item can also be a tuple (edge, 1st_vertex_of_edge)
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_Arithmetic1D hypothesis

    AutomaticLength(*fineness=0*, *UseExisting=0*)
    :   Defines “AutomaticLength” hypothesis

        Parameters:
        :   - **fineness** – for the fineness [0-1]
            - **UseExisting** – if ==true - searches for an existing hypothesis created with the
              same parameters, else (default) - create a new one

    Deflection1D(*d*, *UseExisting=0*)
    :   Defines “Deflection1D” hypothesis

        Parameters:
        :   - **d** – for the deflection
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - create a new one

    FixedPoints1D(*points*, *nbSegs=[1]*, *reversedEdges=[]*, *UseExisting=0*)
    :   Defines “FixedPoints1D” hypothesis to cut an edge using parameter
        :   on curve from 0 to 1 (additionally it is neecessary to check
            orientation of edges and create list of reversed edges if it is
            needed) and sets numbers of segments between given points (default
            values are 1)

        Parameters:
        :   - **points** – defines the list of parameters on curve
            - **nbSegs** – defines the list of numbers of segments
            - **reversedEdges** – is a list of edges to mesh using reversed orientation.
              A list item can also be a tuple (edge, 1st_vertex_of_edge)
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_FixedPoints1D hypothesis

    GeometricProgression(*start*, *ratio*, *reversedEdges=[]*, *UseExisting=0*)
    :   Defines “GeometricProgression” hypothesis to cut an edge in several
        :   segments with a length that changes in Geometric progression

        Parameters:
        :   - **start** – defines the length of the first segment
            - **ratio** – defines the common ratio of the geometric progression
            - **reversedEdges** – is a list of edges to mesh using reversed orientation.
              A list item can also be a tuple (edge, 1st_vertex_of_edge)
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_Geometric1D hypothesis

    LengthNearVertex(*length*, *vertex=-1*, *UseExisting=0*)
    :   Defines “SegmentLengthAroundVertex” hypothesis

        Parameters:
        :   - **length** – for the segment length
            - **vertex** – for the length localization: the vertex index [0,1] | vertex object.
              Any other integer value means that the hypothesis will be set on the
              whole 1D shape, where Mesh_Segment algorithm is assigned.
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

    LocalLength(*l*, *UseExisting=0*, *p=1e-07*)
    :   Defines “LocalLength” hypothesis to cut an edge in several segments with the same length

        Parameters:
        :   - **l** – for the length of segments that cut an edge
            - **UseExisting** – if == true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one
            - **p** – precision, used for calculation of the number of segments.
              The precision should be a positive, meaningful value within the range [0,1].
              In general, the number of segments is calculated with the formula:
              nb = ceil((edge_length / l) - p)
              Function ceil rounds its argument to the higher integer.
              So, p=0 means rounding of (edge_length / l) to the higher integer,
              p=0.5 means rounding of (edge_length / l) to the nearest integer,
              p=1 means rounding of (edge_length / l) to the lower integer.
              Default value is 1e-07.

        Returns:
        :   an instance of StdMeshers_LocalLength hypothesis

    MaxSize(*length=0.0*, *UseExisting=0*)
    :   Defines “MaxSize” hypothesis to cut an edge into segments not longer than given value

        Parameters:
        :   - **length** – is optional maximal allowed length of segment, if it is omitted
              the preestimated length is used that depends on geometry size
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_MaxLength hypothesis

    NumberOfSegments(*n*, *s=[]*, *reversedEdges=[]*, *UseExisting=0*, *beta=None*)
    :   Defines “NumberOfSegments” hypothesis to cut an edge in a fixed number of segments

        Parameters:
        :   - **n** – for the number of segments that cut an edge
            - **s** – for the scale factor (optional)
            - **reversedEdges** – is a list of edges to mesh using reversed orientation.
              A list item can also be a tuple (edge, 1st_vertex_of_edge)
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - create a new one
            - **beta** – beta coefficient for Beta Law distribution

        Returns:
        :   an instance of StdMeshers_NumberOfSegments hypothesis

    Propagation()
    :   Defines “Propagation” hypothesis that propagates 1D hypotheses
        :   from an edge where this hypothesis is assigned to
            on all other edges that are at the opposite side in case of quadrangular faces
            This hypothesis should be assigned to an edge to propagate a hypothesis from.

    PropagationOfDistribution()
    :   Defines “Propagation of Node Distribution” hypothesis that propagates
        :   distribution of nodes from an edge where this hypothesis is assigned to,
            to opposite edges of quadrangular faces, so that number of segments on all these
            edges will be the same, as well as relations between segment lengths.

    QuadraticMesh()
    :   Defines “QuadraticMesh” hypothesis, forcing construction of quadratic edges.
        If the 2D mesher sees that all boundary edges are quadratic,
        it generates quadratic faces, else it generates linear faces using
        medium nodes as if they are vertices.
        The 3D mesher generates quadratic volumes only if all boundary faces
        are quadratic, else it fails.

    StartEndLength(*start*, *end*, *reversedEdges=[]*, *UseExisting=0*)
    :   Defines “StartEndLength” hypothesis to cut an edge in several segments with increasing geometric length

        Parameters:
        :   - **start** – defines the length of the first segment
            - **end** – defines the length of the last segment
            - **reversedEdges** – is a list of edges to mesh using reversed orientation.
              A list item can also be a tuple (edge, 1st_vertex_of_edge)
            - **UseExisting** – if ==true - searches for an existing hypothesis created with
              the same parameters, else (default) - Create a new one

        Returns:
        :   an instance of StdMeshers_StartEndLength hypothesis

    algoType *= 'Regular_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create segment 1D algorithm for edges'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'Segment'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_Segment_Python(*mesh*, *geom=0*)
:   Defines a segment 1D algorithm for discretization of edges with Python function.
    It is created by calling smeshBuilder.Mesh.Segment(smeshBuilder.PYTHON,geom=0)

    PythonSplit1D(*n*, *func*, *UseExisting=0*)
    :   Defines “PythonSplit1D” hypothesis

        Parameters:
        :   - **n** – for the number of segments that cut an edge
            - **func** – for the python function that calculates the length of all segments
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    algoType *= 'Python_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create segment 1D algorithm for edges'*
    :   doc string of the method

    meshMethod *= 'Segment'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_UseExistingElements_1D(*mesh*, *geom=0*)
:   Defines a Use Existing Elements 1D algorithm.

    It is created by calling smeshBuilder.Mesh.UseExisting1DElements(geom=0)

    SourceEdges(*groups*, *toCopyMesh=False*, *toCopyGroups=False*, *UseExisting=False*)
    :   Defines “Source edges” hypothesis, specifying groups of edges to import

        Parameters:
        :   - **groups** – list of groups of edges
            - **toCopyMesh** – if True, the whole mesh *groups* belong to is imported
            - **toCopyGroups** – if True, all groups of the mesh *groups* belong to are imported
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    algoType *= 'Import_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create 1D algorithm for edges with reusing of existing mesh elements'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'UseExisting1DElements'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_UseExistingElements_1D2D(*mesh*, *geom=0*)
:   Defines a Use Existing Elements 1D-2D algorithm.

    It is created by calling smeshBuilder.Mesh.UseExisting2DElements(geom=0)

    SourceFaces(*groups*, *toCopyMesh=False*, *toCopyGroups=False*, *UseExisting=False*)
    :   Defines “Source faces” hypothesis, specifying groups of faces to import

        Parameters:
        :   - **groups** – list of groups of faces
            - **toCopyMesh** – if True, the whole mesh *groups* belong to is imported
            - **toCopyGroups** – if True, all groups of the mesh *groups* belong to are imported
            - **UseExisting** – if ==true - searches for the existing hypothesis created with
              the same parameters, else (default) - Create a new one

    algoType *= 'Import_1D2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create 1D-2D algorithm for faces with reusing of existing mesh elements'*
    :   doc string of the method

    isDefault *= True*
    :   flag pointing whether this algorithm should be used by default in dynamic method
        of smeshBuilder.Mesh class

    meshMethod *= 'UseExisting2DElements'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_UseExisting_1D(*mesh*, *geom=0*)
:   Defines a stub 1D algorithm, which enables “manual” creation of nodes and
    :   segments usable by 2D algorithms.

    It is created by calling smeshBuilder.Mesh.UseExistingSegments(geom=0)

    algoType *= 'UseExisting_1D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create 1D algorithm allowing batch meshing of edges'*
    :   doc string of the method

    meshMethod *= 'UseExistingSegments'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_UseExisting_2D(*mesh*, *geom=0*)
:   Defines a stub 2D algorithm, which enables “manual” creation of nodes and
    faces usable by 3D algorithms.

    It is created by calling smeshBuilder.Mesh.UseExistingFaces(geom=0)

    algoType *= 'UseExisting_2D'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Create 2D algorithm allowing batch meshing of faces'*
    :   doc string of the method

    meshMethod *= 'UseExistingFaces'*
    :   name of the dynamic method in smeshBuilder.Mesh class

*class* StdMeshersBuilder.StdMeshersBuilder_ViscousLayer(*mesh*, *geom=0*)
:   Defines the prismatic layer builder.

    It is created by calling smeshBuilder.Mesh.ViscousLayerBuilder(geom=TheGeometry)

    algoType *= 'ViscousLayerBuilder'*
    :   type of algorithm used with helper function in smeshBuilder.Mesh class

    docHelper *= 'Viscous layer builder for 2D and 3D geometries'*
    :   doc string of the method

    meshMethod *= 'ViscousLayerBuilder'*
    :   name of the dynamic method in smeshBuilder.Mesh class
