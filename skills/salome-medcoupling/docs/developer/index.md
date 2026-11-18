<!-- source: index.dox -->

# Welcome to MEDCoupling!

The MEDCoupling tool gathers several powerful functionalities around the input and output data of
simulation codes (meshes and fields mainly).

*(figure: Example of a field interpolation between two 3D surface meshes)*

The most common usage is to write dedicated code (C++ or Python) linking to the library. However a graphical user interface is also available; for this please refer to the MED module documentation.

- If you don't know where to start, reading the [getting started](start/start.md) section and then
taking a look at the <a class="el" href="../tutorial/index.html">tutorial</a> is probably a good way to go.
- If you are looking for a very specific point (how can I build a mesh from scratch,
 how do I write my data to a file, etc ...), taking a look at the [FAQ](faq.md) or at the numerous
 [code examples](examples/examples.md) might help.
- Finally people looking for the reference documentation of a given function (in C++ or Python) should
take a look at the API documentation. Only the C++ functions are documented, but
the Python API has been designed to be used in a very similar fashion, provided you are aware of the
[conventions used](start/python-api.md).

## Contents

This documentation is organized as follows:
- index (this page!)
- [FAQ - Frequently asked questions](faq.md)
- [Getting started](start/start.md)
    - [What can I do with MED?](start/intro-start.md)
    - [Terminology - Meshes, fields, interpolation](start/terminology.md)
    - [The MED constellation: MEDCoupling, MEDLoader, MED file, etc ...](start/library.md)
    - [Available functionalities](start/functionalities.md)
    - [A word on the Python API](start/python-api.md)
- <a class="el" href="../tutorial/index.html">Tutorial - MEDCoupling/MEDLoader in Python</a>
- [Reference manual](reference/reference.md)
    - [Core data structures (MEDCoupling)](reference/medcoupling.md)
    - [MEDLoader: Writing, reading MED files](reference/medloader/medloader1.md)
    - [Interpolation](reference/interpolation/interpolation.md)
    - [Note for C++ developers](reference/cpp/cpp.md)
    - [Distribution and parallelism in MEDCoupling](reference/distrib/distrib.md)
    - [Miscellaneous - Specialized interfaces and tools](reference/misc/misc.md)
  
- [Code examples](examples/examples.md)
    - medcouplingpyexamples
    - medcouplingcppexamples
  

- [Appendix](appendix/appendix.md)
    - [Porting code/scripts from version 7 to 8](appendix/porting.md)
    - [Glossary, concepts and definitions](appendix/glossary.md)
    - [Notes on the MED file format](appendix/med-file.md)
    - [Configuring and Installing MED from sources](appendix/install.md)

- MEDCoupling, MEDLoader (and other parallel classes) API documentation
