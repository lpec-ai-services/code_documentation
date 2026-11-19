<!-- source: modules/javert/plot_repr.rst -->

# `plot_repr` – Transform test results into `PlotTemplate`

Module containing all available methods to convert a test result in a table to be converted in rst.

### `valjean.javert.plot_repr.dimensions_from_array(array_shape)`

Check if array is consistent with 1D plot.

Checks are done on presence of non-trivial and trivial dimensions, trivial being a dimension with size equal to one, non-trivial being for a dimension with at least two values.

param tuple(int) array_shape  
shape of the **values** array

returns  
indices of the non-trivial dimensions in the shape tuple

rtype  
tuple(int)

### `valjean.javert.plot_repr.dimensions_and_bins(bins, array_shape)`

Determine the dimensions of the result from the `collections.OrderedDict` of bins. It is expected to be the "only non-trivial" dimensions.

param bins  
bins coming from the results dataset

type bins  
collections.OrderedDict(str, numpy.ndarray)

param tuple(int) array_shape  
shape of the **values** array from the results dataset

returns  
dimensions and bins to be used (non-trivial ones), or None if all the dimensions are trivial

rtype  
collections.OrderedDict

### `valjean.javert.plot_repr.trim_range(bins, max_ratio=1000)`

Adapt bins range when extreme bins are very large.

This function suggests reasonable ranges for the given bin axes by trimming the extreme bins if they are too wide. For each axis, the extreme bins are trimmed if their width is at least `max_ratio` times larger than the width of the neighbouring bin (the first bin is compared to the second one, and the last bin is compared to the second-last one). If there is no need to change the previous limits a tuple with initial limits is returned for the considered dimension. A boolean is associated to the tuple to precise if the limits have be changed.

The trimmed ranges extend a bit over the clipped bins, so that their content is still visible in the plots.

param list(numpy.ndarray) bins  
bins of the `PlotTemplate`.

param float max_ratio  
the bin size ratio above which bins will be truncated.

returns  
new limits for all dimensions. The list has one item per dimension; the bool indicates whether the axis was actually trimmed.

rtype  
list(tuple(float, float, bool))

Examples:

\>\>\> bins = \[np.array(\[-1e4, 0, 2, 4, 1e4\]), ... np.array(\[-1e2, 0, 2, 4, 1e4\]), ... np.array(\[-1e2, 0, 2, 4, 1e2\])\] \>\>\> trim_range(bins) \[(-0.2, 4.2, True), (-100.0, 9.2, True), (-100.0, 100.0, False)\]

### `valjean.javert.plot_repr.fit_curve_ranges(curves, threshold=0.0)`

Return a set of best-fit limits for the given curves.

This function suggests axis limits for the given curves that make all curves fill the plot area. The limits are determined by looking at the region where any of the curves exceed the given threshold.

param list(CurveElements) curves  
list of curves

param float threshold  
threshold for the detection

returns  
suggested limits for all dimensions

rtype  
list((float, float))

Example:

\>\>\> bins = \[np.array(\[-1.0, 0.0, 1.0\]), ... np.array(\[0.0, 5.0, 10.0, 15.0\])\] \>\>\> curve1 = CurveElements(np.array(\[\[1.0, 2.0, 3.0\], ... \[2.0, 3.0, 4.0\]\]), ... bins=bins, legend='curve1') \>\>\> curve2 = CurveElements(np.array(\[\[1.0, 4.0, 3.0\], ... \[2.0, 3.0, 2.0\]\]), ... bins=bins, legend='curve2') \>\>\> fit_curve_ranges(\[curve1, curve2\], threshold = 3.5) \[(-1.0, 1.0), (5.0, 15.0)\]

### `valjean.javert.plot_repr.ranges_union(ranges, union_axis=0, minmax_axis=-1)`

Return the union of the given ranges, axis by axis.

param ranges  
an n-dimensional array of range bounds. The array shape can be anything, as long as one of the dimensions has length 2; this axis is assumed to contain the `(min_range, max_range)` pair.

type ranges  
list or numpy.ndarray

param union_axis  
the axis along which the union will be computed. If unspecified, the first axis will be assumed.

type union_axis  
anything that `NumPy` understands as an axis.

param minmax_axis  
the length-2 axis along which the range minimum and maximum are stored. If unspecified, the last axis will be assumed.

type minmax_axis  
int

returns  
an array of union bounds, with the same shape as the input array except for the suppression of `union_axis`.

rtype  
numpy.ndarray

Examples:

\>\>\> ranges_union(\[\[(-1, 1)\]\]) array(\[\[-1, 1\]\])

\>\>\> ranges_union(\[\[(-5, 5)\], \[(-3, 8)\]\]) array(\[\[-5, 8\]\])

\>\>\> ranges_union(\[\[(-5, 5), (-1, 1)\], ... \[(-3, 8), (-2, 2)\]\]) array(\[\[-5, 8\], \[-2, 2\]\])

\>\>\> ranges_union(\[\[(-5, 5), (-1, 1)\], ... \[(-3, 8), (-2, 2)\], ... \[(-7, 1), (0, 6)\]\]) array(\[\[-7, 8\], \[-2, 6\]\])

### `valjean.javert.plot_repr.curve_limits(curve, threshold=0.0)`

Return the set of bounds over each axis where the given curve exceeds the given threshold.

For example, the following curve exceeds the threshold value of 50 in the central bins, which corresponds to <span class="title-ref">2.0\<x\<4.0</span> and \`-0.5\<y\<0.5\`:

\>\>\> bins = \[np.linspace(0.0, 6.0, num=7), ... np.linspace(-2.5, 2.5, num=6)\] \>\>\> curve = CurveElements(np.array(\[\[ 1, 1, 1, 1, 1\], ... \[ 1, 10, 30, 10, 1\], ... \[ 1, 10, 100, 10, 1\], ... \[ 1, 10, 100, 10, 1\], ... \[ 1, 10, 30, 10, 1\], ... \[ 1, 1, 1, 1, 1\]\]), ... bins=bins, legend='curve') \>\>\> curve_limits(curve, threshold=50) \[(2.0, 4.0), (-0.5, 0.5)\]

Changing the threshold to 20 modifies the range for the first axis, but not for the second one.

\>\>\> curve_limits(curve, threshold=20) \[(1.0, 5.0), (-0.5, 0.5)\]

The function also works if the number of bin edges is equal to the number of values along a given direction (as opposed to the number of values plus one):

\>\>\> bins = \[np.array(\[-1.0, 1.0\]), np.array(\[0.0, 5.0, 10.0, 15.0\])\] \>\>\> curve = CurveElements(np.array(\[\[1.0, 2.0, 3.0\], ... \[2.0, 3.0, 4.0\]\]), ... bins=bins, legend='curve') \>\>\> curve_limits(curve, threshold = 3.5) \[(1.0, 1.0), (10.0, 15.0)\]

### `valjean.javert.plot_repr.pad_range(limits, log, padding=0.05)`

Pad the given limits.

This function adds a bit of padding to the input limit range. If `log` is `False`, the new limits will be `(limits[0] - padding * delta, limits[1] + padding * delta)`, where `delta = limits[1] - limits[0]`. In log scale (`log=True`), the padded limits are `(limits[0] * exp(-padding * log_delta), limits[1] * exp(padding * log_delta)`, with `log_delta = log(limits[1] / limits[0])`.

param (float, float) limits  
a pair of floats.

param bool log  
whether we are in log scale.

param float padding  
the amount of padding to insert.

returns  
new limits

rtype  
(float, float)

### `valjean.javert.plot_repr.post_treatment(templates, result)`

Post-treatment of plots after template generate.

For example add names from test result if not done before, suppress zero bins at range edges, etc.

### `valjean.javert.plot_repr.build_plot_template_with_dim(curves, axnames)`

Organise curves in `SubPlotElements`.

If curves are 1D they will all go in the same `SubPlotElements`, if there are in 2 dimensions each curve will have its `SubPlotElements`.

param list(CurveElements) curves  
list of curves

param list(str) axnames  
list of axis names

rtype  
list(SubPlotElements)

### `valjean.javert.plot_repr.repr_datasets_values(result)`

Representation of the datasets values from test results obtained from a child test of `TestDataset`.

Examples:

- `TestResultEqual`;
- `TestResultApproxEqual`;
- `TestResultStudent`.

param TestResult result  
test result from test on datasets

rtype  
list(PlotTemplate)

If the dimension cannot be determined or if the dimension is greater than 2 an empty list is returned.

### `valjean.javert.plot_repr.repr_testresultequal(result, _verbosity=Verbosity.DEFAULT)`

Represent the equal test result as a plot.

param TestResultEqual result  
a test result.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_testresultapproxequal(result, _verbosity=Verbosity.DEFAULT)`

Represent the approx equal test result as a plot.

param TestResultApproxEqual result  
a test result.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_testresultstudent(result, verbosity=Verbosity.DEFAULT)`

Plot the Student results according to verbosity.

param TestResultStudent result  
a test result.

returns  
Representation of a `TestResultStudent` as a plot.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_student_intermediate(result)`

Represent the Student test result as a plot.

By default two `PlotTemplate` are returned in order to get a top plot representing the two series of values and the bottom plot representing Student's t-statistic.

param TestResultStudent result  
a test result.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_student_full_details(result)`

Represent the Student test result as a plot.

By default two `PlotTemplate` are returned in order to get a top plot representing the two series of values and the bottom plot representing Student's t-statistic.

param TestResultStudent result  
a test result.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_student_tstud(result)`

Represent the t distribution from a Student test result as a plot.

param TestResultStudent result  
a test result.

rtype  
list(PlotTemplate)

Note

if we have a member `units` in dataset the axis names would be constructed like `name + units['name']`.

If the dimension cannot be determined an empty list is returned.

### `valjean.javert.plot_repr.repr_student_pvalues(result)`

Representation of p-values from Student test result as a plot.

param TestResultStudent result  
a test result.

rtype  
list(PlotTemplate)

If p-values were not calculated, no `PlotTemplate` is built, so an empty list is returned.

### `valjean.javert.plot_repr.repr_testresultmetadata(_result, _verbosity=Verbosity.DEFAULT)`

Plot metadata test -\> no plot done.

returns  
empty list

### `valjean.javert.plot_repr.repr_testresultexternal(_result, _verbosity=Verbosity.DEFAULT)`

Plot external test -\> no plot done.

If plots are required they are already done. Their representation in the report is done by `ExternalRepresenter`.

returns  
empty list

### `valjean.javert.plot_repr.repr_testresultfailed(_result, _verbosity=Verbosity.DEFAULT)`

Plot failed test -\> no plot done.

returns  
empty list

### `valjean.javert.plot_repr.repr_testresultstats(result, status_ok, label)`

Represent result from statistical test as a plot (pie chart probably).

Null results are omitted from the table.

param TestResult result  
result from a statistical test

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_testresultstatstasks(result, _verbosity=Verbosity.DEFAULT)`

Represent result from statistical test on tasks as a plot (pie chart).

param TestResultStatsTasks result  
result from tasks statistics

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_testresultstatstests(result, _verbosity=Verbosity.DEFAULT)`

Represent result from statistical test on tests as a plot (pie chart).

param TestResultStatsTests result  
result from tasks statistics

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_statstestsby2labels(result)`

Plot statistics on the tests classified by 2 labels.

Caution: the tests are summed over the second label, only the first one will be written on the plot. This is for summaries.

rtype  
list(PlotTemplate)

### `valjean.javert.plot_repr.repr_testresultstatstestsbylabels(result, _verbosity=Verbosity.DEFAULT)`

Plot statistics on the tests classified by labels if 1 or labels.

rtype  
list(PlotTemplate)
