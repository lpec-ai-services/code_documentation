<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classsketcher_1_1Sketcher.html -->

# Sketcher Class Reference sketcher - Simplified sketcher API

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self)
```

## Member Function Documentation

### startAtPoint()

```python
def startAtPoint(self, x = 0, y = 0)
```

### translateToPoint()

```python
def translateToPoint(self, x = 10, y = 0)
```

```python
segment->point->absolute
```

### translateWithVector()

```python
def translateWithVector(self, deltax = 10, deltay = 0)
```

```python
segment->point->relative
```

### translateWithAngleAndLength()

```python
def translateWithAngleAndLength(self, angle = 30, length = 100)
```

```python
segment->direction->angle+length
```

### intersectXWithAngle()

```python
def intersectXWithAngle(self, angle = 30, x = 100)
```

```python
segment->direction->angle+length
```

### intersectYWithAngle()

```python
def intersectYWithAngle(self, angle = 30, y = 100)
```

```python
segment->direction->angle+length
```

### close()

```python
def close(self)
```

```python
add a segment to reach the starting point and get a closed wire.
```

### toString()

```python
def toString(self)
```

### getGeomWire()

```python
def getGeomWire(self)
```

## Field Documentation

### __sketch

```python
__sketch = None static private
```

### __xstart [1/2]

```python
int __xstart = 0 static private
```

### __ystart [1/2]

```python
int __ystart = 0 static private
```

### __xstart [2/2]

```python
__xstart private
```

### __ystart [2/2]

```python
__ystart private
```
