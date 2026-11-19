<!-- source: https://docs.salome-platform.org/latest/dev/FIELDS/medcalc-userguide-api.html -->

# MEDMEM library: Starter guide for users

This document illustrates how to start with the programming interface
of the MEDMEM library. The users is someone who intends to create a
data processing script involving meshes and fields.

## General overview

### Definition of the MEDMEM library

The MEDMEM library is designed to manipulate meshes and fields that
conform to the MED data model. This library can be used in C++
programs as in python scripts for data processing on meshes and
fields. The library contains the data structure to describe meshes and
fields as C++ objects (MEDCoupling package). It provides a set of
functions to manage the persistency toward the med file format
(MEDLoader package), and to process the data through interpolation and
localization algorithms (INTERP_KERNEL and REMAPPER packages), for
example to perform field projections from a mesh to another.

### Installation of the MEDMEM library

The MEDMEM library is part of the SALOME FIELDS module and then is
installed together with this module by the installation process of
SALOME. Nevertheless, it is possible for low-weight deployment to
install only the MEDMEM library from the source files embedded in the
SALOME FIELDS module. Keep in mind that the MEDMEM library is designed to
be a self-consistent library with very few third party software (only
med-file, glibc and mpi typically). In particular, it is strictly
independent from the SALOME framework even if it distributed with
SALOME for convenience reasons.

### Components of the MEDMEM library

The MEDMEM library consists in a small set of atomic libraries files,
in particular:

- medcoupling: this library provides the data structures (C++
  classes) to describe meshes and fields.
- medloader: this library provides I/O functions to the MED file
  format
- interpkernel: this library provides the mathematical
  structures and algorithms required med data processing, in
  particular interpolation and localization.
- medcouplingremapper: this library provides the functions for
  fields projections and interpolation.

The figure below represents the layer structure of the packages of the
library:

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/medlayers_70pc.png)

What we call MEDMEM library in this document is represented by the
orange packages on this diagram. The white packages represent the old
deprecated MEDMEM library. The blue packages represent the additional
components for field manipulation through the user interface (TUI and
GUI).

The MEDMEM library comes also with this set of atomic libraries for
advanced users/programmers:

- medcouplingcorba: this library is designed for cross process
  exchange of medcoupling objects.
- medpartitioner: this library provides functions to split a MED
  domain in several part in the perspective of parallel computing

All these atomic C++ libraries are wrapped into a set of python
modules (using the swig binding technology) so that all the data
processing can be realized by scripting.

Avertissement

It could happen that some parts of the C++ libraries are
not wrapped into python modules. This coverture will be
extend on demand and if the integrity of the concepts is
preserved.

## Main concepts of the MEDMEM library

Avertissement

TODO avec Antony. Présenter les structure de données de
MEDCoupling principalement. Describe the MEDMEM data
model, the typical content of a med file, the types of
cell that compose the meshes, the types of spatial
discretization of fields, …

## Basic usages of the MEDMEM library

This section illustrates the usage of main features of the MEDMEM
library using python examples. The usage of python is just to have a
light syntax that makes more easy the first understanding.

Note

All code examples here after are parts of the tutorial use
cases located in the folder src/MEDCalc/tut in the MED
source directory. These use cases are all working executable
programs and they can be used to initiate your own script.

### Preparing the shell environment

We make the hypothesis here that the MEDMEM library is installed using
the SALOME procedure and then is located in the FIELDS module
installation directory. In addition to the MED library, the third
party software required for executing the examples are: python, hdf5
and med-fichier. Then, you should prepare your shell environment
with a set of instructions that looks like:

```python
#------ python ------
export PYTHONHOME=</path/to/python>
export PYTHONSTARTUP=${PYTHONHOME}/pythonrc.py
export PYTHON_INCLUDE=${PYTHONHOME}/include/python2.6
export PATH=${PYTHONHOME}/bin:${PATH}
export LD_LIBRARY_PATH=${PYTHONHOME}/lib:${LD_LIBRARY_PATH}

#------ hdf5 ------
HDF5HOME=</path/to/hdf5>
export PATH=${HDF5HOME}/bin:$PATH
export LD_LIBRARY_PATH=${HDF5HOME}/lib:${LD_LIBRARY_PATH}
export HDF5_DISABLE_VERSION_CHECK=1

#------ med ------
MED2HOME=</path/to/med>
export PATH=${MED2HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${MED2HOME}/lib:${LD_LIBRARY_PATH}

#------ medmem ---
FIELDS_ROOT_DIR=<path/to/salome_fields_module>
export LD_LIBRARY_PATH=${FIELDS_ROOT_DIR}/lib/salome:${LD_LIBRARY_PATH}
PYTHONPATH=${FIELDS_ROOT_DIR}/lib/python2.6/site-packages/salome:${PYTHONPATH}
PYTHONPATH=${FIELDS_ROOT_DIR}/bin/salome:${PYTHONPATH}
PYTHONPATH=${FIELDS_ROOT_DIR}/lib/salome:${PYTHONPATH}
export PYTHONPATH
```

### Example 01: Explore a med file to get information concerning meshes and fields

objectives:
:   This example illustrates how to get information
    concerning meshes and fields from a med file, using the
    MEDLoader library.

The loading of meshes and fields from a med file to a MEDCoupling data
structure requires first the knowledge of metadata associated to these
meshes and fields. You have to know the names of the meshes, so that
you can specify the one you want to load, and then the names of the
fields associated to one given mesh, the space discretizations used
for each field, and the iterations available.

The MEDLoader library can read these metadata without loading the
physical data that compose the meshes and fields. This feature ensures
the performance of the exploration process, in particular in the case
of big meshes.

This first instruction looks for meshes embedded in the med file
(located by filepath) and returns the list of mesh names:

```python

from MEDLoader import MEDLoader
meshNames = MEDLoader.GetMeshNames(filepath)
```

Then, you may select one of these names (or iterate on all names of
the list) and read the list of fields defined on this mesh:

```python

fieldNames = MEDLoader.GetAllFieldNamesOnMesh(filepath,meshName)
```

A field name could identify several MEDCoupling fields, that differ by
their spatial discretization on the mesh (values on cells, values on
nodes, …). This spatial discretization is specified by the
TypeOfField that is an integer value in this list:

- 0 = ON_CELLS (physical values defined by cell)
- 1 = ON_NODES (physical values defined on nodes)
- 2 = ON_GAUSS_PT (physical values defined on Gauss points)
- 3 = ON_GAUSS_NE

Note

This constant variables are defined by the MEDLoader module
(from MEDLoader import ON_NODES).

As a consequence, before loading the physical values of a field, we
have to determine the types of spatial discretization that come with
this field name and to choose one of this types. The instruction below
read all the spatial discretization types available for the field of
name fieldName defined on the mesh of name meshName:

```python

listOfTypes = MEDLoader.GetTypesOfField(filepath,meshName,fieldName)
```

Once you have selected the spatial discretization of interest (called
typeOfDiscretization in the code below, that corresponds to an
item of the list listOfTypes), you can extract the list of time
iterations available for the identified field:

```python

fieldIterations = MEDLoader.GetFieldIterations(typeOfDiscretization,
                                               filepath,
                                               meshName,
                                               fieldName)
```

The iterations can be weither a list of time steps for which the field
is defined (a timeseries) or a list of frequency steps (spectral
analysis). In any case, an iteration item consists in a couple of
integers, the first defining the main iteration step and the second an
iteration order in this step, that can be consider as a sub-iteration
of the step. In most of cases, the iteration order is set to -1
(no sub-iterations).

The field values can now be read for one particular time step (or
spectrum tic), defined by the pair (iteration number, iteration
order). This is illustrated by the example here after.

### Example 02: Load a mesh and a field from a med file

objectives:
:   This illustrates how to load the physical data of a
    specified mesh and a specified field.

The metadata read from a med file are required to identify the list of
meshes and fields in the med file. We assume in this example that the
mesh and field to load are identified, i.e. we know the name of the
mesh to load (meshName) and the characteristic properties of the
field to load (fieldName, typeOfDiscretization and
iteration). For example, the instruction below load the mesh of
name meshName:

```python

mesh = MEDLoader.ReadUMeshFromFile(filepath, meshName, dimrestriction)
```

and the instruction below load the field with name fieldName
defined on this mesh at a particular iteration step characterized by
the couple (iterationNumber,iterationOrder):

```python

field = MEDLoader.ReadField(typeOfDiscretization,
                            filepath, meshName, dimrestriction,
                            fieldName, iterationNumber, iterationOrder)
```

The variables mesh and field in this code example are instances of
the MEDCoupling classes describing the meshes and fields.

Note that the read functions required the parameter
dimrestriction. This parameter discriminates the mesh dimensions you
are interested to relatively to the maximal dimension of cells
contained in the mesh (then its value could be 0, -1, -2 or -3
depending on the max dimension of the mesh). A value of
dimrestriction=0 means « no restriction ».

### Example 03: Manage the MEDCoupling data load from a med file

objectives:
:   Some suggestions for the MEDCoupling objects management,
    in a programming context.

In a real programming case, it could be relevant to explore first the
med file to load all metadata concerning the whole set of meshes and
associated fields, and then to load the physical data only once when
required by the program.

Such a programming scenario required that you keep all metadata in
data structures created in memory, so that you can manage the
collection of meshes and fields. Nevertheless, the MEDMEM library
does not provide such data structures.

We suggest to work with a simple list concept to store the metadata
for each mesh entry and each field entry. Note that a mesh entry is
characterized by the mesh name only, while a field entry is
characterized by the following attributes:

- fieldName: the name of the field
- meshName: the name of the mesh that supports the field
- typeOfDiscretization: the type of spatial discretization
- iteration: a couple of integers (iter,order) that
  characterizes the step in a serie (timeseries or spectrum).

By default, we suggest to work with a simple map concept (dictionary in a
python context, map in a C++ context) to register the meshes and
fields loaded from the med file for each metadata entry.

Then, depending on the processing algorithm you intend to implement,
you may dispatch the data in a tree structure that fit your specific
case, for performance reasons. For example, the following code
illustrates how to dispatch the metadata in a tree data structure
where leaves are the physical data (field objects). We first have to
define a tree structure (basic definition in this simple case, but it
works fine):

```python

import collections
def tree():
    return collections.defaultdict(tree)

fieldTree = tree()
meshDict = {}
```

Then, we can scan the med structure and dispatch the metadata in the
tree structure:

```python

from MEDLoader import MEDLoader
meshNames = MEDLoader.GetMeshNames(filepath)

meshDimRelToMax = 0 # 0 = no restriction

for meshName in meshNames:
    mesh = MEDLoader.ReadUMeshFromFile(filepath,meshName,meshDimRelToMax)
    meshDict[meshName] = mesh

    fieldNames = MEDLoader.GetAllFieldNamesOnMesh(filepath,meshName)
    for fieldName in fieldNames:
        listOfTypes = MEDLoader.GetTypesOfField(filepath,meshName,fieldName)
        for typeOfDiscretization in listOfTypes:
            fieldIterations = MEDLoader.GetFieldIterations(typeOfDiscretization,
                                                           filepath,
                                                           meshName,
                                                           fieldName)
            for fieldIteration in fieldIterations:
                itNumber = fieldIteration[0]
                itOrder  = fieldIteration[1]

                field = MEDLoader.ReadField(typeOfDiscretization,
                                            filepath,
                                            meshName,
                                            meshDimRelToMax,
                                            fieldName,
                                            itNumber,
                                            itOrder)

                fieldTree\
                           [meshName]\
                           [fieldName]\
                           [typeOfDiscretization]\
                           [itNumber][itOrder] = field
```

Finally (and afterwards), we can display on standard output the
metadata registered in the tree structure:

```python

for meshName in fieldTree:
    print("%s"%meshName)
    for fieldName in fieldTree[meshName]:
        print("  %s"%fieldName)
        for fieldType in fieldTree[meshName][fieldName]:
            print("    %s"%fieldType)
            for itNumber in fieldTree[meshName][fieldName][fieldType]:
                for itOrder in fieldTree[meshName][fieldName][fieldType][itNumber]:
                    print("      (%s,%s)"%(itNumber,itOrder))
                    print(fieldTree[meshName][fieldName][fieldType][itNumber][itOrder])
```

### Example 04: Simple arithmetic operations with fields

objectives:
:   This example illustrates how to load field iterations
    from a med file containing a field timeseries and shows
    how to use these iterations in simple arithmetic
    operations.

We consider a med file timeseries.med, containing one single
mesh named Grid_80x80 that supports a field with values defined
on nodes (typeOfDiscretization=ON_NODES) given for ten
iterations.

This first code block identifies the mesh and the field to consider in
this example:

```python

medfilename = "timeseries.med" # med source filename
meshName = "Grid_80x80"        # name of the support mesh
dimrestriction = 0             # 0=no restriction
fieldName = "Pulse"            # name of the field series
```

The following instructions load the field, make a scaling on the
physical values (multiply by 3) and then save the result in an output
med file named scaling.med:

```python

from MEDLoader import MEDLoader, ON_NODES

iteration, order = (3,-1)      # timestamps to consider
field=MEDLoader.ReadField(ON_NODES,
                          medfilename, meshName, dimrestriction,
                          fieldName, iteration, order)

field.applyFunc("f*3")
outfilename = "scaling.med"
MEDLoader.WriteField(outfilename,field,True)
```

Note the usage of the method applyFunc that takes in argument a
string expression that defined the mathematical function to apply on
the values of the fields. In this expression, the field is symbolized
by the letter f.

The following set of instructions makes the addition of iteration
number 3 with iteration number 4 of the field. Note that this
operation required first to load the mesh:

```python

# Load the support mesh
mesh = MEDLoader.ReadUMeshFromFile(medfilename, meshName, dimrestriction)

# Load the field at timestamps 3
iteration, order = (3,-1)
p3=MEDLoader.ReadField(ON_NODES,
                       medfilename,meshName,dimrestriction,
                       fieldName,iteration,order)
# Associate the mesh
p3.setMesh(mesh)

# Load the field at timestamps 4 
iteration, order = (4,-1)
p4=MEDLoader.ReadField(ON_NODES,
                       medfilename, meshName, dimrestriction,
                       fieldName, iteration, order)
# Associate the mesh
p4.setMesh(mesh)

# Make the addition
result = p3+p4
result.setName("p3+p4")

# We can finally save the result together with the operands fields
outfilename = "addition.med"
MEDLoader.WriteField(outfilename,result,True)
MEDLoader.WriteField(outfilename,p3,False)
MEDLoader.WriteField(outfilename,p4,False)
```

### Example 05: Compare fields load from different files

objectives:
:   Illustrates the usage of the function
    changeUnderlyingMesh

### Example 06: Create a field from scratch on a spatial domain

objectives:
:   Illustrates the applyFunc method of fields

### Example 07: Manipulate structured mesh

objectives:
:   Illustrates the basic usage of the advanced interface of
    MEDLoader.

The MEDLoader frontal interface let you load unstructured meshes:

```python

mesh = MEDLoader.ReadUMeshFromFile(filepath, meshName, dimrestriction)
```

That is to say that even if the mesh is a structured mesh (a grid mesh
for example), then you will get a MEDCoupling unstructured mesh
object.

To manipulate structured mesh objects, you have to use the MEDLoader
backend interface named MEDFileMesh, or its derivative
MEDFileUMesh for unstructured meshes, and MEDFileCMesh for
structured meshes (CMesh for Cartesian Mesh). The code below
illustrates how to load a mesh using the MEDFileMesh interface,
and to know if it is a structured mesh:

```python

from MEDLoader import MEDFileMesh
medfile = MEDFileMesh.New(filepath,meshName)
print(medfile.advancedRepr())
meshDimRelToMax = 0 # 0 = no restriction
mesh = medfile.getGenMeshAtLevel(meshDimRelToMax)
print("mesh is structured: %s"%mesh.isStructured())
```

This second example can be used in the case where you know in advance
that it is a structured mesh:

```python

from MEDLoader import MEDFileCMesh
medfile = MEDFileCMesh.New(filepath,meshName)
cmesh = medfile.getMesh()
# Note that the getMesh method is a short way to the method:
#cmesh = medfile.getGenMeshAtLevel(0,False)
print("cmesh is structured: %s"%cmesh.isStructured())
```

In any cases, you can also save the mesh in another file with the
methode write of the MEDFileMesh object:

```python

outputfilepath="output.med"
mode=0
medfile.write(outputfilepath,mode)
```

### Example 08: Make a projection of a field

objectives:
:   Make the projection of a field from a source mesh to a
    target mesh. The source mesh and the target mesh are
    two different mesh of the same geometry.

The input data of this use case are:

- a source mesh, and a field defined on this source mesh (left side of
  the figure below)
- a target mesh, on which we want to project the field (right side of
  the figure below)

Note

The two meshes are displayed side by side on the figure for
convenience reason, but in the real use case they stand at
the same location in 3D space (they describe the same
geometry).

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/medop_projection_inputs.png)

The expected result is a field defined on the target mesh and which
corresponds to a physical data equivalent to the source field,
i.e. with conservation of some physical properties. This operation
requires the usage of interpolation algorithms provided by the
medcouplingremapper library:

```python

from MEDLoader import MEDLoader, ON_CELLS
from MEDCouplingRemapper import MEDCouplingRemapper, IntensiveMaximum

# Read the source mesh and the source field
it,dt = (-1,-1)
msource = MEDLoader.ReadUMeshFromFile("fieldsource.med","meshsource",0)
fsource = MEDLoader.ReadField(ON_CELLS,"fieldsource.med","meshsource",0,
                              "Temperature",it,dt)
fsource.setMesh(msource)
fsource.setNature(IntensiveMaximum)

# Read the target mesh
mtarget = MEDLoader.ReadUMeshFromFile("meshtarget.med","meshtarget",0)

# Remapper of type P0P0 (interpolation from cells to cells)
remap = MEDCouplingRemapper()
remap.prepare(msource,mtarget,"P0P0")

defaultValue = 1e100
ftarget = remap.transferField(fsource,defaultValue)
ftarget.setName("Temperature")

outfilename = "loadsource_fieldtarget.med"
MEDLoader.WriteField(outfilename,ftarget,True)
```

Some comments on this code:

- The physical property to be preserved by this interpolation is
  specified using the keyword IntensiveMaximum
- The parameter P0P0 given at the preparation step of the
  remapper specifies that the interpolation is done from CELLS (P0) to
  CELLS (P0).
- The interpolation, strictly speaking, is performed by the
  instruction ftarget =
  remap.transferField(fsource,defaultValue)
- In this instruction, the defaultValue is used to set the target value
  in the case where there is no cell in the source mesh that overlap
  the target mesh (for example when the source mesh correspond to a
  geometrical sub-part of the target mesh).

When executing the remapper, the result is a new field defined on
the target mesh, as illustrated on the figure below:

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/medop_projection_result.png)

### Example 09: Make a partition of a mesh using a field

objective:
:   This illustrates how to make a mesh partition using the
    value of a field defined on this mesh.

The input data is a MEDCoupling scalar field (field) defined on
a 3D mesh, and we want to use this field as a criterium to make a
partition of the mesh, for example by creating the mesh surface that
delimits the volumes where the field value is greater that a limit L
(and conversely the volumes where the field value is lower).

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/partition_mesh.png)

The code below shows the simplest way to extract the cells where
field>L and to create the skin mesh:

```python

L=0.
arr = field.getArray()
ids = arr.findIdsInRange(L,1e300)
m3DSub = field.getMesh()[ids]
skin = m3DSub.computeSkin()
MEDLoader.WriteUMesh("partition_skin.med",skin,True);
```

At the end, the variable skin is a 2D mesh that can be saved in
a med file using the MEDLoader:

![figure](https://docs.salome-platform.org/latest/dev/FIELDS/_images/partition_skin.png)

## Advanced usages of the MEDMEM library

This section could explain how to process the physical data
(dataArray) and to manipulate the advanced concepts of the MEDMEM
library.
