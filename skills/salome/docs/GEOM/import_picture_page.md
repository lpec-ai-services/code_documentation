<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/import_picture_page.html -->

# Import a picture in the OCC viewer

It is possible in [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) to import a picture file in the OCC view. The supported formats are : .bmp, .gif, .pix, .xwd, .rgb, .rs

The imported picture (engineering drawing, nautical chart, etc.) may be used as a support for 2D shape design.

It is possible to create a [sketch](create_sketcher_page.md) on top of this picture or use the [Shape recognition](shape_recognition_page.md) functionalities to build geometrical shapes from some elements of the picture (contours, corners ...).

To **import a picture** in the view:

- select **New Entity -> Import a picture in the view** or click on

  ![import_picture.png](https://docs.salome-platform.org/latest/gui/GEOM/import_picture.png)
- Click on **...** and browse your image files to select one of them
- Apply

A new **Picture** object is created. Pan, zoom and rotation operations are available in the view like for any other object.

![picture_import_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/picture_import_dlg.png)
