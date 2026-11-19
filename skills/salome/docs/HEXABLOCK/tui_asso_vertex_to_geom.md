<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_asso_vertex_to_geom.html -->

# TUI: Definition of point of the geometry

Firt you need to define the Geom point you want to associate your vertex to.

Define a point by its coordinates:

```python
geom_object_vertex = geompy.MakeVertex(X, Y, Z)
```

Define a point by reference:

```python
geom_object_vertex = geompy.MakeVertexWithRef(Reference, X,Y,Z)
```

Define a point by an Edge and a Parameter:

```python
geom_object_vertex = geompy.MakeVertexOnCurve(Edge,Parameter)
```

Define a point by an Edge and a Length:

```python
geom_object_vertex = geompy.MakeVertexOnCurveByLength(Edge,Length,StartPoint=None)
```

Define a point by an Edge and Coordinates:

```python
geom_object_vertex = geompy.MakeVertexOnCurveByCoord(Edge,X,Y,Z)
```

Define a point by intersection of two Lines or Wires (or a Wire and a Line):

```python
geom_object_vertex = geompy.MakePointOnLinesIntersection(myLine1,myWire1)
```

Define a point by its position (U-V parameters) on a face:

```python
geom_object_vertex = geompy.MakeVertexOnSurface(myFace,myUParameter,myVParameter)
```

Define a point by its position (Coordinates) on a face:

```python
geom_object_vertex = geompy.MakeVertexOnSurface(myFace,X,Y,Z)
```

GUI: [Vertex Association](gui_asso_quad_to_geom.md#guiassovertex)
