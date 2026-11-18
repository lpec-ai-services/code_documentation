<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/main_user_concepts/user_guide_objects/user_readers.html -->

# User guide for the Readers

In MANTA's jargon, the *readers* refer to the functionalities which read
some part of a mesh in a file and import it in the current calculation. There
are several *readers* available, each of them being able to read and
import from some specific mesh file formats.

Furthermore, each *reader* may have one of the following behaviors with
respect to the final construction in memory of a distributed parallel mesh:

1. The MPI process of rank 0 reads the whole mesh from a single file and loads
   it in its memory. It then calls a partition algorithm to attribute to each
   cell of the mesh a destination process. Then it migrates the cells that are
   not attributed to it to their destination MPI process.

   Whereas being simple, it is clear that this process does not scale at all in
   parallel, especially regarding memory consumption. So it may not be relevant to deal
   with large meshes.
2. Each MPI process reads a "slice" of a single file containing the whole mesh.
   There is no reason that the cells which are read this way form a reasonably
   "connex" local mesh. So one only store the barycenters and identifiers of the
   cells read, and a parallel geometrical partitioning is then called. From the
   output of this geometrical partitioning, each process re-read form the file
   the set of entities which has been attributed to it for the geometrical
   partitioning. This lead to a parallel distributed mesh whose partitioning has
   been determined by the geometrical partitioning algorithm used. If this
   partitioning is not considered suitable for the calculation by the user, the
   reader can perform a re-partitioning with another algorithm, which this time
   is not necessarily a geometric algorithm (it can be a graph partitioning for
   instance).

   This procedure should scale in parallel as the algorithm used to read
   concurrently and partitioning used. It may so be suitable to deal with large
   meshes, but involves notably one or two partitioning operations which can be
   quite costly.
3. Each MPI process reads a part of the mesh for a dedicated file. Then it
   assumes that another program has been able to split a mesh in "reasonably
   connex" parts and generate a mesh file for each (the number of parts must be
   the same as the number of MPI processes that one wants to use for the
   calculation).

   The reading procedure of the reader is much more simple in this case and does
   not involve concurrent read. But this moves the difficulty to the external
   program which splits the big mesh. An advantage of that is that if several
   calculations must be done on the same mesh with the same number of processes,
   the cost of splitting the mesh can be paid just once.

## Available readers

| *Eeader* name | File format supported | Parallel behavior | Notes |
| --- | --- | --- | --- |
| castem/castem_sauv/cast3m/cast3m_sauv | Cast3m "SAUV" format levels \(\geq19\)  <https://www-cast3m.cea.fr/> | 1 |  |
| gmsh | MSH file format version 2, ascii  <https://gmsh.info/doc/texinfo/gmsh.html> | 1 |  |
| med |  | 2 |  |
| splittedmed |  | 3 | The name of each input file must contain the rank of the MPI process to which is is assigned. As such, this should be 0-indexed |
| splittedgmsh | Any version of the MSH file format, ascii or binary  <https://gmsh.info/doc/texinfo/gmsh.html> | 3 | The name of each input file must contain the rank of the MPI process to which is is assigned. As such, this should be 0-indexed |

## General usage

The recommended way to use the reader to get a distributed mesh from a mesh file
on the hard drive (or a collection of mesh files) is to use the function
`readAndPartition`.

```c++
  ExitStatus es = 
    readAndPartition(ctx,                                                                             // ①
                     mesh,                                                                            // ②
                     {"./mesh.*.med", "SPLITTEDMED"},                                                 // ③
                     {"mesh:cells", "left:facets", "bottom:facets", "right:facets", "top:facets"
                      "edges:top_front_edge", "edges:middle_edge",
                      "nodes:middle_node" },                                                          // ④
                     "GRAPH");                                                                        // ⑤
```

- ① Pass the context object to, among other possible things, register some error message in case of failure.
- ② The mesh instance which will be populated from the input file(s).
- ③ A `std::pair` of strings whose first item is the path of the mesh file to read on the filesystem, and the second item is the name of the reader to use to read this file.

  > Note
  >
  > The name of the splitter is case-insensitive
  >
  > Note
  >
  > In case of readers having the "parallel behavior 3", the filename must include exactly one '*' character which will be replaced by the MPI process rank (0-indexed).
- ④ A `manta::Vector<std::string>` instance which defines the set of entities to import from the mesh file(s). Each string of this list must be formated as `name:type` where `name` is the name of the entity set defined in the input mesh file(s), and `type` is one of: `cells`, `facets`, `edges`, `nodes`. `cells` should be used to import sets containing entities which are of "maximum dimension", *i.e* which are not the boundary of any higher dimensional entity. `facets` should be used to import sets of entities which are part of the boundary of a *cell* (an entity of "maximum dimension"), and which have one dimension lower than this *cell*. `edges` should only be used in 3D to import sets containing edges of 3-dimensional entities. Some more details about this can be found [here](user_mesh.md#user-mesh-components).
- ⑤ The last argument is used to specify the partitioning algorithm to use to re-partition the mesh. `NONE` can be used to disable re-partitioning. At this time, the algorithm available are labelled: `RANDOM`, `RCB`, `RIB`, `HSFC`, `GRAPH`. Some more details about these algorithms can be found [here](../../../developer_guide/services/load_balancing.md#load-balancing).

Another equivalent possibility is to use a json-like input structure (through a raw-string with the `_json` suffix), as in the following:

```c++
  auto meshParameters = R"({"file": "./mesh.*.med",
                            "format": "SPLITTEDMED",
                            "domains": ["cells"],
                            "boundaries": ["bottom", "top", "left", "right"],
                            "edges": ["top_front_edge", "middle_edge"],
                            "nodes": ["middle_node"],
                            "partitionMethod": "GRAPH"})"_json;
  ExitStatus es = 
    readAndPartition(ctx,
                     mesh,
                     meshParameters);
```

Of course, the order of the items in this json-like structure does not matter.

## A few more details about importing regions

Users have to define a list of regions imported from the mesh (in a `std::vector<std::string>`).
The name of the regions match the name of entities/object in Gmsh or Cast3M files.
The type of the mesh entities follow a MANTA convention, with cells being the largest dimension objects,
facets boundaries of cells, and edges (*only in 3D*), and nodes. Here is an example of the creation of
Regions `std::vector<std::string>`:

```c++
    Vector<std::string> regions = {"tube:cells", "left_boundary:facets", "right_boundary:facets", "e_capt:cells"};
```

Note that there are several syntax to define regions. First of all ":" or "=" can be used.
Then, as shown above, one can use the keywords cells, facets, nodes, or edges.
Or, one can use numbers (as is currently the case in most internal tests), with the following
correspondance: cells:2, edges:4, facets:1, nodes:0 e.g. :

```c++
    Vector<std::string> regions = {"right_beam=1", "left_beam=1", "beam=2"};
```

After importing the regions, we can pair them with MANTA `MeshSet` objects by calling
the `getSet()` method:

```c++
    MeshSet &beam = mesh.getSet("beam");
    MeshSet &left = mesh.getSet("left_beam");
```

Warning

Imported Cast3m names are forced to lowercase in MANTA.
Consequently, object names (in the **regions** vector) should also be
lowercased.

The import of mesh files generated with two different softwares is supported.
In such a case, `read` functions must be called sequentially and each of them must specify a
`regions` vector for each mesh file.

We encourage using the keyword (*i.e, nodes, cells, facets, edges*) rather than the
type_id to improve clarity of the scripts

As said above, region names *(i.e. physical entities names)* have to be
specified for every set of elements included into the mesh. Each added
region correspond to the creation of a [MeshSet](../../../developer_guide/services/mesh_set.md#mesh-set) in
MANTA.

Each part of the physical domain on which a field needs to be set or
read, or where a **LinearSystem** has to be solved, must be specified
that way.

Note

In Debug mode, imported mesh sets and their type are printed on the
standard output.
