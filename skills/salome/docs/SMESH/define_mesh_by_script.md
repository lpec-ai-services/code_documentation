<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/define_mesh_by_script.html -->

# Use Edges/Faces to be Created Manually

The algorithms **Use Edges to be Created Manually** and **Use Faces to be Created Manually** allow creating a 1D or a 2D mesh in a python script (using *AddNode, AddEdge* and *AddFace* commands) and then using such sub-meshes in the construction of a 2D or a 3D mesh.

For example, you want to use standard algorithms to generate 1D and 3D
meshes and to create 2D mesh by your python code. For this, you

1. create a mesh object, assign a 1D algorithm,
2. invoke **Compute** command, which computes a 1D mesh,
3. assign **Use Faces to be Created Manually** and a 3D algorithm,
4. run your python code, which creates a 2D mesh,
5. invoke **Compute** command, which computes a 3D mesh.

> Warning
>
> - **Use Edges to be Created Manually** and **Use Faces to be Created Manually** algorithms should be assigned *before* mesh generation by the Python code.
> - Nodes and elements created in your script must be assigned to geometry entities by calling *SetMeshElementOnShape*, *SetNodeOnVertex*, *SetNodeOnEdge* etc. in order to be used by an algorithm of upper dimension.

Consider trying a sample script demonstrating the usage of [Use Faces to be Created Manually](tui_defining_hypotheses.md#tui-use-existing-faces) algorithm for construction of a 2D mesh using Python commands.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/use_existing_face_sample_mesh.png)

**See also** [the sample script](tui_defining_hypotheses.md#tui-use-existing-faces) creating the mesh shown in the image in a Shrink mode.
