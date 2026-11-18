<!-- source: modules/javert/rst.rst -->

# `rst` – Convert items to rst format

This module provides the classes to convert test results to reStructuredText format. [reStructuredText](https://docutils.sourceforge.io/rst.html) is a text markup language meant for easy human consumption. The [reStructuredText primer](https://docutils.sourceforge.io/docs/user/rst/quickstart.html) provides a good introduction to its syntax.

### `class valjean.javert.rst.Rst(representation, *, n_workers=None)`

Class to convert `TestResult` objects into [reStructuredText](https://docutils.sourceforge.io/rst.html) format.

#### `Rst.clear(self)`

Clear the content of `self`.

#### `Rst.format_report(self, *, report, author, version)`

Format a report.

Most of the work is actually done in the `format_report_rec` method.

param TestReport report  
the report to format.

returns  
the formatted report.

rtype  
FormattedRst

#### `Rst.format_report_rec(self, *, report, tree)`

Recursively format report sections and populate the `tree_dict` and `text_dict` attributes.

Report sections, as represented by the `TestReport` class, are essentially trees, with `TestResult` objects playing the role of the tree leaves and `TestReport` objects playing the role of the tree nodes. This method performs a recursive, pre-order, depth-first traversal of the tree and fills the `tree_dict` and `text_dict` dictionaries with the information that is necessary to instantiate the final `FormattedRst` object.

Given a report object, this method constructs a dictionary key by concatenating in a tuple the titles of the parent reports and the present report. The tuple containing the parent reports' titles is recursively passed as the `tree` argument (and it is initialized to the empty tuple in the call from `format_report`). For instance, consider the following simplified report structure:

> \>\>\> from valjean.javert.test_report import TestReport \>\>\> subsub1 = TestReport(title='SubSub1') \>\>\> subsub2 = TestReport(title='SubSub2') \>\>\> sub1 = TestReport(title='Sub1', content=\[subsub1, subsub2\]) \>\>\> sub2 = TestReport(title='Sub2') \>\>\> main = TestReport(title='Main', content=\[sub1, sub2\], ... text='Si six scies scient six cyprès, ' ... 'six-cent-six scies scient ' ... 'six-cent-six cyprès.')

We instantiate an `Rst` object and we format the report:

> \>\>\> import valjean.javert.representation as rpr \>\>\> from valjean.javert.rst import Rst \>\>\> rst = Rst(rpr.Representation(rpr.FullRepresenter())) \>\>\> formatted_report = rst.format_report(report=main, author='Me', ... version='0.1')

Let us look at the dictionary keys:

> \>\>\> print(sorted(rst.text_dict.keys())) \[(), ('Sub1',), ('Sub1', 'SubSub1'), ('Sub1', 'SubSub2'), ('Sub2',)\]

The empty tuple, `()`, is associated to the main report. The other keys represent subreports. The length of the tuple corresponds to the depth of the nested report; for instance, the `'SubSub2'` section appears in the `('Sub1', 'SubSub2')` tuple with length 2, because `'SubSub2'` is nested twice (`Main`/`Sub1`/`SubSub2`).

The values of the `text_dict` dictionary are lists of strings representing the text of the given section. For instance, here is what the main section looks like:

\>\>\> print('n'.join(rst.text_dict\[()\])) Main ==== \<BLANKLINE\> Si six scies scient six cyprès, six-cent-six scies scient six-cent-six cyprès. \<BLANKLINE\>

The `tree_dict` dictionary associates a tuple representing a report section to the list of tuples that represent the subsections:

> \>\>\> print(rst.tree_dict\[()\]) \[('Sub1',), ('Sub2',)\] \>\>\> print(rst.tree_dict\[('Sub1',)\]) \[('Sub1', 'SubSub1'), ('Sub1', 'SubSub2')\]

If a section does not have any subsection, the corresponding tuple does not appear in the dictionary:

> \>\>\> ('Sub2',) in rst.tree_dict False

The `tree_dict` and `text_dict` dictionaries contain most of the information required by `FormattedRst` to write out the report in the form of a [reStructuredText](https://docutils.sourceforge.io/rst.html) file tree (see `write`).

#### `Rst.format_section(self, section, *, depth)`

Format a report section.

param TestReport report  
the report section to format.

returns  
the formatted report section.

rtype  
str

#### `Rst.format_result(self, result)`

Format one test result.

param TestResult result  
A `TestResult`.

returns  
the formatted test result.

rtype  
str

### `class valjean.javert.rst.RstFormatter  — bases: Formatter`

Class that dispatches the task of formatting templates as [reStructuredText](https://docutils.sourceforge.io/rst.html). The concrete formatting is handled by separate classes (`RstTable`...).

#### `RstFormatter.header(self, name, depth)`

Produce the header for formatting a `TestResult`.

param str name  
A header name

param int depth  
the depth of this header, 0 being the top.

returns  
the test header, for inclusion in a reST document.

rtype  
str

#### `RstFormatter.text(self, text)`

Format some text.

param str text  
some text to include.

returns  
the text, in rst format.

rtype  
str

#### `RstFormatter.anchor(fingerprint)`

Format an anchor with the given fingerprint.

#### `RstFormatter.format_tabletemplate(table)`

Format a `TableTemplate`.

param TableTemplate table  
A table.

returns  
the reST table.

rtype  
RstTable

#### `RstFormatter.format_plottemplate(plot)`

Format a `PlotTemplate`.

param PlotTemplate plot  
A plot.

returns  
the formatted plot

rtype  
RstPlot

#### `RstFormatter.format_texttemplate(text)`

Format a `TextTemplate`.

param TextTemplate text  
A text with its highlight positions

returns  
the formatted text (text itself)

rtype  
str

### `class valjean.javert.rst.RstTable(table, num_fmt='{:11.6g}')`

Convert a `TableTemplate` into a [reStructuredText](https://docutils.sourceforge.io/rst.html) table.

#### `RstTable.tabularize(cls, headers, rows, *, indent=0)`

Transform a list of headers and a list of rows into a nice reST table.

The `headers` argument must be a list of strings. The `rows` argument represents the table rows, as a list of lists of strings. Each sublist represents a table row, and it must have the same length as `headers`, or terrible things will happen.

The column widths are automatically computed to accommodate the largest template in each column. Smaller templates are automatically right-justified.

\>\>\> headers = \['name', 'quest', 'favourite colour'\] \>\>\> rows = \[\['Lancelot', 'to seek the Holy Grail', 'blue'\], ... \['Galahad', 'to seek the Holy Grail', 'yellow'\]\] \>\>\> table = RstTable.tabularize(headers, rows) \>\>\> print(table) ======== ====================== ================ name quest favourite colour ======== ====================== ================ Lancelot to seek the Holy Grail blue Galahad to seek the Holy Grail yellow ======== ====================== ================ \<BLANKLINE\>

You can also indent the table by a given amount of spaces with the `indent` keyword argument:

\>\>\> table = RstTable.tabularize(headers, rows, indent=4) \>\>\> print(table) ======== ====================== ================ name quest favourite colour ======== ====================== ================ Lancelot to seek the Holy Grail blue Galahad to seek the Holy Grail yellow ======== ====================== ================ \<BLANKLINE\>

param list(str) headers  
The table headers.

param list(list(str)) rows  
The table rows.

returns  
The reST table, as a string.

#### `RstTable.transpose(columns)`

Given a matrix as a list of columns, yield the matrix rows. (Equivalently, if the matrix is given as a list of rows, yield the columns). For instance, consider the following list:

> \>\>\> matrix = \[(11, 21, 31), (12, 22, 32), (13, 23, 33)\] \>\>\> for column in matrix: ... print(' '.join(str(elem) for elem in column)) 11 21 31 12 22 32 13 23 33

If the tuples are interpreted as columns, `matrix` represents the following matrix:

$$\begin{aligned}
\begin{pmatrix}11&12&13\\21&22&23\\31&32&33\end{pmatrix}
\end{aligned}$$

Transposing it yields:

> \>\>\> transposed = RstTable.transpose(matrix) \>\>\> for row in transposed: ... print(' '.join(str(elem) for elem in row)) 11 12 13 21 22 23 31 32 33

Note

The matrix elements returned by `transpose` are actually 0-dimensional `numpy.ndarray` objects. For the purpose of their further manipulation this is of little consequence, as they transparently support most numerical operations.

param columns  
An iterable yielding columns

type columns  
list(list) or list(tuple) or list(numpy.ndarray)

raises ValueError  
if the columns do not have the same length.

returns  
a generator for the rows of the transposed matrix.

#### `RstTable.format_columns(cls, columns, highlights, num_fmt)`

Transform a bunch of columns (containing arbitrary data: floats, bools, ints, strings...) into an iterable of lists of (optionally highlighted) strings representing the table **rows**.

Example:

> \>\>\> cols = \[('European swallow', 'African swallow'), ... (27.7, 35.1), ... ('km/h', 'km/h')\] \>\>\> highs = \[\[False, False\], \[False, True\], \[False, True\]\] \>\>\> for row in RstTable.format_columns(cols, highs, '{:13.8f}'): ... print(row) \['European swallow', ' 27.70000000', 'km/h'\] \['African swallow', '`35.10000000`', '`km/h`'\]

param columns  
An iterable yielding columns. The table columns may contain any kind of data; if the data type is numeric, it will be formatted according to the `num_fmt` argument; other types will just get stringified (`str`).

param highlights  
An iterable yielding a collection of bools for each column. The `j`-th element of the `i`-th iteration decides whether the element in the `j`-th column of the `i`-th row should be highlighted.

param num_fmt  
The format string to be used for numerical types.

returns  
a generator yielding lists of strings, representing the table rows.

#### `RstTable.compute_column_widths(headers, rows)`

Compute the width of the columns that are necessary to accommodate all the headers and table rows.

> \>\>\> headers = \['swallow sub-species', 'airspeed', 'laden'\] \>\>\> rows = \[\['European', '27.7 km/h', 'no'\], ... \['European', '22.0 km/h', 'yes'\], ... \['African', '35.1 km/h', 'no'\], ... \['African', '26.2 km/h', 'yes'\]\] \>\>\> RstTable.compute_column_widths(headers, rows) \[19, 9, 5\] \>\>\> \[len('swallow sub-species'), len('27.7 km/h'), len('laden')\] \[19, 9, 5\]

param list(str) headers  
A list of column headers.

param list(list(str)) rows  
A list of table rows.

returns  
a list of integers indicating how wide each columns must be to accommodate all the table elements and the headers.

rtype  
list(int)

#### `RstTable.highlight(cls, val, flag)`

Wrap `val` in highlight reST markers if flag is `True`.

\>\>\> RstTable.highlight('dis', False) 'dis' \>\>\> RstTable.highlight('DAT', True) '`DAT`'

#### `RstTable.concat_rows(cls, widths, rows, just='>')`

Concatenate the given rows and justify them according to the `just` parameter (see the `python:formatspec`). The columns widths (for justification) must be provided using the `width` argument.

param list(int) widths  
The list of columns widths.

param list(list(str)) rows  
The list of rows; each row must be a list of strings.

param str just  
A format character for the justification (usually one of '\<', '^', '\>').

returns  
the concatenated, justified rows.

rtype  
str

### `class valjean.javert.rst.RstPlot(plot)`

This class models a plot in an [reStructuredText](https://docutils.sourceforge.io/rst.html) document. It converts a `PlotTemplate` object into an `MplPlot`, and it provides the `.. image::` directive to include in the .rst file.

#### `RstPlot.filename(self)`

Make up a(n almost) unique filename for this plot.

returns  
the filename from fingerprint (png format)

rtype  
str

### `class valjean.javert.rst.RstText(text)`

Construct an `RstText` from the given `TextTemplate`.

### `class valjean.javert.rst.FormattedRst(*, author, title, version, tree_dict, text_dict, plots, n_workers=None)`

This class represents a formatted rst document tree, which typically consists of an index file and of several sections.

#### `FormattedRst.write(self, path)`

Write the text files and the plots into the directory specified by `path`.

param path  
path to the directory that will be written to. It is OK if the directory does not exist.

type path  
str or pathlib.Path

#### `FormattedRst.tree_to_path(*, base, tree)`

Convert a tree to a file path.

param base  
the base path for all subtrees.

type base  
pathlib.Path

param tuple(str) tree  
a sequence of tree nodes, starting from the tree root.

#### `FormattedRst.toc(self, toc_title, subtrees)`

Build an rst table of contents.

param str toc_title  
the title for the table of contents (e.g. `'Contents'`).

#### `FormattedRst.setup(self, path)`

Set up the output directory for `write`.

param pathlib.Path path  
the path to the directory.

#### `FormattedRst.configure(resource, dest, formatting=True, **kwargs)`

Copy a package resource to the specified destination, optionally formatting the resource content using `str.format`.

For more information about resources, see [pkg_resources](https://setuptools.pypa.io/en/latest/pkg_resources.html).

param str resource  
the name of the resource.

param pathlib.Path dest  
the destination path.

param bool formatting  
whether formatting should be applied.

param dict kwargs  
any additional keyword arguments will be passed to the formatting.

### `class valjean.javert.rst.RstTestReportTask(name, *, report_task, representation, author, version, deps=None, soft_deps=None)  — bases: PythonTask`

Task class that transforms a list of tests into a test report. `TestResult` objects in the environment.

#### `RstTestReportTask.from_tasks(cls, name, *, make_report, eval_tasks, representation, author, version, kwargs=None, deps=None, soft_deps=None)`

Construct an `RstTestReportTask` from a list of test evaluation tasks and a function to classify test results and put them in test reports.
