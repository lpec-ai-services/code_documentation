<!-- source: https://docs.salome-platform.org/latest/gui/YACS/components.html -->

# Integration of components into the SALOME environment

This document describes operations to be done to integrate codes (for example calculation codes) in the
SALOME architecture.

Several integration scenarios could be envisaged:

- The simplest is local control of the code from a Python interpretor. The code will only operate on one machine.
- The next stage consists of being able to control the code locally or remotely. The selected architecture
  consists of presenting the code as a CORBA server [[CORBA]](references.md#corba), capable of receiving and executing requests
  from CORBA clients. SALOME offers a number of services that simplify the use of CORBA.
- Finally, actual integration into SALOME consists of providing SALOME with all information necessary to control
  the code, for example from the man-machine interface or for example through supervision.

Several types of situations may be envisaged, knowing that there will always be special cases that should be
dealt with by adapting procedures described in this document.
The typical situations envisaged depend on the form of the available code:

- binary executable
- binary library,
- f77/C/C++ source code
- python source code

We will give examples of the different situations encountered wherever possible.

- [Steps in integration of a component](etapes.md)
  - [Concept of component](etapes.md#concept-of-component)
  - [General scheme](etapes.md#general-scheme)
  - [Initial code](etapes.md#initial-code)
  - [Putting the initial code in the form of an internal object](etapes.md#putting-the-initial-code-in-the-form-of-an-internal-object)
  - [Access from a local python interpreter](etapes.md#access-from-a-local-python-interpreter)
  - [Access from CORBA](etapes.md#access-from-corba)
  - [Specific features of the SALOME environment](etapes.md#specific-features-of-the-salome-environment)
- [Defining an internal object](compInterne.md)
  - [Object methods and attributes](compInterne.md#object-methods-and-attributes)
  - [Fortran77 routines / C functions / C++ classes](compInterne.md#fortran77-routines-c-functions-c-classes)
  - [Python function/classes](compInterne.md#python-function-classes)
  - [Initial code in the form of executables](compInterne.md#initial-code-in-the-form-of-executables)
- [Component with local access](accesLocal.md)
  - [Principle](accesLocal.md#principle)
  - [Starting from a python internal object](accesLocal.md#starting-from-a-python-internal-object)
  - [Starting from a C++ internal object](accesLocal.md#starting-from-a-c-internal-object)
- [Component with remote access (through CORBA)](accesCorba.md)
  - [Principle](accesCorba.md#principle)
  - [IDL file](accesCorba.md#idl-file)
  - [Server end interface](accesCorba.md#server-end-interface)
  - [Client interface](accesCorba.md#client-interface)
- [SALOME component](salome.md)
  - [Principle](salome.md#principle)
  - [IDL file](salome.md#idl-file)
  - [Registration into the modules catalog](salome.md#registration-into-the-modules-catalog)
  - [C++ implementation class](salome.md#c-implementation-class)
  - [Python implementation class](salome.md#python-implementation-class)
  - [Using the SALOME compilation and execution environment](salome.md#using-the-salome-compilation-and-execution-environment)
  - [Using data structures provided by SALOME or returned by the component](salome.md#using-data-structures-provided-by-salome-or-returned-by-the-component)
- [Appendix: processing of fortran commons and C / C++ global variables](annexe_common.md)
  - [Fortran common](annexe_common.md#fortran-common)
  - [C/C++ global variables](annexe_common.md#c-c-global-variables)
- [References](references.md)
