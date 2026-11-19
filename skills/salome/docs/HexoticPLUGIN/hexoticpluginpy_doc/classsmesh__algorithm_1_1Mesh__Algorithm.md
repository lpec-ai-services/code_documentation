<!-- source: https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexoticpluginpy_doc/classsmesh__algorithm_1_1Mesh__Algorithm.html -->

# Mesh_Algorithm Class Reference

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self)
```

## Member Function Documentation

### FindHypothesis()

```python
def FindHypothesis(self, hypname, args, CompareMethod, smeshpyD)
```

### FindAlgorithm()

```python
def FindAlgorithm(self, algoname, smeshpyD)
```

### GetSubMesh()

```python
def GetSubMesh(self)
```

### GetAlgorithm()

```python
def GetAlgorithm(self)
```

### GetCompatibleHypothesis()

```python
def GetCompatibleHypothesis(self)
```

### GetName()

```python
def GetName(self)
```

### SetName()

```python
def SetName(self, name)
```

### GetId()

```python
def GetId(self)
```

### Create()

```python
def Create(self, mesh, geom, hypo, so = "libStdMeshersEngine.so")
```

### Assign()

```python
def Assign(self, algo, mesh, geom)
```

### CompareHyp()

```python
def CompareHyp(self, hyp, args)
```

### CompareEqualHyp()

```python
def CompareEqualHyp(self, hyp, args)
```

### Hypothesis()

```python
def Hypothesis(self, hyp, args = [], so = "libStdMeshersEngine.so", UseExisting = 0, CompareMethod = "", toAdd = True)
```

### MainShapeEntry()

```python
def MainShapeEntry(self)
```

### ViscousLayers()

```python
def ViscousLayers(self, thickness, numberOfLayers, stretchFactor, faces = [], isFacesToIgnore = True, extrMethod = StdMeshers.SURF_OFFSET_SMOOTH, groupName = "")
```

### ViscousLayers2D()

```python
def ViscousLayers2D(self, thickness, numberOfLayers, stretchFactor, edges = [], isEdgesToIgnore = True, groupName = "")
```

### ReversedEdgeIndices()

```python
def ReversedEdgeIndices(self, reverseList)
```

## Field Documentation

### mesh

```python
mesh
```

### geom

```python
geom
```

### subm

```python
subm
```

### algo

```python
algo
```
