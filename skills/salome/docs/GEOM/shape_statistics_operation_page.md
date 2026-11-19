<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/shape_statistics_operation_page.html -->

# Shape Statistics

This operation allows plotting a distribution histogram for the numerical parameters and creating the corresponding geometrical groups of the given shape.

To call **Shape Statistics** dialog box, in the **Main Menu** select **Inspection - > Shape Statistics**.

![shape_statistics.png](https://docs.salome-platform.org/latest/gui/GEOM/shape_statistics.png)

In this dialog:

- "Selected objects" standard selection box allows selecting one or more geometrical objects.
- "Type" combo-box with the following items: "Edges length", "Faces area", "Solids volume".

  Note
  :   "Type" combo-box includes only parameters applied to the currently selected shape (e.g. "Solids volume" will not be available for a selected face or shell); multiple selection is processed correspondingly (i.e. only types applicable for all selected shapes will be available).
- "Number of intervals" spin box is used to specify number of distribution histogram ranges.
- "Scalar range" checkable group box, when switched ON, allows specifying custom values range used for plotting and creating groups.

  Note
  :   By default, "Scalar range" controls are empty; pressing "Compute" button allows automatically computing the initial range of the chosen parameter. This is necessary as the computation of the parameters range can be time-consuming for large or complex models. In case of multiple selection, the scalar range is computed for all selected shapes.
- "Plot" button opens or uses an opened Plot2d viewer and plots the distribution histogram for the selected shape(s).
- "Create groups" button allows creating groups according to the currently specified parameters. The group names will include numerical values of the range, e.g. "Edges_length_0-20", "Edges_length_20-40", etc. Empty groups are not created.
- Close dialog box, by pressing **Close** button.

Note
:   This functionality is available only if GUI module is built with Plot 2D Viewer (option SALOME_USE_PLOT2DVIEWER is ON when building GUI module).
