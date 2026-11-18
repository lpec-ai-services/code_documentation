# THE HOMOGENIZATION COMMAND
<!-- source PDF pages 285-286 -->

<!-- page 285 -->
Chapter 21
THE HOMOGENIZATION COMMAND
With the TRIPOLI-4® code, it is also possible to homogenize a composition. This option is useful for calculating
cross-sections with a motif of one or more fuel assemblies in an infinite medium. It is helpful for making
comparisons with lattice codes. It is necessary to request the cross-sections in a grid with a small number of
groups to obtain adequate statistical accuracy for the cross-sections (typically 0.5%). The command used is
HOMOGENIZE.
When this option is requested, the code generates homogenized multigroup cross-sections in a file. A second
TRIPOLI-4® calculation can then be made with these cross-sections.
The syntax is as follows:
HOMOGENIZE
DIFFUSION 1
NBMAT nb(compo)
name(compo-1)
VOLUME LIST nb(volu)
num(vol1) ...num(volN)
OUTPUT ALL
name(grid)
...
name(compo-n)
VOLUME LIST nb(volu)
num(vol1) ...num(volN)
OUTPUT ALL
name(grid)
FILE filename
END_HOMOGENIZE
where:
• nb(compo) is the number of compositions to be homogenized;

<!-- page 286 -->
• name(compo-i) is the name of the i-th composition to be homogenized. The user can give any name
for this compostion;
• num(vol1) ...num(volN) is the list of the nb(volu) volumes in the composition;
• name(grid) is the energy grid on which the composition is homogenized. The grid must have previously
been defined in the GRID_LIST command;
• filename is the name of the file in which the homogenized multigroup cross-sections are stored, plus
the extension -homog. By default, the filename is -homog alone.
A subsequent TRIPOLI-4® calculation can then be made using these cross-sections. All that is required is to
declare that the compositions are made using cross-sections from the file generated using the command (see
COMPOSITION cross-section).
Currently, the total cross-sections Σt, the absorption cross-section Σa, and the product of the fission crosssection
and the number of fission neutrons νΣf are calculated using this command. These outputs are consistent
with the APOTRIM format of APOLLO2.
Keyword NBMAT is required (although not present in version 4.1).
By indicating OUTPUT ALL, the code supplies the self-shielded cross-sections for the compositions to be
homogenized. Output is directed to the conventional output file, but is not taken up into the -homog extension
cross-section file.
When DIFFUSION 1 is indicated, the code outputs scattering coefficients. There must, however, be only one
medium to be homogenized, and it must be infinite (consequently, reflection from all the boundary surfaces
of the geometry is required). Important: for the time being the results are not guaranteed and should not be
used in project studies.
Important: The homogenization command is not allowed in parallel mode.
