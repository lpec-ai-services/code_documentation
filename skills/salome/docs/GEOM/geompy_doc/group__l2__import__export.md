<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l2__import__export.html -->

# Importing/exporting geometrical objects geomBuilder Python module » All package methods, grouped by their purpose

## Detailed Description

## Function Documentation

### ImportFile()

```python
def ImportFile(self, theFileName, theFormatName, theName = None)
```

Import a shape from the BREP, IGES, STEP or other file (depends on given format) with given name.

Note: this function is deprecated, it is kept for backward compatibility only Use Import<FormatName> instead, where <FormatName> is a name of desirable format to import.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theFormatName | Specify format for the file reading. Available formats can be obtained with InsertOp.ImportTranslators() method. If format 'IGES_SCALE' is used instead of 'IGES' or format 'STEP_SCALE' is used instead of 'STEP', length unit will be set to 'meter' and result model will be scaled. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the imported shape. If material names are imported it returns the list of objects. The first one is the imported object followed by material groups.

Note
:   Auto publishing is allowed for the shape itself. Imported material groups are not automatically published.

[Example](../tui_test_others_page.md#swig_Import_Export)

### Import()

```python
def Import(self, theFileName, theFormatName, theName = None)
```

Deprecated analog of [ImportFile()](group__l2__import__export.md#gabab8f9957b6ede79a702558b09135bd2)

### RestoreShape()

```python
def RestoreShape(self, theStream, theName = None)
```

Read a shape from the binary stream, containing its bounding representation (BRep).

Note
:   As the byte-stream representing the shape data can be quite large, this method is not automatically dumped to the Python script with the DumpStudy functionality; so please use this method carefully, only for strong reasons.
:   [GEOM.GEOM_Object.GetShapeStream()](interfaceGEOM_1_1GEOM__Object.md#ab9d9b65c86d4df378bccacb6dee91362) method can be used to obtain the shape's data stream.

Parameters
:   |  |  |
    | --- | --- |
    | theStream | The BRep binary stream. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the shape, read from theStream.

[Example](../tui_test_others_page.md#swig_Import_Export)

### Export()

```python
def Export(self, theObject, theFileName, theFormatName)
```

Export the given shape into a file with given name.

Note: this function is deprecated, it is kept for backward compatibility only Use Export<FormatName> instead, where <FormatName> is a name of desirable format to export.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theFormatName | Specify format for the shape storage. Available formats can be obtained with geompy.InsertOp.ExportTranslators()[0] method. |

[Example](../tui_test_others_page.md#swig_Import_Export)

### ExportSTL()

```python
def ExportSTL(self, theObject, theFileName, theIsASCII = True, theDeflection = 0.001, theIsRelative = True)
```

Export the given shape into a file with given name in STL format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theIsASCII | The format of the exported file (ASCII or Binary) |
    | theDeflection | Deflection of the given shape. |
    | theIsRelative | If True (default value), the deflection is calculated relatively to the size of the shape; if False, the user defined deflection is used. |

### ImportSTL()

```python
def ImportSTL(self, theFileName, theName = None)
```

Import a shape from the STL file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the imported shape. If material names are imported it returns the list of objects. The first one is the imported object followed by material groups.

Note
:   Auto publishing is allowed for the shape itself. Imported material groups are not automatically published.

### ExportBREP()

```python
def ExportBREP(self, theObject, theFileName)
```

Export the given shape into a file with given name in BREP format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |

### ImportBREP()

```python
def ImportBREP(self, theFileName, theName = None)
```

Import a shape from the BREP file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the imported shape. If material names are imported it returns the list of objects. The first one is the imported object followed by material groups.

Note
:   Auto publishing is allowed for the shape itself. Imported material groups are not automatically published.

### ExportSTEP()

```python
def ExportSTEP(self, theObject, theFileName, theUnit = GEOM.LU_METER)
```

Export the given shape into a file with given name in STEP format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theUnit | the length unit (see [GEOM::length_unit](namespaceGEOM.md#a97cb3e88a0c463b3c48a5e555e4eaae6)). In meters by default. |

### GetSTEPUnit()

```python
def GetSTEPUnit(self, theFileName)
```

Return length unit from given STEP file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |

Returns
:   String, containing the units name.

[Example](../tui_test_others_page.md#swig_Import_Export)

### ImportSTEP()

```python
def ImportSTEP(self, theFileName, theIsIgnoreUnits = False, IsCreateAssemblies = False, theName = None)
```

Import a shape from the STEP file with given name.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theIsIgnoreUnits | If True, file length units will be ignored (set to 'meter') and result model will be scaled, if its units are not meters. If False (default), file length units will be taken into account. |
    | IsCreateAssemblies | If True, for each assembly compound is created in the result. If False Compounds that contain a single shape are eliminated from the result. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the imported shape. If material names are imported it returns the list of objects. The first one is the imported object followed by material groups.

Note
:   Auto publishing is allowed for the shape itself. Imported material groups are not automatically published.

[Example](../tui_test_others_page.md#swig_Import_Export)

### ExportIGES()

```python
def ExportIGES(self, theObject, theFileName, theVersion = "5.1")
```

Export the given shape into a file with given name in IGES format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theVersion | Version of IGES format which defines, whether to write only faces (5.1 IGES format) or shells and solids also (5.3 IGES format). |

### GetIGESUnit()

```python
def GetIGESUnit(self, theFileName)
```

Return length unit from given IGES file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |

Returns
:   String, containing the units name.

[Example](../tui_test_others_page.md#swig_Import_Export)

### ImportIGES()

```python
def ImportIGES(self, theFileName, theIsIgnoreUnits = False, theName = None)
```

Import a shape from the IGES file with given name.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theIsIgnoreUnits | If True, file length units will be ignored (set to 'meter') and result model will be scaled, if its units are not meters. If False (default), file length units will be taken into account. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the imported shape. If material names are imported it returns the list of objects. The first one is the imported object followed by material groups.

Note
:   Auto publishing is allowed for the shape itself. Imported material groups are not automatically published.

[Example](../tui_test_others_page.md#swig_Import_Export)

### ExportXAO()

```python
def ExportXAO(self, shape, groups, fields, author, fileName, shapeFileName = "")
```

Export a shape to XAO format.

Parameters
:   |  |  |
    | --- | --- |
    | shape | The shape to export |
    | groups | The list of groups to export |
    | fields | The list of fields to export |
    | author | The author of the file |
    | fileName | The name of the file to export |
    | shapeFileName | The name of the BRep file to export |

Returns
:   True if operation is successful or False otherwise

### ExportXAOMem()

```python
def ExportXAOMem(self, shape, groups, fields, author)
```

Export a shape to XAO format in byte array.

Parameters
:   |  |  |
    | --- | --- |
    | shape | The shape to export |
    | groups | The list of groups to export |
    | fields | The list of fields to export |
    | author | The author of the file |

Returns
:   Byte array with exported data

### ImportXAO()

```python
def ImportXAO(self, fileName, theName = None)
```

Import a shape from XAO format.

Parameters
:   |  |  |
    | --- | --- |
    | fileName | The name of the file to import |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   tuple (*res*, *shape*, *subShapes*, *groups*, *fields*) *res* Flag indicating if the import was successful *shape* The imported shape *subShapes* The list of imported subShapes *groups* The list of imported groups *fields* The list of imported fields

### ImportXAOMem()

```python
def ImportXAOMem(self, byteArray, theName = None)
```

Import a shape from XAO format byte array.

Parameters
:   |  |  |
    | --- | --- |
    | byteArray | byte array with XAO data |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   tuple (*res*, *shape*, *subShapes*, *groups*, *fields*) *res* Flag indicating if the import was successful *shape* The imported shape *subShapes* The list of imported subShapes *groups* The list of imported groups *fields* The list of imported fields

### ExportVTK()

```python
def ExportVTK(self, theObject, theFileName, theDeflection = 0.001)
```

Export the given shape into a file with given name in VTK format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theDeflection | Deflection of the given shape. |
