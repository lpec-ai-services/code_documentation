<!-- source: https://docs.salome-platform.org/latest/gui/YACS/gui.html -->

# Using YACS with the graphical user interface (GUI)

## YACS GUI description

![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/yacs_gui_description_0.png)

**Main Window**

The YACS GUI document contains several 2D and tree views, one of each per run of a schema. There are different view modes of the schema.
The SALOME Object browser is only used to publish the run of the schema as a whole, and under the run,
the outputs of the run that are published for the use of other SALOME modules. During the schema design (edition),
a dedicated edition tree view of the YACS data structure is used for schema building.
Modifications are displayed on the 2D view.

Several executions (run) of the same schema can occur at the same time. Dedicated tree in run mode and 2D views are used for each run.
The run tree view is used to control the execution (stop, breakpoints) and the 2D view reflects the detailed current state of execution.

The Python Console and Log Window often present in other SALOME modules are not used in YACS, so, they are not present by default.

For the quick access to basic operations the system of context-dependent popup menu is supported.
Popup menu is called by click of the right button of the mouse on the selected object.

Drag and drop operations are often used in edition, between tree items and/or 2D items, for associations (link creation, for instance).

The main window look & feel is presented schematically below.
Note that SALOME Object browser and Schema tree view are regrouped under tabs by default.

- [YACS GUI components](gui_components.md)
- [Main Menu](main_menu.md)
- [Toolbars](toolbars.md)

## Functionality list

Let’s describe the principal functionalities of objects creation, edition, visualization and execution of the YACS module.

- [General operations](operations.md)
  - [Activate YACS module](operations.md#activate-yacs-module)
  - [Import/Export a schema](operations.md#import-export-a-schema)
  - [Open/Save a study](operations.md#open-save-a-study)
  - [Set user preferences](operations.md#set-user-preferences)
  - [Select an object](operations.md#select-an-object)
  - [Activate context popup menu](operations.md#activate-context-popup-menu)
  - [Set active schema or run of a schema](operations.md#set-active-schema-or-run-of-a-schema)
- [Modification of a schema](modification.md)
  - [Create an object](modification.md#create-an-object)
  - [Edit an object](modification.md#edit-an-object)
  - [Delete an object](modification.md#delete-an-object)
- [Representation of a schema](representation.md)
  - [Change 2D representation of a schema](representation.md#change-2d-representation-of-a-schema)
  - [Auto-arrange schema nodes](representation.md#auto-arrange-schema-nodes)
  - [Rebuild links between nodes](representation.md#rebuild-links-between-nodes)
  - [Shrink/Expand nodes](representation.md#shrink-expand-nodes)
- [Execution of a schema](execution.md)
  - [Execute a schema](execution.md#execute-a-schema)
  - [Save/Restore execution state](execution.md#save-restore-execution-state)
  - [Schema shutdown](execution.md#schema-shutdown)
  - [Create new edition](execution.md#create-new-edition)

## YACS schema examples

In this section we consider several examples of YACS schemas.

- [Creation of a schema from scratch](scratch.md)
- [A standard dataflow](dataflow.md)
