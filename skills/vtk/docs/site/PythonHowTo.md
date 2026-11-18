<!-- source: https://examples.vtk.org/site/PythonHowTo/ -->

# Python How To

Often you just need a "pointer" to an example that shows you how to do something.

Here are some snippets and examples that highlight interesting features that may help you:

## Callback

| Example Name | Comments | Image |
| --- | --- | --- |
| [CallBack](Python/Interaction/CallBack.md) | Setting up a callback with client data. Two different methods are demonstrated. |  |
|  |  |  |

## Camera

| Example Name | Comments | Image |
| --- | --- | --- |
| [CameraModel1](Python/Visualization/CameraModel1.md) | Illustrate camera movement around the focal point. |  |
|  |  |  |
| [CameraModel2](Python/Visualization/CameraModel2.md) | camera movement centered at the camera position. |  |
|  |  |  |
| [CameraOrientationWidget](Python/Widgets/CameraOrientationWidget.md) | This 3D camera orientation widget can be used in conjunction with [CameraPosition](Python/Snippets/CameraPosition.md) to get a nice camera position. |  |
|  |  |  |
| [CameraPosition](Python/Snippets/CameraPosition.md) | Get the camera position while moving the image. |  |
| [ResetCameraOrientation](Python/Utilities/ResetCameraOrientation.md) | Reset camera orientation to a previously saved orientation. |  |
|  |  |  |
| [ShareCamera](Python/Utilities/ShareCamera.md) | Use the same camera for all renderers. |  |
|  |  |  |

## Check the VTK Version

| Example Name | Comments | Image |
| --- | --- | --- |
| [CheckVTKVersion-Snippet](Python/Snippets/CheckVTKVersion.md) | Check the VTK version returning `True` if the requested VTK version is >= the current version. |  |
| [CheckVTKVersion-Example](Python/Utilities/CheckVTKVersion.md) | Check the VTK version and provide alternatives for different VTK versions. |  |

## Coloring

| Example Name | Comments | Image |
| --- | --- | --- |
| [ShareCamera](Python/Utilities/ShareCamera.md) | Store background colors in a vector for later extraction of the red, green and blue components. |  |
|  |  |  |

## Glyphing

| Example Name | Comments | Image |
| --- | --- | --- |
| [InteractorStyleTrackballCamera](Python/Interaction/InteractorStyleTrackballCamera.md) | Here points are represented as glyphs. |  |
|  |  |  |
| [PointToGlyph](Python/Snippets/PointToGlyph.md) | How to represent points as glyphs. |  |

## Image

| Example Name | Comments | Image |
| --- | --- | --- |
| [WriteImage](Python/Snippets/WriteImage.md) | Write out an image of various types. |  |

## Multiple view ports and render windows

| Example Name | Comments | Image |
| --- | --- | --- |
| [MultipleRenderWindows](Python/Visualization/MultipleRenderWindows.md) | Multiple Render Windows. |  |
|  |  |  |
| [MultipleViewports](Python/Visualization/MultipleViewports.md) | Multiple Viewports. |  |
|  |  |  |

## Physically Based Rendering

Physically based rendering sets metallicity, roughness, occlusion strength and normal scaling of the object. Textures are used to set base color, ORM, anisotropy and normals. Textures for the image based lighting and the skymap are supplied from a cubemap.

Image based lighting uses a cubemap texture to specify the environment. A Skybox is used to create the illusion of distant three-dimensional surroundings.

The results can be quite spectacular, it is hoped that these examples will help you to get started.

| Example Name | Comments | Image |
| --- | --- | --- |
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

## Polydata

| Example Name | Comments | Image |
| --- | --- | --- |
| [ReadPolyData](Python/Snippets/ReadPolyData.md) | This snippet works for most PolyData. |  |

## Random

If you want to ensure that the same random points/colors are used in C++ and other languages then it is best to use [vtkMinimalStandardRandomSequence](https://www.vtk.org/doc/nightly/html/classvtkMinimalStandardRandomSequence.html).

| Example Name | Comments | Image |
| --- | --- | --- |
| [HighlightWithSilhouette](Python/Picking/HighlightWithSilhouette.md) | Here we use randomly positioned spheres with random colors. A [vtkLookupTable](https://www.vtk.org/doc/nightly/html/classvtkLookupTable.html) is filled with random colors. |  |
|  |  |  |

## Render Windows

| Example Name | Comments | Image |
| --- | --- | --- |
| [Model](Python/Rendering/Model.md) | Multiple render windows. |  |
|  |  |  |

## Searching for relevant examples?

| Example Name | Comments | Image |
| --- | --- | --- |
| [SelectExamples](Python/Utilities/SelectExamples.md) | Given a VTK Class and a language, select the matching examples. |  |

## StructuredDataset

How to visualise the information in a structured dataset. All these examples use the combustor dataset.

| Example Name | Comments | Image |
| --- | --- | --- |
| [CombustorIsosurface](Python/VisualizationAlgorithms/CombustorIsosurface.md) | Generate an isosurface of constant flow density. |  |
|  |  |  |
| [CutStructuredGrid](Python/VisualizationAlgorithms/CutStructuredGrid.md) | Cut through structured grid with plane. The cut plane is shown solid shaded. A computational plane of constant k value is shown in wireframe for comparison. The colors correspond to flow density. Cutting surfaces are not necessarily planes: implicit functions such as spheres, cylinders, and quadrics can also be used. |  |
|  |  |  |
| [ProbeCombustor](Python/VisualizationAlgorithms/ProbeCombustor.md) | Probing data in a combustor. Probes are regular arrays of 50 by 50 points that are then passed through a contouring filter. |  |
|  |  |  |
| [PseudoVolumeRendering](Python/VolumeRendering/PseudoVolumeRendering.md) | Here we use 100 cut planes, each with an opacity of 0.05. They are then rendered back-to-front to simulate volume rendering. |  |
|  |  |  |
| [Rainbow](Python/Rendering/Rainbow.md) | Using different vtkLookupTables. |  |
|  |  |  |
| [StreamLines](Python/Visualization/StreamLines.md) | Seed streamlines with vectors from a structured grid. |  |
|  |  |  |
| [StreamlinesWithLineWidget](Python/VisualizationAlgorithms/StreamlinesWithLineWidget.md) | Interact with the streamlines in the combustor dataset. |  |
|  |  |  |
| [VelocityProfile](Python/VisualizationAlgorithms/VelocityProfile.md) | Warping the geometry of three planes to show flow momentum. |  |
|  |  |  |
| [WarpCombustor](Python/VisualizationAlgorithms/WarpCombustor.md) | Carpet plots of combustor flow energy in a structured grid. Colors and plane displacement represent energy values. |  |
|  |  |  |

## Transforms

| Example Name | Comments | Image |
| --- | --- | --- |
| [Frog](https://examples.vtk.org/site/Python/Visualization/Frog/) | This code uses a general way of specifying transformations that can permute image and other geometric data in order to maintain proper orientation regardless of the acquisition order. See the class `SliceOrder`. |  |
|  |  |  |
