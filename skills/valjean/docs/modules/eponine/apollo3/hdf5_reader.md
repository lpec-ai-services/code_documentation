<!-- source: modules/eponine/apollo3/hdf5_reader.rst -->

# `hdf5_reader` – Read an Apollo3 HDF5 and store the results

This module is designed to read all results contained an standard HDF5 output file from Apollo3 (with keff, fluxes and rates) and to store them in memory as a `Browser`. This makes it possible to explore the content of the file using the facilities provided by `Browser`.

Note

The main limitation is on speed, especially if the HDF5 file is big or contains a lot of nested groups. In that case, if you do not need to explore the file and you know exactly which results will be used, use `Picker` instead.

## Data models of Apollo3 HDF5 files

The Apollo3 HDF5 output files mainly follow the standard data model, initially designed for reaction rates, which is structured as follows:

``` 
┌─ info ─┬─ (COMMENT)
│        ├─ NOUT
│        ├─ output_id1 ┬─ GEOMID
│        │             ├─ NG
│        │             └─ COMMENT
│        ├─ output_id2 ┄
│        ┆
│        ┆
│        └─ output_idNOUT ┄
│
├─ geometry ─┬─ NGEO
│            ├─ geometry_id1 ┬─ NZONE
│            │               ├─ VOLUME[NZONE]
│            │               └─ ZONENAME[NZONE]
│            ├─ geometry_id2 ┄
│            ┆
│            ┆
│            └─ geometry_idNGEO ┄
│
├─ output_id1 ─┬─ totaloutput ─┬─ KEFF (float)
│              │               ├─ (KINF (float))
│              │               ├─ (ABSORPTION[NG])
│              │               ├─ (CURRENT[NG])
│              │               ├─ (FLUX[NG])
│              │               ├─ (MIGRATIONAREA (float))
│              │               ├─ (PRODUCTION[NG])
│              │               ├─ (NVAL)
│              │               ├─ (LOCALVALUE[NVAL])
│              │               ├─ (LOCALNAME[NVAL])
│              │               └─ (localvalue) ─┬─ LOCALNAME[NVAL]
│              │                                ├─ value_id1
│              │                                ├─ value_id2
│              │                                ┆
│              │                                ┆
│              │                                └─ value_idNVAL
│              ├─ zone_id_1 ─┬─ NISOT
│              │             ├─ ISOTOPE[NISOT]
│              │             ├─ CONCEN[NISOT]
│              │             ├─ FLUX[NG]
│              │             ├─ macro ─┬─ reaction_id[NG]
│              │             │         ├─┄
│              │             │         ┆
│              │             │
│              │             ├─ isotope_id1 ─┬─ reaction_id[NG]
│              │             │               ├─┄
│              │             │               ┆
│              │             │               ┆
│              │             │
│              │             ├─ isotope_id2 ┄
│              │             ┆
│              │             ┆
│              │             └─ isotope_idNISOT ┄
│              ├─ zone_id2 ┄
│              ┆
│              ┆
│              └─ zone_idNZONE ┄
├─ output_id2 ┄
┆
┆
└─ output_idNOUT ┄
```

Elements in brackets are optional. If `NISOT == 0`, the `ISOTOPE`, `CONCEN` and `isotope_id` groups will be absent. The `macro` group stores the macroscopic reaction rates (= reaction rates for a medium). The `zone_id` folder names appear as values in the ZONENAME dataset in the geometry group, and they are arbitrary strings (chosen by the user in the Apollo3 case). `VOLUME` stores the volumes (in cm³) of the zones, if needed later for normalisation for example. Most physics quantities are given on `NG` energy groups but the group bounds are not stored in the file. Some quantities are given as a function of energy groups and anisotropy. The order of the anisotropy development is available in the `'info'` group, possibly in the `'isotope_id` one. Current and surfacic flux (under `'totaloutput'`) have a `surface id` component in addition to energy groups.

Some files can also contain custom values or user values, especially in some cases the standard structure does not appear at all (no `zone_id` or `totaloutput` folder) but directly local values:

``` 
┌─ info ─┬─ (COMMENT)
│        ├─ (FORMAT)
│        ├─ (VERSION)
│
└─ output ─┬─ (LOCALVALUE[NVAL])
           ├─ (LOCALNAME[NVAL])
           └─ (localvalue) ─┬─ LOCALNAME[NVAL]
                            ├─ value_id1
                            ┆
                            ┆
                            └─ value_idNVAL
```

## Use of `Reader`

``` python
from valjean.eponine.apollo3.hdf5_reader import Reader
ap3r = Reader('MON_FICHIER.hdf')
ap3b = ap3r.to_browser()
```

See `browser` to get more details on how to use the `Browser` objects.

In the resulting `Browser`, the metadata are taken from the `h5py.Group` values, while the actual data are taken from the `h5py.Dataset` ones.

Data are directly stored as `Dataset`. Errors are set to `numpy.nan` by default but this can be changed and be set to 0 (for example) using the `error_value` argument to the constructor. Bins are set to the group indices, or to group indices and number of anisotropies when available. Two specific cases are added: \* surfacic flux: bins are given in group indices and surface numbers \* current: bins are given in group indices, surface numbers and direction

Some metadata keys in the browser are slightly different from the corresponding names of the HDF5 file:

- in the global variables (`Browser.globals`):  
  - under the `'info'` key:  
    - `'geom_id'` for the `'GEOMID'` metadata
    - `'ngroups'` for `'NG'`

  - under the `'geometry'` key: a dictonary associating the `'geom_id'` names to dictionaries of {`'ZONENAME'`: `'VOLUME'`}.

- in the results (`Browser.content`):  
  - zone names: kept as they are given in the HDF5 file (also true for `'totaloutput'`)
  - reaction names, flux, keff are set in lower case instead of upper
  - `'CONCEN'` is renamed in `'concentration'` and appears as a standard result (like reaction rates)
  - isotopes names are kept as they are but spaces surrounding the name are stripped. The `'macro'` key is kept unchanged for macroscopic results (integrated over isotopes)
  - local value names are left inchanged (under the `'result_name'` key).

The most common keys in the `Browser` are `['result_name', 'output', 'zone', 'isotope']`.

An inspect function is also available (no class:<span class="title-ref">Reader</span> object needed) to have a quick look at the content of the file.

``` python
from valjean.eponine.apollo3.hdf5_reader import inspect
inspect('MON_FICHIER.hdf')
```

### `valjean.eponine.apollo3.hdf5_reader.hdf_to_browser(*args, **kwargs)`

Build a `Browser` from an Apollo3 HDF5 output.

param args  
other arguments to be passed to `Reader` constructor

param kargs  
keyword arguments to be passed to `Reader` constructor

returns  
Browser

### `class valjean.eponine.apollo3.hdf5_reader.Reader(fname, error_value=np.nan)`

Read an HDF5 file from Apollo3.

#### `Reader.read_file(self, hfile)`

Read the HDF5 file.

The information read depends on the type of file. In the case of a *standard* output file, we read `'info'`, `'geometry'` and all results. In a *user* output, only results are read.

param str hfile  
path to the HDF5 file

raises ReaderException  
if unexpected keys are found.

#### `Reader.process_standard_values(self, hfile)`

Process standard values (keff, flux, rates).

#### `Reader.process_user_values(self, hfile)`

Process user values stored in files (named local values in file).

#### `Reader.to_browser(self)`

Build a `Browser` from the results in the HDF5 file.

rtype  
Browser

### `valjean.eponine.apollo3.hdf5_reader.extract_geometry(geometry)`

Extract geometry in dict to go to `Browser` globals.

param h5py.Group geometry  
geometry stored in HDF5

### `valjean.eponine.apollo3.hdf5_reader.extract_info(info)`

Extract info in dict to go to `Browser` globals.

param h5py.Group info  
info stored in HDF5

### `valjean.eponine.apollo3.hdf5_reader.extract_standard_values(val, ngroups, error)`

Extract results from Apollo3 HDF5 file.

param str out_id  
name of the output folder in HDF5

param h5py.Group val  
results stored in the folder

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

returns  
list of all results stored with metadata and data shaped as `Dataset`

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.extract_user_values(val, error)`

Extract user results (or 'local' values).

param h5py.Group val  
results stored under `'LOCALVALUES'`

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

returns  
list of results including metadata

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.extract_localvalues(lnames, lvals, error)`

Extract local values from a list of local names.

param list(str) lnames  
list of the names of the local values

param h5py.Dataset lvals  
local (scalar) values

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

returns  
list of results including metadata

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.loop_over_std_values(lres, ngroups, error)`

Loop over results stored in the `'output_*'` groups of the HDF5 file.

Also retrieve number of anisotropies from the `info` `h5py.Group`.

param h5py.Group lres  
list of results

param int ngroups  
number of energy groups

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

returns  
list of results including metadata

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.hdfdataset_to_dataset(hdf_data, what, error, bins=None)`

Build `Dataset` from HDF5 dataset (in *rates* cases).

Returns a scalar or an array depending on data shape.

param h5py.Dataset hdf_data  
dataset containing the data

param str what  
quantity name

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

param collections.OrderedDict bins  
bins corresponding to data, default `None`

rtype  
Dataset

### `valjean.eponine.apollo3.hdf5_reader.build_dataset(data, error, what, bins=None)`

Build `Dataset` from HDF5 result.

param data  
data

type data  
numpy.generic, numpy.ndarray

param str what  
quantity name

param error  
value of error

type error  
numpy.generic, float, int, default = `numpy.nan`

param str what  
quantity name

param collections.OrderedDict bins  
bins corresponding to data, default `None`

rtype  
Dataset

### `valjean.eponine.apollo3.hdf5_reader.make_bins(nres, vres, ngroups, anisotropies=None, nsurfaces=None)`

Build bins `collections.OrderedDict`.

The bins currently available are \* number of energy groups \* number of anisotropies (for isotopes reaction rates) \* number of surfaces (for current and surface flux)

param h5py.Group data  
`info` block from `output_*`

rtype  
dict

returns  
dictionary of all possible number of bins

### `valjean.eponine.apollo3.hdf5_reader.extract_output_info(data, name='anisotropy')`

Extract info from output group containing number of anisotripies.

param h5py.Group data  
`info` block from `output_*`

param str name  
anisotropy name (`'anisotropy'` per default, result name if one

rtype  
dict

returns  
dictionary indexed by anisotropy name

### `valjean.eponine.apollo3.hdf5_reader.extract_surfaces_number(data)`

Extract number of surfaces if available.

### `valjean.eponine.apollo3.hdf5_reader.extract_concentrations(zone, error)`

Store isotopes list and concentration from the zone group.

param h5py.Group zone  
HDF5 group corresponding to the zone

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

returns  
list of dictionaries with isotope name in metadata, `'concentration'` as `result_name` and concentration values stored in a `Dataset` under the `'results'` key

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.extract_zone_values(val, ngroups, error)`

Store results by zone.

Results are stored depending on their nature (flux, concentrations, etc.).

param h5py.Group val  
HDF5 group containing results from a given zone

returns  
list of results including metadata

param error  
value to give to the error (default: `numpy.nan`)

type error  
int, float

rtype  
list(dict)

### `valjean.eponine.apollo3.hdf5_reader.dict_to_list(key_name, tdict)`

Transform a dictionary in a list of dictionaries including the key as a new key, value member of each dictionary.

param str key_name  
key of the new dictionary

param dict tdict  
dictionary whose keys will become values of key_name

returns  
list of results including metadata

rtype  
list(dict)

\>\>\> tdict = OrderedDict() \>\>\> tdict\['Graham'\] = \[{'day': 'Monday', 'meal': 'spam'}, ... {'day': 'Tuesday', 'meal': 'egg'}\] \>\>\> tdict\['Terry'\] = {'day': 'Monday', 'meal': 'bacon'} \>\>\> tlist = dict_to_list('consumer', tdict) \>\>\> len(tlist) 3 \>\>\> from pprint import pprint \>\>\> pprint(tlist) \[{'consumer': 'Graham', 'day': 'Monday', 'meal': 'spam'}, {'consumer': 'Graham', 'day': 'Tuesday', 'meal': 'egg'}, {'consumer': 'Terry', 'day': 'Monday', 'meal': 'bacon'}\]

Simplify this example by changing back OrderedDict in dict when python 3.5 won't be anymore supported.

### `valjean.eponine.apollo3.hdf5_reader.inspect(hfile, name_spaces=50)`

Loop recursively over content of the file and print it.

param str hfile  
path to the Apollo3 HDF5 ouput

param int name_spaces  
number of spaces reserved for the folder's names, default = 50

### `class valjean.eponine.apollo3.hdf5_reader.ReaderException  — bases: Exception`

An error that may be raised by the `Reader` class.
