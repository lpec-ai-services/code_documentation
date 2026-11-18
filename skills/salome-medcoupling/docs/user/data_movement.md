<!-- source: data_movement.rst -->

# Data movement (mesh/field construction)

## Read Mesh from file

To read a mesh from a MED file simply invoke

``` python
from MEDLoader import ReadMeshFromFile

m = ReadMeshFromFile("file2.med")
```

If the file contains more than one mesh, the previous call will return the first one.

You can access to a precise mesh by doing

``` python
m = ReadMeshFromFile("file2.med", "mesh2")
assert m.getName() == "mesh2"
```

## Read field from file

``` python
from MEDLoader import ReadField

f = ReadField("file.med")
```

This command will succeed if there is exactly one field in "file.med" and only one time step attached to it.

If there are more than one field in "file.med" you are expected to specify the field name.

To know all fields in "file.med" either you read exception thrown or you can invoke

``` python
from MEDLoader import GetAllFieldNames

print(GetAllFieldNames("file.med"))
```

When you have the fieldName you can safely invoke.

``` python
f = ReadField("file.med", "Field1")
```

This command will succeed if there are exactly one time step attached on it. If no you are expected to specify the time step attached on it.

A time step is identified by two piece of information :

- pair of integers specifying without ambiguity a key for access
- floating point (physical time step)

To retrieve list of time step of a field invoke

``` python
from MEDLoader import GetAllFieldIterations

print(GetAllFieldIterations("file.med", "Field1"))
```

This method returns a list of triplet. The first 2 elements of triplets is pair of integers of time step and the last element in the triplet is the physical time step.

To read a field "Field1" at time step defined by pair "(ts0,ts1)" you can invoke

``` python
ts0, ts1 = 1, 5
f = ReadField("file.med", "Field1", ts0, ts1)
```

If you do not succeed reading field in "file.med" using this method it means that your MED file is complex and requires more information to be extracted. `Go to advanced reading`.

Remark

the method is concise but by calling this method several times it leads to a several mesh loads.

## Write mesh into file

MED file format expects a mesh sorted by geometric type. You are responsible to reorder, if needed, cells to match MED file format requirements.

This responsability is let to the end user to avoid misrenumbering effect.

You can check this by invoking:

``` python
m.checkConsecutiveCellTypesForMEDFileFrmt()
```

To reorder cells you are encouraged to read `this`.

If *m* is well numbered, you can dump it into a file by doing :

``` python
from MEDLoader import WriteMesh

WriteMesh("file2.med", m, True)
```

The last element specifies the behavior in case if "file2.med" would already exist. True means, scratch it and write it from scratch. False means do not scratch try to append it.

## Write field into file

You are expected to have a field *f* with a mesh `correctly numbered.`

If *f* is a valid MEDCouplingFieldDouble you can dump it into a MED file by simply :

``` python
from MEDLoader import WriteField

WriteField("file.med", f, True)
```

The last element specifies the behavior in case if "file.med" would already exist. The same meaning than for `writing mesh.`

The typical usecase is to store a multi time step field.

To do that, let's consider that *fs* store a list of MEDCouplingFieldDouble with at least one element in it.

Warning

All meshes of elements in *fs* are expected to be the same

``` python
m = fs[0].getMesh()
WriteMesh("file5.med", m, True)
for f in fs:
    assert f.getMesh().getHiddenCppPointer() == m.getHiddenCppPointer()
    # extra line to insist on the fact that
    WriteFieldUsingAlreadyWrittenMesh("file5.med", f)
```

Remark

f.getTime()\[1:3\] returns the pair of integer that specifies the time step.

f.getTime()\[1:3\] should be different each other. If two elements in *fs* have the same pair of integer time step key, the second one will take the place of the first !

## Create an array from scratch

There are several simple ways to create a medcoupling array from a Python list.

The following call creates an array of double values consisting of 3 tuples with 2 components:

``` python
d = DataArrayDouble([1, 2, 3, 4, 5, 6], 3, 2)
```

The next call creates an array equivalent to one create above:

``` python
d = DataArrayDouble([(1, 2), (3, 4), (5, 6)])
```

The call below creates an array holding the same but differently arranged values: 2 tuples with 3 components:

``` python
d = DataArrayDouble([(1, 2, 3), (4, 5, 6)])
```

You can change number of components in *d* so that it holds 3 tuples with 2 components again:

``` python
d.rearrange(2)
```

Arrays of different types (DataArrayInt, DataArrayFloat) can be created in the same way as DataArrayDouble:

``` python
i = DataArrayInt([(1, 2, 3), (4, 5, 6)])
f = DataArrayFloat([(1, 2, 3), (4, 5, 6)])
```

A medcoupling array can be created from a numpy array and can be transformed to a numpy array:

``` python
# NumPy is an optional pre-requisite!
assert MEDCoupling.MEDCouplingHasNumPyBindings()
a = numpy.arange(20, dtype=numpy.int32)
d = DataArrayInt32(a)  # d owns data of a
e = DataArrayInt32(a)  # a not owned -> e only an access to chunk of a
a1 = d.toNumPyArray()
```

## Create an unstructured mesh from scratch

### MEDCouplingUMesh

MEDCouplingUMesh class represents a general case unstructured mesh. Data of MEDCouplingUMesh is defined in several steps.

Firstly define basic mesh data in full interlace mode for coordinates and nodal connectivity cell per cell.

``` python
coords = [
    -0.3,
    -0.3,
    0.0,
    0.2,
    -0.3,
    0.0,
    0.7,
    -0.3,
    0.0,
    -0.3,
    0.2,
    0.0,
    0.2,
    0.2,
    0.0,
    0.7,
    0.2,
    0.0,
    -0.3,
    0.7,
    0.0,
    0.2,
    0.7,
    0.0,
    0.7,
    0.7,
    0.0,
]
nodalConnPerCell = [0, 3, 4, 1, 1, 4, 2, 4, 5, 2, 6, 7, 4, 3, 7, 8, 5, 4]
```

Then create MEDCouplingUMesh instance giving its mesh dimension (2 here) and a name.

``` python
mesh = MEDCouplingUMesh("My2DMesh", 2)
```

Then add cells to the mesh. This step includes

- giving an upper bound of the number of cells to be inserted into the unstructured mesh.
- entering nodal connectivity of all cells, cell per cell using MEDCouplingUMesh.insertNextCell method.
- compacting connectivity arrays by calling MEDCouplingUMesh.finishInsertingCells method.

``` python
mesh.allocateCells(5)  # You can put more than 5 if you want but not less.
# adding cells
mesh.insertNextCell(NORM_QUAD4, nodalConnPerCell[:4])
mesh.insertNextCell(NORM_TRI3, nodalConnPerCell[4:7])
mesh.insertNextCell(NORM_TRI3, nodalConnPerCell[7:10])
mesh.insertNextCell(NORM_QUAD4, nodalConnPerCell[10:14])
mesh.insertNextCell(NORM_QUAD4, nodalConnPerCell[14:])
# compacting
mesh.finishInsertingCells()
```

As the connectivity of the mesh has been defined, let's set the coordinates using array *coords* defined above.

``` python
coordsArr = DataArrayDouble(
    coords, 9, 3
)  # here coordsArr are declared to have 3 components, mesh will deduce that its spaceDim==3.
mesh.setCoords(
    coordsArr
)  # coordsArr contains 9 tuples, that is to say mesh contains 9 nodes.
```

Now the mesh is usable. To assure this, call

``` python
mesh.checkConsistencyLight()
```

### MEDCoupling1SGTUMesh

MEDCoupling1SGTUMesh class represents an unstructured mesh composed of cells of same geometric type. It is more optimal due to this simplicity.

Basically a MEDCoupling1SGTUMesh is defined in the same way as MEDCouplingUMesh. A difference is that the geometric type of cells is specified at construction, and not specified later e.g. in insertNextCell method:

``` python
mesh = MEDCoupling1SGTUMesh("myQuadMesh", NORM_QUAD4)
mesh.allocateCells(3)
mesh.insertNextCell(nodalConnPerCell[:4])
mesh.insertNextCell(nodalConnPerCell[4:8])
mesh.insertNextCell(nodalConnPerCell[8:12])
```

### MEDCoupling1DGTUMesh

MEDCoupling1DGTUMesh also represents an unstructured mesh composed of cells of same geometric type but it is specialized for cell of "dynamic" geometric type only: NORM_POLYHED and NORM_POLYG.

``` python
polymesh = MEDCoupling1DGTUMesh("myPolyhedra", NORM_POLYHED)
polymesh.allocateCells(1)
polymesh.insertNextCell(
    [
        0,
        1,
        2,
        3,
        -1,
        7,
        6,
        5,
        4,
        -1,
        0,
        4,
        5,
        1,
        -1,
        1,
        5,
        6,
        2,
        -1,
        3,
        2,
        6,
        7,
        -1,
        0,
        3,
        7,
        4,
    ]
)
```

When connectivity of a polyhedron is defined, facets are separated one from another by -1.

## Create a cartesian mesh from scratch

We are going to build a 2D cartesian mesh, constituted from 9 nodes along X axis, and 7 nodes along Y axis.

Firstly define for each direction the discretization and build a DataArrayDouble on the corresponding direction.

``` python
XCoords = [-0.3, 0.0, 0.1, 0.3, 0.45, 0.47, 0.49, 1.0, 1.22]  # 9 values along X
YCoords = [0.0, 0.1, 0.37, 0.45, 0.47, 0.49, 1.007]  # 7 values along Y
arrX = DataArrayDouble(XCoords)
arrX.setInfoOnComponent(0, "X [m]")
arrY = DataArrayDouble(YCoords)
arrY.setInfoOnComponent(0, "Y [m]")
```

Then create MEDCoupling.MEDCouplingCMesh instance giving the 2 instances of DataArrayDouble defined above.

``` python
mesh = MEDCouplingCMesh("My2D_CMesh")
mesh.setCoords(arrX, arrY)
```

The mesh is now usable.

## Create a curvelinear mesh from scratch

First we create a curvelinear mesh and define its structure, for instance a 2-dimensional mesh with 2 nodes in one direction and 3 nodes in the other direction:

``` python
m = MEDCouplingCurveLinearMesh("myCurveLinearMesh")
m.setNodeGridStructure([2, 3])
```

Then define coordinates of 6 nodes in 2D space:

``` python
coords = DataArrayDouble(
    [0.0, 0.0, 2.0, 0.0, 0.0, 1.0, 1.9, 1.1, 0.3, 1.9, 2.2, 2.1], 6, 2
)
coords.setInfoOnComponents(["X [m]", "Y [m]"])
m.setCoords(coords)
```

The mesh is now usable. It's a good habit to assure this:

``` python
m.checkConsistencyLight()
```

## Create a field on cell from scratch

Assume we already have a mesh. We create a field on all cells of the mesh.

``` python
fieldOnCells = MEDCouplingFieldDouble(ON_CELLS, ONE_TIME)
fieldOnCells.setName("MyTensorFieldOnCellOneTime")
fieldOnCells.setMesh(mesh)
```

ONE_TIME indicates that the field data relates to a single time step. Now define this time moment.

``` python
fieldOnCells.setTimeUnit("ms")  # Time unit is ms.
fieldOnCells.setTime(
    4.22, 2, -1
)  # Time attached is 4.22 ms, iteration id is 2 and order id (or sub iteration id) is -1
```

Then define field values:

``` python
array = DataArrayDouble()
array.alloc(
    fieldOnCells.getMesh().getNumberOfCells(), 2
)  # Implicitly fieldOnCells will be a 2 components field.
array.fillWithValue(7.0)
fieldOnCells.setArray(array)
fieldOnCells.checkConsistencyLight()
# fieldOnCells is now usable
# ...
```

## Create a field on node from scratch

Assume we already have a mesh. We create a field on all nodes of the mesh. The procedure is same as for a `field on cells` except two points:

- Spatial discretization in the field constructor is ON_NODES
- Number of tuples in an array of values is equal to mesh.getNumberOfNodes()

``` python
fieldOnNodes = MEDCouplingFieldDouble(ON_NODES, ONE_TIME)
fieldOnNodes.setName("MyScalarFieldOnNodeOneTime")
fieldOnNodes.setMesh(mesh)
fieldOnNodes.setTimeUnit("ms")  # Time unit is ms.
fieldOnNodes.setTime(
    4.22, 2, -1
)  # Time attached is 4.22 ms, iteration id is 2 and order id (or sub iteration id) is -1
array = DataArrayDouble()
array.alloc(
    fieldOnNodes.getMesh().getNumberOfNodes(), 1
)  # Implicitly fieldOnNodes will be a 1 component field.
array.fillWithValue(7.0)
fieldOnNodes.setArray(array)
fieldOnNodes.checkConsistencyLight()
# fieldOnNodes is now usable
# ...
```

## Create a field on Gauss points from scratch

Assume we already have a 2D mesh consisting of triangle and quadrangle cells. We create a field on Gauss points. First, a field is constructed with use of ON_GAUSS_PT and its basic attributes are set:

``` python
fieldGauss = MEDCouplingFieldDouble.New(ON_GAUSS_PT, ONE_TIME)
fieldGauss.setMesh(mesh)
fieldGauss.setName("MyFirstFieldOnGaussPoint")
fieldGauss.setTimeUnit("ms")  # Time unit is ms.
fieldGauss.setTime(
    4.22, 2, -1
)  # Time attached is 4.22 ms, iteration id is 2 and order id (or sub iteration id) is -1
```

Now define localization of Gauss points on cells. In this example, we define two Gauss points on triangle cells and four Gauss points on quadrangle cells. Localization of Gauss points is defined by three lists of float values:

1.  Coordinates of nodes of the reference cell.
2.  Coordinates of Gauss points on the reference cell.
3.  Weights of Gauss points.

``` python
tria3CooRef = [0.0, 0.0, 1.0, 0.0, 0.0, 1.0]
tria3CooGauss = [0.1, 0.8, 0.2, 0.7]
wg3 = [0.3, 0.3]
fieldGauss.setGaussLocalizationOnType(NORM_TRI3, tria3CooRef, tria3CooGauss, wg3)
#
quad4CooRef = [-1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0]
quad4CooGauss = [0.3, 0.2, 0.2, 0.1, 0.2, 0.4, 0.15, 0.27]
wg4 = [0.3, 0.3, 0.3, 0.3]
fieldGauss.setGaussLocalizationOnType(NORM_QUAD4, quad4CooRef, quad4CooGauss, wg4)
```

Finally set field values:

``` python
nbTuples = mesh.getNumberOfCellsWithType(NORM_TRI3) * len(
    wg3
) + mesh.getNumberOfCellsWithType(NORM_QUAD4) * len(wg4)
array = DataArrayDouble.New()
values = [float(i + 1) for i in range(nbTuples)]
array.setValues(values, nbTuples, 1)
fieldGauss.setArray(array)
fieldGauss.checkConsistencyLight()
```

## Modify field values

applyFunc method modifies all tuples of a field at once. It changes both values and number of components, only number of tuples remains the same.

To set value *val* to all tuples of the field *f* and to make it have *nbComp* components, call:

``` python
f.applyFunc(nbComp, val)
```

It is also possible to compute new values basing on current values. To do so you can specify a function by which a new value will be computed. For more info on supported expressions that can be used in the function, see [expressions supported](../../developer/arrays.html#MEDCouplingArrayApplyFuncExpr).

You can use some letters, for example "x", "y", "z" etc., to refer to current component values. For example, to transform a 3D vector field to its magnitude, call:

``` python
f.applyFunc(1, "sqrt(X*X+Y*Y+Z*Z)")
```

This way a value resulting from the function evaluation is assigned to all components.

But you can have its own expression for each component within one function. For this purpose, there are predefined variable names (IVec, JVec, KVec, LVec etc) each dedicated to a certain component (IVec, to the component \#0 etc). A factor of such a variable is added to the corresponding component only.

Using this feature, you can set a magnitude of a 3D vector as the fourth component and swap X and Y components by calling:

``` python
f.applyFunc(4, "IVec*y+JVec*x+KVec*z+LVec*sqrt(x*x+y*y+z*z)")
```

## Define groups and write mesh using advanced API

To get access to full power of MED file, for example to define groups of cells, it is necessary to use the advanced medcoupling API, namely class [MEDFileUMesh](../../developer/classMEDCoupling_1_1MEDFileUMesh.html).

First of all we populate a MEDFileUMesh with meshes (MEDCouplingUMesh) of different dimensions, if present:

``` python
from MEDLoader import MEDFileUMesh

mm = MEDFileUMesh.New()
mm.setMeshAtLevel(0, mesh3D)
mm.setMeshAtLevel(-1, mesh2D)
```

Level must be 0 for a mesh of highest dimension, -1 for a mesh of dimension a unit less than highest dimension etc.

If cells are not yet sorted by geometric type, we can pass True as the third argument of setMeshAtLevel to make them sorted:

``` python
mm.setMeshAtLevel(0, mesh3D, True)
```

Warning

meshes of different dimension must share the same point coordinate array and have the same name

We can change point coordinates as soon as all meshes are added:

``` python
mm.setCoords(otherCoordArray)
```

To define groups we call, for example:

``` python
groupNodes = DataArrayInt([1, 3, 4, 5])
groupNodes.setName("myNodes")
groupFaces = DataArrayInt([12, 13, 15])
groupFaces.setName("myFaces")
mm.addGroup(1, groupNodes)
mm.addGroup(-1, groupFaces)
```

The first argument of addGroup defines a type of group. 1 stands for nodes. 0,-1,-2 and -3 have the same meaning as the level in setMeshAtLevel method. Note that a name of DataArrayInt defines a group name.

It is possible to change name of a group or a family by calling:

``` python
mm.changeGroupName(oldName, newName)
mm.changeFamilyName(oldFamName, newFamName)
```

Finally we write all data added to *mm* to a file:

``` python
mm.write("file.med", 2)
```

The last argument defines behavior if a file exists. 2 means remove. 1 means append; if data with same ID present, an exception is thrown. 0 means overwrite data with same ID; that can lead to a file corruption.

## Read/write fields using advanced API

Having *field* on *mesh* we can write it using [MEDFileField1TS](../../developer/classMEDCoupling_1_1MEDFileField1TS.html) class, which is a part of advanced medcoupling API, as following:

``` python
from MEDLoader import MEDFileUMesh, MEDFileField1TS

mm = MEDFileUMesh.New()
mm.setMeshAtLevel(0, mesh)
ff = MEDFileField1TS.New()
ff.setFieldNoProfileSBT(field)
mm.write(fname, 2)
ff.write(fname, 0)
```

The last argument of write method defines behavior if a file exists. 2 means remove. 1 means append; if data with same ID present, an exception is thrown. 0 means overwrite data with same ID; that can lead to a file corruption.

If there is a need to write a field lying only on a part of a mesh, the following code gives an example of this:

``` python
profile = DataArrayInt([1, 3, 7])
profile.setName("pfl137")
fieldPartial = field[profile]
fieldPartial.setName("fieldPartial")
ff.setFieldProfile(fieldPartial, mm, level, profile)
ff.write(fname, 0)
```

*profile* defines entities on which *fieldPartial* lies. *level* defines entities the field lies on: 1 stands for nodes, 0 is for entities of dimension equal to the mesh dimension, -1 is for entities of dimension a unit less than the mesh dimension etc.

MEDFileField1TS also can be used to read a field:

``` python
ff = MEDFileField1TS.New(fname, fieldName, iteration, order)
mm = MEDFileMesh.New(fname)
# you can choose an appropriate method
field = ff.field(mm)
field = ff.getFieldAtLevel(ON_CELLS, level)
field = ff.getFieldOnMeshAtLevel(ON_CELLS, level, mm)
```

- field method can be used if field support is simple: one spatial discretization and one *level*.
- getFieldAtLevel method allows to choose spatial discretization and *level*.
- getFieldOnMeshAtLevel method allows to specify spatial discretization, *level* and mesh.

*level* of a field, if unknown, can be defined by calling:

``` python
maxDim, maxRelDims = ff.getNonEmptyLevels()
```

*maxDim* is the maximal absolute dimension of entities the field lies on. *maxRelDims* is a sequence returning the dimensions relative to the maximal absolute one.

To read/write fields including several time steps medcoupling provides [MEDFileFieldMultiTS](../../developer/classMEDCoupling_1_1MEDFileFieldMultiTS.html) class. To write all time steps it is necessary just to append them to MEDFileFieldMultiTS:

``` python
ff = MEDFileFieldMultiTS.New()
ff.appendFieldNoProfileSBT(fieldTS1)
ff.appendFieldNoProfileSBT(fieldTS2)
ff.appendFieldProfile(fieldPartialTS1, mm, level, profile)
ff.appendFieldProfile(fieldPartialTS2, mm, level, profile)
ff.write(fname, 0)
```

To read a time step with a known *iteration* and *order* MEDFileField1TS can be used as shown above. To iterate through all time steps, use MEDFileFieldMultiTS as following:

``` python
mm = MEDFileMesh.New(fname)
ff = MEDFileFieldMultiTS.New(fname, fieldName)
for ff1TS in ff:
    iteration, order, time = ff1TS.getTime()
    # you can choose an appropriate method
    field = ff1TS.field(mm)
    field = ff1TS.getFieldAtLevel(ON_CELLS, level)
    field = ff1TS.getFieldOnMeshAtLevel(ON_CELLS, level, mm)
```
