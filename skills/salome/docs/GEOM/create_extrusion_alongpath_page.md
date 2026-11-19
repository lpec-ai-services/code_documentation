<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_extrusion_alongpath_page.html -->

# Pipe Construction

To generate a **Pipe** in the **Main Menu** select **New Entity - > Generation - > Extrusion along a path**

Firstly, to create an extruded **Pipe** shape, you can define the **Base Object** (vertex, edge, planar wire, face or shell), which will be extruded and the **Path Object** (edge or wire) along which the **Base Object** will be extruded.  
It is possible to select in GUI several Base Objects to make several pipes (using Shift button).   
In this mode the default pipe generation algorithm is used. The pipe is created so that the **angle between the normal vector** to the base shape **and the tangent to the path** wire remains constant at any point of the given path.   
**Select unpublished edges** checkbox - if checked, allows to select an edge of any other shape as the path object.   
**Generate groups** checkbox - if checked allows to create groups of sub-shapes. For more details on groups creation please refer to [this description](create_groups_page.md).   
The **Result** of the operation will be a GEOM_Object (edge, face, shell, solid or compsolid).

**TUI Command:** *geompy.MakePipe(baseShape, pathShape, IsGenerateGroups=False)*   
**Arguments:** Name + 1 shape (vertex, edge, planar wire, face or shell) serving as base object + 1 shape (edge or wire) for definition of the path + 1 boolean parameter (IsGenerateGroups).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![pipe.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe.png)

**Example:**

![pipe_wire_edgesn.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe_wire_edgesn.png)

Extrusion of a wire

Secondly, you can define the **Base Object** (edge, planar wire or face), which will be extruded, the **Path Object** (edge or wire) along which the **Base Object** will be extruded and the **BiNormal Vector** (edge or wire).

In contrast to the default mode, in this mode the pipe is generated to preserve the constant **angle between the normal vector** to the base shape **and the BiNormal vector** given as the third argument.   
**Select unpublished edges** checkbox - if checked, allows to select an edge of any other shape as the path object.   
**Generate groups** checkbox - if checked allows to create groups of sub-shapes. For more details on groups creation please refer to [this description](create_groups_page.md).   
The **Result** of the operation will be a GEOM_Object (edge, face, shell, solid or compsolid).

**TUI Command:** *geompy.MakePipeBiNormalAlongVector(baseShape, pathShape, binormalShape, IsGenerateGroups=False)*   
**Arguments:** Name + 1 shape (edge, planar wire or face) serving as base object + 1 shape (edge or wire) for definition of the path + 1 shape (edge or wire) to set a fixed BiNormal direction to perform the extrusion + 1 boolean parameter (IsGenerateGroups).

![pipe2.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe2.png)

**Example:**

![pipebinormalsn.png](https://docs.salome-platform.org/latest/gui/GEOM/pipebinormalsn.png)

Extrusion of a face with BiNormal parameter

Thirdly, it is possible to additionally select profiles of the pipe object to be built. For this, you can define the following parameters:

- **Base Object** or a list of objects (edges, planar wires, faces or shells), which will be extruded;
- **Locations** - a vertex or a list of vertices that specify the locations of extruded **Base Objects** on the resulting **Path Object**. The number of Base Objects should be equal to the number of **Locations**.
- **Path Object** (edge or wire), along which the **Base Object** will be extruded.

Additional controls:

- If **With contact** is checked, the section is translated in contact with the spine.
- If **With correction** is checked, the section is rotated to be orthogonal to the spine tangent in the corresponding point.
- If **Step-by-step generation** is checked, the result is created step-by-step, i.e. it creates pipes between each pair of neighbor sections and fuses them into a single shape.

Note
:   If **Step-by-step generation** is checked, **With contact** and **With correction** controls are disabled as corrections of bases are not allowed in step-by-step mode.

**Generate groups** checkbox - if checked allows to create groups of sub-shapes. For more details on groups creation please refer to [this description](create_groups_page.md).   
The **Result** of the operation will be a shell or a solid.

**TUI Commands:**

- *geompy.MakePipeWithDifferentSections(baseShape, locations, pathShape, withContact, withCorrection, IsGenerateGroups=False)*   
  **Arguments:** Name + list of shapes (edges, planar wires, faces or shells) serving as base object + list of locations (vertices) on the path corresponding specified list of the shapes + 1 shape (edge or wire) for definition of the path + 3 Boolean parameters (withContact, withCorrection, IsGenerateGroups).
- *geompy.MakePipeWithDifferentSectionsBySteps(baseShape, locations, pathShape, IsGenerateGroups=False)*   
  **Arguments:** Name + list of shapes (edges, planar wires, faces or shells) serving as base object + list of locations (vertices) on the path corresponding specified list of the shapes + 1 shape (edge or wire) for definition of the path + Boolean parameter.

**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![pipe3.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe3.png)

**Example:**

![pipe3_init.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe3_init.png)

Base objects and Location vertices

![pipe3_res.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe3_res.png)

Extrusion of the profile shapes along the path shape

Our **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_pipe).
