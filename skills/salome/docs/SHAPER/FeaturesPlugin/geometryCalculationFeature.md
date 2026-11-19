<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/geometryCalculationFeature.html -->

# Geometry calculation

The **Geometry calculation** feature displays basic properties of sub-elements of a geometrical object (shape).

The geometry calculation displayed in the property panel are length, area and volume.

**Apply** button does not generate any result and has the same effect as **Cancel** for this feature.

To display geometry calculation in the active part:

1. select in the Main Menu *Inspection - > Geometry calculation* item or
2. click ![GeometryCalculation.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/geometryCalculation.png) **Geometry calculation** button in the toolbar

The geometry calculation can be displayed for a selected object in the property panel :

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/geometryCalculationPropertyPanel.png)

Geometry calculation

Input fields:

- **Object** contains an object selected in 3D OCC viewer or object browser.

The geometry calculation displayed can be selected.

**TUI Command**:

model.getGeometryCalculation(*Part_doc*, *shape*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A shape in format *model.selection(“type”, shape)*.

    Returns:
    :   list containing length, area and volume.

**See Also** a sample TUI Script of [Get Geometry Calculation](TUI_geometryCalculation.md#tui-geometry-calculation) operation.
