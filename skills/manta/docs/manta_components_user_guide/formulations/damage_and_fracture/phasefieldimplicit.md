<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/damage_and_fracture/phasefieldimplicit.html -->

# PhaseFieldDamageImplicitFormulation

## Introduction

This formulation aims at solving a phase-field damage problem, related to
explicited mechanical fields. This formulation solves the equation of damage
implicitly.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-fem_phasefield_damage/phasefield_damage_implicit_formulation.h"
```

With the following constructor:

```c++
    auto &damageImplicitForm = rm.make
        <PhaseFieldDamageImplicitFormulation<ShapeId::hex8>> // ①
        (solidForm, // ②
         Dvar, //<3>
         Gc, l);// ④
```

## Parameters

`PhaseFieldDamageImplicitFormulation` has the following template parameter:

- `ShapeId::hex8`, the shape function used for the discretization of the damage field

`PhaseFieldDamageImplicitFormulation` has the following parameters:

- `solidForm`, the instance of the formulation used to compute the mechanical problem;
- `Dvar`, the dof variable of the damage field (1x1 node field);
- `Gc`, the critical energy release rate;
- `lc`, the internal length of the phase-field model;

## List of commented examples and verification tests

- Component verification test : implicit pinched bar in tension
- Component verification test : implicit plate

Both can be found in the tests of the related component.

## Description

This formulation aims at solving the damage problem related to
phase-field modeling following the approach detailed in [[MHW10](../../../references/references.md#id33)]:

\[\begin{split}\begin{aligned}
&\text{Find }d\text{ such that:}\\
&\left(\frac{G_c}{l}+2H\right)d-G_cl\Delta d=2H
\end{aligned}\end{split}\]

where:

- \(d\) is the scalar damage field
- \(G_c\), \(l\) are material coefficients, respectively the
  energy release rate and the internal length
- \(H\) is a so called 'history-function' which corresponds to the
  maximal value of the tensile energy density \(\psi^+\) over the
  past loading history:
  \(H(\t{x},t)=\max_{\tau<t}\psi^+(\t{x}, \tau)\)

This problem is treated by this formulation through the finite element
discretization of the solution space for the damage field \(d\).

The following `EquationTerms` are therefore successively computed:

LHS
:   finite element discretization of
    \(\left(\frac{G_c}{l}+2H\right)d-G_cl\Delta d\)

RHS
:   finite element discretization of \(2H\)

    Note

    The RHS and LHS are integrated on the initial configuration. The
    mesh can be transformed for the mechanical problem, the initial
    configuration is stored in the damage formulation.

## Pre-conditions

### Conditions on the mechanical formulation

The mechanical formulation linked to the phase-field model (`solidExplicitForm` as described above) must expose three methods:

> - `getInternalVariablesField()` which returns a field
>   :   containing its internal variables
> - `getExternalVariablesField()` which returns a field
>   :   containing its external variables
> - `getBehavior()` which returns a typename:Behavior[] object
>   :   which must compute the positive part of the energy density into
>       an internal variable named "PositiveEnergyDensity"

### Damage field viewed by mechanical problem

The solid formulation does not use directly the finite-element damage
node field that is used in the damage formulation. It requires a
damage variable defined at its Gauss points into its 'external
variables' field. This external variables field can be updated so
that its damage variable matches the damage finite-elements node
field passed to the damage formulation constructor:

> ```c++
>     damageImplicitForm.updateSolidExternalVars(D);
> ```
>
> This function performs a finite element interpolation of the damage
> node field to the Gauss points of the external variables fields of
> the formulation for the mechanical problem passed to the constructor
> of the damage formulation.
