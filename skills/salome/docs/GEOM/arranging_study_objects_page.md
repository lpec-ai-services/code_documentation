<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/arranging_study_objects_page.html -->

# Viewing objects in the Object Browser

## Context Menu

Newly created or imported geometrical objects are listed in the Object Browser. The following commands appear in the Object Browser context menu under certain conditions:

![ob_popup_menu.png](https://docs.salome-platform.org/latest/gui/GEOM/ob_popup_menu.png)

- [Create Group](work_with_groups_page.md) - allows creating groups of geometrical objects.
- **Conceal child items** / **Disclose child items** - hides / shows child sub-objects in the Object Browser, if the selected geometric object has child objects. When some child objects are hidden, the name of the parent object is highlighted with bold font.
- **Show Only Children** - erases from the current viewer all objects and then displays only the children of the selected object(s).
- **Unpublish** - hides the selected geometric object from the Object Browser and erases it from all viewers. To publish unpublished geometric objects select in the context menu of the **Geometry** root object **Publish...** item. The following dialog box will appear

  ![publish_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/publish_dlg.png)

  Switch the check-box near the appropriate object and click **Publish** or **Publish And Close** button.

  "Eye" icons in this dialog box allow previewing unpublished objects in the viewer. By default all unpublished objects are sorted by name in ascending order. It is possible to change the order (ascending / descending) by clicking the corresponding title bar of the objects list.
- [Show dependency tree](dependency_tree_page.md) - shows the dependency tree with parents and children of the selected object in a new 2D View Window.
- [Reduce study](reduce_study_page.md) - allows reducing the study by removing objects from it.

## Folders

In the Object Browser it is possible to classify geometrical objects into folders.

To create a folder select  **Create folder** item in the context menu of the root **Geometry** Object Browser item or in another folder.

The objects can be added into folders by drag and drop

Note
:   Only two categories of objects can be moved into folder:

    - geometrical model(s) under root "Geometry" item or under any folder;
    - another folder.

If a geometrical object has more than one child sub-object, it is possible to sort them in ascending order by selecting **Sort children** context menu item of the parent object.

Our **TUI Scripts** provide you with useful examples of [Arranging objects in study](tui_arranging_study_objects_page.md#tui_arranging_study_objects).

## Information Window

At the bottom of the Object Browser, there is **Information** window providing some information on a selected geometric object:

![creation_op_info.png](https://docs.salome-platform.org/latest/gui/GEOM/creation_op_info.png)

Information window

- **Creation operation** shows a name of the operation used to create the selected object.
- The table below lists **Parameters** used to create the selected object and their **Values**.
