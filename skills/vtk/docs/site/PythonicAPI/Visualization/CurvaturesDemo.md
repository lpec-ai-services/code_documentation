<!-- source: https://examples.vtk.org/site/PythonicAPI/Visualization/CurvaturesDemo/ -->

# CurvaturesDemo

Repository source: [CurvaturesDemo](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Visualization/CurvaturesDemo.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCurvaturesDemo.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Visualization/TestCurvaturesDemo.png?raw=true target=)

### Description

**How to get the Gaussian and Mean curvatures of a surface.**

Two different surfaces are used in this demonstration with each surface coloured according to its Gaussian and Mean curvatures.

- The first surface is a superquadric surface, this demonstrates the use of extra filters that are needed to get a nice smooth surface.
- The second surface is a parametric surface, in this case the surface has already been triangulated so no extra processing is necessary.

In order to get a nice coloured image, a [vtkDiscretizableColorTransferFunction](https://www.vtk.org/doc/nightly/html/classvtkDiscretizableColorTransferFunction.html) has been used to generate a set of colours for the vtkLookUp tables. For use with this particular lookup table, two options are provided:

- -c: Use a continuous color distribution instead of a discretized one.
- -r: Reverse the colors.

In the case of the Parametric Hills Gaussian Curvature surface, this colouration shows the nature of the surface quite nicely:

- The darker blue areas are saddle points (negative Gaussian curvature).
- The yellow to reddish areas have a positive Gaussian curvature (spherical).

For mean curvature, the colouration represents curvatures perpendicular to one of the principal axes.

Two other lookup table functions, using [vtkColorTransferFunction](https://www.vtk.org/doc/nightly/html/classvtkColorTransferFunction.html), are provided that generate a diverging color space. You can use either of these by editing the sections in the code using the lookup table. Comments in the code are provided.

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/CurvaturesDemo/)), ([Python](../../Python/Visualization/CurvaturesDemo.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**CurvaturesDemo.py**

```python
#!/usr/bin/env python3

import copy
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from vtk.util import numpy_support
from vtkmodules.numpy_interface import dataset_adapter as dsa
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import vtkParametricRandomHills
from vtkmodules.vtkCommonCore import (
    VTK_DOUBLE,
    vtkIdList,
    vtkLookupTable
)
from vtkmodules.vtkCommonTransforms import vtkTransform
from vtkmodules.vtkFiltersCore import (
    vtkCleanPolyData,
    vtkFeatureEdges,
    vtkGenerateIds,
    vtkTriangleFilter
)
from vtkmodules.vtkFiltersGeneral import (
    vtkCurvatures,
    vtkTransformFilter
)
from vtkmodules.vtkFiltersSources import (
    vtkParametricFunctionSource,
    vtkSuperquadricSource
)
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkInteractionWidgets import (

    vtkScalarBarRepresentation,
    vtkScalarBarWidget,
    vtkTextRepresentation,
    vtkTextWidget
)
from vtkmodules.vtkRenderingAnnotation import vtkScalarBarActor
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkColorTransferFunction,
    vtkDiscretizableColorTransferFunction,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkTextActor,
    vtkTextProperty
)

def get_program_parameters():
    import argparse
    description = 'Display the Gaussian and Mean curvatures of two surfaces adjusting for edge effects.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', '--continuous', action='store_true', help='Build a continuous colormap.')
    parser.add_argument('-r', '--reverse', action='store_true',
                        help='Reverse the colormap.')

    args = parser.parse_args()
    return args.continuous, args.reverse

def main(argv):
    continuous, reverse = get_program_parameters()
    discretize = not continuous

    colors = vtkNamedColors()

    # We are going to handle two different sources.
    # The first source is a superquadric source.
    torus = vtkSuperquadricSource(center=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0),
                                  phi_resolution=64,
                                  theta_resolution=64, theta_roundness=1,
                                  thickness=0.5, size=0.5, toroidal=True)

    # Rotate the torus towards the observer (around the x-axis)
    toroid_transform = vtkTransform()
    toroid_transform.RotateX(55)

    toroid_transform_filter = vtkTransformFilter(transform=toroid_transform)

    # The quadric is made of strips, so pass it through a triangle filter as
    # the curvature filter only operates on polys
    tri = vtkTriangleFilter()

    # The quadric has nasty discontinuities from the way the edges are generated
    # so let's pass it though a CleanPolyDataFilter and merge any points which
    # are coincident, or very close
    cleaner = vtkCleanPolyData(tolerance=0.005)

    torus >> toroid_transform_filter >> tri >> cleaner

    # The next source will be a parametric function.
    rh_fn_src = vtkParametricFunctionSource(parametric_function=vtkParametricRandomHills())

    sources = list()
    curvatures = dict()
    for i in range(0, 4):
        cc = vtkCurvatures()
        if i < 2:
            cc.input_connection = cleaner.output_port
        else:
            cc.input_connection = rh_fn_src.output_port
        if i % 2 == 0:
            cc.SetCurvatureTypeToGaussian()
            curvature_name = 'Gauss_Curvature'
        else:
            cc.SetCurvatureTypeToMean()
            curvature_name = 'Mean_Curvature'
        cc.update()
        adjust_edge_curvatures(cc.output, curvature_name)
        sources.append(cc.output)
        curvatures[i] = curvature_name

    # Create a common text property.
    # Position the source name according to its length.
    curvature_names = list(curvatures.values())
    curvature_names[:] = [x.replace('_', '\n') for x in curvature_names]

    txt = ['Torus', 'Torus', 'Parametric Surface', 'Parametric Surface']
    text_positions = get_text_positions(txt,
                                        justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                        vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_TOP,
                                        width=0.5)

    text_property = vtkTextProperty(color=colors.GetColor3d('AliceBlue'), bold=True, italic=True, shadow=True,
                                    font_size=12,
                                    # font_family_as_string='Courier',
                                    justification=TextProperty.Justification.VTK_TEXT_CENTERED,
                                    vertical_justification=TextProperty.VerticalJustification.VTK_TEXT_TOP)
    title_text_property = vtkTextProperty(color=colors.GetColor3d('AliceBlue'), bold=True, italic=True, shadow=True,
                                          font_size=16,
                                          justification=TextProperty.Justification.VTK_TEXT_LEFT)
    label_text_property = vtkTextProperty(color=colors.GetColor3d('AliceBlue'), bold=True, italic=False, shadow=True,
                                          font_size=12,
                                          justification=TextProperty.Justification.VTK_TEXT_LEFT)

    # RenderWindow Dimensions.
    renderer_size = 512
    grid_dimensions = 2
    window_width = renderer_size * grid_dimensions
    window_height = renderer_size * grid_dimensions

    # Create the RenderWindow and interactor.
    ren_win = vtkRenderWindow(
        size=(window_width, window_height),
        window_name=f'{Path(argv[0]).stem:s}')
    iren = vtkRenderWindowInteractor()
    iren.render_window = ren_win
    style = vtkInteractorStyleTrackballCamera()
    iren.interactor_style = style

    renderers = list()
    sb_properties = list()
    sb_widgets = list()
    text_widgets = list()

    for i in range(0, len(sources)):
        sbp = ScalarBarProperties
        sbp.orientation = True
        sbp.number_of_labels = 9
        sb_properties.append(sbp)

    # Link the pipeline together.
    for idx, source in enumerate(sources):
        curvature_name = curvatures[idx].replace('_', '\n')

        source.point_data.active_scalars = curvatures[idx]
        scalar_range = source.point_data.GetScalars(curvatures[idx]).range

        ctf = get_fast_ctf(discretize, reverse)
        sb_properties[idx].lut = rescale_ctf(ctf, *scalar_range)

        # Try different lookup tables.
        # sb_properties[idx].lut = get_diverging_lut()
        # sb_properties[idx].lut.range = scalar_range
        # sb_properties[idx].lut = get_diverging_lut1()
        # sb_properties[idx].lut.range = scalar_range

        mapper = vtkPolyDataMapper(input_data=source,
                                   scalar_mode=Mapper.ScalarMode.VTK_SCALAR_MODE_USE_POINT_FIELD_DATA,
                                   scalar_range=scalar_range,
                                   lookup_table=sb_properties[idx].lut,
                                   color_mode=Mapper.ColorMode.VTK_COLOR_MODE_MAP_SCALARS,
                                   interpolate_scalars_before_mapping=True
                                   )
        mapper.SelectColorArray(curvatures[idx])

        actor = vtkActor(mapper=mapper)

        ren = vtkRenderer()
        ren.AddActor(actor)
        renderers.append(ren)

        surface_name = curvature_name.replace('\n', ' ')
        text_actor = vtkTextActor(input=txt[idx], text_scale_mode=vtkTextActor.TEXT_SCALE_MODE_NONE,
                                  text_property=title_text_property)
        # Create the text representation. Used for positioning the text actor.
        text_rep = vtkTextRepresentation(enforce_normalized_viewport_bounds=True)
        text_rep.position_coordinate.value = text_positions[txt[idx]]['p']
        text_rep.position2_coordinate.value = text_positions[txt[idx]]['p2']

        text_widget = vtkTextWidget(representation=text_rep, text_actor=text_actor, interactor=iren,
                                    default_renderer=ren, current_renderer=ren,
                                    selectable=False)
        text_widgets.append(text_widget)

        sb_properties[idx].title_text = curvature_name + '\n'
        sbw = make_scalar_bar_widget(sb_properties[idx], title_text_property,
                                     label_text_property, ren, iren)
        sb_widgets.append(sbw)

    for idx in range(len(sources)):
        if idx < grid_dimensions * grid_dimensions:
            renderers.append(vtkRenderer)

    # Add and position the renders to the render window.
    viewport = list()
    for row in range(grid_dimensions):
        for col in range(grid_dimensions):
            idx = row * grid_dimensions + col

            viewport[:] = []
            viewport.append(float(col) / grid_dimensions)
            viewport.append(float(grid_dimensions - (row + 1)) / grid_dimensions)
            viewport.append(float(col + 1) / grid_dimensions)
            viewport.append(float(grid_dimensions - row) / grid_dimensions)

            if idx > (len(sources) - 1):
                continue

            renderers[idx].SetViewport(viewport)
            ren_win.AddRenderer(renderers[idx])

            renderers[idx].SetBackground(colors.GetColor3d('ParaViewBlueGrayBkg'))

    for sbw in sb_widgets:
        sbw.On()
    for tw in text_widgets:
        tw.On()

    # Share the cameras.
    renderers[1].active_camera = renderers[0].active_camera
    renderers[0].ResetCamera()
    renderers[3].active_camera = renderers[2].active_camera
    renderers[2].ResetCamera()

    ren_win.Render()

    iren.Start()

def get_diverging_lut():
    """
    See: [Diverging Color Maps for Scientific Visualization](https://www.kennethmoreland.com/color-maps/)
                       start point         midPoint            end point
     cool to warm:     0.230, 0.299, 0.754 0.865, 0.865, 0.865 0.706, 0.016, 0.150
     purple to orange: 0.436, 0.308, 0.631 0.865, 0.865, 0.865 0.759, 0.334, 0.046
     green to purple:  0.085, 0.532, 0.201 0.865, 0.865, 0.865 0.436, 0.308, 0.631
     blue to brown:    0.217, 0.525, 0.910 0.865, 0.865, 0.865 0.677, 0.492, 0.093
     green to red:     0.085, 0.532, 0.201 0.865, 0.865, 0.865 0.758, 0.214, 0.233

    :return:
    """
    ctf = vtkColorTransferFunction(color_space=ColorTransferFunction.ColorSpace.VTK_CTF_DIVERGING)
    # Cool to warm.
    ctf.AddRGBPoint(0.0, 0.230, 0.299, 0.754)
    ctf.AddRGBPoint(0.5, 0.865, 0.865, 0.865)
    ctf.AddRGBPoint(1.0, 0.706, 0.016, 0.150)

    table_size = 256
    lut = vtkLookupTable()
    lut.SetNumberOfTableValues(table_size)
    lut.Build()

    for i in range(0, table_size):
        rgba = list(ctf.GetColor(float(i) / table_size))
        rgba.append(1)
        lut.SetTableValue(i, rgba)

    return lut

def get_diverging_lut1():
    colors = vtkNamedColors()

    pts = list()
    pts.append([0.0] + list(colors.GetColor3d('MidnightBlue')))
    pts.append([0.5] + list(colors.GetColor3d('Gainsboro')))
    pts.append([1.0] + list(colors.GetColor3d('DarkOrange')))

    ctf = vtkColorTransferFunction(color_space=ColorTransferFunction.ColorSpace.VTK_CTF_DIVERGING)
    for pt in pts:
        ctf.AddRGBPoint(*pt)

    table_size = 256
    lut = vtkLookupTable(number_of_table_values=table_size)
    lut.Build()

    for i in range(0, table_size):
        rgba = list(ctf.GetColor(float(i) / table_size)) + [1.0]
        lut.SetTableValue(i, rgba)

    return lut

def get_fast_ctf(discretize=True, reverse=False):
    """
    Generate the color transfer function.

    name: Fast, creator: Francesca Samsel, and Alan W. Scott
    interpolationspace: Lab, space: rgb
    file name: Fast.json

    :param discretize: Selects whether the CTF is discretized or not.
    :param reverse: Reverse the colors in the CTF.
    :return: The color transfer function.
    """

    # The points and RGB values.
    pts_rgb = {
        0: (0.05639999999999999, 0.05639999999999999, 0.47),
        0.17159223942480895: (0.24300000000000013, 0.4603500000000004, 0.81),
        0.2984914818394138: (0.3568143826543521, 0.7450246485363142, 0.954367702893722),
        0.4321287371255907: (0.6882, 0.93, 0.9179099999999999),
        0.5: (0.8994959551205902, 0.944646394975174, 0.7686567142818399),
        0.5882260353170073: (0.957107977357604, 0.8338185108985666, 0.5089156299842102),
        0.7061412605695164: (0.9275207599610714, 0.6214389091739178, 0.31535705838676426),
        0.8476395308725272: (0.8, 0.3520000000000001, 0.15999999999999998),
        1: (0.59, 0.07670000000000013, 0.11947499999999994),
    }
    indices = sorted(list(pts_rgb.keys()))

    ctf = vtkDiscretizableColorTransferFunction(color_space=ColorTransferFunction.ColorSpace.VTK_CTF_LAB,
                                                scale=ColorTransferFunction.Scale.VTK_CTF_LINEAR,
                                                nan_color=(0.0, 1.0, 0.0),
                                                number_of_values=len(pts_rgb), discretize=discretize)
    if reverse:
        for index, (key, value) in enumerate(reversed(pts_rgb.items())):
            ctf.AddRGBPoint(indices[index], *value)
    else:
        for index in indices:
            ctf.AddRGBPoint(index, *pts_rgb[index])

    return ctf

def rescale(values, new_min=0, new_max=1):
    """
    Rescale the values.

    See: https://stats.stackexchange.com/questions/25894/changing-the-scale-of-a-variable-to-0-100

    :param values: The values to be rescaled.
    :param new_min: The new minimum value.
    :param new_max: The new maximum value.
    :return: The rescaled values.
    """
    res = list()
    old_min, old_max = min(values), max(values)
    for v in values:
        new_v = (new_max - new_min) / (old_max - old_min) * (v - old_min) + new_min
        # new_v1 = (new_max - new_min) / (old_max - old_min) * (v - old_max) + new_max
        res.append(new_v)
    return res

def rescale_ctf(old_ctf, new_min=0, new_max=1):
    """
    Rescale the color transfer function.

    :param old_ctf: The color transfer function to rescale.
    :param new_min: The new minimum value.
    :param new_max: The new maximum value.
    :return: A new rescaled color transfer function.
    """
    if new_min > new_max:
        r0 = new_max
        r1 = new_min
    else:
        r0 = new_min
        r1 = new_max

    xv = list()
    rgbv = list()
    nv = [0] * 6
    for i in range(0, old_ctf.GetNumberOfValues()):
        old_ctf.GetNodeValue(i, nv)
        x = nv[0]
        rgb = nv[1:4]
        xv.append(x)
        rgbv.append(rgb)
    xvr = rescale(xv, r0, r1)

    new_ctf = vtkDiscretizableColorTransferFunction(color_space=old_ctf.color_space, scale=old_ctf.scale,
                                                    nan_color=old_ctf.nan_color,
                                                    number_of_values=len(xvr), discretize=old_ctf.discretize
                                                    )
    new_ctf.below_range_color = old_ctf.below_range_color
    new_ctf.use_below_range_color = old_ctf.use_below_range_color
    new_ctf.above_range_color = old_ctf.above_range_color
    new_ctf.use_above_range_color = old_ctf.use_above_range_color

    for i in range(0, len(xvr)):
        new_ctf.AddRGBPoint(xvr[i], *rgbv[i])

    return new_ctf

def adjust_edge_curvatures(source, curvature_name, epsilon=1.0e-08):
    """
    This function adjusts curvatures along the edges of the surface by replacing
     the value with the average value of the curvatures of points in the neighborhood.

    Remember to update the vtkCurvatures object before calling this.

    :param source: A vtkPolyData object corresponding to the vtkCurvatures object.
    :param curvature_name: The name of the curvature, 'Gauss_Curvature' or 'Mean_Curvature'.
    :param epsilon: Absolute curvature values less than this will be set to zero.
    :return: The vtkPolyData object with the adjusted edge curvatures.
    """

    def point_neighbourhood(pt_id):
        """
        Find the ids of the neighbors of pt_id.

        :param pt_id: The point id.
        :return: The neighbour ids.
        """
        """
        Extract the topological neighbors for point pId. In two steps:
        1) source.GetPointCells(pt_id, cell_ids)
        2) source.GetCellPoints(cell_id, cell_point_ids) for all cell_id in cell_ids
        """
        cell_ids = vtkIdList()
        source.GetPointCells(pt_id, cell_ids)
        neighbour = set()
        for cell_idx in range(0, cell_ids.number_of_ids):
            cell_id = cell_ids.GetId(cell_idx)
            cell_point_ids = vtkIdList()
            source.GetCellPoints(cell_id, cell_point_ids)
            for cell_pt_idx in range(0, cell_point_ids.number_of_ids):
                neighbour.add(cell_point_ids.GetId(cell_pt_idx))
        return neighbour

    def compute_distance(pt_id_a, pt_id_b):
        """
        Compute the distance between two points given their ids.

        :param pt_id_a:
        :param pt_id_b:
        :return:
        """
        pt_a = np.array(source.GetPoint(pt_id_a))
        pt_b = np.array(source.GetPoint(pt_id_b))
        return np.linalg.norm(pt_a - pt_b)

    # Get the active scalars
    source.point_data.active_scalars = curvature_name
    np_source = dsa.WrapDataObject(source)
    curvatures = np_source.PointData[curvature_name]

    #  Get the boundary point IDs.
    array_name = 'ids'
    id_filter = vtkGenerateIds(input_data=source, point_ids=True, cell_ids=False,
                               point_ids_array_name=array_name, cell_ids_array_name=array_name)

    edges = vtkFeatureEdges(boundary_edges=True, manifold_edges=False,
                            non_manifold_edges=False, feature_edges=False)

    (source >> id_filter >> edges).update()

    edge_array = edges.output.point_data.GetArray(array_name)
    boundary_ids = []
    for i in range(edges.output.number_of_points):
        boundary_ids.append(edge_array.GetValue(i))
    # Remove duplicate Ids.
    p_ids_set = set(boundary_ids)

    # Iterate over the edge points and compute the curvature as the weighted
    # average of the neighbors.
    count_invalid = 0
    for p_id in boundary_ids:
        p_ids_neighbors = point_neighbourhood(p_id)
        # Keep only interior points.
        p_ids_neighbors -= p_ids_set
        # Compute distances and extract curvature values.
        curvs = [curvatures[p_id_n] for p_id_n in p_ids_neighbors]
        dists = [compute_distance(p_id_n, p_id) for p_id_n in p_ids_neighbors]
        curvs = np.array(curvs)
        dists = np.array(dists)
        curvs = curvs[dists > 0]
        dists = dists[dists > 0]
        if len(curvs) > 0:
            weights = 1 / np.array(dists)
            weights /= weights.sum()
            new_curv = np.dot(curvs, weights)
        else:
            # Corner case.
            count_invalid += 1
            # Assuming the curvature of the point is planar.
            new_curv = 0.0
        # Set the new curvature value.
        curvatures[p_id] = new_curv

    #  Set small values to zero.
    if epsilon != 0.0:
        curvatures = np.where(abs(curvatures) < epsilon, 0, curvatures)
        # Curvatures is now an ndarray
        curv = numpy_support.numpy_to_vtk(num_array=curvatures.ravel(),
                                          deep=True,
                                          array_type=VTK_DOUBLE)
        curv.name = curvature_name
        source.point_data.RemoveArray(curvature_name)
        source.point_data.AddArray(curv)
        source.point_data.active_scalars = curvature_name

class ScalarBarProperties:
    """
    The properties needed for scalar bars.
    """
    named_colors = vtkNamedColors()

    lut = None
    # These are in pixels
    maximum_dimensions = {'width': 100, 'height': 260}
    title_text = '',
    number_of_labels: int = 5
    label_format = '{:0.2f}'
    # Orientation vertical=True, horizontal=False.
    orientation: bool = True
    # Horizontal and vertical positioning.
    # These are the default positions, don't change these.
    default_v = {'p': (0.85, 0.2), 'p2': (0.1, 0.7)}
    default_h = {'p': (0.125, 0.05), 'p2': (0.75, 0.1)}
    # Modify these as needed.
    position_v = copy.deepcopy(default_v)
    position_h = copy.deepcopy(default_h)

def make_scalar_bar_widget(scalar_bar_properties, title_text_property, label_text_property, renderer,
                           interactor):
    """
    Make a scalar bar widget.

    :param scalar_bar_properties: The lookup table, title name, maximum dimensions in pixels and position.
    :param title_text_property: The properties for the title.
    :param label_text_property: The properties for the labels.
    :param renderer: The default renderer.
    :param interactor: The vtkInteractor.
    :return: The scalar bar widget.
    """
    sb_actor = vtkScalarBarActor(lookup_table=scalar_bar_properties.lut, title=scalar_bar_properties.title_text,
                                 unconstrained_font_size=True,
                                 number_of_labels=scalar_bar_properties.number_of_labels,
                                 title_text_property=title_text_property, label_text_property=label_text_property,
                                 label_format=scalar_bar_properties.label_format,
                                 )

    sb_rep = vtkScalarBarRepresentation(enforce_normalized_viewport_bounds=True,
                                        orientation=scalar_bar_properties.orientation)

    # Set the position.
    sb_rep.position_coordinate.SetCoordinateSystemToNormalizedViewport()
    sb_rep.position2_coordinate.SetCoordinateSystemToNormalizedViewport()
    if scalar_bar_properties.orientation:
        sb_rep.position_coordinate.value = scalar_bar_properties.position_v['p']
        sb_rep.position2_coordinate.value = scalar_bar_properties.position_v['p2']
    else:
        sb_rep.position_coordinate.value = scalar_bar_properties.position_h['p']
        sb_rep.position2_coordinate.value = scalar_bar_properties.position_h['p2']

    widget = vtkScalarBarWidget(representation=sb_rep, scalar_bar_actor=sb_actor, default_renderer=renderer,
                                interactor=interactor, enabled=True)

    return widget

def position_sbw_h(num_bands, max_bands):
    """
    Position the vertical scalar bar widget.
    :param: num_bands - the number of bands in the scalar bar.
    :param: max_bands - the maximum number of bands.
    :return: The scalar bar position.
    """

    max_bands = abs(max_bands)
    num_bands = abs(num_bands)
    if num_bands > max_bands:
        num_bands = max_bands
    if num_bands == 0:
        num_bands = 1
    # Origin of the scalar bar.
    xy0 = [0.125, 0.05]
    # Width and height of the scalar bar.
    dxy = [0.75, 0.1]
    if num_bands >= max_bands:
        return {'p': tuple(xy0), 'p2': tuple(dxy)}

    dx = dxy[0] - xy0[0] * num_bands / max_bands
    dxy[0] = dxy[0] * num_bands / max_bands
    if num_bands == 1:
        xy0[0] = 0.5 - dx * num_bands / (max_bands * 2)
    else:
        xy0[0] = 0.5 - dx * (num_bands + 1) / (max_bands * 2)
    return {'p': tuple(xy0), 'p2': tuple(dxy)}

def position_sbw_v(num_bands, max_bands):
    """
    Position the vertical scalar bar widget.
    :param: num_bands - the number of bands in the scalar bar.
    :param: max_bands - the maximum number of bands.
    :return: The scalar bar position.
    """

    max_bands = abs(max_bands)
    num_bands = abs(num_bands)
    if num_bands > max_bands:
        num_bands = max_bands
    if num_bands == 0:
        num_bands = 1
    # Origin of the scalar bar.
    xy0 = [0.9, 0.25]
    # Width and height of the scalar bar.
    dxy = [0.08, 0.5]
    if num_bands >= max_bands:
        return {'p': tuple(xy0), 'p2': tuple(dxy)}

    dy = dxy[1] - xy0[1] * num_bands / max_bands
    dxy[1] = dxy[1] * num_bands / max_bands
    if num_bands == 1:
        xy0[1] = 0.5 - dy * num_bands / (max_bands * 2)
    else:
        xy0[1] = 0.5 - dy * (num_bands + 1) / (max_bands * 2)
    return {'p': tuple(xy0), 'p2': tuple(dxy)}

def get_text_positions(names, justification=0, vertical_justification=0, width=0.96, height=0.1):
    """
    Get viewport positioning information for a list of names.

    :param names: The list of names.
    :param justification: Horizontal justification of the text, default is left.
    :param vertical_justification: Vertical justification of the text, default is bottom.
    :param width: Width of the bounding_box of the text in screen coordinates.
    :param height: Height of the bounding_box of the text in screen coordinates.
    :return: A dictionary of positioning information.
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
    if vertical_justification == TextProperty.VerticalJustification.VTK_TEXT_CENTERED:
        y0 = 0.5 - (dy / 2.0 + y0)

    name_len_min = 0
    name_len_max = 0
    first = True
    for k in names:
        sz = len(k)
        if first:
            name_len_max = sz
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
class ColorTransferFunction:
    @dataclass(frozen=True)
    class ColorSpace:
        VTK_CTF_RGB: int = 0
        VTK_CTF_HSV: int = 1
        VTK_CTF_LAB: int = 2
        VTK_CTF_DIVERGING: int = 3
        VTK_CTF_LAB_CIEDE2000: int = 4
        VTK_CTF_STEP: int = 5

    @dataclass(frozen=True)
    class Scale:
        VTK_CTF_LINEAR: int = 0
        VTK_CTF_LOG10: int = 1

@dataclass(frozen=True)
class Mapper:
    @dataclass(frozen=True)
    class ColorMode:
        VTK_COLOR_MODE_DEFAULT: int = 0
        VTK_COLOR_MODE_MAP_SCALARS: int = 1
        VTK_COLOR_MODE_DIRECT_SCALARS: int = 2

    @dataclass(frozen=True)
    class ResolveCoincidentTopology:
        VTK_RESOLVE_OFF: int = 0
        VTK_RESOLVE_POLYGON_OFFSET: int = 1
        VTK_RESOLVE_SHIFT_ZBUFFER: int = 2

    @dataclass(frozen=True)
    class ScalarMode:
        VTK_SCALAR_MODE_DEFAULT: int = 0
        VTK_SCALAR_MODE_USE_POINT_DATA: int = 1
        VTK_SCALAR_MODE_USE_CELL_DATA: int = 2
        VTK_SCALAR_MODE_USE_POINT_FIELD_DATA: int = 3
        VTK_SCALAR_MODE_USE_CELL_FIELD_DATA: int = 4
        VTK_SCALAR_MODE_USE_FIELD_DATA: int = 5

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
    import sys

    main(sys.argv)
```
