<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_curvefitting.html -->

# Create interpolation curve

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchPoints
SketchPoint_1 = Sketch_1.addPoint(-70.28350515463917, 1.388316151202744)
SketchPoint_2 = Sketch_1.addPoint(-26.89862542955327, 51.7147766323024)
SketchPoint_3 = Sketch_1.addPoint(40.08762886597938, 32.27835051546391)
SketchPoint_4 = Sketch_1.addPoint(66.46563573883162, -29.8487972508591)

### Create interpolation curve
InterpolationPoints = [SketchPoint_1.coordinates(),
                       SketchPoint_2.coordinates(),
                       SketchPoint_3.coordinates(),
                       SketchPoint_4.coordinates()]
SketchBSpline_1 = Sketch_1.addInterpolation(InterpolationPoints)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_1.startPoint())
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchBSpline_1.result())
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchBSpline_1.result())
Sketch_1.setCoincident(SketchPoint_4.coordinates(), SketchBSpline_1.endPoint())

### Create periodic interpolation curve
SketchBSpline_2 = Sketch_1.addInterpolation(InterpolationPoints, periodic = True)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_2.result())
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchBSpline_2.result())
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchBSpline_2.result())
Sketch_1.setCoincident(SketchPoint_4.coordinates(), SketchBSpline_2.result())

### Create closed interpolation curve
SketchBSpline_3 = Sketch_1.addInterpolation(InterpolationPoints, closed = True)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_3.startPoint())
Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchBSpline_3.result())
Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchBSpline_3.result())
Sketch_1.setCoincident(SketchPoint_4.coordinates(), SketchBSpline_3.result())
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_3.endPoint())

model.do()

model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/4a874086fdec21655060af913f7d1c69/interpolation.py)

# Create approximation curve

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchPoints
SketchPoint_1 = Sketch_1.addPoint(-70.28350515463917, 1.388316151202744)
SketchPoint_2 = Sketch_1.addPoint(-26.89862542955327, 51.7147766323024)
SketchPoint_3 = Sketch_1.addPoint(40.08762886597938, 32.27835051546391)
SketchPoint_4 = Sketch_1.addPoint(66.46563573883162, -29.8487972508591)

### Create approximating curve
ApproximationPoints = [SketchPoint_1.coordinates(),
                       SketchPoint_2.coordinates(),
                       SketchPoint_3.coordinates(),
                       SketchPoint_4.coordinates()]
SketchBSpline_1 = Sketch_1.addApproximation(ApproximationPoints, precision = 30)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_1.startPoint())
Sketch_1.setCoincident(SketchPoint_4.coordinates(), SketchBSpline_1.endPoint())

### Create periodic approximating curve
SketchBSpline_2 = Sketch_1.addApproximation(ApproximationPoints, precision = 30, periodic = True)

### Create closed approximating curve
SketchBSpline_3 = Sketch_1.addApproximation(ApproximationPoints, precision = 30, closed = True)
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_3.startPoint())
Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchBSpline_3.endPoint())

model.do()

model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/1d7b9057f7852d622f2feebcd5acbf29/approximation.py)
