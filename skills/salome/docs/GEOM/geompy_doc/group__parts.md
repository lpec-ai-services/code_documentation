<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__parts.html -->

# parts structelem - Structural elements package

## Detailed Description

This module defines the different structural element parts. It is used to build the geometric shapes of the structural elements. It should not be used directly in the general case. Structural elements should be created by the [salome.geom.structelem.StructuralElementManager](classstructelem_1_1StructuralElementManager.md).

## Function Documentation

### getParameterInDict()

```python
def parts.getParameterInDict(nameList, parametersDict, default = None)
```

This method finds the value of a parameter in the parameters dictionary.

The argument is a list because some parameters can have several different names.

### VisuPoutreGenerale()

```python
def parts.VisuPoutreGenerale(groupName, groupGeomObj, parameters, name = "POUTRE")
```

Alias for class [GeneralBeam](classparts_1_1GeneralBeam.md).

### VisuPoutreCercle()

```python
def parts.VisuPoutreCercle(groupName, groupGeomObj, parameters, name = "POUTRE")
```

Alias for class [CircularBeam](classparts_1_1CircularBeam.md).

### VisuPoutreRectangle()

```python
def parts.VisuPoutreRectangle(groupName, groupGeomObj, parameters, name = "POUTRE")
```

Alias for class [RectangularBeam](classparts_1_1RectangularBeam.md).

### VisuBarreGenerale()

```python
def parts.VisuBarreGenerale(groupName, groupGeomObj, parameters, name = "BARRE")
```

Alias for class [GeneralBeam](classparts_1_1GeneralBeam.md).

### VisuBarreRectangle()

```python
def parts.VisuBarreRectangle(groupName, groupGeomObj, parameters, name = "BARRE")
```

Alias for class [RectangularBeam](classparts_1_1RectangularBeam.md).

### VisuBarreCercle()

```python
def parts.VisuBarreCercle(groupName, groupGeomObj, parameters, name = "BARRE")
```

Alias for class [CircularBeam](classparts_1_1CircularBeam.md).

### VisuCable()

```python
def parts.VisuCable(groupName, groupGeomObj, parameters, name = "CABLE")
```

Alias for class [CircularBeam](classparts_1_1CircularBeam.md).

### VisuCoque()

```python
def parts.VisuCoque(groupName, groupGeomObj, parameters, name = "COQUE")
```

Alias for class [ThickShell](classparts_1_1ThickShell.md).

### VisuGrille()

```python
def parts.VisuGrille(groupName, groupGeomObj, parameters, name = "GRILLE")
```

Alias for class [Grid](classparts_1_1Grid.md).
