<!-- source: modules/eponine/tripoli4/parse.rst -->

# `parse` – Parse Tripoli-4 outputs

Module performing scanning and parsing of Tripoli-4 outputs.

This module also allows quick checks on outputs:

- presence of `"NORMAL COMPLETION"`
- presence and values of times (simulation, exploitation)

Some options for debugging are available (end flag).

Change absolute imports in relative ones when main will be moved to `cambronne`.

### `class valjean.eponine.tripoli4.parse.ParserException  — bases: Exception`

An error that may be raised by the `Parser` class.

### `class valjean.eponine.tripoli4.parse.Parser(jddname)`

Scan Tripoli-4 listings, then parse the required batches.

#### `Parser.batch_numbers(self)`

Help method to get the available batch numbers.

rtype  
list(int)

#### `Parser.parse_from_number(self, batch_number, name='')`

Parse from batch index or batch number.

param int batch_number  
number of the batch to parse

rtype  
ParseResult

#### `Parser.parse_from_index(self, batch_index=-1, name='')`

Parse from batch index or batch number.

Per default the last batch is parsed (index = -1).

param int batch_index  
index of the batch in the list of batches

rtype  
ParseResult

#### `Parser.print_stats(self)`

Print Tripoli-4 statistics (warnings and errors).

#### `Parser.check_times(self)`

Check if running times are well written in Tripoli-4 listings. These times are at the end of the result block and mark the end flag.

returns  
boolean, True if well present, else False

Returned bool depends on the listing:

- if the job was run in parallel mode (and declared so), `"simulation time"` and `"elapsed time"` should be present in that order, only the second one is checked
- if the listing name contains `"exploit"` or `"verif"`, it is most probably an exploitation job (Green bands for example), `"exploitation time"` is checked
- else `"simulation time"` is checked

#### `Parser.print_times(self)`

Print time characteristics of the Tripoli-4 result considered. This print includes initialization time, simulation time, exploitation time and elapsed time.

### `class valjean.eponine.tripoli4.parse.ParseResult(parse_res, scan_vars, name='')`

Class containing a parsing result from Tripoli-4 output for one batch.

The `ParseResult` object is accessible from the instance attribute

`res`  
that is a unique dictionary containing all the results from scanning and parsing steps. Variables characteristic to a batch are stored under the key `'batch_data'` no matter if they come from `.Scanner` or from `Parser`. Variables characteristic to a run (= one execution of Tripoli-4) are stored under `'run_data'`, coming from the scanning step.

It is possible to transform the `res` dictionary in a `Browser` thanks to the method `to_browser`.

#### `ParseResult.to_browser(self)`

Get a `Browser` from the `ParseResult`.

The global variables in Browser are the batch data. You can access the `run data` only from the parsed result.

rtype  
Browser
