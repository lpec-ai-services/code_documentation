<!-- source: modules/eponine/tripoli4/transform.rst -->

# `transform` – Transform pyparsing result

This module converts `pyparsing` objects in `python` or `numpy` objects.

It is called in the module `grammar` via `pyparsing.ParserElement.setParseAction` functions. It calls the general module `common`.

Note

This module is not standalone, needs a `pyparsing` result in input.

### `valjean.eponine.tripoli4.transform.compose2(f, g)`

Functions composition (2 functions), like fog in mathematics.

params func f  
last function to compose, takes result from g as arguments

params func g  
first function to apply

returns  
composition of the 2 functions (func)

### `valjean.eponine.tripoli4.transform.compose(*fs)`

General composition in case more than 2 functions are needed. For example for fogoh(x) = f(g(h(x))). Takes as many functions as needed as argument.

### `valjean.eponine.tripoli4.transform.convert_spectrum(toks, spectrum_type)`

Convert spectrum to `numpy` object using `common`.

param toks  
spectrum result

type toks  
pyparsing.ParseResults

param str spectrum_type  
type of spectrum that defines the names of the columns

- Default column names: `['score', 'sigma', 'score/lethargy']`

- Other column names taken into account:

  > - vov: adding `'vov'` to previous columns names
  > - uncert: names are `['sigma2(means)', 'mean(sigma_n2)', 'sigma(sigma_n2)', 'fisher test']`
  > - nu and za: no `'score/lethargy'` is available

returns  
dictionary containing spectrum as 7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) for result, `numpy.ndarray` for binnings, discarded batchs, used batchs, integrated result (depending on availability)

`common.convert_spectrum` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_mesh(toks)`

Convert mesh to `numpy` object using `common`.

param toks  
mesh result

type toks  
pyparsing.ParseResults

returns  
dictionary containing meshes (integrated over energy or not) as 7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html), binnings, etc. depending on availability

`common.convert_mesh` and more generally `valjean.eponine.tripoli4.common`

### `valjean.eponine.tripoli4.transform.convert_green_bands(toks)`

Convert Green bands to `numpy` object using `common`.

param toks  
Green bands result

type toks  
pyparsing.ParseResults

returns  
dictionary containing Green bands as 6-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html), `numpy.ndarray` for binnings, etc. depending on availability

`common.convert_green_bands` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_correspondence_table(toks)`

Convert correspondence table to dict (volume id, volume name).

returns  
tuple(tuple)

### `valjean.eponine.tripoli4.transform.convert_scoring_zone_id(toks)`

Convert scoring zone id (volume numbers, cells, points, etc) into native python objects (str, tuple, numpy object).

### `valjean.eponine.tripoli4.transform.convert_list_to_tuple(toks)`

Convert list from pyparsing to tuple.

This function is only used to transform the parseResult in standard python list and send it to convert_list_to_tuple in `common`.

### `valjean.eponine.tripoli4.transform.convert_batch_numbers(score)`

Convert batch numbers (used and discarded) in proper results.

param toks  
score result interpreted as dictionary

type toks  
pyparsing.ParseResults

returns  
dictionary with maximum 2 keys (`'used_batches_res'` and `'discarded_batches_res'`)

rtype  
dict

### `valjean.eponine.tripoli4.transform.convert_score(toks)`

Convert score to `numpy` and python objects. Calls various conversion functions depending on input key (mesh, spectrum, Green bands, default python `dict`, etc.).

param toks  
score result interpreted as dictionary

type toks  
pyparsing.ParseResults

returns  
dictionary using the previous keys and `numpy` objects as values.

### `valjean.eponine.tripoli4.transform.convert_generic_adjoint(toks)`

Convert adjoint output in `numpy` object using `common`.

This method does not take into account sensitivities calculated via the IFP method.

param toks  
Adjoint result (got thanks to IFP or Wielandt method)

type toks  
pyparsing.ParseResults

returns  
list(dict) compatible with `Browser` and `Index`.

`common.convert_generic_adjoint` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_generic_kinetic(toks)`

Convert generic scores for kinetic simulations into a `numpy` object.

param toks  
parsed tokens

type toks  
pyparsing.ParseResults

returns  
list(dict) compatible with `Browser` and `Index`.

`convert_generic_kinetic` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_keff(toks)`

Convert k`eff` response in python dictionary including `numpy.matrix` and using `common`.

param toks  
k`eff` result interpreted as dictionary

type toks  
pyparsing.ParseResults

returns  
dictionary using `numpy` objects including `numpy.matrix`

Note

For the moment, `common.convert_keff_with_matrix` is called. It is possible to call `common.convert_keff` instead.

`common.convert_keff` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_kij_sources(toks)`

Convert k`ij` sources to python dictionary containing `numpy` objects and using `common`.

param toks  
k`ij` source result (interpreted as dictionary)

type toks  
pyparsing.ParseResults

returns  
dictionary where k`ij` values are inside `numpy.ndarray`

`common.convert_kij_sources` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_kij_result(toks)`

Convert k`ij` result to dictionary of `numpy` objects using `common`.

param toks  
k`ij` results (interpreted as dictionary)

type toks  
pyparsing.ParseResults

returns  
dictionary of `numpy.ndarray` and `numpy.matrix`

`common.convert_kij_result` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_kij_keff(toks)`

Convert k`eff` estimated from k`ij` to dictionary of `numpy` objects using `common`.

param toks  
k`eff` block result interpreted as a list t. Only last element is used here (others go to `convert_keff`).

type toks  
pyparsing.ParseResults

returns  
dictionary of `numpy.ndarray` and `numpy.matrix`.

Note

It is possible to add a check on estimator if issue.

`common.convert_kij_keff` and more generally `common`

### `valjean.eponine.tripoli4.transform.convert_parna_keff(pdict)`

Convert Parna likelihood results to python dictionary.

This result is part of the `keff_auto` results.

param pdict  
parna results block to be converted in dictionary (with filter).

returns  
dictionary

### `valjean.eponine.tripoli4.transform.convert_keff_auto(toks)`

Convert auto keff estimation (old or default output, not printed as a usual response) in standard python objects.

Add the `'response_type'` key to the dictionary with `'keff_auto_res'` as associated value (to match browser and data_convertor requirements).

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python list corresponding to input `pyparsing` list

### `valjean.eponine.tripoli4.transform.convert_sensitivities(toks)`

Convert sensitivity results to dictionary of `numpy` objects using `common`.

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python list corresponding to input `pyparsing` list

### `valjean.eponine.tripoli4.transform.convert_shr(toks)`

Convert results on spherical harmonics to dictionary of `numpy.ndarray` using `common`.

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python list corresponding to input `pyparsing` list

### `valjean.eponine.tripoli4.transform.convert_ifp_adj_crit_ed(toks)`

Convert IFP adjoint criticality edition in kinematic array.

### `valjean.eponine.tripoli4.transform.to_final_dict(toks)`

Convert to dictionary result of `pyparsing`.

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python dictionary corresponding to input `pyparsing` dictionary

### `valjean.eponine.tripoli4.transform.lod_to_dot(toks)`

List of dictionaries to dictionary of tuples. This function is dedicated to cases where all the dictionaries (or close) in the list have the same keys.

param list(dict) toks  
list of dictionaries

returns  
dict(tuple)

\>\>\> from pprint import pprint \>\>\> from pyparsing import OneOrMore, Group, Word, nums \>\>\> menu = OneOrMore(Group(Word(nums)('egg') + ',' ... + Word(nums)('bacon') + ',' ... + Word(nums)('spam'))) \>\>\> lod = menu.parseString('1,2,0 2,0,1 0,3,1') \>\>\> dot = lod_to_dot(lod) \>\>\> pprint(dot) \# doctest: +NORMALIZE_WHITESPACE {'bacon': ('2', '0', '3'), 'egg': ('1', '2', '0'), 'spam': ('0', '1', '1')}

\>\>\> lod = \[{'egg': 1, 'bacon': 2, 'spam': 0}, ... {'egg': 2, 'bacon': 0, 'spam': 1}, ... {'egg': 0, 'bacon': 3, 'spam': 1}\] \>\>\> dot = lod_to_dot(lod) \>\>\> pprint(dot) \# doctest: +NORMALIZE_WHITESPACE {'bacon': (2, 0, 3), 'egg': (1, 2, 0), 'spam': (0, 1, 1)}

\>\>\> lod = \[{'egg': 1, 'bacon': 2, 'spam': 0}\] \>\>\> dot = lod_to_dot(lod) \>\>\> pprint(dot) \# doctest: +NORMALIZE_WHITESPACE {'bacon': (2,), 'egg': (1,), 'spam': (0,)}

We always get a tuple as value of the keys, even in case of a single element.

### `valjean.eponine.tripoli4.transform.finalize_response_dict(s, loc, toks)`

Finalize the dictionary of response.

Extract the real response results from pyparsing structure and set it under the `results` key. The previous unique key of the dictionary under the `results` key is stored under the `result_type` key.

The input is the whole response, i.e. the results and the response description. This second part is not "modified" here, only copied in the new dictionary, at the exception of the metadata stored under the `compos_details` key. In that case the dictionary stored under the `compos_details` key is moved to the upper level, i.e. in the response dictionary. As a consequence, the `compos_details` key disappears.

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python dict corresponding to input `pyparsing` response result

### `valjean.eponine.tripoli4.transform.extract_all_metadata(list_of_dicts)`

Extract metadata from nested lists of dictionaries. The metadata to be extracted are here in the second level of list of dictionaries as in the example:

\>\>\> from pprint import pprint \>\>\> lod = \[{'bla': 'X', 'results': \[ ... {'data1_res': 'D1', 'data2_res': 2, 'md1': 'MD1', 'md2': 'MD2'}, ... {'data1_res': 'D3', 'md1': 'MD1', 'md3': 3}\]}\] \>\>\> pprint(extract_all_metadata(lod)) \# doctest: +NORMALIZE_WHITESPACE \[{'bla': 'X', 'md1': 'MD1', 'md2': 'MD2', 'results': {'data1': 'D1', 'data2': 2}}, {'bla': 'X', 'md1': 'MD1', 'md3': 3, 'results': {'data1': 'D3'}}\]

param list(dict) list_of_dicts  
list of dictionaries

returns  
list of dictionaries with no list of dict under 'results' key

rtype  
list(dict)

### `valjean.eponine.tripoli4.transform.extract_metadata(ldict)`

Extract metadata from a list of dictionaries to put it in the surrounding dictionary.

param dict ldict  
dictionary corresponding to a response

rtype  
list(dict)

### `valjean.eponine.tripoli4.transform.index_elements(key)`

Add an item `key` in dictionary corresponding to index in the list containing the dictionary.

param str key  
name of the index

returns  
function that really insert the index in the dict contained in a list

\>\>\> from pprint import pprint \>\>\> lod = \[{'a': 1, 'b': 5}, {'c': -3}, {'d': 4, 'e': 6, 'f': 8}\] \>\>\> func1 = index_elements('index') \>\>\> nlod = func1('', 0, lod) \>\>\> pprint(nlod) \# doctest: +NORMALIZE_WHITESPACE \[{'a': 1, 'b': 5, 'index': 0}, {'c': -3, 'index': 1}, {'d': 4, 'e': 6, 'f': 8, 'index': 2}\]

### `valjean.eponine.tripoli4.transform.propagate_all_metadata(list_of_dicts)`

Concatenate metadata from a list of dictionaries.

It applies `propagate_top_metadata` for all dictionaries in the list of dictionaries, one by one.

The metadata to be propagated are here in the first level of list of dictionaries as in the example:

\>\>\> from pprint import pprint \>\>\> lod = \[{'ext_metadata': {'emd1': 'EMD1', 'emd2': 'EMD2'}, ... 'list_responses': \[ ... {'bla': 'X', 'md1': 'MD1', 'md2': 'MD2', ... 'results': {'data1_res': 'D1', 'data2_res': 2}}, ... {'bla': 'X', 'md1': 'MD1', 'md3': 3, ... 'results': {'data1_res': 'D3'}}\], ... 'omd': 0}\] \>\>\> pprint(propagate_all_metadata(lod)) \# doctest: +NORMALIZE_WHITESPACE \[{'bla': 'X', 'emd1': 'EMD1', 'emd2': 'EMD2', 'md1': 'MD1', 'md2': 'MD2', 'omd': 0, 'results': {'data1_res': 'D1', 'data2_res': 2}}, {'bla': 'X', 'emd1': 'EMD1', 'emd2': 'EMD2', 'md1': 'MD1', 'md3': 3, 'omd': 0, 'results': {'data1_res': 'D3'}}\]

param list(dict) list_of_dicts  
list of dictionaries

returns  
list of dictionaries with common metadata in all responses

rtype  
list(dict)

### `valjean.eponine.tripoli4.transform.propagate_top_metadata(ldict)`

Extract metadata from a list of dictionaries to put them in the surrounding dictionary.

One of the dictionary key has to be `'list_responses'`, i.e. generic scores or arrays built from a list of responses where metadata have already been extracted. This case typically apply to perturbations (not IFP ones).

param dict ldict  
dictionary corresponding to a response

rtype  
list(dict)

### `valjean.eponine.tripoli4.transform.group_to_dict(toks)`

Transform a named group in a dictionary with a single key (removes duplicated levels).

This method also takes into account internal dict that should be part of the main one, like in integrated_res case when units is required and score has no unit.

param toks  
`pyparsing` element

type toks  
pyparsing.ParseResults

returns  
python dict corresponding to input `pyparsing` named group

### `valjean.eponine.tripoli4.transform.fail_spectrum(s, loc, expr, err)`

Parsing error when all bins were at 0 if option '-a' was used while running Tripoli-4.

### `valjean.eponine.tripoli4.transform.fail_parsing(s, loc, expr, err)`

Parsing error with clear message of failing line.
