<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__sketcher.html -->

# gsketcher - Wrapper to help the creation of simple sketches

## Detailed Description

This module provides the user with a simple python API to realize various sketches from the [GEOM](namespaceGEOM.md) text user interface.   
Example:

```python
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a wire for sketcher
geomObj_1 = geompy.MakeMarker(0, 0, 0, 1, 0, 0, 0, 1, 0)

# Create the sketch
sk = geompy.Sketcher2D()
sk.addPoint(0.000000, 0.000000)
sk.addSegmentAbsolute(50.000000, 50.000000)
sk.addSegmentPerpY(0.000000)
sk.addArcAbsolute(0.000000, 0.000000)
sk.close()
Sketch_1 = sk.wire(geomObj_1)

# add objects in the study
geompy.addToStudy( Sketch_1, 'Sketch_1' )

# update object browser
salome.sg.updateObjBrowser()
```

Additional examples can be found as unit tests in the source code.
