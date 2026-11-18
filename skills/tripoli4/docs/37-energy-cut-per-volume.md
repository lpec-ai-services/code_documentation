# ENERGY CUT PER VOLUME
<!-- source PDF pages 419-420 -->

<!-- page 419 -->
Chapter 37
ENERGY CUT PER VOLUME
An energy cut can be set per volume for each particle type. This feature allows to avoid particle tracking in
cells of less physical interest, in particular in the case of electron/positron transport.
The general syntax is as follows :
VOLENERCUT
<TYPE_OF_PARTICLES>
ALL default_energy_cut
numvol(1) energy_cut(1)
...
numvol(n) energy_cut(n)
...
END_VOLENERCUT
where :
1. <TYPE_OF_PARTICLES> can be NEUTRON, PHOTON, ELECTRON or POSITRON
2. ALL default_energy_cut sets a default energy cut for all volumes
The default energy cut is overwritten by all following energy threshold definitions for a given volume.
The following example sets an energy threshold on electrons of 10 MeV for all volumes except 10 and 11
where the threshold is 5 MeV and an energy threshold on photons of respectively 1.0 and 0.5 MeV for
volumes 10 and 13 (all others volumes have the threshold given in SIMULATION command).
VOLENERCUT
ELECTRON
ALL 10.0

<!-- page 420 -->
10
5.0
11
5.0
PHOTON
10
1.0
13
0.5
END_VOLENERCUT
