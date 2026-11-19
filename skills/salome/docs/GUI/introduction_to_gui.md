<!-- source: https://docs.salome-platform.org/latest/gui/GUI/introduction_to_gui.html -->

# Introduction to GUI

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/view2.png)

**SALOME GUI** is based on SUIT (Salome User Interface
Toolkit) that proposes very flexible, powerful and safe mechanisms of
interaction with SALOME tool components (both CORBA and standalone),
resource management, viewers and selection handling,
exception and signals processing.

All Graphical User Interfaces of standard modules have plug-in
structure, i.e. each module is placed in a dynamic library which is
loaded on demand. So, all modules add their own menu items, buttons
in toolbar, windows etc.

**GUI** (Graphical User Interface) provides a common shell for all
components, which can be integrated into the SALOME platform and some
basic GUI functionalities, common for all modules.

![figure](https://docs.salome-platform.org/latest/gui/GUI/_images/mainmenu.png)

- **File** menu corresponds to [Study management](study_management_chapter.md#study-management-page) functionalities (creation, saving, loading, connecting, disconnecting, editing studies, etc.)
- **Edit** menu gives access to ** Copy/Paste** allowing to paste the objects from one study into the other. The availability of this functionality depends on the module and the nature of an operation or an object.
- **View** and **Window** menus provide functionalities of [SALOME desktop](salome_desktop.md#salome-desktop-page). Basically, they allow to show/hide toolbars, activate and manage study windows, change the appearance of Salome, etc. Among key parts of study window are:

  > - Viewer window, used for visualization of objects,
  > - [Using Object Browser](using_object_browser.md#using-object-browser-page), used for management of objects created or imported into the SALOME application, also providing search possibilities with the [Using Find Tool](using_find_tool.md#using-find-tool-page), and
  > - [Using NoteBook](using_notebook.md#using-notebook) - allows to predefine study variables.
  > - [Python Interpreter](working_with_python_scripts.md#python-interpreter-page), used for direct input of python commands and dumping studies into Python scripts.
- **Tools** menu gives access to: [Using Catalog Generator](using_catalog_generator.md#using-catalog-generator-page), [Using Registry tool](using_registry_tool.md#using-registry-tool-page) and [Extend SALOME gui functions using python plugins](using_pluginsmanager.md#using-pluginsmanager)
- **Help** menu gives access to the help on Salome modules. The appropriate help page can also be called from any operation dialog via **Help** button.

Help for the GUI module provides information about standard
[Viewers](viewers_chapter.md#viewers-page).

General application preferences are described in the [Setting Preferences](setting_preferences.md#setting-preferences-page)
section of SALOME GUI Help.

[Using input widgets](using_input_widgets.md#using-input-widgets-page) sub-section
covers specific aspects of behavior of certain kinds of SALOME GUI
input fields.

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
- [Using input widgets](using_input_widgets.md)
  - [Spin boxes](using_input_widgets.md#spin-boxes)
  - [Spin boxes and SALOME Notebook](using_input_widgets.md#spin-boxes-and-salome-notebook)
