<!-- source: https://examples.vtk.org/site/Python/Graphs/SelectedVerticesAndEdges/ -->

# SelectedVerticesAndEdges

Repository source: [SelectedVerticesAndEdges](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Graphs/SelectedVerticesAndEdges.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestSelectedVerticesAndEdges.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Graphs/TestSelectedVerticesAndEdges.png?raw=true target=)

### Description

- Contributed by Eric Monson

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Graphs/SelectedVerticesAndEdges/)), ([PythonicAPI](../../PythonicAPI/Graphs/SelectedVerticesAndEdges.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SelectedVerticesAndEdges.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkInfovisCore import vtkRandomGraphSource
from vtkmodules.vtkViewsInfovis import vtkGraphLayoutView

source = vtkRandomGraphSource()
source.Update()

view = vtkGraphLayoutView()
view.AddRepresentationFromInputConnection(source.GetOutputPort())

def selectionCallback(caller, event):
    # In C++ there is some extra data passed to the callback, but in Python
    # the callback data is lost...

    # There should be two selection nodes, but which one is vertices and which
    # is edges does not seem to be guaranteed...
    sel = caller.GetCurrentSelection()
    node0 = sel.GetNode(0)
    node0_field_type = node0.GetFieldType()
    sel_list0 = caller.GetCurrentSelection().GetNode(0).GetSelectionList()
    node1 = sel.GetNode(1)
    node1_field_type = node1.GetFieldType()
    sel_list1 = caller.GetCurrentSelection().GetNode(1).GetSelectionList()

    if (sel_list0.GetNumberOfTuples() > 0):
        printFieldType(node0_field_type)
        for ii in range(sel_list0.GetNumberOfTuples()):
            print('\t', sel_list0.GetValue(ii))

    if (sel_list1.GetNumberOfTuples() > 0):
        printFieldType(node1_field_type)
        for ii in range(sel_list1.GetNumberOfTuples()):
            print('\t', sel_list1.GetValue(ii))

        print('- - -')

def printFieldType(field_type):
    if field_type == 3:
        print('Vertices Selected:')
    elif field_type == 4:
        print('Edges Selected:')
    else:
        print('Unknown type:')

def main():
    rep = view.GetRepresentation(0)

    # The vtkRenderedGraphRepresentation should already have a vtkAnnotationLink,
    # so we just want to grab it and add an observer with our callback function
    # attached
    link = rep.GetAnnotationLink()
    link.AddObserver('AnnotationChangedEvent', selectionCallback)

    view.GetRenderWindow().SetSize(600, 600)
    view.ResetCamera()
    view.Render()
    view.GetInteractor().Start()

if __name__ == '__main__':
    main()
```
