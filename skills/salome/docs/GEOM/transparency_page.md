<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/transparency_page.html -->

# Transparency

You can change the transparency of a shape in the range between 0% (absolutely opaque) and 100% (absolutely transparent and thus invisible) in the following dialog box.

![neo-transparency.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-transparency.png)

or using a **TUI Command:** *gg.setTransparency(ID, Value)*

where

- *ID* is an object ID (entry)
- *Value* is a transparency value in range [0-1]; 0 means fully opaque, 1 means fully transparent

**Examples:**

![colorsn.png](https://docs.salome-platform.org/latest/gui/GEOM/colorsn.png)

*Opaque*

![transparencysn.png](https://docs.salome-platform.org/latest/gui/GEOM/transparencysn.png)

*50% Transparent*

Our **TUI Scripts** provide you with useful examples of [Changing Display Parameters](tui_viewing_geom_objs_page.md#tui_change_transparency).
