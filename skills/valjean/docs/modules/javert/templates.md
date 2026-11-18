<!-- source: modules/javert/templates.rst -->

# `templates` – Things that can be put in the report

This module contains classes that are supposed to act as containers of all the information that is necessary to represent a test in a given format. For instance, in the case of tables this includes the column contents, the headers, etc. It does **not** include any formatting information, such as column widths, floating-point precision, colours, etc. Decisions about the formatting are handled by suitable formatting classes, such as `Rst`.

### `class valjean.javert.templates.TableTemplate(*columns, headers=None, units=None, highlights=None)`

A container class that encapsulates all the necessary information to represent a table.

Examples of use of mainly show in context of concatentation of `TableTemplate`, obtained with the `join` method.

\>\>\> import numpy as np \>\>\> tit1 = TableTemplate([np.float]()(1.5), [np.float]()(1.4), ... headers=\['egg', 'spam'\]) \>\>\> tit2 = TableTemplate([np.float]()(1.2), [np.float]()(0.9), ... headers=\['egg', 'spam'\]) \>\>\> stab12 = join(tit1, tit2) \>\>\> print(len(tit1.columns), len(tit2.columns)) 2 2 \>\>\> print(tit1.columns\[0\].size, tit2.columns\[0\].size) 1 1 \>\>\> print(len(stab12.columns)) 2 \>\>\> print(stab12.columns\[0\].size) 2 \>\>\> print(f"{stab12!r}") class: \<class 'valjean.javert.templates.TableTemplate'\> headers: \['egg', 'spam'\] egg: \[1.5 1.2\] spam: \[1.4 0.9\] highlights: \[array(\[0., 0.\]), array(\[0., 0.\])\]

`stab12` contained both `tit1` and `tit2` as expected. Headers of the columns are the same, length of the columns is the sum of the two.

\>\>\> tit3 = TableTemplate([np.float]()(0.8), [np.float]()(1.1), ... headers=\['knight', 'parrot'\]) \>\>\> stab13 = join(tit1, tit3) Traceback (most recent call last): ... ValueError: TableTemplates to add should have same headers

An error is raised as the two `TableTemplate` don't contain the same headers, so not the same kind of columns, thus they cannot be concatenated.

It is also possible to join tables with same headers but different 'types' (scalars and arrays):

\>\>\> tit4 = TableTemplate(np.arange(4), np.arange(4)\*0.5, ... headers=\['egg', 'spam'\]) \>\>\> print(len(tit4.columns), tit4.columns\[0\].size) 2 4 \>\>\> stab14 = join(tit1, tit4) \>\>\> print(len(stab14.columns), stab14.columns\[0\].size) 2 5 \>\>\> stab14.columns\[0\].size == tit1.columns\[0\].size + tit4.columns\[0\].size True \>\>\> print(f"{stab14!r}") class: \<class 'valjean.javert.templates.TableTemplate'\> headers: \['egg', 'spam'\] egg: \[1.5 0. 1. 2. 3. \] spam: \[1.4 0. 0.5 1. 1.5\] highlights: \[array(\[0., 0., 0., 0., 0.\]), array(\[0., 0., 0., 0., 0.\])\]

It is also possible to join arrays, a bigger array is obtained, without separation between the initial `TableTemplate`:

\>\>\> tit5 = TableTemplate(np.arange(3)*0.1, np.arange(3)*0.05, ... headers=\['egg', 'spam'\]) \>\>\> stab45 = join(tit4, tit5) \>\>\> print(len(stab45.columns), len(stab45.columns\[0\])) 2 7 \>\>\> print(f"{stab45!r}") class: \<class 'valjean.javert.templates.TableTemplate'\> headers: \['egg', 'spam'\] egg: \[0. 1. 2. 3. 0. 0.1 0.2\] spam: \[0. 0.5 1. 1.5 0. 0.05 0.1 \] highlights: \[array(\[0., 0., 0., 0., 0., 0., 0.\]), array(\[0., 0., 0., 0., 0., 0., 0.\])\]

Any number of `TableTemplate` can be joined (if fulfilling the requirements).

\>\>\> stab145 = join(tit1, tit4, tit5) \>\>\> print(f"{stab145!r}") class: \<class 'valjean.javert.templates.TableTemplate'\> headers: \['egg', 'spam'\] egg: \[1.5 0. 1. 2. 3. 0. 0.1 0.2\] spam: \[1.4 0. 0.5 1. 1.5 0. 0.05 0.1 \] highlights: \[array(\[0., 0., 0., 0., 0., 0., 0., 0.\]), array(\[0., 0., 0., 0., 0., 0., 0., 0.\])\]

The `TableTemplate.join` method updates the left `TableTemplate` as expected:

\>\>\> tit1.join(tit4, tit5) \>\>\> print(f"{tit1!r}") class: \<class 'valjean.javert.templates.TableTemplate'\> headers: \['egg', 'spam'\] egg: \[1.5 0. 1. 2. 3. 0. 0.1 0.2\] spam: \[1.4 0. 0.5 1. 1.5 0. 0.05 0.1 \] highlights: \[array(\[0., 0., 0., 0., 0., 0., 0., 0.\]), array(\[0., 0., 0., 0., 0., 0., 0., 0.\])\]

#### `TableTemplate.copy(self)`

Copy a `TableTemplate` object.

rtype  
TableTemplate

Note

the highlignt function is not really copied, it has the same address as the self one. I don't know how to change that.

#### `TableTemplate.join(self, *others)`

Join a given number a `TableTemplate` to the current one.

Only `TableTemplate` with the same number of columns and same headers can be joined. The method returns the updated current one.

param others  
list of TableTemplates to be joined to the current TableTemplate

type others  
list(TableTemplate)

#### `TableTemplate.data(self)`

Yield bytes representing `self`. Two `TableTemplate` objects containing equal data yield the same data.

### `class valjean.javert.templates.CurveElements(values, bins, legend, *, index=0, errors=None)`

Define the characteristics of a curve to plot.

#### `CurveElements.copy(self)`

Copy a `CurveElements` object.

rtype  
CurveElements

#### `CurveElements.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.javert.templates.SubPlotAttributes(dim)`

Container to store sub-plots attributes:

- axis limits
- axis scale: linear (default) or logatithmic
- additional horizontal or vertical lines

Theses attributes are independent of the used backend (examples: **matplotlib**, **Root**, **gnuplot**, **D3**). The backend then gets the attributes and apply them with its own features.

> If needed new attributes can be added.

#### `SubPlotAttributes.copy(self)`

Copy a `SubPlotAttributes` object.

rtype  
SubPlotAttributes

#### `SubPlotAttributes.limits`

Return limits.

#### `SubPlotAttributes.limits(self, limits)`

Store limits for curves in the `PlotTemplate`.

param list(tuple) limits  
limits for each axis of the sub-plot

Each tuple corresponds to an axis, 2 values are expected: min and max.

#### `SubPlotAttributes.lines`

Return lines to be plotted.

#### `SubPlotAttributes.lines(self, lines)`

Set lines to be added to the plots.

param list(list(dict)) lines  
lines to be added to the plots

### `class valjean.javert.templates.SubPlotElementsException  — bases: Exception`

Error raised if the sub plot looks inconsistent.

### `class valjean.javert.templates.SubPlotElements(*, curves, axnames=('', ''), ptype='1D')`

Container to store a given sub-plot.

#### `SubPlotElements.copy(self)`

Copy a `SubPlotElements` object.

rtype  
SubPlotElements

#### `SubPlotElements.data(self)`

Generator yielding objects supporting the buffer protocol that (as a whole) represent a serialized version of `self`.

### `class valjean.javert.templates.PlotTemplate(*, subplots, small_subplots=True, suppress_xaxes=False, suppress_legends=False, backend_kw=None)`

A container for full test result to be represented as a plot. This includes all the datasets and the test result. This can also include p-values or other test parameters, depending on what is given to the `PlotTemplate`.

Examples mainly present the `join` method, used to concatentate `PlotTemplate`.

\>\>\> bins1, d11, d12 = np.arange(4), np.arange(4), np.arange(4)*10 \>\>\> d13 = d11 + d12 \>\>\> bins2, d2 = np.arange(5), np.arange(5)*0.5 \>\>\> pit1 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d11, \[bins1\], 'd11', index=0)\], ... axnames=\['egg', 'brandy'\])\]) \>\>\> pit2 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d12, bins=\[bins1\], legend='d12', index=1)\], ... axnames=\['egg', 'beer'\])\]) \>\>\> pit3 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d13, legend='d13', bins=\[bins1\], index=2)\], ... axnames=\['egg', 'wine'\])\]) \>\>\> splt123 = join(pit1, pit2, pit3) \>\>\> print(f"{splt123!r}") class: \<class 'valjean.javert.templates.PlotTemplate'\> N subplots: 3 Subplot 0 axnames: \['egg', 'brandy'\], plot type: 1D, N curves: 1 Curve 0 legend: d11 index: 0 bins: \[array(\[0, 1, 2, 3\])\] values: \[0 1 2 3\] errors: None Subplot 1 axnames: \['egg', 'beer'\], plot type: 1D, N curves: 1 Curve 0 legend: d12 index: 1 bins: \[array(\[0, 1, 2, 3\])\] values: \[ 0 10 20 30\] errors: None Subplot 2 axnames: \['egg', 'wine'\], plot type: 1D, N curves: 1 Curve 0 legend: d13 index: 2 bins: \[array(\[0, 1, 2, 3\])\] values: \[ 0 11 22 33\] errors: None \<BLANKLINE\>

As expected a new `PlotTemplate` is obtained, containing three subplots, each one containing one curve.

Like in the TableTemplate case, the `PlotTemplate.join` method updates the left `PlotTemplate` as expected:

\>\>\> pit1.join(pit2, pit3) \>\>\> pit1 == splt123 True

A new curve with the same axes will also create a new suplot:

\>\>\> d14 = d11\*2 \>\>\> pit4 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d14, legend='d14', index=3, bins=\[bins1\])\], ... axnames=\['egg', 'beer'\])\]) \>\>\> split24 = join(pit2, pit4) \>\>\> print(split24) class: \<class 'valjean.javert.templates.PlotTemplate'\> Subplot 0 axnames: \['egg', 'beer'\], plot type: 1D Curve 0 legend: d12 index: 1 bins: \[array(\[0, 1, 2, 3\])\] Subplot 1 axnames: \['egg', 'beer'\], plot type: 1D Curve 0 legend: d14 index: 3 bins: \[array(\[0, 1, 2, 3\])\] \<BLANKLINE\>

To get it in the same subplot it has to be done at creation.

\>\>\> pit24 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d12, legend='d12', index=1, bins=\[bins1\]), ... CurveElements(d14, legend='d14', index=3, bins=\[bins1\])\], ... axnames=\['egg', 'beer'\])\]) \>\>\> print(pit24) class: \<class 'valjean.javert.templates.PlotTemplate'\> Subplot 0 axnames: \['egg', 'beer'\], plot type: 1D Curve 0 legend: d12 index: 1 bins: \[array(\[0, 1, 2, 3\])\] Curve 1 legend: d14 index: 3 bins: \[array(\[0, 1, 2, 3\])\] \<BLANKLINE\> \>\>\> split24 == pit24 False

N-dimensional plot templates can be built, but the plotting engine may not be able to convert multi-dimensional templates into plots.

The same behavior is expected for multi-dimensions plots: `join` will had a new subplot. To be noted: only one curve can be plotted on a subplot in multi-dimensional case, so any additional curve will throw a warning. Plot representation may not be as expected.

\>\>\> d31 = np.arange(bins1.size\*bins2.size).reshape(bins1.size, bins2.size) \>\>\> d32 = np.arange(bins1.size\*bins2.size).reshape( ... bins1.size, bins2.size)\*0.01 \>\>\> pit7 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d31, bins=\[bins1, bins2\], ... legend='d31', index=0)\], ... axnames=\['egg', 'spam', 'bacon'\], ptype='2D')\]) \>\>\> pit8 = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(d32, bins=\[bins1, bins2\], ... legend='d32', index=1)\], ... axnames=\['egg', 'spam', 'lobster'\], ptype='2D')\]) \>\>\> splt78 = join(pit7, pit8) \>\>\> print(f"{splt78!s}") class: \<class 'valjean.javert.templates.PlotTemplate'\> Subplot 0 axnames: \['egg', 'spam', 'bacon'\], plot type: 2D Curve 0 legend: d31 index: 0 bins: \[array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3, 4\])\] Subplot 1 axnames: \['egg', 'spam', 'lobster'\], plot type: 2D Curve 0 legend: d32 index: 1 bins: \[array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3, 4\])\] \<BLANKLINE\>

It is also possible to mix 1D and 2D plots:

\>\>\> splt27 = join(pit2, pit7) \>\>\> print(f"{splt27!s}") class: \<class 'valjean.javert.templates.PlotTemplate'\> Subplot 0 axnames: \['egg', 'beer'\], plot type: 1D Curve 0 legend: d12 index: 1 bins: \[array(\[0, 1, 2, 3\])\] Subplot 1 axnames: \['egg', 'spam', 'bacon'\], plot type: 2D Curve 0 legend: d31 index: 0 bins: \[array(\[0, 1, 2, 3\]), array(\[0, 1, 2, 3, 4\])\] \<BLANKLINE\>

#### `PlotTemplate.copy(self)`

Copy a `PlotTemplate` object.

rtype  
PlotTemplate

#### `PlotTemplate.join(self, *others)`

Join a given number a `PlotTemplate` to the current one.

Only `PlotTemplate` with the same number of columns and same headers can be joined. The method returns the updated current one.

param others  
list of PlotTemplates to be join with the current PlotTemplate

type others  
list(PlotTemplate)

#### `PlotTemplate.data(self)`

Yield bytes representing `self`. Two `TableTemplate` objects containing equal data yield the same data.

#### `PlotTemplate.curves_index(self)`

Return a sorted list of unique index of the curves.

### `class valjean.javert.templates.TextTemplate(text)`

A container class that encapsulates text for the report.

The user has to write the text as a string. ReST markdown can be used as compilation is expected to be done by sphinx.

Note

Titles might not be well represented in a ReSt formatted TextTemplate: no knowledge of the current level of title, nor the associated symbol. Lists or enumerations might be more suitable.

As in the other templates, examples will focus on the concatenation (join) of different TextTemplate.

\>\>\> ttplt1 = TextTemplate('Spam egg bacon') \>\>\> print(f"{ttplt1!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='Spam egg bacon') \>\>\> ttplt2 = TextTemplate('**Spam** egg bacon') \>\>\> print(f"{ttplt2!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='**Spam** egg bacon') \>\>\> ttplt3 = TextTemplate(r".. role:: hlnnsausage `tomato`") \>\>\> ttplt1.join(ttplt3) \>\>\> print(f"{ttplt1!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='Spam egg bacon.. role:: hl\n\nsausage `tomato`')

The sphinx compilation will fail there, as the are no empty line between the first and the second string. If you know some text will follow, think about the `\n`.

\>\>\> ttplt1 = TextTemplate('Spam egg baconnn') \>\>\> ttplt3 = TextTemplate('.. role:: hlnnsausage `tomato`nn') \>\>\> ttplt1.join(ttplt3) \>\>\> print(f"{ttplt1!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='Spam egg baconnn.. role:: hlnnsausage `tomato`nn')

Test of the external function `join`:

\>\>\> ttplt4 = join(ttplt3, ttplt3) \>\>\> print(f"{ttplt4!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='.. role:: hlnnsausage `tomato`nn.. role:: hlnnsausage `tomato`nn')

The copy doesn't affect the original:

\>\>\> ttplt5 = ttplt2.copy() \>\>\> ttplt5.text += ' sausage' \>\>\> print(f"{ttplt2!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='**Spam** egg bacon') \>\>\> print(f"{ttplt5!r}") \<class 'valjean.javert.templates.TextTemplate'\>(text='**Spam** egg bacon sausage')

#### `TextTemplate.copy(self)`

Copy a `TextTemplate` object.

rtype  
TextTemplate

#### `TextTemplate.join(self, *others)`

Join a given number of `TextTemplate` to the current one.

#### `TextTemplate.data(self)`

Yield bytes representing `self`. Two `TableTemplate` objects containing equal data yield the same data.

### `valjean.javert.templates.join(*templates)`

Join a "list" of templates of same kind, `TableTemplate` or `PlotTemplate` using the related `join` methods.

It returns a new templates (`TableTemplate` or `PlotTemplate`).

param templates  
list of templates

type templates  
list(TableTemplate) or list(PlotTemplate)

rtype  
TableTemplate, PlotTemplate, TextTemplate

See `TableTemplate` and `PlotTemplate` for examples of use. Only few error cases will be shown here:

\>\>\> bins1, data11, data12 = np.arange(4), np.arange(4), np.arange(4)*10 \>\>\> bins2, data2 = np.arange(5), np.arange(5)*0.5 \>\>\> tablit = TableTemplate(bins1, data11, headers=\['egg', 'spam'\]) \>\>\> plotit = PlotTemplate(subplots=\[SubPlotElements( ... curves=\[CurveElements(data11, bins=\[bins1\], legend='d11')\], ... axnames=\['egg', 'spam'\])\]) \>\>\> tit = join(tablit, plotit) Traceback (most recent call last): ... TypeError: Only a TableTemplate can be joined to another TableTemplate \>\>\> tit = join(plotit, tablit) Traceback (most recent call last): ... TypeError: Only a PlotTemplate can be joined to another PlotTemplate
