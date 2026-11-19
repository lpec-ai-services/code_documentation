<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_compound_page.html -->

# Compound

To create a **Compound** in the **Main Menu** select **New Entity - > Build - > Compound**.

You can create a compound from a list of shapes.   
The **Result** will be a **GEOM_Object** (COMPOUND).

**TUI Command:** *geompy.MakeCompound(ListOfShape)*   
**Arguments:** Name + List of shapes.   
**Advanced option:** [Set presentation parameters and sub-shapes from arguments](restore_presentation_parameters_page.md).

![neo-obj7.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj7.png)

**Example:**

![compoundsn.png](https://docs.salome-platform.org/latest/gui/GEOM/compoundsn.png)

Edges for creation of a compound

Our **TUI Scripts** provide you with useful examples of creation of [Advanced Geometric Objects](tui_topological_geom_objs_page.md#tui_creation_compound).

**More details:**

Perhaps you ask yourself : [What's the difference between partition, compounds and fuse operation ?](partition_explanation.md)
