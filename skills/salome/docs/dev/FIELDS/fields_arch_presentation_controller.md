<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_presentation_controller.html -->

# PresentationController

## Create Plot3D menu and toolbar items

```cpp
  label   = tr("LAB_PRESENTATION_PLOT3D");
  tooltip = tr("TIP_PRESENTATION_PLOT3D");
  icon    = tr(_getIconName("ICO_PRESENTATION_PLOT3D").c_str());
  actionId = _salomeModule->createStandardAction(label, this, SLOT(onVisualizePlot3D()),
                                                 icon, tooltip, FIELDSOp::OpPlot3D);
  _salomeModule->createTool(actionId, presentationToolbarId);
  _salomeModule->action(actionId)->setIconVisibleInMenu(true);
  _salomeModule->createMenu(actionId, presentationMenuId);
```

```cpp
void
PresentationController::onVisualizePlot3D()
{
  this->visualize(PresentationEvent::EVENT_VIEW_OBJECT_PLOT3D);
}
```

## Translate GUI events into `medcalc` Python API

```cpp
  else if ( event->eventtype == PresentationEvent::EVENT_VIEW_OBJECT_PLOT3D ) {
      commands += QString("presentation_id = medcalc.MakePlot3D(accessField(%1), viewMode=%2, scalarBarRange=%3, colorMap=%4)")
              .arg(fieldHandler->id).arg(viewMode).arg(scalarBarRange).arg(colorMap);
      commands += QString("presentation_id");
  }
```

```cpp
  else if ( event->eventtype == PresentationEvent::EVENT_CHANGE_PLANE_POS ) {
      std::string typ = getPresTypeFromWidgetHelper(event->presentationId);
      commands += QString("params = medcalc.GetPlot3DParameters(%2)").arg(event->presentationId);
      commands += QString("params.planePos = %1").arg(event->aDouble3);
      commands += QString("medcalc.UpdatePlot3D(%1, params)").arg(event->presentationId);
  }
  else if ( event->eventtype == PresentationEvent::EVENT_CHANGE_NORMAL ) {
      std::string typ = getPresTypeFromWidgetHelper(event->presentationId);
      commands += QString("params = medcalc.GetPlot3DParameters(%2)").arg(event->presentationId);
      commands += QString("params.planeNormal = [%1, %2, %3]").arg(event->aDoubleN[0]).arg(event->aDoubleN[1]).arg(event->aDoubleN[2]);
      commands += QString("medcalc.UpdatePlot3D(%1, params)").arg(event->presentationId);
  }
```
