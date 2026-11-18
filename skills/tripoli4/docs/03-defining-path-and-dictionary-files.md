# DEFINING PATH AND DICTIONARY FILES
<!-- source PDF pages 27-31 -->

<!-- page 27 -->
Chapter 3
DEFINING PATH AND DICTIONARY FILES
The elementary data used for particle transport are stored in data files. TRIPOLI-4® needs the location of these files to read the
data.

## 3.1 THE PATH FILE

The path file gives the access paths for the following files:
• the dictionary file (see Section 3.2 below) describing the location of the photon and neutron cross-sections. This file should
only be modified by an expert user
• a file giving the atomic weights of the nuclei
• a file giving the energies released by fissile isotopes during fission for the different particles emitted
• a directory giving all data necessary to electron and positron transport:
– the tabulation of Mott cross-sections relative to the Rutherford cross-sections
– electron interactions data (EEDL)
– atom relaxation data (EADL)
• a file containing the isotopic abundances of natural elements
• a directory (with write-enable rights) where the files of cross-sections at given temperatures are to be written if they do not
exist in the available libraries.

### 3.1.1 LEGACY FORMAT

An example path file follows:
/home/TRIPOLI-4/GALILEE-V0-2.1/CEAV5.1/ceav5.1.dictionary
/home/TRIPOLI-4/GALILEE-V0-2.1/Common_Data/mass_rmd.mas95
/home/TRIPOLI-4/GALILEE-V0-2.1/CEAV5/Qfission
/home/TRIPOLI-4/GALILEE-V0-2.1/ENDL97/ELECTRON_DATA
/home/TRIPOLI-4/GALILEE-V0-2.1/Common_Data/abundance

<!-- page 28 -->
### 3.1.2 NEW FORMAT

Starting from version 11, TRIPOLI-4® accepts a new path file format, which is structured as follows:
t4path 0
njoy_dictionary
/home/TRIPOLI-4/GALILEE-V0-2.1/CEAV5.1/ceav5.1.dictionary
mass_data
/home/TRIPOLI-4/GALILEE-V0-2.1/Common_Data/mass_rmd.mas95
Q_fission
/home/TRIPOLI-4/GALILEE-V0-2.1/CEAV5/Qfission
electron_xs
/home/TRIPOLI-4/GALILEE-V0-2.1/ENDL97/ELECTRON_DATA
abundance_data
/home/TRIPOLI-4/GALILEE-V0-2.1/Common_Data/abundance
The integer following the t4path string is a version identifier, reserved for future compatibility. The rest of the file consists of
key-value pairs, which may be given in any order.
Some keys are optional:
• the own_eval key can be used to specify the location of the directory where TRIPOLI-4 will write the nuclear data libraries
generated on the fly by Njoy (see Section 10.4);
• the electron_bremsstrahlung_xs key can be used to specify the location of data tables for Seltzer and Berger’s electron
bremsstrahlung model [96] (see Section 22.14).
Starting from version 12, the following file format is also accepted:
t4path 1
njoy_dictionary
/(...)GALILEE/GALILEE-V0-3.0/CEAV512/ceav512.dictionary
mass_data
/(...)GALILEE/GALILEE-V0-3.0/Standard_data/mass_rmd.mas95
Q_fission
/(...)GALILEE/GALILEE-V0-3.0/CEAV512/Qfission
electron_xs
/(...)GALILEE/GALILEE-V0-3.0/PEID/Electron_Photon
abundance_data
/(...)GALILEE/GALILEE-V0-3.0/Standard_data/abundance
electron_bremsstrahlung_xs /(...)tripoli4.<X>.<Y>/AdditionalData/Bremsstrahlung
idt_photon_xs_file
/(...)tripoli4.<X>.<Y>/AdditionalData/apolib/Gamma/ap3(...)3.1.8_Photo.h5
idt_neutron_xs_file
/(...)tripoli4.<X>.<Y>/AdditionalData/apolib/Neutron/ap3(...)_N-a3ver1.h5
The idt_photon_xs_file and idt_neutron_xs_file keywords specify the default location of the HDF5 cross section files for
the IDT solver (see Chapter 20).
The AdditionnalData directory comes with the code and not with a nuclear data library. When installing the code, if the reference
nuclear data is already installed, as required by the automatic installation tests, the code installer will automatically migrate
the t4path file available in the nuclear data library (e.g.: /(...)/GALILEE/GALILEE-V0-3.0/CEAV512/t4path.ceav512) into
a new t4path file using the new path file format in the Env directory (e.g. /(...)tripoli4.<X>.<Y>/Env/t4path.ceav512). In particular
it will feed the last three lines about the electron_bremsstrahlung_xs, idt_photon_xs_file, idt_neutron_xs_file
keywords. In case the user wants to use another nuclear data library, the following tool can be used to help with this task
(/(...)tripoli4.<X>.<Y>/CODE/<OS>/tools/Pathfile/migrate-t4path).

<!-- page 29 -->
## 3.2 THE DICTIONARY FILE

The dictionary, or catalogue, file is required for a proper execution of a calculation performed using the TRIPOLI-4® code.
A dictionary contains:
• the path to a directory containing all the cross-section files referred to in the previous chapter;
• the names of the isotopes used to define the material compositions used in the calculation and all the NJOY codes associated
with the isotopes (see specification of material compositions).
• Starting from TRIPOLI-4® version 8, specifications on the calculations of Q-values (see later on).
The dictionary is installed with the tapes and code. Its use should be transparent to the user. However, it can be helpful to understand
the principles involved when connecting libraries or creating new ones.
The first item in the dictionary file is the path to the directory containing the nuclear data files necessary for the simulation. The
code automatically seeks the evaluation files, the pointwise or multigroup cross-section files and the anisotropy files in the directory
(all of which must be present).
For dictionary files to be used with TRIPOLI-4® versions up to 7 (included), the second item in the file is the number of isotopes
contained in the directory. Starting from TRIPOLI-4® version 8, the second item in the file is the number of isotopes contained in
the directory increased by 10000. For instance, if 25 isotopes are present, this item will be 10025.
The following data are present for each isotope:
• the name of the isotope as given in the TRIPOLI-4® code data file (any name is possible and must only be identical to that of
the isotope as used in the composition specifications);
• the material number for neutron cross-sections (which is assigned to each isotope by NJOY):
NJOY(neutron);
• the material number for gamma cross-sections (which is assigned to each isotope by NJOY):
NJOY(gamma);
• the material number for thermal cross-sections. The material number for a thermal cross-section is a combination of NJOY
material numbers. As for the neutron cross-sections, each isotope with thermalization data has a thermal material number
assigned by NJOY: NJOY(therm). The number to be given in the dictionary is, therefore, coded as follows: T4(therm) =
NJOY(neutron) × 10000 + NJOY(therm);
• (only for dictionary files intended to be used with TRIPOLI-4® versions starting from 8) a flag by which the user specifies
whether reaction Q-values are to be computed from mass defect (based on the atomic weights file: flag= 0; this is the
value suggested for most isotopes in the dictionary, and coincides with older versions of TRIPOLI-4®), or read from nuclear
evaluation files. This flag affects the calculations of energy deposition, gas production, DPA and kinematic limits. See section
13.7 and in particular section 13.7.1 for the values of this flag. The flag values chosen by default should only be modified by
an expert user. When the item defining the number of isotopes in the directory is not augmented by 10000, this column of
the dictionary file is ignored (to preserve compatibility with older versions of TRIPOLI-4®). This means that in this case the
Q-values are by default computed from mass defect.
• the name of the file containing the evaluation in the directory.
For the pointwise case, in the absence of thermal or gamma data, or if these types of data are not used in the calculation (in which
case they do not have to be read), these material numbers must be set to -1. In the multigroup case, these numbers must always be
set to -1.
Note: for certain materials, the isotopes required are special isotopes (as a result of different chemical bonds). A frequent case is
that of water, for which a specific hydrogen must be used: H_H2O (or H1_H2O, depending on the name used in the dictionary).
It is, therefore, necessary to use:

<!-- page 30 -->
• hydrogen H_H2O (or H1_H2O) for water;
• hydrogen H_CH2 (or H1_CH2) in certain polymers (polyethylene for instance);
• deuterium D_D2O for heavy water;
• carbon C_G (or C_GRAPHITE) for graphite.
The dictionary file syntax is, therefore, as follows (TRIPOLI-4® versions up to 7 included):
path
number of isotopes
NAME(isotope_1) NJOY(neutron) NJOY(gamma) T4(therm) name(file_1)
...
NAME(isotope_n) NJOY(neutron) NJOY(gamma) T4(therm) name(file_n)
where name(file_i) is the name of the evaluation file in ASCII form.
Starting from TRIPOLI-4® version 8, the dictionary file syntax is instead as follows:
path
number of isotopes + 10000
NAME(isotope_1) NJOY(neutron) NJOY(gamma) T4(therm) FLAG(Q-value) name(file_1)
...
NAME(isotope_n) NJOY(neutron) NJOY(gamma) T4(therm) FLAG(Q-value) name(file_n)
Dictionary of the criticality calculation example of chapter 5, with TRIPOLI-4® version 8
/home/TRIPOLI-4/GALILEE-V0-2.1/JEFF311/T4XS/
10025
FE54 2625 -1 -1 0 jeff311.neutron.Fe54.bcd
FE56 2631 -1 -1 0 jeff311.neutron.Fe56.bcd
FE57 2634 -1 -1 0 jeff311.neutron.Fe57.bcd
FE58 2637 -1 -1 0 jeff311.neutron.Fe58.bcd
CR50 2425 -1 -1 0 jeff311.neutron.Cr50.bcd
CR52 2431 -1 -1 0 jeff311.neutron.Cr53.bcd
CR53 2434 -1 -1 0 jeff311.neutron.Cr53.bcd
CR54 2437 -1 -1 0 jeff311.neutron.Cr54.bcd
NI58 2825 -1 -1 0 jeff311.neutron.Ni58.bcd
NI60 2831 -1 -1 0 jeff311.neutron.Ni60.bcd
NI61 2834 -1 -1 0 jeff311.neutron.Ni61.bcd
NI62 2837 -1 -1 0 jeff311.neutron.Ni62.bcd
NI64 2843 -1 -1 0 jeff311.neutron.Ni64.bcd
N14
725
-1 -1 0 jeff311.neutron.N14.bcd
O16
825
-1 -1 0 jeff311.neutron.O16.bcd
U234 9225 -1 -1 0 jeff311.neutron.U234.bcd
U235 9228 -1 -1 0 jeff311.neutron.U235.bcd

<!-- page 31 -->
U236 9231 -1 -1 0 jeff311.neutron.U236.bcd
U238 9237 -1 -1 0 jeff311.neutron.U238.bcd
H1
125
-1 -1 0 jeff311.neutron.H1.bcd
AL27 1325 -1 -1 0 jeff311.neutron.Al27.bcd
SI
1400 -1 -1 0 jeff311.neutron.Si.bcd
CA
2000 -1 -1 0 jeff311.neutron.Ca.bcd
BE9
425
-1 -1 2 jeff311.neutron.Be9.bcd
NA23 1125 -1 -1 0 jeff311.neutron.Na23.bcd
Here, /home/TRIPOLI-4/GALILEE-V0-2.1/JEFF311/T4XS is the directory where the cross-sections are located, and 25 is the
number of isotopes (plus 10000), each line giving the name, neutron number, photon number (here set to -1 as there are no photon
data), thermal number (here set to -1 as there are no thermal data), Q-value flag, and the name of the evaluation file (neutron) for
each of these isotopes. A Q-value flag 0 means that the reaction Q-values are computed based on the mass defect, a Q-value flag 1
means that the reaction Q-values are read in the evaluation file, and a Q-value flag 2 means that the reaction Q-values are read in
the evaluation file and that special kinematics are applied for the isotope (see sections 13.8, 13.9 and 13.10).
With the above dictionary, the links are only created for neutron cross-sections since the photon and thermalization cross-sections
are not loaded (indices set to -1).
Mixed evaluations
If cross-sections found in two directories are to be used (for example, in two evaluations), the root may be changed and the path
included in the file name:
/home/TRIPOLI-4/GALILEE-V0-2.1/
10006
FE54 2625 -1 -1 0 JEFF311/T4XS/jeff311.neutron.Fe54.bcd
FE56 2631 -1 -1 0 JEFF311/T4XS/jeff311.neutron.Fe56.bcd
FE57 2634 -1 -1 0 JEFF311/T4XS/jeff311.neutron.Fe57.bcd
FE58 2637 -1 -1 0 JEF2/T4XS/jef2.neutron.Fe58.bcd
CR50 2425 -1 -1 0 JEF2/T4XS/jef2.neutron.Cr50.bcd
BE9
425
-1 -1 2 JEFF311/T4XS/jeff311.neutron.Be9.bcd
Using dosimetry or activation evaluations
Dosimetry and activation evaluations provide only neutron cross-sections data but neither angular nor energy distributions data.
These evaluations can thus be used only to request reaction rates on virtual nuclei which are not part of the transport simulation
(see section 13.2). Starting from TRIPOLI-4® version 8, the user can request reaction rates from dosimetry evaluations (such as
International Reactor Dosimetry Files 2002) or activation evaluations (such as European Activation File 2003), without any change
in the dictionary file (as was the case with previous versions). The corresponding names of the isotopes (which can be found in
the dictionary) are ended by _D (e.g FE54_D) for the IRDF2002 case and by _A (e.g FE54_A) for the EAF2003 case. Moreover,
when cross-section data are only present as production of radioactive elements data in these evaluations, TRIPOLI-4®, starting
from version 8, reads and handles them as standard cross-sections.
