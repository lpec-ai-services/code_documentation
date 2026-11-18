<!-- source: appendix/med-file.dox -->

# Notes on the MED file format

## Introduction

The MED file format is a specialization of the HDF5 standard, and existed well before
MEDCoupling. Take a look at the
<a class="el" href="http://www.hdfgroup.org/HDF5/">HDF5 Group website</a> for more details on HDF5 itself.
It focuses on (potentially) big amount of data, and the design philosophy was to facilitate a
parallel usage.

The official documentation of the MED-file format is available on-line (in French) in
your SALOME installation at:

```sh
${MEDFILE_ROOT_DIR}/share/doc/html/index.html
```

Remember that the term "MED-file" denotes both:
- a file format on disk (I/O)
- a comprehensive low level C library to read/write MED files (now with a Python wrapping)
and authored by Eric FAYOLLE  (EdF R&D).

## What does it look like?

The picture below shows an UML-like diagram of the MED file format.
We see for example that the mesh name is the unique key linking a [field](reference/fields/fields.md)
to its supporting [mesh](reference/meshes/meshes.md).

*(figure: Functional diagram of the MED file format)*
