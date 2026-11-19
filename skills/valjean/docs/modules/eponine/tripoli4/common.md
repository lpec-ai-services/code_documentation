<!-- source: modules/eponine/tripoli4/common.rst -->

# `common` – Common methods to build numpy arrays from dictionaries and lists

This module provides generic functions to convert parsing outputs to `NumPy` objects.

Inputs (outputs from parsers) should be python lists or dictionary, dictionary keys should be the same in all parsers...

Not a standalone code, needs inputs.  
To be tested in a more general context.

## Goal

Parsing results are normally stored as lists and dictionaries but it could be easier to use other objects, as `NumPy` arrays. In our context these objects are used to represent

- spectrum results, i.e. tables splitted at least in energy, sometimes with additional splittings in time, µ and φ direction angles
- mesh results, i.e. tables splitted in space (cartesian, cylindrical, spherical depending on case), sometimes with additional splittings in energy and/or time
- Green bands results
- IFP results
- k`eff` results
- k`ij` results (matrices, eigenvectors and eigenvalues)

`NumPy` objects are useful for future calculations or plotting for example.

## Spectrum and meshes

### Generalities

Spectrum and meshes results use a common representation build using `DictBuilder`. This common representation is a **7-dimension structured array** from `NumPy`, see [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html).

Kinematic dimensions are:

u, v, w  
space coordinates (typically (x, y, z), (r, θ, z) or (r, θ, φ), depending on frame reference)

e  
energy

t  
time

mu, phi  
direction angles µ and φ whose definitions can vary depending on the reference frame of direction[^1].

Order should always be that one.

The result for each bin `(u, v, w, e, t, mu, phi)` is filled in a [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) whose `numpy.dtype` can be:

meshes  
normally `'score'` and `'sigma'` where *sigma* is in % and *score* in its unit (not necessarly precised in the listing)

default spectrum  
`'score'`, `'sigma'`, `'score/lethargy'` where *sigma* is in %, *score* and *score/lethargy* in the unit of the score (not necessarly precised in the listing)

spectrum with variance of variance (vov)  
as default spectrum case + a fourth element named `'vov'` (no unit)

uncertainties spectrum  
in case of *covariance perturbations*, elements are `'sigma2(means)'`, `'mean(sigma_n2)'`, `'sigma(sigma_n2)'` and `'fisher test'`[^2]

Spectrum and mesh results don't only consist in arrays: binning (except in space) and number of dicarded batchs are also available for example. Other optional can also be added, like integrated result on one or more dimensions. The final result of spectrum and mesh is returned as a dictionary detailed in `result_spectrum` and `result_mesh`.

### Initialization

`DictBuilder` cannot be instantiated as it has abstract methods (pure virtual): `fill_arrays_and_bins` and `add_last_bins`. It is mother class of `MeshDictBuilder` for mesh and `SpectrumDictBuilder` for spectrum.

Initialization is done giving names of the columns (`'score'` and `'sigma'` for mesh for example) and the list of number of bins. The length of this list should be 7 as we have 7 dimensison.

> \>\>\> from valjean.eponine.tripoli4.common import (DictBuilder, ... MeshDictBuilder, SpectrumDictBuilder) \>\>\> db = DictBuilder(\['score', 'sigma'\], \[1,2,3,4,5,6,7\]) Traceback (most recent call last): \[...\] TypeError: Can't instantiate abstract class DictBuilder ... \>\>\> mdb = MeshDictBuilder(\['score', 'sigma'\], \[1,2,3,4,5,6,7\]) \>\>\> mdb = MeshDictBuilder(\['result', 'sigma'\], \[1,2,3,4,5,6,7\]) \>\>\> sdb = SpectrumDictBuilder(\['score', 'sigma', 'score/lethargy'\], ... \[1,2,3,4,5,6,7\])

Errors are raised if the dimension is not correct.

> \>\>\> mdb = MeshDictBuilder(\['score', 'sigma'\], \[1,2,3,4,5,6\]) Traceback (most recent call last): ... AssertionError

Number of bins should be 7 (3 space dimensions, 1 energy, 1 time, 2 direction angles).

These methods initializes both the 7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) and the arrays of bins, first stored as list for simplicity. Arrays of bins are in reality array of the edges of bins, starting by the lower one to the higher one after flipping if needed.

### Filling arrays and bins

Mesh and spectrum are read from the output listing and first stored as list and dictionary following listing structure. Building `numpy.ndarray` for arrays and bins simplifies post-processing. It calls `fill_arrays_and_bins`.

To fill arrays and bins needed objects are outputs from the chosen parser. Some dictionary keys may be needed:

mesh:  
data is a list of all meshes available. Each mesh is a dictionary that can have the following keys:

`'meshes'`  
list of dictionary containing the mesh results (mandatory), dictionaries with keys:

- `{'mesh_energyrange': [], 'mesh_vals': [[], ]}` to get mesh per energy range (mandatory)
- `{'mesh_energyintegrated':, 'mesh_vals': [[], ]}` if result is also available on the full range of energy but still splitted in space (facultative)

A mesh line in the list under `'mesh_vals'` key is constructed as a list of `[[u, v, w], score, sigma]`. In `'mesh_energyrange'`, energy range is given as `['unit', e1, e2]`.

`'time_step'`  
if a time splitting is available Remark: for the moment, no splitting in µ or φ are available.

`'integrated result'`  
if `'time_step'` exists, integrated result can be available, meaning integrated over space and energy (not time)

spectrum:  
data is a list of dictionaries containing spectrum results.

Possible keys are:

`'spectrum_vals'`  
spectrum values, given in a list `[e1, e2, score, sigma, score/lethargy]` (mandatory)

`'time_step'`  
if result splitted in time

`'mu_angle_zone'`  
if result splitted in µ angle

`'phi_angle_zone'`  
if result splitted in φ angle

`'integrated_res'`  
if `'time_step'` exits, integrated result can also be given in time steps, so integrated over energy.

When arrays are filled, bins are also filled on their first appearance. At the end of the filling special care needs to be taken to bins. Indeed, as usual there are Nbins+1 edges. The last edge may be the lowest one or the highest one, depending on the order required in the job. So it will inserted in first position or appended to the end.

If bins are in decreasing order in one dimension (energy, time, µ or φ), arrays will be flipped in that direction. This step as to be done on all arrays stored and on the bins array to stay consistant.

If time, µ or φ grids are given, they will always appear in the same order: t -\> µ -\> φ. µ and φ can exist without time; time can exist alone, like µ; φ cannot exist without µ[^3]. If more than one is present, the first one is not repeated at each step, so needs to be propagated to the next steps (instance variables `itime`, `imu` and `iphi`).

### Result and use in the framework

In the framework, `MeshDictBuilder` and `SpectrumDictBuilder` are called in `convert_mesh` and `convert_spectrum`, themselves from transformation modules (transforming parsing result in `NumPy`/`python` containers. Theses methods then returns dictionaries containing the `numpy.ndarray` and other results.

mesh:  
Default keys are:

`'array'`  
7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with `numpy.dtype` `('score', 'sigma')`

`'bins'`  
`collections.OrderedDict` (str, `numpy.ndarray`), order corresponds to the order of the shape in the array. Space are normally at center of the bin, while E, t, μ and φ are given as edges. If no binning is available an empty array is present.

`'units'`  
available limits (default set, including score and sigma)

Other keys can be available:

`'eintegrated_array'`  
7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with dtype `('score', 'sigma')` and list of number of bins (`lnbins`) is `[n_u, n_v, n_w, 1, n_t, 1, 1]`

`'integrated'`  
7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with dtype `('score', 'sigma')` and list of number of bins (`lnbins`) is `[1, 1, 1, 1, n_t, 1, 1]`

`'used_batch'`  
if `'integrated_res'` exists, number of used batch is also given

spectrum:  
Default keys are:

`'spectrum'`  
7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with `numpy.dtype` `('score', 'sigma', 'score/lethargy')` if this is a default spectrum, `numpy.dtype` will change in some cases (vov, uncertainties), see `eponine-spectrummesh-intro`

`'bins'`  
`collections.OrderedDict` (str, `numpy.ndarray`), order corresponds to the order of the shape in the array. In spectrum no space bins are given (corresponding to empty arrays), other dimensions are normally given as edges when available, else as an empty array.

`'discarded_batches'`  
number of discarded batchs

Optional keys are:

`'integrated'`  
7-dimensions [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with same `numpy.dtype` as `'array'` and list of number of bins (`lnbins`) is `[1, 1, 1, 1, n_t, 1, 1]` (integrated over energy)

`'used_batch'`  
if `'integrated_res'` exists, number of used batch is also given

## Other available arrays

### Green bands

Green bands are stored in `numpy.ndarray` that look like the spectrum or mesh ones but with different bins and dtypes, these are 6-dimensions arrays.

The 6 dimensions are given, in order, by:

se  
`'step'` in input, bin of the energy of source (source are treated in energy steps)

ns  
`'source'` in input, number of the source

u, v, w  
coordinates of the source, `(0, 0, 0)` if not given

e  
energy of the output neutron

The result for each bin (se, ns, u, v, w, e) is filled in a [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) whose `numpy.dtype` is the default spectrum one, `('score', 'sigma', 'score/lethargy')`.

Bins are also stored for all the dimensions in same order as in the array. Empty array corresponds to unused dimensions. Like in spectrum, last bins of energy (source and followed particle) are added after the main loop.

The returned dictionary contains:

`'array'`  
6-dimension [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html)

`'bins'`  
`collections.OrderedDict` (str, `numpy.ndarray`) of bins in same order as array shape

`'units'`  
dict of units

### Adjoint results

Results obtained from the calculation of the adjoint can beassociated to array like spectra or meshes or to more generic scores. Dimensions are usually a bit different. The output from Tripoli-4 is also different and has to be treated separately.

Different knid of arrays are available, depending on the type of calculation:

Generic adjoint result:  
corresponds generic scores calculated by IFP or Wielandt methods. They are returned as standard dictionary containing usual integrated results (pair score, sigma), so no array. 'Dimensions' correspond to the dictionary keys (like nucleus, family, length, etc.).

Adjoint criticality results from specific edition:  
only calculated with the IFP method. Two kind of results are for the moment available: multi-dimensions arrays, close to meshes and arrays in (volume, energy) where volume corresponds to the geometrical id of the volume. The available dimension for the multi-dimensions arrays are: X, Y, Z (only cartesian in space), φ and θ in direction, energy. No time is considered. These spectra inherit from `KinematicDictBuilder` but have a different order of bins compared to spectra and meshes and time is automatically set to 1 bin (integrated).

More details and code are available in `convert_generic_adjoint`, `AdjointCritEdDictBuilder` and `VolAdjCritEdDictBuilder`.

### Nu and (Z,A) spectrum

Spectra indexed by the number of neutrons produced in fission (Nu) and indexed by the (Z,A) of the produced fission products (isotopes) as also available as spectra.

The results are given as standard array results: a dictionary with the usual keys (`'array'`, `'bins'`, `'units'`).

More details in `convert_nu_spectrum` and `convert_za_spectrum`.

### Scores on spherical harmonics

These scores are foreseen to be passed to deterministic codes. They are calculated on real spherical harmonics, using the Schmid semi-normalized harmonics as described in \[[SHTools](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018GC007529)\] to be consistent with Apollo3. Thus the associated functions are not only Legendre polynomials but also contains a factor $cos(m\phi)$ for $m>0$ and a factor $sin(|m|\phi)$ for $m<0$.

In practice, they are discretized on a space mesh ($(u, v, w)$ coordinates), on incident energy bins ($ie$), on energy bins ($e$) and on the order of the moments ($(l, m)$). $l$ moments go from 0 to $L$ (so there are $L+1$ values), $m$ ones go from $-l$ to $l$, ($2L+1$ values).

The eight scores available in such description are converted in a single array of 7 dimensions $(u, v, w, ie, e, l, m)$<span class="title-ref">. The forbidden :math:</span><span class="title-ref">(l, m)</span> pairs ($m>|l|$) are set to `numpy.nan`. A `mask` is applied to the resulting Dataset.

Note that $m$ ids goes from 0 to 2L+1 in slicing, corresponding to bins values $-m$ to $m$.

All the arrays have 7 dimensions, but incident energy bins are only relevant for the scattering matrix. The fission spectrum only allows $l=0, m=0$.

## k`eff` results

Only k`eff` as generic response are converted in *NumPy* objects; historical k`eff` block is stored in a dictionary (see `valjean.eponine.tripoli4.grammar`).

In the generic response case, results (value, σ) are available for 3 estimators: KSTEP, KCOLL and KTRACK. Their correlation coefficients, combined values, combined σ (in %) and the full combination result are also given. This means that results given are in reality a matrix. One choice in order to store k`eff` results is to use `numpy.ndarray` seen as matrix (`convert_keff_with_matrix`), the other one uses more standard arrays (`convert_keff`).

### Conversion to matrices

The 3 estimators are always considered in the listing order KSTEP, KCOLL, KTRACK, so KSTEP = 0, KCOLL = 1 and KTRACK = 2.

Three arrays are filled:

`'keff_matrix'`  
symmetric matrix 3×3, with k`eff` result for each estimator on diagonal and combined values off-diagonal (for 2 estimators)

`'correlation_matrix'`  
symmetric matrix 3×3, with 1 on diagonal and correlation cofficient off-diagonal (for 2 estimators)

`'sigma_matrix'`  
symmetric matrix 3×3 with σ in % for each estimator on diagonal and combined σ in % off-diagonal (for 2 estimators)

In summary:

- for k`eff` and σ matrices (replace k`eff` by σ in 2`d` case, cb stands for combined):

  |        |                           |                           |                           |
  |--------|---------------------------|---------------------------|---------------------------|
  |        | KSTEP                     | KCOLL                     | KTRACK                    |
  | KSTEP  | k`eff` (KSTEP)            | cb k`eff` (KSTEP, KCOLL)  | cb k`eff` (KSTEP, KTRACK) |
  | KCOLL  | cb k`eff` (KSTEP, KCOLL)  | k`eff` (KCOLL)            | cb k`eff` (KCOLL, KTRACK) |
  | KTRACK | cb k`eff` (KSTEP, KTRACK) | cb k`eff` (KCOLL, KTRACK) | k`eff` (KTRACK)           |

- the correlation matrix:

  |        |                     |                     |                     |
  |--------|---------------------|---------------------|---------------------|
  |        | KSTEP               | KCOLL               | KTRACK              |
  | KSTEP  | 1                   | corr(KSTEP, KCOLL)  | corr(KSTEP, KTRACK) |
  | KCOLL  | corr(KSTEP, KCOLL)  | 1                   | corr(KCOLL, KTRACK) |
  | KTRACK | corr(KSTEP, KTRACK) | corr(KCOLL, KTRACK) | 1                   |

Values are set to `numpy.nan` if not converged (string `"Not converged"` appearing in the listing).

These arrays can be easily converted to matrices if matrix methods are needed but array is easier to initialized and more general.

The method `convert_keff_with_matrix` takes as input the generic k`eff` response as a dictionary and returns a dictinary containing different keys:

- the number of batchs used under `'used_batches'`;
- the 3 matrices mentioned above (`'keff_matrix'`, `'correlation_matrix'` and `'sigma_matrix'`) and the list of estimators (`['KSTEP', 'KCOLL', 'KTRACK']` by default) are stored under the common key `'keff_per_estimator'` as a dictionary;
- the full combination result (k`eff` and σ in %) under `'keff_combination'` key

Not converged cases are taken into account and return a key `'not_converged'`.

### Conversion to standard arrays

The conversion closer to the output listing is done in `convert_keff`. A dictionary is built with the following elements:

`'used_batch'`  
number of batchs used

`'full_comb_estimation'`  
full combination result (k`eff` and σ in %), like in `eponine-keff-matrix`

`'res_per_estimator'`  
dictionary with estimator as key and [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) with `dtype = ('keff', 'sigma')` as value

`'correlation_matrix'`  
dictionary with tuple as key and [numpy structured array](https://numpy.org/doc/stable/user/basics.rec.html) as value, `('estimator1', 'estimator2'): numpy.array('correlations', 'combined values', 'combined sigma%')`

In correlation matrix diagoanl is set to 1 and not converged values (str) are set to `numpy.nan`. If the full combination did not converged the string is kept.

## k`ij` results

k`ij` matrix gives the number of neutrons produced by fission in the volume i from a neutron emited in the volume j. Its highest eigenvalue is equal to the k`eff` of the system. The corresponding eigenvector represents the neutrons sources in the volumes (necessarly containing fissile metrial). For more details, see user guide.

Different k`ij` results can be available:

- list of k`ij` sources in `convert_kij_sources`
- k`ij` matrix and associated results in `convert_kij_result`
- k`ij` estimation in historical k`eff` block (k`ij` is an additional estimator in that case) in `convert_kij_keff`

### k`ij` sources

In that case the input dictionary is returned with a conversion of the `'kij_sources_vals'` as a `numpy.ndarray`. Its length corresponds to the number of volumes.

### k`ij` matrix (result)

The k`ij` matrix results block contains various results including k`ij` eigenvalues, k`ij` eigenvectors and k`ij` matrix that will be converted in `numpy.ndarray` or `numpy.matrix`. The size of the arrays depends on the number of volumes containing fissle material, N.

The returned object is a dictionary containing the following keys and objects:

`'used_batches'`  
number of batchs used (`int`)

`'kij_mkeff'`  
result of k`ij`-k`eff` (`float`), where k`ij` is the hightest eigenvalue of k`ij`

`'kij_domratio'`  
dominant ratio (`float`), ratio between the hightest k`ij` eigenvalue and the next one

`'kij_reigenval'`  
`numpy.ndarray` of N **complex** numbers (real and imaginary parts given in the listings) corresponding to the **right** eigenvalues.

`'kij_reigenvec'`  
`numpy.ndarray` of N vectors of N elements corresponding to **right** eigenvectors.

`'kij_matrix'`  
`numpy.matrix` of N×N being the k`ij` matrix.

### k`ij` in k`eff` block

k`ij` results are also present in the "historical" k`eff` block, as an additional estimator. Results are presented in a different way and are different... Typical results are k`ij` - k`eff`, the eigenvector corresponding to the best estimation, k`ij` matrix, standard deviation matrix and sensibility matrix.

The returned object is a dictionary with the following keys (faculative can be specified):

`'keff_estimator'`  
name of the estimator (`str`), `'KIJ'` here

`'results'`  
usual results block, built here for once containing the following dictionary (same keys as in the previous case when possible):

`'used_batches'`  
number of batchs used to calculate the k`ij` (`int`)

`'kij_mkeff'`  
result of k`ij`-k`eff` (`float`)

`'space_bins'`  
**facultative**, list of N volumes/mesh elements considered (`numpy.ndarray` of

- `int` for volumes,
- `tuple` of `int` (u, v, w) for mesh elements,

`'kij_leigenvec'`  
eigenvector corresponding dominant **left** eigenvector (`numpy.ndarray` of N elements)

`'kij_matrix'`  
k`ij` matrix (N×N `numpy.matrix`)

`'kij_stddev_matrix'`  
standard deviation matrix (N×N `numpy.matrix`)

`'kij_sensibility_matrix'`  
sensibility matrix (N×N `numpy.matrix`)

**Footnotes**

## Module API

### `class valjean.eponine.tripoli4.common.DictBuilder(colnames, lnbins)  — bases: ABC`

General class to build dictionaries.

This class implements a pattern for array results storage as dictionaries. It transforms the Tripoli-4 array strings in numpy arrays of a given number of dimensions, depending on the kind of array (spectrum, mesh, IFP result, etc.). General methods are implemented, mandatory methods are implemented as abstract and need to be derived in daughter classes.

#### `DictBuilder.add_array(self, name, colnames, lnbins)`

Add a new array to dictionary arrays with key name.

param str name  
name of the new array (integrated_res, etc.)

type name  
str

param colnames  
list of the columns names (score, sigma, etc.)

type colnames  
tuple(str)

param lnbins  
number of bins in each dimension

type lnbins  
list(int)

#### `DictBuilder.add_last_bins(self, data)`

Add last bins based on keywords presence in data.

param list data  
mesh or spectrum results

#### `DictBuilder.convert_bins_to_increasing_arrays(self)`

Flip bins if given in decreasing order in the output listing.

Depending on the required grid (GRID or DECOUPAGE) energies, times, mu and phi can be given from upper edge to lower edge. This is not convenient for post-traitements, especially plots. They have to be flipped at a moment, here or later, easiest is here, and all results will look the same :-).

This function calls an internal function and needs to match the dimension with the number of the axis: ('e' → 3, 't' → 4, 'mu' → 5, 'phi' → 6)

#### `DictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spectrum or mesh data.

param list data  
mesh or spectrum results

### `class valjean.eponine.tripoli4.common.KinematicDictBuilder(colnames, lnbins)  — bases: DictBuilder`

Class to build the dictionary for spectrum and mesh results as 7-dimensions structured arrays. 7-dimensions are: space (3, written `'u', 'v', 'w'`), energy (`'e'`), time (`'t'`), mu (`mu'`) and phi (`'phi'`) (direction angles).

This class has 2 abstract methods, `_add_last_energy_bin` and `fill_arrays_and_bins`, so it cannot be initialized directly.

KinematicDictBuilder.VAR_FLAG

`{'t': 'time_step', 'mu': 'mu_angle_zone', 'phi': 'phi_angle_zone'}`: correspondance dictionary between internal name of dimensions and names in listings

#### `KinematicDictBuilder.add_last_bins(self, data)`

Add last bins in energy, time, mu and phi direction angles. Based on keywords presence in data.

param list data  
mesh or spectrum results

#### `KinematicDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spectrum or mesh data.

param list data  
mesh or spectrum results

### `class valjean.eponine.tripoli4.common.MeshDictBuilderException  — bases: Exception`

Exception to mesh builder

### `class valjean.eponine.tripoli4.common.MeshDictBuilder(colnames, lnbins)  — bases: KinematicDictBuilder`

Class specific to mesh dictionary -\> mainly filling of bins and arrays.

This class inherites from KinematicDictBuilder, see `KinematicDictBuilder` for initialization and common methods.

#### `MeshDictBuilder.from_data(cls, data)`

Initialize MeshDictBuilder from data.

#### `MeshDictBuilder.fill_space_bins(self, nb_tokens, vals)`

Fill the mesh space bins.

Two different cases are possible:

- the default one, where only the cell indices are given: the space bins are set to all possible cell index in the 3 dimensions. For example: if there are 3 cells in `u`, the bins will be 0, 1, 2. Only center of bins are given here (no possibility of calculation of a width). In that case the mesh contains 3 tokens: a comma-separated list of cell indices (without intervening whitespace), the value and the sigma.
- a standard MESH was required with the option `MESH_INFO` in Tripoli-4: center of cells are given on the 3 dimensions, the space bins will be set to these values if the mesh is Cartesian and its axes coincide with the coordinate axes. In MESH_INFO case the mesh line contains 6 or 7 tokens, depending on Tripoli-4 version: the comma-separated list of cell indices (as above), the three space coordinates of the midpoint of the cell, \[the cell volume\], the value and the sigma. When the cell coordinates are not aligned on the axes, the bins stay the cell indices and the coordinates stay available.

param int nb_tokens  
number of tokens by line of mesh result

param list vals  
mesh results

#### `MeshDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for mesh data.

param list data  
mesh results

Different arrays can be filled. Current possibilities are:

- `'default'` (mandatory)
- `'eintegrated_mesh'` (facultative, integrated over energy, still splitted in space)
- `'integrated_res'` (over energy and space, splitted in time)

#### `MeshDictBuilder.fill_score_units(self, data)`

Fill score units if available in data, else leave to unknown.

#### `MeshDictBuilder.fill(self, nb_elts, data)`

Fill data in mesh.

### `class valjean.eponine.tripoli4.common.SpectrumDictBuilderException  — bases: Exception`

Exception to spectrum builder (bad bins)

### `class valjean.eponine.tripoli4.common.SpectrumDictBuilder(colnames, lnbins)  — bases: KinematicDictBuilder`

Class specific to spectrum dictionary -\> mainly filling of bins and arrays.

This class inherites from KinematicDictBuilder, see `KinematicDictBuilder` for initialization and common methods.

#### `SpectrumDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spectrum data.

param list data  
spectrum results

Current arrays possibly filled are:

- `'default'` (mandatory)
- `'integrated_res'` (over energy, splitted in time for the moment)

#### `SpectrumDictBuilder.fill_score_units(self, data)`

Fill score units if available in data, else leave to unknown.

### `valjean.eponine.tripoli4.common.convert_spectrum(spectrum, colnames=('score', 'sigma', 'score/lethargy'))`

Convert spectrum results in 7D NumPy structured array.

param list spectrum  
list of spectra. Accepts time and (direction) angular grids.

param list(str) colnames  
list of the names of the columns. Default = `['score', 'sigma', 'score/lethargy']`

returns  
dictionary with keys and elements

> - `'array'`: 7 dimensions NumPy structured array with related binnings as NumPy arrays `v[u, v, w, E, t, mu, phi] = ('score', 'sigma', 'score/lethargy')`
> - `'bins'`: `collections.OrderedDict` of the available bins
> - `'units'`: dict containing units of dimensions (bins), score and sigma
> - `'eintegrated_array'`: 7 dimensions NumPy structured array `v[u, v, w, E, t, mu, phi] = ('score', 'sigma')`; facultative, seen when time required alone and sometimes when neither time nor mu nor phi are required

### `valjean.eponine.tripoli4.common.get_energy_bins(meshes)`

Get the number of energy bins for mesh.

param list meshes  
mesh, list of dictionaries, at least one should have the key `'mesh_energyrange'`

### `valjean.eponine.tripoli4.common.convert_mesh(meshres)`

Convert mesh in 7-dimensions NumPy array.

param list meshres  
Mesh result constructed as: `[{'time_step': [], 'meshes': [], 'integrated_res': {}}, {}]`, see `eponine-spectrummesh-fill` for more details.

returns  
python dictonary with keys

> - `'array'`: NumPy structured array of dimension 7 `v[u, v ,w, E, t, mu, phi] = ('score', 'sigma')`
> - `'bins'`: `collections.OrderedDict` of the available bins
> - `'units'`: dict containing units of dimensions (bins), score and sigma
> - `'eintegrated_array'`: 7-dimensions NumPy structured array `v[u,v,w,E,t,mu,phi] = ('score', 'sigma')` corresponding to mesh integrated on energy (facultative)
> - `'integrated'`: 7 dimensions NumPy structured array `v[u,v,w,E,t,mu,phi] = (score, sigma)` corresponding to mesh integrated over energy and space; *facultative*, available when time grid is required (so corresponds to integrated results splitted in time)
> - `'used_batches'`: number of used batchs (only if integrated result)

### `class valjean.eponine.tripoli4.common.NuSpectrumDictBuilder(colnames, lnbins)  — bases: DictBuilder`

Class specific to spectrum dictionary -\> mainly filling of bins and arrays.

This class inherites from DictBuilder, see `DictBuilder` for initialization and common methods.

#### `NuSpectrumDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spectrum data.

param list data  
spectrum results

Current arrays possibly filled are:

- `'default'` (mandatory)
- `'integrated_res'` (over nu)

#### `NuSpectrumDictBuilder.add_last_bins(self, data)`

Add last bin in nu from spectrum.

param list data  
spectrum results

#### `NuSpectrumDictBuilder.fill_score_units(self, data)`

Fill score units if available in data, else leave to unknown.

### `valjean.eponine.tripoli4.common.convert_nu_spectrum(spectrum, colnames=('score', 'sigma'))`

Convert nu spectrum results in 1D NumPy structured array.

param list spectrum  
list of spectra. Accepts time and (direction) angular grids.

param list(str) colnames  
list of the names of the columns. Default = `['score', 'sigma']`

returns  
dictionary with keys and elements

> - `'array'`: 1 dimension NumPy structured array with related binnings as NumPy arrays `v[nu] = ('score', 'sigma')`
> - `'bins'`: `collections.OrderedDict`, nu binning
> - `'units'`: dict containing units of dimensions (bins), score and sigma
> - `'integrated_array'`: 1 dimension NumPy structured array `v[nu] = ('score', 'sigma')`

### `class valjean.eponine.tripoli4.common.ZASpectrumDictBuilder(colnames, bins)  — bases: DictBuilder`

Class specific to spectrum dictionary to parse arrays indexed by Z and A numbers (isotopes).

This class inherites from DictBuilder, see `DictBuilder` for initialization and common methods.

#### `ZASpectrumDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spectrum data.

param list data  
spectrum results

Current arrays possibly filled are:

- `'default'` (mandatory)
- `'integrated_res'` (over Z and A, i.e. all isotopes)

#### `ZASpectrumDictBuilder.add_last_bins(self, data)`

Add last bin in Z,A from spectrum, not applicable in this case.

param list data  
spectrum results

#### `ZASpectrumDictBuilder.fill_score_units(self, data)`

Fill score units if available in data, else leave to unknown.

### `valjean.eponine.tripoli4.common.convert_za_spectrum(spectrum, colnames=('score', 'sigma'))`

Convert nu spectrum results in 1D NumPy structured array.

param list spectrum  
list of spectra. Accepts time and (direction) angular grids.

param list(str) colnames  
list of the names of the columns. Default = `['score', 'sigma']`

returns  
dictionary with keys and elements

> - `'array'`: 1 dimension NumPy structured array with related binnings as NumPy arrays `v[Z, A] = ('score', 'sigma')`
> - `'bins'`: `collections.OrderedDict`, Z and A binnings
> - `'units'`: dict containing units of dimensions (bins), score and sigma
> - `'integrated_array'`: 1 dimension NumPy structured array `v[Z, A] = ('score', 'sigma')`

Remark: no call to add_last_bins or convert_bins_to_increasing_arrays is done here as no energy, time or space bins are given for the moment.

### `valjean.eponine.tripoli4.common.convert_keff_with_matrix(res)`

Convert k`eff` results in NumPy matrices.

param dict res  
k`eff` results

returns  
dict filled as:

<!-- -->

    {'used_batches': int,
     'keff_per_estimator': {'estimators': [str],
                            'keff_matrix': numpy.array,
                            'correlation_matrix': numpy.array,
                            'sigma_matrix': numpy.array},
     'keff_combination': numpy.array}

### `valjean.eponine.tripoli4.common.convert_keff(res)`

Convert k`eff` results in dictionary containing NumPy objects.

param dict res  
keff results

returns  
dict containing

<!-- -->

    {'used_batches': int, 'estimators': [str, ],
     'full_comb_estimation': numpy.array,
     'res_per_estimator': {'estimator': numpy.array, },
     'correlation_matrix': {('estimator1', 'estimator2'): numpy.array, }}

See `eponine-keff-stdarrays` for more details.

### `class valjean.eponine.tripoli4.common.GreenBandsDictBuilder(colnames, lnbins)  — bases: DictBuilder`

Class to build Green bands spectrum results.

#### `GreenBandsDictBuilder.add_last_bins(self, data)`

Add last bins from source energy bins and energy bins. Also remove duplicates in source number and source tabulations.

param data  
Green bands results

#### `GreenBandsDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins from Green bands result.

param data  
Green bands results

### `valjean.eponine.tripoli4.common.convert_green_bands(gbs)`

Convert Green bands contribution results in arrays, using same schema as spectrum or mesh.

param gbs  
Green bands results

returns  
dict

### `valjean.eponine.tripoli4.common.convert_generic_adjoint(res)`

Convert adjoint results in association of dictionaries and NumPy array.

param list res  
Adjoint result got thanks to IFP or Wielandt method to be converted

returns  
list(dict) each dictionary containing

> - metadata like nucleus name, family number or cycle length
> - data saved as `'integrated_res'`

Units, if available, and used batch are also saved under the integrated result.

This structure is compatible with the browser and the index. Selections are done like in the default score cases.

### `valjean.eponine.tripoli4.common.convert_generic_kinetic(res)`

Convert kinetic results into association of dictionaries and NumPy array.

param list res  
parsed tokens

returns  
list(dict) each dictionary containing

> - metadata like nucleus name, family number or cycle length
> - data saved as `'integrated_res'`

Units, if available, and used batch are also saved under the integrated result.

This structure is compatible with the browser and the index. Selections are done like in the default score cases.

### `class valjean.eponine.tripoli4.common.AdjointCritEdDictBuilderException  — bases: Exception`

Exception to adjoint criticality edition array builder (bad bins)

### `class valjean.eponine.tripoli4.common.AdjointCritEdDictBuilder(colnames, bins)  — bases: KinematicDictBuilder`

Specific class to build IFP adjoint criticality edition results as a KinematicDictBuilder.

#### `AdjointCritEdDictBuilder.fill_arrays_and_bins(self, data)`

Only fill array in IFP adjoint criticality edition case.

### `class valjean.eponine.tripoli4.common.VolAdjCritEdDictBuilder(colnames, bins)  — bases: DictBuilder`

Class to build spectrum per volume instead of per kinematic variables. E is still present.

#### `VolAdjCritEdDictBuilder.fill_arrays_and_bins(self, data)`

Only fill array in IFP adjoint criticality edition case.

### `valjean.eponine.tripoli4.common.convert_crit_edition(res)`

Convert IFP adjpint criticality edition results in standard kinematic result.

### `valjean.eponine.tripoli4.common.convert_kij_sources(res)`

Convert k`ij` sources result in python dictionary in which k`ij` sources values are converted in a NumPy array.

param dict res  
k`ij` sources

returns  
same dictionary with `numpy.ndarray` for k`ij` sources values

### `valjean.eponine.tripoli4.common.convert_kij_result(res)`

Convert k`ij` result in NumPy objects and return a dictionary.

param dict res  
k`ij` result with keys `'used_batches'`, `'kij_eigenval'`, `'kij_eigenvec'`, `'kij_matrix'`

returns  
dictionary containing the same keys but with different types:

<!-- -->

    {'used_batches_res': int, 'kij_mkeff_res': float,
     'kij_domratio_res': float, 'kij_reigenval_res': numpy.array,
     'kij_reigenvec_res': numpy.array, 'kij_matrix_res': numpy.array}

For more details see `eponine-kij-result`.

This result returns **right** eigenvalues and **right** eigenvectors (meaning of the 'r' in the key).

### `valjean.eponine.tripoli4.common.convert_kij_keff(res)`

Convert matrices in NumPy array or matrix when estimating k`eff` from k`ij`

param dict res  
k`ij` result from k`eff` result block

returns  
dictionary containing `NumPy` arrays:

<!-- -->

    {'keff_estimator': str,
     'results': {'used_batches_res': int,
                 'kij_mkeff': float (kij result - keff),
                 'space_bins_res': numpy.array of int with shape (nbins,) or
                   (nbins, 3), the latter case corresponding to space mesh,
                 'kij_leigenvec_res': numpy.array,
                 'kij_matrix_res': numpy.array,
                 'kij_stddev_matrix_res': numpy.array,
                 'kij_sensibility_matrix_res': numpy.array}}

Key `'space_bins'` is facultative.

For more details see `eponine-kij-in-keff`.

The eigenvector is here the dominant **left** eigenvector.

### `class valjean.eponine.tripoli4.common.SensitivityDictBuilder(colnames, lnbins)  — bases: DictBuilder`

Class to build sensitivity results dictionary.

#### `SensitivityDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for sensitivities.

Fill integrated result (written as energy integrated but integrated over all dimensions) in the `'integrated_res'` array, that will be in parallel of the default sensitivity result (a priori always here).

#### `SensitivityDictBuilder.add_last_bins(self, data)`

Add last bins in incident energy (E), energy (E') and direction cosine (µ). All orders are possible.

param list data  
results as a list of dictionaries

### `valjean.eponine.tripoli4.common.convert_sensitivities(res)`

Convert sensitivities to dictionary containing `numpy.ndarray`.

param res  
result

return  
list(dict) containing the results and the associated metadata.

The dictionary contains a structured array of 3 dimensions: incident energy `'einc'`, exiting energy `'e'` and direction cosine `'mu'`. The dtype is `('score', 'sigma')`.

Bins are filled in an `collections.OrderedDict` always containing the 3 keys `'einc', 'e', 'mu'` in the order of the bins in the `numpy.ndarray`.

### `class valjean.eponine.tripoli4.common.SphericalHarmonicsDictBuilder(colnames, bins, corr_names)  — bases: DictBuilder`

Class specific to results on spherical harmonics.

This class inherites from DictBuilder, see `DictBuilder` for initialization and common methods.

Arrays are indexed by $(u, v, w)$ for space, $ie$ for incident energy, $e$ for energy, $l$ for moment and $m$ for sub_moment with $L + 1$ values of $l$ and $2L + 1$ values of $m$, $L$ being the maximum value of $l$.

#### `SphericalHarmonicsDictBuilder.fill_arrays_and_bins(self, data)`

Fill arrays and bins for spherical harmonics results.

param data  
parsed result from *pyparsing*

#### `SphericalHarmonicsDictBuilder.add_last_bins(self, data)`

Add last bins in incident energy and energy.

param dict data  
last result

#### `SphericalHarmonicsDictBuilder.fill_space_bins(self)`

Fill spaces bins based on array shape.

#### `SphericalHarmonicsDictBuilder.fill_moments_bins(self)`

Fill moments bins.

- $l$ goes from 0 to $L$
- $m$ goes from $-L$ to $L$

#### `SphericalHarmonicsDictBuilder.reduced_bins(self, score)`

Reduce bins according to score.

Bins are initialized with highest dimensions possible for each. This method makes them match with the array shape. For example, remove incident energy bins keeping first and last edges in most case. A special case is done for fission_spectrum score that only has one $l$ value, so $l=0$, $m=0$.

param str score  
score name

returns  
bins

rtype  
collections.OrderedDict

### `valjean.eponine.tripoli4.common.convert_spherical_harmonics(res, colnames=('score', 'sigma'))`

Convert results on spherical harmonics to dictionary containing `numpy.ndarray`.

param res  
result

param list(str) colnames  
name of the columns/results

returns  
dict containing the results and the associated metadata.

### `valjean.eponine.tripoli4.common.convert_list_to_tuple(liste)`

Convert nested list to nested tuple (to get imutable object).

If list is not nested just convert it to tuple.

param liste  
result as a liste

return  
(nested) tuple

[^1]: Definition of µ and φ, direction angles (see also user guide)

    - µ = cos(θ)
    - if ANGULAR keyword used: result only splitted in µ, with θ is defined with respect to the normal of the surface used in SURF
    - if 2D_ANGULAR keyword used: result splitted in µ and φ, defined in the global frame

[^2]: The structured array elements in uncertainty spectrum case are:

    > - `'sigma2(means)'`: variance of means or σ`2` of means
    > - `'mean(sigma_n2)'`: mean of variances, with variance = v`n`
    > - `'sigma(sigma_n2)'`: σ(variances) = $\sqrt{v(v_n)}$
    > - `'fisher test'`: this is an estimator more than a test
    > - Variance, or sigma_n2 is given by: $v_n = \frac{\sum^n_i{(x_i -m)^2}}{n(n-1)}$

[^3]: Definition of µ and φ, direction angles (see also user guide)

    - µ = cos(θ)
    - if ANGULAR keyword used: result only splitted in µ, with θ is defined with respect to the normal of the surface used in SURF
    - if 2D_ANGULAR keyword used: result splitted in µ and φ, defined in the global frame
