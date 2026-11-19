<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/reduce_study_page.html -->

# Reduce Study

It can be sometimes necessary to keep in the study only the objects that present the final result(s) of the design operations and to delete all other objects, which do not contribute to these results.

This is especially useful when the model is designed using the GUI and it is necessary to generate a simplified "clean" Python dump without "useless" objects at the end of the model construction.

This feature can be activated by selecting the desirable object(s) in Object Browser or OCC Viewer and calling "Reduce study" context item.

![reduce_study_dialog.png](https://docs.salome-platform.org/latest/gui/GEOM/reduce_study_dialog.png)

- **Objects to be kept** - objects that will be kept in the study after applying reduce study operation. The objects selected by the user are highlighted in bold font.
- **Objects to be removed** - objects that will be deleted.

  Note
  :   It is possible to show/hide object(s) in the current Viewer using "eye" icon next to each tree item. ALL objects in the tree can be shown/hidden by clicking the "eye" icon in the head of the tree view.
- **Intermediate objects** group box allows choosing what should be done with the objects that are used to produce the selected object(s):
- **Sub-objects** group box allows choosing the same operations for sub-objects of the selected object(s).

  - Keep - object(s) will be kept in the study;
  - Unpublish - object(s) will be unpublished (hidden) from the study;
  - Remove - object(s) will be removed from the study.

    Note
    :   Since use of this option can cause a broken Dump Python script, the warning message is shown confirm/reject removing intermediate objects.
- **Remove empty folders** - if this option is checked, all folders, which will become empty after removing unused objects from the study, will be also removed; otherwise, empty folders will be kept.
- **Soft removal** - if this option is checked, the operation will unpublish the redundant objects from the study instead of deleting them.   
  So, soft removal keeps all data in the study to give the user a chance to revert this operation using [Publish Objects](arranging_study_objects_page.md#publish_hidden_objects) dialog box.
