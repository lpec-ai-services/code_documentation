# TRIPOLI-4/GEANT4 COUPLING
<!-- source PDF pages 479-489 -->

<!-- page 479 -->
Chapter 42
TRIPOLI-4/GEANT4 COUPLING
GEANT4 is a particle-transport toolkit developed by several institutions around the world. The main application
areas of GEANT4 are particle physics, space-radiation physics and medical physics. These domains often
involve the transport of charged particles and high-energy particles; in this sense, GEANT4 and TRIPOLI-4
complement each other fairly well.
The coupling between TRIPOLI-4 and GEANT4 makes it possible for users to tap into GEANT4 physics
library and use TRIPOLI-4 to solve transport problems which involve charged particles.
Additionally,
TRIPOLI-4 can use GEANT4 geometries just like another geometry format (similarly to what is done for
ROOT geometries; see Chapter 36).
Note that GEANT4 is not a required prerequisite for normal TRIPOLI-4 execution. GEANT4 is only required
for the execution of input decks using the TRIPOLI-4/GEANT4 coupling. In this case, you need to ensure that
the GEANT4 environment is properly sourced before executing TRIPOLI-4.

## 42.1 REQUIREMENTS ON THE GEANT4 COMPILATION PHASE

The TRIPOLI-4/GEANT4 coupling requires GEANT4 to be compiled in single-threaded mode.
In the
GEANT4 version used by TRIPOLI-4 (v10.4), this requires setting the GEANT4_BUILD_MULTITHREADED
CMake build flag to OFF.
If you has access to the TRIPOLI-4 sources, it is possible to recompile TRIPOLI-4 and couple it to a multithreaded
version of GEANT4. In this case, you must set the GEANT4_BUILD_TLS_MODEL CMake build option
to global-dynamic. Failing to do so will result in mysterious run-time errors at the moment the GEANT4
shared libraries are loaded. For further details, please consult the GEANT4 documentation about the meaning
of this option.

## 42.2 USING GEANT4 GEOMETRIES IN TRIPOLI-4

Since GEANT4 is not a particle-transport code, but rather a toolkit for particle transport, it does not offer a
simple language to describe the problem geometry, like TRIPOLI-4 does. Instead, a GEANT4 geometry is
defined by a set of one or more C++ source files. GEANT4 users need to compile these files to an executable
format, together with a small main program and other simulation specifications.

<!-- page 480 -->
Using GEANT4 geometries outside of GEANT4 is possible, but they still need to be compiled into a shared
library linked to GEANT4. Also, the GEANT4 geometry description are implemented as a C++ class. Since
the name of the geometry class and the arguments to the constructor are not known ahead of time, they cannot
be coded in TRIPOLI-4.
The simplest way to make it possible to instantiate the GEANT4 geometry class from a shared library is to
wrap the construction (and destruction) is a C function with a predefined name. The C wrapper must be
compiled along with the wrapped GEANT4 geometry class.
Adding a wrapper to an existing GEANT4 can be done in two ways. The first, simpler way (Section 42.2.1)
is to use a small open-source utility written for this purpose called g42so; the second way (Section 42.2.2) is
to write the wrapper by hand.

### 42.2.1 WRAPPING A GEANT4 GEOMETRY WITH G42SO

One of the design principles of the TRIPOLI-4/GEANT4 coupling is that using an existing GEANT4 geometry
in TRIPOLI-4 should require minimal user intervention.
This task is simplified by g42so, a
small tool written in Python 2. The g42so source code is shipped with the TRIPOLI-4® installation, but
it can also be downloaded from Github (https://github.com/arekfu/g42so) or installed from PyPI
(https://pypi.org/project/g42so/) via the Python package manager pip:
$ pip install g42so
# install from PyPI
$ pip install --user g42so
# install from PyPI into $HOME
$ pip install --user /path/to/g42so
# install from a local directory into $HOME
Please consult the Python documentation for instructions about using pip.
For the purpose of this example, assume that we are working with a GEANT4 geometry consisting of the
following files:
• include/DetectorConstruction.hh;
• src/DetectorConstruction.cc;
• include/CustomVolumeShape.hh;
• src/CustomVolumeShape.cc.
In real life, these files would belong to a larger GEANT4 application, which would include a main executable,
a primary-generator action (particle source) and other components. Also, we assume that the name of the
geometry class is DetectorConstruction and, to make things a bit less trivial, that it uses a customized
volume shape defined in CustomVolumeShape.{cc,hh}.
If g42so is installed, wrapping the geometry is easy:
$ g42so -I include --geant4 -config /path/to/bin/geant4 -config \
src/DetectorConstruction.cc src/CustomVolumeShape.cc
The command above will produce a libDetectorConstruction.so file that can be used in the TRIPOLI-4
input file (see Section 42.2.3 below). The -v (or --verbose) option will show the compilation commands
that g42so is executing.

<!-- page 481 -->
/* This source files provides wrappers around the construction and the
* destruction of your detector -construction class , which should derive from
* G4VUserDetectorConstruction. You can expand the code as you like , for
* instance by adding parameters to the class constructor or by calling your
* detector -construction factories. Just make sure you expose the required
* createG4Geometry and deleteG4Geometry functions.
*
* Once you have modified this file , save it and pass it to g42so as a source
* file. Make sure you add the --custom -detector -wrapper CLI option , so that
* g42so does not include its standard wrapper.
*/
#include "G4VUserDetectorConstruction.hh"
#include "G4GeometryManager.hh"
// This is where you should #include your custom headers
#include "MyDetectorConstruction.hh"
extern "C" {
G4VUserDetectorConstruction *createG4Geometry() {
// Replace "MyDetectorConstruction" with the name of your class
G4VUserDetectorConstruction *aDetector = new MyDetectorConstruction ();
return aDetector;
}
void deleteG4Geometry(G4VUserDetectorConstruction *aGeom) {
G4GeometryManager *manager = G4GeometryManager::GetInstance ();
if(manager ->IsGeometryClosed ())
manager ->OpenGeometry ();
delete aGeom;
}
}
Listing 42.1: Template wrapper code for the instantiation of GEANT4 geometries generated by g42so.

### 42.2.2 BUILDING THE GEOMETRY WRAPPER BY HAND

Sometimes g42so cannot build the wrapper automatically. This happens, in particular, when the geometry
class needs to be instantiated with some arguments. In such cases, g42so can still help you write your own
wrapper.
First, running
$ g42so --dump -detector -wrapper >template_geom.cc
will write a template C++ wrapper to file template_geom.cc, shown in Listing 42.1. The template needs to
be customized to match your class declaration. An example of customization is shown in Listing 42.2.
The customized wrapper can be subsequently compiled together with the geometry source files.
This
can be done using g42so or by invoking the compiler by hand. If you use g42so, you need to use the
--custom-detector-wrapper option in order to tell g42so that it should not include its default wrapper.

<!-- page 482 -->
#include "G4VUserDetectorConstruction.hh"
#include "G4GeometryManager.hh"
#include "DetectorConstruction.hh"
// note the custom header here
extern "C" {
G4VUserDetectorConstruction *createG4Geometry() {
G4VUserDetectorConstruction *aDetector = new DetectorConstruction("/path/to/data_file");
return aDetector;
}
void deleteG4Geometry(G4VUserDetectorConstruction *aGeom) {
G4GeometryManager *manager = G4GeometryManager::GetInstance ();
if(manager ->IsGeometryClosed ())
manager ->OpenGeometry ();
delete aGeom;
}
}
Listing 42.2:
An example of a customised geometry wrapper.
Here we assume that the wrapped geometry class
DetectorConstruction is declared in the DetectorConstruction.hh header file and that it must be instantiated with a string
argument representing a path to a data file.
So, assuming that the customized wrapper was saved as src/wrapper_geom_custom.cc, the compilation
command line with the custom wrapper should read
$ g42so -I include --geant4 -config /path/to/bin/geant4 -config --custom -detector -wrapper \
src/DetectorConstruction.cc src/CustomVolumeShape.cc src/wrapper_geom_custom.cc

### 42.2.3 DECLARING THE GEANT4 GEOMETRY IN THE TRIPOLI-4 INPUT FILE

At this point you should have a compiled shared library object containing the GEANT4 geometry and the
wrapper code. To use it in TRIPOLI-4, add a G4_GEOMETRY block, as follows:
G4_GEOMETRY
NO_COMPOSITION
geometry_library.so
END_G4_GEOMETRY
Here the geometry_library.so file is the shared library wrapping the GEANT4 geometry, as described
above.

<!-- page 483 -->
The NO_COMPOSITION keyword is optional. If it is not present, TRIPOLI-4 will attempt to build composition
definitions based on the GEANT4 materials defined in the geometry. For each converted composition,
TRIPOLI-4 will print a message translating the GEANT4 composition in a TRIPOLI-4 point-wise composition
like the following:
Translated G4Material EAU as:
PUNCTUAL 300 EAU 2
H1 0.07676
O16 0.03338
You should check that these compositions are correct. In this case, no COMPOSITION or GEOMCOMP blocks are
necessary.
The definition of the GEANT4 geometry may contain nuclides or material temperatures that are not available
in the TRIPOLI-4 cross-section dictionary. In such cases, the NO_COMPOSITION option can be used to to
turn off the automatic conversion. You must then provide a COMPOSITION block; the association between
volumes and compositions is defined by the GEANT4 geometry, so no GEOMCOMP block is needed. Note that
temperature interpolation (see Section 22.1) can also be used to work around mismatched temperatures in the
GEANT4 compositions and in the TRIPOLI-4 cross-section dictionary.

## 42.3 VISUALIZING THE GEOMETRY WITH T4G

The TRIPOLI-4 visualizer T4G (Chapter 38) can be used to display GEANT4 geometries. For geometries
that are not parametrized by UI commands, you just need to pass the name of the shared library to the T4G
executable. Using our libDetectorConstruction.so example library from above, the command reads
$ static_visutripoli4 libDetectorConstruction.so
It is also possible to directly run T4G on the TRIPOLI-4 input file. This is the only way to display geometries
parametrized by UI commands. The TRIPOLI-4 input file, however, must be given a .t4native extension.
So, for example, if detector.t4 is a TRIPOLI-4 input file using a parametrized GEANT4 geometry, it can
be viewed with T4G with the following commands:
$ ln -s detector.t4 detector.t4native
$ static_visutripoli4 detector.t4native

## 42.4 PHYSICS COUPLING

The TRIPOLI-4/GEANT4 coupling can be used to delegate the simulation of particles outside TRIPOLI-4’s
energy range to GEANT4. The principle is that any particle that is not treated by TRIPOLI-4 will be handed
to GEANT4; this can happen for one of the following reasons:
1. TRIPOLI-4 cannot transport particles of the given type (for example: protons);
2. TRIPOLI-4 can transport the given particle type, but the type is not listed in the SIMULATION block under
the PARTICLE keyword (see Section 22.2);
3. the particle energy is outside TRIPOLI-4’s energy range, as determined by the ENERGY_INF and
ENERGY_SUP parameters (see Section 22.2).

<!-- page 484 -->
Note that GEANT4 can only transport particles that are actually produced by some process. Since TRIPOLI-4
will usually not produce particles outside its own range of applicability, the typical coupling scenario involves
high-energy particles being transported by GEANT4 at the beginning of their life; neutrons, photons and other
particles (depending on the options in the SIMULATION block) may then migrate to TRIPOLI-4 when they
enter the low-energy range. The task of injecting high-energy particles into the simulation can be handled by
wrapped GEANT4 sources (see Section 42.5 below).
Note also that the physics coupling between TRIPOLI-4 and GEANT4 is only possible in a GEANT4 geometry.

### 42.4.1 SYNTAX

The physics coupling with GEANT4 requires the presence of a G4_INTERFACE block in the input deck. The
syntax is the following:
G4_INTERFACE
PHYSICS
PHYSICS_LIST physics_list_name
END_G4_INTERFACE
The PHYSICS keyword requests initialization of the GEANT4 physics. The PHYSICS_LIST keyword may be
used to specify which physics list should be used by GEANT4 [41]. The physics list defaults to FTFP_INCLXX.
Note that the G4_INTERFACE block must appear at the beginning of the input file, before G4_UI_COMMANDS
and G4_GEOMETRY.

## 42.5 USING GEANT4 PARTICLE SOURCES IN TRIPOLI-4

High-energy source particles can be produced using GEANT4 sources. In the GEANT4 parlance, sources
are called primary generator actions. Like for geometries, GEANT4 sources are described by implementing
a special C++ class. The instantiation and the destruction of the primary-generator-action class need to be
wrapped in a simple C function. The g42so utility can automatically generate the wrapper if the primarygenerator
-action class can be instantiated without any arguments; otherwise, the wrapper needs to be written
by hand (although, again, g42so can help in that respect, too).
For the sake of illustration, we assume that the GEANT4 particle source consists of the following source files:
• include/PrimaryGeneratorAction.hh;
• src/PrimaryGeneratorAction.cc;
• include/PrimaryGeneratorActionMessenger.hh;
• src/PrimaryGeneratorActionMessenger.cc.

<!-- page 485 -->
Here we assume that the primary generator action proper is defined in PrimaryGeneratorAction.cc, and
that PrimaryGeneratorActionMessenger.cc defines a messenger class for the primary generator action
(see Section 42.8 below).

### 42.5.1 WRAPPING A GEANT4 SOURCE WITH G42SO

Invoking g42so on the source (*.cc) files
$ g42so -I include --geant4 -config /path/to/bin/geant4 -config \
src/PrimaryGeneratorAction.cc src/PrimaryGeneratorActionMessenger.cc
will produce a shared library called libPrimaryGeneratorAction.so containing the particle source and
the wrapper.

### 42.5.2 BUILDING THE SOURCE WRAPPER BY HAND

If the constructor of the primary-generator-action class cannot be invoked without any arguments, it is necessary
to build the wrapper by hand. The process is very similar to the processes for building the geometry
wrapper (Section 42.2.2). First, one creates a wrapper template for primary generator actions with the commmand

$ g42so --dump -pga -wrapper >template_pga.cc
The wrapper template is shown in Listing 42.3. The template needs to be customized to match your class
declaration. An example of customization is shown in Listing 42.4.
The customized wrapper can be subsequently compiled together with the primary-generator-action source
files. This can be done using g42so or by invoking the compiler by hand. If you use g42so, you need to
use the --custom-pga-wrapper option in order to tell g42so that it should not include its default wrapper.
So, assuming that the customized wrapper was saved as src/wrapper_pga_custom.cc, the compilation
command line with the custom wrapper should read
$ g42so -I include --geant4 -config /path/to/bin/geant4 -config --custom -pga -wrapper \
src/PrimaryGeneratorAction.cc src/PrimaryGeneratorActionMessenger.cc \
src/wrapper_pga_custom.cc

<!-- page 486 -->
/* This source files provides wrappers around the construction and the
* destruction of your primary -generator -action class , which should derive from
* G4VUserPrimaryGeneratorAction. You can expand the code as you like , for
* instance by adding parameters to the class constructor or by calling your
* particle factories. Just make sure you expose the required createG4PGA and
* deleteG4PGA functions.
*
* Once you have modified this file , save it and pass it to g42so as a source
* file. Make sure you add the --custom -pga -wrapper CLI option , so that g42so
* does not include its standard wrapper.
*/
#include "G4VUserPrimaryGeneratorAction.hh"
// This is where you should #include your custom headers
#include "MyPrimaryGeneratorAction.hh"
extern "C" {
G4VUserPrimaryGeneratorAction *createG4PGA() {
// Replace "MyPrimaryGeneratorAction" with the name of your class
G4VUserPrimaryGeneratorAction *aPGA = new MyPrimaryGeneratorAction ();
return aPGA;
}
void deleteG4PGA(G4VUserPrimaryGeneratorAction *aPGA) {
delete aPGA;
}
}
Listing 42.3: Template wrapper code for the instantiation of GEANT4 primary generator actions (sources) generated by g42so.
#include "G4VUserPrimaryGeneratorAction.hh"
#include "PrimaryGeneratorAction.hh"
extern "C" {
G4VUserPrimaryGeneratorAction *createG4PGA() {
G4VUserPrimaryGeneratorAction *aPGA = new PrimaryGeneratorAction("/path/to/data_file");
return aPGA;
}
void deleteG4PGA(G4VUserPrimaryGeneratorAction *aPGA) {
delete aPGA;
}
}
Listing 42.4: An example of a customised primary-generator-action wrapper. Here we assume that the wrapped primary-generatoraction
class PrimaryGeneratorAction is declared in the PrimaryGeneratorAction.hh header file and that it must be instantiated
with a string argument representing a path to a data file.

<!-- page 487 -->
### 42.5.3 DECLARING THE GEANT4 SOURCE IN THE TRIPOLI-4 INPUT FILE

At this point you should have a compiled shared library object containing the GEANT4 primary generator
action and the wrapper code. To use it in TRIPOLI-4, add a G4_SOURCE to the SOURCES_LIST block, as
follows:
SOURCE
ALL_PARTICLE
G4_SOURCE pga_library.so
END_SOURCE
Here the pga_library.so file is the shared library wrapping the GEANT4 primary generator action, as
described above.

## 42.6 WRAPPING SOURCES AND GEOMETRIES IN THE SAME SHARED LIBRARY

It is possible to use g42so to wrap a GEANT4 geometry and a primary generator action in the same shared
library. To this end, simply run g42so on all the relevant source files at the same time, possibly including any
hand-coded wrappers (in this case, remember to specify the relevant --custom-*-wrapper option).
Using the examples of Sections 42.2.2 and 42.5 above, a complete command line for g42so might read
$ g42so -I include --geant4 -config /path/to/bin/geant4 -config \
src/DetectorConstruction.cc src/CustomVolumeShape.cc \
src/PrimaryGeneratorAction.cc src/PrimaryGeneratorActionMessenger.cc \
-o libG4sim.so
The generated libG4sim.so file can be used both in the G4_GEOMETRY and in the G4_SOURCE blocks.

## 42.7 SCORES

Particles treated by GEANT4 and recognized by TRIPOLI-4 (neutrons, photons, electrons and positrons) are
normally taken into account for the purpose of the scores defined in the TRIPOLI-4 input deck. This is true
even outside TRIPOLI-4’s usual energy range.
However, since there is no special syntax for defining scores on particles in the GEANT4 domain, it is currently
not possible to define scores for particles that TRIPOLI-4 does not recognize.

## 42.8 SUPPORT FOR GEANT4 UI COMMANDS

Some GEANT4 applications are parametrized using GEANT4’s UI commands. UI commands typically have
the form “/myApp/setDetectorX 3 cm”; they can be used to change some simulation parameters (including

<!-- page 488 -->
the geometry) at run time, without recompiling the application. Executing a GEANT4 UI commands is only
possible if the GEANT4 kernel is the correct state; for instance, commands that modify the geometry can
typically be executed only in PREINIT state.
The TRIPOLI-4/GEANT4 coupling supports the execution of arbitrary UI commands in PREINIT state (before
the call to the /run/initialize UI command) and IDLE state (after /run/initialize but before
/run/beamOn). The commands must be specified in a G4_UI_COMMANDS block, as follows:
G4_UI_COMMANDS
PREINIT
/some/ui/command params
/some/ui/command params
...
FIN_PREINIT
IDLE
/some/ui/command params
/some/ui/command params
...
FIN_IDLE
END_G4_UI_COMMANDS
Any number of commands may be included in each kernel state.
Some important remarks:
• the /run/initialize and /run/beamOn commands must not be included;
• the G4_UI_COMMANDS block must appear before G4_GEOMETRY if the geometry is parametrized by UI
commands.

## 42.9 TROUBLESHOOTING

When TRIPOLI-4 loads the shared libraries containing the user’s GEANT4 geometry or source, errors like the
following may appear:
/.../bin/dynamic_tripoli4 -root -enabled: symbol lookup error:
./libPrimaryGeneratorAction.so: undefined symbol:
_ZN31PrimaryGeneratorActionMessengerC1EP22PrimaryGeneratorAction
The long string at the end is a mangled C++ identifier. It is the internal representation the name of a class, a
method or a function that could not be found when TRIPOLI-4 loaded the libDetectorConstruction.so

<!-- page 489 -->
shared library. Tools called demanglers1 can transform the internal representation into a human-readable
string. The symbol above demangles to
PrimaryGeneratorActionMessenger::PrimaryGeneratorActionMessenger(PrimaryGeneratorAction*)
Typically, errors about missing symbols are caused by the omission of some necessary source files at the
in the arguments to g42so. In this particular case, the demangled string indicates that we probably forgot to
include the PrimaryGeneratorActionMessenger.cc source file when compiling the shared library. Indeed,
the error message above was generated by omitting this source file.
Ideally, this kind of omissions should be detected when the shared library is compiled. Future versions of
g42so might support this feature.
1See c++filt or https://demangler.com, for instance.
