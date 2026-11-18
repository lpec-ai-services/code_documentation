# SPECIAL OUTPUTS
<!-- source PDF pages 384-389 -->

<!-- page 384 -->
Chapter 31
SPECIAL OUTPUTS
This command is used to output data intended to be displayed as plots or directly looked up by the user in a
text format. The syntax is as follows:
OUTPUT
LANGUAGE <language>
*
XVGR
Data for scores display
END_XVGR
*
SECTION
Data for cross-sections display
END_SECTION
*
INFO NUCLEI
Data for info on nuclei
END_OUTPUT
where: <language> is either FRENCH or ENGLISH (the default is an output in English).

## 31.1 XVGR PLOTS

The XVGR option is used to create plots from the code results in XVGR format. The syntax is as follows:

<!-- page 385 -->
XVGR
ENERGY_INF Ein f
ENERGY_SUP Esup
TYPE <type>
EDITION nb(edit)
LETHARGY
HISTO
END_XVGR
or:
XVGR
< ENTROPY_TYPE >
END_XVGR
where:
• ENERGY_INF (optional) allows to set the lower bound Ein f of x axis, default is 1·10−11.
• ENERGY_SUP (optional) allows to set the upper bound Esup of x axis, default is 2·10+01.
• TYPE (optional) allows to select the graphical interpolation type from LIN_LIN, LIN_LOG, LOG_LIN or
LOG_LOG, default is LOG_LIN.
• EDITION (optional) allows to select a multiple of the printout frequency nb(edit), default is 1. Files
are not created for each printout but only for a subset of one printout out of nb(edit). For example if
the frequency output requested in the simulation block (see chapter 22) is 100 but no EDITION option is
requested in the OUTPUT XVGR command block, then XVGR files are created every 100 batches. Now, if
addionally an OUTPUT XVGR edition is requested and nb(edit) is set to 5, then XVGR files are created
every 500 batches.
• LETHARGY (optional) produces score/lethargy values in XVGR files.
• HISTO (optional) produces XVGR files in histogram interpolation mode.
• <ENTROPY_TYPE> is either SHANNON or BOLTZMANN.
The code produces as many plots (which can be displayed with XVGR, XMGR, GRACE and XMGRACE) as
there are spectrum printouts in the output file (plot filenames are attributed in the output file after the line
“Next score corresponds to file”).
In a criticality calculation, two files are created (for kcoll and kstep estimators), showing the variation in keff
as a function of the number of batches (files are updated at each batch).
If entropy is asked, then one file is produced and updated at each batch (spectrum plots are not produced).
This option does not work with angle or time grids.
It is also limited to flux, current and reaction rates response types.

<!-- page 386 -->
## 31.2 CROSS-SECTION DATA AND PLOTS

The SECTION option enables to output neutron or photon macroscopic or microscopic cross-sections. The
output values are those directly used by the code during the simulation, after the nuclear data reading and the
initialization step of the code. The output format is a two-column ASCII format giving (energy, cross-section)
couples. The cross-sections may then be plotted with XMGRACE or any other graphical tool. The syntax is
as follows:
SECTION
n
<output_type_1> name_1 temperature_1
...
<output_type_n> name_n temperature_n
ENERGY_INF Ein f
ENERGY_SUP Esup
NB_POINTS nb(points)
PARTICLE <particle_type>
UNITS ENERGY <unit>
END_SECTION
where:
• n is the number of cross-section outputs requested
• for each cross-section output i, <output_type_i> is either MATERIAL (for a macroscopic crosssection
), NUCLEUS (for a total microscopic cross-section) or INTERACTION (for a microscopic crosssection
of a given interaction). In this latter case, the keyword INTERACTION must be followed by the
interaction code and the keyword NUCLEUS, before entering name_i. This interaction code is defined in
the same way as for the reaction rates input data of the response types chapter (see section 13.2)
• name_i is the name of one of the compositions presents in the COMPOSITION command block (in case
of a macroscopic cross-section) or the name of a nuclide present in one or several compositions (in case
of a microscopic cross-section)
• temperature_i is an integer and is the temperature of the composition or nuclide
• Ein f is the lower energy requested for the output of each cross-section (the default is 1e-11 MeV for
neutrons and 1e-3 MeV for photons)
• Esup is the upper energy requested for the output of each cross-section (the default is 20 MeV)
• nb(points) is the total number of points requested for the output of each cross-section (the default is
500 000 points). Cross-sections are interpolated by the code at nb(points) regularly spaced energies
between Ein f and Esup. For photon cross-sections, the user is advised to keep a minimum of 10 000
points because the interpolation of the evaluation is generally not linear-linear between points.

<!-- page 387 -->
• <particle_type> is either NEUTRON or PHOTON (the default is NEUTRON)
• <unit> is either MEV for MeV or EV for eV (the default is MEV).
The five last lines of the OUTPUT SECTION command block are optional.
The names of the produced files are such as "xs_output_<NAME>_<TEMP>K.dat" for the MATERIAL and
NUCLEUS cases, with <NAME> the name of the requested composition or nuclide and <TEMP> the requested
temperature. The file names are such as "xs_output_<NAME>_<TEMP>K_int<NUM>.dat" for
the INTERACTION case, with <NAME> the requested nuclide, <TEMP> the requested temperature and
<NUM> the requested interaction code.
The user will take advantage of a log-log scale when displaying these data with a graphical tool.

## 31.3 INFORMATION ON SIMULATED NUCLEI

The INFO NUCLEI option enables to produce a specific text file containing a list of interactions simulated by
the code for the different nuclides presents in the data file (needed for the transport or for fictive reaction rates
tallies). The syntax is as follows:
INFO NUCLEI
filename
where filename is the name of the text file produced.
For each nuclide, a list of neutronic and/or photoatomic and photonuclear reactions is provided, depending
on the types of simulated particles and simulation mode. Information on photonuclear reactions is given only
if the PHOTO_NUCLEAR simulation mode is requested by the user (see chapter 22). The information consists
of the interaction name, the TRIPOLI-4® interaction code (as given in the section 13.2), the MT number of
the ENDF format (see reference [35]), the interaction threshold, and an indication of presence of any photon
production data (for coupled neutron-gamma simulations only). This information comes from the nuclear
data, as retrieved by TRIPOLI-4® for its simulation step.

## 31.4 T4G DEDICATED OUTPUTS

Two dedicated outputs are available for T4G: meshes and point events. Their format is easily readable and
understandable by the user (similar to the Open DX general format from IBM, see reference [23]).

### 31.4.1 MESH OUTPUTS

Mesh outputs are
• Tabulated sources: STORE_IN_FILE <output_filename> just after the TABULATED keyword in the
GEOMETRIC_DISTRIBUTION of the source block;

<!-- page 388 -->
• Importance maps: STORE_IN_FILE ASCIIG (block VARIANCE_REDUCTION);
• Mesh results: STORE_IN_FILE (block EXTENDED_MESH), see also NORMALIZE.
Communications with the T4G tool are described in the chapter 38. It is however reminded that this tool is
made aware of the mesh outputs by the mean of the <inputDeck>.meshes file using the following format
name <meshfile0>.general [frame <ox> <oy> <oz> <ux> <uy> <uz> <vx> <vy> <vz>]
name ...

### 31.4.2 POINT EVENT OUTPUTS

Point event outputs must be called from the SIMULATION block using the keywords
• Source points: STORE_SOURCES_IN_FILE;
• Collision points: STORE_COLLISIONS_IN_FILE;
• Leakage points: STORE_LEAKAGE_IN_FILE.
As the output size may be voluminous, dump is done in a per batch/cycle basis and can either be in ASCII or
BINARY mode.
STORE_XXX_IN_FILE
#ASCII
#BINARY
GENERAL
LIST <nbbatch> <batch_1> <batch_2> <batch_nbbatch>
For use in T4G, point files must declared by the mean of the <inputdeck>.points file using the following
syntax
name <pointfile0>.general
name ...
The current list of fields can be found in the corresponding header (.general file), for example:
field = x, y, z, ox, oy, oz, energy, simulation_weight, sid, pid, time, mxs, nbcoll,
parttype, status, cellid, nucleus, interaction_type, sampled_fission
We can find the following quantities
• x, y, z, t, position and time coordinates of the event
• ox, oy, oz, direction coordinates of the event
• simulation_weight, statistical weight of the particle during the event
• sid, pid are the source particle identifier and the particle identifier

<!-- page 389 -->
• mxs, macroscopic total cross section at the location and during the event (can be used to calculate a flux)
• cellid, volume identifier
• energy, nucleus, interaction_type, sampled_fission, should be self explanatory
