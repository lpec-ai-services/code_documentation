<!-- source: introduction_to_gui.rst -->

# Introduction to GUI

**SALOME GUI** is based on SUIT (Salome User Interface Toolkit) that proposes very flexible, powerful and safe mechanisms of interaction with SALOME tool components (both CORBA and standalone), resource management, viewers and selection handling, exception and signals processing.

All Graphical User Interfaces of standard modules have plug-in structure, i.e. each module is placed in a dynamic library which is loaded on demand. So, all modules add their own menu items, buttons in toolbar, windows etc.

**GUI** (Graphical User Interface) provides a common shell for all components, which can be integrated into the SALOME platform and some basic GUI functionalities, common for all modules.

- **File** menu corresponds to `study_management_page` functionalities (creation, saving, loading, connecting, disconnecting, editing studies, etc.)

- **Edit** menu gives access to \*\* Copy/Paste\*\* allowing to paste the objects from one study into the other. The availability of this functionality depends on the module and the nature of an operation or an object.

- **View** and **Window** menus provide functionalities of `salome_desktop_page`. Basically, they allow to show/hide toolbars, activate and manage study windows, change the appearance of Salome, etc. Among key parts of study window are:

  > - Viewer window, used for visualization of objects,
  > - `using_object_browser_page`, used for management of objects created or imported into the SALOME application, also providing search possibilities with the `using_find_tool_page`, and
  > - `using_notebook` - allows to predefine study variables.
  > - `python_interpreter_page`, used for direct input of python commands and dumping studies into Python scripts.

- **Tools** menu gives access to: `using_catalog_generator_page`, `using_registry_tool_page` and `using_pluginsmanager`

- **Help** menu gives access to the help on Salome modules. The appropriate help page can also be called from any operation dialog via **Help** button.

Help for the GUI module provides information about standard `viewers_page`.

General application preferences are described in the `setting_preferences_page` section of SALOME GUI Help.

`using_input_widgets_page` sub-section covers specific aspects of behavior of certain kinds of SALOME GUI input fields.

- `study_management_chapter.rst` (`study_management_chapter.rst.md`)
- `salome_desktop.rst` (`salome_desktop.rst.md`)
- `using_object_browser.rst` (`using_object_browser.rst.md`)
- `using_find_tool.rst` (`using_find_tool.rst.md`)
- `using_notebook.rst` (`using_notebook.rst.md`)
- `using_catalog_generator.rst` (`using_catalog_generator.rst.md`)
- `working_with_python_scripts.rst` (`working_with_python_scripts.rst.md`)
- `working_with_python_console.rst` (`working_with_python_console.rst.md`)
- `using_registry_tool.rst` (`using_registry_tool.rst.md`)
- `viewers_chapter.rst` (`viewers_chapter.rst.md`)
- `setting_preferences.rst` (`setting_preferences.rst.md`)
- `using_input_widgets.rst` (`using_input_widgets.rst.md`)
