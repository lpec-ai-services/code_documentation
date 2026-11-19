<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/common_operation_page.html -->

# Common

**Common** operation cuts the common part of a list of shapes and transforms it into an independent geometrical object.

To produce it, select in the main menu **Operations - > Boolean - > Common**.

![bool2.png](https://docs.salome-platform.org/latest/gui/GEOM/bool2.png)

Common dialog

In this dialog:

- Input or accept the default **Name** of the resulting shape.
- Click the arrow button and select in the Object Browser or in the Viewer the **Objects** the common part which of should be found.
- Activate the corresponding check-box if you wish to  **Detect Self-intersections**
- Activate the corresponding check-box if you wish to use a  **fuzzy parameter** .   
  If activated, you can define the fuzzy tolerance in the  **fuzzy parameter**  input box.
- Activate [Advanced options](restore_presentation_parameters_page.md) if required.
- Press "Apply" or "Apply & Close" button to get the result (GEOM_Object).

Note
:   This algorithm does not find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections use [Detect Self-intersection tool](check_self_intersections_page.md).

This operation can be performed using a **TUI Command:**

*geompy.MakeCommonList(theShapesList, checkSelfInte, name, fuzzyParam)*

**Arguments:** a list of shapes + an optional flag for self-intersection check + an optional name + an optional fuzzy parameter.

There is also a special **TUI Command** for the Common operation on two shapes :

*geompy.MakeCommon(s1, s2, checkSelfInte, name, fuzzyParam)*

**Arguments:** 2 shapes + an optional flag for self-intersection check + an optional name + an optional fuzzy parameter.

**Example:**

![fusesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/fusesn1.png)

The initial shapes

![commonsn.png](https://docs.salome-platform.org/latest/gui/GEOM/commonsn.png)

The resulting object

Our **TUI Scripts** provide you with useful examples of the use of [Boolean Operations](tui_boolean_operations_page.md#tui_common).

**More details**

Please, refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf) for a detailed description of Boolean operations. It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.
