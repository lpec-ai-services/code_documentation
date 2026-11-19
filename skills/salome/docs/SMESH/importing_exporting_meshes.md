<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/importing_exporting_meshes.html -->

# Importing and exporting meshes

## File formats

In MESH there is a functionality allowing import/export of meshes in the following formats:

- **MED**,
- **UNV** (I-DEAS 10),
- **STL**,
- **CGNS**,
- **GMF** (internal format of DISTENE products from the MeshGems suite),
- **DAT** (simple ascii format).

You can also export a group as a whole mesh.

### Additional file formats with **GMSH**

It is possible to use additional file formats using **GMSH** backend with the following approach:

- The mesh is first saved in a temporary MED file.
- The MED file is then read by **GMSH** and converted to the desired file format using `--format` option.

Following formats are currently supported:

- Gmsh 4.1 ([*](#id1).msh)
- Gmsh 2.2 ([*](#id3).msh)
- MAIL ([*](#id5).mail)
- Abaqus ([*](#id7).inp)
- MED/Salome ([*](#id9).med)
- Medit MESH ([*](#id11).mesh)
- Nastran ([*](#id13).bdf)
- OBJ ([*](#id15).obj)
- OFF ([*](#id17).off)
- PLY ([*](#id19).ply)
- STL ([*](#id21).stl)
- SU2 ([*](#id23).su2)
- Tecplot ([*](#id25).tec)
- VTK ([*](#id27).vtk)

**WARNING**: Due to limitations in the Gmsh 2.2 format, groups will be automatically created by dimension to export the various elements (Group_Of_All_Edges, Group_Of_All_Faces, Group_Of_All_Volumes).

### Additional file formats with **MeshIO**

It is also possible to use additional file formats using **MeshIO** library:

- The mesh is first saved in a temporary MED file.
- The MED file is then read by **MeshIO** and converted to the desired file formatusing `--output-format` option.

The following formats are currently supported:

- ANSYS msh ([*](#id29).msh)
- AVS-UCD ([*](#id31).avs)
- DOLFIN XML ([*](#id33).xml)
- Exodus ([*](#id35).e)
- Exodus ([*](#id37).exo)
- FLAC3D ([*](#id39).f3grid)
- H5M ([*](#id41).h5m)
- Kratos/MDPA ([*](#id43).mdpa)
- Medit MESHB ([*](#id45).meshb)
- Nastran ([*](#id47).fem)
- Nastran ([*](#id49).nas)
- Netgen ([*](#id51).vol)
- Netgen ([*](#id53).vol.gz)
- PERMAS ([*](#id55).post)
- PERMAS ([*](#id57).dato)
- SVG, 2D output only ([*](#id59).svg)
- TetGen ([*](#id61).node)
- TetGen ([*](#id63).ele)
- UGRID ([*](#id65).ugrid)
- VTU ([*](#id67).vtu)
- WKT, TIN ([*](#id69).wkt)
- XDMF ([*](#id71).xdmf)
- XDMF ([*](#id73).xmf)

## Import

*To import a mesh:*

1. From the **File** menu choose the **Import** item, from its sub-menu select the corresponding format (MED, UNV, STL, GMF and CGNS) of the file containing your mesh.
2. In the standard **Search File** dialog box find the file for import. It is possible to select multiple files to be imported all at once.
3. Click the **OK** button.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshimportmesh.png)

## Export

*To export a mesh or a group:*

1. Select the object you wish to export.
2. From the **File** menu choose the **Export** item, from its sub-menu select the format (MED, UNV, DAT, STL, GMF and CGNS) of the file which will contain your exported mesh.
3. In the standard **Search File** select a location for the exported file and enter its name.
4. Click the **OK** button.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshexportmesh.png)

If you try to export a group, the warning will be shown:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshexportgroupwarning.png)

- **Don’t show this warning anymore** check-box allows to switch off the warning. You can re-activate the warning in [Preferences](mesh_preferences.md#group-export-warning-pref).

Only MED format supports all types of elements that can be created in the module. If you export a mesh or group that includes elements of types that are not supported by chosen format, you will be warned about that.

There are additional parameters available at export to MED format files.

- **Z tolerance** field if enabled specifies distance of nodes from the XOY plane below which the nodes snap to this plane. A default value can be set in [Preferences](mesh_preferences.md#medexport-z-tolerance-pref).
- **Automatically create groups** check-box specifies whether to create groups of all mesh entities of available dimensions or not. The created groups have names like “Group_On_All_Nodes”, “Group_On_All_Faces”, etc. A default state of this check-box can be set in [Preferences](mesh_preferences.md#export-auto-groups-pref).
- **Automatically define space dimension** check-box specifies whether to define space dimension for export by mesh configuration or not. Usually the mesh is exported as a mesh in 3D space, just as it is in Mesh module. The mesh can be exported as a mesh of a lower dimension in the following cases, provided that this check-box is checked:

  - **1D**: if all mesh nodes lie on OX coordinate axis.
  - **2D**: if all mesh nodes lie in XOY coordinate plane.
- [Save cell/node numbers to MED file](mesh_preferences.md#med-export-numbers-pref) preference controls whether node and cell numbers are saved.

**See Also** a sample TUI Script of an [Export Mesh](tui_creating_meshes.md#tui-export-mesh) operation.
