<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/intersectionFeature.html -->

# Intersection

Intersection feature a boolean operation for intersection of a set of main objects with a set of tool objects.

To perform a boolean operation Intersection in the active part:

1. select in the Main Menu *Features - > Intersection* item or
2. click ![intersection_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/intersection_btn.png) **Intersection** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/intersection_property_panel.png)

**Intersection operation**

**Objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be intersected.

**Fuzzy Parameter** - defines the additional tolerance value used to eliminate tiny results.

All intersected objects should be 1- or 2-dimensional (edges, faces, shells). However, it is allowed to select
3-dimensional objects, but only their shells will be taken into operation.

**TUI Command**:

model.addIntersection(*Part_doc*, *Objects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Created object.

## Result

The Result of the operation will be a shape which is an intersection of selected objects:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedIntersection.png)

**Intersection created**

**See Also** a sample TUI Script of [Create Intersection](TUI_intersectionFeature.md#tui-create-intersection) operation.
