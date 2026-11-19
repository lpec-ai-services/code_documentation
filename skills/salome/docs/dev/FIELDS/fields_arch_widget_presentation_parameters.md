<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_widget_presentation_parameters.html -->

# Plot3D presentation’s parameters panel implementation

## Functions to access the cutting plane normal

```cpp
void
WidgetPresentationParameters::setNormal(const double normX, const double normY, const double normZ)
{
  _blockSig = true;
  _ui.labelCutPlaneNormal->show();
  _ui.spinNormalX->show();
  _ui.spinNormalY->show();
  _ui.spinNormalZ->show();
  _ui.spinNormalX->setValue(normX);
  _ui.spinNormalY->setValue(normY);
  _ui.spinNormalZ->setValue(normZ);
  _blockSig = false;
}
```

```cpp
void WidgetPresentationParameters::getNormal(double* arr) const
{
  arr[0] = _ui.spinNormalX->value();
  arr[1] = _ui.spinNormalY->value();
  arr[2] = _ui.spinNormalZ->value();
}
```

## Functions to access the cutting plane position

```cpp
void
WidgetPresentationParameters::setNormal(const double normX, const double normY, const double normZ)
{
  _blockSig = true;
  _ui.labelCutPlaneNormal->show();
  _ui.spinNormalX->show();
  _ui.spinNormalY->show();
  _ui.spinNormalZ->show();
  _ui.spinNormalX->setValue(normX);
  _ui.spinNormalY->setValue(normY);
  _ui.spinNormalZ->setValue(normZ);
  _blockSig = false;
}
```

```cpp
void WidgetPresentationParameters::getNormal(double* arr) const
{
  arr[0] = _ui.spinNormalX->value();
  arr[1] = _ui.spinNormalY->value();
  arr[2] = _ui.spinNormalZ->value();
}
```

## Signal-slot connections

```cpp
  QObject::connect(_ui.spinNormalX,            SIGNAL(editingFinished()),
                     this,                     SLOT(onSpinNormalEditingFinished()) );
  QObject::connect(_ui.spinNormalY,            SIGNAL(editingFinished()),
                     this,                     SLOT(onSpinNormalEditingFinished()) );
  QObject::connect(_ui.spinNormalZ,            SIGNAL(editingFinished()),
                     this,                     SLOT(onSpinNormalEditingFinished()) );
  QObject::connect(_ui.spinPlanePos,           SIGNAL(editingFinished()),
                     this,                     SLOT(onSpinPlanePosEditingFinished()) );
```
