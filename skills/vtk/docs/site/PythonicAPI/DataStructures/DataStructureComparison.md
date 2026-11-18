<!-- source: https://examples.vtk.org/site/PythonicAPI/DataStructures/DataStructureComparison/ -->

# DataStructureComparison

Repository source: [DataStructureComparison](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/DataStructures/DataStructureComparison.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestDataStructureComparison.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/DataStructures/TestDataStructureComparison.png?raw=true target=)

### Description

In Python use the 'u' key to go up a level and the 'd' key to go down a level.

Info

Using the 'p' key in Python will generate the warning **no current renderer on the interactor style**.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/DataStructures/DataStructureComparison/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**DataStructureComparison.py**

```python
#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import (
    vtkKdTreePointLocator,
    vtkOctreePointLocator,
    vtkPolyData
)
from vtkmodules.vtkFiltersFlowPaths import vtkModifiedBSPTree
from vtkmodules.vtkFiltersGeneral import vtkOBBTree
from vtkmodules.vtkFiltersSources import vtkPointSource
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkPolyDataMapper,
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkTextActor,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Compare data structures.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('file_name', nargs='?', default=None,
                        help='The XML polydata source file name,e.g. Bunny.vtp.')
    args = parser.parse_args()

    return args.file_name

def main():
    colors = vtkNamedColors()

    file_name = get_program_parameters()
    original_mesh = vtkPolyData()
    if file_name:
        # If a file name is specified, open and use the file.
        if Path(file_name).is_file():
            reader = vtkXMLPolyDataReader(file_name=file_name)
            original_mesh.ShallowCopy(reader.update().output)
        else:
            print(f'{file_name} not found.')
    else:
        # If a file name is not specified, create a random cloud of points.
        sphere_source = vtkPointSource()
        sphere_source.SetNumberOfPoints(1000)

        original_mesh.ShallowCopy(sphere_source.update().output)

    number_of_viewports = 4
    style = KeyPressInteractorStyle(original_mesh)

    camera = vtkCamera()

    viewports = dict()
    for i in range(0, 4):
        viewports[i] = float(i) / number_of_viewports, 0, float(i + 1) / number_of_viewports, 1

    render_window = vtkRenderWindow(size=(300 * number_of_viewports, 400),
                                    window_name=f'{Path(sys.argv[0]).stem:s}')

    for i in range(0, 4):
        renderer = vtkRenderer(viewport=viewports[i],
                               background=colors.GetColor3d('cobalt'))  # background=(0.2, 0.3, 0.4))
        renderer.active_camera = camera
        render_window.AddRenderer(renderer)
        style.renderers.append(renderer)
        # if i == 0:
        #     style.current_renderer = renderer

    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window
    render_window_interactor.interactor_style = style

    style.initialize()
    style.renderers[0].ResetCamera()
    style.renderers[0].active_camera.Zoom(1.0)

    render_window_interactor.Start()

class KeyPressInteractorStyle(vtkInteractorStyleTrackballCamera):
    def __init__(self, data):
        super().__init__(self)

        self.colors = vtkNamedColors()

        self.data = data
        self.renderers = list()
        self.trees = list()
        self.mappers = list()
        self.actors = list()

        self.text_actors = list()
        self.text_representations = list()
        self.text_widgets = list()

        self.level = 1

        self.trees.append(vtkKdTreePointLocator())
        self.trees.append(vtkOBBTree())
        self.trees.append(vtkOctreePointLocator())
        self.trees.append(vtkModifiedBSPTree())

        self.mesh_mapper = vtkPolyDataMapper()
        self.mesh_actor = vtkActor(mapper=self.mesh_mapper)
        self.mesh_actor.property.color = self.colors.GetColor3d('Peru')

        self.AddObserver('KeyPressEvent', self.on_char)

    def initialize(self):
        self.mesh_mapper.input_data = self.data
        for i in range(0, 4):
            mapper = vtkPolyDataMapper()
            actor = vtkActor(mapper=mapper)
            actor.property.SetRepresentationToWireframe()
            self.mappers.append(mapper)
            self.actors.append(actor)
            self.renderers[i].AddActor(actor)
            self.renderers[i].AddActor(self.mesh_actor)

        # Create the text widgets.
        text = {0: 'Kd-tree', 1: 'OBB tree', 2: 'Octree', 3: 'BSP tree'}

        # text_actors = list()
        # text_representations = list()
        # text_widgets = list()
        text_property = vtkTextProperty(color=self.colors.GetColor3d('Yellow'), bold=True, italic=False, shadow=False,
                                        font_size=12, font_family_as_string='Courier',
                                        justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_CENTERED)

        text_positions = get_text_positions(list(text.values()),
                                            justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                            vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_BOTTOM
                                            )

        for k, v in text.items():
            self.text_actors.append(
                vtkTextActor(input=v, text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE, text_property=text_property))

            # Create the text representation. Used for positioning the text actor.
            self.text_representations.append(vtkTextRepresentation(enforce_normalized_viewport_bounds=True))
            self.text_representations[k].position_coordinate.value = text_positions[v]['p']
            self.text_representations[k].position2_coordinate.value = text_positions[v]['p2']

            # Create the TextWidget
            self.text_widgets.append(
                vtkTextWidget(representation=self.text_representations[k], text_actor=self.text_actors[k],
                              default_renderer=self.renderers[k], interactor=self.interactor, selectable=False))

        for k in text.keys():
            self.text_widgets[k].On()

        # print(f'Level = {self.level}')
        self.redraw()

    def on_char(self, obj, event):
        ch = self.interactor.GetKeySym()

        if ch == 'd':
            self.level += 1
        elif ch == 'u':
            if self.level > 1:
                self.level -= 1
        else:
            print('An unhandled key was pressed.')

        self.redraw()

        # Don't forward the "pick" command.
        if ch != 'p':
            # Forward events
            super().OnChar()

    def redraw(self):
        # print(f'Level = {self.level}')
        for i in range(0, 4):
            tree = self.trees[i]
            tree.SetDataSet(self.data)
            tree.BuildLocator()
            polydata = vtkPolyData()

            print(f'Tree {i} has {tree.level} levels.')

            if self.level >= tree.GetLevel():
                tree.GenerateRepresentation(tree.GetLevel(), polydata)
            else:
                tree.GenerateRepresentation(self.level, polydata)

            self.mappers[i].SetInputData(polydata)

        self.interactor.GetRenderWindow().Render()

def get_text_positions(names, justification=0, vertical_justification=0, width=0.96, height=0.1):
    """
    Get viewport positioning information for a list of names.

    :param names: The list of names.
    :param justification: Horizontal justification of the text, default is left.
    :param vertical_justification: Vertical justification of the text, default is bottom.
    :param width: Width of the bounding_box of the text in screen coordinates.
    :param height: Height of the bounding_box of the text in screen coordinates.
    :return: A list of positioning information.
    """
    # The gap between the left or right edge of the screen and the text.
    dx = 0.02
    width = abs(width)
    if width > 0.96:
        width = 0.96

    y0 = 0.01
    height = abs(height)
    if height > 0.9:
        height = 0.9
    dy = height
    if vertical_justification == TextProperty.VerticalJustification.VTK_TEXT_TOP:
        y0 = 1.0 - (dy + y0)
        dy = height
    if vertical_justification == TextProperty.VerticalJustification.VTK_TEXT_CENTERED:
        y0 = 0.5 - (dy / 2.0 + y0)
        dy = height

    name_len_min = 0
    name_len_max = 0
    first = True
    for k in names:
        sz = len(k)
        if first:
            name_len_min = name_len_max = sz
            first = False
        else:
            name_len_min = min(name_len_min, sz)
            name_len_max = max(name_len_max, sz)
    text_positions = dict()
    for k in names:
        sz = len(k)
        delta_sz = width * sz / name_len_max
        if delta_sz > width:
            delta_sz = width

        if justification == TextProperty.Justification.VTK_TEXT_CENTERED:
            x0 = 0.5 - delta_sz / 2.0
        elif justification == TextProperty.Justification.VTK_TEXT_RIGHT:
            x0 = 1.0 - dx - delta_sz
        else:
            # Default is left justification.
            x0 = dx

        # For debugging!
        # print(
        #     f'{k:16s}: (x0, y0) = ({x0:3.2f}, {y0:3.2f}), (x1, y1) = ({x0 + delta_sz:3.2f}, {y0 + dy:3.2f})'
        #     f', width={delta_sz:3.2f}, height={dy:3.2f}')
        text_positions[k] = {'p': [x0, y0, 0], 'p2': [delta_sz, dy, 0]}

    return text_positions

@dataclass(frozen=True)
class TextProperty:
    @dataclass(frozen=True)
    class Justification:
        VTK_TEXT_LEFT: int = 0
        VTK_TEXT_CENTERED: int = 1
        VTK_TEXT_RIGHT: int = 2

    @dataclass(frozen=True)
    class VerticalJustification:
        VTK_TEXT_BOTTOM: int = 0
        VTK_TEXT_CENTERED: int = 1
        VTK_TEXT_TOP: int = 2

if __name__ == '__main__':
    main()
```
