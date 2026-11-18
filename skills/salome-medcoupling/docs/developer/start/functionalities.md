<!-- source: start/functionalities.dox -->

# Available functionalities

This page tries to list most of the available functionalities of the MEDCoupling library.
It is by no mean exhaustive, but gives an overview of the capabilities of the core library.

## Direct operations on fields

### Field creation

- From scratch: **New**

- Copy: **clone*,** **deepCopy**

### Partial modifications

- Creation: **New,** **setMesh,** **setArray***   

  
  Example 1: medcouplingpyexamplesFieldDoubleBuild1   

  Example 2: medcouplingpyexamplesFieldDoubleBuild2   

  Example 3: medcouplingpyexamplesFieldDoubleBuild3   

  Example 4: medcouplingpyexamplesFieldDoubleBuild4   

  
- Copy
  - **buildNewTimeReprFromThis**
  
  .
  Example: py_mcfielddouble_buildNewTimeReprFromThis
  
- Subparts
  - **buildSubPart***
  
  .
  Example: py_mcfielddouble_subpart1
  
  - **keepSelectedComponents,** **setSelectedComponents**

And also:

- Description: **setName**

- I/O: cf. MEDLoader

## Local arithmetic

### Operations on scalars

- Affectation
  - From a constant: **=**
  - From an expression: **applyFunc*** **applyLin** **fillFromAnalytic***   

  
    Example 1: py_mcfielddouble_applyFunc_same_nb_comp   

    Example 2: py_mcfielddouble_applyFunc3   

    Example 3: py_mcfielddouble_applyFunc2   

    Example 4: py_mcfielddouble_applyFunc   

    Example 5: py_mcmesh_fillFromAnalytic3   

    Example 6: py_mcmesh_fillFromAnalytic2   

    Example 7: py_mcmesh_fillFromAnalytic   

    Example 8: cpp_mcfielddouble_fillFromAnalytic_c_func   

    Example 9: cpp_mcfielddouble_applyFunc_c_func
  
- Addition
  - **+** **+=** **AddFields**
  
  .
  Example: medcouplingpyexamplesFieldDoubleBuild5
  
- Subtraction
  - **\-** **\-=** **SubstractFields**
  - **substractInPlaceDM**
  
  .
  Example: py_mcfielddouble_substractInPlaceDM
  
- Multiplication
  - ***** ***=** **MultiplyFields**
  
  .
  Example: medcouplingpyexamplesFieldDoubleBuild5
  
- Division:
  - **/** **/=** **DivideFields**
  
  .
  Example: medcouplingpyexamplesFieldDoubleBuild5
  
- Power: **^** **^=** **PowFields**

### Operations on vectors or second order tensors

- Contracted product: **doublyContractedProduct**
- Determinant: **determinant**
- Eigenvalues and eigenvectors: **eigenValues,** **eigenVectors**
- Tensor inversion: **inverse**
- Trace: **trace**
- Deviator: **deviator**
- Norms: **norm***

## Interpolation

A full section is dedicated to interpolation, as this is far from being a trivial matter. See: [Interpolation](reference/interpolation/interpolation.md)

## Global operations

- Spatial extrema: **MaxFields,** **MinFields**   

  
  Example: py_mcfielddouble_MaxFields
  
- Spatial mean: **getAverageValue**

- Temporal extrema
  - **getMaxValue***
  - **getMinValue***

## Others

- Renumbering a mesh: **renumber***   

  
  Example 1: py_mcfielddouble_renumberNodes   

  Example 2: py_mcfielddouble_renumberCells
  
- Merge non overlapping fields: **MergeFields**   

  
  Example: py_mcfielddouble_MergeFields
