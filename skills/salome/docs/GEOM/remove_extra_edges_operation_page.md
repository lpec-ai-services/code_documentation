<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/remove_extra_edges_operation_page.html -->

# Remove Extra Edges

To **Remove extra edges** in the **Main Menu** select **Repair - > Remove extra edges**.   
This operation removes all seam and degenerated edges from a given shape. Its main purpose is healing of solids and compounds to obtain hexahedral solids and compounds of hexahedral solids. However, there is an option to unite all faces sharing one surface, which produces not only hexahedral solids.

**TUI Command:** *geompy.RemoveExtraEdges(theShape,doUnionFaces)*, where *theShape* is a compound or a single solid and *doUnionFaces* is a boolean parameter, that regulates, whether the faces, sharing a common surface, should be united.   
**Arguments:** Name + one shape + a flag.   
**Advanced option:** [Set presentation parameters and sub-shapes from arguments](restore_presentation_parameters_page.md).

![remove_extra_edges.png](https://docs.salome-platform.org/latest/gui/GEOM/remove_extra_edges.png)

**Example:**

![remove_extra_edges1.png](https://docs.salome-platform.org/latest/gui/GEOM/remove_extra_edges1.png)

*Shape with extra edges*

![remove_extra_edges2.png](https://docs.salome-platform.org/latest/gui/GEOM/remove_extra_edges2.png)

*Improved shape*

Our **TUI Scripts** provide you with useful examples of the [Remove Extra Edges](tui_test_others_page.md#swig_RemoveExtraEdges) functionality usage.
