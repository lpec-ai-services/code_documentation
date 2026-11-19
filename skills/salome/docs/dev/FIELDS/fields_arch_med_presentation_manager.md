<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_med_presentation_manager.html -->

# MEDCALC::MEDPresentationManager

## Plot3D presentation parameters

```cpp
  struct Plot3DParameters {
    long fieldHandlerId;
    ScalarBarRangeType scalarBarRange;
    ColorMapType colorMap;
    boolean visibility;
    boolean scalarBarVisibility;
    DoubleArray scalarBarRangeArray;
    boolean hideDataOutsideCustomRange; 
    DoubleArray planeNormal;
    double planePos;
  };
```

## Methods to create and update Plot3D presentation

```cpp
interface MEDPresentationManager : SALOME::GenericObj
{
  ...
  long                 makePlot3D(in Plot3DParameters params, in ViewModeType viewMode)  raises (SALOME::SALOME_Exception);
  Plot3DParameters     getPlot3DParameters(in long presId);
  void                 updatePlot3D (in long presId, in Plot3DParameters params)         raises (SALOME::SALOME_Exception);
  ...
}
```

- Method `makePlot3D` takes as parameters:

  1. `Plot3DParameters` structure.
  2. `ViewModeType` enumerator which can have the following values:
  > - **VIEW_MODE_OVERLAP**: a newly created presentation is published in the *Object browser* and displayed in the active 3D Viewer.
  >   All previously created presentations are deleted.
  > - **VIEW_MODE_REPLACE**: a newly created presentation is added into *Object browser* and displayed in the active 3D Viewer.
  >   All previously created presentations are kept as is.
  > - **VIEW_MODE_NEW_LAYOUT**: a newly created presentation is added into *Object browser*. New 3D Viewer (layout) is created and
  >   presentation is displayed in this new 3D Viewer. All previously created presentations are kept as is.
  > - **VIEW_MODE_SPLIT_VIEW**: a newly created presentation is added into *Object browser*. An active 3D Viewer (layout) is split,
  >   and a new 3D Viewer is added to the layout. Newly created presentation is displayed in this new 3D Viewer;
  >   all previously created presentations are kept as is.
  >
  > This method returns ID of a newly created presentation.
- Method `getPlot3DParameters` takes single parameter which is an ID of presentation; it returns `Plot3DParameters` structure.
- Method `updatePlot3D` takes as parameters a presentation ID and `Plot3DParameters` structure.
