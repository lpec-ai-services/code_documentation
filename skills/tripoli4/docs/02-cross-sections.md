# CROSS-SECTIONS
<!-- source PDF pages 25-26 -->

<!-- page 25 -->
Chapter 2
CROSS-SECTIONS

## 2.1 NUCLEAR DATA FILE NAMES

The cross-sections used in the TRIPOLI-4® code simulations are pointwise cross-sections in ENDF format,
or multigroup cross-sections in the GENDF format, or multigroup cross-sections calculated with the APOLLO2 code [95].
The name of an ENDF file containing simulation data is created as follows:
lib.particle.isotope.format[.section_type(.therm).temperature]
where
• lib can be:
– endfb6;
– jef2;
– jeff3;
– fendl.
• particle can be:
– neutron;
– gamma;
– electron;
– positron.
Note: For multigroup cross-section in the GENDF format, only particles of type neutron are allowed.
• isotope can be any library isotope value;
• format can be:
– bcd if it is an ASCII file;
– bin if it is a binary file;
– xdr if it is a binary file of the xdr type.
• section_type can be:
– nothing for evaluation files;

<!-- page 26 -->
– pointwise cross-sections:
* pendf for files containing pointwise cross-sections;
* aniso for files containing anisotropy data.
– multigroup cross-sections:
* gendf for files containing multigroup cross-sections;
* mganiso and mgextra for files containing anisotropy data.
• temperature can have any desired temperature value, provided that Doppler broadening by the NJOY system has been
performed;
• therm is a suffix indicating whether the tape contains thermal data or not.
All of the terms between [ ] and ( ) are suffixes indicating the types of cross-sections contained in the file.
The other terms are mandatory.

## 2.2 OPTIMIZING CROSS-SECTION USE

To accelerate code execution, several options are available to access macroscopic cross-sections. Only neutron simulations without
probability tables are concerned.
1. By default, for all materials including up to 25 isotopes, the total macroscopic cross-section is calculated during the initialization
step and stored using an isotope-unionized energy grid. This speeds-up the running time during the simulation, at the
price of a larger memory use. For materials with more than 25 isotopes, the macroscopic cross-section is calculated on the
fly during the simulation.
2. If memory occupation is an issue, it is possible to disable this option. This is carried out using the following additional
command with keyword MEMORY.
3. Conversely, if memory capacities are large enough, the storage of macroscopic cross-sections can be requested for all materials
, whatever the number of isotopes. This is carried out using the following additional command with keyword SPEED_UP.
The syntax for the two last options is as follows (see section 4.3 for syntax conventions):
OPTIMIZE
#
MEMORY 1
#
SPEED_UP 1
END_OPTIMIZE
