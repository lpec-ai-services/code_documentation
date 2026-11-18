<!-- source: https://examples.vtk.org/site/Python/Modelling/Finance/ -->

# Finance

Repository source: [Finance](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Modelling/Finance.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestFinance.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Modelling/TestFinance.png?raw=true target=)

### Description

The first step is to choose dependent and independent variables. This choice is essentially a mapping from multidimensional data into an unstructured point dataset. This example chooses MONTHLY_PAYMENT, INTEREST_RATE, and LOAN_AMOUNT as (x, y, z) point coordinates, and TIME_LATE as a scalar value. This maps four of six variables. For now we will ignore the other two variables.

The example uses [vtkGaussianSplatter](https://www.vtk.org/doc/nightly/html/classvtkGaussianSplatter.html) to perform the splatting operation (i.e., conversion from unstructured points to volume dataset). This is followed by an isosurface extraction. We splat the data two times. The first time we splat the entire population. This is to show context and appears as gray/ wireframe in the figure. The second time we splat the data and scale it by the value of TIME_LATE . As a result, only payments that are late contribute to the second isosurface. The results of this visualization are interesting. First, we see that there is a strong correlation between the two independent variables MONTHLY_PAYMENT and LOAN_AMOUNT . (This is more evident when viewing the data interactively.) We see that the data falls roughly on a plane at a 45 degree angle between these two axes. With a little reflection this is evident: the monthly payment is strongly a function of loan amount (as well as interest rate and payment period). Second, we see that there is a clustering of delinquent accounts within the total population. The cluster tends to grow with larger interest rates and shrink with smaller monthly payments and loan amounts. Although the relationship with interest rate is expected, the clustering towards smaller monthly payments is not. Thus our visualization has provided a clue into the data. Further exploration may reveal the reason(s), or we may perform additional data analysis and acquisition to understand the phenomena.

One important note about multidimensional visualization. Because we tend to combine variables in odd ways (e.g., the use of MONTHLY_PAYMENT , INTEREST_RATE , and LOAN_AMOUNT as (x, y, z) coordinates), normalization of the data is usually required. To normalize data we simply adjust data values to lie between (0,1). Otherwise our data can be badly skewed and result in poor visualizations.

Info

See [Figure 9-50](../../VTKBook/09Chapter9.md#Figure%209-50) in [Chapter 9](../../VTKBook/09Chapter9.md) The [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Modelling/Finance/)), ([PythonicAPI](../../PythonicAPI/Modelling/Finance.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Finance.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkFloatArray,
    vtkPoints
)
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid
from vtkmodules.vtkFiltersCore import (
    vtkContourFilter,
    vtkTubeFilter
)
from vtkmodules.vtkFiltersGeneral import vtkAxes
from vtkmodules.vtkImagingHybrid import vtkGaussianSplatter
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    colors = vtkNamedColors()

    colors.SetColor('PopColor', [230, 230, 230, 255])

    fileName = get_program_parameters()

    keys = ['NUMBER_POINTS', 'MONTHLY_PAYMENT', 'INTEREST_RATE', 'LOAN_AMOUNT', 'TIME_LATE']

    # Read in the data and make an unstructured data set.
    dataSet = make_dataset(fileName, keys)

    # Construct the pipeline for the original population.
    popSplatter = vtkGaussianSplatter()
    popSplatter.SetInputData(dataSet)
    popSplatter.SetSampleDimensions(100, 100, 100)
    popSplatter.SetRadius(0.05)
    popSplatter.ScalarWarpingOff()

    popSurface = vtkContourFilter()
    popSurface.SetInputConnection(popSplatter.GetOutputPort())
    popSurface.SetValue(0, 0.01)

    popMapper = vtkPolyDataMapper()
    popMapper.SetInputConnection(popSurface.GetOutputPort())
    popMapper.ScalarVisibilityOff()

    popActor = vtkActor()
    popActor.SetMapper(popMapper)
    popActor.GetProperty().SetOpacity(0.3)
    popActor.GetProperty().SetColor(colors.GetColor3d('PopColor'))

    # Construct the pipeline for the delinquent population.
    lateSplatter = vtkGaussianSplatter()
    lateSplatter.SetInputData(dataSet)
    lateSplatter.SetSampleDimensions(50, 50, 50)
    lateSplatter.SetRadius(0.05)
    lateSplatter.SetScaleFactor(0.005)

    lateSurface = vtkContourFilter()
    lateSurface.SetInputConnection(lateSplatter.GetOutputPort())
    lateSurface.SetValue(0, 0.01)

    lateMapper = vtkPolyDataMapper()
    lateMapper.SetInputConnection(lateSurface.GetOutputPort())
    lateMapper.ScalarVisibilityOff()

    lateActor = vtkActor()
    lateActor.SetMapper(lateMapper)
    lateActor.GetProperty().SetColor(colors.GetColor3d('Red'))

    # Create axes.
    popSplatter.Update()
    bounds = popSplatter.GetOutput().GetBounds()

    axes = vtkAxes()
    axes.SetOrigin(bounds[0], bounds[2], bounds[4])
    axes.SetScaleFactor(popSplatter.GetOutput().GetLength() / 5)

    axesTubes = vtkTubeFilter()
    axesTubes.SetInputConnection(axes.GetOutputPort())
    axesTubes.SetRadius(axes.GetScaleFactor() / 25.0)
    axesTubes.SetNumberOfSides(6)

    axesMapper = vtkPolyDataMapper()
    axesMapper.SetInputConnection(axesTubes.GetOutputPort())

    axesActor = vtkActor()
    axesActor.SetMapper(axesMapper)

    # Graphics stuff.
    renderer = vtkRenderer()

    renWin = vtkRenderWindow()
    renWin.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renWin)

    # Set up the renderer.
    renderer.AddActor(lateActor)
    renderer.AddActor(axesActor)
    renderer.AddActor(popActor)
    renderer.SetBackground(colors.GetColor3d('Wheat'))
    renWin.SetSize(640, 480)
    renWin.SetWindowName('Finance')

    renderer.ResetCamera()
    renderer.GetActiveCamera().Dolly(1.3)
    renderer.ResetCameraClippingRange()

    # Interact with the data.
    renWin.Render()
    interactor.Start()

def get_program_parameters():
    import argparse
    description = 'Visualization of multidimensional financial data.'
    epilogue = '''
    The gray/wireframe surface represents the total data population.
    The red surface represents data points delinquent on loan payment.
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='financial.txt.')
    args = parser.parse_args()
    return args.filename

def normalise(maximum, minimum, x):
    return minimum + x / (maximum - minimum)

def read_file(filename):
    '''
    Read in the data set.
    :param filename:
    :return:
    '''
    res = dict()

    with open(filename) as ifn:
        k = ''
        v = list()
        for line in ifn:
            cl = ' '.join(line.split()).split()  # Clean the line.
            if cl:
                if len(cl) == 2 and cl[0] == 'NUMBER_POINTS':
                    k = cl[0]
                    v = [int(cl[1])]
                    has_key = True
                    continue
                if len(cl) == 1 and not has_key:
                    has_key = True
                    k = cl[0]
                    v = list()
                else:
                    v += map(float, cl)
            else:
                if has_key:
                    # Normalise the data.
                    minimum = min(v)
                    maximum = max(v)
                    # Emulate the bug in the C++ code.
                    for i in v:
                        if i > minimum:
                            maximum = i
                    if maximum != minimum:
                        res[k] = list(map(lambda x: minimum + x / (maximum - minimum), v))
                    else:
                        res[k] = v
                    has_key = False
    return res

def make_dataset(filename, keys):
    res = read_file(filename)
    if res:
        newPts = vtkPoints()
        newScalars = vtkFloatArray()
        xyz = list(zip(res[keys[1]], res[keys[2]], res[keys[3]]))
        for i in range(0, res[keys[0]][0]):
            # print(xyz[i])
            newPts.InsertPoint(i, xyz[i])
            newScalars.InsertValue(i, res[keys[4]][i])

        dataset = vtkUnstructuredGrid()
        dataset.SetPoints(newPts)
        dataset.GetPointData().SetScalars(newScalars)
        return dataset

if __name__ == '__main__':
    main()
```
