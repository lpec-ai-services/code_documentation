<!-- source: https://examples.vtk.org/site/PythonicAPI/PolyData/VertexConnectivity/ -->

# VertexConnectivity

Repository source: [VertexConnectivity](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/PolyData/VertexConnectivity.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestVertexConnectivity.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/PolyData/TestVertexConnectivity.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/PolyData/VertexConnectivity/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**VertexConnectivity.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkIdList,
    vtkIdTypeArray,
)
from vtkmodules.vtkCommonDataModel import (
    vtkSelection,
    vtkSelectionNode
)
from vtkmodules.vtkFiltersCore import (
    vtkExtractEdges,
    vtkTriangleFilter
)
from vtkmodules.vtkFiltersExtraction import vtkExtractSelection
from vtkmodules.vtkFiltersGeneral import vtkVertexGlyphFilter
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    sphere_source = vtkSphereSource()

    triangle_filter = vtkTriangleFilter()

    extract_edges = vtkExtractEdges()

    mesh = (sphere_source >> triangle_filter >> extract_edges).update().output
    connected_vertices = get_connected_vertices(mesh, 0)

    ids = vtkIdTypeArray(number_of_components=1)
    cv = list()
    for i in range(0, connected_vertices.GetNumberOfIds()):
        ids.InsertNextValue(connected_vertices.GetId(i))
        cv.append(connected_vertices.GetId(i))
    print('Connected vertices:', ', '.join(list(map(str, cv))))

    selection_node = vtkSelectionNode(field_type=vtkSelectionNode.POINT, content_type=vtkSelectionNode.INDICES,
                                      selection_list=ids)

    selection = vtkSelection()
    selection.AddNode(selection_node)

    extract_selection = vtkExtractSelection()
    extract_selection.SetInputData(1, selection)
    extract_edges >> extract_selection
    extract_selection.update()

    glyph_filter = vtkVertexGlyphFilter()

    connected_vertex_mapper = vtkDataSetMapper()
    extract_selection >> glyph_filter >> connected_vertex_mapper

    connected_vertex_actor = vtkActor(mapper=connected_vertex_mapper)
    connected_vertex_actor.property.color = colors.GetColor3d('Red')
    connected_vertex_actor.property.point_size = 5

    ids2 = vtkIdTypeArray(number_of_components=1)
    ids2.InsertNextValue(0)

    query_selection_node = vtkSelectionNode(field_type=vtkSelectionNode.POINT, content_type=vtkSelectionNode.INDICES,
                                            selection_list=ids2)

    query_selection = vtkSelection()
    query_selection.AddNode(query_selection_node)

    query_extract_selection = vtkExtractSelection()
    query_extract_selection.SetInputData(1, query_selection)
    extract_edges >> query_extract_selection
    query_extract_selection.update()

    query_glyph_filter = vtkVertexGlyphFilter()

    query_vertex_mapper = vtkDataSetMapper()
    query_extract_selection >> query_glyph_filter >> query_vertex_mapper

    query_vertex_actor = vtkActor(mapper=query_vertex_mapper)
    query_vertex_actor.property.color = colors.GetColor3d('Lime')
    query_vertex_actor.property.point_size = 5

    sphere_mapper = vtkDataSetMapper()
    extract_edges >> sphere_mapper
    sphere_actor = vtkActor(mapper=sphere_mapper)
    sphere_actor.property.color = colors.GetColor3d('Snow')

    # Create a renderer, render window, and interactor
    renderer = vtkRenderer(background=colors.GetColor3d('DarkSlateGray'))
    render_window = vtkRenderWindow(window_name='VertexConnectivity')
    render_window.AddRenderer(renderer)
    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    # Add the actors to the scene
    renderer.AddActor(sphere_actor)
    renderer.AddActor(query_vertex_actor)
    renderer.AddActor(connected_vertex_actor)

    render_window.Render()
    interactor.Start()

def get_connected_vertices(mesh, vertex_id):
    connected_vertices = vtkIdList()

    # Get all cells that vertex 'id' is a part of.
    cell_id_list = vtkIdList()
    mesh.GetPointCells(vertex_id, cell_id_list)

    # print("Vertex 0 is used in cells")
    # for i in range(0, cell_id_list.GetNumberOfIds()):
    #   print(f'id: {cell_id_list.GetId(i)}')
    for i in range(0, cell_id_list.GetNumberOfIds()):
        # print(f'id {i} : {cell_id_list.GetId(i)}')
        point_id_list = vtkIdList()
        mesh.GetCellPoints(cell_id_list.GetId(i), point_id_list)
        # print(f'End points are {point_id_list.GetId(0)} and {point_id_list.GetId(1)}')
        if point_id_list.GetId(0) != vertex_id:
            # print(f'Connected to {point_id_list.GetId(0)}')
            connected_vertices.InsertNextId(point_id_list.GetId(0))
        else:
            # print(f'Connected to {point_id_list.GetId(1)}')
            connected_vertices.InsertNextId(point_id_list.GetId(1))

    return connected_vertices

if __name__ == '__main__':
    main()
```
