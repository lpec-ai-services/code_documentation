<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/extract_and_rebuild_page.html -->

# Extract and Rebuild

This operation allows extraction of sub-shapes from a given shape.

To use this operation, select in the Main Menu **Operations -> Extract and Rebuild**. The following dialog box appears:

![extract_rebuild.png](https://docs.salome-platform.org/latest/gui/GEOM/extract_rebuild.png)

Extract and Rebuild Dialog

In this dialog:

- **Name** is a result object name.
- **Main Object** is the main object selected for the operation. It is possible to select the object in the Object Browser or in the viewer using "selection" button.
- **Sub-shape type** is the type filter for sub-shapes to be chosen for the extraction.
- **Filtered shapes** is the list of filtered sub-shape IDs available for the extraction.
- **Shapes to extract** is the list of sub-shape IDs to be extracted grouped by shape types.
- **>>** is the button to copy object IDs from **Filtered shapes** to **Shapes to extract**.
- **<<** is the button to copy object IDs from **Shapes to extract** to **Filtered shapes**.
- **Show Only Selected** is the button to show objects selected in the **Filtered shapes** list and hide all other objects.
- **Hide Selected** is the button to hide objects selected in the **Filtered shapes** list.
- **Show all sub-shapes** is the button to show all objects from the **Filtered shapes** list.
- **Rebuild** is the button to perform extraction and show the operation statistics.
- The block of **Statistics** shows how many shapes of a certain type are **Removed**, **Modified** and **Added**.
- **Apply** is the button to create the result.
- **Apply and Close** is the button to create the result and close the dialog.
- **Close** is the button to close this dialog.
- **Help** is the button to show this help page.

**TUI Command:** *geompy.MakeExtraction(theShape, theListOfID),*   
where *theShape* is the main shape, *theListOfID* is a list of sub-shape IDs to be extracted.

Our **TUI Scripts** provide you with useful example of the use of [Extract and Rebuild](tui_test_all_page.md#swig_MakeExtraction) functionality.

**More details**

If a sub-shape is extracted, all its ancestors should be modified. An ancestors of extracted sub-shapes can be either:

- created anew without extracted sub-shapes, or
- extracted if it is not possible to create a valid shape without extracted sub-shape.

E.g. it is necessary to extract the vertex from the box:

![extract_init.png](https://docs.salome-platform.org/latest/gui/GEOM/extract_init.png)

Extraction of the vertex from the box

In this case 3 ancestor edges are removed as they can't be valid without this vertex. 3 faces that contain these edges are also removed. It is because the wires without edges are not closed and it is not possible to create a valid face on not closed wire. These wires should contain two remaining edges, but they are removed as they are the part of the remaining shell. So these wires become empty that means that they should be removed as well.

The shell is replaced by another one that contains 3 not modified faces. As It is not possible to construct a valid solid from not closed shell the solid is removed. So the result of the extraction is a shell that contains 3 faces:

![extract_result.png](https://docs.salome-platform.org/latest/gui/GEOM/extract_result.png)

Result shape

Please, refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/ExtractAndRebuild.pdf) for a detailed description of Extract and Rebuild operation.
