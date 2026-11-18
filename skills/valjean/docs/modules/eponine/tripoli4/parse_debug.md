<!-- source: modules/eponine/tripoli4/parse_debug.rst -->

# `parse_debug` – Debug parsing of Tripoli-4 outputs

Extension of `parse` module for debugging.

Main difference is the possibility of using the `end_flag` parameter in the `scan`.

### `class valjean.eponine.tripoli4.parse_debug.ParserDebug(jddname, *, end_flag='', ofile='')  — bases: Parser`

Scan up to the end flag then parse. For parsing debugging.

#### `ParserDebug.parse_from_number(self, batch_number, name='')`

Parse from batch index or batch number.

Per default the last batch is parsed (index = -1).

param int batch_number  
the number of the batch to parse

returns  
list(dict)

#### `ParserDebug.check_parsing(self, parsed_res)`

Check if parsing went to the end:

- if the end flag was not precised, a time should appear in the last result;
- if not, no check can be performed as the end flag can be anywhere, even "transformed" during parsing.

Print a logger message if not found but don't block access to the parsing result (this can help to find the issue).
