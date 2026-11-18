<!-- source: faq.dox -->

# FAQ - Frequently asked questions

Many points covered in this FAQ are illustrated via Python scripts. Remember that the
Python API is almost 100% identical to the C++ one, with the [rules listed here](start/python-api.md).

## Questions

[General questions](faq.md)
    -# [I am a complete newbie, where should I start?](faq.md)
    -# [What is a mesh, what is a field?](faq.md)
    -# [What is a the difference between MED file, MEDCoupling and the SALOME MED module?](faq.md)
    -# [How can I visualize a mesh and/or a field?](faq.md)
    -# [What does a P0- (or P1-) field mean?](faq.md)
    -# [What does surjective/old-2-new/new-2-old format mean?](faq.md)
    -# [What is the implicit numbering of a structured mesh?](faq.md)

[MEDCoupling scripts in Python](faq.md)
    -# ["Can you show me a simple example to get me started"](faq.md)
    -# ["When trying to execute my Python script I have 'ImportError: No module named MEDCoupling'"](faq.md)
    -# ["How to build a mesh from scratch"](faq.md)
    -# ["How to build a field from scratch"](faq.md)
    -# ["How to write/read a mesh to/from a file"](faq.md)
    -# ["How to control the validity of my mesh"](faq.md)
    -# ["How can I read/write groups on a mesh"](faq.md)
    -# ["How can I transform a structured mesh into an unstructured one"](faq.md)

[Projection, interpolation, remapping](faq.md)
    -# [How to project a field from one mesh to the other](faq.md)
    -# [Which formula are used in the field projection algorithms](faq.md)

[C++ specific questions](faq.md)
    -# [Is there some coding guidelines that I should follow](faq.md)
    -# [My C++ program produces a SIGSEGV, what should I do](faq.md)

## Answers

### General questions

#### I am a complete newbie, where should I start?

Take a look at the [getting started](start/start.md) section and the tutorial.

#### What is a mesh, what is a field?

Take a look at [Terminology - Meshes, fields, interpolation](start/terminology.md)

#### What is a the difference between MED file, MEDCoupling and the SALOME MED module?

Take a look at [The MED constellation: MEDCoupling, MEDLoader, MED file, etc ...](start/library.md)

#### How can I visualize a mesh and/or a field?

Use the PARAVIS module of SALOME to visualize your MED file. The following dedicated filters have been
written specifically for MED files: Extract group, Extract cell types, ELNO Mesh, ELNO Points, ELNO Surface.

#### What does a P0- (or P1-) field mean?

Take a look at [Terminology - Meshes, fields, interpolation](start/terminology.md)

#### What does surjective/old-2-new/new-2-old format mean?

Take a look at [Array indexing and numbering](reference/arrays/numbering.md)

#### What is the implicit numbering of a structured mesh?

When converting a structured mesh to unstructured one, or when storing a field onto a structured
mesh, the numbering convention detailed in MEDCoupling::MEDCouplingStructuredMesh::buildUnstructured() is used.

### MEDCoupling scripts in Python

#### "Can you show me a simple example to get me started"

TODO

#### "When trying to execute my Python script I have 'ImportError: No module named MEDCoupling'"

Check that the environment variables PYTHONPATH and LD_LIBRARY_PATH (PATH under Windows) are correctly set.
If you have a full SALOME installation, use the 'shell' command that will automatically set up everything as it
should be:

```sh
cd <salome_install>
salome shell
```

With a custom installation you may want to set the variable manually:

```sh
export PYTHONPATH=<install_root>/lib/python2.7/site-packages/salome
export LD_LIBRARY_PATH=<install_root>/lib/salome
```

#### "How to build a mesh from scratch"

Take a look at this example: medcouplingpyexamplesUmeshStdBuild1

#### "How to build a field from scratch"

Take a look at this example: medcouplingpyexamplesFieldDoubleBuild1

#### "How to write/read a mesh to/from a file"

For starter, take a look at the [basic MEDLoader API](reference/medloader/MEDLoaderBasicAPI.md).

#### "How to control the validity of my mesh"

Use the methods MEDCouplingUMesh::checkConsistencyLight() or
MEDCouplingUMesh::checkConsistency()

#### "How can I read/write groups on a mesh"

Take a look at [Reading a mesh.](reference/medloader/MEDLoaderAdvancedAPI.md) and AdvMEDLoaderAPIMeshWriting.

#### "How can I transform a structured mesh into an unstructured one"

Use the method MEDCouplingCMesh::buildUnstructured()

### Projection, interpolation, remapping

#### How to project a field from one mesh to the other

This the job of the interpolation algorithms in the MED library. For starters, take a look at the
[general introduction on interpolation](reference/interpolation/interpolation.md). Also
this simple example gives a good first illustration.
Finally, if you are intersected in parallel projection (C++ only!), you should take a
look at the [DEC](reference/distrib/parallel.md).

#### Which formula are used in the field projection algorithms

The documentation for non [P0 field](appendix/glossary.md) (i.e. non [cell-based fields](appendix/glossary.md)) is still an
on-going work, but for the P0->P0 case, [this page](reference/interpolation/interptheory.md) gives a good overview.

### C++ specific questions

#### Is there some coding guidelines that I should follow

Yes. Please:
- document your code (this is true for Python too!)
- write some tests (this is true for Python too!)
- and finally, take a look at the page [Note for C++ developers](reference/cpp/cpp.md)

#### My C++ program produces a SIGSEGV, what should I do

Re-compile in debug mode (with `CMAKE_BUILD_TYPE=Debug),` and use either valgrind or gdb
to spot the place where the segfault happens.
The most common source of mistake is some memory mis-allocation and/or deallocation.
With this respect using the auto pointer class
MCAuto
can be of great help.
