<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/physical_system/mesh/mesh_user.html -->

# Defining the mesh

A mesh must be specified when creating a physical system. Most of the
time, the mesh is expected to be generated through an external software
and then read in MANTA. Three mesh format are supported:

- [MED](https://docs.salome-platform.org/latest/dev/MEDCoupling/developer/med-file.html),
- [GMSH](http://gmsh.info),
- [Cast3M](http://www-cast3m.cea.fr/index.php).

MANTA also provides the [grid generator](#manta-front-user-guide-physical-system-mesh-grid-generator) which
allows to create a cartesian mesh of linear elements.

When reading the mesh, the user must specify the mesh file and the list of
*meshsets* , *i.e.*, named regions of the mesh, to be imported using the
`domains` , `boundaries`, `edges` or `nodes`
parameters. Only mesh entities in those regions and their sub-entities are
actually imported.

Defining named region of the mesh enables the user to apply different
properties, constraints, behaviours on those uniquely named regions.

PYTHON

```python
ps = manta.PhysicalSystem(mesh = {'file': 'mesh.med',
                                  'meshName': 'MESH',
                                  'domains': ['nameOfDomain'],
                                  'boundaries': ['nameOfBoundary1',
                                                 'nameOfBoundary2',
                                                 'nameOfBoundary3'],
                                  'nodes': ['nameOfNode1'], 
                                  'edges': ['nameOfEdge1', 'nameOfEdge2']})
```

C++

```c++
const auto mesh_parameters = Parameters{{"file", "mesh.med"},{"meshName", "nameOfMesh"},
{"domains", "nameOfDomain"}, {"boundaries", {"nameOfBoundary1", "nameOfBoundary2", "nameOfBoundary3"}}, {"nodes", {"nameOfNode1"}}, {"edges", {"nameOfEdge1", "nameOfEdge2"}}};
auto ps = construct<PhysicalSystem>(ctx, Parameters{{"mesh", mesh_parameters}});
```

Here, the user specifies:

- `file`: string of the name and path of the read file.
- `format` : format of the mesh file. *optional*
- `meshName`: string of the name of the mesh. *optional*
- `domains`: name of the mesh sets of maximum dimension. (cells).
- `boundaries`: name of the mesh sets of dimension \(n-1\). (facets). *optional*
- `nodes`: name of the mesh sets of dimension \(0\). (nodes). *optional*
- *ONLY IN 3D* `edges`: name of the mesh sets of dimension \(1\). (edges in 3D). *optional*
- `partitionMethod`: method used for partitioning the mesh. *optional*

Note

- `format` is facultative if the mesh file is of MED format with
  .med extension. Format is detected from the file extension.
  Authorized strings as format are (case-insensitive):

  > - MED mesh file: "med" / "splittedmed"
  > - Cast3M mesh file: "castem" / "cast3m" / "castem_sauv" / "cast3m_sauv"
  > - Gmsh mesh file: "gmsh"
- `meshName` is only necessary when multiple meshes are saved in the input
  mesh file.
- `partitionMethod` options are {RCB, RIB, HSFC, GRAPH, NONE, RANDOM}.
  Default is "RIB" (Recursive Inertial Bisection)

## Reading a `MED` mesh

A MED mesh file is read in parallel. The MED file format should be preferred
for larger meshes. It can be read from a single file (`format` = "med")
or from splitted files (`format` = "splittedmed"). In case of splitted
files, the `file` parameter must include a single wildcard '*' character
to specify input files to be read.

Each item in the list of *meshsets* given in the `domains`,
`boundaries`, `edges` or `nodes` parameters must match a
MED group. Case must match.

Warning

- Only elements in the mesh file are imported. Then groups containing
  isolated nodes, which are not linked to any element, cannot be directly
  imported. It is then necessary to create groups of 0D elements from these
  nodes, with the same name as the underlying group of nodes.
- MED files generated with Cast3M and the "SORT MED" operator may be
  missing node numbers. Manta will throw an error in that case. You may need
  to import and re-export your mesh file with SALOME.

## Reading a `Cast3M` or `GMSH` mesh

Cast3M and Gmsh mesh readers were the first readers included in MANTA.
Reading is initially done by the root process and then mesh partitions are
scattered on processes after partitioning.

> - For GMSH, the export mesh file MUST be in **version 2** *(version 4.0
>   is not supported yet)*. Case for *MeshSets* and PhysicalGroups must
>   match.
> - Cast3M mesh files must be generated with the "SAUV" operator.
>   `Gibiane` level over 20 is needed for compatibility with MANTA
>   *(i.e. Cast3M18 or later)*. Only meshes are extracted from those meshfiles.
>   Nodes and elements fields are ignored.
> - The name of Cast3M mesh elements is case-insensitive. *Meshsets*
>   imported from Cast3M mesh files must be specified with **lowercase**
>   strings.

## Mesh generation with the `Grid` generator

To generate a regular grid in MANTA, one can use this minimalistic
call of the `Grid` generator:

PYTHON

```python
ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                      'spaceDimension': 3})
```

C++

```c++
    const auto mesh_parameters = Parameters{{"generator", "Grid"},{"spaceDimension", 3}};
    auto ps = construct<PhysicalSystem>(ctx, Parameters{{"mesh", mesh_parameters}});
```

This call generates (in \(3D\)) a cube
of one element of unit lengths named `cube`, as well as the
boundaries `left`, `right`, `rear`, `front`,
`top`, and `bottom`, and default names for the external edges and external nodes. However, several parameters can be specified
to generate a grid which is more in line with the user's need.

PYTHON

```python
ps = manta.PhysicalSystem(mesh = {'generator': 'Grid',
                                  'spaceDimension': 2,
                                  'lengths': [a, b],
                                  'centerPosition': [x, y],
                                  'domain': 'nameOfDomain',
                                  'boundaries': ['nameOfBoundary1', 'nameOfBoundary2',
                                                 'nameOfBoundary3', 'nameOfBoundary4'],
                                  'numberOfElements': [n_elem_x, n_elem_y]})
```

C++

```c++
    const auto mesh_parameters = Parameters{{"generator", "Grid"},{"spaceDimension", 2},
    {"lengths", {a,b}}, {"centerPosition", {x,y}}, {"domain", "nameOfDomain"},
    {"boundaries", {"nameOfBoundary1", "nameOfBoundary2", "nameOfBoundary3", "nameOfBoundary4"}},
    {"numberOfElements", {n_elem_x, n_elem_y}}};
    auto ps = construct<PhysicalSystem>(ctx, Parameters{{"mesh", mesh_parameters}});
```

For instance, one can specify:

- `spaceDimension`: integer specifying the dimension of the problem.
- `domains`: name of the mesh sets of maximum dimension. (cells). This is an *optional* parameter, default is `cube`.
- `boundaries`: name of the mesh sets of dimension \(n-1\). (facets). This is an *optional* parameter, defaults are listed above.
- `centerPosition`: coordinates of the center of the generated box. This is an *optional* parameter, default is \((0,0,0)\).
- `lengths`: specifies the lengths of the sides of the generated grid. This is an *optional* parameter, default is \(1\) m per side.
- `numberOfElements`: specifies the amount of element per side. This is an *optional* parameter, default is \(1\) element per side.

Note

In order to rename the default mesh sets, we can use the boundary/domain parameter.
However, boundary names are specified in the following specific order in \(3D\):

- name of the first face perpendicular to the x-axis
- name of the second face perpendicular to the x-axis
- name of the first face perpendicular to the y-axis (if the dimension is greater or equal to 2)
- name of the second face perpendicular to the y-axis (if the dimension is greater or equal to 2)
- name of the first face perpendicular to the z-axis (if the dimension is greater or equal to 3)
- name of the second face perpendicular to the z-axis (if the dimension is greater or equal to 3)

Note

A similar convention was set up for edges and nodes. A scheme of these conventions is illustrated in [Fig. 1](#fig-gridnomenclature). In one dimension, edges and nodes do not exist (edges is the cell, nodes are the boundaries).
In two dimension, only nodes and boundaries can be named, by default corner nodes are called are labeled by their coordinate, e.g., the node x0y0
corresponds to the bottom left node. The naming order is:

- x0y0
- x0y1
- x1y0
- x1y1

In three dimensions, edges, nodes, and boundaries can be named, by default, edges and nodes are labeled by their coordinates
following the scheme illustrated in the [Fig. 1](#fig-gridnomenclature). In order to rename those default meshsets,
one should follow this specific order for corner nodes:

- x0y0z1
- x0y0z0
- x0y1z1
- x0y1z0
- x1y0z1
- x1y0z0
- x1y1z1
- x1y1z0

And this specific order for boundary edges:

- x0y0
- x0y1
- x1y0
- x1y1
- x0z0
- x0z1
- x1z0
- x1z1
- y0z0
- y0z1
- y1z0
- y1z1

[![figure](https://manta-project.gitlab.io/manta/_images/grid_nomenclature.svg)](../../../_images/grid_nomenclature.svg)

Fig. 1 Nomenclature of the grid. Left: nodes and edges in 2D. Middle: nodes in 3D. Right: edges in 3D.

## Creating *meshsets* in Python

### Operations on *meshsets*

There are two equivalent ways of creating new *meshsets* in Python:

- the `makeMeshSet` free function,
- the `makeMeshSet` method of the Mesh class.

For the sake of simplicity, only the `makeMeshSet` free function
is described in this section. This function takes two arguments:

- an object describing the operation to be made (see below),
- the name of the resulting *meshset*.

Warning

This function fails if a *meshset* of the same name already
exists.

The following operations are available:

- `UnionOf`: this operation generates the union of the given
  *meshsets*.
- `IntersectionOf`: this operation generates the intersection of
  the given *meshsets*.
- `SubstractionOf`: this operation generates the substraction of a
  first *meshset* with a second *meshset*.
- `BoundaryOf`: this operation returns the boundaries of a
  *meshset*.
- `FacetsOf`: this operation returns the facets of a
  *meshset*.
- `NodesOf`: this operation returns the nodes of a
  *meshset*.
- `CornerNodesOf`: this operation returns the corner nodes of a
  *meshset*.
- `AdjacentEntitiesOf`: this operation returns the adjacent
  entities of a *meshset*.

The `makeMeshSet` function returns the created *meshset*.

#### Example of usage

The following code creates a *meshset* named `steel` by
sustracting a *meshset* named `bar` by a *meshset*
named `copper`, where `ps` is the physical system:

```python
steel = manta.makeMeshSet(manta.SubstractionOf(ps.getMeshSet('bar'),
                                               ps.getMeshSet('copper')),
                          'steel')
```

### Extracting a sub-*meshset* using a spatial function

The function `extractMeshSetByCoordinates` allows to create a new
*meshset* from an existing *meshset* using a spatial
function.

The following arguments are expected:

- `name`: name of the generated mesh set
- `meshSet`: mesh set from which the mesh set is extracted
- `function`: spatial function used to select the elements of the new meshset
- `criterion`: criterion used to select the elements. See the
  `MeshSetExtractCriterion` class for details. By default,
  the function is evaluated at the barycenter of each element.

The `makeMeshSet` function returns the created *meshset*.

Warning

This function fails if a *meshset* of the same name already
exists.

#### Example of usage

The following code creates a new *meshset* named `copper` from a *meshset* named
`bar`. Each node of the selected elements satisfy the following condition:

\[y\leq 5\,\cdot\,10^{-2}\, m\]

where \(y\) is the second coordinate of the node.

```python
copper = manta.extractMeshSetByCoordinates(name = 'copper',
                                           meshSet = ps.getMeshSet('bar'),
                                           function =  lambda x, y: y <= 5e-2,
                                           criterion =  manta.MeshSetExtractCriterion.allNodes)
```
