<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/user_guide_objects/user_mesh.html -->

# User guide for the Mesh

The first step to create a mesh in MANTA is to create an empty mesh in the
`ResourcesManager`. Here for a 3D mesh:

```c++
    ResourcesManager rm(3);
    auto &mesh = rm.getMesh();
```

After this, MANTA offers two ways of filling the empty declared mesh within the `ResourcesManager`:

- Generating a regular grid of linear elements,
- Reading a mesh generated through an external software.

Let us review the steps of generating the mesh in MANTA and enabling the manipulation
of its entities by defining `MeshSet` objects, in both those cases.

## Reading an external `Mesh`

MANTA supports to read meshes in several formats. Please have a look at
[this page](user_readers.md#user-readers-components) for information about how to import
mesh entities from mesh files.

## Generating a mesh

MANTA also provides some basic mesh generators:

- [generateGrid](#gridgenerator) creates a cartesian 1D/2D/3D mesh of linear elements aligned with x/xy/xyz-axis.
  It can therefore be a line of `seg2` , a grid of `qua4` or a cube of `hex8`.
- [generateLine](#linegenerator) creates a mesh of `seg2` linear elements, arbitrarily oriented. It can be used to generate n lines with a single call to `generateLine`.

### Generating a grid and its `MeshSet`

The grid can be generated with the following call for a 3D grid.

```c++
    auto gridMeshSets = mesh.generateGrid<2>("grid", {.5, .5}, {1., 1.}, {n, n});
```

The parameters are:

1. string specifying the name of the mesh,
2. the coordinates of the center of the grid,
3. length of the sides of the grid (in x,y direction),
4. number of elements per direction.

A 1D or 3D grid could be created by specifying the dimension as a template parameter and specifying
respectively 1, and 3 coordinates/length/number of cells.

A second optional template parameter can be set to true to set the grid as periodic, *e.g*,
for a 2D periodic mesh:

```c++
    auto [revMeshSets, periodicNodes] = mesh.generateGrid<2, true>("rev", {cx, cy}, {lx, ly}, {nx, ny});
```

Several base `MeshSet` are created with the grid to ease its manipulation.
External boundaries and nodes are easily accessible following a convention illustrated in
[this section about Mesh in the higher level API](../../../manta_frontend_user_guide/physical_system/mesh/mesh_user.md#mesh-namingconvention). At this layer
the `MeshSet` will be named `<nameOfMesh>_x<i>y<j>z<k>`,
where all the variables between brackets are replaced by their appropriate value
as described in the naming convention linked above.

For instance, in order to get the complete mesh, and specific parts
of the "nozzle" grid generated here, we call:

```c++
    mesh.generateGrid<1>("nozzle", {L / 2.}, {L}, {NCells});

    const MeshSet &cells         = mesh.getSet("nozzle");
    const MeshSet &leftBoundary  = mesh.getSet("nozzle_x0");
    const MeshSet &rightBoundary = mesh.getSet("nozzle_x1");
```

### Generating a 1D-line and its `MeshSet`

The following example shows how to generate a single straight line of `seg2` elements
between two points:

```c++
    // create nodes A and B
    Vector<EntityHandle> nodesA = mesh.generateNodes(0., 0., 0.);
    Vector<EntityHandle> nodesB = mesh.generateNodes(0., length, 0.);
    // create the "line" meshset and its boundary facets
    mesh.generateLine<dim>({"beam"}, nodesA, nodesB, nbElements);
    // get the meshsets from their names
    MeshSet &beam  = mesh.getSet("beam");
    MeshSet &left  = mesh.getSet("beam_0");
    MeshSet &right = mesh.getSet("beam_1");
```

The parameters of `generateNodes` are:

1. Real (or Vector of Real) representing the first coordinate of the node(s) to generate.
2. Real (or vector of Real) representing the second coordinate of the node(s) to generate (set to 0 if not given).
3. Real (or Vector of Real) representing the third coordinate of the node(s) to generate (set to 0 if not given).

The parameters of `generateLine` are:

1. Vector of string(s) specifying the name of the MeshSet(s),
2. Vector of EntityHandle defining the starting node(s),
3. Vector of EntityHandle defining the ending node(s),
4. number of elements to generate,
5. optionally, in case of arc-line(s), a Vector of EntityHandle defining the center(s).

Note that all arguments are given as vectors,
in order to use this method to generate \(n\) independent lines at once,
each with a given name, start/end coordinates, etc.

An arc-line implies that given points must not be aligned,
and that starting and ending point are equidistant to the center point.

As a convention, the boundary facets (starting and ending nodes)
are named by suffixing the argument name by _0 and _1.

As for the `generateGrid` function, it is also possible to directly get the Meshsets
from the array returned by `generateLine`:

```c++
    Vector<EntityHandle> nodesA = mesh.generateNodes(0., 0., 0.);
    Vector<EntityHandle> nodesB = mesh.generateNodes(length, 0., 0.);
    auto msArrays               = mesh.generateLine<dim>({"beam"}, nodesA, nodesB, nbElements);
    auto msArray                = msArrays[0];
    MeshSet &beam               = msArray[0];
    MeshSet &left               = msArray[1];
    MeshSet &right              = msArray[2];
```

When running on p MPI processes, `generateLine` called with vectors of n items
generates concurrently n lines distributed on the p processes with the rule
illustrated by the following figure:

![figure](https://manta-project.gitlab.io/manta/_images/generateLine_dispatch.svg)

Fig. 2 Distribution of nodes ands lines by `generateNodes` and `generateLine`.

Such an example of usage is given hereafter:

```c++
    // create nTubes nodes concurrently on all proc
    const Index nTubes = R.size();
    Vector<Real> _X(nTubes);
    Vector<Real> _Y(nTubes);
    Vector<Real> _Z(nTubes);

    for (Index i = 0; i < nTubes; i++) {
      _X[i] = -R[i];
    }
    Vector<EntityHandle> nodePsol1 = mesh.generateNodes(_X);
    for (Index i = 0; i < nTubes; i++) {
      _Z[i] = H;
    }
    Vector<EntityHandle> nodePc1 = mesh.generateNodes(_X, _Y, _Z);
    for (Index i = 0; i < nTubes; i++) {
      _X[i] = 0;
    }
    Vector<EntityHandle> nodePcentre = mesh.generateNodes(_X, _Y, _Z);
    for (Index i = 0; i < nTubes; i++) {
      _Z[i] = R[i] + H;
    }
    Vector<EntityHandle> nodePapex = mesh.generateNodes(_X, _Y, _Z);
    for (Index i = 0; i < nTubes; i++) {
      _X[i] = R[i];
      _Z[i] = H;
    }
    Vector<EntityHandle> nodePc2 = mesh.generateNodes(_X, _Y, _Z);
    for (Index i = 0; i < nTubes; i++) {
      _Z[i] = 0.;
    }
    Vector<EntityHandle> nodePsol2 = mesh.generateNodes(_X, _Y, _Z);

    // > Create a uniform mesh
    const Index nCellsPerLeg      = H / meshDensity;
    const Index nCellsPerHalfBend = (0.5 * pi) * ((R[0] + R[1]) / 2.) / meshDensity;
    mesh.generateLine<dim>(_hotLegs, nodePsol1, nodePc1, nCellsPerLeg);
    mesh.generateLine<dim>(_hotBends, nodePc1, nodePapex, nCellsPerHalfBend, nodePcentre);
    mesh.generateLine<dim>(_coldBends, nodePapex, nodePc2, nCellsPerHalfBend, nodePcentre);
    mesh.generateLine<dim>(_coldLegs, nodePc2, nodePsol2, nCellsPerLeg);
```

If n is not a multiple of p, the lines will be not equally distributed
as illustrated on the previous figure.

If the vector of strings contains a single string,
a single Meshsets embedding all lines is generated.
Otherwise, it must be of the same length as the number of lines (i.e. n),
and n Meshsets will be generated.

If n<p, some processes will have empty Meshsets.

Warning

**About parallel generation of line meshes that share nodes**

As it is explained in the previous paragraphs,
in MPI context, `generateNodes` and `generateLine` will generate
**independent** nodes and Meshsets respectively on every process (i.e. no entity are shared).
If this is not desired, these functions may be called on a single process,
and then, the mesh can be distributed manually or automatically
(through the `mesh::migrateEntities` or `ResourcesManager::rebalance` functions).

## `printoutPartition`: written vizualization of the mesh

All of the created `Meshsets` can be visualised with:

```c++
    mesh.printoutPartition();
```

## Geometrical types

Available geometry types in MANTA are contained into
`GeoType`. They include eight basic types (Point, Segment,
Triangle, Quadrangle, Tetrahedron, Hexahedron, Wedge and Pyramid), their
quadratic counterparts, and some more. Here is the correspondence table
with VTK entities :

Table 4 GeoType - VTK correspondence table

| Id | GeoType | VTK |
| --- | --- | --- |
| 0 | poi1 | VERTEX |
| 1 | seg2 | LINE |
| 2 | tri3 | TRIANGLE |
| 3 | qua4 | QUAD |
| 4 | tet4 | TETRA |
| 5 | hex8 | HEXAHEDRON |
| 6 | pri6 | WEDGE |
| 7 | pyr5 | PYRAMID |
| 9 | seg3 | QUADRATIC_EDGE |
| 10 | tri6 | QUADRATIC_TRIANGLE |
| 11 | qua8 | QUADRATIC_QUAD |
| 12 | te10 | QUADRATIC_TETRA |
| 13 | he20 | QUADRATIC_HEXAHEDRON |
| 14 | we15 | QUADRATIC_WEDGE |
| 15 | py13 | QUADRATIC_PYRAMID |
| 17 | seg4 | CUBIC_LINE |
| 19 | qua9 | BIQUADRATIC_QUAD |
| 21 | he27 | TR IQUADRATIC_HEXAHEDRON |
| 22 | we18 | BIQUAD RATIC_QUADRATIC_WEDGE |
| 23 | py14 | NOT ASSIGNED IN VTK - Quadratic Pyramid with 1 Node in the center of the basis face |

See also: [Node numbering of geometry types](../../../developer_guide/services/node_numbering.md#node-numbering).

The number of each kind of entity can be obtained with
`Mesh::getNumEntitiesOfType(GeoType type)`.

## Other informations

Other information about the `Mesh` class, its handling through
a *MeshBackend*, the system of node numbering can be found in
the developer guide's [services section](../../../developer_guide/services/services.md#services).
