<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_med_presentation_py.html -->

# `medpresentation` Python API

```python
def MakePlot3D(proxy,
              viewMode=MEDCALC.VIEW_MODE_DEFAULT,
              scalarBarRange=MEDCALC.SCALAR_BAR_RANGE_DEFAULT,
              colorMap=MEDCALC.COLOR_MAP_DEFAULT
              ):
  # Create the presentation instance in CORBA engine
  # The engine in turn creates the ParaView pipeline elements
  visibility = DEFAULT_VISIBILITY
  scalarBarVisibility = DEFAULT_SCALAR_BAR_VISIBILITY
  scalarBarRangeArray = DEFAULT_SCALAR_BAR_RANGE
  hideDataOutsideCustomRange = DEFAULT_HIDE_DATA_OUTSIDE_CUSTOM_RANGE
  scalarBarRangeArray = DEFAULT_SCALAR_BAR_RANGE
  planeNormal = DEFAULT_PLANE_NORMAL
  planePos = DEFAULT_PLANE_POS
  params = MEDCALC.Plot3DParameters(proxy.id, scalarBarRange, colorMap, visibility,
                                    scalarBarVisibility, scalarBarRangeArray, hideDataOutsideCustomRange, planeNormal, planePos)
  try:
    presentation_id = __manager.makePlot3D(params, viewMode)
    notifyGui_addPresentation(proxy.id, presentation_id)
    return presentation_id
  except SALOME.SALOME_Exception as e:
    notifyGui_error("An error occurred while creating the Plot3D:\n" + e.details.text)
    raise Exception(e.details.text)
```

```python
GetPlot3DParameters = lambda pres_id: __GetGENERICParameters("Plot3D", pres_id)
```

Method `__GetGENERICParameters` is an internal helper method that calls `getPlot3DParameters` function of `MEDPresentationManager` CORBA service.

```python
UpdatePlot3D = lambda pres_id, params: __UpdateGENERIC("Plot3D", pres_id, params)
```

Method `__GetGENERICParameters` is an internal helper method that calls `updatePlot3D` function of `MEDPresentationManager` CORBA service.
