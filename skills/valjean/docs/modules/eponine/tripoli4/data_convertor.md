<!-- source: modules/eponine/tripoli4/data_convertor.rst -->

# `data_convertor` – Convert Tripoli-4 results to `Dataset`

This module converts Tripoli-4 data from parsing in `Dataset`.

### `valjean.eponine.tripoli4.data_convertor.bins_reduction(def_bins, reduced_dims)`

Reduce number of bins for integrated results (on one or more dimension).

For the reduced dimensions, all the bounds are suppressed except the first and the last one. This is also the case if they represent center of bins. The dimension is supposed to be squeezed afterwards.

param def_bins  
default bins (all of them)

type def_bins  
`collections.OrderedDict` (str, `numpy.ndarray`)

param list(bool)  
dimensions to be reduced or not

returns  
`collections.OrderedDict` (str, `numpy.ndarray`), i.e. adapted bins

\>\>\> ibins = OrderedDict(\[('a', np.array(\[0, 1, 2, 3, 4\])), ... ('b', np.array(\[-10, 0, 10\]))\]) \>\>\> dshape_1 = (5, 3) \>\>\> b11 = bins_reduction(ibins, \[True, True\]) \>\>\> b11\['a'\] array(\[0, 4\]) \>\>\> b11\['b'\] array(\[-10, 10\]) \>\>\> b51 = bins_reduction(ibins, \[False, True\]) \>\>\> b51\['a'\] array(\[0, 1, 2, 3, 4\]) \>\>\> b51\['b'\] array(\[-10, 10\])

### `valjean.eponine.tripoli4.data_convertor.special_array(array, score, bins, array_key='array', name='', what='')`

Convert special arrays in `Dataset`.

These special cases are typically vov results or uncertainty spectrum associated to a perturbation result. No error is associated to the score in that case. Bins are given by the spectrum.

param dict array  
result

param str score  
key of the score to get

param collections.OrderedDict bins  
bins correspondig to required array

param str array_key  
default=`'array'` but it can be an integrated array for example, should be a key inside `farray_res`

param str name  
name of dataset

param str what  
what attribute of dataset

rtype  
Dataset

### `valjean.eponine.tripoli4.data_convertor.array_result(farray_res, res_type, name='', what='', array_key='array', score='score')`

Conversion of arrays in `Dataset`.

param dict farray_res  
results dictionary containing `res_type` key

param str res_type  
result type, like `'spectrum'`, `'mesh'`

param str array_key  
default=`'array'` but it can be an integrated array for example, should be a key inside `farray_res`

param str name  
name of dataset

param str what  
what attribute of dataset

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.masked_array_result(farray_res, res_type, name='', what='', array_key='array', score='score')`

Mask invalid (`np.nan` and `np.inf`) values.

### `valjean.eponine.tripoli4.data_convertor.integrated_result(result, res_type='integrated', name='', what='', score='score', sigma='sigma')`

Conversion of generic score (or energy integrated result) in `Dataset`.

Bins are squeezed according to the integrated dimension obtained from another array stored in the same result. Default full arrays are `'spectrum'` and `'mesh'`. A case is also foreseen for uncertainty results (in perturbation cases).

param dict result  
results dictionary containing `res_type` key

param str res_type  
should be 'integrated'

param str name  
name of dataset

param str what  
what attribute of dataset

param str score  
score key in results array like `'score'` or `'score/lethargy'`

param str sigma  
sigma key in results array, usually `'sigma'`

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.results_wo_error(result, res_type, name='', what='', score=None)`

Conversion of results without error, allowing multiple scores in the same container.

dict result  
results dictionary containing `res_type` key

param str res_type  
key in result allowing access to the desired quantity

param str name  
name of dataset

param str what  
what attribute of dataset

param str score  
score key in results array like `'score'`

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.result_wo_error(result, res_type, name='', what='')`

Conversion of a result without error.

The result can be of any dimension (matrix, vector, scalar) or any type (float, int, complex).

dict result  
results dictionary containing `res_type` key

param str res_type  
key in result allowing access to the desired quantity

param str name  
name of dataset

param str what  
what attribute of dataset

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.result_with_error(result, res_type, name='', what='', score='score', sigma='sigma')`

Conversion of generic score (or energy integrated result) in `Dataset`.

param dict result  
results dictionary containing `res_type` key

param str res_type  
should be 'generic'

param str name  
name of dataset

param str what  
what attribute of dataset

param str score  
score key in results array like `'score'` or `'score/lethargy'`

param str sigma  
sigma key in results array, usually `'sigma'`

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.unbinned_result(result, res_type, name='', what='', score=None, sigma=None)`

Conversion of all unbinned results in `Dataset`.

dict result  
results dictionary containing `res_type` key

param str res_type  
key in result allowing access to the desired quantity

param str name  
name of dataset

param str what  
what attribute of dataset

param str score  
score key in results array like `'score'` or `'score/lethargy'`

param str sigma  
sigma key in results array, usually `'sigma'`

returns  
`Dataset`

### `valjean.eponine.tripoli4.data_convertor.nan_result(name='', what='')`

Returns a NaN `Dataset` (value and error).

This `Dataset` can be returned for example in case of non converged results or when no dataset can be built.

Values are scalar per default, not arrays.

param str name  
name of dataset

param str what  
what attribute of dataset

rtype  
`Dataset`

returns  
dataset containing NaN as value and error

### `valjean.eponine.tripoli4.data_convertor.convert_data(data, data_type, name='', what='', **kwargs)`

Test for data conversion using dict or default.

An exception for integrated is for the moment needed as they can come from spectrum res or generic scores but are treated a bit differently. To be homogenized.

param dict data  
results dictionary containing `data_type` key

param str data_type  
data key

param kwargs  
keyword arguements if needed

returns  
`Dataset`
