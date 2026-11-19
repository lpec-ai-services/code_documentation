<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/adaptation.html -->

# Adaptation

Mesh module provides the possibility to perform different adaptations of a mesh.
To refine the mesh means to cut out elements indicated according to indications provided by the user.

## HOMARD

HOMARD can treat meshes into 2 or 3 dimensions and comprising the following elements:
:   - mesh-points
    - segments
    - triangles
    - quadrangles
    - tetrahedra
    - hexahedra
    - prisms

These elements can be present simultaneously. For example, HOMARD will be able to adapt a comprising mesh of the triangles and the quadrangles.

To start operation, select **Remesh with HOMARD** item in **Adaptation** menu.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_with_homard_arguments.png)

- **Mesh In** is the initial mesh to remesh.
- **Mesh Out** is the resulting mesh after remeshing. By default, the name of the initial mesh is kept and the file name is based on the name of the initial mesh.
- **Conformity type** is a choice between **Conformal** and **Non conformal**.
- **Boundary type** is a choice between **No boundary**, **CAO** and **Non CAO**.

- If the choice is **CAO**, a XAO file is required for each CAO boundary creation.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_with_homard_boundary_cao.png)

**See more** at [CAO boundary](homard_create_boundary.md#homard-create-boundary-cao).

- If the choice is **Non CAO**, some discrete and/or analytical boundaries can be created.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_with_homard_boundary_discrete.png)

**See more** at [Discrete boundary](homard_create_boundary.md#homard-create-boundary-di).

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_with_homard_boundary_analytical.png)

**See more** at [Analytical boundary](homard_create_boundary.md#homard-create-boundary-an).

Note

The exhaustive description of HOMARD can be read into its documentation. It can be reached by the general help button.

**See Also** a sample TUI Script of adaptation with [HOMARD](tui_adaptation.md#tui-homard-adapt).

## MG_Adapt

For meshes made of triangles and/or tetrahedra, remeshing operations are available with the MG-Adapt plugin. The remeshing is based on wanted mesh sizes defined over the mesh or as a constant. The boundaries are dedeuced from the initial mesh.

To start **Remeshing** operation, select **Remesh with MG_Adapt** item in **Adaptation** menu.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_01.png)

- **Mesh In** is the initial mesh to remesh.
- **Mesh Out** is the resulting mesh after remeshing. By default, the name of the initial mesh is kept and the file name is based on the name of the initial mesh.
- **Size map definition** is a choice between **Local**, **Background** and **Constant**.

- If the choice is **Background**, the name of the MED file must be given.
- If the choice is **Local** or **Background**, the name of the field must be selected from the list, together with time step.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/adaptation_02.png)

Note

The exhaustive description of MG-Adapt can be read into its documentation. It can be reached by the general help button.

**See Also** a sample TUI Script of [Adaptation](tui_adaptation.md#tui-adaptation-page).
