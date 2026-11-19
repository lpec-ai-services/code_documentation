<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/shellFeature.html -->

# Shell

Shell feature creates a shell using faces already existing in other objects.

To create a shell in the active part:

1. select in the Main Menu *Build - > Shell* item or
2. click ![feature_shell.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_shell.png) **Shell** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Shell.png)

Create a shell

Select one or several faces in the viewer. Additionally, it is allowed to select a whole sketch result from the object browser. In this case, the result shell will contain faces corresponding to all smallest closed contours of the sketch.

**Apply** button creates a shell.

**Cancel** button cancels the operation.

**TUI Command**:

model.addShell(*Part_doc*, *Objects*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a shell created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateShell.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Shell](TUI_shellFeature.md#tui-create-shell) operation.
