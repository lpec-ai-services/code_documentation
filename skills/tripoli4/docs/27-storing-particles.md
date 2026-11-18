# STORING PARTICLES
<!-- source PDF pages 349-351 -->

<!-- page 349 -->
Chapter 27
STORING PARTICLES
This command is used to store the characteristics (energy, position, direction, weight) for the particles
crossing a given list of boundaries.
• For a given dump file, the user can request a list of boundaries.
• An additional keyword is required in order to set a maximum for the size of the dump file in Mega bytes.

<!-- page 350 -->
The syntax is as follows:
STORAGE
nb(items-stored)
filename(1)
LIMIT_SIZE nb_Mo(1)
<PARTICLE>
Emax Emin
< FILTER > VOLU LIST nb1(volu)
volume(1) volume(2) ...volume(nb1)
FRONTIER LIST nb1(boundaries)
num1,1(vol1) num1,1(vol2)
...
num1,i(vol1) num1,i(vol2)
num1,nb1(vol1) num1,nb1(vol2)
...
filename(n)
LIMIT_SIZE nb_Mo(n)
<PARTICLE>
Emax Emin
< FILTER > VOLU LIST nbn(volu)
volume(1) volume(2) ...volume(nbn)
FRONTIER LIST nbn(boundaries)
numn,1(vol1) numn,1(vol2)
...
numn,i(vol1) numn,i(vol2)
numn,nbn(vol1) numn,nbn(vol2)
END_STORAGE
where:
• nb(items-stored) is the number of files to be created;
• filename(i) is the beginning of the name of a series of dump files: the name filename(i) is suffixed
by "_1_.stock". When this dump file is written, and once the size of nb_Mo(i) has been reached, the
code automatically generates a new dump file with the name: filename(i), suffixed by "_2_.stock", and
so forth, as many times as necessary in order to store all of the particles during the simulation.
• nb_Mo(i) the maximum size for a dump file, given in Mega bytes.
• <PARTICLE> is the type of particles to be stored (currently, only NEUTRON and PHOTON are available).
The option ALL_PARTICLE may be used in order to store both the neutrons and photons in the same file).
The particles are only written for the interval [Emax,Emin];
• <FILTER> is optional and may have the values FILTER_OR, FILTER_AND, FILTER_SEQ, FILTER_TARGET.
The filter is thereafter defined by inputting a list of volume numbers. The different possible filters are
defined in the same way as for the scores (see chapter 15 for information on scores).

<!-- page 351 -->
• num(vol1) and num(vol2) are the volumes that define the boundary in the direction from 1 toward 2
for the file to be created.
The file contains the following data in the given order:
• a header showing the boundary list, the energy bounds Emax and Emin, the type of information to be
stored for each particle, as well as the general simulation data (number of batches, size of the batches,
type of particles, intensity of the source, and the simulation mode ("SHIELDING", "CRITICALITY" or
"FIXED_SOURCES_CRITICALITY")).
• markers showing the beginning and end of each batch: "BEGIN_OF_BATCH i" and "END_OF_BATCH i"
followed by the statistic weight of the batch: "WEIGHT_OF_BATCH Wb".
• the particles are stored between these batch markers. For each particle stored, the following information
is given:
– the name of the particle,
– the energy E in MeV,
– (x,y,z), defining the position,
– (u,v,w), defining the direction,
– Wt, the weight of the particle.
Note : the format of this file has changed over the TRIPOLI-4 versions.
It must also be noted that the storage of particles may also be requested using the SCORE command in the case
of a FLUX_PT ("next-event" type) estimator on a target surface (see chapter 15).
These outputs can be used to generate sources for a calculation with another code or with TRIPOLI-4 (in the
case of a source resulting from source files for the global / local zooming approach, see paragraph 12.6.2 of
the chapter on sources).
