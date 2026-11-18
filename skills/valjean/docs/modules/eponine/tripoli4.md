<!-- source: modules/eponine/tripoli4.rst -->

# `tripoli4` – Parsing for Tripoli-4

 .. \_pyparsing: <https://pythonhosted.org/pyparsing/>

## Introduction

The goal of this sub-package is to parse Tripoli-4 results giving them an easy access and transforming them in the standard data format of `valjean`.

It contains various modules from scanning the Tripoli-4 output to conversion of its data in datasets, listed here starting from the most external modules to the innest ones:

> - Integration of parsing in the `valjean` workflow is handled by `use`;
>
> - Conversion of data to `Dataset` in `data_convertor`;
>
> - Parsing module `parse` calling the scanning one `scan`;
>
> - The parsing itself is done thanks to 3 modules:
>
>   > - `grammar`: the grammar of the Tripoli-4 ASCII output using `pyparsing`;
>   > - `transform`: methods to transform the parsing result in standard `python` and `NumPy` objects called in `grammar` via `setParseAction` applied on the `pyparsing.ParseResults`;
>   > - `common`: methods to transform Tripoli-4 data in `NumPy` objects.
>   > - One additional module parsing module is available for debugging and development: `parse_debug`
>
> > - Access to Tripoli-4 results from depletion, so reading ROOT files is handled by `depletion`.

## Main modules

- `tripoli4/data_convertor` (`tripoli4/data_convertor.md`)
- `tripoli4/parse` (`tripoli4/parse.md`)
- `tripoli4/scan` (`tripoli4/scan.md`)
- `tripoli4/use` (`tripoli4/use.md`)
- `tripoli4/depletion` (`tripoli4/depletion.md`)

## More details on parsing

Most of the Tripoli-4 functionalities are now parsed by [pyparsing](). If a new score or a new response is implemented in Tripoli-4, it would be easier for its output to match the existing responses, or else parsing will have to be updated.

When parsing fails it indicates the last line and column where parsing succeeded (relative to the beginning of the parsed string, not the full output) and the problematic line. This should help debugging.

Tests should be performed in the code to take the latter case into account (example: test presence of `'simulation time'` keyword, see `check_times`).

- `tripoli4/grammar` (`tripoli4/grammar.md`)
- `tripoli4/transform` (`tripoli4/transform.md`)
- `tripoli4/common` (`tripoli4/common.md`)
- `tripoli4/parse_debug` (`tripoli4/parse_debug.md`)
