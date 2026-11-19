<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/additional_hypo_page.html -->

# Additional Hypotheses

**Additional Hypotheses** can be applied as a supplement to introducing additional concepts to mesh creation.

Following additional hypotheses can be used together with NETGEN algorithm:

- **Viscous Layers** additional hypothesis can be used together with NETGEN 3D and NETGEN 1D-2D-3D algorithms. This hypothesis allows creation of layers of highly stretched prisms near mesh boundary, which is beneficial for high quality viscous computations. The prisms constructed on the quadrangular mesh faces are actually the hexahedrons.
- **Quadrangle Preference** - This additional hypothesis can be used together with NETGEN 2D algorithm. It allows NETGEN 2D to build quad-dominant meshes.

For more detailed description of the described above hypothesis please refer SALOME Mesh User's Guide.
