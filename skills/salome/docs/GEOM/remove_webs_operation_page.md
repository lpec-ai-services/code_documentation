<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/remove_webs_operation_page.html -->

# Remove Internal Faces

To **Remove internal faces** in the **Main Menu** select **Repair - > Remove internal faces**.

This operation removes all shared faces from given solids to obtain one or more bigger solids from a set of smaller solids.

![remove_webs.png](https://docs.salome-platform.org/latest/gui/GEOM/remove_webs.png)

**Arguments:** Name + one or more shapes containing solids.   
**Advanced option:** [Set presentation parameters and sub-shapes from arguments](restore_presentation_parameters_page.md).

Note
:   Only shared faces will be removed. Coincident but not shared faces will stay as is, use [Glue Faces](glue_faces_operation_page.md) or [Partition](partition_page.md) before **Remove Internal Faces** if you need to remove them.

**TUI Command:**   
*geompy.RemoveInternalFaces( theSolids )*,  
where *theSolids* is either a compound or a list of solids.

Our **TUI Scripts** provide you with useful examples of the [Remove Internal Faces](tui_repairing_operations_page.md#tui_remove_webs) functionality usage.
