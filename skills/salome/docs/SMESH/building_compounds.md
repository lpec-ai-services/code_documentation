<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/building_compounds.html -->

# Building Compound Meshes

Compound Mesh is a combination of several mesh objects (meshes, groups, submeshes). All elements and groups present in input meshes are present in the compound mesh. However, it does not use geometry or hypotheses of the initial mesh objects.
The links between the input meshes and the compound mesh are not supported, consequently the modification of an input mesh does not lead to the update of the compound mesh.

There are two modes of building a compound:

- joining selected mesh objects into a new mesh.
- appending selected mesh objects to an existing mesh.

*To Build a compound mesh:*

From the **Mesh** menu select **Build Compound** or click *“Build Compound Mesh”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image161.png) in the toolbar. The following dialog box will appear:

> ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/buildcompound.png)

- **Result** group allows selecting a mode of operation

  - Activating **Create new mesh named** enables typing the name of the resulting compound mesh.
  - Activating **Append to mesh** enables selection of a mesh to append other selected objects to.
- **Meshes, sub-meshes, groups** allows selecting the meshes, sub-meshes and groups to be concatenated. They can be chosen in the Object Browser while holding *Ctrl* button.
- **Processing identical groups** allows selecting the method of processing the namesake groups existing in the input meshes. They can be either

  - **United** - all elements of *Group1* of *Mesh_1* and *Group1* of *Mesh_2* become the elements of *Group1* of the *Compound_Mesh*, or
  - **Renamed** - *Group1* of *Mesh_1* becomes *Group1_1* and *Group1* of *Mesh_2* becomes *Group1_2*.

  See [Grouping elements](grouping_elements.md#grouping-elements-page) for more information about groups.
- **Create groups from input objects** check-box permits to automatically create groups corresponding to every initial mesh.

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/buildcompound_groups.png)
  >
  > **Groups created from input meshes ‘Box_large’ and ‘Box_small’**
- You can choose to additionally [Merge coincident nodes](merging_nodes.md#merging-nodes-page) [and elements](merging_elements.md#merging-elements-page) in the compound mesh, in which case it is possible to define the **Tolerance** for this operation.

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image160.gif)
  >
  > **Example of a compound of two meshed cubes**

**See Also** a sample script of [Building a compound of meshes](tui_creating_meshes.md#tui-building-compound).
