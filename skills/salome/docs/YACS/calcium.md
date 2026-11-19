<!-- source: https://docs.salome-platform.org/latest/gui/YACS/calcium.html -->

# Guide for the use of CALCIUM coupling in SALOME

This manual only contains a brief explanation of the use of primitives (see [CALCIUM C and Fortran coupling library](calciumapi.md#calciumapi)
and [calcium – python interface](calciummod.md#calciummod) for reference guide),
please refer to [[Calcium1]](#calcium1) and [[Calcium2]](#calcium2) for further information on this subject.

- [From the old CALCIUM product to CALCIUM in SALOME](calciumyacs.md)
  - [The existing CALCIUM product](calciumyacs.md#the-existing-calcium-product)
  - [CALCIUM ports in SALOME](calciumyacs.md#calcium-ports-in-salome)
  - [CALCIUM / SALOME ports and the YACS supervisor](calciumyacs.md#calcium-salome-ports-and-the-yacs-supervisor)
- [Creating a SALOME component using CALCIUM](calciumyacs.md#creating-a-salome-component-using-calcium)
  - [The IDL declaration of components using CALCIUM ports](calciumyacs.md#the-idl-declaration-of-components-using-calcium-ports)
  - [Declaration of a C++ component using CALCIUM ports](calciumyacs.md#declaration-of-a-c-component-using-calcium-ports)
  - [Declaration of component resources (part 1)](calciumyacs.md#declaration-of-component-resources-part-1)
  - [Definition of a component using CALCIUM ports](calciumyacs.md#definition-of-a-component-using-calcium-ports)
  - [Declaration of component resources (part 2)](calciumyacs.md#declaration-of-component-resources-part-2)
  - [Configuring a CALCIUM port](calciumyacs.md#configuring-a-calcium-port)
  - [Calls to CALCIUM methods](calciumyacs.md#calls-to-calcium-methods)
- [Starting CALCIUM coupling](calciumyacs.md#starting-calcium-coupling)
  - [Setting up the environment](calciumyacs.md#setting-up-the-environment)
  - [Running a simple coupling through a python script](calciumyacs.md#running-a-simple-coupling-through-a-python-script)
  - [Running coupling through the YACS GUI](calciumyacs.md#running-coupling-through-the-yacs-gui)
  - [Running coupling through YACS without GUI](calciumyacs.md#running-coupling-through-yacs-without-gui)
  - [Setting up a timeout to interrupt execution in case of interlocking](calciumyacs.md#setting-up-a-timeout-to-interrupt-execution-in-case-of-interlocking)
- [Creating a SALOME application](calciumyacs.md#creating-a-salome-application)
- [Coupling scheme: example of YACS XML file](calciumyacs.md#coupling-scheme-example-of-yacs-xml-file)
- [CALCIUM C and Fortran coupling library](calciumapi.md)
  - [Include files](calciumapi.md#include-files)
  - [Functions to connect and disconnect](calciumapi.md#functions-to-connect-and-disconnect)
  - [Functions to export data](calciumapi.md#functions-to-export-data)
  - [Functions to import data](calciumapi.md#functions-to-import-data)
  - [Functions to erase data](calciumapi.md#functions-to-erase-data)
  - [Examples](calciumapi.md#examples)
  - [Error codes](calciumapi.md#error-codes)
  - [Some considerations about architecture (32, 64 bits) and programming language (C, Fortran)](calciumapi.md#some-considerations-about-architecture-32-64-bits-and-programming-language-c-fortran)
- [`calcium` – python interface](calciummod.md)
  - [Constants](calciummod.md#constants)
  - [Array types](calciummod.md#array-types)
  - [Functions to connect and disconnect](calciummod.md#functions-to-connect-and-disconnect)
  - [Functions to export data](calciummod.md#functions-to-export-data)
  - [Functions to import data](calciummod.md#functions-to-import-data)
  - [Functions to erase data](calciummod.md#functions-to-erase-data)
  - [Example](calciummod.md#example)

[[Calcium1](#id1)]

EDF report HI-26/03/007/A

[[Calcium2](#id2)]

EDF report HI-76/96/009/B
