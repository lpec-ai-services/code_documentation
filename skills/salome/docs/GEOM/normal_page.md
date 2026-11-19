<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/normal_page.html -->

# Normal to a Face

This operation calculates the normal vector to the selected **Face**.

![normaletoface.png](https://docs.salome-platform.org/latest/gui/GEOM/normaletoface.png)

- **Face** is the face whose Normal should be calculated.
- **Point** is a point on this face. If the point is not given, the normal is calculated at the center of mass.

Press **Apply** or **Apply and Close** button to publish the **Normal** **Vector** in the study.

**TUI Command:** *geompy.GetNormal(Face, OptionalPoint = None)*.

See also a [TUI example](tui_normal_face_page.md).
