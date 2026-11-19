<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/using_notebook_geom_page.html -->

# Using SALOME NoteBook

**SALOME NoteBook** allows defining variables to be used for creation and modification of objects.

A detailed description of the SALOME NoteBook can be found in the GUI documentation.

![using_notebook_geom.png](https://docs.salome-platform.org/latest/gui/GEOM/using_notebook_geom.png)

Definition of variables in SALOME NoteBook

![box3.png](https://docs.salome-platform.org/latest/gui/GEOM/box3.png)

Use of variables for creation of a box in Geometry module

The following limitations on the use of variables still exist:

- [Local Coordinate System](create_lcs_page.md) dialog box.  
  The notebook parameters are correctly applied, but the study update is problematic in case if the LCS is defined using an object whose dimensions are given by parameters.
- [Select color](color_page.md) dialog box.
- [Select Number of Isos](isolines_page.md) dialog box.

Our **TUI Scripts** provide you with useful examples of [Using SALOME NoteBook](tui_notebook_geom_page.md#tui_notebook_geom).
