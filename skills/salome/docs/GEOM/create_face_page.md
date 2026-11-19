<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_face_page.html -->

# Face

To create a **Face** in the **Main Menu** select **New Entity - > Build - > Face**

There are three algorithms to create a **Face**. In all cases the **Result** of the operation will be a GEOM_Object (FACE).

Firstly, to create a **Face** you need to select input shape(s). The list of input shapes can include shapes of any type except vertices; if the shapes are neither wires nor edges, the algorithm extracts all edges from the input shapes and works on the obtained edges.   
The edges and wires do not necessarily have to be closed, the algorithm automatically builds a wire of maximum length from all given edges and wires. If several closed wires are detected the algorithm tries to create a face with holes. It is possible only if there is only one wire that can be interpreted as an outer one; other wires can be considered as inner ones.   
Check **Try to create a planar face** to create a planar face or nothing if it is impossible.

Note
:   Please note, that the resulting face can have a huge tolerance, if the initial wire has a big deviation from the plane. If the final tolerance exceeds 1e-06, a warning will be shown, but the face will be created and published in the study in a normal way. Using such faces can lead to failures or unpredictable results in most operations.

The **Result** will be a **GEOM_Object**. It can be either a single face or, in specific cases, a compound of faces.

**TUI Command:** *geompy.MakeFaceWires([list of Shapes], isPlanarWanted)*   
**Arguments:** Name + 1 wire.

![neo-obj4.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj4.png)

Create face by input shape(s)

Secondly, it is possible to create a face based on another face's surface and bounded by a wire.

The **Result** will be a **GEOM_Object** (face).

**TUI Command:** *geompy.MakeFaceFromSurface(theFace, theWire)*   
**Arguments:** Name + 1 face + 1 wire.

![neo-obj4_2.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj4_2.png)

Create face by another face's surface

Thirdly, it is possible to create a **Face** by specifying a set of edges forming a closed wire and constraints:

- Specify an input wire by selecting it in the object browser or in the viewer. The input wire will be exploded on edges which will be shown in the **Constraints** list box.
- Specify constraints by associating faces with the edges.

Note
:   Please note, that the constraint face must be connected to a reference edge.

The **Result** will be a **GEOM_Object** (face).

**TUI Command:** *geompy.MakeFaceWithConstraints([List of constraints])*   
**Arguments:** Name + List of input edges and constraint faces. If a constraint face is missing for some edge, this means that there is no constraint associated to this edge.

Note
:   Set of edges should form a closed wire.

![neo-obj4_3.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj4_3.png)

Create face by a wire and its constraints

**Example:**

![facesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/facesn1.png)

![facesn2.png](https://docs.salome-platform.org/latest/gui/GEOM/facesn2.png)

![facesn3.png](https://docs.salome-platform.org/latest/gui/GEOM/facesn3.png)

Examples of faces

Our **TUI Scripts** provide you with useful examples of creation of [Advanced Geometric Objects](tui_topological_geom_objs_page.md#tui_creation_face).
