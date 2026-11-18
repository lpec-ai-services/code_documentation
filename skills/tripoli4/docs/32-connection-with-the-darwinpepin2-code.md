# CONNECTION WITH THE DARWIN/PEPIN2 CODE
<!-- source PDF pages 390-391 -->

<!-- page 390 -->
Chapter 32
CONNECTION WITH THE DARWIN/PEPIN2
CODE
It is possible to prepare an input deck for the DARWIN-PEPIN2 code [99], in order to perform an activation
calculation. Creation of a deck for fuel depletion calculations is not yet implemented.
The syntax is as follows:
PEPIN
GRID name(grid)
SCORE_MODE <MODE>
HISTORY nb(steps)
time(init) <UNIT>
time(1) <UNIT> value(1)
...
time(final) <UNIT> value(final)
VOLUME nb(volu)
num(vol1)...num(voln)
END_PEPIN
• The energy grid name must correspond to a known grid: “3_GRS”, “SAILOR”, “APOLLO_99”,
“GAM2”, “APOLLO_172”, “APOLLO_281” or “TRIPOLI_315”.
• ISOTOPES means that the composition for INTERPEP is the one that was input in the TRIPOLI-4® data
set. By default, the values for module INTERPEP are rebuilt according to the natural composition of the
materials.
• <MODE> = TRACK or COLL, indicating the type of flux (volume related) for calculating file INTERPEP.
This is because, in a simulation, it is possible to calculate the scores for a given volume using the “track
length” estimator and the “collision” estimator. The keyword is used to indicate which type of estimator
is retained (there must, therefore, be a score with this estimator) for use in the creation of the file for
INTERPEP.

<!-- page 391 -->
• nb(steps) is the number of steps (for burnup) plus the number of intersteps (relating to a zero flux).
• The initial time must be indicated, then the final time of the interval i and the value by which the flux
will be multiplied during the interval, e.g.,
0 SECO
30 SECO 1
1 MINU 0
3 MINU 4
In this case, for the interval (0 - 30 s), the flux is multiplied by 1, during the interval (30 s - 1 min) by 0
(interstep), then by 4 for (1 - 3 min).
• The units <UNIT> possible are SECO (s), MINU (min), HOUR (h), YEAR (year).
• This is followed by the number of volumes for which results are required, and a list of them.
• A filename interpep and a filename spallation are created, and the outputs are given by second and
by unit volume as the volumes are indicated in VOLSURF or calculated and allocated by CALCULATION
(default 1).
