# DEFINING COMPOSITIONS
<!-- source PDF pages 127-136 -->

<!-- page 127 -->
Chapter 10
DEFINING COMPOSITIONS
Commands are introduced using the keyword COMPOSITION.
A composition in the TRIPOLI-4® sense is the cross-section type data used in particle transport for the composition
in question, the temperature of the composition, and the name given to the composition by the user.
The data necessary for each type of cross-section are then required.
The types of cross-sections currently available in TRIPOLI-4® are:
• pointwise cross-sections derived from evaluation in ENDF format;
• multigroup and homogenized cross-sections (currently the self-shielded cross-sections of APOLLO2
[95] in APOTRIM format and those calculated by TRIPOLI-4® after a homogenization process);
• multigroup cross-sections in GENDF format, created by the GROUPR module of the NJOY code.
If the TRIPOLI-4®-NJOY coupling option is specified when the TRIPOLI-4® code is run (option -j, see
chapter 1), the temperatures may be any temperatures desired by the user, provided that the files exist for
cross-sections at 0K temperatures exist. Otherwise, the temperatures may be any temperatures desired by the
user, provided that the cross-section files exist at these temperatures (see section 10.4).
The names of the compositions are up to the user’s discretion. The names of the isotopes comprising these
compositions must be chosen from the names available in the dictionary file or, in the case of a natural
element, must include the suffix -NAT. With this option, the existence of the nuclear data file for the natural
element is checked. If this check fails, TRIPOLI-4® will use the isotopic abundance file (see chapter 3) to
split the natural element into its naturally occurring isotopes. In case the user wants to work, exclusively, with
the isotopic abundance file, he has to use -NAT-SPLIT instead.

<!-- page 128 -->
The general syntax used to define compositions is as follows:
COMPOSITION
nb(compositions)
*
FILE
<ELECTRONIC_PROPERTIES>
temperature name(compo)
filename
*
POINT_WISE
<ELECTRONIC_PROPERTIES>
temperature name(compo)
Composition data
...
*
DENSITY
<ELECTRONIC_PROPERTIES>
temperature name(compo)
Composition data
...
*
MULTIGROUP_HOMOGENEOUS
temperature name(compo)
Composition data
...
*
MULTIGROUP
temperature name(compo)
Composition data
...
*
MULTIGROUP DENSITY
temperature name(compo)
Composition data
...
END_COMPOSITION
where:
• FILE indicates that the definition for the material is located in the file named filename, which includes
the path, if necessary. A file of this type contains a list of the materials in a format accepted by TRIPOLI-
4®. The syntax of such a file corresponds to that of the COMPOSITION command; however, it does not
use the initial and final keywords COMPOSITION-END_COMPOSITION, it does not indicate the number of
nb(compositions), and it does not call any compositions from another file;
• POINT_WISE is a keyword that initializes pointwise cross-sections in ENDF format by supplying the
number of atoms per cm3 (warning: this is true even if the lengths are given in another unit than cm);
• DENSITY is a keyword that initializes pointwise cross-sections in ENDF format by entering the density
(in g/cm3) and mass fractions or number of atoms;
• MULTIGROUP_HOMOGENEOUS is a keyword that initializes the homogenized multigroup cross-sections;

<!-- page 129 -->
• MULTIGROUP codes the multigroup cross-sections in GENDF format by providing the number of atoms
per cm3;
• MULTIGROUP DENSITY is a keyword that initializes the multigroup cross-sections in GENDF format by
entering the density (in g/cm3) and the mass fractions;
• temperature is an integer (the temperature is expressed in Kelvin).
• <ELECTRONIC_PROPERTIES> is an optional keyword that defines electron and positron transport properties
(see section 10.1)
For pointwise cross-sections, one can define compositions using both formats FILE, POINT_WISE and
DENSITY. For multigroup cross-sections, the formats FILE, MULTIGROUP and MULTIGROUP DENSITY can be
mixed. Nonetheless, it is not allowed to mix pointwise compositions with multigroup compositions.

## 10.1 POINTWISE CROSS-SECTIONS IN ENDF FORMAT

Compositions with pointwise cross-sections are identified using:
• the number of isotopes making up the composition;
• a list of the isotopes.
For each isotope, it is necessary to specify:
• the name of the isotope is given in the dictionary file or, in the case of a natural element, the name of
the isotope is defined in the isotopic natural abundance file (see chapter 3) to which the suffix -NAT is
appended (for example C-NAT for natural carbon). The user can force TRIPOLI-4® to work with the
isotopic abundance file using -NAT-SPLIT instead of -NAT;
• the number of atoms per 10−24 cm3 or the density.
All the isotopes with the same composition have the same temperature.
10.1.1
DEFINING COMPOSITIONS BY SUPPLYING THE NUMBER OF ATOMS PER 10−24 CM3
The syntax for a composition of this type is as follows:
POINT_WISE
<ELECTRONIC_PROPERTIES>
temperature
name(compo)
nb(isotopes)
isotope(1) nb-atom(1)
...
isotope(n) nb-atom(n)

<!-- page 130 -->
where:
• <ELECTRONIC_PROPERTIES> is an optional keyword that defines electronic transport properties,
significant only in PHOTON ELECTRON POSITRON calculation mode. It overwrites the default choice of
TRIPOLI-4®. The possible keywords are :
– GASNTP for a gas at normal temperature and pressure conditions (0°C - 1 atm)
– CONDUCTOR for an electric conductor
– NONPOLARIZABLE for all other condensed materials (liquid or solid)
• temperature is the temperature in kelvin which must be an integer and entered as such without dots or
commas (e.g., “300” not “300.”);
• name(compo) is the name chosen by the user for the composition to be defined;
• nb(isotopes) is the number of isotopes in the composition, followed by a list of the isotopes entered,
each with its name isotope(i) in the library and the number of atoms nb-atoms(i) per 10−24 cm3 in
the composition.
Note: if the name VOID is used for a material, the use of a variance reduction technique will establish the
value of k at half the minimum of the values of k of the other materials (see chapter 17 on variance reduction
techniques).

### 10.1.2 DEFINING COMPOSITIONS BY ENTERING THE DENSITY (IN G/CM3)

The syntax for a composition of this type is as follows:
DENSITY
<ELECTRONIC_PROPERTIES>
temperature
name(compo)
density
nb(isotopes)
isotope(1) frac-mass(1)
...
isotope(n) frac-mass(n)

<!-- page 131 -->
or
DENSITY
<ELECTRONIC_PROPERTIES>
temperature
name(compo)
density NB_ATOM
nb(isotopes)
isotope(1) nb_molecular(1)
...
isotope(n) nb_molecular(n)
where:
• <ELECTRONIC_PROPERTIES> is an optional keyword that defines electronic transport properties,
significant only in PHOTON ELECTRON POSITRON calculation mode. It overwrites the default choice of
TRIPOLI-4®. The possible keywords are :
– GASNTP for a gas at normal temperature and pressure conditions (0°C - 1 atm)
– CONDUCTOR for an electric conductor
– NONPOLARIZABLE for all other condensed materials (liquid or solid)
• temperature is the temperature in kelvin which must be an integer and entered as such without dots or
commas (e.g., “300” not “300.”);
• name(compo) is the name chosen by the user for the composition to be defined;
• density is the density;
• NB_ATOM allows the user to define the composition as a molecule.
• nb(isotopes) is the number of isotopes in the composition, followed by a list of the isotopes entered,
each with its name isotope(i) in the library and their mass fraction frac-mass(i) or, in case of
NB_ATOM keyword, the number of atoms (or isotopes) nb_molecular(i).
Note: if the name VOID is used for a material, the use of a variance reduction technique will establish the
value of k at half the minimum of the values of k of the other materials (see chapter 17 on variance reduction
techniques).

<!-- page 132 -->
## 10.2 MULTIGROUP HOMOGENIZED CROSS-SECTIONS

Multigroup homogenized cross-sections can currently only be self-shielded cross-sections derived from
APOLLO2 in APOTRIM format and those of TRIPOLI-4® (created using the HOMOGENIZE command).
10.2.1
SELF-SHIELDED
HOMOGENIZED
MULTIGROUP
CROSS-SECTIONS
FROM
APOLLO2 AND TRIPOLI-4®
APOTRIM format compositions are defined using:
• burnup;
• the name of the library containing the self-shielded homogenized cross-sections.
The composition must be specified in an APOTRIM format cross-section file with the same name as that of
the TRIPOLI-4® data file, at the same temperature and burnup. Syntax is, therefore, shown in the box below.
MULTIGROUP_HOMOGENEOUS
temperature
name(compo) APOLLO2
burnup
file(APOLLO)
where:
• temperature is the temperature of the composition, expressed in degrees Kelvin. The temperature is an
integer and must be entered as such (for example, “300” rather than “300.”). It must correspond to the
temperature given in the cross-section file, which is given in degrees Celsius (which must be a relative
integer: the difference between the two values must be 273);
• name(compo) is the name of the composition in the file;
• <TYPE_SECTION> equals APOLLO2 or T4HOMOT4;
• burnup is the burnup and must correspond to the value read from the APOTRIM file. This value must be
an integer (this value is 0 when TRIPOLI-4® cross-sections are used);
• file is the name of the APOLLO or TRIPOLI-4® cross-section file. If a file is not found in the directory
from which the executable is run, it is necessary to add the path. It is recommended that absolute path
be used (e.g., /home/user/directory/file).
Note: The maximum anisotropy order taken into account by TRIPOLI-4® in APOTRIM format files is order
3 in the Legendre polynomial expansion (P3). The method is based on the Nonequally Probable Step Function
Representation which is described in reference [77].

<!-- page 133 -->
## 10.3 MULTIGROUP CROSS-SECTIONS IN GENDF FORMAT

The syntax for a multigroup composition is as follows:
MULTIGROUP
temperature
name(compo)
nb(isotopes)
isotope(1) nb-atome(1)
...
isotope(n) nb-atome(n)
or
MULTIGROUP DENSITY
temperature
name(compo)
density
nb(isotopes)
isotope(1) frac-mass(1)
...
isotope(n) frac-mass(n)
For an explanation of the fields in the above syntax, refer to the pointwise cross-sections case, section 10.1.
Use of multigroup cross-sections requires one of the following command line options:
-s GENDF or -s TABPROB_GENDF (see chapter 1).

## 10.4 TRIPOLI-4®-NJOY COUPLING

If a cross-section at temperature newtemp is needed and cannot be found in the available libraries or in the
directory containing the user-defined cross sections (see chapter 3), TRIPOLI-4® can create the corresponding
files automatically. To accomplish this the user must use the NJOY code (version 99), which is called directly
by TRIPOLI-4® using the execution option -j (see chapter 1). The input deck provided to TRIPOLI-4® may
be a simplified one, used specifically to generate the cross-section files, or else it may be the input deck for
the envisioned simulation. TRIPOLI-4® first calls NJOY (BROADR at newtemp K, errthn = 0.001, using
reconstructed files at 0K, i.e., using the provided bcd.pendf.0) then TRIPOLI-4® calls its own routines. The
created files are put into the directory specified by the user in the path file (see chapter 3) and may be reused
in the future.
Once the file at the temperature newtemp has been created in the user repertory, the option -j is no longer
needed for subsequent simulations at this temperature.
It should be noted that only pointwise neutron
cross-sections are created by the option -j. Hence:

<!-- page 134 -->
• the probability table files produced by the CALENDF code and the multigroup files generated by the
GROUPR module of NJOY are not created by the option -j. All calculations using the new temperatures
will then be performed without probability tables, even if the option TABPROP is specified.
• The files for bonded elements are not taken into account. Calling a temperature for a bonded element
that is not present in the files will result in an error. In order to avoid this, the user can create a link to
the file with the closest temperature to the bonded element in question.
• This option should exclusively be run in mono-processor mode. If any run in parallel should accidentally
occur, the created cross-section files must be cleaned and the run should be executed again in monoprocessor
mode.
Note: instructions for compiling the NJOY code are provided in the installation files of the TRIPOLI-4® code.

<!-- page 135 -->
Defining compositions for the criticality calculation example in chapter 5
with pointwise cross-sections
COMPOSITION 4
POINT_WISE 300 INOX_STEEL
13
FE54 3.6805E-3 FE56 5.6188E-2 FE57 1.2943E-3
FE58 1.7176E-4 CR50 7.4596E-4 CR52 1.3832E-2
CR53 1.5397E-3 CR54 3.7545E-4 NI58 5.6052E-3
NI60 2.0697E-3 NI61 8.7556E-5 NI62 2.7564E-4
NI64 6.8909E-5
POINT_WISE 300 AIR
2
N14 1.900E-5 O16 9.7457E-6
POINT_WISE 300 SOLUTION_U
11
U234 2.5554E-6 U235 2.8247E-4 U236 8.7585E-7
U238 2.7877E-5 FE54 5.6745E-8 FE56 8.6631E-7
FE57 1.9955E-8 FE58 2.6481E-9 N14 1.8650E-3
O16 3.6262E-2 H1 6.1314E-2
POINT_WISE 300 CONCRETE
6
H1 1.3740E-2 O16 4.5908E-2 AL27 1.7380E-3
SI 1.6608E-2 CA 1.4989E-3 NA23 2.7780E-3
END_COMPOSITION
Defining compositions for the criticality calculation example
using multigroup homogenized cross-sections
COMPOSITION 4
MULTIGROUP_HOMOGENEOUS 300 INOX_STEEL APOLLO2
0
/home/am/APOLLO2/resultats/bi.ur2cyl86
MULTIGROUP_HOMOGENEOUS 300 AIR APOLLO2
0
/home/am/APOLLO2/resultats/bi.ur2cyl86
MULTIGROUP_HOMOGENEOUS 300 SOLUTION_U APOLLO2
0
/home/am/APOLLO2/resultats/bi.ur2cyl86
MULTIGROUP_HOMOGENEOUS 300 CONCRETE APOLLO2
0

<!-- page 136 -->
/home/am/APOLLO2/resultats/bi.ur2cyl86
END_COMPOSITION
Defining compositions for the criticality calculation example by calling a file
COMPOSITION 4
FILE 300 INOX_STEEL
/home/am/catalogue
FILE 300 AIR
/home/am/catalogue
FILE 300 SOLUTION_U
/home/am/catalogue
FILE 300 CONCRETE
/home/am/catalogue
END_COMPOSITION
with, for example, the following /home/am/catalogue file:
POINT_WISE 300 INOX_STEEL
13
FE54 3.6805E-3 FE56 5.6188E-2 FE57 1.2943E-3
FE58 1.7176E-4 CR50 7.4596E-4 CR52 1.3832E-2
CR53 1.5397E-3 CR54 3.7545E-4 NI58 5.6052E-3
NI60 2.0697E-3 NI61 8.7556E-5 NI62 2.7564E-4
NI64 6.8909E-5
POINT_WISE 300 AIR
2
N14 1.900E-5 O16 9.7457E-6
POINT_WISE 300 SOLUTION_U
11
U234 2.5554E-6 U235 2.8247E-4 U236 8.7585E-7
U238 2.7877E-5 FE54 5.6745E-8 FE56 8.6631E-7
FE57 1.9955E-8 FE58 2.6481E-9 N14 1.8650E-3
O16 3.6262E-2 H1 6.1314E-2
MULTIGROUP_HOMOGENEOUS 300 CONCRETE APOLLO2
0
/home/am/APOLLO2/resultats/bi.ur2cyl86
