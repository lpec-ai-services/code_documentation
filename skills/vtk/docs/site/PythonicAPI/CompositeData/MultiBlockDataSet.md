<!-- source: https://examples.vtk.org/site/PythonicAPI/CompositeData/MultiBlockDataSet/ -->

# MultiBlockDataSet

Repository source: [MultiBlockDataSet](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/CompositeData/MultiBlockDataSet.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/CompositeData/TestMultiBlockDataSet.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/CompositeData/TestMultiBlockDataSet.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/CompositeData/MultiBlockDataSet/)), ([Python](../../Python/CompositeData/MultiBlockDataSet.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MultiBlockDataSet.py**

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.util.execution_model import select_ports
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkMultiBlockDataSet
from vtkmodules.vtkFiltersCore import vtkExtractEdges
from vtkmodules.vtkFiltersGeometry import vtkCompositeDataGeometryFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkProperty
)

def main():
    colors = vtkNamedColors()

    # PART 1 Make some Data.
    # Make a tree.
    root = vtkMultiBlockDataSet()

    # Make some leaves.
    leaf1 = vtkSphereSource(center=(0, 0, 0))
    leaf2 = vtkSphereSource(center=(1.75, 2.5, 0), radius=1.5)
    leaf3 = vtkSphereSource(center=(4, 0, 0), radius=2)

    branch = vtkMultiBlockDataSet()
    root.SetBlock(0, branch)
    branch.SetBlock(0, leaf1.update().output)
    branch.SetBlock(1, leaf2.update().output)
    root.SetBlock(1, leaf3.update().output)

    # PART 2 Do something with the data
    # a non composite aware filter, the pipeline will iterate
    edges = vtkExtractEdges(input_data=root)

    # PART 3 Show the data
    # also demonstrate a composite aware filter
    # this filter aggregates all blocks into one polydata
    # this is handy for display, although fairly limited.
    polydata = vtkCompositeDataGeometryFilter()
    edges >> polydata

    # Create the Renderer, RenderWindow, and RenderWindowInteractor.
    ren = vtkRenderer(background=colors.GetColor3d('CornflowerBlue'))
    ren_win = vtkRenderWindow(window_name=Path(sys.argv[0]).stem)
    ren_win.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(ren_win)

    mapper = vtkPolyDataMapper()
    select_ports(0, polydata) >> select_ports(0, mapper)
    prop = vtkProperty(color=colors.GetColor3d('Yellow'), line_width=2)
    actor = vtkActor(mapper=mapper, property=prop)

    # Enable user interface interactor.
    ren.AddActor(actor)
    ren_win.Render()
    iren.Start()

if __name__ == '__main__':
    main()
```
