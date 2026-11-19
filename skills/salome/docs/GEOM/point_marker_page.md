<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/point_marker_page.html -->

# Point Marker

You can change the representation of the geometrical vertices in the 3D viewer either by selecting one of the predefined shapes or by loading a custom texture from an external file.

- Standard point markers

The Geometry module provides a set of predefined point marker shapes which can be used to display vertices in 3D viewer. Each standard point marker has two attributes: type (defines shape form) and scale factor (defines shape size).

![point_marker_dlg1.png](https://docs.salome-platform.org/latest/gui/GEOM/point_marker_dlg1.png)

**TUI Command:** *go.SetMarkerStd(Type, Size)*.

![std_point_marker.png](https://docs.salome-platform.org/latest/gui/GEOM/std_point_marker.png)

Standard point markers

- Custom point markers

It is also possible to load a point marker shape from an external file. This file should provide a description of the point texture as a set of lines; each line is represented as sequence of "0" and "1" symbols, where "1" symbol means an opaque pixel and "0" symbol means a transparent pixel. The width of the texture correspond to the length of the longest line in the file, expanded to the nearest byte-aligned value. The height of the texture is equal to the number of non-empty lines in the file. Note that missing symbols are replaced by "0".

Here is a texture file sample:

```python

00111100
00111100
11111111
11111111
11111111
11111111
00111100
00111100
```

![point_marker_dlg2.png](https://docs.salome-platform.org/latest/gui/GEOM/point_marker_dlg2.png)

**TUI Command:** *go.SetMarkerTexture(ID)*.

![custom_point_marker.png](https://docs.salome-platform.org/latest/gui/GEOM/custom_point_marker.png)

Custom point markers

Our **TUI Scripts** provide you with useful examples of [Point Marker](tui_viewing_geom_objs_page.md#tui_point_marker) setting.
