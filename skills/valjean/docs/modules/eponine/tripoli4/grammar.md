<!-- source: modules/eponine/tripoli4/grammar.rst -->

# `grammar` – Pyparsing grammar

This module provides `pyparsing` grammar for Tripoli-4 output listings.

Documentation on the `pyparsing` package can be found at [pyparsing](https://pythonhosted.org/pyparsing/).

Transformation from `pyparsing.ParseResults` to more standard python objects, including `numpy` arrays, is done with `transform`, calling `common`.

## Generalitites

- This parser only parses the result part of the listing (selection done in `scan`).
- It takes into account all responses in `qualtrip` database up to Tripoli-4, version 10.2.
- If a response is not taken into account parsing will fail:
  - with a big, ugly message ending by location of the end of successful parsing in the result string (possible to print it) → normally where starts your new response
  - it seems to end normally, but did not in reality. One of the best checks in that case is to test if the `endflag` in `scan` was read in the parser, usually not. Then the new response probably have to be added.
- A general parser is proposed for use in the file, but other parsers can be built from the partial parsers written here
- Numbers are automatically converted to `numpy` numbers (possibility to choose the dtype used for numbers)
- Keywords and most of the variables used to build parsers are private

## Organisation

This module is divided in 3 parts:

keywords:  
list of all keywords used to parse the listings, this part is important as these keywords trigger the parsing

parsers:  
parsers for each part of the listing (introduction, mesh, spectra, general responses, k`eff`, etc.)

general parser:  
parser to parse the full listing, taking into accout all current response (present in V&V)

Keywords are in most of the cases used as flags and suppressed when data are stored.

A first structure is designed when building the parsers results as lists and dictionaries in the `pyparsing.ParseResults`. Then `parse actions` are used to standard python or `numpy` objects. These `parse actions`, called with `pyparsing.ParserElement.setParseAction`, can be found in `transform`.

### Main parsers blocks

The main parsers blocks are defined at the end of the module, named `mygram` and `response`. The default parser is `mygram`.

Typically, each result block in the listing should start by the `intro` block, parsed by `intro`, and end with at least one `runtime` block, parsed by `runtime`. This parts follows the `scan`: `str` starting by `'RESULTS ARE GIVEN'` and ending with `'simulation time'`, `'exploitation time'` or `'elapsed time'`.

Between these blocks can be found the data blocks. The major ones are:

- one or more responses, driven by the keyword `'RESPONSE FUNCTION'`,
- the editions of IFP adjoint criticality,
- the "default" k`eff` block, in most of the cases at the end of the listing,
- the *contributing particles block*, mainly in first pass listings,
- the perturbation block,
- an optional additional `runtime` block.

Main data blocks are described below (results taken into account, main features).

### Response block, parser `response`

The core of the listings is the list of responses, including all the required scores. This big block is constructed as a `list` of `dict`, each one representing a response (key `'list_responses'` in the final result).

Response are constructed as:

- response introduction containing its definition, parsed by `respintro`:
  - a description of the response parsed by `respdesc` including:
    - `'RESPONSE FUNCTION'` keyword as mandatory (afaik)
    - `'RESPONSE NAME'`, `'SCORE NAME'` and `'ENERGY DECOUPAGE NAME'` that are present in most of the cases
  - more characteristics of the response, parsed by `respcarac`, like:
    - considered particle (`'PARTICULE'` in the listing)
    - nucleus on which the reaction happens (if `'RESPONSE FUNCTION'` is a `'REACTION'`)
    - temperature
    - compostion of the volumes considered
    - concentration
    - reaction considered (usually given as codes)
    - others like DPA type, required arguments, mode, filters, etc.
- responses themselves, using parser `responseblock`, are various:
  - responses including *score* description, all included in the `scoreblock` parser. More than one can be present, they are grouped in the `listscoreblock` parser. `scoreblock` parser contains:
    - score description (parser `scoredesc`) contains the score mode (`'TRACK'`, `'SURF'` or `'COLL'`) and the score zone (currently taken into account: mesh, results cumulated on all geometry or on all sources, Volume, Volume Sum, Frontier, Frontier Sum, Point, Cells and Maille)
    - results block, where at least one of these results can be found, are by parsed by the following parsers:
      - `spectrumblock`: spectrum
      - `meshblock`: mesh
      - `vovspectrumblock`: spectrum with variance of variance
      - `entropy`: entropy results (Boltzmann and Shannon entropies)
      - `medfile`: location of optional MED file
      - `genericscoreblock`: default result integrated over energy
      - `uncertblock`: uncertainty results
      - `uncertintegblock`: uncertainties on integrated results over energy
      - `gbblock`: Green bands results
  - k`eff` presented as a generic response, possibly transformed in `numpy.matrix` (parser `keffblock`)
  - k`ij` results: matrix, eigenvalues, eigenvectors (parser `kijres`)
  - k`ij` sources (parser `kijsources`)
  - Adjoint related results (parser `adjointres`): scores ordered by precursors and families, by perturbation index, by cycle length or sensitivities (this last case is represented in a 3 dimensions `numpy.ndarray`, incident energy, energy ("leaving neutron"), direction cosine (µ)). For the moment this is only for IFP method , in close future also for Wielandt method
  - default result integrated over energy where no scoring mode and zone are precised (parser `defintegratedres`)
  - perturbation results (parser `perturbation`)

### Other parsers

Various other blocks can appear in the Tripoli-4 listing, located at the same level as the response block. These parsers and the associated dictionary key (same level as `'list_responses'`) are:

- `ifpadjointcriticality`: edition of IFP adjoint criticality, key `'ifp_adjoint_crit_edition'`;
- `autokeffblock`: "default" k`eff` block, containing for example the best estimation of k`eff` using variable number of discarded batches, key `'keff_auto'`;
- `contribpartblock`: *contributing particles block*, key `'contributing_particles'`
- `perturbation`: perturbation results, containing a description of the calculation of the perturbation followed by the perturbation result presented like a usual response (spectrum, mesh, etc. depending on required score), key `'perturbation'`
- `runtime`: simulation, exploitation or elapsed time.

Adjoint results: for the moment only IFP is really parsed. Grammar has already more or less adapted to welcome Wielandt method that will have the same kind of outputs (renaming as adjoint_res for example). No key is set for the moment to specify the method, it can be obtained from the response function itself. Adjoint criticality editions are only done for IFP, this may change when the same will be available for Wielandt. Some renaming can also be needed.
