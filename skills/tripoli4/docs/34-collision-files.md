# COLLISION FILES
<!-- source PDF pages 400-402 -->

<!-- page 400 -->
Chapter 34
COLLISION FILES
This command makes it possible, during a simulation, to store as a binary file the attributes of particles, i.e.,
particle type (currently neutron or photon), the direction, time, and weight of particles passing through given
volumes, the crossing of given boundaries or involvement in collisions in any of the fixed volumes.
Once the simulation is completed, the data stored can be read in order to rapidly calculate new scores. The
scores must, of course, depend on only the information stored. For instance, if all the collision points in a
volume have been stored, it is then possible, in a later phase, to calculate all the reaction rates by the collision
estimator in the volume.
All types of collection and response functions can be reproduced from the dumped records. However, the
scores using the sub-command FILTER, which enables only the particles which pass through certain volumes
to be counted, are not compatible with the collision files. (It would be necessary to store the history of the
particles, which would be costly in terms of memory and disk usage.)

<!-- page 401 -->
## 34.1 CREATION OF A COLLISION FILE

The syntax is as follows for the collision file creation phase:
COLLISION_TAPE
CREATION
number of files
name of file_1
<PARTICLE_TYPE>
*
FRONTIER
nbzones
Emax(1) Emin(1) volume1 volumebis1
...
Emax(nbzones) Emin(nbzones) volumenbzone volumebisnbzone
*
VOLUME
nbzones
Emax(1) Emin(1) volume1
...
Emax(nbzones) Emin(nbzones) volumenbzone
*
CELL
nbzones
Emax(1) Emin(1) volume1
depth1 ni(1) nj(1) nk(1) ... ni(depth1) nj(depth1) nk(depth1)
...
Emax(nbzones) Emin(nbzones) volumenbzones
depthnbzones ni(nbzones) nj(nbzones) nk(nbzones) ...
ni(depthnbzones) nj(depthnbzones) nk(depthnbzones)
name of file_2
...
name of file_n
END_CREATION
END_COLLISION_TAPE
The meanings of the fields are as follows:
• Number_of_files corresponds to the number of files to be created.
• <PARTICLE_TYPE> corresponds to the type of particles for which information is stored.
• This is followed by an indication of the type of geometrical zone affected by the storage, i.e., FRON-
TIER, VOLUME, and CELL.
• The number of geographical zones where information is stored.
• Emax and Emin correspond to the maximum and minimum energies for the information stored.

<!-- page 402 -->
• A list is then given of the geometrical elements for which information is stored. In the case of boundaries,
it should be borne in mind that each boundary is defined by a volume-number pair, and there is, therefore,
an equal number of volume-number pairs to be defined as there are declared storage zones. In the case
where the geometrical zone is a lattice cell, it is necessary to specify the volume number and then, as
in the score command (see Section 15.7), it is necessary to specify the depth of the lattice one likes to
access and, finally, the number of the cell concerned for each depth number.
The user can create as many files as desired.

## 34.2 USE OF A COLLISION FILE

The use of data stored in a file is introduced using the keyword EXPLOITATION.
The syntax is as follows:
COLLISION_TAPE
EXPLOITATION
number of files
name of file 1
...
name of file n
END_EXPLOITATION
END_COLLISION_TAPE
The data are, therefore:
• the number of files to be used,
• a list of filenames to be used.
All other commands of the code, and their meanings, remain unchanged. In particular, the SCORE command
can be used to obtain new reaction rates with little cost.
