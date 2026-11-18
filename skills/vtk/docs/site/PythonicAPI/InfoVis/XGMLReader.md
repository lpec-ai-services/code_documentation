<!-- source: https://examples.vtk.org/site/PythonicAPI/InfoVis/XGMLReader/ -->

# XGMLReader

Repository source: [XGMLReader](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/InfoVis/XGMLReader.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestXGMLReader.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/InfoVis/TestXGMLReader.png?raw=true target=)

### Description

This example reads and displays the graph from a gml file.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/InfoVis/XGMLReader/)), ([CSharp](https://examples.vtk.org/site/CSharp/InfoVis/XGMLReader/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**XGMLReader.py**

```python
#!/usr/bin/env python3

from pathlib import Path

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOInfovis import vtkXGMLReader
from vtkmodules.vtkViewsCore import vtkViewTheme
from vtkmodules.vtkViewsInfovis import (
    vtkGraphLayoutView
)

def get_program_parameters():
    import argparse
    description = 'XGML Reader.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename',
                        help='The path to the gml file, e.g. fsm.gml.')
    args = parser.parse_args()
    return args.filename

def main():
    colors = vtkNamedColors()

    fn = get_program_parameters()
    fp = Path(fn)
    file_check = True
    if not fp.is_file():
        print(f'Missing geometry file: {fp}.')
        file_check = False
    else:
        if fp.suffix.lower() != '.gml':
            print(f'The geometry file : {fp} must have a .wrl suffix.')
            file_check = False
    if not file_check:
        return

    reader = vtkXGMLReader(file_name=fp)
    reader.update()

    g = reader.output

    theme = vtkViewTheme(line_width=1, point_size=5, cell_opacity=0.99, outline_color=colors.GetColor3d('Gray'),
                         # Vertices
                         point_color=colors.GetColor3d('Chartreuse'), selected_point_color=colors.GetColor3d('Magenta'),
                         point_hue_range=(1.0, 1.0), point_saturation_range=(1.0, 1.0), point_value_range=(0.0, 1.0),
                         # Edges
                         cell_color=colors.GetColor3d('Honeydew'), selected_cell_color=colors.GetColor3d('Cyan'),
                         cell_hue_range=(1.0, 1.0), cell_saturation_range=(1.0, 1.0), cell_value_range=(0.0, 1.0),
                         )
    # simple2D = vtkSimple2DLayoutStrategy()

    graphLayoutView = vtkGraphLayoutView()
    graphLayoutView.AddRepresentationFromInput(g)
    graphLayoutView.ApplyViewTheme(theme)
    # If we create a layout object directly, just set the pointer to this method.
    # graphLayoutView.SetLayoutStrategy(simple2D).
    graphLayoutView.SetLayoutStrategyToSimple2D()

    graphLayoutView.ResetCamera()

    graphLayoutView.renderer.gradient_background = True
    graphLayoutView.renderer.background2 = colors.GetColor3d('DarkSlateGray')
    graphLayoutView.renderer.background = colors.GetColor3d('Black')

    graphLayoutView.render_window.size = (600, 600)
    graphLayoutView.render_window.window_name = 'XGMLReader'

    graphLayoutView.Render()

    graphLayoutView.interactor.Start()

if __name__ == '__main__':
    main()
```
