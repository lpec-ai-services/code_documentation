<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/unionFeature.html -->

# Union

**Caution**. This operation is obsolete. Fuse operation should be used instead.

Union feature implements a Boolean operation for creation of a union of selected objects.

To create a Union in the active part:

1. select in the Main Menu *Features - > Union* item or
2. click ![union_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/union_btn.png) **Union** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Union.png)

**Union operation**

Here it is necessary to select some objects. Only faces with shared edges or solids with shared faces are allowed for selection.

**Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.

**Apply** button creates a union shape.

**Cancel** button cancels the operation.

**TUI Command**:

model.addUnion(*Part_doc*, *objects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object.
        - **objects** – A list of objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Result object.

## Result

The Result of the operation will be a shape which is a union of selected objects:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedUnion.png)

**Union created**

**See Also** a sample TUI Script of [Create Union](TUI_unionFeature.md#tui-create-union) operation.
