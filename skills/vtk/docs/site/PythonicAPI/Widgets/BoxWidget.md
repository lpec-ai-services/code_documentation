<!-- source: https://examples.vtk.org/site/PythonicAPI/Widgets/BoxWidget/ -->

# BoxWidget

Repository source: [BoxWidget](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Widgets/BoxWidget.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestBoxWidget.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Widgets/TestBoxWidget.png?raw=true target=)

### Description

This example uses a [vtkBoxWidget](https://www.vtk.org/doc/nightly/html/classvtkBoxWidget.html) to manipulate an actor. The class includes geometry to draw a box around the object, which is bound to it via `SetProp3D`. The box is dimensioned using the `SetPlaceFactor` method, and positioned with the `PlaceWidget` method.

After the initial setup, synchronizing the box with the object is done through a custom callback class or function, which is passed to the box widget through the `AddObserver` method.

For a widget that isn't tied to a specific [vtkProp3D](https://www.vtk.org/doc/nightly/html/classvtkProp3D.html) and has its geometric representation separate from the interaction logic, see the example [BoxWidget2](BoxWidget2.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Widgets/BoxWidget/)), ([Python](../../Python/Widgets/BoxWidget.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**BoxWidget.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkInteractionWidgets import vtkBoxWidget
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_program_parameters():
    import argparse
    description = 'Demonstrate two ways of using callbacks.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--fn_cb', action='store_false',
                        help='Use a function callback instead of a class callback.')
    args = parser.parse_args()
    return args.fn_cb

def main():
    #  Decide what approach to use.
    use_class_callback = get_program_parameters()

    colors = vtkNamedColors()

    # Create a Cone
    cone = vtkConeSource(resolution=20)
    cone_mapper = vtkPolyDataMapper()
    cone >> cone_mapper
    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.color = colors.GetColor3d('BurlyWood')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('Blue'))
    renderer.AddActor(cone_actor)

    ren_win = vtkRenderWindow(window_name='BoxWidget')
    ren_win.AddRenderer(renderer)
    ren_win.SetWindowName('BoxWidget')

    # An interactor.
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = ren_win

    # A Box widget
    # We use a place_factor of 1.25 to make the box 1.25x larger than the actor.
    box_widget = vtkBoxWidget(interactor=interactor, prop3d=cone_actor, place_factor=1.25)
    box_widget.PlaceWidget()
    box_widget.On()

    # Set up and register the callback with the object that it is observing.
    if use_class_callback:
        box_widget.AddObserver('InteractionEvent', BoxCallback())
        # Or:
        # box_callback = BoxCallback()
        # box_widget.AddObserver('InteractionEvent', box_callback)
    else:
        box_widget.AddObserver('EndInteractionEvent', box_callback)

    # Start
    interactor.Initialize()
    ren_win.Render()
    interactor.Start()

class BoxCallback:
    def __call__(self, caller, ev):
        # Just do this to demonstrate who called callback and the event that triggered it.
        # print(caller.class_name, 'Event Id:', ev)
        t = vtkTransform()
        caller.GetTransform(t)
        caller.prop3d.user_transform = t

def box_callback(obj, event):
    t = vtkTransform()
    obj.GetTransform(t)
    obj.prop3d.user_transform = t

if __name__ == '__main__':
    main()
```
