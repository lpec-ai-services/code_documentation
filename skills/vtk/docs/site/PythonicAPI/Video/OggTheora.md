<!-- source: https://examples.vtk.org/site/PythonicAPI/Video/OggTheora/ -->

# OggTheora

Repository source: [OggTheora](https://gitlab.kitware.com/vtk/vtk-examples/-/blob/master/src/PythonicAPI/Video/OggTheora.py)

Other languages

See ([Cxx](https://examples.vtk.org/site/Cxx/Video/OggTheora/)), ([Java](https://examples.vtk.org/site/Java/Video/OggTheora/))

Question

If you have a question about this example, please use the [VTK Discourse Forum](https://discourse.vtk.org/)

### Code

**OggTheora.py**

```python
#!/usr/bin/env python3

from vtkmodules.vtkCommonCore import VTK_UNSIGNED_CHAR
from vtkmodules.vtkIOOggTheora import vtkOggTheoraWriter
from vtkmodules.vtkImagingSources import vtkImageCanvasSource2D

def main():
    source = vtkImageCanvasSource2D(scalar_type=VTK_UNSIGNED_CHAR, number_of_scalar_components=3,
                                    extent=(0, 100, 0, 100, 0, 0))

    writer = vtkOggTheoraWriter(file_name='test.avi')
    source >> writer
    writer.Start()

    for i in range(0, 100):
        source.draw_color = (0, 0, 0, 1)  # black
        source.FillBox(0, 100, 0, 100)  # clear image
        source.draw_color = (255, 0, 0, 1)  # red
        source.FillBox(i, 20, 10, 20)
        source.update()

        writer.Write()
    writer.End()

if __name__ == '__main__':
    main()
```
