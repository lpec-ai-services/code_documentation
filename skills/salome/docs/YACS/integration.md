<!-- source: https://docs.salome-platform.org/latest/gui/YACS/integration.html -->

# Integration of components into SALOME for YACS

This part of the documentation provides information to create SALOME components that can be coupled with YACS, either
starting from scratch or by including an existing code.

The first two chapters are tutorials to create SALOME modules with a single “Hello World” type component, implemented
in Python ([Guide for the development of a SALOME module in Python](pysalome.md#pysalome)) or in C++ ([Guide for the development of a SALOME module in C++](cppsalome.md#cppsalome)).

The next chapter ([Integration of components into the SALOME environment](components.md#components)) describes operations to be done to include calculation codes into the SALOME
architecture.
The fourth chapter ([MEDCoupling Calculator Component](calculator.md#calculator)) shows how to create a SALOME component that uses MED objects.

The next chapter presents a tool ([hxx2salome : a SALOME component generator](hxx2salome.md#hxx2salome)) that automates much of the work to integrate a C++ calculation
code, provided that only the dataflow ports are used.

The sixth chapter ([Introduction to the DSC programming model for SALOME components](progdsc.md#progdsc)) is aimed particularly at persons who would like to develop new datastream ports
based on the DSC programming model.

Finally, the last chapter is a [Guide for the use of CALCIUM coupling in SALOME](calcium.md#calcium). CALCIUM ports are datastream ports predefined in SALOME that simply implement
datastream couplings in YACS.

- [Guide for the development of a SALOME module in Python](pysalome.md)
  - [Steps in construction of the example module](pysalome.md#steps-in-construction-of-the-example-module)
  - [Create the module tree structure](pysalome.md#create-the-module-tree-structure)
  - [Creating a component that can be loaded by a container](pysalome.md#creating-a-component-that-can-be-loaded-by-a-container)
  - [Declared SALOME component](pysalome.md#declared-salome-component)
  - [Adding a graphic GUI](pysalome.md#adding-a-graphic-gui)
- [Guide for the development of a SALOME module in C++](cppsalome.md)
  - [Steps in the construction of the example module](cppsalome.md#steps-in-the-construction-of-the-example-module)
  - [Creating the module tree structure](cppsalome.md#creating-the-module-tree-structure)
  - [IDL interface](cppsalome.md#idl-interface)
  - [C++ implementation](cppsalome.md#c-implementation)
  - [Controlling the component from Python (TUI mode)](cppsalome.md#controlling-the-component-from-python-tui-mode)
  - [Graphic interface](cppsalome.md#graphic-interface)
  - [Syntax naming rules](cppsalome.md#syntax-naming-rules)
- [Integration of components into the SALOME environment](components.md)
  - [Steps in integration of a component](etapes.md)
  - [Defining an internal object](compInterne.md)
  - [Component with local access](accesLocal.md)
  - [Component with remote access (through CORBA)](accesCorba.md)
  - [SALOME component](salome.md)
  - [Appendix: processing of fortran commons and C / C++ global variables](annexe_common.md)
  - [References](references.md)
- [MEDCoupling Calculator Component](calculator.md)
  - [The MED libraries](calculator.md#the-med-libraries)
  - [Creation of a new SALOME module - Compilation](calculator.md#creation-of-a-new-salome-module-compilation)
  - [Modification of interface (IDL)](calculator.md#modification-of-interface-idl)
  - [Component implementation](calculator.md#component-implementation)
- [hxx2salome : a SALOME component generator](hxx2salome.md)
  - [Getting started](hxx2salome.md#getting-started)
  - [What is a C++ component?](hxx2salome.md#what-is-a-c-component)
  - [SALOME component architecture (insights)](hxx2salome.md#salome-component-architecture-insights)
  - [SALOME Component generation](hxx2salome.md#id3)
  - [IDL definition](hxx2salome.md#idl-definition)
  - [IDL Implementation](hxx2salome.md#idl-implementation)
  - [Usage](hxx2salome.md#usage)
  - [Limitations – Advice](hxx2salome.md#limitations-advice)
- [Introduction to the DSC programming model for SALOME components](progdsc.md)
  - [The principle of the programming model](progdsc.md#the-principle-of-the-programming-model)
  - [Benefits of the DSC extension](progdsc.md#benefits-of-the-dsc-extension)
  - [Connections between DSC ports](progdsc.md#connections-between-dsc-ports)
  - [The two programming layers](progdsc.md#the-two-programming-layers)
  - [DSC through examples](progdsc.md#dsc-through-examples)
- [Guide for the use of CALCIUM coupling in SALOME](calcium.md)
  - [From the old CALCIUM product to CALCIUM in SALOME](calciumyacs.md)
  - [Creating a SALOME component using CALCIUM](calciumyacs.md#creating-a-salome-component-using-calcium)
  - [Starting CALCIUM coupling](calciumyacs.md#starting-calcium-coupling)
  - [Creating a SALOME application](calciumyacs.md#creating-a-salome-application)
  - [Coupling scheme: example of YACS XML file](calciumyacs.md#coupling-scheme-example-of-yacs-xml-file)
  - [CALCIUM C and Fortran coupling library](calciumapi.md)
  - [`calcium` – python interface](calciummod.md)
