<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/fast_intersection_page.html -->

# Fast intersection

This operation checks if two selected shapes are overlapped.

This tool is useful for fast detection of intersections and gaps. In contrast to Boolean Operations, Partition and Detect Self-intersection algorithms that compute topological intersections, this algorithm computes intersections by generating tessellation (triangulation) of the source shapes and detecting overlapping of resulting meshes. High performance is achieved through the use of existing triangulation of faces. Due to this fact, the tool is not suitable for computing exact intersection of shapes; however, it can be used to quickly find zones where intersections can present, and then use these results in further analysis.

Note
:   For more information about Partition and Boolean Operations Algorithms and their limitations refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf).

![measures12.png](https://docs.salome-platform.org/latest/gui/GEOM/measures12.png)

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

In this dialog:

- **Object 1**  and  **Object 2**  the checked objects. **Selection** button allows picking them in the viewer or in the object browser.
- **Deflection coefficient** specifies the quality of shapes tessellation.
- **Detect gaps** - when switched on, allows detecting gaps between shapes.
- **Tolerance** - specifies the distance between shapes used for detecting gaps.
- **Compute intersections** - press this button to compute interferences.
- **Sub-shapes of Object 1** - list of sub-shapes from the first source shape that localize the intersection.
- **Sub-shapes of Object 2** - list of sub-shapes from the second source shape that localize the intersection.
- **Apply** and **Apply and Close** buttons are used to store selected intersected shapes in the study for further analysis (see below).

Note
:   The result quality depends on the quality of triangulation. Changing the value of the deflection coefficient parameter can strongly affect the result. However, small values of the deflection coefficient might lead to some performance loss of the algorithm, as number of triangles of the tessellation mesh depends on this parameter.

Press **Apply and Close** or **Apply** button to store the selected sub-shapes in the study for further analysis. The selection will be published as a compound containing intersected sub-shapes from both source objects.

**TUI Command:** *geompy.FastIntersect(theShape1, theShape2, theTolerance = 0.0, theDeflection = 0.001),*   
where:

- *theShape1* First shape.
- *theShape2* Second shape.
- *theTolerance* When it is negative or equal to zero, the function detects intersections; when it is positive, the function detects gaps.
- *theDeflection* Linear deflection for shapes; if deflection <= 0, default deflection 0.001 is used

**Result:** Boolean + two lists of IDs of sub-shapes (from input shapes) that localize the intersection.

See also a [TUI example](tui_fast_intersection_page.md).
