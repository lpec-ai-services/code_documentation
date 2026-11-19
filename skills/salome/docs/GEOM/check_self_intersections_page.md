<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/check_self_intersections_page.html -->

# Detect Self-intersections

To **Detect Self-intersections,** select in the **Main Menu** **Inspection - > Detect Self-intersections**.

There are two ways to check self-intersections.

### Check topological intersections

This operation checks the topology of the selected shape to detect self-intersections.

![measures11.png](https://docs.salome-platform.org/latest/gui/GEOM/measures11.png)

In this dialog:

- **Object** - the checked object. **Selection** button allows picking it in the viewer or in the object browser.
- **Level of check** - combo box allows setting the level of self-interference checking. It defines, which interferences will be checked. The default value is "All interferences".
- **Compute self-intersections** button performs the computation.
- **Summary** section contains the general report about self-intersections of the object and/or errors that occurred during the computation.
- **Self-intersections** list contains the list of detected self-intersections. Select the intersection to show **Sub-shapes** in the field to the right.
- **Apply** and **Apply and Close** buttons store the interferences selected in the **Self-intersections** list box in the study for further analysis. If no interferences are selected, all of them are published in the study. Each interference is published as a child compound of the source shape and contains a couple of intersecting sub-shapes.

Note
:   This tool is useful for detection of shapes that are not suitable as arguments of Boolean operations and Partition algorithm. For more information about Partition and Boolean Operations Algorithms and their limitations refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf).

**Result:** Boolean.   
**TUI Command:** *geompy.CheckSelfIntersections(theShape, theCheckLevel = [GEOM.SI_ALL](../GEOM/geompy_doc/namespaceGEOM.md#a641c5ffe8056644e5e5d7ba64f10734ba0f8b4970af9e8b95bc385134fda213f7)),*   
where:   
*theShape* is the shape checked for validity.   
*theCheckLevel* is the level of check. Default value is [GEOM.SI_ALL](../GEOM/geompy_doc/namespaceGEOM.md#a641c5ffe8056644e5e5d7ba64f10734ba0f8b4970af9e8b95bc385134fda213f7) to check all interferences.

See also a [TUI example](tui_check_self_intersections_page.md).

### Fast intersection

This operation allows quickly detecting self-interferences of the given shape using the algorithm based on mesh intersections.

The algorithm works on the face level, i.e. it computes only face-to-face intersections. No additional intersection types are computed.

This can be useful to detect all intersections between subshapes of type "surface" in an assembly. The result quality will depend on the tessellation quality. However, small deflection values can significantly decrease the performance of the algorithm. Nevertheless, the performance of Fast Intersect algorithm is much higher than that of the topological intersection.

![measures13.png](https://docs.salome-platform.org/latest/gui/GEOM/measures13.png)

In this dialog:

- **Object** - the checked object. **Selection** button allows picking it in the viewer or in the object browser.
- **Deflection coefficient** - a linear deflection coefficient that defines the tessellation quality. If theDeflection <= 0, default deflection 0.001 is used.
- **Detect gaps with tolerance** specifies the distance between shapes used for detecting gaps:
  - if theTolerance <= 0, the algorithm detects intersections;
  - if theTolerance > 0, the algorithm detects gapss.
- **Compute self-intersections** button performs the computation.
- **Summary** section contains the general report about self-intersections of the object and/or errors that occurred during the computation.
- **Self-intersections** list contains the list of detected self-intersections. Select the intersection to show **Sub-shapes** in the field to the right.
- **Apply** and **Apply and Close** buttons store the interferences selected in the **Self-intersections** list box in the study for further analysis. If no interferences are selected, all of them are published in the study. Each interference is published as a child compound of the source shape and contains a couple of intersecting sub-shapes.

**Result:** Boolean.   
**TUI Command:** *geompy.CheckSelfIntersectionsFast(theShape, theDeflection, theTolerance),*   
where:   
*theShape* is the shape checked for validity.   
*theDeflection* that specifies the quality of tessellation. *theTolerance* Specifies the distance between shapes used for detecting gaps.

See also a [TUI example](tui_check_self_intersections_fast_page.md).
