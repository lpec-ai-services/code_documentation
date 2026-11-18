<!-- source: reference/misc/MEDCouplingFieldTemplates.dox -->

# Field templates in MEDCoupling

This concept appears in ICOCO API.
A field template is the adequate data structure to perform costly interpolation matrix computation as [Remapper class](reference/interpolation/remapper.md) does.
A field template can be seen as field without its double values. The double values are only used for light matrix vector multiplication.

Concretely a field template is a pair containing :

- a [mesh](reference/meshes/meshes.md)
- a spatial discretization (on cells, on nodes, on Gauss points (including localizations, reference elements), )

TODO enhance here

 LocalWords:  discretization
