<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/faceFeature.html -->

# Face

Face feature creates one or several faces using shapes already existing in other objects.

To create a face in the active part:

1. select in the Main Menu *Build - > Face* item or
2. click ![feature_face.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_face.png) **Face** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Face.png)

Create a face

Select one or several faces in viewer. Additionally, a face can be build by a closed wire or a set of edges composing a closed wire.

It is possible to build a non-planar face by selecting non-planar wire or set of edges composing a closed wire, which do not belong to only one plane.

It is also possible to select a whole sketch result from the object browser. In this case, the smallest closed contour of the sketch will be transformed to the planar face.

**Apply** button creates faces.

**Cancel** button cancels the operation.

**TUI Command**:

model.addFace(*Part_doc*, *Shapes*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a set of faces created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateFace.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Face](TUI_faceFeatures.md#tui-create-face) operation.
