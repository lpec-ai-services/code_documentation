<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/using_notebook_smesh_page.html -->

# Using SALOME NoteBook

**SALOME NoteBook** allows defining variables to be used for
creation and modification of objects.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/using_notebook_smesh.png)

**Setting of variables in SALOME NoteBook**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addnode_notebook.png)

**Use of variables to add a node in MESH module**

The following limitations on the use of variables still exist:

- [Distribution of Layers](radial_prism_algo.md#radial-prism-algo-page) hypothesis - parametrical values are correctly applied, but they are not restored after “Update study” operation.
- [Number of Segments](1d_meshing_hypo.md#a1d-meshing-hypo-page) hypothesis, Distribution with Table Density and Distribution with Analytic Density - parametrical values are not applicable.
- [Translation](translation.md#translation-page) dialog box, default mode (translation by two points) - parametrical values are correctly applied, but they are not restored after “Update study” operation.
- [Merging nodes](merging_nodes.md#merging-nodes-page) dialog box - parametrical value (tolerance of coincident nodes detection) is correctly applied, but it is not restored after “Update study” operation.
- [Revolution](revolution.md#revolution-page) dialog box - it is impossible to use the angle of revolution as “total angle” if it is defined as variable.
- [Extrusion along a path](extrusion_along_path.md#extrusion-along-path-page) dialog box - it is impossible to use “Linear variation of the angles” mode if at least one of those angles is defined as variable.
- [Pattern mapping](pattern_mapping.md#pattern-mapping-page) dialog box - parametrical values (indices of nodes) are correctly applied, but they are not restored after “Update study” operation.
- [Clipping](clipping.md#clipping-page) dialog box.
- [Properties](colors_size.md#colors-size-page) dialog box.

Our **TUI Scripts** provide you with useful examples of [Using SALOME NoteBook](tui_notebook_smesh.md#tui-notebook-smesh).
