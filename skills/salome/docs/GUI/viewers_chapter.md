<!-- source: https://docs.salome-platform.org/latest/gui/GUI/viewers_chapter.html -->

# Viewers

SALOME GUI module includes several 2D and 3D viewers, that are used for
different purposes within the platform:

- [OCC 3D Viewer](occ_3d_viewer.md#occ-3d-viewer-page) has been developed on the basis of Open CASCADE Technology (<http://www.opencascade.org>). This is the default viewer for SALOME Geometry module, it provides good representation of construction and transformation of geometrical objects.
- [VTK 3D Viewer](vtk_3d_viewer.md#vtk-3d-viewer-page) has been developed basing on Kitware Visualization ToolKit library (<http://www.vtk.org>). This is the default viewer for SALOME Mesh module, where it is used for visualization of meshes. OCC and VTK 3d viewers share some [Functionality common for OCC and VTK viewers](common_functionality.md#common-functionality-page).
- [Plot 2D viewer](plot2d_viewer.md#plot2d-viewer-page) has been developed basing on the open-source Qwt library (<http://qwt.sourceforge.net>). It can be used, for example, for the representation of 2D plots and graphs.
- [GL 2D Viewer](gl_2d_viewer.md#gl-2d-viewer-page) is a general purpose OpenGL-based viewer, which can be used for visualization of 2D scenes. This type of viewer is not currently used in SALOME platform directly, but can be used in custom modules for 2D visualization purposes.
- [QxScene 2D Viewer](qxscene_2d_viewer.md#qxscene-2d-viewer-page) has been developed on the basis of Qt QGraphicsView scene. This viewer is used in SALOME YACS module for visualization of computation schemes.
- [Python viewer](python_viewer.md#python-viewer-page) is an editor for Python scripts.

- [OCC 3D Viewer](occ_3d_viewer.md)
  - [Operations](occ_3d_viewer.md#operations)
  - [Clipping Planes](occ_3d_viewer.md#clipping-planes)
  - [Environment texture](occ_3d_viewer.md#environment-texture)
- [VTK 3D Viewer](vtk_3d_viewer.md)
  - [Operations](vtk_3d_viewer.md#operations)
- [Functionality common for OCC and VTK viewers](common_functionality.md)
  - [Background](common_functionality.md#background)
  - [Selection](common_functionality.md#selection)
  - [Navigation modes](common_functionality.md#navigation-modes)
- [Plot 2D viewer](plot2d_viewer.md)
  - [Settings](plot2d_viewer.md#settings)
  - [Analytical curves](plot2d_viewer.md#analytical-curves)
- [GL 2D Viewer](gl_2d_viewer.md)
  - [Operations](gl_2d_viewer.md#operations)
  - [Background](gl_2d_viewer.md#background)
- [QxScene 2D Viewer](qxscene_2d_viewer.md)
  - [Operations](qxscene_2d_viewer.md#operations)
- [Python viewer](python_viewer.md)
  - [Custom Python preferences](python_viewer.md#custom-python-preferences)
