<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/chimera.html -->

# Chimera

## Introduction

This formulation implements the Chimera method in a finite volume framework for
fast transient fluid dynamics (explicit time integration). The Chimera method
allows the transfer of information between non-matching overlapping grids. The
typical use case is the introduction of small geometrical details into a
larger-scale domain. Details on the use of the Chimera method in this context
and its implementation in MANTA can be found in [[PLJ+21](../../../../../references/references.md#id73)].

## Example of usage

to include:

```c++
#include "manta/components-fvm_chimera/chimera.h"
```

In the Chimera framework, the MeshSet designating the coarser global domain is
usually called the "substrate", and the finer local detail is usually call the
"patch".

Here is an exemple of setting the Chimera exchange. You first construct a
Chimera object on the patch, then you construct a Chimera object on the
substrate, using the ChimeraPatch as argument.

```c++
    auto &U0 = rm.make<ElementField<1, 1>>(substrat, "U0");
    auto &U1 = rm.make<ElementField<1, 1>>(patch, "U1");

    Chimera<3, 1, ChimeraLinearReconstructionOperator<3, 1, ChimeraDuboisLimitingOperator>, ChimeraDuboisLimitingOperator>
        chimeraPatch(U0, U1, chimBound, 2, "isGhostCell0", false, LimitingArguments{.k = 0.75});
    Chimera<3, 1, ChimeraLinearReconstructionOperator<3, 1, ChimeraDuboisLimitingOperator>, ChimeraDuboisLimitingOperator>
        chimeraSubstrate(chimeraPatch, 2, "isGhostCell1", false, LimitingArguments{.k = 0.75});
```

## Parameters

`Chimera` has the following template parameters:

- `geoDim` is the space dimension of the formulation support ;
- `nVar` is the number of components of the field to exchange ;
- `RecoOperator` specifies the order of reconstruction (`PieceWiseConstant` or
  `ChimeraLinearReconstructionOperator`) - default = PieceWiseConstant;
- `LimitOperator` specifies the type of limiter associated with the
  reconstruction (None if `RecoOperator` = `PieceWiseConstant`,
  `ChimeraLimitingOperator` if `RecoOperator` =
  `ChimeraLinearReconstructionOperator`) - default = None.

Reconstruction operator and limiter for a 2nd order exchange of data between
substrate and patch are modified versions of the classical Euler reconstruction
operator. The `ChimeraLinearReconstructionOperator` has to properly
identify neighbor cells to compute the field gradient. The
`ChimeraLimitingOperator` is a modified version of the Dubois limiter
([see here](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-reconstruction-and-limiters)) where the distances are computed between
center and nodes instead of center and faces.

Each of the substrate or patch is associated with a Chimera object. One that
send data from the substrate to the patch and the other one from the patch to
the substrate. The exchange zone is automatically determined as a mesh
intersection, given a boundary and the size of the ghost cell layer. Once a
first Chimera is constructed, the second one takes the first one as argument.

First `Chimera` constructor has the following arguments:

- `sender` is the *Field* to send ;
- `receiver` is the *Field* to receive ;
- `exchBound` is the *meshSet* for the boundary of the exchange zone;
- `kGC` is the number of ghost cells ;
- `isGhostCellName` is the name of the ghost cell field (=1 if ghost cell, else 0), for post-processing ;
- `extendDetection` is a boolean to activate an extended detection ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

The second constructor uses a previously constructed Chimera object, and has the following arguments:

- `patchChimera` is the `Chimera` object previously instantiated (sender and receiver are switched);
- `kGC` is the number of ghost cells ;
- `isGhostCellName` is the name of the ghost cell field (=1 if ghost cell, else 0), for post-processing ;
- `extendDetection` is a boolean to activate an extended detection ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).
