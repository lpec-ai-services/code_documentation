<!-- source: modules/eponine/tripoli4/depletion.rst -->

# `depletion` – Read Tripoli-4 depletion results

Module to deal with ROOT outputs from Tripoli-4 in depletion mode.

This module is an interface with Tripoli-4 depletion results, stored as `ROOT` files, see the Tripoli-4 user guide and [the ROOT website](https://root.cern/) for more details.

The available results match the usual Tripoli-4 results from depletion:

- k`eff` as `kcoll`, `ktrack`, `kstep`;
- β\_`eff` from prompt and Nauchi, called `beff_prompt` and `beff_nauchi`;
- renormalisation factor, called `renorm`
- total power
- power
- local burnup
- flux: fast neutron flux (`fast_flux`), thermal neutron flux (`therm_flux`) and total flux (`flux`)
- mass
- concentration
- activity
- reaction rates: for fast neutrons (`fast_reaction_rate`), for thermal neutrons (`thermal_reaction_rate`) and for one group (`reaction_rate`). The thermal group only gives non-zero results for fission rate.

Some of these results can be accessed from valjean using the `DepletionReader` class from this module. In some cases, it is necessary to provide keyword for the composition name (`componame`), the isotope name (`isotope`) or the reaction name (`reaction`).

Results can be obtained at a given depletion step (so a scalar value) or for all available steps, giving in both cases a `Dataset`. The access method of the array ends with `_time` if the required quantity is given in function of *time* and `_burnup` if it is in function of *burnup*.

A typical example of use of this module is the following:

``` python
from valjean.eponine.tripoli4.depletion import DepletionReader
depr = DepletionReader.from_evolution_steps(
    'evolution_1.root', 'evolution_2.root',
    root_build='/path/where/to/build/root/libraries')
# get kstep at step 1
kstep = depr.kstep(1)
# get kstep as a function of burnup
akstep = depr.kstep_burnup()
# get total power as a function of time
atotpow = depr.total_power_time()
# get U238 concentration in composition COMPO1 at step 5
conc_u238 = depr.concentration(step=5, componame='COMPO1', isotope='U238')
# get U238 fission reaction rate in composition COMP1 as a function of time
reac_u238 = depr.reaction_rate_time(componame='COMP1', isotope='U238',
                                    reaction='REAMT18')
```

Some helper methods provide the list of compositions, the list of isotopes in a given composition or the reaction rates associated to a given isotope in a given composition.

### `valjean.eponine.tripoli4.depletion.title_to_snake_case(word)`

Convert `word` from title case to snake case.

\>\>\> title_to_snake_case('ThisIsATitle') 'this_is_a_title'

### `valjean.eponine.tripoli4.depletion.generic_docstrings(res_type, *list_params)`

Define generic docstrings for the access functions of depleted results.

### `valjean.eponine.tripoli4.depletion.add_accessors(dict_res)`

Automatic construction of result accessors.

### `class valjean.eponine.tripoli4.depletion.DepletionReader(mbr)`

Class to use depletion results from Tripoli-4

#### `DepletionReader.init_postscripts(root_build='')`

Initialize postscripts from ROOT macros.

ROOT macros are in the `resources/depletion` folder. They are compiled in the `root_build/__t4depletion__` folder to be used afterwards. Thus it is recommended to give a `root_build` path in order to avoid the default one, in `valjean` folder where the user may not have write permissions.

#### `DepletionReader.from_evolution_steps(cls, *fnames, root_build='')`

Initialisation from `evolution.root` files (one per simulation).

param str fnames  
ROOT files

#### `DepletionReader.from_mbr(cls, fname, mbr_name, root_build='')`

Initialisation from ROOT file containing a MeanBurnupResults class.

param str fname  
ROOT file name

param str mbr_name  
name of the MeanBurnupResults object in the file

#### `DepletionReader.save_mbr(self, name)`

Save the MeanBurnupResults in a ROOT file.

param str name  
name of the output ROOT file name

#### `DepletionReader.nb_simu(self)`

Return the number of independent simulations.

rtype  
int

#### `DepletionReader.nb_compositions(self)`

Return the number of compositions.

:rtype; int

#### `DepletionReader.nb_steps(self)`

Return the number of steps.

rtype  
int

#### `DepletionReader.burnup(self, step)`

Return burnup from MeanBurnupResults object.

param int step  
calculation step to use to get the value

returns  
burnup value and error

rtype  
Dataset

#### `DepletionReader.burnup_array(self)`

Return burnup array from MeanBurnupResults object.

returns  
burnup value and error by step

rtype  
Dataset

#### `DepletionReader.time(self, step)`

Return time from MeanBurnupResults object.

param int step  
calculation step to use to get the value

returns  
time value and error

rtype  
Dataset

#### `DepletionReader.time_array(self)`

Return time array from MeanBurnupResults object.

returns  
time value and error by step

rtype  
Dataset

#### `DepletionReader.composition_names(self)`

Return the list of composition names.

rtype  
list(str)

#### `DepletionReader.isotope_names(self, step, componame)`

Return the list of isotopes in the given composition at the given step.

param int step  
calculation step to use to get the value

param str componame  
composition name in which list of isotopes is required

returns  
list of available isotopes

rtype  
list(str)

#### `DepletionReader.reaction_names(self, step, componame, isotope)`

Get reaction names in composition for the given isotope.

param int step  
calculation step to use to get the value

param str componame  
composition name where reaction is required

param str isotope  
isotope name for which reaction is required

returns  
list of available reactions

rtype  
list(str)

#### `DepletionReader.isotope_reaction_names(self, step, componame)`

Get dictionary of reactions per isotope for the given step and composition.

param int step  
calculation step to use to get the value

param str componame  
composition name where reactions per isotope are required

returns  
reactions by isotopes

rtype  
dict(str, list(str))

#### `DepletionReader.dump_global_results(self, step)`

Print results for a given step.

This includes compositions.

### `class valjean.eponine.tripoli4.depletion.DepletionReaderException  — bases: Exception`

An error that may be raised by the `DepletionReader` class.
