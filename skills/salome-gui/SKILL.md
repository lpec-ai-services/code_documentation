---
name: salome-gui
description: SALOME platform desktop and GUI module — user guide for the SALOME application: desktop, study management, object browser, Python console and scripts, notebook, preferences, viewers (OCC 3D, VTK 3D, Plot 2D, GL 2D, QxScene, Python viewer), find tool, plugins manager, catalog generator, registry tool, adding/removing modules, text user interface (salome.py, sg), and for module developers drag and drop and the use-case builder, plus the GUI architecture. Use for questions on using or extending the SALOME desktop; for meshes and fields use salome-medcoupling.
---

# SALOME GUI documentation

The SALOME GUI user guide from the SALOME repository (master branch) is in `docs/`, converted to Markdown, one file per page. It is the site docs.salome-platform.org/latest/main/gui.html. Paths are relative to this file's directory.

- `docs/INDEX.md` lists every page with its title and headings. **Start here.**
- `docs/architecture/`: the GUI architecture notes for developers (from the GUI's Doxygen pages).
- Screenshots are not included. Pages refer to them by name.
- `docs/_meta.json` records the source commit.

This is a usage guide, so the skill has no physics/methods split. Pages fall into three groups:

| Topic | Pages |
|---|---|
| **Getting around**: introduction, desktop, study management, object browser, find tool, preferences, colours and fonts, input widgets, help panel | `introduction.md`, `introduction_to_gui.md`, `salome_desktop.md`, `study_management_chapter.md`, `using_object_browser.md`, `using_find_tool.md`, `setting_preferences.md`, `select_color_and_font.md`, `using_input_widgets.md`, `using_help_panel.md` |
| **Python and automation**: Python console, running scripts, notebook (study parameters), text user interface (`salome.py`, `sg`) | `working_with_python_console.md`, `working_with_python_scripts.md`, `using_notebook.md`, `text_user_interface.md` |
| **Viewers**: OCC 3D, VTK 3D, common functions (selection, navigation modes), Plot 2D, GL 2D, QxScene, Python viewer | `viewers_chapter.md`, `occ_3d_viewer.md`, `vtk_3d_viewer.md`, `common_functionality.md`, `plot2d_viewer.md`, `gl_2d_viewer.md`, `qxscene_2d_viewer.md`, `python_viewer.md` |
| **Extending SALOME**: add/remove modules, plugins manager, catalog generator, registry tool; for module developers, drag and drop and the use-case builder | `extend_salome.md`, `using_pluginsmanager.md`, `using_catalog_generator.md`, `using_registry_tool.md`, `drag_and_drop.md`, `use_case_builder.md`, `howtos_and_best_practives.md`, `architecture/` |

## How to answer

Find the page in the table or `INDEX.md`, then describe menu paths and dialog fields exactly as the page names them. Don't invent menu entries. Cite the page.

## Related skills

**`salome-medcoupling`** covers meshes and fields (MED files, interpolation).
