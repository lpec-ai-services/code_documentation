<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/scaled_jacobian.html -->

# Scaled Jacobian

The **Scaled Jacobian** mesh quality criteria is a scalar measure of the deviation from the perfect element in the geometrical sense. This measure normalizes the range of reported values between [0,1] for a normal element, the value of 1 is considered a perfect element and 0 a element with a collapsed side. Negative values are also accepted for invalid elements.

The **Scaled Jacobian** is implemented for all volumetric elements (except for polyhedrons, returning 0).

For tetrahedrons and hexahedrons, the formulas are
defined in [The Verdict Library Reference Manual [1]](https://gitlab.kitware.com/third-party/verdict/-/blob/master/SAND2007-2853p.pdf).

For pyramid, the minimum scaled jacobian of the four tetrahedrons formed
in the four vertices of the pyramid base is reported.

For pentahedron, a decomposition into tetrahedron is also done.

For hexahedron prisms, the minimum scaled jacobian between two pentahedrons and one hexahedron is reported.

- Geometrically the Scaled Jacobian of a **tetrahedron** can be understood by the follow figure:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaled_jacobian_tetra.png)
  >
  > The reported Scaled Jacobian will be 1 if \(\alpha=45^{\circ}\)
- For **hexadrons** this measure return 1 for the perfect non rotated elements:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaled_jacobian_hexa.png)
  >
  > The reported Scaled Jacobian will be 1 if \(\alpha=0^{\circ}\) for all the vertices

*To visualize the Scaled Jacobian quality criterion in your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Volume Controls > Scaled Jacobian** or click *“Scaled Jacobian”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaled_jacobian.png) of the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaled_jacobian_mesh_hexa.png)

**See Also** a sample TUI Script of a [Scaled Jacobian](tui_quality_controls.md#tui-scaled-jacobian) filter.
