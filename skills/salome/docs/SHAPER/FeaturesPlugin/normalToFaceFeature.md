<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/normalToFaceFeature.html -->

# Normal to a face

The **Normal to a face** feature displays the normal to a face. A vertex can be specified to indicate the position of the normal else the center of face is used.

The resulting normal can be created via a dedicated check-box **Create normal**. If this last is checked corresponding result and feature would be created.

If the check-box **Create normal** isn’t checked, **Apply** button does not generate any result and has the same effect as **Cancel** for this feature.

To display the normal to a face in the active part:

1. select in the Main Menu *Inspection - > Normal to a face* item or
2. click ![normalToFace.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/normal.png) **Normal to a face** button in the toolbar

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/normalToFacePropertyPanel.png)

Normal to a face

Input fields:

- **Face** contains face selected in 3D OCC viewer or object browser.
- **Vertex** contains optional vertex selected in 3D OCC viewer or object browser.
- **Create normal** check-box allow the creation of the normal (result and feature).

**TUI Command**:

model.getNormal(*Part*, *face*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A face in format *model.selection(“FACE”, face)*.

    Returns:
    :   Created normal to a face in the center of the face.

## Result

Result of **Normal to a face**.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/normalToFaceResult.png)

Normal to a face

**See Also** a sample TUI Script of [Create normal to a face](TUI_normalToFaceFeature.md#tui-create-normal-to-face) operation.

**TUI Command**:

model.getNormal(*Part*, *face*, *vertex*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A face in format *model.selection(“FACE”, face)*.
        - **object** – A vertex in format *model.selection(“VERTEX”, vertex)*.

    Returns:
    :   Created normal to a face at vertex.

## Result

Result of **Normal to aface** where **Vertex** is selecteted.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/normalToFaceResultWithVertex.png)

Normal to a face at vertex

**See Also** a sample TUI Script of [Create normal to a face at vertex](TUI_normalToFaceFeature.md#tui-create-normal-to-face-at-vertex) operation.
