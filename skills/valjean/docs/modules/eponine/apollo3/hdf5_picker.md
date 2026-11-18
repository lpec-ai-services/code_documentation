<!-- source: modules/eponine/apollo3/hdf5_picker.rst -->

# `hdf5_picker` – Pick results in HDF5 from Apollo3

This module is designed to pick the required results from an Apollo3 standard HDF5 output file. This means that the users should already know which result they want to extract. Some navigation methods exist, but they are not optimised for speed of access.

One possibility is to first explore the output file interactively with a `Reader`, and then to write the efficient code using `Picker`.

## Picking results with `Picker`

``` python
from valjean.eponine.apollo3.hdf5_picker import Picker
ap3p = Picker('MON_FICHIER.hdf')
rate_ds = ap3p.pick_standard_value(output='OUTPUT_FOLDER',
                                   zone='ZONE_FOLDER',
                                   result_name='REQUIRED_RESULT')
```

For example to get the k`eff`, in `output_1` under `totaloutput`:

``` python
keff = ap3p.pick_standard_value(output='output_1', zone='totaloutput',
                                result_name='KEFF')
```

The result will be a `Dataset`. The error is not available and it is set to `numpy.nan` by default. It can be changed using the `error_value` to the `Picker` constructor.

In the case of a *rates* file, bins are set to groups index in most cases. When the quantity is also calculated on anisotropies (e.g. diffusion) the bins are `('anisotropies', 'groups')`. The surfacic flux (`'SURFFLUX'`) bins are `('groups', 'surfaces')` and the current (`'CURRENT'`) ones are `('groups', 'surfaces', 'direction')`.

Results per isotopes can be obtained with an additional keyword argument, for example for `10`B absorption in `output_0` from zone `5`:

``` python
b10abs = ap3p.pick_standard_value(output='output_0', zone='5',
                                  result_name='Absorption', isotope='B10')
```

Macroscopic rates are obtained with `isotope='macro'`.

Local values can also be retrived using the `Picker.pick_user_value` method:

- if `'LOCALNAME'` and `'LOCALVALUE'` belong to zone names:

  > ``` python
  > locv = ap3p.pick_user_value(output='output', zone=None,
  >                             result_name='LOCAL_VALUE_NAME')
  > ```

- if `'LOCALNAME'` and `'LOCALVALUE'` belong to result names in a zone:

  > ``` python
  > locv = ap3p.pick_user_value(output='output', zone='totaloutput',
  >                             result_name='LOCAL_VALUE_NAME')
  > ```

- if `'localvalue'` belongs to zone names:

  > ``` python
  > locv = ap3p.pick_user_value(output='output', zone='localvalue',
  >                             result_name='LOCAL_VALUE_NAME')
  > ```

In both cases, it might be useful to check the zones and the local names first.

## Quick exploration with `Picker`

Some helpers exist if needed:

- `Picker.outputs`: list of output folders
- `Picker.geometry`: list of geometries stored in a given output folder
- `Picker.nb_groups`: number of energy groups available in a given output folder
- `Picker.zones`: list of zones in a given output folder
- `Picker.isotopes`: list of isotopes in a given zone of a given output folder
- `Picker.results`: list of available results in a given zone of a given output folder, isotope can be precised if needed
- `Picker.nb_anisotropies`: number of anisotropies available for a given result for the considered isotope in its zone and output
- `Picker.local_names`: list of names of the local values stored in a given zone from a given output folder

### `class valjean.eponine.apollo3.hdf5_picker.Picker(fname, error_value=np.nan)`

Pick selected values from an Apollo3 HDF5 file.

#### `Picker.close(self)`

Close HDF5 file.

#### `Picker.geometry_from_geomid(self, *, geometry)`

Return geometry as a dictionary of zone names and volumes.

param str geometry  
geometry name

#### `Picker.geometry(self, *, output)`

Return geometry characteristics (zones and their volumes) from the output name.

param str output  
output in which zones will be found

rtype  
dict

#### `Picker.nb_groups(self, *, output)`

Return the number of groups for the `output`.

param str output  
output in which zones will be found

rtype  
int

#### `Picker.outputs(self)`

Return list of available outputs.

rtype  
list(str)

#### `Picker.zones(self, *, output)`

Return list of available zones in `output`.

param str output  
output in which zones will be found

rtype  
list(str)

#### `Picker.isotopes(self, *, output, zone)`

Return list of available isotopes in `zone` from `output`.

param str output  
output folder considered

param str zone  
zone from output folder

rtype  
list(str)

#### `Picker.results(self, *, output, zone, isotope=None)`

Return available results for the given configuration.

The `'info'` group is not considered as a result (group containing the number of anisotropies), so it is omitted from of the results list.

param str output  
output folder considered

param str zone  
zone from the output folder

param isotope  
isotope considered for results (`'macro'` is counted as an isotope, if no isotope is given global results are given like flux or keff)

type isotope  
str or None

rtype  
list(str)

#### `Picker.nb_anisotropies(self, *, output, zone, isotope, result)`

Return number of anisotropies for the given configuration.

param str output  
output folder considered

param str zone  
zone from the output folder

param isotope  
isotope considered for results (`'macro'` is counted as an isotope, if no isotope is given global results are given like flux or keff)

type isotope  
str or None

param str result  
result considered

rtype  
list(str)

#### `Picker.pick_standard_value(self, *, output, zone, result_name, isotope=None)`

Pick a result according to required parameters from a standard file (like keff, flux or rate).

#### `Picker.local_names(self, *, output, zone)`

Return the list of available local value names.

Note

The most common zones seem to be in this case: `'totaloutput'` (especially in rates files), `None` or `'localvalue'` in core files.

param str output  
output folder considered

param zone  
zone from the output folder

type zone  
str or None

rtype  
list(str)

#### `Picker.pick_value_from_index(self, *, output, result_index, zone, name)`

Pick a user value result from required parameters.

param str output  
output folder considered

param int result_index  
index of the required result

param str zone  
zone from the output folder

rtype  
Dataset

#### `Picker.pick_user_value(self, *, output, result_name, zone)`

Pick a user value result from required parameters (under local value in the file).

param str output  
output folder considered

param str result_name  
name of the required result

param str zone  
zone from the output folder

rtype  
Dataset

### `class valjean.eponine.apollo3.hdf5_picker.PickerException  — bases: Exception`

An error that may be raised by the `Picker` class.
