<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/addons_Features/TUI_xmlFile_rectangleFeature.html -->

# File widget.xml

```html
<source>
  <workbench id="Sketch">
    <group id="Linear geometry">

      <!-- SketchRectangle (python feature) -->
      <feature
        id="SketchRectangle"
        title="Rectangle"
        tooltip="Create rectangle"
        icon="icons/Addons/rectangle.png"
        helpfile="rectangleFeature.html">
        <sketch-2dpoint_selector id="RectStartPoint" accept_expressions="0" title="Start point" tooltip="Start point coordinates"
                                 enable_value="enable_by_preferences"/>
        <sketch-2dpoint_selector id="RectEndPoint" accept_expressions="0" title="End point" tooltip="End point coordinates"
                                 enable_value="enable_by_preferences"/>
        <boolvalue id="Auxiliary" label="Auxiliary" default="false" tooltip="Construction element" obligatory="0"/>
        <validator id="GeomValidators_Different" parameters="RectStartPoint,RectEndPoint"/>
      </feature>

    </group>
  </workbench>
</source>
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/53573b50c85b25ca6e6797e329417916/widget.xml)
