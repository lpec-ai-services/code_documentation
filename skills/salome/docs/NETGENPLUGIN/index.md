<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/index.html -->

# Introduction to NETGENPLUGIN

**NETGENPLUGIN** plugin is destined for:

- Meshing 1D, 2D and 3D geometric entities.
  - Faces are split into triangular elements. Quad-dominant mesh is also possible.
  - Solids are split into tetrahedral elements. Pyramids are constructed as a transition from quadrangles to tetrahedra.
- Generating 3D meshes from 2D meshes, working without geometrical objects.
- Generating 2D meshes from 2D meshes, working without geometrical objects.

When working without geometrical objects, Negten requires that the input mesh to be a manifold shell.

To manage parameters of the NETGENPLUGIN use [NETGEN 2D and 3D hypotheses](netgen_2d_3d_hypo_page.md) and [Additional Hypotheses](additional_hypo_page.md).

Native Netgen mesher usually prints a lot of trace output to the terminal window. This output is redirected to some log file by the Plugin. It is possible to switch off this redirection by setting up KEEP_NETGEN_OUTPUT environment variable.

Also all NETGENPLUGIN functionalities are accessible via [NETGENPLUGIN Python interface](netgenplugin_python_interface_page.md).

![image1.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/image1.png)

Example of a triangular 2D mesh

![image2.gif](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/image2.gif)

Example of a tetrahedral 3D mesh
