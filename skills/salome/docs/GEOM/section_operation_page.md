<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/section_operation_page.html -->

# Intersection

**Intersection** operation creates a vertex, an edge, a wire or a compound of them representing the intersection of two shapes.

To produce it, select in the main menu **Operations - > Boolean - > Intersection**

![neo-section.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-section.png)

Intersection dialog

In this dialog:

- Input or accept the default **Name** of the resulting shape.
- Click the arrow button and select in the Object Browser or in the Viewer the intersecting **Objects**.
- Activate the corresponding check-box if you wish to  **Detect Self-intersections**. If a self-intersection detected the operation fails.
- Activate the corresponding check-box if you wish to use a  **fuzzy parameter** .   
  If activated, you can define the fuzzy tolerance in the  **fuzzy parameter**  input box.
- Activate [Advanced options](restore_presentation_parameters_page.md) if required.
- Press "Apply" or "Apply & Close" button to get the result (VERTEX, EDGE, WIRE or COMPOUND).

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

This operation can be performed using a **TUI Command:**

*geompy.MakeSection(s1, s2, checkSelfInte, name, fuzzyParam)*

**Arguments:** 2 shapes + an optional flag for self-intersection check + an optional name + an optional fuzzy parameter.

**Example:**

![fusesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/fusesn1.png)

The initial shapes

![sectionsn.png](https://docs.salome-platform.org/latest/gui/GEOM/sectionsn.png)

The resulting object

Our **TUI Scripts** provide you with useful examples of the use of [Boolean Operations](tui_boolean_operations_page.md#tui_section).

**More details**

Please refer to [this document](https://docs.salome-platform.org/latest/gui/GEOM/SALOME_BOA_PA.pdf) for a detailed description of Boolean operations. It provides a general review of the Partition and Boolean operations algorithms, describes the usage methodology and highlights major limitations of these operations.
