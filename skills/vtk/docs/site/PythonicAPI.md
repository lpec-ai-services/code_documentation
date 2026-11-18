<!-- source: https://examples.vtk.org/site/PythonicAPI/ -->

# PythonicAPI Examples

Warning

These examples only work with VTK Version: 9.3.20240428 or greater.

These examples:

- Use the improved VTK Python interface. Some information about the improved Python interface can be found [here](PythonicAPIComments.md)
- Are either newly crafted examples or upgrades of existing Python examples

See:

- [More Pythonic VTK wrapping](https://discourse.vtk.org/t/more-pythonic-vtk-wrapping/13092) for the VTK Discourse discussion
- [Wrap VTK properties to pythonic properties with snake_case names](https://gitlab.kitware.com/vtk/vtk/-/merge_requests/10820) for the merge request

## Upgrading an existing example to use the improved VTK Python interface

1. Copy the example from the **src/Python** folder into the **src/PythonicAPI** folder maintaining the same path structure. If there is a corresponding markdown file, copy it.
2. Copy the corresponding test image from **src/Testing/Baseline/Python/** into **src/Testing/Baseline/PythonicAPI/**
3. Edit **src/PythonicAPI.md**, possibly creating a table and headings to match the original example in **src/Python**.
4. Upgrade the Python example.
5. The associated markdown file (if any) may need checking to ensure any links in the document remain valid.
6. Check everything is working and do a Merge Request.

## Adding a new example

Follow the documented procedure [ForDevelopers](https://examples.vtk.org/site/Instructions/ForDevelopers/) remembering that the folder to use is **PythonicAPI**.

## VTK Classes Summary

This Python script, [SelectExamples](PythonicAPI/Utilities/SelectExamples.md), will let you select examples based on a VTK Class and language. It requires Python 3.7 or later. The following tables will produce similar information.

- [VTK Classes with Examples](PythonicAPI/Coverage/PythonicAPIVTKClassesUsed.md), this table is really useful when searching for example(s) using a particular class.
- [VTK Classes with No Examples](PythonicAPI/Coverage/PythonicAPIVTKClassesNotUsed.md), please add examples in your area of expertise!

## Snippets

|  |  |  |
| --- | --- | --- |
| [Snippets](PythonicAPI/Snippets.md) | These are chunks of code that can be cut (*snipped*) and pasted into examples. |  |

## Tutorials

## Hello World

| Example Name | Description | Image |
| --- | --- | --- |
| [A hello world example](PythonicAPI/GeometricObjects/CylinderExample.md) | Cylinder example from the VTK Textbook and source code. A hello world example. |  |
|  |  |  |

## Simple Operations

| Example Name | Description | Image |
| --- | --- | --- |
| [DistanceBetweenPoints](PythonicAPI/SimpleOperations/DistanceBetweenPoints.md) | Distance between two points. |  |
| [DistancePointToLine](PythonicAPI/SimpleOperations/DistancePointToLine.md) | Distance between a point and a line. |  |
| [GaussianRandomNumber](PythonicAPI/SimpleOperations/GaussianRandomNumber.md) | Generates Gaussian random numbers. |  |
| [PerspectiveTransform](PythonicAPI/SimpleOperations/PerspectiveTransform.md) | Apply a perspective transformation to a point. |  |

## Input and Output

### Graph Formats

### 3D File Formats

| Example Name | Description | Image |
| --- | --- | --- |
| [XGMLReader](PythonicAPI/InfoVis/XGMLReader.md) | Read a .gml file |  |
|  |  |  |

#### Standard Formats

##### Input

| Example Name | Description | Image |
| --- | --- | --- |
| [CSVReadEdit](PythonicAPI/IO/CSVReadEdit.md) | Read and edit a CSV file using pandas and numpy. |  |
|  |  |  |
| [CSVReadEdit1](PythonicAPI/IO/CSVReadEdit1.md) | Read and edit a CSV file using pandas and [vtkDelimitedTextReader](https://www.vtk.org/doc/nightly/html/classvtkDelimitedTextReader.html). |  |
|  |  |  |
| [ParticleReader](PythonicAPI/IO/ParticleReader.md) | This example reads ASCII files where each line consists of points with its position (x,y,z) and (optionally) one scalar or binary files in RAW 3d file format. |  |
|  |  |  |
| [ReadAllPolyDataTypesDemo](PythonicAPI/IO/ReadAllPolyDataTypesDemo.md) | Read all VTK polydata file types. |  |
|  |  |  |
| [ReadCML](PythonicAPI/IO/ReadCML.md) | Read Chemistry Markup Language files. |  |
|  |  |  |
| [ReadExodusData](PythonicAPI/IO/ReadExodusData.md) | A simple script for reading and viewing ExodusII data interactively. |  |
|  |  |  |
| [ReadSLC](PythonicAPI/IO/ReadSLC.md) | Read an SLC file. |  |
|  |  |  |
| [TemporalHDFReader](PythonicAPI/IO/TemporalHDFReader.md) | Read temporal data written inside a vtkhdf file. |  |

###### Importers

| Example Name | Description | Image |
| --- | --- | --- |
| [3DSImporter](PythonicAPI/IO/3DSImporter.md) | Import a 3D Studio scene that includes multiple actors. |  |
|  |  |  |
| [ImportPolyDataScene](PythonicAPI/IO/ImportPolyDataScene.md) | Import a polydata scene using multiblock datasets. |  |
|  |  |  |
| [ImportToExport](PythonicAPI/IO/ImportToExport.md) | Import a scene and optionally export the scene. |  |
|  |  |  |

##### Output

| Example Name | Description | Image |
| --- | --- | --- |
| [DelimitedTextWriter](PythonicAPI/InfoVis/DelimitedTextWriter.md) | Write data to a delimited file. |  |
| [WritePLY](PythonicAPI/IO/WritePLY.md) |  |  |
|  |  |  |
| [WriteSTL](PythonicAPI/IO/WriteSTL.md) |  |  |
|  |  |  |

###### Exporters

#### VTK Formats

##### Input

##### Output

| Example Name | Description | Image |
| --- | --- | --- |
| [ExodusIIWriter](PythonicAPI/Parallel/ExodusIIWriter.md) | Write a time varying ExodusII file. |  |

#### Legacy VTK Formats

| Example Name | Description | Image |
| --- | --- | --- |
| [GenericDataObjectReader](PythonicAPI/IO/GenericDataObjectReader.md) | Read any type of legacy .vtk file. |  |
| [ReadLegacyUnstructuredGrid](PythonicAPI/IO/ReadLegacyUnstructuredGrid.md) | Read an unstructured grid that contains 11 linear cells. |  |
|  |  |  |
| [WriteLegacyLinearCells](PythonicAPI/IO/WriteLegacyLinearCells.md) | Write each linear cell into a legacy UnstructuredGrid file (.vtk). |  |
| [WriteXMLLinearCells](PythonicAPI/IO/WriteXMLLinearCells.md) | Write each linear cell into an XML UnstructuredGrid file (.vtu). |  |

### Image Format

#### Input

| Example Name | Description | Image |
| --- | --- | --- |
| [HDRReader](PythonicAPI/IO/HDRReader.md) | Read a high-dynamic-range imaging file. |  |
|  |  |  |
| [ReadDICOM](PythonicAPI/IO/ReadDICOM.md) | Read DICOM file. |  |
|  |  |  |
| [ReadDICOMSeries](PythonicAPI/IO/ReadDICOMSeries.md) | This example demonstrates how to read a series of DICOM images and scroll through slices |  |
|  |  |  |

#### Output

## Geometric Objects

| Example Name | Description | Image |
| --- | --- | --- |
| [Dodecahedron](PythonicAPI/GeometricObjects/Dodecahedron.md) | Create a dodecahedron using [vtkPolyhedron](https://www.vtk.org/doc/nightly/html/classvtkPolyhedron.html). |  |
|  |  |  |
| [GeometricObjectsDemo](PythonicAPI/GeometricObjects/GeometricObjectsDemo.md) |  |  |
|  |  |  |
| [PipelineReuse](PythonicAPI/GeometricObjects/PipelineReuse.md) | How to reuse a pipeline. |  |
|  |  |  |
| [PlaneSourceDemo](PythonicAPI/GeometricObjects/PlaneSourceDemo.md) | Display the instance variables that define a [vtkPlaneSource](https://www.vtk.org/doc/nightly/html/classvtkPlaneSource.html). |  |
|  |  |  |
| [Planes](PythonicAPI/GeometricObjects/Planes.md) | We create a convex hull of the planes for display purposes. |  |
|  |  |  |
| [PlanesIntersection](PythonicAPI/GeometricObjects/PlanesIntersection.md) |  |  |
| [SourceObjectsDemo](PythonicAPI/GeometricObjects/SourceObjectsDemo.md) | Examples of source objects that procedurally generate polygonal models. These nine images represent just some of the capability of VTK. From upper left in reading order: sphere, cone, cylinder, cube, plane, text, random point cloud, disk (with or without hole), and line source. Other polygonal source objects are available; check subclasses of [vtkPolyDataAlgorithm](https://www.vtk.org/doc/nightly/html/classvtkPolyDataAlgorithm.html). |  |
|  |  |  |

### Cells

| Example Name | Description | Image |
| --- | --- | --- |
| [CellTypeSource](PythonicAPI/GeometricObjects/CellTypeSource.md) | Generate tessellated cells. |  |
|  |  |  |
| [ConvexPointSet](PythonicAPI/GeometricObjects/ConvexPointSet.md) | Generate a ConvexPointSet cell. |  |
|  |  |  |
| [LinearCellsDemo](PythonicAPI/GeometricObjects/LinearCellsDemo.md) | Linear cell types found in VTK. The numbers define the ordering of the points making the cell. |  |
|  |  |  |
| [Polyhedron](PythonicAPI/GeometricObjects/Polyhedron.md) | Create an unstructured grid representation of a polyhedron (cube) and write it out to a file. |  |
|  |  |  |

### Sources

| Example Name | Description | Image |
| --- | --- | --- |
| [ConesOnSphere](PythonicAPI/GeometricObjects/ConesOnSphere.md) | Generate a sphere and position a cone at the center of each cell on the sphere, aligned with the face normal. |  |
|  |  |  |
| [EarthSource](PythonicAPI/GeometricObjects/EarthSource.md) | Create the Earth. |  |
|  |  |  |
| [Frustum](PythonicAPI/GeometricObjects/Frustum.md) |  |  |
|  |  |  |
| [GoldenBallSource](PythonicAPI/GeometricObjects/GoldenBallSource.md) | Construct a solid, tetrahedralized ball. |  |
|  |  |  |
| [OrientedArrow](PythonicAPI/GeometricObjects/OrientedArrow.md) | Orient an arrow along an arbitrary vector. |  |
|  |  |  |
| [OrientedCylinder](PythonicAPI/GeometricObjects/OrientedCylinder.md) | Orient a cylinder along an arbitrary vector. |  |
|  |  |  |
| [PlatonicSolids](PythonicAPI/GeometricObjects/PlatonicSolids.md) | All five platonic solids are displayed. |  |
|  |  |  |
| [SphereSource](PythonicAPI/GeometricObjects/SphereSource.md) | Construct a sphere. |  |
|  |  |  |
| [TessellatedBoxSource](PythonicAPI/GeometricObjects/TessellatedBoxSource.md) | Generate a box with tessellated sides. |  |
|  |  |  |

### Non Linear

| Example Name | Description | Image |
| --- | --- | --- |
| [IsoparametricCellsDemo](PythonicAPI/GeometricObjects/IsoparametricCellsDemo.md) | Nonlinear isoparametric cell types in VTK. |  |
|  |  |  |

### Parametric Objects

| Example Name | Description | Image |
| --- | --- | --- |
| [ParametricObjectsDemo](PythonicAPI/GeometricObjects/ParametricObjectsDemo.md) | Demonstrates the Parametric classes added by Andrew Maclean and additional classes added by Tim Meehan. The parametric spline is also included. Options are provided to display single objects, add backface, add normals and print out an image. |  |
|  |  |  |
| [ParametricKuenDemo](PythonicAPI/GeometricObjects/ParametricKuenDemo.md) | Interactively change the parameters for a Kuen Surface. |  |
|  |  |  |

## Implicit Functions and Iso-surfaces

| Example Name | Description | Image |
| --- | --- | --- |
| [BooleanOperationImplicitFunctions](PythonicAPI/ImplicitFunctions/BooleanOperationImplicitFunctions.md) | Demonstrate booleans of two different implicit functions |  |
|  |  |  |
| [ContourTriangulator](PythonicAPI/Modelling/ContourTriangulator.md) | Create a contour from a structured point set (image) and triangulate it. |  |
|  |  |  |
| [DiscreteFlyingEdges3D](PythonicAPI/Modelling/DiscreteFlyingEdges3D.md) | Generate surfaces from labeled data. |  |
|  |  |  |
| [ExtractData](PythonicAPI/VisualizationAlgorithms/ExtractData.md) | Implicit functions used to select data: Two ellipsoids are combined using the union operation used to select voxels from a volume. Voxels are shrunk 50 percent. |  |
|  |  |  |
| [ExtractLargestIsosurface](PythonicAPI/Modelling/ExtractLargestIsosurface.md) | Extract largest isosurface. |  |
|  |  |  |
| [IceCream](PythonicAPI/VisualizationAlgorithms/IceCream.md) | How to use boolean combinations of implicit functions to create a model of an ice cream cone. |  |
|  |  |  |
| [ImplicitDataSet](PythonicAPI/ImplicitFunctions/ImplicitDataSet.md) | Convert an imagedata to an implicit function. |  |
| [ImplicitQuadric](PythonicAPI/ImplicitFunctions/ImplicitQuadric.md) | Create an ellipsoid using an implicit quadric |  |
|  |  |  |
| [ImplicitSphere](PythonicAPI/ImplicitFunctions/ImplicitSphere.md) | Demonstrate sampling of a sphere implicit function |  |
|  |  |  |
| [ImplicitSphere1](PythonicAPI/ImplicitFunctions/ImplicitSphere1.md) | Demonstrate sampling of a sphere implicit function |  |
|  |  |  |
| [IsoContours](PythonicAPI/ImplicitFunctions/IsoContours.md) | Visualize different isocontours using a slider. |  |
|  |  |  |
| [Lorenz](PythonicAPI/Visualization/Lorenz.md) | Visualizing a Lorenz strange attractor by integrating the Lorenz equations in a volume. |  |
|  |  |  |
| [MarchingCubes](PythonicAPI/Modelling/MarchingCubes.md) | Create a voxelized sphere. |  |
|  |  |  |
| [SampleFunction](PythonicAPI/ImplicitFunctions/SampleFunction.md) | Sample and visualize an implicit function. |  |
|  |  |  |
| [SmoothDiscreteFlyingEdges3D](PythonicAPI/Modelling/SmoothDiscreteFlyingEdges3D.md) | Generate smooth surfaces from labeled data. |  |
|  |  |  |

## Working with 3D Data

| Example Name | Description | Image |
| --- | --- | --- |
| [AlignTwoPolyDatas](PythonicAPI/PolyData/AlignTwoPolyDatas.md) | Align two [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html)'s. |  |
|  |  |  |
| [BooleanPolyDataFilters](PythonicAPI/PolyData/BooleanPolyDataFilters.md) | This example performs a boolean operation (intersection, union or difference) of two PolyData using either a [vtkBooleanOperationPolyDataFilter](https://www.vtk.org/doc/nightly/html/classvtkBooleanOperationPolyDataFilter.html) or a [vtkLoopBooleanPolyDataFilter](https://www.vtk.org/doc/nightly/html/classvtkLoopBooleanPolyDataFilter.html) |  |
|  |  |  |
| [Bottle](PythonicAPI/Modelling/Bottle.md) | Model a rotationally symmetric object. |  |
|  |  |  |
| [CappedSphere](PythonicAPI/Modelling/CappedSphere.md) | Rotate an arc to create a capped sphere. |  |
|  |  |  |
| [CellsInsideObject](PythonicAPI/PolyData/CellsInsideObject.md) | Extract cells inside a closed surface. |  |
|  |  |  |
| [CenterOfMass](PythonicAPI/PolyData/CenterOfMass.md) | Compute the center of mass of the points. |  |
| [ConnectivityFilter](PythonicAPI/Filtering/ConnectivityFilter.md) | Color any dataset type based on connectivity. |  |
|  |  |  |
| [DecimatePolyline](PythonicAPI/PolyData/DecimatePolyline.md) | Decimate polyline. |  |
|  |  |  |
| [DistancePolyDataFilter](PythonicAPI/PolyData/DistancePolyDataFilter.md) | Compute the distance function from one [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) to another. |  |
|  |  |  |
| [ExternalContour](PythonicAPI/PolyData/ExternalContour.md) | Get the external contour of a PolyData object. |  |
|  |  |  |
| [ExtractPolyLinesFromPolyData](PythonicAPI/PolyData/ExtractPolyLinesFromPolyData.md) | Extract polylines from polydata. |  |
|  |  |  |
| [ExtractSelection](PythonicAPI/PolyData/ExtractSelection.md) | Extract selected points. |  |
|  |  |  |
| [ExtractSelectionOriginalId](PythonicAPI/PolyData/ExtractSelectionOriginalId.md) | Extract selection and find the correspondence between the new and original ids. |  |
|  |  |  |
| [ExtractSelectionUsingCells](PythonicAPI/PolyData/ExtractSelectionUsingCells.md) | Extract cell, select cell. |  |
|  |  |  |
| [ExtractSelectionUsingPoints](PythonicAPI/PolyData/ExtractSelectionUsingPoints.md) | Extract points but bring cells that are still complete with them. |  |
|  |  |  |
| [ExtractVisibleCells](PythonicAPI/Filtering/ExtractVisibleCells.md) | Extract and highlight visible cells. |  |
|  |  |  |
| [Finance](PythonicAPI/Modelling/Finance.md) | Visualization of multidimensional financial data. The gray/wireframe surface represents the total data population. The red surface represents data points delinquent on loan payment. |  |
|  |  |  |
| [FinanceFieldData](PythonicAPI/Modelling/FinanceFieldData.md) | Visualization of multidimensional financial data. The yellow surface represents the total data population. The red surface represents data points delinquent on loan payment. |  |
|  |  |  |
| [FitSplineToCutterOutput](PythonicAPI/PolyData/FitSplineToCutterOutput.md) | Fit a spline to cutter output. |  |
|  |  |  |
| [Glyph2D](PythonicAPI/Filtering/Glyph2D.md) |  |  |
|  |  |  |
| [GradientFilter](PythonicAPI/PolyData/GradientFilter.md) | Compute the gradient of a scalar field on a data set. |  |
|  |  |  |
| [ImplicitPolyDataDistance](PythonicAPI/PolyData/ImplicitPolyDataDistance.md) |  |  |
|  |  |  |
| [IntersectionPolyDataFilter](PythonicAPI/PolyData/IntersectionPolyDataFilter.md) | Compute the intersection of two [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) objects. |  |
|  |  |  |
| [KMeansClustering](PythonicAPI/InfoVis/KMeansClustering.md) | KMeans Clustering |  |
|  |  |  |
| [LineOnMesh](PythonicAPI/DataManipulation/LineOnMesh.md) | Plot a spline on a terrain-like surface. |  |
|  |  |  |
| [KochanekSplineDemo](PythonicAPI/PolyData/KochanekSplineDemo.md) | Interactively change the parameters of the Kochanek spline. |  |
|  |  |  |
| [MergeSelections](PythonicAPI/PolyData/MergeSelections.md) | Merge selected points. |  |
|  |  |  |
| [MeshLabelImageColor](PythonicAPI/DataManipulation/MeshLabelImageColor.md) | Mesh a single label from a label image. Then smooth and color the vertices according to the displacement error introduced by the smoothing. |  |
|  |  |  |
| [MultiBlockMergeFilter](PythonicAPI/PolyData/MultiBlockMergeFilter.md) | Combine MultiBlockDataSets. |  |
| [OrientedBoundingCylinder](PythonicAPI/PolyData/OrientedBoundingCylinder.md) | Create an oriented cylinder that encloses a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). The axis of the cylinder is aligned with the longest axis of the [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). |  |
|  |  |  |
| [Outline](PythonicAPI/PolyData/Outline.md) | Draw the bounding box of the data. |  |
|  |  |  |
| [PerlinNoise](PythonicAPI/Filtering/PerlinNoise.md) |  |  |
|  |  |  |
| [PolyDataContourToImageData](PythonicAPI/PolyData/PolyDataContourToImageData.md) |  |  |
| [PolyDataToImageDataStencil](PythonicAPI/PolyData/PolyDataToImageDataStencil.md) |  |  |
|  |  |  |
| [ResamplePolyLine](PythonicAPI/PolyData/ResamplePolyLine.md) |  |  |
|  |  |  |
| [RuledSurfaceFilter](PythonicAPI/PolyData/RuledSurfaceFilter.md) |  |  |
|  |  |  |
| [Silhouette](PythonicAPI/PolyData/Silhouette.md) |  |  |
|  |  |  |
| [SmoothMeshGrid](PythonicAPI/PolyData/SmoothMeshGrid.md) | Create a terrain with regularly spaced points and smooth it with vtkLoopSubdivisionFilter and vtkButterflySubdivisionFilter. |  |
|  |  |  |
| [SpatioTemporalHarmonicsSource](PythonicAPI/Filtering/SpatioTemporalHarmonicsSource.md) | Generate image data containing spatio-temporal harmonic data. |  |
|  |  |  |
| [Spring](PythonicAPI/Modelling/Spring.md) | Rotation in combination with linear displacement and radius variation. |  |
|  |  |  |
| [ThinPlateSplineTransform](PythonicAPI/PolyData/ThinPlateSplineTransform.md) |  |  |
|  |  |  |
| [VertexConnectivity](PythonicAPI/PolyData/VertexConnectivity.md) | Get a list of vertices attached (through an edge) to a vertex. |  |
|  |  |  |
| [WarpTo](PythonicAPI/Filtering/WarpTo.md) | Deform geometry by warping towards a point. |  |
|  |  |  |
| [WarpVector](PythonicAPI/PolyData/WarpVector.md) | This example warps/deflects a line. |  |
|  |  |  |

### Data Types

| Example Name | Description | Image |
| --- | --- | --- |
| [CompositePolyDataMapper](PythonicAPI/CompositeData/CompositePolyDataMapper.md) |  |  |
|  |  |  |
| [OverlappingAMR](PythonicAPI/CompositeData/OverlappingAMR.md) | Demonstrates how to create and populate VTK's Overlapping AMR Grid type with data. |  |
|  |  |  |

### Data Type Conversions

### Point Cloud Operations

| Example Name | Description | Image |
| --- | --- | --- |
| [DensifyPoints](PythonicAPI/Points/DensifyPoints.md) | Add points to a point cloud. |  |
|  |  |  |
| [ExtractClusters](PythonicAPI/Points/ExtractClusters.md) | From a set of randomly distributed spheres, extract connected clusters. |  |
|  |  |  |
| [ExtractPointsDemo](PythonicAPI/Points/ExtractPointsDemo.md) | Extract points inside an implicit function. |  |
|  |  |  |
| [ExtractSurface](PythonicAPI/Points/ExtractSurface.md) | Create a surface from unorganized points using point filters. |  |
|  |  |  |
| [ExtractSurfaceDemo](PythonicAPI/Points/ExtractSurfaceDemo.md) | Create a surface from unorganized points using point filters (DEMO). |  |
|  |  |  |
| [FitImplicitFunction](PythonicAPI/Points/FitImplicitFunction.md) | Extract points within a distance to an implicit function. |  |
|  |  |  |
| [MaskPointsFilter](PythonicAPI/Points/MaskPointsFilter.md) | Extract points within an image mask. |  |
|  |  |  |
| [SignedDistance](PythonicAPI/Points/SignedDistance.md) | Compute signed distance to a point cloud. |  |
|  |  |  |
| [UnsignedDistance](PythonicAPI/Points/UnsignedDistance.md) | Compute unsigned distance to a point cloud. |  |
|  |  |  |

### Working with Meshes

This section includes examples of manipulating meshes.

| Example Name | Description | Image |
| --- | --- | --- |
| [ClosedSurface](PythonicAPI/PolyData/ClosedSurface.md) | Check if a surface is closed. |  |
| [DeformPointSet](PythonicAPI/Meshes/DeformPointSet.md) | Use the [vtkDeformPointSet](https://www.vtk.org/doc/nightly/html/classvtkDeformPointSet.html) filter to deform a [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html) with arbitrary polydata. |  |
|  |  |  |
| [DelaunayMesh](PythonicAPI/Modelling/DelaunayMesh.md) | Two-dimensional Delaunay triangulation of a random set of points. Points and edges are shown highlighted with sphere glyphs and tubes. |  |
|  |  |  |
| [DijkstraGraphGeodesicPath](PythonicAPI/PolyData/DijkstraGraphGeodesicPath.md) | Find the shortest path between two points on a mesh. |  |
|  |  |  |
| [ElevationFilter](PythonicAPI/Meshes/ElevationFilter.md) | Color a mesh by height. |  |
|  |  |  |
| [FillHoles](PythonicAPI/Meshes/FillHoles.md) | Close holes in a mesh. |  |
|  |  |  |
| [FitToHeightMap](PythonicAPI/Meshes/FitToHeightMap.md) | Drape a polydata over an elevation map. |  |
|  |  |  |
| [GreedyTerrainDecimation](PythonicAPI/PolyData/GreedyTerrainDecimation.md) | Create a mesh from an ImageData |  |
|  |  |  |
| [HighlightBadCells](PythonicAPI/PolyData/HighlightBadCells.md) |  |  |
|  |  |  |
| [IdentifyHoles](PythonicAPI/Meshes/IdentifyHoles.md) | Close holes in a mesh and identify the holes. |  |
|  |  |  |
| [ImplicitSelectionLoop](PythonicAPI/PolyData/ImplicitSelectionLoop.md) | Select a region of a mesh with an implicit function. |  |
|  |  |  |
| [InterpolateFieldDataDemo](PythonicAPI/Meshes/InterpolateFieldDataDemo.md) | Resample a fine grid and interpolate field data. |  |
|  |  |  |
| [MeshQuality](PythonicAPI/PolyData/MeshQuality.md) |  |  |
|  |  |  |
| [MatrixMathFilter](PythonicAPI/Meshes/MatrixMathFilter.md) | Compute various quantities on cells and points in a mesh. |  |
|  |  |  |
| [OBBDicer](PythonicAPI/Meshes/OBBDicer.md) | Breakup a mesh into pieces. |  |
|  |  |  |
| [PointInterpolator](PythonicAPI/Meshes/PointInterpolator.md) | Plot a scalar field of points onto a PolyData surface. |  |
|  |  |  |
| [SplitPolyData](PythonicAPI/Meshes/SplitPolyData.md) | Breakup a mesh into pieces and save the pieces into files |  |
|  |  |  |

#### Clipping

| Example Name | Description | Image |
| --- | --- | --- |
| [BoxClipStructuredPoints](PythonicAPI/Visualization/BoxClipStructuredPoints.md) | Clip [vtkStructuredPoints](https://www.vtk.org/doc/nightly/html/classvtkStructuredPoints.html) with a box. The results are unstructured grids with tetrahedra. |  |
|  |  |  |
| [BoxClipUnstructuredGrid](PythonicAPI/Visualization/BoxClipUnstructuredGrid.md) | Clip a [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html) with a box. The results are unstructured grids with tetrahedra. |  |
|  |  |  |
| [ClipClosedSurface](PythonicAPI/Meshes/ClipClosedSurface.md) | Clip a surface with multiple planes. |  |
|  |  |  |
| [ClipDataSetWithPolyData](PythonicAPI/Meshes/ClipDataSetWithPolyData.md) | Clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with arbitrary polydata. In this example, use a [vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) to generate polydata to slice the grid, resulting in an unstructured grid. |  |
|  |  |  |
| [ClipDataSetWithPolyData1](PythonicAPI/Meshes/ClipDataSetWithPolyData1.md) | Clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with arbitrary polydata. In this example, use a [vtkConeSource](https://www.vtk.org/doc/nightly/html/classvtkConeSource.html) to generate polydata to slice the grid, resulting in an unstructured grid. |  |
|  |  |  |
| [ImplicitDataSetClipping](PythonicAPI/PolyData/ImplicitDataSetClipping.md) | Clip using an implicit data set. |  |
|  |  |  |
| [SolidClip](PythonicAPI/Meshes/SolidClip.md) | Create a "solid" clip. The "ghost" of the part clipped away is also shown. |  |
|  |  |  |
| [TableBasedClipDataSetWithPolyData2](PythonicAPI/Meshes/TableBasedClipDataSetWithPolyData2.md) | Clip a [vtkRectilinearGrid](https://www.vtk.org/doc/nightly/html/classvtkRectilinearGrid.html) with a checkerboard pattern. |  |
|  |  |  |

### Working with Structured 3D Data

#### vtkImageData

| Example Name | Description | Image |
| --- | --- | --- |
| [ClipVolume](PythonicAPI/ImageData/ClipVolume.md) | Clip a volume and produce a vtkUnhstructuredGrid. |  |
|  |  |  |
| [ImageIterator](PythonicAPI/ImageData/ImageIterator.md) |  |  |
| [ImageIteratorDemo](PythonicAPI/ImageData/ImageIteratorDemo.md) | Demonstrate using indexing to access pixels in a region. |  |
|  |  |  |
| [ImageTranslateExtent](PythonicAPI/ImageData/ImageTranslateExtent.md) | Change the extent of a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html). |  |
|  |  |  |
| [ImageWeightedSum](PythonicAPI/ImageData/ImageWeightedSum.md) | Add two or more images. |  |
|  |  |  |

#### vtkExplicitStructuredGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [CreateESGrid](PythonicAPI/ExplicitStructuredGrid/CreateESGrid.md) | Create an explicit structured grid and convert this to an unstructured grid or vice versa. |  |
|  |  |  |
| [LoadESGrid](PythonicAPI/ExplicitStructuredGrid/LoadESGrid.md) | Load a VTU file and convert the dataset to an explicit structured grid. |  |
|  |  |  |

#### vtkStructuredGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [BlankPoint](PythonicAPI/StructuredGrid/BlankPoint.md) | Blank a point of a [vtkStructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkStructuredGrid.html). |  |
|  |  |  |
| [SGrid](PythonicAPI/StructuredGrid/SGrid.md) | Creating a structured grid dataset of a semi-cylinder. Vectors are created whose magnitude is proportional to radius and oriented in tangential direction. |  |
|  |  |  |

#### vtkStructuredPoints

| Example Name | Description | Image |
| --- | --- | --- |
| [Vol](PythonicAPI/StructuredPoints/Vol.md) | Creating a image data dataset. Scalar data is generated from the equation for a sphere. Volume dimensions are 26 x 26 x 26. |  |
|  |  |  |

#### vtkRectilinearGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [RGrid](PythonicAPI/RectilinearGrid/RGrid.md) | Creating a rectilinear grid dataset. The coordinates along each axis are defined using an instance of [vtkDataArray](https://www.vtk.org/doc/nightly/html/classvtkDataArray.html). |  |
|  |  |  |
| [VisualizeRectilinearGrid](PythonicAPI/RectilinearGrid/VisualizeRectilinearGrid.md) | Visualize the cells of a rectilinear grid. |  |
|  |  |  |

### Working with Unstructured 3D Data

This section includes vtkUnstructuredGrid.

#### vtkUnstructuredGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [ClipUnstructuredGridWithPlane](PythonicAPI/UnstructuredGrid/ClipUnstructuredGridWithPlane.md) | Clip a UGrid with a plane. |  |
|  |  |  |
| [ClipUnstructuredGridWithPlane2](PythonicAPI/UnstructuredGrid/ClipUnstructuredGridWithPlane2.md) | Clip a UGrid with a plane. |  |
|  |  |  |

### Registration

### Medical

| Example Name | Description | Image |
| --- | --- | --- |
| [GenerateCubesFromLabels](PythonicAPI/Medical/GenerateCubesFromLabels.md) | Create cubes from labeled volume data. |  |
|  |  |  |
| [GenerateModelsFromLabels](PythonicAPI/Medical/GenerateModelsFromLabels.md) | Create models from labeled volume data. |  |
| [MedicalDemo1](PythonicAPI/Medical/MedicalDemo1.md) | Create a skin surface from volume data. |  |
|  |  |  |
| [MedicalDemo2](PythonicAPI/Medical/MedicalDemo2.md) | Create a skin and bone surface from volume data. |  |
|  |  |  |
| [MedicalDemo3](PythonicAPI/Medical/MedicalDemo3.md) | Create skin and tissue slices from volume data. |  |
|  |  |  |
| [MedicalDemo4](PythonicAPI/Medical/MedicalDemo4.md) | Create a volume rendering. |  |
|  |  |  |
| [TissueLens](PythonicAPI/Medical/TissueLens.md) | A "magnifying lens" or "window" effect is generated, allowing users to peek inside a 3D medical dataset. |  |
|  |  |  |

### Surface reconstruction

| Example Name | Description | Image |
| --- | --- | --- |
| [Delaunay3DDemo](PythonicAPI/Modelling/Delaunay3DDemo.md) | Interactively adjust Alpha for Delaunay3D. |  |
|  |  |  |

## Utilities

| Example Name | Description | Image |
| --- | --- | --- |
| [BoundingBox](PythonicAPI/Utilities/BoundingBox.md) | Bounding Box construction. |  |
| [BoundingBoxIntersection](PythonicAPI/Utilities/BoundingBoxIntersection.md) | Box intersection and Inside tests. |  |
| [CheckVTKVersion](PythonicAPI/Utilities/CheckVTKVersion.md) | Check the VTK version and provide alternatives for different VTK versions. |  |
| [ClassesInLang1NotInLang2](PythonicAPI/Utilities/ClassesInLang1NotInLang2.md) | Select VTK classes with corresponding examples in one language but not in another. |  |
| [ConstrainedDelaunay2D](PythonicAPI/Filtering/ConstrainedDelaunay2D.md) | Perform a 2D Delaunay triangulation on a point set respecting a specified boundary. |  |
|  |  |  |
| [Delaunay2D](PythonicAPI/Filtering/Delaunay2D.md) | Perform a 2D Delaunay triangulation on a point set. |  |
|  |  |  |
| [FileOutputWindow](PythonicAPI/Utilities/FileOutputWindow.md) | Write errors to a log file instead of the usual vtk pop-up window. |  |
| [JSONColorMapToLUT](PythonicAPI/Utilities/JSONColorMapToLUT.md) | Take a JSON description of a colormap and convert it to a VTK colormap. |  |
|  |  |  |
| [ColorMapToLUT](PythonicAPI/Utilities/ColorMapToLUT.md) | Use [vtkDiscretizableColorTransferFunction](https://www.vtk.org/doc/nightly/html/classvtkDiscretizableColorTransferFunction.html) to generate a VTK colormap. |  |
|  |  |  |
| [DetermineActorType](PythonicAPI/Utilities/DetermineActorType.md) | Determine the type of an actor. |  |
|  |  |  |
| [MassProperties](PythonicAPI/Utilities/MassProperties.md) | Compute volume and surface area of a closed, triangulated mesh. |  |
| [MultipleRenderWindows](PythonicAPI/Visualization/MultipleRenderWindows.md) | Multiple Render Windows. |  |
|  |  |  |
| [MultipleViewports](PythonicAPI/Visualization/MultipleViewports.md) | Multiple Viewports. |  |
|  |  |  |
| [OffScreenRendering](PythonicAPI/Utilities/OffScreenRendering.md) | Off Screen Rendering. |  |
| [PassThrough](PythonicAPI/InfoVis/PassThrough.md) | Pass input along to output. |  |
| [PCADemo](PythonicAPI/Utilities/PCADemo.md) | Project 2D points onto the best 1D subspace using PCA values. |  |
|  |  |  |
| [PCAStatistics](PythonicAPI/Utilities/PCAStatistics.md) | Compute Principal Component Analysis (PCA) values. |  |
| [RescaleReverseLUT](PythonicAPI/Utilities/RescaleReverseLUT.md) | Demonstrate how to adjust a colormap so that the colormap scalar range matches the scalar range on the object. You can optionally reverse the colors. |  |
|  |  |  |
| [ResetCameraOrientation](PythonicAPI/Utilities/ResetCameraOrientation.md) | Reset camera orientation to a previously saved orientation. |  |
|  |  |  |
| [SaveSceneToFieldData](PythonicAPI/Utilities/SaveSceneToFieldData.md) | Save a [vtkCamera](https://www.vtk.org/doc/nightly/html/classvtkCamera.html)'s state in a [vtkDataSet](https://www.vtk.org/doc/nightly/html/classvtkDataSet.html)'s [vtkFieldData](https://www.vtk.org/doc/nightly/html/classvtkFieldData.html) and restore it. |  |
|  |  |  |
| [SaveSceneToFile](PythonicAPI/Utilities/SaveSceneToFile.md) | Save a [vtkCamera](https://www.vtk.org/doc/nightly/html/classvtkCamera.html)'s state in a file and restore it. |  |
|  |  |  |
| [Screenshot](PythonicAPI/Utilities/Screenshot.md) |  |  |
|  |  |  |
| [SelectExamples](PythonicAPI/Utilities/SelectExamples.md) | Given a VTK Class and a language, select the matching examples. |  |
| [ShareCamera](PythonicAPI/Utilities/ShareCamera.md) | Share a camera between multiple renderers. |  |
|  |  |  |
| [VTKWithNumpy](PythonicAPI/Utilities/VTKWithNumpy.md) |  |  |
|  |  |  |
| [XMLColorMapToLUT](PythonicAPI/Utilities/XMLColorMapToLUT.md) | Take an XML description of a colormap and convert it to a VTK colormap. |  |
|  |  |  |

### Arrays

| Example Name | Description | Image |
| --- | --- | --- |
| [ArrayCalculator](PythonicAPI/Utilities/ArrayCalculator.md) | Perform in-place operations on arrays. |  |
| [ArrayToTable](PythonicAPI/InfoVis/ArrayToTable.md) | Convert a [vtkDenseArray](https://www.vtk.org/doc/nightly/html/classvtkDenseArray.html) to a [vtkTable](https://www.vtk.org/doc/nightly/html/classvtkTable.html). |  |
| [ArrayWriter](PythonicAPI/Utilities/ArrayWriter.md) | Write a DenseArray or SparseArray to a file. |  |
| [ExtractArrayComponent](PythonicAPI/Utilities/ExtractArrayComponent.md) | Extract a component of an array. |  |

### Events

## Math Operations

| Example Name | Description | Image |
| --- | --- | --- |
| [MatrixInverse](PythonicAPI/Math/MatrixInverse.md) | Matrix inverse. |  |
| [MatrixTranspose](PythonicAPI/Math/MatrixTranspose.md) | Matrix transpose. |  |

## Graphs

| Example Name | Description | Image |
| --- | --- | --- |
| [AdjacencyMatrixToEdgeTable](PythonicAPI/Graphs/AdjacencyMatrixToEdgeTable.md) | Convert an adjacency matrix to an edge table. |  |
| [AdjacentVertexIterator](PythonicAPI/Graphs/AdjacentVertexIterator.md) | Get all vertices connected to a specified vertex. |  |
|  |  |  |
| [ConstructTree](PythonicAPI/Graphs/ConstructTree.md) | Construct a tree. |  |
|  |  |  |
| [CreateTree](PythonicAPI/Graphs/CreateTree.md) | Create a tree and label the vertices and edges. |  |
|  |  |  |
| [EdgeListIterator](PythonicAPI/Graphs/EdgeListIterator.md) | Iterate over edges of a graph. |  |
| [GraphToPolyData](PythonicAPI/Graphs/GraphToPolyData.md) | Convert a graph to a PolyData. |  |
|  |  |  |
| [InEdgeIterator](PythonicAPI/Graphs/InEdgeIterator.md) | Iterate over edges incoming to a vertex. |  |
| [LabelVerticesAndEdges](PythonicAPI/Graphs/LabelVerticesAndEdges.md) | Label vertices and edges. |  |
|  |  |  |
| [MutableGraphHelper](PythonicAPI/InfoVis/MutableGraphHelper.md) | Create either a [vtkMutableDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkMutableDirectedGraph.html) or [vtkMutableUndirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkMutableUndirectedGraph.html). |  |
|  |  |  |
| [OutEdgeIterator](PythonicAPI/Graphs/OutEdgeIterator.md) | Iterate over edges outgoing from a vertex. |  |
| [RandomGraphSource](PythonicAPI/Graphs/RandomGraphSource.md) | Create a random graph. |  |
|  |  |  |
| [SideBySideGraphs](PythonicAPI/Graphs/SideBySideGraphs.md) | Display two graphs side by side. |  |
|  |  |  |
| [ScaleVertices](PythonicAPI/Graphs/ScaleVertices.md) | Size/scale vertices based on a data array. |  |
|  |  |  |
| [SelectedVerticesAndEdges](PythonicAPI/Graphs/SelectedVerticesAndEdges.md) | Get a list of selected vertices and edges. |  |
|  |  |  |
| [SelectedVerticesAndEdgesObserver](PythonicAPI/Graphs/SelectedVerticesAndEdgesObserver.md) | Get a list of selected vertices and edges using an observer of AnnotationChangedEvent. |  |
|  |  |  |
| [VisualizeDirectedGraph](PythonicAPI/Graphs/VisualizeDirectedGraph.md) | Visualize a directed graph. |  |
|  |  |  |

### Graph Conversions

| Example Name | Description | Image |
| --- | --- | --- |
| [DirectedGraphToMutableDirectedGraph](PythonicAPI/Graphs/DirectedGraphToMutableDirectedGraph.md) | [vtkDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkDirectedGraph.html) to [vtkMutableDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkMutableDirectedGraph.html). |  |
| [MutableDirectedGraphToDirectedGraph](PythonicAPI/Graphs/MutableDirectedGraphToDirectedGraph.md) | [vtkMutableDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkMutableDirectedGraph.html) to [vtkDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkDirectedGraph.html). |  |
| [TreeToMutableDirectedGraph](PythonicAPI/Graphs/TreeToMutableDirectedGraph.md) | [vtkTree](https://www.vtk.org/doc/nightly/html/classvtkTree.html) to [vtkMutableDirectedGraph](https://www.vtk.org/doc/nightly/html/classvtkMutableDirectedGraph.html) |  |

## Data Structures

| Example Name | Description | Image |
| --- | --- | --- |
| [AttachAttributes](PythonicAPI/PolyData/AttachAttributes.md) | Attach attributes to a VTK array. |  |
| [CellTreeLocator](PythonicAPI/PolyData/CellTreeLocator.md) | Points on an object using [vtkCellTreeLocator](https://www.vtk.org/doc/nightly/html/classvtkCellTreeLocator.html). |  |

### Timing Demonstrations

### KD-Tree

| Example Name | Description | Image |
| --- | --- | --- |
| [DataStructureComparison](PythonicAPI/DataStructures/DataStructureComparison.md) | Illustrates, side by side, the differences between several spatial data structures |  |
|  |  |  |
| [KDTree](PythonicAPI/DataStructures/KDTree.md) |  |  |
| [KDTreeAccessPoints](PythonicAPI/DataStructures/KDTreeAccessPoints.md) | Access the points of a KDTree. |  |
| [VisualizeKDTree](PythonicAPI/DataStructures/VisualizeKDTree.md) | Visualize levels of the tree. |  |
|  |  |  |

### Oriented Bounding Box (OBB) Tree

| Example Name | Description | Image |
| --- | --- | --- |
| [OBBTreeExtractCells](PythonicAPI/DataStructures/OBBTreeExtractCells.md) | Intersect a line with an OBB Tree and display all intersected cells. |  |
|  |  |  |
| [OBBTreeIntersectWithLine](PythonicAPI/DataStructures/OBBTreeIntersectWithLine.md) | Intersect a line with an [vtkOBBTree](https://www.vtk.org/doc/nightly/html/classvtkOBBTree.html). |  |
| [VisualizeOBBTree](PythonicAPI/DataStructures/VisualizeOBBTree.md) | Visualize levels of the tree. |  |
|  |  |  |

### Octree

| Example Name | Description | Image |
| --- | --- | --- |
| [OctreeVisualize](PythonicAPI/DataStructures/OctreeVisualize.md) | Visualize levels of the tree. |  |
|  |  |  |

### Modified BSP Tree

| Example Name | Description | Image |
| --- | --- | --- |
| [IncrementalOctreePointLocator](PythonicAPI/DataStructures/IncrementalOctreePointLocator.md) | Insert points into an octree without rebuilding it. |  |
| [ModifiedBSPTreeExtractCells](PythonicAPI/DataStructures/ModifiedBSPTreeExtractCells.md) | Intersect a line with a modified BSP Tree and display all intersected cells. |  |
|  |  |  |
| [VisualizeModifiedBSPTree](PythonicAPI/DataStructures/VisualizeModifiedBSPTree.md) | Visualize levels of the tree. |  |
|  |  |  |

### HyperTreeGrid

| Example Name | Description | Image |
| --- | --- | --- |
| [HyperTreeGridSource](PythonicAPI/HyperTreeGrid/HyperTreeGridSource.md) | Create a [vtkHyperTreeGrid](https://www.vtk.org/doc/nightly/html/classvtkHyperTreeGrid.html). |  |
|  |  |  |

## VTK Concepts

## Rendering

| Example Name | Description | Image |
| --- | --- | --- |
| [ColoredSphere](PythonicAPI/Rendering/ColoredSphere.md) | A simple sphere. |  |
|  |  |  |
| [GradientBackground](PythonicAPI/Rendering/GradientBackground.md) | Demonstrates the background shading options. |  |
|  |  |  |
| [InterpolateCamera](PythonicAPI/Rendering/InterpolateCamera.md) | Use [vtkCameraInterpolator](https://www.vtk.org/doc/nightly/html/classvtkCameraInterpolator.html) to generate a smooth interpolation between camera views. |  |
|  |  |  |
| [LayeredActors](PythonicAPI/Rendering/LayeredActors.md) | Demonstrates the use of two linked renderers. The orientation of objects in the non active layer is linked to those in the active layer. |  |
|  |  |  |
| [MotionBlur](PythonicAPI/Rendering/MotionBlur.md) | Example of motion blur. |  |
|  |  |  |
| [MultipleLayersAndWindows](PythonicAPI/Rendering/MultipleLayersAndWindows.md) | Demonstrates the use of four renderers in two layers. |  |
|  |  |  |
| [OutlineGlowPass](PythonicAPI/Rendering/OutlineGlowPass.md) | Demonstrates how to render a object in a scene with a glowing outline. |  |
|  |  |  |
| [PBR_Anisotropy](PythonicAPI/Rendering/PBR_Anisotropy.md) | Render spheres with different anisotropy values. |  |
|  |  |  |
| [PBR_Clear_Coat](PythonicAPI/Rendering/PBR_Clear_Coat.md) | Render a cube with custom texture mapping and a coat normal texture. |  |
|  |  |  |
| [PBR_Edge_Tint](PythonicAPI/Rendering/PBR_Edge_Tint.md) | Render spheres with different edge colors using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_HDR_Environment](PythonicAPI/Rendering/PBR_HDR_Environment.md) | Renders spheres with different materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Mapping](PythonicAPI/Rendering/PBR_Mapping.md) | Render a cube with custom texture mapping. |  |
|  |  |  |
| [PBR_Materials](PythonicAPI/Rendering/PBR_Materials.md) | Renders spheres with different materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Materials_Coat](PythonicAPI/Rendering/PBR_Materials_Coat.md) | Render spheres with different coat materials using a skybox as image based lighting. |  |
|  |  |  |
| [PBR_Skybox](PythonicAPI/Rendering/PBR_Skybox.md) | Demonstrates physically based rendering, a skybox and image based lighting. |  |
|  |  |  |
| [PBR_Skybox_Texturing](PythonicAPI/Rendering/PBR_Skybox_Texturing.md) | Demonstrates physically based rendering, a skybox, image based lighting and texturing. |  |
|  |  |  |
| [PBR_Skybox_Anisotropy](PythonicAPI/Rendering/PBR_Skybox_Anisotropy.md) | Demonstrates physically based rendering, a skybox, image based lighting, and anisotropic texturing. |  |
|  |  |  |
| [Shadows](PythonicAPI/Rendering/Shadows.md) | Draw model with shadows. |  |
|  |  |  |
| [StringToImageDemo](PythonicAPI/Rendering/StringToImageDemo.md) | Demonstrates how to generate images from strings. |  |
|  |  |  |
| [StripFran](PythonicAPI/Rendering/StripFran.md) | Triangle strip examples. (a) Structured triangle mesh consisting of 134 strips each of 390 triangles. (b) Unstructured triangle mesh consisting of 2227 strips of average length 3.94, longest strip 101 triangles. Images are generated by displaying every other triangle strip. |  |
|  |  |  |
| [TransformSphere](PythonicAPI/Rendering/TransformSphere.md) | The addition of a transform filter to [ColoredSphere](PythonicAPI/Rendering/ColoredSphere.md). |  |
|  |  |  |
| [TransparentBackground](PythonicAPI/Rendering/TransparentBackground.md) | Demonstrates the use of two renderers. Notice that the second (and subsequent) renderers will have a transparent background. |  |
|  |  |  |

## Lighting

| Example Name | Description | Image |
| --- | --- | --- |
| [Light](PythonicAPI/Lighting/Light.md) | Add a directional light to a scene. |  |
|  |  |  |
| [ShadowsLightsDemo](PythonicAPI/Visualization/ShadowsLightsDemo.md) | Show lights casting shadows. |  |
|  |  |  |

## Shaders

| Example Name | Description | Image |
| --- | --- | --- |
| [MarbleShaderDemo](PythonicAPI/Shaders/MarbleShaderDemo.md) | Explore the parameter space with the sliders. |  |
|  |  |  |

## Texture Mapping

| Example Name | Description | Image |
| --- | --- | --- |
| [AnimateVectors](PythonicAPI/Texture/AnimateVectors.md) | One frame from a vector field animation using texture maps. |  |
|  |  |  |
| [TextureCutQuadric](PythonicAPI/Texture/TextureCutQuadric.md) | Cut a quadric with boolean textures. |  |
|  |  |  |
| [TextureCutSphere](PythonicAPI/Texture/TextureCutSphere.md) | Examples of texture thresholding using a boolean combination of two planes to cut nested spheres. |  |
|  |  |  |
| [TexturePlane](PythonicAPI/Texture/TexturePlane.md) | Example of texture mapping. |  |
|  |  |  |
| [TextureThreshold](PythonicAPI/Texture/TextureThreshold.md) | Demonstrate the use of scalar thresholds to show values of flow density on three planes. |  |
|  |  |  |
| [TexturedSphere](PythonicAPI/Texture/TexturedSphere.md) | Texture a sphere. |  |
|  |  |  |

## Tutorial

If you are new to VTK then these tutorials will help to get you started.

## Video

| Example Name | Description | Image |
| --- | --- | --- |
| [OggTheora](PythonicAPI/Video/OggTheora.md) | Write out an AVI file. |  |

## Visualization

See [this tutorial](http://www.vtk.org/Wiki/VTK/Tutorials/3DDataTypes) for a brief explanation of the VTK terminology of mappers, actors, etc.

| Example Name | Description | Image |
| --- | --- | --- |
| [AnnotatedCubeActor](PythonicAPI/Visualization/AnnotatedCubeActor.md) | Annotated cube. |  |
|  |  |  |
| [AssignCellColorsFromLUT](PythonicAPI/Visualization/AssignCellColorsFromLUT.md) | Demonstrates how to assign colors to cells in a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html) structure using lookup tables. |  |
|  |  |  |
| [AxisActor](PythonicAPI/Visualization/AxisActor.md) | Generate a single axis. |  |
|  |  |  |
| [BillboardTextActor3D](PythonicAPI/Visualization/BillboardTextActor3D.md) | Label points with billboards. |  |
|  |  |  |
| [Blow](PythonicAPI/Visualization/Blow.md) | Ten frames from a blow molding finite element analysis. |  |
|  |  |  |
| [CameraActor](PythonicAPI/Visualization/CameraActor.md) | Visualize a camera (frustum) in a scene. |  |
|  |  |  |
| [CameraModel1](PythonicAPI/Visualization/CameraModel1.md) | Illustrate camera movement around the focal point. |  |
|  |  |  |
| [CameraModel2](PythonicAPI/Visualization/CameraModel2.md) | Illustrate camera movement centered at the camera position. |  |
|  |  |  |
| [CaptionActor2D](PythonicAPI/Visualization/CaptionActor2D.md) | Draw a caption/bubble pointing to a particular point. |  |
|  |  |  |
| [ClipSphereCylinder](PythonicAPI/VisualizationAlgorithms/ClipSphereCylinder.md) | A plane clipped with a sphere and an ellipse. The two transforms place each implicit function into the appropriate position. Two outputs are generated by the clipper. |  |
|  |  |  |
| [ColoredAnnotatedCube](PythonicAPI/Visualization/ColoredAnnotatedCube.md) | How to color the individual faces of an annotated cube. |  |
|  |  |  |
| [CollisionDetection](PythonicAPI/Visualization/CollisionDetection.md) | Collison between two spheres. |  |
|  |  |  |
| [CombineImportedActors](PythonicAPI/PolyData/CombineImportedActors.md) | Combine actors from a scene into one actor. |  |
|  |  |  |
| [CornerAnnotation](PythonicAPI/Visualization/CornerAnnotation.md) | Write text in the corners of a window. |  |
|  |  |  |
| [CorrectlyRenderTranslucentGeometry](PythonicAPI/Visualization/CorrectlyRenderTranslucentGeometry.md) | Correctly Rendering Translucent Geometry. |  |
|  |  |  |
| [CreateBFont](PythonicAPI/VisualizationAlgorithms/CreateBFont.md) | A scanned image clipped with a scalar value of 1/2 its maximum intensity produces a mixture of quadrilaterals and triangles. |  |
|  |  |  |
| [CubeAxesActor](PythonicAPI/Visualization/CubeAxesActor.md) | Display three orthogonal axes with with labels. |  |
|  |  |  |
| [CubeAxesActor2D](PythonicAPI/Visualization/CubeAxesActor2D.md) | This example uses the [vtkCubeAxesActor2D](https://www.vtk.org/doc/nightly/html/classvtkCubeAxesActor2D.html) to show your scene with axes to indicate the spatial extent of your data. |  |
|  |  |  |
| [Cursor2D](PythonicAPI/Visualization/Cursor2D.md) |  |  |
|  |  |  |
| [Cursor3D](PythonicAPI/Visualization/Cursor3D.md) |  |  |
|  |  |  |
| [CurvatureBandsWithGlyphs](PythonicAPI/Visualization/CurvatureBandsWithGlyphs.md) | Demonstrates the coloring of a surface by partitioning the gaussian curvature of a surface into bands and using arrows to display the normals on the surface. |  |
|  |  |  |
| [Curvatures](PythonicAPI/Visualization/Curvatures.md) | Compute either Mean or Gaussian Curvatures with adjustments for edge effects. |  |
|  |  |  |
| [CurvaturesAdjustEdges](PythonicAPI/Visualization/CurvaturesAdjustEdges.md) | Get the Gaussian and Mean curvatures of a surface with adjustments for edge effects. |  |
|  |  |  |
| [CurvaturesDemo](PythonicAPI/Visualization/CurvaturesDemo.md) | Demonstrates how to get the Gaussian and Mean curvatures of a surface. |  |
|  |  |  |
| [CurvaturesNormalsElevations](PythonicAPI/Visualization/CurvaturesNormalsElevations.md) | Gaussian and Mean curvatures of a surface with arrows colored by elevation to display the normals. The surfaces are also adjusted for edge effects. |  |
|  |  |  |
| [DataSetSurface](PythonicAPI/VisualizationAlgorithms/DataSetSurface.md) | Cutting a hexahedron with a plane. The red line on the surface shows the cut. |  |
|  |  |  |
| [DepthSortPolyData](PythonicAPI/Visualization/DepthSortPolyData.md) | Poly Data Depth Sorting. |  |
|  |  |  |
| [DisplacementPlot](PythonicAPI/VisualizationAlgorithms/DisplacementPlot.md) | Show modal lines for a vibrating beam. |  |
|  |  |  |
| [DistanceToCamera](PythonicAPI/Visualization/DistanceToCamera.md) |  |  |
|  |  |  |
| [EdgePoints](PythonicAPI/Visualization/EdgePoints.md) | Generate points along an edge. |  |
|  |  |  |
| [ElevationBandsWithGlyphs](PythonicAPI/Visualization/ElevationBandsWithGlyphs.md) | Demonstrates the coloring of a surface by partitioning the elevation into bands and using arrows to display the normals on the surface. |  |
|  |  |  |
| [FastSplatter](PythonicAPI/Visualization/FastSplatter.md) | Convolve a splat image with every point in an input image. |  |
|  |  |  |
| [FireFlow](PythonicAPI/VisualizationAlgorithms/FireFlow.md) | Combine geometry from a VRML file and a solution from a [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html) file. |  |
|  |  |  |
| [FireFlowDemo](PythonicAPI/VisualizationAlgorithms/FireFlowDemo.md) | Combine geometry from a VRML file and a solution from a [vtkUnstructuredGrid](https://www.vtk.org/doc/nightly/html/classvtkUnstructuredGrid.html) file (interactive). |  |
|  |  |  |
| [FlyingHeadSlice](PythonicAPI/VisualizationAlgorithms/FlyingHeadSlice.md) | Flying edges used to generate contour lines. |  |
|  |  |  |
| [FroggieSurface](PythonicAPI/Visualization/FroggieSurface.md) | Construct surfaces from a segmented frog dataset. Up to fifteen different surfaces may be extracted. You can turn on and off surfaces and control the camera position. |  |
|  |  |  |
| [FroggieView](PythonicAPI/Visualization/FroggieView.md) | View surfaces of a segmented frog dataset using preprocessed `*.vtk` tissue files. You can turn on and off surfaces, control their opacity through the use of sliders and control the camera position. |  |
|  |  |  |
| [Hanoi](PythonicAPI/Visualization/Hanoi.md) | Towers of Hanoi. |  |
|  |  |  |
| [HanoiInitial](PythonicAPI/Visualization/HanoiInitial.md) | Towers of Hanoi - Initial configuration. |  |
|  |  |  |
| [HanoiIntermediate](PythonicAPI/Visualization/HanoiIntermediate.md) | Towers of Hanoi - Intermediate configuration. |  |
|  |  |  |
| [HeadBone](PythonicAPI/VisualizationAlgorithms/HeadBone.md) | Marching cubes surface of human bone. |  |
|  |  |  |
| [HyperStreamline](PythonicAPI/VisualizationAlgorithms/HyperStreamline.md) | Example of hyperstreamlines, the four hyperstreamlines shown are integrated along the minor principal stress axis. A plane (colored with a different lookup table) is also shown. |  |
|  |  |  |
| [IsosurfaceSampling](PythonicAPI/Visualization/IsosurfaceSampling.md) | Demonstrates how to create point data on an isosurface. |  |
|  |  |  |
| [Kitchen](PythonicAPI/Visualization/Kitchen.md) | Demonstrates stream tracing in a kitchen. |  |
|  |  |  |
| [LODProp3D](PythonicAPI/Visualization/LODProp3D.md) | Level of detail rendering. |  |
|  |  |  |
| [LOx](PythonicAPI/VisualizationAlgorithms/LOx.md) | Streamtubes created by using the computational grid just in front of the post as a source for seeds. |  |
|  |  |  |
| [LOxGrid](PythonicAPI/VisualizationAlgorithms/LOxGrid.md) | Portion of computational grid for the LOx post. |  |
|  |  |  |
| [LOxSeeds](PythonicAPI/VisualizationAlgorithms/LOxSeeds.md) | Streamlines seeded with spherical cloud of points. Four separate cloud positions are shown. |  |
|  |  |  |
| [LabelPlacementMapper](PythonicAPI/Visualization/LabelPlacementMapper.md) | Display a non-overlapping text label at each point. |  |
|  |  |  |
| [LabeledMesh](PythonicAPI/Visualization/LabeledMesh.md) | Label Mesh. |  |
|  |  |  |
| [LoopShrink](PythonicAPI/Visualization/LoopShrink.md) | A network with a loop. VTK 5.0 and later do not allow you to execute a looping visualization network; this was possible in previous versions of VTK. |  |
|  |  |  |
| [Motor](PythonicAPI/VisualizationAlgorithms/Motor.md) | Texture cut used to reveal internal structure of a motor. Two cut planes are used in combination with transparent texture. |  |
|  |  |  |
| [MovableAxes](PythonicAPI/Visualization/MovableAxes.md) | Movable axes. |  |
|  |  |  |
| [Office](PythonicAPI/VisualizationAlgorithms/Office.md) | Using random point seeds to create streamlines. |  |
|  |  |  |
| [OfficeA](PythonicAPI/VisualizationAlgorithms/OfficeA.md) | Corresponds to Fig 9-47(a) in the VTK textbook. |  |
|  |  |  |
| [OfficeTube](PythonicAPI/VisualizationAlgorithms/OfficeTube.md) | The stream polygon. Sweeping a polygon to form a tube. |  |
|  |  |  |
| [ProteinRibbons](PythonicAPI/Visualization/ProteinRibbons.md) | Display Protein Data Bank ribbons. |  |
|  |  |  |
| [PineRootConnectivity](PythonicAPI/VisualizationAlgorithms/PineRootConnectivity.md) | Applying the connectivity filter to remove noisy isosurfaces. |  |
|  |  |  |
| [PineRootConnectivityA](PythonicAPI/VisualizationAlgorithms/PineRootConnectivityA.md) | The isosurface, with no connectivity filter applied. |  |
|  |  |  |
| [PineRootDecimation](PythonicAPI/VisualizationAlgorithms/PineRootDecimation.md) | Applying the decimation and connectivity filters to remove noisy isosurfaces and reduce data size. |  |
|  |  |  |
| [PlateVibration](PythonicAPI/VisualizationAlgorithms/PlateVibration.md) | Demonstrates the motion of a vibrating beam. |  |
|  |  |  |
| [PointDataSubdivision](PythonicAPI/Visualization/PointDataSubdivision.md) | Demonstrates the use of the [vtkLinearSubdivisionFilter](https://www.vtk.org/doc/nightly/html/classvtkLinearSubdivisionFilter.html) and [vtkButterflySubdivisionFilter](https://www.vtk.org/doc/nightly/html/classvtkButterflySubdivisionFilter.html). |  |
|  |  |  |
| [ProgrammableGlyphFilter](PythonicAPI/Visualization/ProgrammableGlyphFilter.md) | Generate a custom glyph at each point. |  |
|  |  |  |
| [ProgrammableGlyphs](PythonicAPI/Visualization/ProgrammableGlyphs.md) | Generate programmable glyphs. |  |
|  |  |  |
| [PseudoVolumeRendering](PythonicAPI/VolumeRendering/PseudoVolumeRendering.md) | Here we use 20 cut planes, each with an opacity of of 0.25. They are then rendered back-to-front to simulate volume rendering. |  |
|  |  |  |
| [QuadricVisualization](PythonicAPI/Visualization/QuadricVisualization.md) | Visualizing a quadric function. |  |
|  |  |  |
| [ReverseAccess](PythonicAPI/Visualization/ReverseAccess.md) | Demonstrates how to access the source (e.g. [vtkSphereSource](https://www.vtk.org/doc/nightly/html/classvtkSphereSource.html)) of an actor reversely. |  |
| [StreamlinesWithLineWidget](PythonicAPI/VisualizationAlgorithms/StreamlinesWithLineWidget.md) | Using the [vtkLineWidget](https://www.vtk.org/doc/nightly/html/classvtkLineWidget.html) to produce streamlines in the combustor dataset. The StartInteractionEvent turns the visibility of the streamlines on; the InteractionEvent causes the streamlines to regenerate themselves. |  |
|  |  |  |
| [TensorEllipsoids](PythonicAPI/VisualizationAlgorithms/TensorEllipsoids.md) | Display the scaled and oriented principal axes as tensor ellipsoids representing the stress tensor. |  |
|  |  |  |
| [TransformActorCollection](PythonicAPI/Visualization/TransformActorCollection.md) | Transform an actor collection. |  |
|  |  |  |
| [VoxelsOnBoundary](PythonicAPI/ImageData/VoxelsOnBoundary.md) | Extract voxels on the border of an isosurface. |  |
|  |  |  |
| [WarpCombustor](PythonicAPI/VisualizationAlgorithms/WarpCombustor.md) | Carpet plots of combustor flow energy in a structured grid. Colors and plane displacement represent energy values. |  |
|  |  |  |

## Working with vtkImageData

| Example Name | Description | Image |
| --- | --- | --- |
| [ImageNormalize](PythonicAPI/ImageData/ImageNormalize.md) | Normalize an image. |  |
|  |  |  |
| [WriteReadVtkImageData](PythonicAPI/ImageData/WriteReadVtkImageData.md) | Generate, edit and read out vtk image data. |  |
|  |  |  |

## Volume Rendering

| Example Name | Description | Image |
| --- | --- | --- |
| [IntermixedUnstructuredGrid](PythonicAPI/VolumeRendering/IntermixedUnstructuredGrid.md) | A mix of poly data and unstructured grid volume mapping. |  |
|  |  |  |
| [MinIntensityRendering](PythonicAPI/VolumeRendering/MinIntensityRendering.md) | Min intensity rendering. |  |
|  |  |  |
| [MultiBlockVolumeMapper](PythonicAPI/VolumeRendering/MultiBlockVolumeMapper.md) | Using a [vtkMultiBlockVolumeMapper](https://www.vtk.org/doc/nightly/html/classvtkMultiBlockVolumeMapper.html) to render a [vtkMultiBlockDataSet](https://www.vtk.org/doc/nightly/html/classvtkMultiBlockDataSet.html) containing eight subvolumes. |  |
|  |  |  |
| [RayCastIsosurface](PythonicAPI/VolumeRendering/RayCastIsosurface.md) | Isosufaces produced by volume rendering. |  |
|  |  |  |

## User Interaction

| Example Name | Description | Image |
| --- | --- | --- |
| [AreaPicking](PythonicAPI/Picking/AreaPicking.md) | Area Picking. |  |
|  |  |  |
| [Assembly](PythonicAPI/Interaction/Assembly.md) | Combine/group actors into an assembly. |  |
|  |  |  |
| [CallBack](PythonicAPI/Interaction/CallBack.md) | Setting up a callback with client data. Two different methods are demonstrated. |  |
|  |  |  |
| [CellPicking](PythonicAPI/Picking/CellPicking.md) | Cell Picking. |  |
|  |  |  |
| [EllipticalButton](PythonicAPI/Interaction/EllipticalButton.md) | Create an elliptical button. |  |
|  |  |  |
| [HighlightPickedActor](PythonicAPI/Picking/HighlightPickedActor.md) | Pick and highlight an actor based on mouse clicks. |  |
|  |  |  |
| [HighlightSelection](PythonicAPI/Picking/HighlightSelection.md) | Highlight selection. |  |
|  |  |  |
| [HighlightWithSilhouette](PythonicAPI/Picking/HighlightWithSilhouette.md) | Highlight a picked actor by adding a silhouette. |  |
|  |  |  |
| [ImageClip](PythonicAPI/Interaction/ImageClip.md) | Demonstrates how to interactively select and display a region of an image. |  |
|  |  |  |
| [ImageRegion](PythonicAPI/Interaction/ImageRegion.md) | Select a region of an image. |  |
|  |  |  |
| [InteractorStyleTrackballActor](PythonicAPI/Interaction/InteractorStyleTrackballActor.md) |  |  |
|  |  |  |
| [InteractorStyleTrackballCamera](PythonicAPI/Interaction/InteractorStyleTrackballCamera.md) |  |  |
|  |  |  |
| [MouseEvents](PythonicAPI/Interaction/MouseEvents.md) | Subclass the interactor style. |  |
|  |  |  |
| [MouseEventsObserver](PythonicAPI/Interaction/MouseEventsObserver.md) | Use an observer. |  |
|  |  |  |
| [RubberBand3D](PythonicAPI/Interaction/RubberBand3D.md) |  |  |
|  |  |  |
| [RubberBandZoom](PythonicAPI/Interaction/RubberBandZoom.md) |  |  |
|  |  |  |
| [StyleSwitch](PythonicAPI/Interaction/StyleSwitch.md) | Choose between multiple interaction modes. |  |
|  |  |  |

## Working with Images

| Example Name | Description | Image |
| --- | --- | --- |
| [BackgroundImage](PythonicAPI/Images/BackgroundImage.md) | Display an image as the "background" of a scene, and render a superquadric in front of it. |  |
|  |  |  |
| [CannyEdgeDetector](PythonicAPI/Images/CannyEdgeDetector.md) | Perform Canny edge detection on an image. |  |
|  |  |  |
| [DotProduct](PythonicAPI/Images/DotProduct.md) | Compute the pixel-wise dot product of two vector images. |  |
|  |  |  |
| [ExtractComponents](PythonicAPI/Images/ExtractComponents.md) | Extract components of an image. This can be used to get, for example, the red channel of an image. |  |
|  |  |  |
| [ImageCityBlockDistance](PythonicAPI/Images/ImageCityBlockDistance.md) | Compute the Manhattan distance from every point to every black point in a binary image. |  |
|  |  |  |
| [ImageGridSource](PythonicAPI/Images/ImageGridSource.md) | Create a image of a grid. |  |
|  |  |  |
| [ImageHistogram](PythonicAPI/Images/ImageHistogram.md) | Compute the histogram of an image. |  |
|  |  |  |
| [ImageMask](PythonicAPI/Images/ImageMask.md) | Mask a region of an image. |  |
|  |  |  |
| [ImageNonMaximumSuppression](PythonicAPI/Images/ImageNonMaximumSuppression.md) | Find peaks in an image using non maximum suppression. |  |
|  |  |  |
| [ImageOpenClose3D](PythonicAPI/Images/ImageOpenClose3D.md) | Open or close (morphologically) an image. |  |
|  |  |  |
| [ImageOrientation](PythonicAPI/Images/ImageOrientation.md) | Reorder the axes of the image. |  |
|  |  |  |
| [ImageRange3D](PythonicAPI/Images/ImageRange3D.md) | Replace every pixel with the range of its neighbors according to a kernel. |  |
|  |  |  |
| [ImageSeparableConvolution](PythonicAPI/Images/ImageSeparableConvolution.md) | Convolve a separable kernel with an image. |  |
|  |  |  |
| [ImageSlice](PythonicAPI/Images/ImageSlice.md) | Visualize and interact with an image. This is even more powerful than [vtkImageSliceMapper](https://www.vtk.org/doc/nightly/html/classvtkImageSliceMapper.html). It can also do oblique slices. |  |
|  |  |  |
| [ImageStack](PythonicAPI/Images/ImageStack.md) | Display layers of images. |  |
|  |  |  |
| [ImageToPolyDataFilter](PythonicAPI/Images/ImageToPolyDataFilter.md) | Convert a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html) to a [vtkPolyData](https://www.vtk.org/doc/nightly/html/classvtkPolyData.html). |  |
|  |  |  |
| [MarkKeypoints](PythonicAPI/Images/MarkKeypoints.md) | Mark keypoints in an image. |  |
|  |  |  |

## Image Processing

| Example Name | Description | Image |
| --- | --- | --- |
| [Attenuation](PythonicAPI/ImageProcessing/Attenuation.md) | This MRI image illustrates attenuation that can occur due to sensor position. The artifact is removed by dividing by the attenuation profile determined manually. |  |
|  |  |  |
| [CenterAnImage](PythonicAPI/Images/CenterAnImage.md) | Center an image. |  |
|  |  |  |
| [CombiningRGBChannels](PythonicAPI/Images/CombiningRGBChannels.md) | Combine layers into an RGB image. |  |
|  |  |  |
| [EnhanceEdges](PythonicAPI/ImageProcessing/EnhanceEdges.md) | High-pass filters can extract and enhance edges in an image. Subtraction of the Laplacian (middle) from the original image (left) results in edge enhancement or a sharpening operation (right). |  |
|  |  |  |
| [GaussianSmooth](PythonicAPI/ImageProcessing/GaussianSmooth.md) | Low-pass filters can be implemented as convolution with a Gaussian kernel. |  |
|  |  |  |
| [HybridMedianComparison](PythonicAPI/ImageProcessing/HybridMedianComparison.md) | Comparison of median and hybrid-median filters. The hybrid filter preserves corners and thin lines, better than the median filter. |  |
|  |  |  |
| [IdealHighPass](PythonicAPI/ImageProcessing/IdealHighPass.md) | This figure shows two high-pass filters in the frequency domain. The Butterworth high-pass filter has a gradual attenuation that avoids ringing produced by the ideal high-pass filter with an abrupt transition. |  |
|  |  |  |
| [ImageContinuousDilate3D](PythonicAPI/Images/ImageContinuousDilate3D.md) | Dilate an image. |  |
|  |  |  |
| [ImageContinuousErode3D](PythonicAPI/Images/ImageContinuousErode3D.md) | Erode an image. |  |
|  |  |  |
| [ImageConvolve](PythonicAPI/Images/ImageConvolve.md) | Convolve an image with a kernel. |  |
|  |  |  |
| [ImageCorrelation](PythonicAPI/Images/ImageCorrelation.md) | Correlate two images. |  |
|  |  |  |
| [ImageDifference](PythonicAPI/Images/ImageDifference.md) | Compute the difference image of two images. |  |
|  |  |  |
| [ImageDivergence](PythonicAPI/Images/ImageDivergence.md) | Divergence of a vector field. |  |
|  |  |  |
| [ImageEllipsoidSource](PythonicAPI/Images/ImageEllipsoidSource.md) | Create an image of an ellipsoid. |  |
|  |  |  |
| [ImageGradient](PythonicAPI/VisualizationAlgorithms/ImageGradient.md) | Create an imaging pipeline to visualize gradient information. |  |
|  |  |  |
| [ImageGradientMagnitude](PythonicAPI/Images/ImageGradientMagnitude.md) | Compute the magnitude of the gradient at each pixel of an image. |  |
|  |  |  |
| [ImagePermute](PythonicAPI/Images/ImagePermute.md) | Reorder the axes of the image. |  |
|  |  |  |
| [ImageSobel2D](PythonicAPI/Images/ImageSobel2D.md) | Sobel edge detection 2D. |  |
|  |  |  |
| [ImageVariance3D](PythonicAPI/Images/ImageVariance3D.md) | Construct a new image consisting of the variance of the input image at each pixel. |  |
|  |  |  |
| [ImageWarp](PythonicAPI/Images/ImageWarp.md) | Combine the imaging and visualization pipelines to deform an image in the z-direction. The [vtkMergeFilter](https://www.vtk.org/doc/nightly/html/classvtkMergeFilter.html) is used to combine the warped surface with the original color data. |  |
|  |  |  |
| [IsoSubsample](PythonicAPI/ImageProcessing/IsoSubsample.md) | This figure demonstrates aliasing that occurs when a high-frequency signal is subsampled. High frequencies appear as low frequency artifacts. The left image is an isosurface of a skull after subsampling. The right image used a low-pass filter before subsampling to reduce aliasing. |  |
|  |  |  |
| [MorphologyComparison](PythonicAPI/ImageProcessing/MorphologyComparison.md) | This figure demonstrates various binary filters that can alter the shape of segmented regions. |  |
|  |  |  |
| [Pad](PythonicAPI/ImageProcessing/Pad.md) | Convolution in frequency space treats the image as a periodic function. A large kernel can pick up features from both sides of the image. The left image has been padded with a constant to eliminate wraparound during convolution. On the right, mirror padding has been used to remove artificial edges introduced by borders. |  |
|  |  |  |
| [RGBToHSI](PythonicAPI/Images/RGBToHSI.md) | Convert RGB to HSI. |  |
|  |  |  |
| [RGBToHSV](PythonicAPI/Images/RGBToHSV.md) | Convert RGB to HSV. |  |
|  |  |  |
| [RGBToYIQ](PythonicAPI/Images/RGBToYIQ.md) | Convert RGB to YIQ. |  |
|  |  |  |
| [ResizeImage](PythonicAPI/Images/ResizeImage.md) | Resize an image using a sinc interpolator. |  |
|  |  |  |
| [VTKSpectrum](PythonicAPI/ImageProcessing/VTKSpectrum.md) | The discrete Fourier transform changes an image from the spatial domain into the frequency domain, where each pixel represents a sinusoidal function. This figure shows an image and its power spectrum displayed using a logarithmic transfer function. |  |
|  |  |  |

## Widgets

| Example Name | Description | Image |
| --- | --- | --- |
| [AffineWidget](PythonicAPI/Widgets/AffineWidget.md) | Apply an affine transformation interactively. |  |
|  |  |  |
| [AngleWidget](PythonicAPI/Widgets/AngleWidget.md) |  |  |
|  |  |  |
| [AngleWidget2D](PythonicAPI/Widgets/AngleWidget2D.md) | [vtkAngleWidget](https://www.vtk.org/doc/nightly/html/classvtkAngleWidget.html) + [vtkAngleRepresentation2D](https://www.vtk.org/doc/nightly/html/classvtkAngleRepresentation2D.html). |  |
|  |  |  |
| [BalloonWidget](PythonicAPI/Widgets/BalloonWidget.md) | Uses a [vtkBalloonWidget](https://www.vtk.org/doc/nightly/html/classvtkBalloonWidget.html) to draw labels when the mouse stays above an actor. |  |
|  |  |  |
| [BiDimensionalWidget](PythonicAPI/Widgets/BiDimensionalWidget.md) | Used to measure a 2D (X, Y) size of some aspect of an object. |  |
|  |  |  |
| [BorderWidget](PythonicAPI/Widgets/BorderWidget.md) | 2D selection, 2D box. |  |
|  |  |  |
| [BoxWidget](PythonicAPI/Widgets/BoxWidget.md) | This 3D widget defines a region of interest that is represented by an arbitrarily oriented hexahedron with interior face angles of 90 degrees (orthogonal faces). The object creates 7 handles that can be moused on and manipulated. |  |
|  |  |  |
| [BoxWidget2](PythonicAPI/Widgets/BoxWidget2.md) | This 3D widget defines a region of interest that is represented by an arbitrarily oriented hexahedron with interior face angles of 90 degrees (orthogonal faces). The object creates 7 handles that can be moused on and manipulated. vtkBoxWidget2 and vtkBoxRepresentation are used in this example. |  |
|  |  |  |
| [CameraOrientationWidget](PythonicAPI/Widgets/CameraOrientationWidget.md) | Demonstrate the usage and versatility of the [vtkCameraOrientationWidget](https://www.vtk.org/doc/nightly/html/classvtkCameraOrientationWidget.html). |  |
|  |  |  |
| [CaptionWidget](PythonicAPI/Widgets/CaptionWidget.md) |  |  |
|  |  |  |
| [CheckerboardWidget](PythonicAPI/Widgets/CheckerboardWidget.md) | Compare two images using a checkerboard. |  |
|  |  |  |
| [CompassWidget](PythonicAPI/Widgets/CompassWidget.md) | Draws an interactive compass. |  |
|  |  |  |
| [ContourWidget](PythonicAPI/Widgets/ContourWidget.md) | Draw a contour (line) which can be deformed by the user. |  |
|  |  |  |
| [DistanceWidget](PythonicAPI/Widgets/DistanceWidget.md) |  |  |
|  |  |  |
| [HoverWidget](PythonicAPI/Widgets/HoverWidget.md) | How to detect a hover. |  |
|  |  |  |
| [ImagePlaneWidget](PythonicAPI/Widgets/ImagePlaneWidget.md) |  |  |
|  |  |  |
| [ImageTracerWidgetInsideContour](PythonicAPI/Widgets/ImageTracerWidgetInsideContour.md) | Highlight pixels inside a non-regular region scribbled on an image. |  |
|  |  |  |
| [ImageTracerWidgetNonPlanar](PythonicAPI/Widgets/ImageTracerWidgetNonPlanar.md) | Draw on a non-planar surface. |  |
|  |  |  |
| [ImplicitAnnulusWidget](PythonicAPI/Widgets/ImplicitAnnulusWidget.md) | Clip polydata with an implicit annulus. |  |
|  |  |  |
| [ImplicitConeWidget](PythonicAPI/Widgets/ImplicitConeWidget.md) | An interactive implicit cone widget. |  |
|  |  |  |
| [ImplicitPlaneWidget2](PythonicAPI/Widgets/ImplicitPlaneWidget2.md) | Clip polydata with an implicit plane. |  |
|  |  |  |
| [LineWidget2](PythonicAPI/Widgets/LineWidget2.md) |  |  |
|  |  |  |
| [LogoWidget](PythonicAPI/Widgets/LogoWidget.md) | Logo widget. |  |
|  |  |  |
| [PlaneWidget](PythonicAPI/Widgets/PlaneWidget.md) | Interact with a plane. |  |
|  |  |  |
| [PolygonalSurfacePointPlacer](PythonicAPI/PolyData/PolygonalSurfacePointPlacer.md) | Used in conjunction with [vtkContourWidget](https://www.vtk.org/doc/nightly/html/classvtkContourWidget.html) to draw curves on a surface. |  |
|  |  |  |
| [RadioButton](PythonicAPI/Widgets/RadioButton.md) | Display a sphere and three radio buttons controlling the appearance of the sphere. |  |
|  |  |  |
| [RectilinearWipeWidget](PythonicAPI/Widgets/RectilinearWipeWidget.md) | Compare two images. |  |
|  |  |  |
| [Slider2D](PythonicAPI/Widgets/Slider2D.md) | 2D Slider. |  |
|  |  |  |
| [Slider3D](PythonicAPI/Widgets/Slider3D.md) | 3D Slider. |  |
|  |  |  |
| [SphereWidget](PythonicAPI/Widgets/SphereWidget.md) | This 3D widget defines a sphere that can be interactively placed in a scene. |  |
|  |  |  |
| [SplineWidget](PythonicAPI/Widgets/SplineWidget.md) | This example shows how to use [vtkSplineWidget](https://www.vtk.org/doc/nightly/html/classvtkSplineWidget.html) with a callback being used to get the length of the spline widget. |  |
|  |  |  |

## Plotting

| Example Name | Description | Image |
| --- | --- | --- |
| [AreaPlot](PythonicAPI/Plotting/AreaPlot.md) | Plot the area between two curves. |  |
|  |  |  |
| [BoxChart](PythonicAPI/Plotting/BoxChart.md) | Box plot. |  |
|  |  |  |
| [ChartMatrix](PythonicAPI/Plotting/ChartMatrix.md) | Create a marix of plots. |  |
|  |  |  |
| [FunctionalBagPlot](PythonicAPI/Plotting/FunctionalBagPlot.md) | Functional Bag Plot. |  |
|  |  |  |
| [Histogram2D](PythonicAPI/Plotting/Histogram2D.md) | 2D Histogram of a [vtkImageData](https://www.vtk.org/doc/nightly/html/classvtkImageData.html). |  |
|  |  |  |
| [HistogramBarChart](PythonicAPI/Plotting/HistogramBarChart.md) | Histogram using bar chart. |  |
|  |  |  |
| [LinePlot2D](PythonicAPI/Plotting/LinePlot2D.md) | Line plot of 2D data. |  |
|  |  |  |
| [LinePlot3D](PythonicAPI/Plotting/LinePlot3D.md) | Line plot of 3D data. |  |
|  |  |  |
| [MultiplePlots](PythonicAPI/Plotting/MultiplePlots.md) | Display multiple plots by using viewports in a single render window. |  |
|  |  |  |
| [ParallelCoordinates](PythonicAPI/Plotting/ParallelCoordinates.md) | Parallel coordinates. |  |
|  |  |  |
| [PieChart](PythonicAPI/Plotting/PieChart.md) | Pie chart. |  |
|  |  |  |
| [PieChartActor](PythonicAPI/Plotting/PieChartActor.md) | Pie chart. |  |
|  |  |  |
| [ScatterPlot](PythonicAPI/Plotting/ScatterPlot.md) | Scatter plot. |  |
|  |  |  |
| [SpiderPlot](PythonicAPI/Plotting/SpiderPlot.md) | Spider plot. |  |
|  |  |  |
| [StackedBar](PythonicAPI/Plotting/StackedBar.md) | Stacked bar. |  |
|  |  |  |
| [SurfacePlot](PythonicAPI/Plotting/SurfacePlot.md) | Surface plot. |  |
|  |  |  |

## Animation

| Example Name | Description | Image |
| --- | --- | --- |
| [AnimateActors](PythonicAPI/Animation/AnimateActors.md) | Animate actors. |  |
|  |  |  |
| [AnimateSphere](PythonicAPI/Animation/AnimateSphere.md) | Animate a sphere by opening it to an angle of 90°. |  |
|  |  |  |
| [Animation](PythonicAPI/Utilities/Animation.md) | Move a sphere across a scene. |  |
|  |  |  |
| [AnimationScene](PythonicAPI/Animation/AnimationScene.md) | Animation (the right way). Zoom in on a sphere. |  |
|  |  |  |

## Annotation

| Example Name | Description | Image |
| --- | --- | --- |
| [LegendScaleActor](PythonicAPI/Annotation/LegendScaleActor.md) | Display the scale of a scene. |  |
|  |  |  |
| [PolarAxesActor](PythonicAPI/Annotation/PolarAxesActor.md) | Draw polar axes in a specified plane for a given pole. |  |
|  |  |  |
| [TextOrigin](PythonicAPI/Annotation/TextOrigin.md) | This example demonstrates the use of [vtkVectorText](https://www.vtk.org/doc/nightly/html/classvtkVectorText.html) and [vtkFollower](https://www.vtk.org/doc/nightly/html/classvtkFollower.html). [vtkVectorText](https://www.vtk.org/doc/nightly/html/classvtkVectorText.html) is used to create 3D annotation. |  |
|  |  |  |

## InfoVis

| Example Name | Description | Image |
| --- | --- | --- |
| [ParallelCoordinatesView](PythonicAPI/InfoVis/ParallelCoordinatesView.md) | How to use Parallel Coordinates View to plot and compare data set attributes. |  |
|  |  |  |

## PyQt
