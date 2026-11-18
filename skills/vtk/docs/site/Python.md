<!-- source: https://examples.vtk.org/site/Python/ -->

# Python Examples

Please see [this page](https://www.vtk.org/Wiki/VTK/PythonDevelopment) to learn how to setup your environment to use VTK in Python.

It would be appreciated if there are any Python VTK experts who could convert any of the [c++ examples](https://examples.vtk.org/Cxx/) to Python!

## VTK Classes Summary

This Python script, [SelectExamples](Python/Utilities/SelectExamples.md), will let you select examples based on a VTK Class and language. It requires Python 3.7 or later. The following tables will produce similar information.

- [VTK Classes with Examples](Python/Coverage/PythonVTKClassesUsed.md), this table is really useful when searching for example(s) using a particular class.
- [VTK Classes with No Examples](Python/Coverage/PythonVTKClassesNotUsed.md), please add examples in your area of expertise!

## Tutorials

If you are new to VTK then these [tutorials](#tutorial) will help to get you started.

## Hello World

| Example Name | Description | Image |
| --- | --- | --- |
| [A hello world example](Python/GeometricObjects/CylinderExample.md) | Cylinder example from the VTK Textbook and source code. A hello world example. |  |
|  |  |  |

## Simple Operations

| Example Name | Description | Image |
| --- | --- | --- |
| [DistanceBetweenPoints](Python/SimpleOperations/DistanceBetweenPoints.md) |  |  |

## Input and Output

### Graph Formats

### 3D File Formats

#### Standard Formats

##### Input

| Example Name | Description | Image |
| --- | --- | --- |
| [CSVReadEdit](Python/IO/CSVReadEdit.md) | Read and edit a CSV file using pandas and numpy. |  |
|  |  |  |
| [CSVReadEdit1](Python/IO/CSVReadEdit1.md) | Read and edit a CSV file using pandas and [vtkDelimitedTextReader](https://www.vtk.org/doc/nightly/html/classvtkDelimitedTextReader.html). |  |
|  |  |  |
| [PolyDataToImageDataConverter](Python/IO/PolyDataToImageDataConverter.md) | Converts PolyData to binary LabelImage. |  |
| [ReadExodusData](Python/IO/ReadExodusData.md) | A simple script for reading and viewing ExodusII data interactively. |  |
|  |  |  |
| [ReadPLOT3D](Python/IO/ReadPLOT3D.md) | Read CFD (computational fluid dynamics) data produced by PLOT3D. |  |
|  |  |  |
| [ReadSLC](Python/IO/ReadSLC.md) | Read an SLC file. |  |
|  |  |  |
| [ReadSTL](Python/IO/ReadSTL.md) | Read an STL file. |  |
|  |  |  |
| [ReadUnstructuredGrid](Python/IO/ReadUnstructuredGrid.md) | Using [vtkUnstructuredGridReader](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGridReader.html) to read a (legacy) *.vtk file |  |
|  |  |  |
| [ReadVTP](Python/IO/ReadVTP.md) | Read a VTK XML PolyData file. |  |
|  |  |  |
| [TemporalHDFReader](Python/IO/TemporalHDFReader.md) | Read temporal data written inside a vtkhdf file. |  |

###### Importers

| Example Name | Description | Image |
| --- | --- | --- |
| [3DSImporter](Python/IO/3DSImporter.md) | Import a 3D Studio scene that includes multiple actors. |  |
|  |  |  |

##### Output

| Example Name | Description | Image |
| --- | --- | --- |
| [WritePLY](Python/IO/WritePLY.md) |  |  |
|  |  |  |
| [WriteSTL](Python/IO/WriteSTL.md) |  |  |
|  |  |  |

#### VTK Formats

##### Input

| Example Name | Description | Image |
| --- | --- | --- |
| [ReadImageData](Python/IO/ReadImageData.md) | Read an image data (.vti) file |  |
|  |  |  |
| [ReadPolyData](Python/IO/ReadPolyData.md) | Read a polygonal data (.vtp) file |  |
|  |  |  |

##### Output

#### Legacy VTK Formats

| Example Name | Description | Image |
| --- | --- | --- |
| [ReadLegacyUnstructuredGrid](Python/IO/ReadLegacyUnstructuredGrid.md) | Read an unstructured grid that contains 11 linear cells. |  |
|  |  |  |
| [WriteLegacyLinearCells](Python/IO/WriteLegacyLinearCells.md) | Write each linear cell into a legacy UnstructuredGrid file. |  |
| [WriteXMLLinearCells](Python/IO/WriteXMLLinearCells.md) | Write each linear cell into an XML UnstructuredGrid file (.vtu). |  |

### Image Format

#### Input

| Example Name | Description | Image |
| --- | --- | --- |
| [HDRReader](Python/IO/HDRReader.md) | Read a high-dynamic-range imaging file. |  |
|  |  |  |
| [ReadDICOM](Python/IO/ReadDICOM.md) | Read DICOM file. |  |
|  |  |  |
| [ReadDICOMSeries](Python/IO/ReadDICOMSeries.md) | This example demonstrates how to read a series of DICOM images and scroll through slices |  |
|  |  |  |

#### Output

| Example Name | Description | Image |
| --- | --- | --- |
| [ImageWriter](Python/IO/ImageWriter.md) | Write an imagefile based on the file extension. |  |
|  |  |  |

## Geometric Objects

| Example Name | Description | Image |
| --- | --- | --- |
| [Axes](Python/GeometricObjects/Axes.md) |  |  |
|  |  |  |
| [Circle](Python/GeometricObjects/Circle.md) | A disk is shown however this can be modified to show a circle. |  |
|  |  |  |
| [ColoredLines](Python/GeometricObjects/ColoredLines.md) |  |  |
|  |  |  |
| [Dodecahedron](Python/GeometricObjects/Dodecahedron.md) | Create a dodecahedron using [vtkPolyhedron](https://www.vtk.org/doc/nightly/html/classvtkPolyhedron.html). |  |
|  |  |  |
| [EllipticalCylinder](Python/GeometricObjects/EllipticalCylinder.md) | Create an elliptical cylinder using extrusion. |  |
|  |  |  |
| [EllipticalCylinderDemo](Python/GeometricObjects/EllipticalCylinderDemo.md) | Show the base and extrusion vector. |  |
|  |  |  |
| [GeometricObjectsDemo](Python/GeometricObjects/GeometricObjectsDemo.md) |  |  |
|  |  |  |
| [Planes](Python/GeometricObjects/Planes.md) | We create a convex hull of the planes for display purposes. |  |
|  |  |  |
| [PlanesIntersection](Python/GeometricObjects/PlanesIntersection.md) |  |  |
| [PolygonIntersection](Python/GeometricObjects/PolygonIntersection.md) | IntersectWithLine() |  |
| [SourceObjectsDemo](Python/GeometricObjects/SourceObjectsDemo.md) | Examples of source objects that procedurally generate polygonal models. These nine images represent just some of the capability of VTK. From upper left in reading order: sphere, cone, cylinder, cube, plane, text, random point cloud, disk (with or without hole), and line source. Other polygonal source objects are available; check subclasses of [vtkPolyDataAlgorithm](https://www.vtk.org/doc/nightly/html/classvtkPolyDataAlgorithm.html). |  |
|  |  |  |

### Cells

| Example Name | Description | Image |
| --- | --- | --- |
| [Cell3DDemonstration](Python/GeometricObjects/Cell3DDemonstration.md) | Sample objects are generated from the classes derived from [vtkCell3D](https://www.vtk.org/doc/nightly/html/classvtkCell3D.html) and displayed. |  |
|  |  |  |
| [CellTypeSource](Python/GeometricObjects/CellTypeSource.md) | Generate tessellated cells. |  |
|  |  |  |
| [ConvexPointSet](Python/GeometricObjects/ConvexPointSet.md) | Generate a ConvexPointSet cell. |  |
|  |  |  |
| [Hexahedron](Python/GeometricObjects/Hexahedron.md) |  |  |
|  |  |  |
| [LinearCellsDemo](Python/GeometricObjects/LinearCellsDemo.md) | Linear cell types found in VTK. The numbers define the ordering of the points making the cell. |  |
|  |  |  |
| [LongLine](Python/GeometricObjects/LongLine.md) | Manually create a polyline. |  |
|  |  |  |
| [Point](Python/GeometricObjects/Point.md) |  |  |
|  |  |  |
| [PolyLine](Python/GeometricObjects/PolyLine.md) |  |  |
|  |  |  |
| [Polygon](Python/GeometricObjects/Polygon.md) |  |  |
|  |  |  |
| [Polyhedron](Python/GeometricObjects/Polyhedron.md) | Create an unstructured grid representation of a polyhedron (cube) and write it out to a file. |  |
|  |  |  |
| [PolyhedronAndHexahedron](Python/GeometricObjects/PolyhedronAndHexahedron.md) | Create an unstructured grid representation of mixed cells, one polyhedron and one hexahedron. |  |
|  |  |  |
| [Pyramid](Python/GeometricObjects/Pyramid.md) |  |  |
|  |  |  |
| [Quad](Python/GeometricObjects/Quad.md) |  |  |
|  |  |  |
| [Tetrahedron](Python/GeometricObjects/Tetrahedron.md) |  |  |
|  |  |  |
| [Triangle](Python/GeometricObjects/Triangle.md) |  |  |
|  |  |  |
| [TriangleStrip](Python/GeometricObjects/TriangleStrip.md) |  |  |
|  |  |  |
| [Vertex](Python/GeometricObjects/Vertex.md) |  |  |
|  |  |  |

### Sources

| Example Name | Description | Image |
| --- | --- | --- |
| [Arrow](Python/GeometricObjects/Arrow.md) |  |  |
|  |  |  |
| [Cone](Python/GeometricObjects/Cone.md) |  |  |
|  |  |  |
| [Cube](Python/GeometricObjects/Cube.md) | Manually build a polygonal cube. |  |
|  |  |  |
| [Cube1](Python/GeometricObjects/Cube1.md) | A nice simple example that demonstrates the operation of the VTK pipeline. |  |
|  |  |  |
| [Cylinder](Python/GeometricObjects/Cylinder.md) |  |  |
|  |  |  |
| [Disk](Python/GeometricObjects/Disk.md) | A circle with a hole in it. |  |
|  |  |  |
| [EarthSource](Python/GeometricObjects/EarthSource.md) | Create the Earth. |  |
|  |  |  |
| [Frustum](Python/GeometricObjects/Frustum.md) |  |  |
|  |  |  |
| [Line](Python/GeometricObjects/Line.md) |  |  |
|  |  |  |
| [OrientedArrow](Python/GeometricObjects/OrientedArrow.md) | Orient an arrow along an arbitrary vector. |  |
|  |  |  |
| [OrientedCylinder](Python/GeometricObjects/OrientedCylinder.md) | Orient a cylinder along an arbitrary vector. |  |
|  |  |  |
| [Plane](Python/GeometricObjects/Plane.md) |  |  |
|  |  |  |
| [PlatonicSolids](Python/GeometricObjects/PlatonicSolids.md) | All five platonic solids are displayed. |  |
|  |  |  |
| [PolyLine1](Python/GeometricObjects/PolyLine1.md) | This example demonstrates how to create a polygon through several ordered points. |  |
|  |  |  |
| [RegularPolygonSource](Python/GeometricObjects/RegularPolygonSource.md) |  |  |
|  |  |  |
| [ShrinkCube](Python/GeometricObjects/ShrinkCube.md) | Applying shrink filter to an object. |  |
|  |  |  |
| [Sphere](Python/GeometricObjects/Sphere.md) |  |  |
|  |  |  |
| [TessellatedBoxSource](Python/GeometricObjects/TessellatedBoxSource.md) | Generate a box with tessellated sides. |  |
|  |  |  |
| [TextActor](Python/GeometricObjects/TextActor.md) | 2D "HUD-type" text |  |
|  |  |  |

### Non Linear

| Example Name | Description | Image |
| --- | --- | --- |
| [IsoparametricCellsDemo](Python/GeometricObjects/IsoparametricCellsDemo.md) | Nonlinear isoparametric cell types in VTK. |  |
|  |  |  |
| [QuadraticHexahedron](Python/GeometricObjects/QuadraticHexahedron.md) | Create and tessellate a nonlinear cell. |  |
|  |  |  |
| [QuadraticHexahedronDemo](Python/GeometricObjects/QuadraticHexahedronDemo.md) | Interactively adjust chord error. |  |
|  |  |  |
| [QuadraticTetra](Python/GeometricObjects/QuadraticTetra.md) | Create and tessellate a nonlinear cell. |  |
|  |  |  |
| [QuadraticTetraDemo](Python/GeometricObjects/QuadraticTetraDemo.md) | Interactively adjust chord error. |  |
|  |  |  |

### Parametric Objects

| Example Name | Description | Image |
| --- | --- | --- |
| [ParametricKuenDemo](Python/GeometricObjects/ParametricKuenDemo.md) | Interactively change the parameters for a Kuen Surface. |  |
|  |  |  |
| [ParametricObjectsDemo](Python/GeometricObjects/ParametricObjectsDemo.md) | Demonstrates the Parametric classes added by Andrew Maclean and additional classes added by Tim Meehan. The parametric spline is also included. Options are provided to display single objects, add backface, add normals and print out an image. |  |
|  |  |  |
| [ParametricSuperEllipsoidDemo](Python/GeometricObjects/ParametricSuperEllipsoidDemo.md) | Interactively change the parameters for a SuperEllipsoid Surface. |  |
|  |  |  |
| [ParametricSuperToroidDemo](Python/GeometricObjects/ParametricSuperToroidDemo.md) | Interactively change the parameters for a SuperToroid Surface. |  |
|  |  |  |

## Implicit Functions and Iso-surfaces

| Example Name | Description | Image |
| --- | --- | --- |
| [BooleanOperationImplicitFunctions](Python/ImplicitFunctions/BooleanOperationImplicitFunctions.md) | Demonstrate booleans of two different implicit functions |  |
|  |  |  |
| [ContourTriangulator](Python/Modelling/ContourTriangulator.md) | Create a contour from a structured point set (image) and triangulate it. |  |
|  |  |  |
| [CutWithScalars](Python/VisualizationAlgorithms/CutWithScalars.md) | Cut a surface with scalars. |  |
|  |  |  |
| [DiscreteMarchingCubes](Python/Modelling/DiscreteMarchingCubes.md) | Generate surfaces from labeled data. |  |
|  |  |  |
| [ExtractData](Python/VisualizationAlgorithms/ExtractData.md) | Implicit functions used to select data: Two ellipsoids are combined using the union operation used to select voxels from a volume. Voxels are shrunk 50 percent. |  |
|  |  |  |
| [ExtractLargestIsosurface](Python/Modelling/ExtractLargestIsosurface.md) | Extract largest isosurface. |  |
|  |  |  |
| [Hello](Python/VisualizationAlgorithms/Hello.md) | Implicit modelling used to thicken a stroked font. |  |
|  |  |  |
| [IceCream](Python/VisualizationAlgorithms/IceCream.md) | How to use boolean combinations of implicit functions to create a model of an ice cream cone. |  |
|  |  |  |
| [ImplicitQuadric](Python/ImplicitFunctions/ImplicitQuadric.md) | Create an ellipsoid using an implicit quadric |  |
|  |  |  |
| [ImplicitSphere](Python/ImplicitFunctions/ImplicitSphere.md) | Demonstrate sampling of a sphere implicit function |  |
|  |  |  |
| [ImplicitSphere1](Python/ImplicitFunctions/ImplicitSphere1.md) | Demonstrate sampling of a sphere implicit function |  |
|  |  |  |
| [Lorenz](Python/Visualization/Lorenz.md) | Visualizing a Lorenz strange attractor by integrating the Lorenz equations in a volume. |  |
|  |  |  |
| [MarchingCases](Python/VisualizationAlgorithms/MarchingCases.md) | Explore the Marching Cubes cases. |  |
|  |  |  |
| [MarchingCasesA](Python/VisualizationAlgorithms/MarchingCasesA.md) | The 256 possible cases have been reduced to 15 cases using symmetry. |  |
|  |  |  |
| [MarchingCasesB](Python/VisualizationAlgorithms/MarchingCasesB.md) | Marching cubes complementary cases. Cases 3c, 6c, 7c, 10c, 12c and 13c are displayed. |  |
|  |  |  |
| [MarchingCasesC](Python/VisualizationAlgorithms/MarchingCasesC.md) | Marching cubes, case 3 is rotated 90 degrees about the y-axis with no label. |  |
|  |  |  |
| [MarchingCasesD](Python/VisualizationAlgorithms/MarchingCasesD.md) | Marching cubes, case 7 is rotated 180 degrees about the y-axis with no label. |  |
|  |  |  |
| [MarchingCubes](Python/Modelling/MarchingCubes.md) | Create a voxelized sphere. |  |
|  |  |  |
| [SampleFunction](Python/ImplicitFunctions/SampleFunction.md) | Sample and visualize an implicit function. |  |
|  |  |  |
| [SmoothDiscreteMarchingCubes](Python/Modelling/SmoothDiscreteMarchingCubes.md) | Generate smooth surfaces from labeled data. |  |
|  |  |  |

## Working with 3D Data

| Example Name | Description | Image |
| --- | --- | --- |
| [AlignTwoPolyDatas](Python/PolyData/AlignTwoPolyDatas.md) | Align two [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html)'s. |  |
|  |  |  |
| [AppendFilter](Python/Filtering/AppendFilter.md) | Append different types of data, |  |
|  |  |  |
| [BooleanOperationPolyDataFilter](Python/PolyData/BooleanOperationPolyDataFilter.md) | This example performs a boolean operation (Intersection, Union, Difference) of two PolyData |  |
|  |  |  |
| [Bottle](Python/Modelling/Bottle.md) | Rotationally symmetric objects. |  |
|  |  |  |
| [CappedSphere](Python/Modelling/CappedSphere.md) | Rotate an arc to create a capped sphere. |  |
|  |  |  |
| [CellsInsideObject](Python/PolyData/CellsInsideObject.md) | Extract cells inside a closed surface. |  |
|  |  |  |
| [ColoredTriangle](Python/PolyData/ColoredTriangle.md) | Creates a file TriangleColored.vtp. |  |
| [CombinePolyData](Python/Filtering/CombinePolyData.md) | This example combines Polydata objects, and displays the result to the screen. |  |
|  |  |  |
| [ConnectivityFilter](Python/Filtering/ConnectivityFilter.md) | Color any dataset type based on connectivity. |  |
|  |  |  |
| [ExtractPolyLinesFromPolyData](Python/PolyData/ExtractPolyLinesFromPolyData.md) | Extract polylines from polydata. |  |
|  |  |  |
| [ExtractSelection](Python/PolyData/ExtractSelection.md) | Extract selected points. |  |
|  |  |  |
| [ExtractSelectionUsingCells](Python/PolyData/ExtractSelectionUsingCells.md) | Extract cell, select cell. |  |
|  |  |  |
| [FilledPolygon](Python/PolyData/FilledPolygon.md) |  |  |
|  |  |  |
| [Finance](Python/Modelling/Finance.md) | Visualization of multidimensional financial data. The gray/wireframe surface represents the total data population. The red surface represents data points delinquent on loan payment. |  |
|  |  |  |
| [FinanceFieldData](Python/Modelling/FinanceFieldData.md) | Visualization of multidimensional financial data. The yellow surface represents the total data population. The red surface represents data points delinquent on loan payment. |  |
|  |  |  |
| [Glyph2D](Python/Filtering/Glyph2D.md) |  |  |
|  |  |  |
| [Glyph3D](Python/Filtering/Glyph3D.md) |  |  |
|  |  |  |
| [ImplicitPolyDataDistance](Python/PolyData/ImplicitPolyDataDistance.md) |  |  |
|  |  |  |
| [IterateOverLines](Python/PolyData/IterateOverLines.md) | Iterate through the lines of a PolyData. |  |
| [IterativeClosestPoints](Python/Filtering/IterativeClosestPoints.md) |  |  |
| [LineOnMesh](Python/DataManipulation/LineOnMesh.md) |  |  |
|  |  |  |
| [MeshLabelImageColor](Python/DataManipulation/MeshLabelImageColor.md) |  |  |
|  |  |  |
| [Outline](Python/PolyData/Outline.md) |  |  |
|  |  |  |
| [PerlinNoise](Python/Filtering/PerlinNoise.md) |  |  |
|  |  |  |
| [PolyDataContourToImageData](Python/PolyData/PolyDataContourToImageData.md) |  |  |
| [PolyDataToImageDataStencil](Python/PolyData/PolyDataToImageDataStencil.md) |  |  |
|  |  |  |
| [RotationAroundLine](Python/PolyData/RotationAroundLine.md) |  |  |
|  |  |  |
| [RuledSurfaceFilter](Python/PolyData/RuledSurfaceFilter.md) |  |  |
|  |  |  |
| [SmoothMeshGrid](Python/PolyData/SmoothMeshGrid.md) |  |  |
|  |  |  |
| [SolidColoredTriangle](Python/PolyData/SolidColoredTriangle.md) | Writes out a file TriangleSolidColor.vtp. |  |
| [Spring](Python/Modelling/Spring.md) | Rotation in combination with linear displacement and radius variation. |  |
|  |  |  |
| [TransformPolyData](Python/Filtering/TransformPolyData.md) | Apply a Transformation to a PolyData. |  |
|  |  |  |
| [TriangleColoredPoints](Python/PolyData/TriangleColoredPoints.md) |  |  |
| [TriangleCornerVertices](Python/PolyData/TriangleCornerVertices.md) |  |  |
| [TriangleCorners](Python/PolyData/TriangleCorners.md) |  |  |
| [TriangulateTerrainMap](Python/Filtering/TriangulateTerrainMap.md) | Generate heights (z values) on a 10x10 grid (a terrain map) and then triangulate the points to form a surface. |  |
|  |  |  |
| [TubeFilter](Python/PolyData/TubeFilter.md) | Give lines a thickness (produce a cylinder around lines). |  |
|  |  |  |
| [VertexGlyphFilter](Python/Filtering/VertexGlyphFilter.md) | Add a vertex to each point. |  |
|  |  |  |
| [WarpTo](Python/Filtering/WarpTo.md) | Deform geometry by warping towards a point. |  |
|  |  |  |
| [WarpVector](Python/PolyData/WarpVector.md) | This example warps/deflects a line. |  |
|  |  |  |
| [WriteTriangleToFile](Python/IO/WriteTriangleToFile.md) |  |  |

### Data Types

| Example Name | Description | Image |
| --- | --- | --- |
| [CompositePolyDataMapper](Python/CompositeData/CompositePolyDataMapper.md) |  |  |
|  |  |  |
| [MultiBlockDataSet](Python/CompositeData/MultiBlockDataSet.md) | Demonstrates how to make and use VTK's MultiBlock type data |  |
|  |  |  |
| [OverlappingAMR](Python/CompositeData/OverlappingAMR.md) | Demonstrates how to create and populate a VTK's Overlapping AMR Grid type Data |  |
|  |  |  |

### Data Type Conversions

### Point Cloud Operations

| Example Name | Description | Image |
| --- | --- | --- |
| [PointSource](Python/PolyData/PointSource.md) | Generate a random point cloud. |  |
|  |  |  |

### Working with Meshes

This section includes examples of manipulating meshes.

| Example Name | Description | Image |
| --- | --- | --- |
| [BoundaryEdges](Python/Meshes/BoundaryEdges.md) | Find the edges that are used by only one face. |  |
|  |  |  |
| [ClosedSurface](Python/PolyData/ClosedSurface.md) | Check if a surface is closed. |  |
| [ColoredElevationMap](Python/Meshes/ColoredElevationMap.md) | Color a mesh by height. |  |
|  |  |  |
| [Decimation](Python/Meshes/Decimation.md) | Reduce the number of triangles in a mesh. |  |
|  |  |  |
| [DeformPointSet](Python/Meshes/DeformPointSet.md) | Use the [vtkDeformPointSet](https://www.vtk.org/doc/nightly/html/classvtkDeformPointSet.html) filter to deform a [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) with arbitrary polydata. |  |
|  |  |  |
| [DelaunayMesh](Python/Modelling/DelaunayMesh.md) | Two-dimensional Delaunay triangulation of a random set of points. Points and edges are shown highlighted with sphere glyphs and tubes. |  |
|  |  |  |
| [PointInterpolator](Python/Meshes/PointInterpolator.md) | Plot a scalar field of points onto a PolyData surface. |  |
|  |  |  |

#### Clipping

| Example Name | Description | Image |
| --- | --- | --- |
| [CapClip](Python/Meshes/CapClip.md) | Cap a clipped polydata with a polygon. |  |
|  |  |  |
| [ClipDataSetWithPolyData](Python/Meshes/ClipDataSetWithPolyData.md) | Clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with arbitrary polydata. In this example, use a [vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) to generate polydata to slice the grid, resulting in an unstructured grid. |  |
|  |  |  |
| [ClipDataSetWithPolyData1](Python/Meshes/ClipDataSetWithPolyData1.md) | Clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with arbitrary polydata. In this example, use a [vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) to generate polydata to slice the grid, resulting in an unstructured grid. |  |
|  |  |  |
| [SolidClip](Python/Meshes/SolidClip.md) | Create a "solid" clip. The "ghost" of the part clipped away is also shown. |  |
|  |  |  |

### Working with Structured 3D Data

This section includes [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html), [vtkExplicitStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkExplicitStructuredGrid.html), [vtkStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkStructuredGrid.html), [vtkStructuredPoints](https://www.vtk.org/doc/nightly/html/classvtkStructuredPoints.html) and [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html).

"ImageData" is not the traditional "flat, 2D image" you are used to. It is a special VTK data structure in the collection of 3D data structures provided by VTK. Image data can represent at typical 2D image, but also, a 3D volume.

#### [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [ImageWeightedSum](Python/ImageData/ImageWeightedSum.md) | Add two or more images. |  |
|  |  |  |

#### [vtkExplicitStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkExplicitStructuredGrid.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [CreateESGrid](Python/ExplicitStructuredGrid/CreateESGrid.md) | Create an explicit structured grid and convert this to an unstructured grid or vice versa. |  |
|  |  |  |
| [LoadESGrid](Python/ExplicitStructuredGrid/LoadESGrid.md) | Load a VTU file and convert the dataset to an explicit structured grid. |  |
|  |  |  |

#### [vtkStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkStructuredGrid.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [BlankPoint](Python/StructuredGrid/BlankPoint.md) | Blank a point of a [vtkStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkStructuredGrid.html). |  |
|  |  |  |
| [SGrid](Python/StructuredGrid/SGrid.md) | Creating a structured grid dataset of a semi-cylinder. Vectors are created whose magnitude is proportional to radius and oriented in tangential direction. |  |
|  |  |  |

#### [vtkStructuredPoints](https://www.vtk.org/doc/nightly/html/classvtkStructuredPoints.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [Vol](Python/StructuredPoints/Vol.md) | Creating a image data dataset. Scalar data is generated from the equation for a sphere. Volume dimensions are 26 x 26 x 26. |  |
|  |  |  |

#### [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [RGrid](Python/RectilinearGrid/RGrid.md) | Creating a rectilinear grid dataset. The coordinates along each axis are defined using an instance of [vtkDataArray](https://www.vtk.org/doc/nightly/html/classvtkDataArray.html). |  |
|  |  |  |
| [RectilinearGrid](Python/RectilinearGrid/RectilinearGrid.md) | Create a rectilinear grid. |  |
|  |  |  |
| [VisualizeRectilinearGrid](Python/RectilinearGrid/VisualizeRectilinearGrid.md) | Visualize the cells of a rectilinear grid. |  |
|  |  |  |

### Working with Unstructured 3D Data

This section includes [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html).

#### [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [ClipUnstructuredGridWithPlane](Python/UnstructuredGrid/ClipUnstructuredGridWithPlane.md) | Clip a UGrid with a plane. |  |
|  |  |  |
| [ClipUnstructuredGridWithPlane2](Python/UnstructuredGrid/ClipUnstructuredGridWithPlane2.md) | Clip a UGrid with a plane. |  |
|  |  |  |
| [UGrid](Python/UnstructuredGrid/UGrid.md) | Creation of an unstructured grid. |  |
|  |  |  |

### Registration

### Medical

| Example Name | Description | Image |
| --- | --- | --- |
| [GenerateCubesFromLabels](Python/Medical/GenerateCubesFromLabels.md) | Create cubes from labeled volume data. |  |
|  |  |  |
| [GenerateModelsFromLabels](Python/Medical/GenerateModelsFromLabels.md) | Create models from labeled volume data. |  |
| [MedicalDemo1](Python/Medical/MedicalDemo1.md) | Create a skin surface from volume data. |  |
|  |  |  |
| [MedicalDemo2](Python/Medical/MedicalDemo2.md) | Create a skin and bone surface from volume data. |  |
|  |  |  |
| [MedicalDemo3](Python/Medical/MedicalDemo3.md) | Create skin and tissue slices from volume data. |  |
|  |  |  |
| [MedicalDemo4](Python/Medical/MedicalDemo4.md) | Create a volume rendering. |  |
|  |  |  |
| [TissueLens](Python/Medical/TissueLens.md) | Cut a volume with a sphere. |  |
|  |  |  |

### Surface reconstruction

| Example Name | Description | Image |
| --- | --- | --- |
| [GaussianSplat](Python/Filtering/GaussianSplat.md) | Create a surface from Unorganized Points (Gaussian Splat). |  |
|  |  |  |

## Utilities

| Example Name | Description | Image |
| --- | --- | --- |
| [CheckVTKVersion](Python/Utilities/CheckVTKVersion.md) | Check the VTK version and provide alternatives for different VTK versions. |  |
| [JSONColorMapToLUT](Python/Utilities/JSONColorMapToLUT.md) | Take a JSON description of a colormap and convert it to a VTK colormap. |  |
|  |  |  |
| [ColorMapToLUT](Python/Utilities/ColorMapToLUT.md) | Use [vtkDiscretizableColorTransferFunction](https://www.vtk.org/doc/nightly/html/classvtkDiscretizableColorTransferFunction.html) to generate a VTK colormap. |  |
|  |  |  |
| [ColorNamePatches](Python/Utilities/ColorNamePatches.md) | Produce a HTML page called ColorNamePatches.html showing the available colors in [vtkNamedColors](https://www.vtk.org/doc/nightly/html/classvtkNamedColors.html). |  |
| [ColorSeriesPatches](Python/Utilities/ColorSeriesPatches.md) | Produce a HTML page called ColorSeriesPatches.html showing the available color series in [vtkColorSeries](https://www.vtk.org/doc/nightly/html/classvtkColorSeries.html). |  |
| [ConstrainedDelaunay2D](Python/Filtering/ConstrainedDelaunay2D.md) | Perform a 2D Delaunay triangulation on a point set respecting a specified boundary. |  |
|  |  |  |
| [Delaunay2D](Python/Filtering/Delaunay2D.md) |  |  |
|  |  |  |
| [LUTUtilities](Python/Utilities/LUTUtilities.md) | A utility class for [vtkLookupTable](https://www.vtk.org/doc/nightly/html/classvtkLookupTable.html) allowing you to output the table contents or to compare tables. |  |
| [MultipleRenderWindows](Python/Visualization/MultipleRenderWindows.md) | Multiple Render Windows. |  |
|  |  |  |
| [MultipleViewports](Python/Visualization/MultipleViewports.md) | Multiple Viewports. |  |
|  |  |  |
| [RescaleReverseLUT](Python/Utilities/RescaleReverseLUT.md) | Demonstrate how to adjust a colormap so that the colormap scalar range matches the scalar range on the object. You can optionally reverse the colors. |  |
|  |  |  |
| [ResetCameraOrientation](Python/Utilities/ResetCameraOrientation.md) | Reset camera orientation to a previously saved orientation. |  |
|  |  |  |
| [SaveSceneToFieldData](Python/Utilities/SaveSceneToFieldData.md) | Save a [vtkCamera](https://www.vtk.org/doc/nightly/html/classvtkCamera.html)'s state in a [vtkDataSet](https://www.vtk.org/doc/nightly/html/classvtkDataSet.html)'s [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html) and restore it. |  |
|  |  |  |
| [SaveSceneToFile](Python/Utilities/SaveSceneToFile.md) | Save a [vtkCamera](https://www.vtk.org/doc/nightly/html/classvtkCamera.html)'s state in a file and restore it. |  |
|  |  |  |
| [SelectExamples](Python/Utilities/SelectExamples.md) | Given a VTK Class and a language, select the matching examples. |  |
| [Screenshot](Python/Utilities/Screenshot.md) |  |  |
|  |  |  |
| [ShareCamera](Python/Utilities/ShareCamera.md) | Share a camera between multiple renderers. |  |
|  |  |  |
| [VTKImportsForPython](Python/Utilities/VTKImportsForPython.md) | Generate import statements for the VTK classes in your Python code. |  |
| [VTKModulesForCxx](Python/Utilities/VTKModulesForCxx.md) | Generate a find_package(VTK COMPONENTS ...) command for CMake. |  |
| [VTKWithNumpy](Python/Utilities/VTKWithNumpy.md) |  |  |
|  |  |  |
| [Variant](Python/Utilities/Variant.md) |  |  |
| [XMLColorMapToLUT](Python/Utilities/XMLColorMapToLUT.md) | Take an XML description of a colormap and convert it to a VTK colormap. |  |
|  |  |  |

### Arrays

| Example Name | Description | Image |
| --- | --- | --- |
| [GetValues](Python/Arrays/GetValues.md) |  |  |
| [RenameArray](Python/Arrays/RenameArray.md) |  |  |

### Events

## Math Operations

## Graphs

| Example Name | Description | Image |
| --- | --- | --- |
| [ColorEdges](Python/Graphs/ColorEdges.md) | Color edges. |  |
|  |  |  |
| [ColorVertexLabels](Python/Graphs/ColorVertexLabels.md) | Set the color of vertex labels. |  |
|  |  |  |
| [ColorVerticesLookupTable](Python/Graphs/ColorVerticesLookupTable.md) | Color vertices. |  |
|  |  |  |
| [ConstructGraph](Python/Graphs/ConstructGraph.md) | Construct a graph. |  |
|  |  |  |
| [ConstructTree](Python/Graphs/ConstructTree.md) | Construct a tree. |  |
|  |  |  |
| [CreateTree](Python/Graphs/CreateTree.md) | Create a tree and label the vertices and edges. |  |
|  |  |  |
| [EdgeWeights](Python/Graphs/EdgeWeights.md) |  |  |
|  |  |  |
| [GraphToPolyData](Python/Graphs/GraphToPolyData.md) | Convert a graph to a PolyData. |  |
|  |  |  |
| [LabelVerticesAndEdges](Python/Graphs/LabelVerticesAndEdges.md) | Label vertices and edges. |  |
|  |  |  |
| [NOVCAGraph](Python/Graphs/NOVCAGraph.md) |  |  |
| [RandomGraphSource](Python/Graphs/RandomGraphSource.md) | Create a random graph. |  |
|  |  |  |
| [ScaleVertices](Python/Graphs/ScaleVertices.md) | Size/scale vertices based on a data array. |  |
|  |  |  |
| [SelectedVerticesAndEdges](Python/Graphs/SelectedVerticesAndEdges.md) |  |  |
|  |  |  |
| [SideBySideGraphs](Python/Graphs/SideBySideGraphs.md) | Display two graphs side by side. |  |
|  |  |  |
| [VisualizeDirectedGraph](Python/Graphs/VisualizeDirectedGraph.md) | Visualize a directed graph. |  |
|  |  |  |
| [VisualizeGraph](Python/Graphs/VisualizeGraph.md) |  |  |
|  |  |  |

### Graph Conversions

## Data Structures

### Timing Demonstrations

### KD-Tree

### Oriented Bounding Box (OBB) Tree

### Octree

### Modified BSP Tree

### HyperTreeGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [HyperTreeGridSource](Python/HyperTreeGrid/HyperTreeGridSource.md) | Create a [vtkHyperTreeGrid](https://www.vtk.org/doc/nightly/html/classvtkHyperTreeGrid.html). |  |
|  |  |  |

## VTK Concepts

## Rendering

| Example Name | Description | Image |
| --- | --- | --- |
| [AmbientSpheres](Python/Rendering/AmbientSpheres.md) | Demonstrates the effect of ambient lighting on spheres. |  |
|  |  |  |
| [CameraBlur](Python/Rendering/CameraBlur.md) | Example of a scene rendered with focal depth. |  |
|  |  |  |
| [ColoredSphere](Python/Rendering/ColoredSphere.md) | A simple sphere. |  |
|  |  |  |
| [Cone3](Python/Rendering/Cone3.md) | Four frames of output, based on the VTK example Cone3.py. |  |
|  |  |  |
| [Cone4](Python/Rendering/Cone4.md) | Modifying properties and transformation matrix based on the VTK example Cone4.py. |  |
|  |  |  |
| [DiffuseSpheres](Python/Rendering/DiffuseSpheres.md) | Demonstrates the effect of diffuse lighting on spheres. |  |
|  |  |  |
| [FlatVersusGouraud](Python/Rendering/FlatVersusGouraud.md) | Flat and Gouraud shading. Different shading methods can dramatically improve the look of an object represented with polygons. On the top, flat shading uses a constant surface normal across each polygon. On the bottom, Gouraud shading interpolates normals from polygon vertices to give a smoother look. |  |
|  |  |  |
| [GradientBackground](Python/Rendering/GradientBackground.md) | Demonstrates the background shading options. |  |
|  |  |  |
| [LayeredActors](Python/Rendering/LayeredActors.md) | Demonstrates the use of two linked renderers. The orientation of objects in the non active layer is linked to those in the active layer. |  |
|  |  |  |
| [Mace](Python/Rendering/Mace.md) | An example of multiple inputs and outputs. |  |
|  |  |  |
| [Model](Python/Rendering/Model.md) | Illustrative diagram of graphics objects. |  |
|  |  |  |
| [MotionBlur](Python/Rendering/MotionBlur.md) | Example of motion blur. |  |
|  |  |  |
| [OutlineGlowPass](Python/Rendering/OutlineGlowPass.md) | Demonstrates how to render a object in a scene with a glowing outline. |  |
|  |  |  |
| [PBR_Anisotropy](Python/Rendering/PBR_Anisotropy.md) | Render spheres with different anisotropy values. |  |
|  |  |  |
| [PBR_Clear_Coat](Python/Rendering/PBR_Clear_Coat.md) | Render a cube with custom texture mapping and a coat normal texture. |  |
|  |  |  |
| [PBR_Edge_Tint](Python/Rendering/PBR_Edge_Tint.md) | Render spheres with different edge colors using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_HDR_Environment](Python/Rendering/PBR_HDR_Environment.md) | Renders spheres with different materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Mapping](Python/Rendering/PBR_Mapping.md) | Render a cube with custom texture mapping. |  |
|  |  |  |
| [PBR_Materials](Python/Rendering/PBR_Materials.md) | Renders spheres with different materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Materials_Coat](Python/Rendering/PBR_Materials_Coat.md) | Render spheres with different coat materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Skybox](Python/Rendering/PBR_Skybox.md) | Demonstrates physically based rendering, a skybox and image based lighting. |  |
|  |  |  |
| [PBR_Skybox_Texturing](Python/Rendering/PBR_Skybox_Texturing.md) | Demonstrates physically based rendering, a skybox, image based lighting and texturing. |  |
|  |  |  |
| [PBR_Skybox_Anisotropy](Python/Rendering/PBR_Skybox_Anisotropy.md) | Demonstrates physically based rendering, a skybox, image based lighting, and anisotropic texturing. |  |
|  |  |  |
| [Rainbow](Python/Rendering/Rainbow.md) | Use and manipulation of vtkLookupTables. |  |
|  |  |  |
| [Rotations](Python/Rendering/Rotations.md) | Rotations of a cow about her axes. |  |
|  |  |  |
| [RotationsA](Python/Rendering/RotationsA.md) | Perform six rotations of a cow about her x-axis (Figure 3-31a). |  |
|  |  |  |
| [RotationsB](Python/Rendering/RotationsB.md) | Perform six rotations of a cow about her y-axis (Figure 3-31b). |  |
|  |  |  |
| [RotationsC](Python/Rendering/RotationsC.md) | Perform six rotations of a cow about her z-axis (Figure 3-31c). |  |
|  |  |  |
| [RotationsD](Python/Rendering/RotationsD.md) | First a rotation of a cow about her x-axis, then six rotations about her y-axis (Figure 3-31d). |  |
|  |  |  |
| [Shadows](Python/Rendering/Shadows.md) | Draw model with shadows. |  |
|  |  |  |
| [SpecularSpheres](Python/Rendering/SpecularSpheres.md) | Demonstrates the effect of specular lighting on spheres. |  |
|  |  |  |
| [StippledLine](Python/Rendering/StippledLine.md) | Draw a stippled line. |  |
|  |  |  |
| [StripFran](Python/Rendering/StripFran.md) | Triangle strip examples. (a) Structured triangle mesh consisting of 134 strips each of 390 triangles. (b) Unstructured triangle mesh consisting of 2227 strips of average length 3.94, longest strip 101 triangles. Images are generated by displaying every other triangle strip. |  |
|  |  |  |
| [TransformSphere](Python/Rendering/TransformSphere.md) | The addition of a transform filter to [ColoredSphere](Python/Rendering/ColoredSphere.md). |  |
|  |  |  |
| [TransparentBackground](Python/Rendering/TransparentBackground.md) | Demonstrates the use of two renderers. Notice that the second (and subsequent) renderers will have a transparent background. |  |
|  |  |  |
| [WalkCow](Python/Rendering/WalkCow.md) | This generates Figs. 3-32, 3-33 found in VTKTextbook.pdf. |  |
|  |  |  |
| [WalkCowA](Python/Rendering/WalkCowA.md) | This generates Fig. 3-33a found in VTKTextbook.pdf. |  |
|  |  |  |
| [WalkCowB](Python/Rendering/WalkCowB.md) | This generates Fig. 3-33b found in VTKTextbook.pdf. |  |
|  |  |  |

## Lighting

| Example Name | Description | Image |
| --- | --- | --- |
| [ShadowsLightsDemo](Python/Visualization/ShadowsLightsDemo.md) | Show lights casting shadows. |  |
|  |  |  |

## Texture Mapping

| Example Name | Description | Image |
| --- | --- | --- |
| [AnimateVectors](Python/Texture/AnimateVectors.md) | One frame from a vector field animation using texture maps. |  |
|  |  |  |
| [TextureCutQuadric](Python/Texture/TextureCutQuadric.md) | Cut a quadric with boolean textures. |  |
|  |  |  |
| [TextureCutSphere](Python/Texture/TextureCutSphere.md) | Examples of texture thresholding. (b) Boolean combination of two planes to cut nested spheres. |  |
|  |  |  |
| [TexturePlane](Python/Texture/TexturePlane.md) | Example of texture mapping. |  |
|  |  |  |
| [TextureThreshold](Python/Texture/TextureThreshold.md) | Demonstrate the use of scalar thresholds to show values of flow density on three planes. |  |
|  |  |  |

## Tutorial

If you are new to VTK then these tutorials will help to get you started.

| Tutorial | Description | Image |
| --- | --- | --- |
| [Step 1](Python/Tutorial/Tutorial_Step1.md) | Create a cone, render it and rotate it through 360°. |  |
|  |  |  |
| [Step 2](Python/Tutorial/Tutorial_Step2.md) | Adding an observer. |  |
|  |  |  |
| [Step 3](Python/Tutorial/Tutorial_Step3.md) | Using multiple renderers within a render window. |  |
|  |  |  |
| [Step 4](Python/Tutorial/Tutorial_Step4.md) | The creation of multiple actors and the manipulation of their properties and transformations. |  |
|  |  |  |
| [Step 5](Python/Tutorial/Tutorial_Step5.md) | Introducing the concept of interaction. |  |
|  |  |  |
| [Step 6](Python/Tutorial/Tutorial_Step6.md) | Using a 3D widget. |  |
|  |  |  |

## Visualization

See [this tutorial](http://www.vtk.org/Wiki/VTK/Tutorials/3DDataTypes) for a brief explanation of the VTK terminology of mappers, actors, etc.

| Example Name | Description | Image |
| --- | --- | --- |
| [AlphaFrequency](Python/Visualization/AlphaFrequency.md) | Linearly extrude fonts to show letter frequencies in text. |  |
|  |  |  |
| [AnatomicalOrientation](Python/VisualizationAlgorithms/AnatomicalOrientation.md) | Show a labelled set of anatomical planes transecting a human figure. |  |
|  |  |  |
| [AnnotatedCubeActor](Python/Visualization/AnnotatedCubeActor.md) | Annotated cube. |  |
|  |  |  |
| [AssignCellColorsFromLUT](Python/Visualization/AssignCellColorsFromLUT.md) | Demonstrates how to assign colors to cells in a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) structure using lookup tables. |  |
|  |  |  |
| [BillboardTextActor3D](Python/Visualization/BillboardTextActor3D.md) | Label points with billboards. |  |
|  |  |  |
| [BlobbyLogo](Python/Visualization/BlobbyLogo.md) | A logo created with [vtkImplicitModeller](https://www.vtk.org/doc/nightly/html/classvtkImplicitModeller.html). |  |
|  |  |  |
| [Blow](Python/Visualization/Blow.md) | Ten frames from a blow molding finite element analysis. |  |
|  |  |  |
| [BluntStreamlines](Python/VisualizationAlgorithms/BluntStreamlines.md) | Demonstrates airflow around a blunt fin using streamlines. |  |
|  |  |  |
| [Camera](Python/Visualization/Camera.md) | Positioning and aiming the camera. |  |
|  |  |  |
| [CameraModel1](Python/Visualization/CameraModel1.md) | Illustrate camera movement around the focal point. |  |
|  |  |  |
| [CameraModel2](Python/Visualization/CameraModel2.md) | camera movement centered at the camera position. |  |
|  |  |  |
| [CarotidFlow](Python/VisualizationAlgorithms/CarotidFlow.md) | Visualizing blood flow in the human carotid arteries. Streamtubes of flow velocity are generated. |  |
|  |  |  |
| [CarotidFlowGlyphs](Python/VisualizationAlgorithms/CarotidFlowGlyphs.md) | Visualizing blood flow in human carotid arteries. Cone glyphs indicate flow direction and magnitude. |  |
|  |  |  |
| [ClampGlyphSizes](Python/Visualization/ClampGlyphSizes.md) | Use [vtkGlyph3D](https://www.vtk.org/doc/nightly/html/classvtkGlyph3D.html) with ClampingOn to limit glyph sizes |  |
|  |  |  |
| [ClipSphereCylinder](Python/VisualizationAlgorithms/ClipSphereCylinder.md) | A plane clipped with a sphere and an ellipse. The two transforms place each implicit function into the appropriate position. Two outputs are generated by the clipper. |  |
|  |  |  |
| [CollisionDetection](Python/Visualization/CollisionDetection.md) | Collison between two spheres. |  |
|  |  |  |
| [ColorAnActor](Python/Visualization/ColorAnActor.md) | Colour the actor. |  |
|  |  |  |
| [ColoredAnnotatedCube](Python/Visualization/ColoredAnnotatedCube.md) | How to color the individual faces of an annotated cube. |  |
|  |  |  |
| [CombustorIsosurface](Python/VisualizationAlgorithms/CombustorIsosurface.md) | Generate an isosurface of constant flow density. |  |
|  |  |  |
| [ComplexV](Python/Visualization/ComplexV.md) | ComplexV from the VTK Textbook. |  |
|  |  |  |
| [ContourQuadric](Python/VisualizationAlgorithms/ContourQuadric.md) | Contouring a quadric function. |  |
|  |  |  |
| [CreateBFont](Python/VisualizationAlgorithms/CreateBFont.md) | A scanned image clipped with a scalar value of 1/2 its maximum intensity produces a mixture of quadrilaterals and triangles. |  |
|  |  |  |
| [CreateColorSeriesDemo](Python/Visualization/CreateColorSeriesDemo.md) | Create a custom [vtkColorSeries](https://www.vtk.org/doc/nightly/html/classvtkColorSeries.html). |  |
|  |  |  |
| [CubeAxesActor](Python/Visualization/CubeAxesActor.md) | Display three orthogonal axes with labels. |  |
|  |  |  |
| [CurvatureBandsWithGlyphs](Python/Visualization/CurvatureBandsWithGlyphs.md) | Demonstrates the coloring of a surface by partitioning the gaussian curvature of a surface into bands and using arrows to display the normals on the surface. |  |
|  |  |  |
| [Curvatures](Python/Visualization/Curvatures.md) | Compute Gaussian, and Mean Curvatures. |  |
|  |  |  |
| [CurvaturesAdjustEdges](Python/Visualization/CurvaturesAdjustEdges.md) | Get the Gaussian and Mean curvatures of a surface with adjustments for edge effects. |  |
|  |  |  |
| [CurvaturesDemo](Python/Visualization/CurvaturesDemo.md) | Demonstrates how to get the Gaussian and Mean curvatures of a surface. |  |
|  |  |  |
| [CutStructuredGrid](Python/VisualizationAlgorithms/CutStructuredGrid.md) | Cut through structured grid with plane. The cut plane is shown solid shaded. A computational plane of constant k value is shown in wireframe for comparison. The colors correspond to flow density. Cutting surfaces are not necessarily planes: implicit functions such as spheres, cylinders, and quadrics can also be used. |  |
|  |  |  |
| [Cutter](Python/VisualizationAlgorithms/Cutter.md) | How to use [vtkCutter](https://www.vtk.org/doc/nightly/html/classvtkCutter.html) by cutting through a cube. |  |
|  |  |  |
| [DataSetSurface](Python/VisualizationAlgorithms/DataSetSurface.md) | Cutting a hexahedron with a plane. The red line on the surface shows the cut. |  |
|  |  |  |
| [DecimateFran](Python/VisualizationAlgorithms/DecimateFran.md) | Examples of decimation algorithm. (a) Decimation of laser digitizer data. |  |
|  |  |  |
| [DecimateHawaii](Python/VisualizationAlgorithms/DecimateHawaii.md) | Examples of decimation algorithm. (b) Decimation of terrain data. |  |
|  |  |  |
| [DisplacementPlot](Python/VisualizationAlgorithms/DisplacementPlot.md) | Show modal lines for a vibrating beam. |  |
|  |  |  |
| [DisplayCoordinateAxes](Python/Visualization/DisplayCoordinateAxes.md) | Display coordinate axes. |  |
|  |  |  |
| [DisplayQuadricSurfaces](Python/Visualization/DisplayQuadricSurfaces.md) | Create and display a quadratic surface. |  |
|  |  |  |
| [ElevationBandsWithGlyphs](Python/Visualization/ElevationBandsWithGlyphs.md) | Demonstrates the coloring of a surface by partitioning the elevation into bands and using arrows to display the normals on the surface. |  |
|  |  |  |
| [ExponentialCosine](Python/VisualizationAlgorithms/ExponentialCosine.md) | Carpet plots. Visualization of an exponential cosine function. Function values are indicated by surface displacement. Colors indicate derivative values. |  |
|  |  |  |
| [FlyingHeadSlice](Python/VisualizationAlgorithms/FlyingHeadSlice.md) | Flying edges used to generate contour lines. |  |
|  |  |  |
| [FrogBrain](Python/Visualization/FrogBrain.md) | The frog's brain. Model extracted without smoothing (left) and with smoothing (right). |  |
|  |  |  |
| [FroggieSurface](Python/Visualization/FroggieSurface.md) | Construct surfaces from a segmented frog dataset. Up to fifteen different surfaces may be extracted. You can turn on and off surfaces and control the camera position. |  |
|  |  |  |
| [FroggieView](Python/Visualization/FroggieView.md) | View surfaces of a segmented frog dataset using preprocessed `*.vtk` tissue files. You can turn on and off surfaces, control their opacity through the use of sliders and control the camera position. |  |
|  |  |  |
| [FrogSlice](Python/Visualization/FrogSlice.md) | Photographic slice of frog (upper left), segmented frog (upper right) and composite of photo and segmentation (bottom). The purple color represents the stomach and the kidneys are yellow. |  |
|  |  |  |
| [GlyphTable](Python/Visualization/GlyphTable.md) | Vary the shapes of glyphed points using a glyph table |  |
|  |  |  |
| [Hanoi](Python/Visualization/Hanoi.md) | Towers of Hanoi. |  |
|  |  |  |
| [HanoiInitial](Python/Visualization/HanoiInitial.md) | Towers of Hanoi - Initial configuration. |  |
|  |  |  |
| [HanoiIntermediate](Python/Visualization/HanoiIntermediate.md) | Towers of Hanoi - Intermediate configuration. |  |
|  |  |  |
| [HardwareSelector](Python/Visualization/HardwareSelector.md) |  |  |
|  |  |  |
| [Hawaii](Python/Visualization/Hawaii.md) | Visualize elevations by coloring the scalar values with a lookup table. |  |
|  |  |  |
| [HeadBone](Python/VisualizationAlgorithms/HeadBone.md) | Marching cubes surface of human bone. |  |
|  |  |  |
| [HeadSlice](Python/VisualizationAlgorithms/HeadSlice.md) | Marching squares used to generate contour lines. |  |
|  |  |  |
| [HyperStreamline](Python/VisualizationAlgorithms/HyperStreamline.md) | Example of hyperstreamlines, the four hyperstreamlines shown are integrated along the minor principle stress axis. A plane (colored with a different lookup table) is also shown. |  |
|  |  |  |
| [IronIsoSurface](Python/VisualizationAlgorithms/IronIsoSurface.md) | Marching cubes surface of iron-protein. |  |
|  |  |  |
| [IsosurfaceSampling](Python/Visualization/IsosurfaceSampling.md) | Demonstrates how to create point data on an isosurface. |  |
|  |  |  |
| [Kitchen](Python/Visualization/Kitchen.md) | Demonstrates stream tracing in a kitchen. |  |
|  |  |  |
| [KochSnowflake](Python/Visualization/KochSnowflake.md) | This example draws a Koch snowflake fractal using recursive functions and some of the convenient tools in the toolkit. |  |
|  |  |  |
| [LOx](Python/VisualizationAlgorithms/LOx.md) | Streamtubes created by using the computational grid just in front of the post as a source for seeds. |  |
|  |  |  |
| [LOxGrid](Python/VisualizationAlgorithms/LOxGrid.md) | Portion of computational grid for the LOx post. |  |
|  |  |  |
| [LOxSeeds](Python/VisualizationAlgorithms/LOxSeeds.md) | Streamlines seeded with spherical cloud of points. Four separate cloud positions are shown. |  |
|  |  |  |
| [LoopShrink](Python/Visualization/LoopShrink.md) | A network with a loop. VTK 5.0 does not allow you to execute a looping visualization network; this was possible in previous versions of VTK. |  |
|  |  |  |
| [Motor](Python/VisualizationAlgorithms/Motor.md) | Texture cut used to reveal internal structure of a motor. Two cut planes are used in combination with transparent texture. |  |
|  |  |  |
| [NamedColors](Python/Visualization/NamedColors.md) | Demonstrates how to use the [vtkNamedColors](https://www.vtk.org/doc/nightly/html/classvtkNamedColors.html) class. |  |
|  |  |  |
| [NormalsDemo](Python/Visualization/NormalsDemo.md) | Demo different options to generate normals. |  |
|  |  |  |
| [Office](Python/VisualizationAlgorithms/Office.md) | Using random point seeds to create streamlines. |  |
|  |  |  |
| [OfficeA](Python/VisualizationAlgorithms/OfficeA.md) | Corresponds to Fig 9-47(a) in the VTK textbook. |  |
|  |  |  |
| [OfficeTube](Python/VisualizationAlgorithms/OfficeTube.md) | The stream polygon. Sweeping a polygon to form a tube. |  |
|  |  |  |
| [OrientedGlyphs](Python/Visualization/OrientedGlyphs.md) | Create oriented glyphs from vector data. |  |
|  |  |  |
| [PineRootConnectivity](Python/VisualizationAlgorithms/PineRootConnectivity.md) | Applying the connectivity filter to remove noisy isosurfaces. |  |
|  |  |  |
| [PineRootConnectivityA](Python/VisualizationAlgorithms/PineRootConnectivityA.md) | The isosurface, with no connectivity filter applied. |  |
|  |  |  |
| [PineRootDecimation](Python/VisualizationAlgorithms/PineRootDecimation.md) | Applying the decimation and connectivity filters to remove noisy isosurfaces and reduce data size. |  |
|  |  |  |
| [PlateVibration](Python/VisualizationAlgorithms/PlateVibration.md) | Demonstrates the motion of a vibrating beam. |  |
|  |  |  |
| [PointDataSubdivision](Python/Visualization/PointDataSubdivision.md) | Demonstrates the use of the [vtkLinearSubdivisionFilter](https://www.vtk.org/doc/nightly/html/classvtkLinearSubdivisionFilter.html) and [vtkButterflySubdivisionFilter](https://www.vtk.org/doc/nightly/html/classvtkButterflySubdivisionFilter.html). |  |
|  |  |  |
| [PointSize](Python/Visualization/PointSize.md) |  |  |
|  |  |  |
| [ProbeCombustor](Python/VisualizationAlgorithms/ProbeCombustor.md) | Probing data in a combustor. Probes are regular arrays of 50 by 50 points that are then passed through a contouring filter. |  |
|  |  |  |
| [ProgrammableGlyphFilter](Python/Visualization/ProgrammableGlyphFilter.md) | Generate a custom glyph at each point. |  |
|  |  |  |
| [ProgrammableGlyphs](Python/Visualization/ProgrammableGlyphs.md) | Generate programmable glyphs. |  |
|  |  |  |
| [PseudoVolumeRendering](Python/VolumeRendering/PseudoVolumeRendering.md) | Here we use 20 cut planes, each with an opacity of of 0.25. They are then rendered back-to-front to simulate volume rendering. |  |
|  |  |  |
| [QuadricVisualization](Python/Visualization/QuadricVisualization.md) | Visualizing a quadric function. |  |
|  |  |  |
| [SingleSplat](Python/VisualizationAlgorithms/SingleSplat.md) | Elliptical splatting. (a) Single elliptical splat with eccentricity E=10. Cone shows orientation of vector. |  |
|  |  |  |
| [SphereTexture](Python/Visualization/SphereTexture.md) | Apply an ImageData texture to an sphere |  |
|  |  |  |
| [SpikeFran](Python/VisualizationAlgorithms/SpikeFran.md) | Glyphs indicate surface normals on model of human face. Glyph positions are randomly selected. |  |
|  |  |  |
| [SplatFace](Python/VisualizationAlgorithms/SplatFace.md) | Elliptical splatting. (b) Surface reconstructed using elliptical splats into 100^3 volume followed by isosurface extraction. Points regularly subsampled and overlaid on original mesh. |  |
|  |  |  |
| [Stocks](Python/VisualizationAlgorithms/Stocks.md) | Two views from the stock visualization script. The top shows closing price over time; the bottom shows volume over time. |  |
|  |  |  |
| [StreamLines](Python/Visualization/StreamLines.md) | Seed streamlines with vectors from a structured grid. |  |
|  |  |  |
| [StreamlinesWithLineWidget](Python/VisualizationAlgorithms/StreamlinesWithLineWidget.md) | Using the [vtkLineWidget](https://www.vtk.org/doc/nightly/html/classvtkLineWidget.html) to produce streamlines in the combustor dataset. The StartInteractionEvent turns the visibility of the streamlines on; the InteractionEvent causes the streamlines to regenerate themselves. |  |
|  |  |  |
| [TensorAxes](Python/VisualizationAlgorithms/TensorAxes.md) | Display the scaled and oriented principal axes of the stress tensor. |  |
|  |  |  |
| [TensorEllipsoids](Python/VisualizationAlgorithms/TensorEllipsoids.md) | Display the scaled and oriented principal axes as tensor ellipsoids representing the stress tensor. |  |
|  |  |  |
| [TextSource](Python/Visualization/TextSource.md) |  |  |
|  |  |  |
| [VectorText](Python/Visualization/VectorText.md) | Display high resolution text. |  |
|  |  |  |
| [VelocityProfile](Python/VisualizationAlgorithms/VelocityProfile.md) | Warping the geometry of three planes to show flow momentum. |  |
|  |  |  |
| [WarpCombustor](Python/VisualizationAlgorithms/WarpCombustor.md) | Carpet plots of combustor flow energy in a structured grid. Colors and plane displacement represent energy values. |  |
|  |  |  |
| [WindowTitle](Python/Visualization/WindowTitle.md) |  |  |
|  |  |  |

## Working with [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html)

| Example Name | Description | Image |
| --- | --- | --- |
| [ImageDataGeometryFilter](Python/ImageData/ImageDataGeometryFilter.md) | Convert a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html) to a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). |  |
|  |  |  |
| [ImageNormalize](Python/ImageData/ImageNormalize.md) | Normalize an image. |  |
|  |  |  |
| [SumVTKImages](Python/ImageData/SumVTKImages.md) | A function to simplify the summing of images, where you can pass a list of images and weights. |  |
| [WriteReadVtkImageData](Python/ImageData/WriteReadVtkImageData.md) | Generate, edit and read out vtk image data. |  |
|  |  |  |

## Volume Rendering

| Example Name | Description | Image |
| --- | --- | --- |
| [SimpleRayCast](Python/VolumeRendering/SimpleRayCast.md) | Volume rendering of a high potential iron protein. |  |
|  |  |  |

## User Interaction

| Example Name | Description | Image |
| --- | --- | --- |
| [CallBack](Python/Interaction/CallBack.md) | Setting up a callback with client data. Two different methods are demonstrated. |  |
|  |  |  |
| [CellPicking](Python/Picking/CellPicking.md) | Cell Picking. |  |
|  |  |  |
| [HighlightPickedActor](Python/Picking/HighlightPickedActor.md) | Pick and highlight an actor based on mouse clicks. |  |
|  |  |  |
| [HighlightWithSilhouette](Python/Picking/HighlightWithSilhouette.md) | Highlight a picked actor by adding a silhouette. |  |
|  |  |  |
| [InteractorStyleTrackballActor](Python/Interaction/InteractorStyleTrackballActor.md) |  |  |
|  |  |  |
| [InteractorStyleTrackballCamera](Python/Interaction/InteractorStyleTrackballCamera.md) |  |  |
|  |  |  |
| [MouseEvents](Python/Interaction/MouseEvents.md) | Subclass the interactor style. |  |
|  |  |  |
| [MouseEventsObserver](Python/Interaction/MouseEventsObserver.md) | Use an observer. |  |
|  |  |  |

## Working with Images

| Example Name | Description | Image |
| --- | --- | --- |
| [Actor2D](Python/Images/Actor2D.md) | 2D actor and mapper. |  |
|  |  |  |
| [BackgroundImage](Python/Images/BackgroundImage.md) | Display an image as the "background" of a scene, and render a superquadric in front of it. |  |
|  |  |  |
| [Cast](Python/Images/Cast.md) | Cast an image to a different type. |  |
|  |  |  |

## Image Processing

| Example Name | Description | Image |
| --- | --- | --- |
| [Attenuation](Python/ImageProcessing/Attenuation.md) | This MRI image illustrates attenuation that can occur due to sensor position. The artifact is removed by dividing by the attenuation profile determined manually. |  |
|  |  |  |
| [EnhanceEdges](Python/ImageProcessing/EnhanceEdges.md) | High-pass filters can extract and enhance edges in an image. Subtraction of the Laplacian (middle) from the original image (left) results in edge enhancement or a sharpening operation (right). |  |
|  |  |  |
| [GaussianSmooth](Python/ImageProcessing/GaussianSmooth.md) | Low-pass filters can be implemented as convolution with a Gaussian kernel. |  |
|  |  |  |
| [HybridMedianComparison](Python/ImageProcessing/HybridMedianComparison.md) | Comparison of median and hybrid-median filters. The hybrid filter preserves corners and thin lines, better than the median filter. |  |
|  |  |  |
| [IdealHighPass](Python/ImageProcessing/IdealHighPass.md) | This figure shows two high-pass filters in the frequency domain. The Butterworth high-pass filter has a gradual attenuation that avoids ringing produced by the ideal high-pass filter with an abrupt transition. |  |
|  |  |  |
| [ImageGradient](Python/VisualizationAlgorithms/ImageGradient.md) | Create an imaging pipeline to visualize gradient information. |  |
|  |  |  |
| [ImageWarp](Python/Images/ImageWarp.md) | Combine the imaging and visualization pipelines to deform an image in the z-direction. The [vtkMergeFilter](https://www.vtk.org/doc/nightly/html/classvtkMergeFilter.html) is used to combine the warped surface with the original color data. |  |
|  |  |  |
| [IsoSubsample](Python/ImageProcessing/IsoSubsample.md) | This figure demonstrates aliasing that occurs when a high-frequency signal is subsampled. High frequencies appear as low frequency artifacts. The left image is an isosurface of a skull after subsampling. The right image used a low-pass filter before subsampling to reduce aliasing. |  |
|  |  |  |
| [MedianComparison](Python/ImageProcessing/MedianComparison.md) | Comparison of Gaussian and Median smoothing for reducing low-probability high-amplitude noise. |  |
|  |  |  |
| [MorphologyComparison](Python/ImageProcessing/MorphologyComparison.md) | This figure demonstrates various binary filters that can alter the shape of segmented regions. |  |
|  |  |  |
| [Pad](Python/ImageProcessing/Pad.md) | Convolution in frequency space treats the image as a periodic function. A large kernel can pick up features from both sides of the image. The lower-left image has been padded with a constant to eliminate wraparound during convolution. On the right, mirror padding has been used to remove artificial edges introduced by borders. |  |
|  |  |  |
| [VTKSpectrum](Python/ImageProcessing/VTKSpectrum.md) | The discrete Fourier transform changes an image from the spatial domain into the frequency domain, where each pixel represents a sinusoidal function. This figure shows an image and its power spectrum displayed using a logarithmic transfer function. |  |
|  |  |  |

## Widgets

| Example Name | Description | Image |
| --- | --- | --- |
| [BalloonWidget](Python/Widgets/BalloonWidget.md) | Uses a [vtkBalloonWidget](https://www.vtk.org/doc/nightly/html/classvtkBalloonWidget.html) to draw labels when the mouse stays above an actor. |  |
|  |  |  |
| [BoxWidget](Python/Widgets/BoxWidget.md) | This 3D widget defines a region of interest that is represented by an arbitrarily oriented hexahedron with interior face angles of 90 degrees (orthogonal faces). The object creates 7 handles that can be moused on and manipulated. |  |
|  |  |  |
| [CameraOrientationWidget](Python/Widgets/CameraOrientationWidget.md) | Demonstrates a 3D camera orientation widget. |  |
|  |  |  |
| [CompassWidget](Python/Widgets/CompassWidget.md) | Draws an interactive compass. |  |
|  |  |  |
| [ContourWidget](Python/Widgets/ContourWidget.md) | Draw a contour (line) which can be deformed by the user |  |
|  |  |  |
| [ImplicitPlaneWidget2](Python/Widgets/ImplicitPlaneWidget2.md) | Clip polydata with an implicit plane. |  |
|  |  |  |
| [OrientationMarkerWidget](Python/Widgets/OrientationMarkerWidget.md) | Draws two cubes. One of them can be clicked to be rotated, and will rotate the second one. The second one has annotations on it, and can also be moved. |  |
|  |  |  |
| [OrientationMarkerWidget1](Python/Widgets/OrientationMarkerWidget1.md) | Display a polydata as an orientation icon. |  |
|  |  |  |
| [ScalarBarWidget](Python/Widgets/ScalarBarWidget.md) | The ScalarBarWidget displays a scalar bar that is movable and changes orientation automatically when close to the borders of the image. It needs a ScalarBarActor |  |
|  |  |  |
| [SphereWidget](Python/Widgets/SphereWidget.md) | This 3D widget defines a sphere that can be interactively placed in a scene. |  |
|  |  |  |
| [SplineWidget](Python/Widgets/SplineWidget.md) | This example shows how to use [vtkSplineWidget](https://www.vtk.org/doc/nightly/html/classvtkSplineWidget.html) with a callback being used to get the length of the spline widget. |  |
|  |  |  |
| [TextWidget](Python/Widgets/TextWidget.md) | Annotate a VTK image with movable text |  |
|  |  |  |

## Plotting

| Example Name | Description | Image |
| --- | --- | --- |
| [MultiplePlots](Python/Plotting/MultiplePlots.md) | Display multiple plots by using viewports in a single render window. |  |
|  |  |  |
| [ScatterPlot](Python/Plotting/ScatterPlot.md) | Scatter plot. |  |
|  |  |  |
| [SpiderPlot](Python/Plotting/SpiderPlot.md) | Spider plot. |  |
|  |  |  |
| [SurfacePlot](Python/Plotting/SurfacePlot.md) | Surface plot. |  |
|  |  |  |

## Animation

| Example Name | Description | Image |
| --- | --- | --- |
| [Animation](Python/Utilities/Animation.md) | Move a sphere across a scene. |  |
|  |  |  |

## Annotation

| Example Name | Description | Image |
| --- | --- | --- |
| [MultiLineText](Python/Annotation/MultiLineText.md) | Display multiline text. |  |
|  |  |  |
| [TextOrigin](Python/Annotation/TextOrigin.md) | This example demonstrates the use of [vtkVectorText](https://www.vtk.org/doc/nightly/html/classvtkVectorText.html) and [vtkFollower](https://www.vtk.org/doc/nightly/html/classvtkFollower.html). [vtkVectorText](https://www.vtk.org/doc/nightly/html/classvtkVectorText.html) is used to create 3D annotation. |  |
|  |  |  |

## InfoVis

| Example Name | Description | Image |
| --- | --- | --- |
| [ParallelCoordinatesExtraction](Python/InfoVis/ParallelCoordinatesExtraction.md) | Extract data based on a selection in a Parallel Coordinates View. |  |
|  |  |  |
| [ParallelCoordinatesView](Python/InfoVis/ParallelCoordinatesView.md) | How to use Parallel Coordinates View to plot and compare data set attributes. |  |
|  |  |  |
| [SelectedGraphIDs](Python/InfoVis/SelectedGraphIDs.md) | Callback on [vtkAnnotationLink](https://www.vtk.org/doc/nightly/html/classvtkAnnotationLink.html) in a Graph Layout View when selection is changed. |  |
|  |  |  |

## PyQt

| Example Name | Description | Image |
| --- | --- | --- |
| [EmbedInPyQt](Python/Widgets/EmbedInPyQt.md) | Shows how to easily embed VTK in PyQt with QVTKRenderWindowInteractor, first example |  |
|  |  |  |
| [EmbedInPyQt2](Python/Widgets/EmbedInPyQt2.md) | Shows how to embed VTK in PyQt with QVTKRenderWindowInteractor, second example |  |
|  |  |  |
