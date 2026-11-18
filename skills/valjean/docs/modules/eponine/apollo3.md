<!-- source: modules/eponine/apollo3.rst -->

# `apollo3` – Data reading for Apollo3

 Introduction ------------

This sub-package transforms some results from Apollo3 in the standard data format of `valjean`. For the moment only results stored in the HDF5 format are concerned.

Two possibilities are given to the user, available in two different modules:

- Reading and storing all results in the HDF5 file in a `Browser` with `hdf5_reader`. All results are converted in `Dataset`, metadata allow selection in `Browser`. Further selections are possible with the `Browser` as usual.
- Picking only results of interest for the user (normally largely quicker) with `hdf5_picker`. All results are returned as `Dataset`. No `Browser` is built.

## Main modules

- `apollo3/hdf5_reader` (`apollo3/hdf5_reader.md`)
- `apollo3/hdf5_picker` (`apollo3/hdf5_picker.md`)
