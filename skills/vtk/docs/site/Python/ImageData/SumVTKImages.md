<!-- source: https://examples.vtk.org/site/Python/ImageData/SumVTKImages/ -->

# SumVTKImages

Repository source: [SumVTKImages](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/Python/ImageData/SumVTKImages.py)

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**SumVTKImages.py**

```python
#!/usr/bin/env python

from vtkmodules.vtkImagingMath import vtkImageWeightedSum

# ImageSets = List of Image sets
# Weights  = List of weights e.g [1, 1, 1]

def SumVTKImages(ImageSets, Weights):
    NumOfImages = len(ImageSets)
    SumFilter = vtkImageWeightedSum()
    for x in range(0, NumOfImages, 1):
        SumFilter.AddInputConnection(ImageSets[x])
        SumFilter.SetWeight(x, Weights[x])
    SumFilter.Update()

    # Return summed Image as vtkImageData
    return SumFilter.GetOutput()
```
