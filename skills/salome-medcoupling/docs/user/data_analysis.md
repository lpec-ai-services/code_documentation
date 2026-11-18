<!-- source: data_analysis.rst -->

# Data analysis

## Object size in memory

medcoupling provides information on memory occupied by every object: mesh, field, array etc.:

``` python
print(mesh.getHeapMemorySizeStr())
print(field.getHeapMemorySizeStr())
print(array.getHeapMemorySizeStr())
```

## Extract data

### Extract for meshes

If *m* is a mesh (MEDCouplingUMesh) and *Ids* a list of cell ids, you can extract the mesh ids by simply doing :

``` python
part = m[Ids]
```

Note

in medcoupling ids count from zero unlike SMESH where they count from one.

*part* is also a MEDCouplingUMesh with same coordinates than *m*. Reason is that medcoupling tries to reduce memory effort.

But it's highly likely that some nodes in part will be not fetched by part.

It can be interesting to locate the fetched nodes.

``` python
subNodeIds = part.computeFetchedNodeIds()
```

To extract coordinates, simply invoke

``` python
m.getCoords()[subNodeIds]
```

It can be interesting to reduce set of points *part* is lying on. Simply by doing.

``` python
part.zipCoords()
```

Or it can be interesting for further data handling to have both reduction and array.

``` python
o2n = part.zipCoordsTraducer()
```

To have more information about *o2n* read [renumbering](../../developer/numbering.html) section.

Extraction in meshes often leads to locate cells/nodes regarding their neighborhood.

Let's consider *m2* 3D mesh. To locate nodes on boundaries simply invoke :

``` python
bn = m2.findBoundaryNodes()
```

And now to extract cells lying on boundary nodes simply call :

``` python
bc = m2.getCellIdsLyingOnNodes(bn, False)
```

False means if a cell has at least one node in *bn*, take it. True means if all nodes of cell are in *bn*, take it.

If a mesh consists of several contiguous zones of cells, it is possible to retrieve cell ids of each zone:

``` python
# make a structured mesh 1x5
coords = DataArrayDouble(list(range(6)))
cmesh = MEDCouplingCMesh("cmesh")
cmesh.setCoords(coords, coords[:2])

# make a mesh with two zones
zmesh = cmesh.buildUnstructured()[0, 1, 3, 4]

# get cells ids of zones
zoneArrays = zmesh.partitionBySpreadZone()
print([ids.getValues() for ids in zoneArrays])
```

Zones returned by partitionBySpreadZone are:

    [[0, 1], [2, 3]]

### Extract for arrays

Arrays are the common entry point to selection. If *arr* is a 2 component DataArrayDouble you can locate tuple ids by finding those whose first component is in \[a,b):

``` python
tupleIds = arr[:, 0].findIdsInRange(a, b)
```

Or you can find tuples whose magnitude is in \[c,d):

``` python
tupleIds1 = arr.magnitude().findIdsInRange(c, d)
```

To find which of *tupleIds* are missing from *tupleIds1*, call

``` python
tupleIds2 = DataArrayInt.buildSubstraction(tupleIds, tupleIds1)
```

### Extract for fields

If *field4* is a MEDCouplingFieldDouble, you can extract a sub-part of *field4* on a specified cell ids *ids4* by doing

``` python
subField = field4[ids4]
```

Note

It works whatever the spatial discretization of *field4*

You can extract a field on plane by cutting *field5* like this:

``` python
origin = [0, 0, 2]
normvec = [-1, -1, 6]
slice5 = field5.extractSlice3D(origin, normvec, 1e-10)
```

The plane is defined by its *origin* and its normal vector *normvec*. The last argument is a half-thickness of the plane.

Note

It works for fields on cells only

## Geometric handling of unstructured meshes

Consider *m2* as a 3D MEDCouplingUMesh instance. You can translate it by simply

``` python
m2.translate([1.0, 2.0, 3.0])
```

Which is equivalent to

``` python
m2.getCoords()[:] += DataArrayDouble([1.0, 2.0, 3.0], 1, 3)
```

Samely you can simply rotate it around the point \[1,2,1\] along Y axis with an angle of pi/3 by doing

``` python
m2.rotate([1, 2, 1], [0, 1, 0], math.pi / 3)
```

Which is equivalent to

``` python
MEDCouplingPointSet.Rotate3DAlg([1, 2, 1], [0, 1, 0], math.pi / 3, m2.getCoords())
```

To scale *m2* relative to point \[1,2,4\] by a factor of 6, call

``` python
m2.scale([1, 2, 4], 6.0)
```

It can also interesting to retrieve volume of cells in m2 (resp area, length in 2D, 1D):

``` python
volPerCell = m2.getMeasureField(True)
```

*volPerCell* is a field on cell (MEDCouplingFieldDouble). *True* means I don't care of cell orientation. *False* tells I care of cell orientation using signed values.

You can compute total volume covered by mesh by doing

``` python
volPerCell.getArray().accumulate()
```

You also can locate cells (using *cellIds*) having volume greater than a threshold *t1*:

``` python
part = volPerCell.getArray().findIdsGreaterOrEqualTo(t1)
```

In this case it is easy to `build a sub-mesh` containing cells having a volume higher than *t1*:

``` python
m2[part]
```

There are other common geometric methods on meshes:

``` python
centers = m2.computeCellCenterOfMass()
```

*centers* will be a DataArrayDouble giving for each cell of *m2* its center of mass.

It's possible to compute a DataArrayDouble giving the center of mass of *m2* simply by doing

``` python
(centers * volPerCell.getArray()).accumulate() / DataArrayDouble(
    volPerCell.accumulate()
)
```

Iso barycenter of nodes constituting each cell can be computed by calling

``` python
ibc = m2.computeIsoBarycenterOfNodesPerCell()
```

*ibc* will be a DataArrayDouble.

You can retrieve a field (MEDCouplingFieldDouble) of unitary vectors normal to cells:

``` python
ortho_field = m.buildOrthogonalField()
```

You also have a set of methods to caracterize mesh quality: getEdgeRatioField, getAspectRatioField, getWarpField, getSkewField, computeDiameterField.

medcoupling provides methods to intersect 2D meshes in 2D space. MEDCouplingUMesh.Intersect2DMeshWith1DLine partitions a 2D and a 1D mesh:

``` python
m2d, m1d, a2d, a1d = MEDCouplingUMesh.Intersect2DMeshWith1DLine(mesh2d, mesh1d, 1e-12)
```

The last argument is a precision used to perform intersections and localization operations.

Intersect2DMeshWith1DLine returns new 2D and 1D meshes and two arrays. *a2d* gives for each cell in *m2d* the id in *mesh2d* it comes from. *a1d* is an array of pair that gives for each cell id i in *m1d* the cell in *md2* on the left for the 1st component and the cell in *m2d* on the right for the 2nd component. -1 means no cell.

For the example in the picture above *a2d* is:

    [0, 4, 1, 1, 2, 2, 3, 3]

and *a1d* is:

    [-1, -1, -1, -1, 2, 3, 4, 5, 4, 5, 6, 7, 6, 7, -1, -1, -1, -1]

There also a method to partition a 2D mesh by another 2D mesh:

``` python
m, a1, a2 = MEDCouplingUMesh.Intersect2DMeshes(mesh1, mesh2, 1e-12)
```

Intersect2DMeshes returns a new 2D mesh and two arrays. *a1* gives for each result cell an id of the cell of *mesh1* it comes from. *a2* for each result cell gives an id of the cell of *mesh2* it comes from.

You can compute distance from a set of points to cells of a mesh by calling

``` python
dist, cells = mesh.distanceToPoints(points)
```

This method returns distance and a closest cell id for each of given *points*. *points* is a DataArrayDouble with 3 components. Returned *dist* is a DataArrayDouble and *cells* is a DataArrayInt.

## Mesh comparison

It is a common question. You have two meshes *m1* and *m2* coming from 2 different sources (2 files) and expected to be more or less equivalent.

medcoupling proposes some methods to help to caracterize equivalence of these 2 meshes.

The first, the strongest, is informatical equality:

``` python
m1.isEqual(m2, eps)
```

*eps* is the tolerance in coordinates.

If true is returned, you are lucky.

Sometimes only names (and or component names or units) are not the same:

``` python
m1.isEqualWithoutConsideringStr(m2, eps)
```

But sometime the last call also returns False. It may mean that there is a permutation of nodes and or cells.

If you know by construction that *m1* and *m2* share the same coords object:

``` python
a, _ = m1.checkGeoEquivalWith(m2, 20, 1e-12)
assert m1[a].isEqualWithoutConsideringStr(m2, 1e-12)
```

checkGeoEquivalWith returns 2 elements. The first one is relative to cells and the second one is relative to nodes.

If the mapping between *m1* and *m2* is impossible regarding the specified code an exception is thrown. Code meaning:

> - 20=2\*10+0. 2 tells I know that coords are the same. 0 tells two cells are equal if and only if their connectivity is exactly the same.
> - 21=2\*10+1. 2 tells I know that coords are the same. 1 tells two cells are equal if and only if their connectivity is equal within a circular permutation.
> - 22=2\*10+2 . 2 tells I know that coords are the same. 2 tells two cells are equal if and only if nodes set is the same independently from `order`.

If you expect that two meshes are geometrically the same without knowing if there is any cell/node permutation use code 12:

``` python
a, b = m1.checkGeoEquivalWith(m2, 12, 1e-12)
m2.renumberNodes(b, len(b))
assert m1[a].isEqualWithoutConsideringStr(m2, 1e-12)
```

Code meaning: 12=1\*10+2. 1 tells coords can be different. 2 tells two cells are equal if and only if nodes set is the same independently from order.

Remark

*a* and/or *b* may be *None*. It's not a bug it only means that renumbering is equal to identity, meaning that no associated permutation is needed.

## Common handling mesh

*field1* is a node field containing non simplex cells. simplexize on field1.getMesh() can help to overpass this limitation.

``` python
assert field1.getTypeOfField() == ON_NODES
field1.getMesh().simplexize(PLANAR_FACE_5)
field1.getValueOnMulti(pts)
```

Remark

The mesh has been modified by simplexize. This method of simplexization is fast but leads to non conform mesh that can be a problem in some context

tetrahedrize method is dedicated to simplexization of 3D meshes only. It can create a conform mesh. Unlike simplexize method, tetrahedrize method can add new points to the result mesh.

``` python
mtet, n2ocells, np = m3.tetrahedrize(PLANAR_FACE_5)
```

The argument specifies how to split hexahedral cells. it must be in (PLANAR_FACE_5, PLANAR_FACE_6, GENERAL_24, GENERAL_48). *n2ocells* is a DataArrayInt holding, for each new cell, an id of old cell producing it. *np* is a number of new points.

Using medcoupling you can create a 3D extruded mesh. To do that you need a 2D mesh and a 1D mesh, which defines the vector of extrusion and the number of steps. The both meshes must be in 3D space. To extrude a 2D mesh *m2* along a 1D mesh *m1*, call

``` python
m3 = m2.buildExtrudedMesh(m1, 0)
```

The last argument is a policy defining the type of extrusion:

- 0 means "translation only": the cells of the 1D mesh represent the vectors along which the 2D mesh will be repeated to build each level.
- 1 means "translation and rotation": the translation is done as above. For each level, an arc of circle is fitted on the 3 preceding points of the 1D mesh. The center of the arc is the center of rotation for each level, the rotation is done along an axis normal to the plane containing the arc, and finally the angle of rotation is defined by the first two points on the arc.

In order to aggregate several meshes of the same dimension into one mesh, call

``` python
m5 = MEDCouplingUMesh.MergeUMeshes([m3, m4])
```

To transform a linear mesh into a quadratic one, call

``` python
m1.convertLinearCellsToQuadratic(0)
```

A parameter of convertLinearCellsToQuadratic provides type of conversion:

- 0 creates cells of simple quadratic types, e.g. NORM_TRI6 and NORM_QUAD8
- 1 creates cells of complex quadratic types, e.g. NORM_TRI7 and NORM_QUAD9

It's common to deduce skin of a mesh *m1*:

``` python
skin = m1.computeSkin()
```

*skin* and *m1* share the same coordinate array.

In order to get a 1D mesh from a given 2D or 3D mesh, call

``` python
mesh1d, d, di, r, ri = mesh3d.explodeIntoEdges()
```

In addition to *mesh1d*, explodeIntoEdges method returns four arrays describing descending connectivity and reverse descending connectivity in [indirect-indexing](../../developer/numbering.html#numbering-indirect) format. *d* and *di* describe the descending connectivity, i.e. enumerate cells of *mesh1d* bounding each cell of *mesh3d*. *r* and *ri* describe the reverse descending connectivity, i.e. enumerate cells of *mesh3d* bounded by each cell of *mesh1d*.

There is also a method similar to [explodeIntoEdges](#explodeIntoEdges) which returns a mesh of one less dimensions than a given mesh, i.e. 3D-\>2D or 2D-\>1D:

``` python
mesh2d, d, di, r, ri = mesh3d.buildDescendingConnectivity()
```

If a mesh is non-conformal, medcoupling can make it conformal. conformize2D method is to conformize a 2D mesh in 2D space, conformize3D is to conformize a 3D mesh in 3D space:

``` python
changedCells = mesh2d.conformize2D(eps)
```

*changedCells* is an array of ids of changed cells. The changed cells become polygons in 2D and polyhedrons in 3D. *eps* is the relative error to detect merged edges.

You can duplicate some nodes in a mesh by calling

``` python
mesh2d.duplicateNodes([3, 4])
```

This will create new nodes at locations of nodes \#3 and \#4, the new nodes will replace nodes \#3 and \#4 within cells so that the nodes \#3 and \#4 will become orphan.

Inversly it is possible to merges nodes equal within a given precision:

``` python
m.mergeNodes(1e-12)
```

If your 2D mesh in 3D space includes incorrectly oriented cells, you can fix their orientation by calling:

``` python
vec = [0, 0, -1]
skin.orientCorrectly2DCells(vec, False)
```

The last argument if True, only polygons are checked, else, all cells are checked.

Alternatively you can orient all 2D cells equally using the first cell as a reference:

``` python
skin.orientCorrectly2DCells(None)
```

Also it is possible to orient some selected 2D cells by using another group of cells as the reference:

``` python
refCells = [0, 2, 4]
objCells = [1, 3, 5, 6, 7, 8, 20]
refGroup = skin.buildPartOfMySelf(refCells)
objGroup = skin.buildPartOfMySelf(objCells)
objGroup.orientCorrectly2DCells(refGroup)
skin.setPartOfMySelf(objCells, objGroup)
```

If your mesh includes incorrectly oriented polyhedra, the following method can help to fix your mesh:

``` python
m3.orientCorrectlyPolyhedrons()
```

If *m1d* is a 1D line mesh, you can ensure consecutive order of its segments by calling

``` python
m1d.renumberCells(
    m1d.orderConsecutiveCells1D().invertArrayN2O2O2N(m1d.getNumberOfCells())
)
```

orderConsecutiveCells1D method returns a permutation map in [new-to-old](../../developer/numbering.html#MEDCouplingArrayRenumberingN2O) mode but renumberCells method requires the map in [old-to-new](../../developer/numbering.html#MEDCouplingArrayRenumberingO2N) mode, hence we use invertArrayN2O2O2N method to fit to that requirement.

To arrange cells to comply with MED format requirement you can call either of the following methods:

``` python
m3.renumberCells(m3.rearrange2ConsecutiveCellTypes())
m3.sortCellsInMEDFileFrmt()
```

It is also possible to rearrange, and even remove, nodes by calling renumberNodes:

``` python
m.renumberNodes([2, 1, 0, -1], 3)
```

The code above rearranges a mesh with 4 nodes so that old node \#0 becomes \#2, old node \#1 remains \#1, old node \#2 becomes \#0, old node \#3 is removed. The last argument 3 means that number of nodes becomes 3.

## Operations on fields

Integral of a *field* can be computed by calling

``` python
field.integral(True)
field.integral(0, True)
```

The first call returns a list of integrals of all components. The second, returns integral of 0-th component. True means that abs is applied to support size used for computing the integral.

deviator method returns the stress deviator tensor field of a stress tensor *field* (with 6 components):

``` python
assert field.getNumberOfComponents() == 6
diviatorfield = field.deviator()
```

To get value of a *field* at certain *points* call

``` python
points = DataArrayDouble([(0.0, 0.0), (1, 1)])
values = field.getValueOnMulti(points)
```

## Iterative statistics on fields

Statistical moments accross several *field* instances can be computed without having to store all fields in memory. The mean, standard-deviation, variance, and the variance-covariance matrix of field components on each field tuple can be computed by calling

``` python
# check moments on simple linear 3-d field defined on an 1-d mesh
import medcoupling as mc
from MEDCouplingIterativeStatistics import IterativeFieldMoments

# 1-d mesh
size = int(1e1)
coords = [i / size for i in range(size)]
arrX = mc.DataArrayDouble(coords, size, 1)
mesh = mc.MEDCouplingCMesh()
mesh.setCoords(arrX)

# compute statistics
istats = IterativeFieldMoments()

# aggregate 3-d fields
sampling_size = 10
dim = 3
for i in range(sampling_size):
    coeff = 1.0 + i / sampling_size
    field = mesh.fillFromAnalytic(
        mc.ON_NODES, dim, f"2*x*IVec + 3*x*{coeff}*JVec + 5*KVec"
    )
    istats.increment(field)

# check moments on last node
mean = istats.mean()
variance = istats.variance()
stddev = istats.stddev()
covariance = istats.covariance()
```

In a similar fashion Sobol indices from *field* instances can be computed without having to store all fields in memory. The parameters of the fields must be sampled in a *pick-freeze* manner and the fields must be generated on the fly according to these generated parameters combinations.

``` python
# Sobol' test over an 1-d mesh
import medcoupling as mc
from MEDCouplingIterativeStatistics import IterativeFieldSobol
from iterative_stats.experimental_design.experiment import AbstractExperiment

# 1-d mesh [-1; -1]
size = int(1e2)
coords = [-1 + 2 * i / size for i in range(size)]
arrX = mc.DataArrayDouble(coords, size, 1)
mesh = mc.MEDCouplingCMesh()
mesh.setCoords(arrX)

# class to sample 2 parameters: in [0,1]^2 for nb_sim repetitions in a pick-freeze manner
nb_parms = 2
nb_sim = 300

class ABSampler(AbstractExperiment):
    def __init__(self):
        super(ABSampler, self).__init__(nb_parms, nb_sim)
        np.random.seed(42)

    def draw(self):
        return np.random.rand(1, self.nb_parms)

# aggregate the nb_sim simulations
isobol = IterativeFieldSobol(nb_parms)
for pf_sample in ABSampler().generator():
    # build the fields of the time-series f(a, b)_x=a+bx^2 for each (a,b) tuple in the pick-freeze sample
    fields = [
        mesh.fillFromAnalytic(mc.ON_NODES, 1, f"({a}+{b}*x*x)*IVec")
        for a, b in pf_sample
    ]
    # note that for each simulation we need to instanciate nb_parms+2 fields
    isobol.increment(fields)

# retrieve the Sobol' indices of f(a, b)_x in the beginning (x=-1) and middle (x=0) tuples of the time grid
first_beg, total_beg = isobol.indices(0)
print(f"at 0  : first={first_beg} total={total_beg}")

first_mid, total_mid = isobol.indices(size // 2)
print(f"at mid: first={first_mid} total={total_mid}")
```
