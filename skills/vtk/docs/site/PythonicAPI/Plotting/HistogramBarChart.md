<!-- source: https://examples.vtk.org/site/PythonicAPI/Plotting/HistogramBarChart/ -->

# HistogramBarChart

Repository source: [HistogramBarChart](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Plotting/HistogramBarChart.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestHistogramBarChart.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/PythonicAPI/Plotting/TestHistogramBarChart.png?raw=true target=)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Plotting/HistogramBarChart/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**HistogramBarChart.py**

```python
#!/usr/bin/env python3

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkIntArray
from vtkmodules.vtkCommonDataModel import vtkDataObject
from vtkmodules.vtkIOImage import vtkImageReader2Factory
from vtkmodules.vtkImagingCore import vtkImageExtractComponents
from vtkmodules.vtkImagingStatistics import vtkImageAccumulate
from vtkmodules.vtkRenderingAnnotation import vtkBarChartActor
from vtkmodules.vtkRenderingCore import (
    vtkRenderer,
    vtkRenderWindow,
    vtkRenderWindowInteractor
)

def get_program_parameters():
    import argparse
    description = 'Histogram Bar Chart.'
    epilogue = '''
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Pileated.jpg.')
    parser.add_argument('-i', '--ignore_zero', action='store_true', help='Ignore zero.')
    args = parser.parse_args()
    return args.filename, args.ignore_zero

def main():
    colors = vtkNamedColors()

    file_name, ignore_zero = get_program_parameters()

    # Read the image.
    reader = vtkImageReader2Factory().CreateImageReader2(file_name)
    reader.file_name = file_name

    num_components = reader.update().output.number_of_scalar_components
    print(f'Number of components {num_components}')
    if num_components > 3:
        print(f'Error: cannot process an image with {num_components} components!')
        return

    num_tuples = 54

    histogram_colors = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    red_frequencies = vtkIntArray(number_of_components=1, number_of_tuples=num_tuples)
    green_frequencies = vtkIntArray(number_of_components=1, number_of_tuples=num_tuples)
    blue_frequencies = vtkIntArray(number_of_components=1, number_of_tuples=num_tuples)

    # Process the image, extracting and bar charting a histogram for each component.
    for i in range(0, num_components):
        extract = vtkImageExtractComponents(components=i)

        histogram = vtkImageAccumulate(component_extent=(1, num_tuples + 1, 0, 0, 0, 0),
                                       component_origin=(0, 0, 0),
                                       component_spacing=(1, 0, 0),
                                       ignore_zero=ignore_zero)
        reader >> extract >> histogram
        output = histogram.update().output

        array = vtkIntArray(number_of_components=1, number_of_tuples=0)
        current_array = vtkIntArray(number_of_components=1, number_of_tuples=num_tuples)
        for j in range(0, num_tuples):
            frequency = int(output.point_data.scalars.GetTuple1(j))
            print(j, frequency)
            array.InsertTuple1(j, frequency)

        current_array.SetVoidArray(array, num_tuples, 1)

        if i == 0:
            red_frequencies.DeepCopy(current_array)
        elif i == 1:
            green_frequencies.DeepCopy(current_array)
        else:
            blue_frequencies.DeepCopy(current_array)

    data_object = vtkDataObject()
    if num_components == 1:
        data_object.field_data.AddArray(red_frequencies)
    else:
        rgb = list()
        all_frequencies = vtkIntArray(number_of_components=1)
        if num_components == 2:
            rgb.append(red_frequencies)
            rgb.append(green_frequencies)
        else:
            rgb.append(red_frequencies)
            rgb.append(green_frequencies)
            rgb.append(blue_frequencies)

        for i in range(0, num_tuples):
            for j in range(0, num_components):
                all_frequencies.InsertNextTuple1(rgb[j].GetTuple1(i))

        data_object.GetFieldData().AddArray(all_frequencies)

    # Create a vtkBarChartActor.
    bar_chart = vtkBarChartActor(input=data_object, title='Histogram', legend_visibility=False, label_visibility=False)
    bar_chart.position_coordinate.SetValue(0.15, 0.05, 0.0)
    bar_chart.position2_coordinate.SetValue(0.95, 0.85, 0.0)

    bar_chart.GetProperty().SetColor(1, 1, 1)

    # If the number of entries is not set to the number of data array
    # tuples, the bar chart actor will crash. The crash occurs whether the legend
    # and or labels are visible or not.
    bar_chart.GetLegendActor().SetNumberOfEntries(
        data_object.GetFieldData().GetArray(0).GetNumberOfTuples())

    count = 0
    for i in range(0, num_tuples):
        for j in range(0, num_components):
            bar_chart.SetBarColor(count, histogram_colors[j])
            count += 1

    # Visualize the histogram(s)
    named_colors = vtkNamedColors()

    renderer = vtkRenderer(background=named_colors.GetColor3d('SlateGray'))
    renderer.AddActor(bar_chart)

    render_window = vtkRenderWindow(size=(640, 480), window_name='HistogramBarChart')
    render_window.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.render_window = render_window

    render_window.Render()
    # Initialize the event loop and then start it.
    interactor.Initialize()
    interactor.Start()

if __name__ == '__main__':
    main()
```
