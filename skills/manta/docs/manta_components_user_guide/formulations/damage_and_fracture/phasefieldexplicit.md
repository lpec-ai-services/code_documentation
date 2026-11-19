<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/damage_and_fracture/phasefieldexplicit.html -->

# PhaseFieldDamageExplicitFormulation

## Introduction

This formulation aims at solving a phase-field damage problem, related to
explicited mechanical fields. This formulation solves the equation of damage
explicitly. Note that the phase-field time integrators can be used with this
formulation to solve a mechanics/phase-field problem in a staggered fashion.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-fem_phasefield_damage/phasefield_damage_explicit_formulation.h"
```

With the following constructor:
:   ```c++
      auto &damageExplicitForm = rm.make
          <PhaseFieldDamageExplicitFormulation<ShapeId::hex8>> // ①
          (solidExplicitForm, // ②
           D, Dvar, // ③
           Gc, l, eta // ④
           );
    ```

## Parameters

`PhaseFieldDamageExplicitFormulation` has the following template parameter:

- `ShapeId::hex8`, the shape function used for the discretization of the damage field

`PhaseFieldDamageExplicitFormulation` has the following parameters:

- `solidExplicitForm`, the instance of the formulation used to compute the mechanical problem;
- `D`, `Dvar`, the damage field (1x1 node field) and its dof variable;
- `Gc`, the critical energy release rate;
- `lc`, the internal length of the phase-field model;
- `eta`, the viscosity, a usual term in the explicit phase-field model.

## List of commented examples and verification tests

- Explicit Phase-field example : Kalthoff test (in examples/phasefield/kalthoff)
- Component verification test : explicit plate (tested with several time integrators)

The multiple verification tests can be found in the tests repository of this module.

## Description

This formulation aims at solving the following problem:

\[\begin{split}\begin{aligned}
&\text{Find }\dot{d}\text{ such that:}\\
&\eta\,\dot{d}=\left<2(1-d)\psi^+ - \left[\frac{G_c}{l}d - G_cl\Delta d\right]\right>
\end{aligned}\end{split}\]

where:

- \(d\) is the scalar damage field
- \(\eta\), \(G_c\), \(l\) are material coefficients,
  respectively the viscosity parameter, the energy release rate and the
  internal length
- \(\psi^+\) an energy density related to tension state
- \(<>\) the positive part operator

This problem is treated by this formulation through the finite element
discretization of the damage field \(d\) and the solution space for
its damage rate \(\dot{d}\). The mass matrix related to the term
\(\eta\,\dot{d}\) is lumped (row-sum).

The following `EquationTerms` are therefore successively computed:

LHS
:   \(\dot{d}\) being the unknown of the considered problem, the term
    \(\eta\,\dot{d}\) is assembled into a diagonalized (row-sum) mass
    matrix

RHS
:   \(2(1-d)\psi^+ - \left[\frac{G_c}{l}d - G_cl\Delta d\right]\) is
    assembled

    Warning

    The assembled RHS does not involve the positive part operator.
    This has to be done 'externally' as in the following snippet:

    ```c++
      AdvancedExitStatus s=dSystem.assemble(ctx);
      s.update(dSystem.solve(ctx));
      s.update(dSystem.updateField(ctx, dDdt, Dvar)); // ①
      D += dt * max(dDdt, 0.); // ②
    ```

    - the field `dDdt` can have negative terms
    - applies the positive part operator with the function cwiseMax
      to the field `dDdt`

    Note

    The provided [time integrators](../../algorithms_and_numerics/time_integrators/pf_time_integrators.md#pf-time-integrator) for damage field
    handle internally the positive
    part operator.

    Note

    The RHS is integrated on the initial configuration. The mesh can
    be transformed for the mechanical problem, the initial
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

### Critical time-step

Considering the explicit nature of this formulation, a specific consideration of the critical time-step
must be conducted. It can be computed with:

> ```c++
>     Real dtCrit = damageExplicitForm.getCriticalTimeStep();
> ```

Using the following formula:

> \[\Delta t=\frac{\eta h^2}{2 l G_c}\]
>
> where \(h\) is the smallest charcteristic size for the cells on
> which the formulation is applied. This is the critical time step for
> a simplified heat-like equation:
>
> \[\eta\,\dot{d}= - G_c l\Delta d\]
>
> In [[ZRS16](../../../references/references.md#id34)] the authors suggest a more thorough computation of the
> critical time step (but which could cause a very important drop of
> the critical time step when the damage field is close to 1). This
> 'safer' critical time step can be computed using:
>
> ```c++
> #include "manta/components-modeling/finite_elements/phasefield/phasefield_damage_explicit_formulation_with_safe_timestep.h"
> //...
> Real dtCrit = damageExplicitForm.getSafeCriticalTimeStep();
> ```
>
> This 'safe' critical time step depends on the damage field, then it
> must be recomputed at each time step.

### Damage field viewed by mechanical problem

The solid formulation does not use directly the finite-element damage
node field that is used in the damage formulation. It requires a
damage variable defined at its Gauss points into its 'external
variables' field. This external variables field can be updated so
that its damage variable matches the damage finite-elements node
field passed to the damage formulation constructor:

> ```c++
>   damageExplicitForm.updateSolidExternalVars();
> ```
>
> This function performs a finite element interpolation of the damage
> node field to the Gauss points of the external variables fields of
> the formulation for the mechanical problem passed to the constructor
> of the damage formulation.
>
> Note
>
> This function is called automatically by the [specific time
> integrators for damage field problems](https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/damage_and_fracture/pf_time_integrator)
