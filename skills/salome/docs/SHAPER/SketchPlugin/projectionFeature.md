<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/projectionFeature.html -->

# Projection

The Projection operation creates a projection of 3D edge or vertex onto the sketch plane.

The result of projection is a line.

To create a Projection in the active Sketch:

1. select in the Main Menu *Sketch - > Projection* item or
2. click ![projection.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Projection.png) **Projection** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Projection_panel.png)

Projection

Input fields:

- **Object** is the 3D object (edge or vertex) to project onto the sketch plane.
- **Include into the sketch result** option defines whether to include the projection line into the sketch result.

**TUI Commands**:

Sketch_1.addProjection(*EdgeOrVertex*, *IncludeIntoResult*)
:   Parameters:
    :   - **object** – Edge or vertex.
        - **boolean** – Include into the result flag.

    Returns:
    :   Result object.

Sketch_1.addProjection(*EdgeOrVertexName*, *IncludeIntoResult*)
:   Parameters:
    :   - **object** – Edge or vertex name.
        - **boolean** – Include into the result flag.

    Returns:
    :   Result object.

## Result

Created Projection appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Projection_res.png)

Created projection (purple line)

**See Also** a sample TUI Script of [Create Projection](TUI_projection.md#tui-create-projection) operation.
