<!-- source: modules/eponine/tripoli4/scan.rst -->

# `scan` – Scan Tripoli-4 outputs and select relevant results

Module performing a scan of Tripoli-4 output listing in order to only keep relevant parts of it = results to be used for V&V or analysis or the run.

## Summary

- Quickly reads the results file
- Recognize beginning and end of results sections
- Get the required number of batchs
- Get the edition batch numbers (if exists)

## Use of `scan`

scan

\>\>\> import os \>\>\> work_dir = 'scan' \>\>\> os.mkdir(work_dir) \>\>\> with open(os.path.join(work_dir, 'spam.res'), 'w') as tmpfile: ... print("BATCH 10n" ... "initialization time (s): 7n" ... " batch number : 10n" ... "RESULTS ARE GIVEN FOR SOURCE INTENSITY : 1.000000e+00n" ... "Edition after batch number : 10n" ... "simulation time (s) : 1n" ... "NORMAL COMPLETION", ... file=tmpfile)

To use this module you need to create a `Scanner` object giving at least the path to the file you want to read. This file should be a Tripoli-4 output containing at least the flags precised in `eponine-t4-scan-caveats`.

> \>\>\> import os \>\>\> from valjean.eponine.tripoli4.scan import Scanner \>\>\> results = Scanner(os.path.join(work_dir, 'spam.res')) \>\>\> results.normalend True \>\>\> len(results) 1 \>\>\> results.times\['initialization_time'\] 7
>
> The expected key of the `Scanner` object is the batch number, not an index. If you have the index you need to obtain the corresponding batch number first.
>
> \>\>\> 'simulation time' in results\[10\] \# batch number = 10 True \>\>\> 'simulation time' in results\[-1\] \# -1 can only be an index, like 0 Traceback (most recent call last): ... KeyError: -1 \>\>\> 'simulation time' in results\[results.batch_number(-1)\] True

Note

It will probably be better to directly load a test file...

## Caveats

### Beginning and end of results sections

Important for the scan: results will be kept

- **from** "RESULTS ARE GIVEN"
- **to** an end flag available in the list `Scanner.end_flags`. Possibilities are:
  - Default end flag is `"simulation time"`;
  - For exploitation jobs use `"exploitation time"` (example: Green bands);
  - for jobs running in parallel, `"elapsed time"` will also appear, after `"simulation time"` normal.

## Module API

### `class valjean.eponine.tripoli4.scan.PhEmEpBalanceOutput()`

Class to store photon-electron-positron balance.

#### `PhEmEpBalanceOutput.add_line(self, line)`

Add line to the photon electron positron output and counts.

### `class valjean.eponine.tripoli4.scan.HomogMatOutput()`

Class to store the homogenized material output.

#### `HomogMatOutput.add_line(self, line)`

Add line to the homogenized material output and count.

### `class valjean.eponine.tripoli4.scan.BatchResultScanner(current_batch, para, line)`

Class to build batchs collection.

param int current_batch  
current batch number

param bool para  
flag to identify outputs run in parallel

param str line  
current line in file

Note

- **current_batch** normally refers to lines before flag "RESULTS ARE GIVEN". They can be used if "Edition after batch number" does not appear in the file.
- **line** should contain "RESULTS ARE GIVEN" here. It is used to initialize the list of strings corresponding to the result block.

#### `BatchResultScanner.build_result(self, line)`

Scan line to build batch result: mainly deals with specific patterns and store line.

param str line  
last line to be taken into account

#### `BatchResultScanner.check_batch_number(self)`

Check batch number value and replace it by current value or by the greater value if needed.

#### `BatchResultScanner.get_result(self)`

Send result. Called if end flag has been found, add last line and concatenates result.

return  
string build from list of strings junction

### `class valjean.eponine.tripoli4.scan.ScannerException  — bases: Exception`

An error that may be raised by the `Scanner` class.

### `class valjean.eponine.tripoli4.scan.Scanner(fname, end_flag='')  — bases: Mapping`

Class to scan the Tripoli-4 listing and keep the relevant parts of it like results per batch used for edition or times.

There are no class variables, but instance variables (initialized when the object is built or when the file is read). They are directly accessible from the object. Main results are accessible directly from the `Scanner` object.

**Instance variables:**

`fname` (`str`)  
name of the file that will be scanned

`batches` (`dict`)  
keep the number of batches and the packet_length (read from file `fname`)

`normalend` (`bool`)  
presence of "NORMAL COMPLETION"

`end_flags` (`list` (`str`))  
possible end flags to stop the saving of results

`para` (`bool`)  
`True` in parallel mode

`countwarnings` (`int`)  
count number of warnings (for statistics)

`counterrors` (`int`)  
count number of errors (for statistics)

`times` (`collections.OrderedDict`)  
save times (initialization, simulation, exploitation and elapsed if exists). Mandatory ones are `'initialization time'` and `'simulation time'` or `'exploitation time'`. `'elapsed time'` only appears in listings from parallel jobs.

`last_generator_state` (`str`)  
keep the random generator state (not included in the result as given after `endflag`)

`phemep_balance` (`dict`)  
keep the photon electron positron balance as `str` indexed by batch number

`homog_mat` (`dict`)  
keep the homogenized material dump as `str` indexed by batch number

**Available methods:**

`Scanner` inherits from `collections.abc.Mapping` so many methods are implemented or available by default: `keys`, `items`, `values`, `get`, `__contains__` (used via `in`). `__getitem` (used with `[]`), `__iter__` (when iterators are required), `__len__` and `__reversed__` are redefined.

This class points on the `collections.OrderedDict` that it contains. The keys are the available batch numbers in the Tripoli-4 output, obtained using `scan_obj.keys()`.

#### `Scanner.batch_index(self, batch_number)`

Get the index of the batch_number in the results list.

#### `Scanner.batch_number(self, batch_index)`

Get the batch number from the batch index.

#### `Scanner.fatal_error(self)`

Return the fatal error message if found.

#### `Scanner.global_variables(self, batch_number)`

Return a dictionary of the global quantities in the TRIPOILI-4 output:

- warnings
- errors
- number of tasks (to distinguish MONO and PARA for example)
- normal end
- required batches
- partial (if the job as been stopped)
- batch number, especially when 'edition after batch number' is not in the Tripoli-4 output
- t4_file: path to the scanned file
- times of the required batch (can be simulation time, initialisation time, elapsed time)

param int batch_number  
batch number (used for times)

rtype  
dict

#### `Scanner.print_statistics(self)`

Print statistics of the listing scanned: normal end, number of warnings and errors.

#### `Scanner.check_times(self)`

Check times.

If the results come from a parallel job, the *times* dictionary should contain the `'elapsed_time'` key. In all kind of outputs or `'simulation_time'` or `'exploitation_time'` should be found (in parallel case the only possibility is in reality `'simulation_time'`). Finally, while `'initialization_time'` value is an *int* as occuring only once, the others are lists with length equal to the number of batches in the edition for `'simulation_time'` and `'exploitation_time'` and equal to the number of batches + 1 for `'elapsed_time'`. If all these checks are successful True is returned, else False.

rtype  
bool
