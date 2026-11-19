<!-- source: https://docs.salome-platform.org/latest/gui/GUI/introduction.html -->

# Introduction to Salome Platform

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/icon_about.png)

Welcome to SALOME Platform! Modern technological products (cars,
structures, electrical or electronic equipment) are getting more and
more complex every year and must meet increasingly severe requirements
in terms of quality and performance. For example, for structures and
their environment the demands to reduce risks and optimize costs are
extremely high. It requires particularly refined simulations
concerning structural behavior and robustness to ensure high
reliability.

The numeric modeling of a physical problem, the development of
solutions and their integration into the design process are often
handled in very specific environments. SALOME represents a generic
CAD-based application for digital simulation with “high reactivity to
market evolutions and customer expectations”.

SALOME is a free software that provides a generic platform for Pre and
Post-Processing for numerical simulation. It is based on an open and
flexible architecture made of reusable components available as free
software.

SALOME is a CAD/CAE integration platform. It provides reusable
components for:

1. 3D modeling (bottom-up construction, import, healing);
2. Visualization;
3. Computational schemas management;
4. Post-processing.

SALOME is tailored for integration of custom components:

1. CAD interfaces;
2. Mesh generators;
3. Finite Element solvers with specific pre-processors.

The SALOME platform is available in Open Source.

**Salome Platform:**

1. Supports interoperability between CAD modeling and computation software (CAD-CAE link)
2. Makes easier the integration of new components on heterogeneous systems for numerical computation
3. Sets the priority to multi-physics coupling between computation software
4. Provides a generic user interface, user-friendly and efficient, which helps to reduce the costs and delays of carrying out the studies
5. Reduces training time to the specific time for learning the software solution which has been based on this platform
6. All functionalities are accessible through the programmatic integrated Python console

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/image65.png)

**What can you do in SALOME? (Some of SALOME main functions)**

1. Define geometrical models (create/modify geometrical items), import and export them using the BREP, IGES and STEP formats;
2. Define meshing of these geometrical items, import and export them;
3. Handle physical properties and quantities attached to geometrical items, import and export them to a reusable format;
4. Perform computations using a solver (optionally provided): read input data, configure the solver, and write calculation results);
5. Visualize result fields in 3D, 2D and export images of their visualization to an appropriate format;
6. Manage study schemes: definition, save/restore;
7. Manage computation schemes: definition, execution.

This part of documentation on Salome also covers
[Introduction to GUI](introduction_to_gui.md#introduction-to-gui-page), common for all modules, such as study management, Salome viewers,
preferences, etc.

And finally, there is an additional chapter, which provides a short
guide about the [Using SALOME GUI python interface](text_user_interface.md#tui-page) to access SALOME GUI
functionalities from the Python code.

- [Introduction to GUI](introduction_to_gui.md)
  - [Study management](study_management_chapter.md)
  - [SALOME desktop](salome_desktop.md)
  - [Using Object Browser](using_object_browser.md)
    - [Sorting](using_object_browser.md#sorting)
  - [Using Find Tool](using_find_tool.md)
  - [Using NoteBook](using_notebook.md)
  - [Using Catalog Generator](using_catalog_generator.md)
  - [Python Interpreter](working_with_python_scripts.md)
  - [Python Console](working_with_python_console.md)
    - [Asynchronous mode](working_with_python_console.md#asynchronous-mode)
    - [Tracing](working_with_python_console.md#tracing)
  - [Using Registry tool](using_registry_tool.md)
  - [Viewers](viewers_chapter.md)
    - [OCC 3D Viewer](occ_3d_viewer.md)
      - [Operations](occ_3d_viewer.md#operations)
      - [Clipping Planes](occ_3d_viewer.md#clipping-planes)
        - [Ray tracing](occ_3d_viewer.md#ray-tracing)
      - [Environment texture](occ_3d_viewer.md#environment-texture)
        - [Light source](occ_3d_viewer.md#light-source)
    - [VTK 3D Viewer](vtk_3d_viewer.md)
      - [Operations](vtk_3d_viewer.md#operations)
    - [Functionality common for OCC and VTK viewers](common_functionality.md)
      - [Background](common_functionality.md#background)
      - [Selection](common_functionality.md#selection)
        - [Rectangle selection](common_functionality.md#rectangle-selection)
        - [Polyline selection](common_functionality.md#polyline-selection)
        - [Circle selection](common_functionality.md#circle-selection)
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
  - [Setting Preferences](setting_preferences.md)
    - [General Preferences](setting_preferences.md#general-preferences)
    - [3D Viewer Preferences](setting_preferences.md#d-viewer-preferences)
    - [OCC 3D Viewer Preferences](setting_preferences.md#occ-3d-viewer-preferences)
    - [VTK 3D Viewer Preferences](setting_preferences.md#vtk-3d-viewer-preferences)
    - [Plot 2D Viewer Preferences](setting_preferences.md#plot-2d-viewer-preferences)
    - [Python Viewer Preferences](setting_preferences.md#python-viewer-preferences)
    - [Directories Preferences](setting_preferences.md#directories-preferences)
    - [Object Browser Preferences](setting_preferences.md#object-browser-preferences)
    - [Shortcut Preferences](setting_preferences.md#shortcut-preferences)
      - [Select Color and Font](select_color_and_font.md)
        - [Select Color Dialog](select_color_and_font.md#select-color-dialog)
          - [Select color](select_color_and_font.md#select-color)
          - [Select font](select_color_and_font.md#select-font)
  - [Using input widgets](using_input_widgets.md)
    - [Spin boxes](using_input_widgets.md#spin-boxes)
    - [Spin boxes and SALOME Notebook](using_input_widgets.md#spin-boxes-and-salome-notebook)
- [Using SALOME GUI python interface](text_user_interface.md)
