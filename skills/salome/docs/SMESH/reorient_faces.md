<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/reorient_faces.html -->

# Orient faces

This operation allows fixing the orientation of a set of faces in the following ways:

- The required orientation of a set of neighboring faces can be defined by a vector giving the direction of a normal to a certain face. Since the direction of face normals in the set can be even opposite, it is necessary to specify a *control* face, the normal to which will be compared with the vector. This face can be either:
  :   - found by proximity to a given point, or
      - specified explicitly.
- The required orientation is given by faces of specified reference groups or/and sub-meshes. The reference groups can be omitted, then orientation of an arbitrary selected face to orient defines common orientation.
- Alternatively, the faces can be oriented relatively to the adjacent volumes.

The orientation of a face is changed by reverting the order of its nodes.

*To set orientation of faces:*

1. In the **Modification** menu select **Reorient faces** item or click *“Reorient faces”* button ![imgfac](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_faces_face.png) in the toolbar.
2. In the “Reorient faces” dialog box

   - Select a way to define orientation:

     > - ![imgpnt](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_faces_point.png) - by specifying a point and a vector
     > - ![imgfac](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_faces_face.png) - by specifying a face and a vector
     > - ![imggrp](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_faces_ref_groups.png) - by specifying reference face groups
     > - ![imgvol](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_faces_volume.png) - by specifying reference volume groups
   - Select the **Object(s)** (mesh, groups and/or sub-meshes) containing faces to reorient, in the Object Browser or in the 3D Viewer.
   - To reorient by direction of the face normal:

     > - Specify the coordinates of the **Point** by which the control face will be found. You can specify the **Point** by picking a node in the 3D Viewer or selecting a vertex in the Object Browser.
     > - Set up the **Direction** vector to be compared with the normal of the control face. There are following options:
     >
     >   > - adjust vector components directly;
     >   > - select a vertex in the Object Browser or a node in the 3D Viewer; their coordinates will define vector components;
     >   > - pick two nodes (holding Shift button), the **Direction** vector will go from the first to the second node.![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_2d_point.png)
     >   >
     >   > **The orientation of adjacent faces is chosen according to a vector. The control face is found by point.**
   - In the second mode it is possible to pick the **Face** by mouse in the 3D Viewer or directly enter the **Face** ID in the corresponding field.

     > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_2d_face.png)
     >
     > **The orientation of adjacent faces is chosen according to a vector. The control face is explicitly given.**
   - In the third mode, the faces can be reoriented equally to reference faces:

     - If necessary, select 2D **Reference objects** (groups or/and sub-meshes) containing the reference faces, in the Object Browser or in the 3D Viewer. This field can be left empty, then orientation of an arbitrary face will be used as a reference.

       > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_2d_refgroup.png)
       >
       > **The orientation of faces is given by reference face groups and/or sub-meshes.**
   - In the fourth mode, the faces can be reoriented according to volumes:

     - Select an object (mesh, sub-mesh or group) containing reference **Volumes**, in the Object Browser or in the 3D Viewer.
     - Specify whether face normals should point outside or inside the reference volumes using **Face normal outside volume** check-box.

       > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/reorient_2d_volume.png)
       >
       > **The orientation of faces is chosen relatively to adjacent volumes.**
3. Click the **Apply** or **Apply and Close** button to confirm the operation.

**See Also** a sample TUI Script of a [Reorient faces](tui_transforming_meshes.md#tui-reorient-faces) operation.
