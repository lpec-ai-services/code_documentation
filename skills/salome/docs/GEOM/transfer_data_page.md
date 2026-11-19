<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/transfer_data_page.html -->

# Transfer Data

This operation performs copying of non-topological data from one shape to another. The topology of the destination object will not change, only non-topological data will be transferred (if it is present in the source object). It is possible to transfer the following data with this operation:

- **Names**
- **Materials**

To use this operation, select in the Main Menu **Operations -> Transfer Data**. The following dialog box will appear.

![transfer_data1.png](https://docs.salome-platform.org/latest/gui/GEOM/transfer_data1.png)

Transfer Data Dialog

In this dialog:

- **Source Shape** is an object that is a source of non-topological data.
- **Destination Shape** is a data destination object.
- **Type of detection operation** allows choosing how to search sub-shapes of the **Source Shape** in the **Destination Shape**. The data are transferred from these corresponding sub-shapes. The following methods are possible:
  - **Get In Place** - the current implementation of Get In Place algorithm (default value).
  - **Get In Place (old)** - the old implementation of Get In Place algorithm.
  - **Get In Place By History** - Get In Place By History algorithm.

To copy the data click on **Apply** or **Apply and Close** button. It is possible to see how many names and materials are copied as well as the maximum number of names and materials available for copying. This information is provided in the following message box:

![transfer_data2.png](https://docs.salome-platform.org/latest/gui/GEOM/transfer_data2.png)

Transfer Data Information

**TUI Command:** *geompy.TransferData(ObjectFrom, ObjectTo, FindMethod),*   
where *ObjectFrom* is a data source object, *ObjectTo* is a destination object and *FindMethod* is a same shape detection method with default value *[GEOM.FSM_GetInPlace](../GEOM/geompy_doc/namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea8d5ebcfdf2f81affbc89309f798413dd)*.

Our **TUI Scripts** provide you with useful example of the use of [Transfer Data](tui_test_others_page.md#swig_TransferData) functionality.
