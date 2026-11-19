<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_replace_hexa.html -->

# Replace hexahedron

To **Replace an hexahedron** in the **Main Menu** select **Model -> Operation -> Replace Hexahedron**.

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_replacehexa.png)

**Replace Hexahedron Dialog Box**

The following data are required:

- Quad(s) source
  :   - Quad’s source: the set of quads to be extruded (select quads).
      - s1, s2, s3: vertices from the set of quads. (select vertices).
- Quad destination
  :   - d1, d2, d3: vertices which define the target quad.
        As a result of the operation, each one are replaced: s1->d1, s2->d2, s3->d3 (select vertices).

Here is an example where the source quadrangles and vertices are highlighted:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/before_replacehexa.png)

**Source selection**

The result is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/replacehexa.png)

**Hexa replaced**

TUI command: [Replace Hexahedron](tui_replace_hexa.md#tuireplacehexa)
