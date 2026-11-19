<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__transform__d.html -->

# Transformation Operations deprecated methods geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### MultiRotate1D()

```python
def MultiRotate1D(self, theObject, theAxis, theNbTimes, theName = None)
```

Deprecated method.

Use MultiRotate1DNbTimes instead.

### MultiRotate2D()

```python
def MultiRotate2D(self, theObject, theAxis, theAngle, theNbTimes1, theStep, theNbTimes2, theName = None)
```

The same, as [MultiRotate2DByStep()](group__l3__transform.md#gaeb16678a6ec2aaa88013f1281f02bfb9), but theAngle is in degrees.

This method is DEPRECATED. Use [MultiRotate2DByStep()](group__l3__transform.md#gaeb16678a6ec2aaa88013f1281f02bfb9) instead.

### MakeMultiRotation1D()

```python
def MakeMultiRotation1D(self, aShape, aDir, aPoint, aNbTimes, theName = None)
```

The same, as [MultiRotate1D()](group__l3__transform__d.md#ga1756faf7332d8004f48b4877758ecd7b), but axis is given by direction and point This method is DEPRECATED.

Use MakeMultiRotation1DNbTimes instead.

### MakeMultiRotation2D()

```python
def MakeMultiRotation2D(self, aShape, aDir, aPoint, anAngle, nbtimes1, aStep, nbtimes2, theName = None)
```

The same, as [MultiRotate2D()](group__l3__transform__d.md#gad2bb612b9e96d51e1b0698706becf5cc), but axis is given by direction and point This method is DEPRECATED.

Use MakeMultiRotation2DByStep instead.
