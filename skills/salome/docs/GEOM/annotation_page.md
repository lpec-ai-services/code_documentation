<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/annotation_page.html -->

# Shape annotation

**Annotation**  functionality allows showing in the viewer special user-defined text label connected to corresponding part of a CAD model with a line. Annotation text is always parallel to the screen and horizontal. It is not zoomed or rotated when a 3D scene is zoomed or rotated by the user. The annotation text is defined using UTF-8 encoding and thus support any Unicode characters.

There are several algorithms for the annotation position calculation during the scene manipulations (panning, zooming, rotation):

- Algorithm 1: an annotation has fixed position in 2D screen coordinates (fixed screen position mode). In this mode, the annotations are always visible (appear as topmost objects), never hidden by the (annotated) geometry.
- Algorithm 2: an annotation has fixed position in 3D model space, this position is projected onto the screen just as normal point coordinates. In this mode, some annotations may be invisible depending on the camera (position, orientation, zoom).

![annotation_preview.png](https://docs.salome-platform.org/latest/gui/GEOM/annotation_preview.png)

It can be accessed from the main menu via **Inspection -> Annotation**

![annotation.png](https://docs.salome-platform.org/latest/gui/GEOM/annotation.png)

Create Annotation dialog

In this dialog you can:

- Set **Text** text shown in View 3d and a name of annotation presented in the Text Browser.
- Select a **Shape** to which the annotation will be assigned.
- Set **Fixed screen position** to select alogithm for the annotation position caldulation.
- Select a **Shape Type** to which the annotation will be assigned on the shape. It contains "Whole shape", "Vertex", "Edge", "Face" and "Solid" choices.
- Select a sub shape to assign annotation to. Text control contains information about local selection in the viewer.
- Move annotation dragging it in 3D view to select an appropriate position.
- Push **Apply** or **Apply and Close** button to commit creation of the field.

Annotations appear in an Annotations sub-tree in Text Browser. The foolowing context menu commands are provided for annotation object in Text Browser:

- **Edit** allows modifying the annotation text, the positioning algorithm and the annotation position.
- **Delete** deletes selected annotation.
- **Show**/**Hide** change visibility of annotation in the active view.

**Edit** and **Delete** actions are also available in View 3d for selected annotation object/s.

All annotations may be shown/hidden in a 3D view. The corresponded popup menu is available in Text Browser.

All annotations of a shape may be shown/hidden in a 3D view using corresponded popup menu on the shape item in Object Browser.

Synchronization of selection between 3D view and Text browser is available. It means that selection of annotation in 3D view will select this annotation in Text browser and vice versa.

Annotation is logically connected to the shape:

- Selection of an annotation will highlight corresponding shape/subshape in 3D view.
- When the shape is deleted, the annotation will be also deleted.

The user is able to modify the font, the style, the color and the size of the annotation text and the color, the width and the style of the connection line applied to all annotations. It can be accessed from the main menu via **File -> Preferences**. The Shape annotations group on Geometry Settings pane contains controls for it.
