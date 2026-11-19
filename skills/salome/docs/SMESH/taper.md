<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/taper.html -->

# Taper

**Taper** mesh quality criterion represents the ratio of the areas
of two triangles separated by a diagonal within a quadrilateral face.

```python
**JA = 0.25 * (A1 + A2 + A3 + A4)**
**TAPER = MAX(|A1/JA - 1|, |A2/JA - 1|, |A3/JA - 1|, |A4/JA - 1|)**
```

*To apply the Taper quality criterion to your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Face Controls > Taper** or click *“Taper”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image36.png) in the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image90.jpg)

**See Also** a sample TUI Script of a [Taper](tui_quality_controls.md#tui-taper) filter.
