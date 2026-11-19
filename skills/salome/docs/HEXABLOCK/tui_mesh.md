<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_mesh.html -->

# Generate the mesh

Use the SMESH component of SALOME:

```python
import smesh
m = hexablock.mesh(name, doc)
```

Export to a MED file:

```python
m.ExportMED("/tmp/mesh.med")
```

Get some information about the mesh:

```python
print "Number of hexahedra: ", m.NbHexas()
print "Number of quadrangles: ", m.NbQuadrangles()
print "Number of segments: ", m.NbEdges()
print "Number of nodes: ", m.NbNodes()
```

GUI command: [Generate the mesh](gui_mesh.md#guimesh)
