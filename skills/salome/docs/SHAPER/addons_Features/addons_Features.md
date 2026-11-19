<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/addons_Features/addons_Features.html -->

# Python addons

It is possible to create custom features.

The corresponding folder should be created for each feature at *../sources/src/PythonAddons/macros*.

A feature description includes 4 files:

- widget.xml with a description of the property panel,
- __init__.py,
- feature.py with python commands,
- icon.png with image of button in the toolbar (the file is located at sub-folder /icons).

Some examples of already created custom features are:

- [Compound Vertices](compoundVerticesFeature.md)
- [Import Parameters](importParametersFeature.md)
- [Fibre neutre](midSurfaceFeature.md)
- [Rectangle](rectangleFeature.md)
- [Réseau de tuyaux](pipeNetworkFeature.md)
