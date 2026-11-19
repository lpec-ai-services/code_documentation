<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/fields_introduction.html -->

# Introduction to Fields module

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/image_fields.png)

Fields module is used for analysis and post-processing of numerical simulation results. It is based upon ParaVis module, MEDReader ParaVis
module plugin and MEDCoupling library. Main advantage of this module is that it provides a simplified (in comparison with ParaVis module)
way to create different presentations. After applying this simplified visualization it is possible to switch to ParaVis module and
complete a more complex presentation if necessary.

Fields module uses Python API of the ParaVis module to build presentations.
Any presentation in the Fields module is a pipeline of the ParaVis filters, which always starts with MEDReader.
For example, [Plot3D presentation](fields_plot3d_presentation.md#fields-plot3d-presentation-page) is a sequence of the following ParaVis filters: **MEDReader > Calculator > WarpByScalar**.
