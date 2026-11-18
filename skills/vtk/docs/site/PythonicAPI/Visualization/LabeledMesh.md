<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/LabeledMesh/ -->

# LabeledMesh

Repository source: [LabeledMesh](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/LabeledMesh.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLabeledMesh.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestLabeledMesh.png?raw=true target=)

### Description

This example was translated into C++ from its TCL counterpart by Jake Nickel from the University of Iowa. It demonstrates the use of [vtkLabeledDataMapper](https://www.vtk.org/doc/nightly/html/classvtkLabeledDataMapper.html). This class is used for displaying numerical data from an underlying data set. In the case of this example, the underlying data are the point and cell ids.

Note

This original source code for this example is [here](https://gitlab.kitware.com/vtk/vtk/blob/395857190c8453508d283958383bc38c9c2999bf/Examples/Annotation/Cxx/LabeledMesh/LabeledMesh.cxx).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/LabeledMesh/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**LabeledMesh.py**

```python
#!/usr/bin/env python3

from dataclasses import dataclass

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingFreeType
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkCellArray
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkFiltersCore import (
    vtkCellCenters,
    vtkGenerateIds
)
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor, vtkActor2D,
    vtkPolyDataMapper, vtkPolyDataMapper2D,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkSelectVisiblePoints
)
from vtkmodules.vtkRenderingLabel import vtkLabeledDataMapper

def main():
    colors = vtkNamedColors()

    # Create a selection window.
    # We will display the point and cell ids that lie within this window.
    xmin = 200
    x_length = 100
    xmax = xmin + x_length
    ymin = 200
    y_length = 100
    ymax = ymin + y_length
    selection = (xmin, xmax, ymin, ymax)

    pts = vtkPoints()
    pts.InsertPoint(0, xmin, ymin, 0)
    pts.InsertPoint(1, xmax, ymin, 0)
    pts.InsertPoint(2, xmax, ymax, 0)
    pts.InsertPoint(3, xmin, ymax, 0)

    rect = vtkCellArray()
    rect.InsertNextCell(5)
    rect.InsertCellPoint(0)
    rect.InsertCellPoint(1)
    rect.InsertCellPoint(2)
    rect.InsertCellPoint(3)
    rect.InsertCellPoint(0)

    select_rect = vtkPolyData(points=pts, lines=rect)

    rect_mapper = vtkPolyDataMapper2D(input_data=select_rect)

    rect_actor = vtkActor2D(mapper=rect_mapper)
    rect_actor.property.color = colors.GetColor3d('Black')

    # Create a sphere and its associated mapper and actor.
    sphere = vtkSphereSource()
    sphere_mapper = vtkPolyDataMapper()
    sphere >> sphere_mapper

    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('BurlyWood')

    # Generate data arrays containing point and cell ids.
    ids = vtkGenerateIds(point_ids=True, cell_ids=True, field_data=True)
    sphere >> ids

    # Create the renderer here because vtkSelectVisiblePoints needs it.
    ren = vtkRenderer(use_hidden_line_removal=True, background=colors.GetColor3d('SlateGray'))

    # Create labels for points
    vis_pts = vtkSelectVisiblePoints(renderer=ren, selection_window=True, selection=selection)

    # Create the mapper to display the point ids.  Specify the
    # format to use for the labels.  Also create the associated actor.
    # Note: We need to change the field_data_name because the point ID array
    #       default name has changed in vtkGenerateIds.
    ldm = vtkLabeledDataMapper(label_mode=LabeledDataMapper.LabelMode.VTK_LABEL_FIELD_DATA,
                               field_data_name='vtkPointIds')
    ids >> vis_pts >> ldm

    point_labels = vtkActor2D(mapper=ldm)
    point_labels.property.color = colors.GetColor3d('Yellow')

    # Create labels for cells
    cc = vtkCellCenters()

    vis_cells = vtkSelectVisiblePoints(renderer=ren, selection_window=True, selection=selection)

    # Create the mapper to display the cell ids.  Specify the
    # format to use for the labels.  Also create the associated actor.
    cell_mapper = vtkLabeledDataMapper(label_mode=LabeledDataMapper.LabelMode.VTK_LABEL_FIELD_DATA)
    ids >> cc >> vis_cells >> cell_mapper
    cell_mapper.label_text_property.color = colors.GetColor3d('DarkGreen')

    cell_labels = vtkActor2D(mapper=cell_mapper)

    # Create the RenderWindow and RenderWindowInteractor
    ren_win = vtkRenderWindow(size=(500, 500), window_name='LabeledMesh')
    ren_win.AddRenderer(ren)

    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win

    # Add the actors to the renderer set the background and size render
    ren.AddActor(sphere_actor)
    ren.AddViewProp(rect_actor)
    ren.AddViewProp(point_labels)
    ren.AddViewProp(cell_labels)

    ren_win.Render()

    data = {'Visible Points': vis_pts, 'Visible Cells': vis_cells, 'Points': pts, 'Render Window': ren_win}

    # Move the selection window across the data set.
    move_window(data, x_length, y_length)

    # Put the selection window in the center of the render window.
    # This works because the xmin = ymin = 200, x_length = y_length = 100, and
    # the render window size is 500 x 500.
    place_window(data, selection)

    iren.Initialize()
    iren.Start()

def place_window(data, selection):
    data['Visible Points'].selection = selection
    data['Visible Cells'].selection = selection

    xmin = selection[0]
    ymin = selection[2]
    data['Points'].InsertPoint(0, xmin, ymin, 0)
    data['Points'].InsertPoint(1, xmin, ymin, 0)
    data['Points'].InsertPoint(2, xmin, ymin, 0)
    data['Points'].InsertPoint(3, xmin, ymin, 0)

    # Call Modified because InsertPoints does not modify vtkPoints
    # (for performance reasons).
    data['Points'].Modified()

    data['Render Window'].Render()

def move_window(data, xLength, yLength):
    for y in range(100, 300, 25):
        for x in range(100, 300, 25):
            selection = (x, x + xLength, y, y + yLength)
            place_window(data, selection)

@dataclass(frozen=True)
class LabeledDataMapper:
    @dataclass(frozen=True)
    class LabelMode:
        VTK_LABEL_IDS: int = 0
        VTK_LABEL_SCALARS: int = 1
        VTK_LABEL_VECTORS: int = 2
        VTK_LABEL_NORMALS: int = 3
        VTK_LABEL_TCOORDS: int = 4
        VTK_LABEL_TENSORS: int = 5
        VTK_LABEL_FIELD_DATA: int = 6

if __name__ == '__main__':
    main()
```
