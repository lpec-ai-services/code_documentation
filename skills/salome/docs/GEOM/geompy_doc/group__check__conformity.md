<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__check__conformity.html -->

# CheckConformity - Wrapper to find imperfections in the shape

## Detailed Description

This tool provides the user with a simple python API to analyze, available shape for Boolean Operations or not. Also tool provide advanced output to indicate imperfections in the input shape.   
Example:

```python
import GEOM
from salome.geom import geomBuilder
from salome.geom.CheckConformity import CheckConformity

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geompy.MakeVertex(-30, -70, 0)
Vertex_2 = geompy.MakeVertex(-30, 50, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_1)
Vertex_3 = geompy.MakeVertex(0, -50, 0)
Vertex_4 = geompy.MakeVertex(-40, -10, 0)
Vertex_5 = geompy.MakeVertex(0, 40, 0)
Arc_1 = geompy.MakeArc(Vertex_5, Vertex_4, Vertex_3)
Vertex_6 = geompy.MakeVertex(10, -50, 4)
Vertex_7 = geompy.MakeVertex(10, -50, 10)
Vertex_8 = geompy.MakeVertex(10, 40, 10)
Arc_1_vertex_3 = geompy.GetSubShape(Arc_1, [3])
Line_2 = geompy.MakeLineTwoPnt(Arc_1_vertex_3, Vertex_6)
Line_3 = geompy.MakeLineTwoPnt(Vertex_6, Vertex_7)
Line_4 = geompy.MakeLineTwoPnt(Vertex_7, Vertex_8)
Vertex_9 = geompy.MakeVertex(15, 40, 10)
Vertex_10 = geompy.MakeVertex(17, 0, 6)
Vertex_11 = geompy.MakeVertex(17, 0, 3)
Line_5 = geompy.MakeLineTwoPnt(Vertex_8, Vertex_9)
Line_6 = geompy.MakeLineTwoPnt(Vertex_9, Vertex_10)
Line_7 = geompy.MakeLineTwoPnt(Vertex_10, Vertex_11)
Arc_1_vertex_2 = geompy.GetSubShape(Arc_1, [2])
Line_8 = geompy.MakeLineTwoPnt(Vertex_11, Arc_1_vertex_2)
Wire_1 = geompy.MakeWire([Arc_1, Line_2, Line_3, Line_4, Line_5, Line_6, Line_7, Line_8], 1e-07)
Wire_2 = geompy.MakeWire([Line_1], 1e-07)
Compound_1 = geompy.MakeCompound([Wire_1, Wire_2])

# Create class CheckConformity for check shape
cc = CheckConformity(Compound_1, geompy)
valid = cc.isValid()
dist = cc.distantShapes()
small = cc.smallEdges()
interfer = cc.interferingSubshapes()
intersect = cc.selfIntersected2D()

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudyInFather( Arc_1, Arc_1_vertex_3, 'Arc_1:vertex_3' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudy( Vertex_9, 'Vertex_9' )
geompy.addToStudy( Vertex_10, 'Vertex_10' )
geompy.addToStudy( Vertex_11, 'Vertex_11' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Line_6, 'Line_6' )
geompy.addToStudy( Line_7, 'Line_7' )
geompy.addToStudyInFather( Arc_1, Arc_1_vertex_2, 'Arc_1:vertex_2' )
geompy.addToStudy( Line_8, 'Line_8' )
geompy.addToStudy( Wire_1, 'Wire_1' )
geompy.addToStudy( Wire_2, 'Wire_2' )
geompy.addToStudy( Compound_1, 'Compound_1' )

salome.sg.updateObjBrowser()
```

Additional examples can be found as unit tests in the source code.
