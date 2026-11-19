<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/cut_operation_page.html -->

# Cut

**Cut** operation cuts a shape with a list of other shapes.

To produce it, select in the main menu **Operations - > Boolean - > Cut**

![bool3.png](https://docs.salome-platform.org/latest/gui/GEOM/bool3.png)

Cut dialog

In this dialog:

- Input or accept the default **Name** of the resulting shape.
- Click the arrow button and select in the Object Browser or in the Viewer the **Main Object**, which will be cut by tool objects.
- Select the **Tool objects**, which will cut the main object.
- Activate the corresponding check-box if you wish to  **Detect Self-intersections** .
- Activate the corresponding check-box if you wish to use a  **fuzzy parameter** .   
  If activated, you can define the fuzzy tolerance in the  **fuzzy parameter**  input box.
- Activate [Advanced options](restore_presentation_parameters_page.md) if required.
- Press "Apply" or "Apply & Close" button to get the result (GEOM_Object).

Note
:   This algorithm does not find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections use [Detect Self-intersection tool](check_self_intersections_page.md).

This operation can be performed using a **TUI Command:**

*geompy.MakeCutList(theMainShape, theShapesList, checkSelfInte, name, fuzzyParam)*

**Arguments:** a main shape + a list of other shapes + an optional flag for self-intersection check + an optional name + an optional fuzzy parameter.

There is also a special **TUI Command:** for the Cut operation on two shapes (object and tool) :

*geompy.MakeCut(s1, s2, checkSelfInte, name, fuzzyParam)*

**Arguments:** the object + the tool + an optional flag for self-intersection check + an optional name + an optional fuzzy parameter.

**Example:**

![fusesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/fusesn1.png)

The initial shapes

![cutsn.png](https://docs.salome-platform.org/latest/gui/GEOM/cutsn.png)

The resulting object

Our **TUI Scripts** provide you with useful examples of the use of [Boolean Operations](tui_boolean_operations_page.md#tui_cut).

**More details**

Please refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf) for a detailed description of Boolean operations. It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.
