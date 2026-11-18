<!-- source: reference/interpolation/remapper.dox -->

# The remapper class.

## High-level usage

The simplest way of using the [interpolations](intro-interp.md) in sequential mode is to use the class `MEDCoupling::MEDCouplingRemapper` . This class fulfills `HXX2SALOME` rules and may be used in YACS coupling graphs.

If you intend to use [MEDCoupling data structures](reference/medcoupling.md), the MEDCoupling::MEDCouplingRemapper class should be used.

Here is a C++ example.

## Middle-level usage

This mode is the mode that needs the minimum of prerequisites
(algorithms and the data structure you intend to use). On the other
hand it is needed to specify precisely nature of interpolator.

As a consequence of the genericity of the interpolators,  they are usable only by
instantiating an underlying [mesh](appendix/interpkernel.md) and [matrix](appendix/interpkernel.md) data structure fulfilling some requirements.

Here is a C++ example.
