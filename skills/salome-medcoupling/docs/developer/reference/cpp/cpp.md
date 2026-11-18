<!-- source: reference/cpp/cpp.dox -->

# Note for C++ developers

Using the C++ API provided by MED requires you to be familiar with some specificities which are not
visible to the Python user.

- MCAuto
- [Time label in MEDCoupling](MEDCouplingTimeLabel.md)

**Note:** from version 8, all the standard (sequential and parallel) MEDCoupling API lies in a single
 MEDCoupling namespace.
The true parallel functionalities of the [MED library](start/library.md) are detailed here: [Parallelism](reference/distrib/parallel.md)

The memory management of the various structures is eased by the class
MCAuto. It acts as an auto pointer and takes care of deleting the
memory automatically when going out of scope. See an example usage in cpp_mcfielddouble_WriteVTK .
Beware however that not all functions return a pointer that should be deleted when going out of scope.
Some methods only return an observer to the data, see for example getCoords(). The API documentation of each method indicates whether the caller is responsible of the returned
data or not.

For advanced usage, one has to be aware of the stamping mechanism used internally to know
whether an instance has been modified or not. This is described in the second page above:
 [Time label in MEDCoupling](MEDCouplingTimeLabel.md)

If your interested into wrapping your C++ code to Python with SWIG and intend to do this in a parallel context
you might also want to check swig_mpi.
