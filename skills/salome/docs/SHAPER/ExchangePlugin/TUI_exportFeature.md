<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ExchangePlugin/TUI_exportFeature.html -->

# Export File

```python
from salome.shaper import model
import os 

model.begin()
file_path = os.path.join(os.getenv("DATA_DIR"), "test.step")
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Export_1 = model.exportToFile(Part_1_doc, file_path,
                              [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/bc2f2b633a08fe657ae81d5b66ffdfb9/export.py)

# Export XAO File

```python
from salome.shaper import model
import os 

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)

file_xao = os.path.join(os.getenv("DATA_DIR"), "test.xao")
Export_1 = model.exportToXAO(Part_1_doc, file_xao,
                             model.selection("SOLID", "Box_1_1"), "author", "box")

file_xao = os.path.join(os.getenv("DATA_DIR"), "test1.xao")
file_brep = os.path.join(os.getenv("DATA_DIR"), "test1_shape.brep")
Export_2 = model.exportToXAO(Part_1_doc, file_xao,
                             model.selection("SOLID", "Box_1_1"), "author", "box",
                             file_brep)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/9999a0ee2a0bd69eaf0e6c171718b855/exportXAO.py)

# Export STL File

```python
from salome.shaper import model
import os

model.begin()
file_path = os.path.join(os.getenv("DATA_DIR"), "test.stl")
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Export_1 = model.exportToSTL(Part_1_doc, file_path,
                              model.selection("SOLID", "Box_1_1"),0.0001,0.5,True,False)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/a2f921337bafe50d04fc2a3f111ff6f9/exportSTL.py)
