<!-- source: https://examples.vtk.org/site/Python/Tutorial/Tutorial_Step2/ -->

# Tutorial Step2

Repository source: [Tutorial_Step2](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Tutorial/Tutorial_Step2.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Tutorial/TestTutorial_Step2.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Tutorial/TestTutorial_Step2.png?raw=true target=)

### Description

This example shows how to add an observer to a Python program. It extends the [Tutorial_Step1](Tutorial_Step1.md) example (see that example for information on the basic setup).

VTK uses a command/observer design pattern. That is, observers watch for particular events that any [vtkObject](https://www.vtk.org/doc/nightly/html/classvtkObject.html) (or subclass) may invoke on itself. For example, the [vtkRenderer](https://www.vtk.org/doc/nightly/html/classvtkRenderer.html) invokes a "StartEvent" as it begins to render. Here we add an observer that invokes a command when this event is observed.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Tutorial/Tutorial_Step2/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Tutorial_Step2.py**

```python
#!/usr/bin/env python

"""
=========================================================================

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/

"""

# First access the VTK module (and any other needed modules) by importing them.
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderer
)

def main(argv):
    colors = vtkNamedColors()

    #
    # The pipeline creation is documented in Tutorial_Step1.
    #
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))
    ren1.ResetCamera()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300, 300)
    renWin.SetWindowName('Tutorial_Step2')

    # Here is where we setup the observer.
    mo1 = vtkMyCallback(ren1)
    ren1.AddObserver('StartEvent', mo1)

    #
    # Now we loop over 360 degrees and render the cone each time.
    #
    for i in range(0, 360):
        # Render the image.
        renWin.Render()
        # Rotate the active camera by one degree.
        ren1.GetActiveCamera().Azimuth(1)

class vtkMyCallback(object):
    """
    Callback for the interaction.
    """

    def __init__(self, renderer):
        self.renderer = renderer

    def __call__(self, caller, ev):
        position = self.renderer.GetActiveCamera().GetPosition()
        print('({:5.2f}, {:5.2f}, {:5.2f})'.format(*position))

if __name__ == '__main__':
    import sys

    main(sys.argv)
```
