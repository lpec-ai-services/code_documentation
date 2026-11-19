<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_med_presentation_manager_impl.html -->

# MEDCALC::MEDPresentationManager implementation

```cpp
MEDPresentation::TypeID
MEDPresentationManager_i::makePlot3D(const MEDCALC::Plot3DParameters& params, const MEDCALC::ViewModeType viewMode)
{
  return _makePresentation<MEDPresentationPlot3D>(params, viewMode);
}
```

Method `_makePresentation` is a private template method of `MEDPresentationManager_i` class; it calls the constructor of particular presentation class, in this case `MEDPresentationPlot3D::MEDPresentationPlot3D`.

```cpp
MEDCALC::Plot3DParameters*
MEDPresentationManager_i::getPlot3DParameters(MEDPresentation::TypeID presentationID)
{
  MEDCALC::Plot3DParameters* p = new MEDCALC::Plot3DParameters();
  _getParameters<MEDPresentationPlot3D>(presentationID, *p);
  MEDCALC::Plot3DParameters_var tmp(p);
  return tmp._retn();
}
```

Method `_getParameters` is a private template method of `MEDPresentationManager_i` class; it calls `getParameters` method of particular presentation instance, in this case `MEDPresentationPlot3D::getParameters`.

```cpp
void
MEDPresentationManager_i::updatePlot3D(MEDPresentation::TypeID presentationID, const MEDCALC::Plot3DParameters& params)
{
  return _updatePresentation<MEDPresentationPlot3D>(presentationID, params);
}
```

Method `_updatePresentation` is a private template method of `MEDPresentationManager_i` class, it calls `updatePipeline` of particular presentation instance, in this case `MEDPresentationPlot3D::updatePipeline`.
