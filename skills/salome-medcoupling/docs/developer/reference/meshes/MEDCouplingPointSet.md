<!-- source: reference/meshes/MEDCouplingPointSet.dox -->

# Point set mesh

This is a **non** **instantiable** class that implements many algorithm working only on a set of points without any connectivity aspect.
The presence of this class is only for factorization reasons.

The class that incarnates this concept in [MEDCoupling](reference/medcoupling.md) is : MEDCoupling::MEDCouplingPointSet.
Instantiable class MEDCoupling::MEDCouplingUMesh inherits from MEDCoupling::MEDCouplingPointSet.

Some of most important implemented methods by MEDCouplingPointSet class are :

- getSpaceDimension
- getNumberOfNodes
- rotate
- translate
- scale
- findCommonNodes
- renumberNodes
- getBoundingBox
