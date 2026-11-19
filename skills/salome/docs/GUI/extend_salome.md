<!-- source: https://docs.salome-platform.org/latest/gui/GUI/extend_salome.html -->

# Add/remove modules dynamically

“SALOME on demand” feature provides a possibility to dynamically add or remove
SALOME modules directly from GUI.

## Description file

**“SALOME on demand”** feature introduces notion of a module description file.
This is the file in JSON format that has .salomex extension. The description
file provides some parameters of the module; two parameters are mandatory:
name of the module and path to its root directory.

Example:

```json
{
  "name": "PYHELLO",
  "root": "/home/user/salome/modules/PYHELLO"
}
```

Note

In the description file, the name parameter is an **internal** name of the module,
in contrast to its **title** which is described in SalomeApp.xml or LightApp.xml
resource file.

Note

One .salomex file may describe one SALOME module only.

## Modules toolbar

The *Modules* toolbar provides two additional buttons, which allow adding or removing
modules directly from GUI.

![Modules toolbar](https://docs.salome-platform.org/latest/gui/GUI/_images/modules_toolbar.png)

### Adding modules

Pressing the first button [![add](https://docs.salome-platform.org/latest/gui/GUI/_images/modules_add.png)](https://docs.salome-platform.org/latest/gui/GUI/_images/modules_add.png) shows a standard *Open File* dialog that allows
selecting one or more .salomex files. Each module correctly configured in the
corresponding .salomex file is then added to the SALOME session and appears in the
*Modules* toolbar. As soon as it is done, the user may work with the module in the same
way as with any other module: all features are available after activating module from
*Modules* toolbar.

The modules added in this way become *persistent*. This means that after restarting
SALOME these modules are available in the *Modules* toolbar.

### Removing modules

Pressing a small arrow near the second button [![remove](https://docs.salome-platform.org/latest/gui/GUI/_images/modules_remove.png)](https://docs.salome-platform.org/latest/gui/GUI/_images/modules_remove.png) shows a drop-down menu with
the list of manually added modules, where the user may select a module to remove. As soon
as user selects a module to remove, a message box is shown asking the user if it is
necessary also to remove a directory, containing the module, from disk. If user
confirms removal of the directory, it will be necessary to save the study, in order to
avoid possible data loss.

Note

The module libraries are not removed from RAM until exit from the current
SALOME session, so some its functionality may be still accessible, for example,
via Python API. However, using module functionality may have unpredicted
behavior.
