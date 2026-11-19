<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/import_export_geom_obj_page.html -->

# Importing/exporting geometrical objects

### Table of Contents

- [General information](#io_general)
- [Import file](#io_import)
- [Export file](#io_export)
- [Import and export of shapes in XAO format](#io_xao)

# General information

In Geometry module you can import and export geometrical objects from/into **BREP**, **IGES**, **STEP**, **STL**, **XAO**, **VTK** (only export) and others files. The mechanisms of import and export are implemented via plugins, which gives the opportunity to expand the range of available formats by adding more plugins (for example, CATIA 5 or ACIS).

Note
:   If a plugin supports import of materials associated with shapes, these shapes are grouped corresponding to the imported materials. For the moment STEP import is the only plugin that supports this feature.

Our **TUI Scripts** provide you with useful examples of the use of [Import/Export](tui_import_export_page.md)

# Import file

*To import geometrical objects from a BREP, IGES, STEP or STL file:*

:   From the **File** menu choose **Import/<FormatName>**, where **<FormatName>** is a name of desirable format. In the **Import <FormatName>** dialog box select the file to import and press **Open**. The file will be imported in the module and its contents (geometrical object) will be displayed in the **Object Browser**.

The dialog box to import the file can provide additional parameters.

For example, dialog box for importing files in STL format:

![geomimport.png](https://docs.salome-platform.org/latest/gui/GEOM/geomimport.png)

Note
:   If the selected file is in IGES or STEP format and the model size is not expressed in meters, the user will be asked whether to take or not the units into account (see the picture below). This feature can be helpful if some wrong units have been written to the IGES or STEP file by a 3rd-party software.

![iges_unit.png](https://docs.salome-platform.org/latest/gui/GEOM/iges_unit.png)

Note
:   It is possible to re-open from the initial file a previously imported shape if the file has been changed on disk. For this, select **Reload From Disk** in the context menu of the imported shape. The reloaded shape will have the same representation parameters as before this operation.

![geomimport_reopen.png](https://docs.salome-platform.org/latest/gui/GEOM/geomimport_reopen.png)

# Export file

*To export geometrical objects into a BREP, IGES, STEP, STL or VTK file:*

:   Select the object you wish to export, then from the **File** menu choose **Export/<FormatName>**, where **<FormatName>** is a name of desirable format. In the **Export <FormatName>** dialog box define the name and the location of the file to export and press **Save**.

The dialog box to export the file can provide additional advanced parameters.

For example, dialog box for exporting files in STL format:

![geomexport.png](https://docs.salome-platform.org/latest/gui/GEOM/geomexport.png)

# Import and export of shapes in XAO format

XAO is a file format which describes a shape with its topology, groups and fields.

*To import a shape in the **XAO** format:*

:   In the **File** menu select **Import/XAO**.

![importxao_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/importxao_dlg.png)

It is possible to import a shape from XAO file using the TUI Command:

*ok, Shape, Sub_Shapes, Groups, Fields = geompy.ImportXAO(FileName)*

It is also possible to import a shape from XAO format memory buffer (bytes array) using the TUI Command:

*ok, Shape, Sub_Shapes, Groups, Fields = geompy.ImportXAOMem(aBuffer)*

*To export a shape in the **XAO** format:*

:   In the **File** menu select **Export/XAO**.

![exportxao_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/exportxao_dlg.png)

In this dialog:

- Click the arrow button and select in the Object Browser or in the Viewer the **Shape** to be exported.
- Input the **File name** to create a new file or click browse button to save in an existing file.
- Input the **Author** if needed.
- Tick **Export shape in a separate file** to write the shape in a separate BREP file, referenced in the XAO file. It will have the same name as the XAO file with the .brep extension appended.
- Select the **Groups** of the chosen shape to be exported.
- Select the **Fields** of the chosen shape to be exported.
- Press "Apply" or "Apply & Close" button to get the result.

It is possible to export a shape in XAO file using the TUI Command:

*geompy.ExportXAO(Shape, Groups, Fields, Author, FileName, ShapeFileName)*

It is also possible to export a shape in XAO format memory buffer (bytes array) using the TUI Command:

*aBuffer = geompy.ExportXAOMem(Shape, Groups, Fields, Author)*
