<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/checkSharedFaceFeature.html -->

# Check shared faces

The **Check shared faces** feature find the shared faces within a composolid or compound.

The result is a list of faces and a group that can be created with a specified name.

To check shared faces in the active part:

1. Select in the Main Menu *Inspection - > Check shared faces* item or
2. Click ![shared_shapes.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/shared_shapes.png) **Check shared faces** button in the toolbar

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/checkSharedFacesPropertyPanel.png)

Check shared faces

Input fields:

- **Object** contains composolid or compound selected in 3D OCC viewer or object browser.
- **Number of shared faces** indicate the number of found faces.
- **List of faces** the list of found faces.
- **Transparency** set the transparency of selected object.
- **Create group** check-box that allows the creation of the found faces group.
- **Group name** specifies the name of the group created.

**TUI Command**:

model.getSharedFaces(*Part_doc*, *shape*, *nameGroup*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A composolid or compound in format *model.selection(TYPE, shape)*.
        - **string** – The name of group to create

    Returns:
    :   Created group.

## Result

Result of **Check shared faces** where **Create group** is checked.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/sharedFacesResult.png)

Shared faces

**See Also** a sample TUI Script of [Check shared faces](TUI_sharedFacesFeature.md#tui-shared-faces) operation.
