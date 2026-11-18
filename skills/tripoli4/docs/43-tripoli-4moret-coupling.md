# TRIPOLI-4/MORET COUPLING
<!-- source PDF pages 490-491 -->

<!-- page 490 -->
Chapter 43
TRIPOLI-4/MORET COUPLING
The MORET code is developed by the IRSN and simulates the transport of neutrons in three dimensions
by the means of the Monte Carlo method. TRIPOLI-4 and its visualisation tool T4G can use the MORET
code to process geometrical calls and boundary conditions. The integration of MORET into TRIPOLI-4 was
designed so that minimal modifications are required in data files. The geometry part of the MORET code
is linked on the fly in the TRIPOLI-4 code in order to process all geometry calls in place of the TRIPOLI-4
geometrical functions. The geometry functions of MORET must thus be made available to TRIPOLI-4 by
means of a dynamic library. To inform TRIPOLI-4 of the location of the MORET library on the system, the
user must fill the LD_LIBRARY_PATH appropriately.
We will give the keywords used to declare a block to be processed by the MORET code. However, users will
need to refer to the MORET documentation for the syntax inside the blocks.

## 43.1 USING A MORET GEOMETRY

To invoke MORET for the geometry, the keyword MORET_GEOMETRY must be placed before the geometry
declaration block inside the data file. Upon reading that keyword, TRIPOLI or T4G will call the MORET
geometry reader. The keyword ENDG must be used to end the geometry.
The syntax block is then
MORET_GEOMETRY
file(name)
ENDG

<!-- page 491 -->
## 43.2 USING MORET BOUNDARY CONDITIONS

As with a native TRIPOLI-4 geometry, the MORET geometry allows for boundary conditions to be applied.
The command used for this is as follows:
MORET_LIMIT
FACE F_<iface1>:V_<ivolu1>:M_<imodule1> <condition_type1>
FACE F_<iface2>:V_<ivolu2>:M_<imodule2> <condition_type2>
...
ENDB
Only reflection boundary conditions and the default leakage boundary conditions are available in the version
12 of TRIPOLI-4. The condition_type is 1 for the reflection.
