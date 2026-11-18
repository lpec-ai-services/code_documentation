<!-- source: https://examples.vtk.org/site/Python/Visualization/Blow/ -->

# Blow

Repository source: [Blow](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/Visualization/Blow.py)

[![figure](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestBlow.png?raw=true)](https://github.com/Kitware/vtk-examples/blob/gh-pages/src/Testing/Baseline/Python/Visualization/TestBlow.png?raw=true target=)

### Description

Extrusion blow molding process.

In the extrusion blow molding process, a material is extruded through an annular die to form a hollow cylinder. This cylinder is called a parison. Two mold halves are then closed on the parison, while at the same time the parison is inflated with air. Some of the parison material remains within the mold while some becomes waste material. The material is typically a polymer plastic softened with heat, but blow molding has been used to form metal parts. Plastic bottles are often manufactured using a blow molding process.

In this example the polymer was molded using an isothermal, nonlinear-elastic, incompressible (rubber-like) material. Triangular membrane finite elements were used to model the parison, while a combination of triangular and quadrilateral finite elements were used to model the mold. The mold surface is assumed to be rigid, and the parison is assumed to attach to the mold upon contact. Thus the thinning of the parison is controlled by its stretching during inflation and the sequence in which it contacts the mold.

Ten steps of the analysis are illustrated. The color of the parison indicates its thickness. Using a rainbow scale, red areas are thinnest while blue regions are thickest. Our visualization shows clearly one problem with the analysis technique we are using. Note that while the nodes (i.e., points) of the finite element mesh are prevented from passing through the mold, the interior of the triangular elements are not. This is apparent from the occlusion of the mold wireframe by the parison mesh.

You can also view the individual steps.

Info

See [Figure 12-17](../../VTKBook/12Chapter12.md#Figure%2012-17) in [Chapter 12](../../VTKBook/12Chapter12.md) the [VTK Textbook](../../VTKBook/01Chapter1.md).

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Visualization/Blow/)), ([PythonicAPI](../../PythonicAPI/Visualization/Blow.md))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**Blow.py**

```python
#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import vtkLookupTable
from vtkmodules.vtkFiltersCore import (
    vtkConnectivityFilter,
    vtkContourFilter,
    vtkPolyDataNormals
)
from vtkmodules.vtkFiltersGeneral import vtkWarpVector
from vtkmodules.vtkFiltersGeometry import vtkGeometryFilter
from vtkmodules.vtkIOLegacy import vtkDataSetReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkDataSetMapper,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    fileName, dataPoint = get_program_parameters()

    colors = vtkNamedColors()

    thickness = list()
    displacement = list()
    for i in range(0, 10):
        thickness.append('thickness' + str(i))
        displacement.append('displacement' + str(i))

    reader = list()
    warp = list()
    connect = list()
    mold = list()
    moldMapper = list()
    moldActor = list()
    connect2 = list()
    parison = list()
    normals2 = list()
    parisonMapper = list()
    parisonActor = list()
    cf = list()
    contourMapper = list()
    contours = list()
    ren = list()

    lut = vtkLookupTable()
    lut.SetHueRange(0.0, 0.66667)

    for i in range(0, 10):
        # Create the reader and warp the data vith vectors.
        reader.append(vtkDataSetReader())
        reader[i].SetFileName(fileName)
        reader[i].SetScalarsName(thickness[i])
        reader[i].SetVectorsName(displacement[i])
        reader[i].Update()

        warp.append(vtkWarpVector())
        warp[i].SetInputData(reader[i].GetUnstructuredGridOutput())

        # Extract the mold from the mesh using connectivity.
        connect.append(vtkConnectivityFilter())
        connect[i].SetInputConnection(warp[i].GetOutputPort())
        connect[i].SetExtractionModeToSpecifiedRegions()
        connect[i].AddSpecifiedRegion(0)
        connect[i].AddSpecifiedRegion(1)
        mold.append(vtkGeometryFilter())
        mold[i].SetInputConnection(connect[i].GetOutputPort())
        moldMapper.append(vtkDataSetMapper())
        moldMapper[i].SetInputConnection(mold[i].GetOutputPort())
        moldMapper[i].ScalarVisibilityOff()
        moldActor.append(vtkActor())
        moldActor[i].SetMapper(moldMapper[i])
        moldActor[i].GetProperty().SetColor(colors.GetColor3d("ivory_black"))
        moldActor[i].GetProperty().SetRepresentationToWireframe()

        # Extract the parison from the mesh using connectivity.
        connect2.append(vtkConnectivityFilter())
        connect2[i].SetInputConnection(warp[i].GetOutputPort())
        connect2[i].SetExtractionModeToSpecifiedRegions()
        connect2[i].AddSpecifiedRegion(2)
        parison.append(vtkGeometryFilter())
        parison[i].SetInputConnection(connect2[i].GetOutputPort())
        normals2.append(vtkPolyDataNormals())
        normals2[i].SetInputConnection(parison[i].GetOutputPort())
        normals2[i].SetFeatureAngle(60)
        parisonMapper.append(vtkPolyDataMapper())
        parisonMapper[i].SetInputConnection(normals2[i].GetOutputPort())
        parisonMapper[i].SetLookupTable(lut)
        parisonMapper[i].SetScalarRange(0.12, 1.0)
        parisonActor.append(vtkActor())
        parisonActor[i].SetMapper(parisonMapper[i])

        cf.append(vtkContourFilter())
        cf[i].SetInputConnection(connect2[i].GetOutputPort())
        cf[i].SetValue(0, 0.5)
        contourMapper.append(vtkPolyDataMapper())
        contourMapper[i].SetInputConnection(cf[i].GetOutputPort())
        contours.append(vtkActor())
        contours[i].SetMapper(contourMapper[i])

        ren.append(vtkRenderer())
        ren[i].AddActor(moldActor[i])
        ren[i].AddActor(parisonActor[i])
        ren[i].AddActor(contours[i])
        ren[i].SetBackground(colors.GetColor3d("AliceBlue"))
        ren[i].GetActiveCamera().SetPosition(50.973277, 12.298821, 29.102547)
        ren[i].GetActiveCamera().SetFocalPoint(0.141547, 12.298821, -0.245166)
        ren[i].GetActiveCamera().SetViewUp(-0.500000, 0.000000, 0.866025)
        ren[i].GetActiveCamera().SetClippingRange(36.640827, 78.614680)

    # Create the RenderWindow and RenderWindowInteractor.
    renWin = vtkRenderWindow()
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    rendererSizeX = 750
    rendererSizeY = 400
    renWinScale = 0.5
    renWin.SetWindowName("Blow")
    if 0 <= dataPoint < 10:
        renWin.AddRenderer(ren[dataPoint])
        renWin.SetSize(rendererSizeX, rendererSizeY)
    else:
        gridDimensionsX = 2
        gridDimensionsY = 5
        renWin.SetSize(int(rendererSizeX * gridDimensionsX * renWinScale),
                       int(rendererSizeY * gridDimensionsY * renWinScale))
        # Add and position the renders to the render window.
        viewPort = list()
        for row in range(0, gridDimensionsY):
            for col in range(0, gridDimensionsX):
                idx = row * gridDimensionsX + col
                x0 = float(col) / gridDimensionsX
                y0 = float(gridDimensionsY - row - 1) / gridDimensionsY
                x1 = float(col + 1) / gridDimensionsX
                y1 = float(gridDimensionsY - row) / gridDimensionsY
                viewPort[:] = []
                viewPort.append(x0)
                viewPort.append(y0)
                viewPort.append(x1)
                viewPort.append(y1)
                renWin.AddRenderer(ren[idx])
                ren[idx].SetViewport(viewPort)

    iren.Initialize()
    iren.Start()

def get_program_parameters():
    import argparse
    description = 'Produce figure 12-17 from the VTK Textbook.'
    epilogue = '''

        It is a translation of the original blow.tcl.

        data_point allows you to specify which frame is to be displayed.
        If data_point < 0 or data_point > 9 all ten frames are then displayed.

   '''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue)
    parser.add_argument('filename', help='blow.vtk')
    parser.add_argument('-d', '--data_point', default=-1, type=int, nargs='?',
                        help='The frame to display (0...9).')
    args = parser.parse_args()
    return args.filename, args.data_point

if __name__ == '__main__':
    main()
```
