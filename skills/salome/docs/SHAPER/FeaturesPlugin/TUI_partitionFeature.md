<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_partitionFeature.html -->

# Create Partition

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Cylinder_1 = model.addCylinder(Part_1_doc,
                               model.selection("VERTEX", "PartSet/Origin"),
                               model.selection("EDGE", "PartSet/OZ"), 5, 10)
Partition_1 = model.addPartition(Part_1_doc,
                                 [model.selection("SOLID", "Cylinder_1_1"), model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/34bc0b69254a1b08beb39b23a21e2b0d/partition.py)
