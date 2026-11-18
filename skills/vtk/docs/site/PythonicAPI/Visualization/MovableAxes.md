<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/MovableAxes/ -->

# MovableAxes

Repository source: [MovableAxes](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/MovableAxes.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMovableAxes.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestMovableAxes.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/MovableAxes/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**MovableAxes.py**

```python
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import (
    vtkConeSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballActor
from vtkmodules.vtkRenderingAnnotation import vtkAxesActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer, vtkFollower, vtkAssembly, vtkPropCollection
)
from vtkmodules.vtkRenderingFreeType import vtkVectorText

def main():
    colors = vtkNamedColors()

    cone_source = vtkConeSource()

    # Create a mapper.
    cone_mapper = vtkPolyDataMapper()
    cone_source >> cone_mapper

    # Create an actor.
    cone_actor = vtkActor(mapper=cone_mapper)
    cone_actor.property.color = colors.GetColor3d('Gold')

    # A renderer and render window.
    renderer = vtkRenderer(background=colors.GetColor3d('SlateGray'))
    render_window = vtkRenderWindow(window_name='MovableAxes')
    render_window.AddRenderer(renderer)

    # An interactor.
    render_window_interactor = vtkRenderWindowInteractor()
    render_window_interactor.render_window = render_window

    # Add the actors to the scene.
    renderer.AddActor(cone_actor)

    # vtkAxesActor is currently not designed to work with
    # vtkInteractorStyleTrackballActor since it is a hybrid object containing
    # both vtkProp3D's and vtkActor2D's, the latter of which does not have a 3D
    # position that can be manipulated.
    axes = vtkAxesActor()

    # Get a copy of the axes' constituent 3D actors and put them into a
    # vtkAssembly so they can be manipulated as one prop.
    collection = vtkPropCollection()
    axes.GetActors(collection)

    collection.InitTraversal()

    movable_axes = vtkAssembly()

    for i in range(0, collection.GetNumberOfItems()):
        movable_axes.AddPart(collection.GetNextProp())

    renderer.AddActor(movable_axes)

    # Create our own labels that will follow and face the camera.
    x_text = vtkVectorText(text='X')
    x_text_mapper = vtkPolyDataMapper()
    x_text >> x_text_mapper
    # In order to get the position of the tips of the X, Y, and Z axes we do:
    #  "collection.GetItemAsObject(k).GetCenter()" where k = [3 ... 5].
    x_label = vtkFollower(mapper=x_text_mapper, scale=0.3, camera=renderer.active_camera,
                          position=collection.GetItemAsObject(3).GetCenter(), pickable=False)
    renderer.AddActor(x_label)

    y_text = vtkVectorText(text='Y')
    y_text_mapper = vtkPolyDataMapper()
    y_text >> y_text_mapper
    y_label = vtkFollower(mapper=y_text_mapper, scale=0.3, camera=renderer.active_camera,
                          position=collection.GetItemAsObject(4).GetCenter(), pickable=False)
    renderer.AddActor(y_label)

    z_text = vtkVectorText(text='Z')
    z_text_mapper = vtkPolyDataMapper()
    z_text >> z_text_mapper
    z_label = vtkFollower(mapper=z_text_mapper, scale=0.3, camera=renderer.active_camera,
                          position=collection.GetItemAsObject(5).GetCenter(), pickable=False)
    renderer.AddActor(z_label)

    # The custom callback to set the positions of the labels.
    callback = PositionCallback(x_label, y_label, z_label, movable_axes)

    renderer.ResetCamera()
    render_window.Render()

    style = vtkInteractorStyleTrackballActor()
    render_window_interactor.interactor_style = style
    style.AddObserver('InteractionEvent', callback)

    # Begin mouse interaction.
    render_window_interactor.Start()

class PositionCallback:
    def __init__(self, x_label, y_label, z_label, axes):
        self.x_label = x_label
        self.y_label = y_label
        self.z_label = z_label
        self.axes = axes
        self.followers = [self.x_label, self.y_label, self.z_label]

    def __call__(self, caller, ev):
        self.axes.InitPathTraversal()
        count = 0

        follower_id = -1
        path = self.axes.GetNextPath()
        while path:
            count += 1
            if count > 2:
                prop_3d = path.GetLastNode().GetViewProp()
                if prop_3d:
                    prop_3d.PokeMatrix(path.GetLastNode().GetMatrix())
                    self.followers[follower_id].SetPosition(prop_3d.GetCenter())
                    follower_id += 1
                    prop_3d.PokeMatrix(None)
            path = self.axes.GetNextPath()

if __name__ == '__main__':
    main()
```
