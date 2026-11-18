# TRIPOLI-4/ROOT COUPLING
<!-- source PDF pages 410-418 -->

<!-- page 410 -->
Chapter 36
TRIPOLI-4/ROOT COUPLING
ROOT is an object oriented software package used for processing and analyzing data and has been developed
by the CERN. More information on this software is available on the ROOT website at the following URL:
http://root.cern.ch/ . This chapter illustrates the different possibilities offered by coupling TRIPOLI-4® and
ROOT.

## 36.1 INSTALLATION PROCEDURE

In order to use the functionalities afforded by ROOT, it is first necessary to install the software itself. The
instructions for this are found on the website mentioned, above. TRIPOLI-4® version 12 is coupled with
ROOT version 6.12.06-90-g4816da3.
The TRIPOLI-4® code must then be compiled using the --enable-root option as follows:
./configure --enable-root
make
Be sure that the ROOT environment variables ($ROOTSYS, $LD_LIBRARY_PATH, and $PATH) have been
properly defined (as indicated on the CERN website) before attempting this.

## 36.2 USING A ROOT GEOMETRY

### 36.2.1 DEFINING THE GEOMETRY

The TRIPOLI-4® code is capable of using a geometry defined with ROOT. Constructing a geometry input
deck using ROOT is described in great detail in the chapter "The Geometry Package" of the ROOT user’s
manual. Once the geometry has been entered, TRIPOLI-4® can use ROOT to navigate in it.
It should be noted that throughout the TRIPOLI-4® input deck we no longer allude to volumes by their
numbers but by their names. The name of a volume is given by its path followed by its occurrence number.
For example, if in the definition of a ROOT geometry there are two occurrences of volume B in volume A, then
volume A will be designated as /A_1, volume B as /A_1/B_1, and the second occurrence of B as /A_1/B_2
. In addition, the GEOMCOMP command is no longer required: in creating a ROOT geometry, the user must
associate a composition name, as it is defined in the COMPOSITION command, for each ROOT volume.
The ROOT geometry can be entered either via a file or directly via C++ or Python code within the

<!-- page 411 -->
ROOT_GEOMETRY directive.

#### 36.2.1.1 Defining the geometry via a file

There are 4 different possibilities to specify a ROOT geometry via a file:
• a ROOT geometry file. In order to do this, the user must save his or her TGeoManager in a ROOT file.
• a ROOT script (with extension .C) interpreted on-the-fly
• a ROOT script (with extension .C) first compiled and then executed on-the-fly
• a PyROOT script (ROOT with Python bindings)
The user must then use the following syntax block to replace the command block GEOMETRY.
ROOT_GEOMETRY
file(name)
END_ROOT_GEOM
where file(name) can be :
• a file name with extension .root
• a ROOT script with extension .C to be interpreted on-the-fly
• a ROOT script with extension .C+ to be compiled and then executed on-the-fly. This should be faster
than the previous option.
• a PyROOT script (reactor physics templates can be used if the $PYTHONPATH environment variable
is properly set)

<!-- page 412 -->
#### 36.2.1.2 Defining the geometry directly in C++ or Python code

For quality insurance purposes, another way of defining the ROOT geometry has been made available to users.
It consists in defining the geometry directly via C++ or Python code embedded in the ROOT_GEOMETRY
directive of the TRIPOLI-4® input deck, preceded and followed by the keyword CPP_ROOT_GEOM or
PYTHON_ROOT_GEOM . Such a geometry definition appears like this in the input deck (for a C++ example
):
ROOT_GEOMETRY
CPP_ROOT_GEOM
gSystem →Load("libGeom");
TGeoManager *mgr = new TGeoManager("Geom","composite shape example");
TGeoMaterial * neutre = new TGeoMaterial("NEUTRE",
mgr→GetElementTable()→GetElement(0),1);
...
...
mgr→Close();
CPP_ROOT_GEOM
END_ROOT_GEOM
Starting from TRIPOLI-4 version 10, it is no more necessary to export the ROOT geometry in a ROOT file and
then specify the same ROOT file just after the closing CPP_ROOT_GEOM or PYTHON_ROOT_GEOM
keyword. The TGeoManager object is built on-the-fly and directly used in the simulation.
Also, it is important to be aware that such an input deck does not allow to embed complex set of multiple
C++ or Python class and files and shall therefore be restricted to simple geometries declared in a unique file.

<!-- page 413 -->
### 36.2.2 DEFINING BOUNDARY CONDITIONS

As with a native TRIPOLI-4® geometry, the ROOT geometry allows for boundary conditions to be applied.
The command used for this is as follows:
ROOT_LIMIT
name(vol1) name(vol1’) <TYPE_CONDITION>
...
name(voln) name(voln’) <TYPE_CONDITION>
END_ROOT_LIMIT
where <TYPE_CONDITION> may be equal to one of the following values: REFLECTION, TRANSLATION (works
only on box), or COSINUS. Unlike in native TRIPOLI-4® geometry, the boundary conditions in a ROOT
geometry are oriented (signed) and are attached to surfaces where two volumes are in contact. As such,
the boundary condition <TYPE_CONDITION> is applied to particles transported from volume name(voln) to
volume name(voln’). One can also set name(voln’) to *ALL*, in which case the boundary condition is
applied to all particles that penetrate the volume name(voln) (warning: unlike in the first case, the use of
*ALL* keyword reverses the logic used by the boundary condition concerning the sequence of input volumes).
In the case of the rotation boundary condition, the syntax is as follows:
num(vol1) num(vol1’) ROTATION Xc Yc Zc ux uy uz α
see boundary limit chapter 9 for parameters details if needed.

### 36.2.3 DEFINING A SCORE

In the case of a score on a volume it is possible to ask for the scores on all the volumes who are inside it
without having to ask for them one by one.
Example:
2 TRACK
GRID GRID_ABSORPTION
VOLUME LIST 1 /TOP_1/boite_1/*
Response 2 is requested with estimator TRACK for the grid indicated in all the volumes who are declared (in
the ROOT geometry definition) as inside the "/TOP_1/boite_1" volume.
Notes: the sum of the results can be made by using the keyword SUM instead of LIST.

<!-- page 414 -->
### 36.2.4 HOW TO CHECK A ROOT GEOMETRY

Some tools are available to check the user’s ROOT geometry. Besides usual TRIPOLI-4® checking tools (c.f.
7.13.2), Root also offers convenient tools to check on the geometry. The user is advised to read carefully the
ROOT user guide to fully take advantage of all ROOT geometry possibilities.

### 36.2.5 CAVEAT: USE OF OVERLAPPING NODES

ROOT offers the possibility to construct geometries with overlapping volumes. To use this feature, the volumes
must be added to the construction tree with the TGeoVolume::AddNodeOverlap() method. However,
particle tracking in overlapping volumes does not seem to be fully supported in ROOT, according to the ROOT
developers1. The use of ROOT geometries constructed with TGeoVolume::AddNodeOverlap() is therefore
not recommended in TRIPOLI-4. Users are encouraged to replace calls to TGeoVolume::AddNodeOverlap()
with TGeoVolume::AddNode() and to modify the volume shapes using Boolean operators to suppress any
existing overlap.

### 36.2.6 EXAMPLE

A simple example using the ROOT geometry is described here. The ROOT input deck in C++ used to construct
the geometry indicated by figure 36.2 is given in figure 36.1. In this file it should be noted, in particular, the
geometry/composition association made in the TGeoMedium class constructor. It is the name of the material
declared at this point in the construction of the geometry that is reused later in the TRIPOLI-4® input deck
(see figure 36.3).
1https://root-forum.cern.ch/t/unexpected-navigation-behaviour-with-overlapping-nodes/26618

<!-- page 415 -->
gSystem->Load("libGeom");
TGeoManager *geom = new TGeoManager("test_conditions", "Boundary Conditions Test");
TGeoVolume *bigbox, *ball, *mesure, *elem;
TGeoMaterial *vacuum = new TGeoMaterial("vacuum", geom->GetElementTable()->GetElement(0), 1);
TGeoMedium *fuel = new TGeoMedium("FUEL", 1, vacuum);
TGeoMedium *water = new TGeoMedium("WATER", 1, vacuum);
TGeoMedium *air = new TGeoMedium("AIR", 1, vacuum);
TGeoMedium *carb = new TGeoMedium("CARBON", 1, vacuum);
world = geom->MakeBox("world", air, 100, 100, 100);
bigbox = geom->MakeBox("BigBox", air, 10, 10, 10);
bigbox2 = geom->MakeBox("BigBox2", air, 60, 60, 3);
bigbox3 = geom->MakeBox("BigBox3", air, 60, 60, 3);
bigbox4 = geom->MakeBox("BigBox4", air, 60, 3, 60);
bigbox5 = geom->MakeBox("BigBox5", air, 60, 3, 60);
volrefl = geom->MakeBox("volrefl", water, 5, 70, 70);
volrefl->SetLineColor(63);
ball = geom->MakeSphere("uranium", fuel, 0, 10);
ball->SetLineColor(2);
world->AddNode(ball, 1, new TGeoTranslation("tball", 80, 0, 0));
world->AddNode(bigbox, 1, new TGeoTranslation("tbigbox", -80, 0, 0));
world->AddNode(bigbox2, 1, new TGeoTranslation("tbigbox2", 0, 0, 90));
world->AddNode(bigbox3, 1, new TGeoTranslation("tbigbox3", 0, 0, -90));
world->AddNode(bigbox4, 1, new TGeoTranslation("tbigbox4", 0, 90, 0));
world->AddNode(bigbox5, 1, new TGeoTranslation("tbigbox5", 0, -90, 0));
world->AddNode(volrefl, 1, new TGeoTranslation("tvolrefl", 0, 0, 0));
geom->SetTopVolume(world);
geom->CloseGeometry();
world->SetVisContainers(kTRUE);
geom->SetTopVisible(kTRUE);
geom->Export("test_conditions.root");
world->Draw();
Figure 36.1: Sequence of ROOT commands in C++ used in defining a simple geometry

<!-- page 416 -->
Figure 36.2: Visualization of the preceding geometry using ROOT

<!-- page 417 -->
ROOT_GEOMETRY
test_conditions.root
ENDGEOM
ROOT_LIMIT
/world_1/BigBox2_1 *ALL* REFLECTION
END_ROOT_LIMIT
COMPOSITION
4
POINT_WISE 300 FUEL 1
O16 3.2967e-15
POINT_WISE 300 CARBON 1
C 100
POINT_WISE 300 WATER 1
O16 100
POINT_WISE 300 AIR 1
N14 4e-9
END_COMPOSITION
// post-processing data
TRACKS
...
END_TRACKS
Figure 36.3: TRIPOLI-4® input deck allowing for the previously defined ROOT geometry to be used

<!-- page 418 -->
## 36.3 ROOT POST-PROCESSING: RECORDING PARTICLE TRACKS

It is also possible to record the set of tracks (or a sample of it, if the number of simulated particles is significant
) for a simulation. The command is as follows:
TRACKS
BATCH nb(batch) num(batchi) ...num(batchj)
VOLUME nb(vol) name(voln) ...name(voln’)
INTERACTION nb(inter) code(interm) ...code(interm’)
REDUCED_TRACKS
PATH name(file)
END_TRACKS
where nb(batch), nb(vol), nb(inter), num(batchi), name(voln) and code(interm) are, respectively,
the number of batches, the number of volumes, the number of interaction types, the batch number i, the name
of volume n and the code for interaction m (as listed in section 13.2).
Various filters can be used, either alone or together. The BATCH command may be used to filter the batches
to be recorded, the VOLUME command may be used to select the tracks that pass through certain selected
volumes and the INTERACTION command may be used to filter the occurrence of given interaction types. If
both INTERACTION and REDUCED_TRACKS are requested, then only the events corresponding to the requested
interaction types are recorded, whereas if REDUCED_TRACKS is not present, the whole particle histories are
recorded, provided one of their events at least matches a requested interaction type.
When these keywords are absent, no filtering is performed, and, as a consequence, all of the tracks are
recorded (when the storage space of the system allows it).
The tracks are recorded in a file command with the extension .root, which contains all of the simulation
data: the type of particle simulated, the type of collision, the position, the time, the weight, etc... With
this file, it is thus possible to develop post-processing tools using the ROOT libraries. The path of this file
may be specified by the PATH command (with name(file) the chosen path). Otherwise, the file is written
in the current directory with a default name : Tripoli_tracks.root in case of native geometry and
name(geom)_tracks.root in case of ROOT geometry.
