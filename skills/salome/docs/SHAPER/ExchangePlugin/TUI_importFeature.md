<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ExchangePlugin/TUI_importFeature.html -->

# Import File

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Import_1 = model.addImport(Part_1_doc, "/dn48/newgeom/for_gzy/gzy_data/Compound_2.brep")
model.do()
Import_1.setName("Compound_2")
Import_1.result().setName("Compound_2_1")
Import_1.result().subResult(0).setName("Compound_2_1_1")
Import_1.result().subResult(1).setName("Compound_2_1_2")
Import_1.result().subResult(2).setName("Compound_2_1_3")
Import_1.result().subResult(3).setName("Compound_2_1_4")
Import_1.result().subResult(4).setName("Compound_2_1_5")
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/c7d426ab97ddca1141edbb00613817ef/import.py)

# Import STEP File

```python
from salome.shaper import model
import os

model.begin()
file_path = os.path.join(os.getenv("DATA_DIR"),"Shapes","Step","black_and_white.step")
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Import_1 = model.addImportSTEP(Part_1_doc,file_path, True, True, True)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/4de6fcbff34b53804e1d2b935ec956cc/importStep.py)
