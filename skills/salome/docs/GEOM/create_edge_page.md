<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_edge_page.html -->

# Edge

To create an **Edge**, in the **Main Menu** select **New Entity > Build > Edge**   
There are three ways to create an edge. In all cases the **Result** will be a **GEOM_Object** (EDGE).

Firstly, you can create a linear **Edge** by specifying two points (**Point1** and **Point2**), which are the first and the last vertices of the edge.

**TUI Command:** *geompy.MakeEdge(Vertex1, Vertex2)*  
**Arguments:** Name + 2 vertices (Vertex1 and Vertex2 are correspondingly the first and the last vertex of the edge).

![edge1.png](https://docs.salome-platform.org/latest/gui/GEOM/edge1.png)

Create edge by two points

Secondly, you can create an **Edge** by specifying a single wire.

In this mode the following use cases are possible:

- All edges that form the wire lie on the same geometrical curve (i.e. curve(edge1) == curve(edge2)).
- The edges that form the wire lie on analytical curves of the same type, for example, segments of line, arcs, etc. In this case, the algorithm checks geometrical coincidence of these curves using a certain tolerance. If the curves are coinciding in terms of the given tolerance, the resulting edge is built as if on a single curve.
- The edges that form the wire have the same tangency in the connection points. In this case the curves are interpolated by the single b-spline curve with sufficient precision. The resulting edge will be built on this curve.

The case when the edges that form the wire have different tangency in the connection points (sharp bend) is not processed.

**TUI Command:** *geompy.MakeEdgeWire(Wire, LinearTolerance, AngularTolerance)*  
**Arguments:** Name + 1 wire + Linear Tolerance + Angular Tolerance (tolerance values are used to check coincidence of the underlying curves).

![edge2.png](https://docs.salome-platform.org/latest/gui/GEOM/edge2.png)

Create edge from wire

Thirdly, it is possible to build an edge of required **Length** on any existing **Edge**.

**Start Point** parameter is optional:

- if used, it allows selecting any existing point - in such a case the start point of the new edge will be chosen as start or end point of the selected **Edge** whatever is closest to the selected **Start Point**
- if it is missed, the start point of the initial edge is used

**Length** can exceed the length of the initial edge length or be negative. In this case the existing edge is extrapolated along its curve (except for bezier and b-spline curves).

**TUI Command:** *geompy.MakeEdgeOnCurveByLength(Edge, Length, StartPoint = None)*  
**Arguments:** Name + 1 edge + Length + 1 Vertex

![edge3.png](https://docs.salome-platform.org/latest/gui/GEOM/edge3.png)

Create edge on curve

**Example:**

![edgesn.png](https://docs.salome-platform.org/latest/gui/GEOM/edgesn.png)

Edge

Our **TUI Scripts** provide you with useful examples of creation of [Advanced Geometric Objects](tui_topological_geom_objs_page.md#tui_creation_edge).
