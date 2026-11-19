<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geom_field_page.html -->

# Working with Fields

A field object allows assigning some values to geometrical entities. These values can be later transferred to mesh entities generated on the geometrical entities during export to MED file in Mesh module. Geometrical fields can be stored in/restored from [XAO format](import_export_geom_obj_page.md#io_xao) files.

A field object assigns values to either

- all vertices of a GEOM_Object or
- all edges of a GEOM_Object or
- all faces of a GEOM_Object or
- all solids of a GEOM_Object or
- the whole GEOM_Object.

Values can be of one of the following types:

- boolean,
- integer,
- double,
- string.

Note
:   Only integer and double values can be exported into the MED file.

The field can hold several named values (components) per a geometrical entity.

The field can include several sets of data called *steps*, each dedicated to a certain time moment. A step is described by

- an integer ID,
- a time stamp number,
- values.

To create a field, in the **Main Menu** select **New Entity -> Field -> Create Field**.

![create_field_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/create_field_dlg.png)

Create Field dialog

In this dialog you can:

- Set **Field Name** with which a field will appear in the Object Browser.
- Select a **Shape** to which the field values will be assigned.
- Select a **Type** of field values.
- Select a type of **Sub-shapes** to assign values to.
- Specify **Nb. Components** per a shape/sub-shape.
- Specify names of components and the values in a table of **Values**. (To change a component name, double-click a column header).
- Push **Add Step** button to add a new time step. (Specify a step ID in **Step** field before pushing this button).
- Adjust a time stamp number in **Stamp** field.
- Push **Previous Step** and **Next Step** buttons to navigate through added steps or use a drop-down list to the right of the **Step** field to select a step by its ID.
- Push **Remove Step** to delete a current step.
- Push **Apply** or **Apply and Close** button to commit creation of the field.

Later you can modify the values and the time stamp number of a created field and to add/remove steps to it. To do it, choose **Edit Field** in a contextual menu of a field or step in the Object Browser.

**Python API** for field manipulations includes the following commands:

```python

field          = geompy.CreateField(shape, name, type, dimension, componentNames)
geompy.RemoveField(field)
shape          = field.getShape()
name           = field.getName()
field.setName(name)
type           = field.getType()
dim            = field.getDimension()
componentNames = field.getComponents()
nbFileds       = geompy.CountFields(shape)
fields         = geompy.GetFields(shape)
field          = geompy.GetField(shape, name)
```
```python
field.addStep(stepID, stamp, values)
field.removeStep(stepID)
nbSteps        = field.countSteps()
stepIDs        = field.getSteps()
stamp          = field.getStamp(stepID)
field.setStamp(stepID, stamp)
values         = field.getValues(stepID)
field.setValues(step, values)
```

Our **TUI Scripts** provide you with examples of [GEOM fields creation](tui_geom_field_page.md).
