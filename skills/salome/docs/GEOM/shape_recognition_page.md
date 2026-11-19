<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/shape_recognition_page.html -->

# Shape recognition from a picture

Note
:   1. This functionality is not fully operational yet. It is provided for testing purpose and because it might already be helpful in some situations. (Do not hesitate to make feedbacks on possible bugs ...)
    2. The functionality is only available if SALOME has been built with the optional prerequisite OpenCV.

This tool allows you to automatically create geometrical shapes from pictures with help of shape recognition algorithms. **Contours** or **Corners** can be built.

**Example:**

Detection of the cost line on a nautical chart

![contour_detection_example2.png](https://docs.salome-platform.org/latest/gui/GEOM/contour_detection_example2.png)

To use the **Shape recogition** tool:

1. [Import a picture](import_picture_page.md) in the view
2. Select **New Entity -> Shape Recognition** or click on

   ![feature_detect.png](https://docs.salome-platform.org/latest/gui/GEOM/feature_detect.png)

Then you can choose to create either **contours** or **corners** from this picture.

To create **Contours** :

1. Select in the **Picture** field a previously imported picture.
2. Click on

   ![occ_view_camera_dump.png](https://docs.salome-platform.org/latest/gui/GEOM/occ_view_camera_dump.png)
3. Draw a rectangle in the zone whose contour is to be found. The zone will be identified by the colors of this **Filtering Sample**.

   **Example:**

   In the picture shown above, the contours have been drawn basing on the sample, containing white and violet color, thus all white and violet areas in the picture are included in the outlined zone.

   ![feature_detection_dlg3.png](https://docs.salome-platform.org/latest/gui/GEOM/feature_detection_dlg3.png)
4. **Output type**

   - **Spline** : The **result** will be a **Compound** of **Edges**. Each contour will be a single **edge** based on a B-Spline curve (it will be smooth).
   - **Polyline** : The **result** will be a **Compound** of **Wires**. Each contour will be a wire made of lines (i.e. a **Polygon**)

   In both cases each contour can then be retrieved by an explode operation with the appropriate subshape type.

   Note
   :   It is better to use the **Spline** output type unless you want to find the frontier of a polygon (rectangle ...)

To create **Corners** :

1. In the **Picture** field select a previously imported picture.
2. Apply

   The **Result** will be a **Compound** of **Vertices**

   ![feature_detection_dlg2.png](https://docs.salome-platform.org/latest/gui/GEOM/feature_detection_dlg2.png)
