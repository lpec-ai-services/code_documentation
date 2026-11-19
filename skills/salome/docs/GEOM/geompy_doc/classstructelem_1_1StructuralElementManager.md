<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classstructelem_1_1StructuralElementManager.html -->

# StructuralElementManager Class Reference structelem - Structural elements package

This class manages the structural elements in the study.
[More...](classstructelem_1_1StructuralElementManager.md#details)

## Detailed Description

This class manages the structural elements in the study.

It is used to create a new structural element from a list of commands.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self)
```

## Member Function Documentation

### createElement()

```python
def createElement(self, commandList)
```

Create a structural element from the list of commands *commandList*.

Each command in this list represent a part of the structural element, that is a specific kind of shape (circular beam, grid, etc.) associated with one or several geometrical primitives. A command must be a tuple. The first element is the structural element part class name or alias name. The second element is a dictionary containing the parameters describing the part. Valid class names are all the classes defined in the module salome.geom.structelem.parts and inheriting [parts.StructuralElementPart](classparts_1_1StructuralElementPart.md). There are also several aliases for backward compatibility. Here is the complete list:   
- [parts.GeneralBeam](classparts_1_1GeneralBeam.md)

- [parts.CircularBeam](classparts_1_1CircularBeam.md)
- [parts.RectangularBeam](classparts_1_1RectangularBeam.md)
- [parts.ThickShell](classparts_1_1ThickShell.md)
- [parts.Grid](classparts_1_1Grid.md)
- [parts.VisuPoutreGenerale()](group__parts.md#gabf9c399302530d5b7a1e8e31288c445d) (alias for [parts.GeneralBeam](classparts_1_1GeneralBeam.md))
- [parts.VisuPoutreCercle()](group__parts.md#ga3dbec7b6a8b26194a84c1d312f0921e3) (alias for [parts.CircularBeam](classparts_1_1CircularBeam.md))
- [parts.VisuPoutreRectangle()](group__parts.md#ga7a7a5a41388aa6002fce71609ed543df) (alias for [parts.RectangularBeam](classparts_1_1RectangularBeam.md))
- [parts.VisuBarreGenerale()](group__parts.md#ga5d751bece84745d69aa3a46b21ecf194) (alias for [parts.GeneralBeam](classparts_1_1GeneralBeam.md))
- [parts.VisuBarreRectangle()](group__parts.md#ga01146a7956773b31f699f5b044c98308) (alias for [parts.RectangularBeam](classparts_1_1RectangularBeam.md))
- [parts.VisuBarreCercle()](group__parts.md#ga94dddd11457f6511b5d3183a6b5e2dcd) (alias for [parts.CircularBeam](classparts_1_1CircularBeam.md))
- [parts.VisuCable()](group__parts.md#ga2da9cab48657bdf3139a46ba1a71945d) (alias for [parts.CircularBeam](classparts_1_1CircularBeam.md))
- [parts.VisuCoque()](group__parts.md#gaf8cca11e9743ddb91558bd59d6214990) (alias for [parts.ThickShell](classparts_1_1ThickShell.md))
- [parts.VisuGrille()](group__parts.md#ga61faf3b1ebdca4054484192f6ae76185) (alias for [parts.Grid](classparts_1_1Grid.md))
- **Orientation:** This identifier is used to specify the orientation of one or several 1D structural element parts (i.e. beams). The parameters are described in class [orientation.Orientation1D](classorientation_1_1Orientation1D.md).

The valid parameters in the dictionary depend on the type of the structural element part, and are detailed in the documentation of the corresponding class. The only parameter that is common to all the classes is "MeshGroups" (that can also be named "Group_Maille"). It defines the name of the geometrical object(s) in the study that will be used as primitives to build the structural element part. This parameter can be either a list of strings or a single string with comma separated names.

### _extractMeshGroups()

```python
def _extractMeshGroups(self, command) private
```

This method extracts the names of the mesh groups (i.e.

the geometrical objects used to build the structural element part) in the command in parameter. It returns a tuple containing the mesh groups as a list of strings and the other parameters of the command as a new dictionary.

## Field Documentation

### _studyEditor

```python
_studyEditor private
```
