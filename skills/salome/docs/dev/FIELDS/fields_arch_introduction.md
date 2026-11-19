<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_arch_introduction.html -->

# Introduction to FIELDS module architecture

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_fields_arch.png)

Generally FIELDS module architecture is presented on the scheme above.
FIELDS module is used for analysis and post-processing of numerical simulation results. It is based upon ParaVis module, MEDReader ParaVis module plugin and MEDCoupling library.
FIELDS module uses Python API of the ParaVis module to build presentations. Any presentation in the FIELDS module is a pipeline of the ParaVis filters, which always starts with MEDReader.
ParaVis module API is used via medcalc Python module and CORBA services.

In the FIELDS module architecture, the following parts can be distinguished:

- [FIELDS module GUI](fields_arch_gui.md)
- [FIELDS medcalc python package](fields_arch_medcalc_py.md)
- [FIELDS module CORBA services](fields_arch_corba_services.md)
- [FIELDS module implementation layer](fields_arch_implementation_layer.md)

See also:

- [Implementation example: Plot3D presentation](fields_arch_plot3d_implementation_example.md)
  - [General description of Plot3D presentation](fields_arch_plot3d_implementation_example.md#general-description-of-plot3d-presentation)
  - [GUI controls](fields_arch_plot3d_implementation_example.md#gui-controls)
  - [Extend `MEDCALC::MEDPresentationManager`](fields_arch_plot3d_implementation_example.md#extend-medcalc-medpresentationmanager)
  - [Extend `medcalc` API](fields_arch_plot3d_implementation_example.md#extend-medcalc-api)
  - [Implement pipeline](fields_arch_plot3d_implementation_example.md#implement-pipeline)
