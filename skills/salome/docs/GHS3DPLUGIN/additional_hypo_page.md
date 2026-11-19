<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/additional_hypo_page.html -->

# Additional Hypotheses

**Additional Hypotheses** can be applied as a supplement to the main hypotheses, introducing additional concepts to mesh creation.

One additional hypotheses can be used together with MG-Tetra algorithm:

- **Viscous Layers** additional hypothesis can be used together with MG-Tetra. This hypothesis allows creation of layers of highly stretched prisms near mesh boundary, which is beneficial for high quality viscous computations. The prisms constructed on the quadrangular mesh faces are actually the hexahedrons.

For more detailed description of the this additional hypothesis please refer SALOME Mesh User's Guide.
