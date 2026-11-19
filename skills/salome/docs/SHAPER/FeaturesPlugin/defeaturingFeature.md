<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/defeaturingFeature.html -->

# Defeaturing

**Defeaturing** operation is intended for removal of the unwanted parts or features from the model. These parts can be holes, protrusions, gaps, chamfers, fillets, etc.

To create a Defeaturing in the active part:

1. select in the Main Menu *Feature -> Defeaturing* item or
2. click ![defeaturing.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/defeaturing.png) **Defeaturing** button in the toolbar.

After that select one or more faces of solids to suppress them. The Defeaturing works with faces from comsolids and compounds of solids as well.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/defeaturing_property_panel.png)

Defeaturing property panel

Input field:

- **Faces to remove** panel contains the list of faces which should be suppressed.

**TUI Command**:

model.addDefeaturing(*Part_doc*[, *faces*])
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of faces in format *model.selection(“FACE”, shape)*.

    Returns:
    :   Created object.

## Result

Result of **Defeaturing** is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/defeaturing_result.png)

Defeaturing operation

**See Also** a sample TUI Script of [Perform Defeaturing](TUI_defeaturingFeature.md#tui-defeaturing) operation.

## References

For more information, please, visit [OpenCASCADE Documentation](https://dev.opencascade.org/doc/overview/html/occt_user_guides__modeling_algos.html#occt_modalg_defeaturing).
