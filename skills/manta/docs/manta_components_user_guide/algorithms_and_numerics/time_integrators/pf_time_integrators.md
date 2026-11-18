<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/algorithms_and_numerics/time_integrators/pf_time_integrators.html -->

# Phase-field specific time integrators

Time integrators are provided to ease the time integration of phasefield
problems. A description of the phase-field specific formulations is available
[in the catalog of formulations](../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme).
Those time integrators handle the staggered scheme used to solve the
mechanical - phase-field model.

## PhaseFieldHeunTimeIntegrator

This integrates the problem using a Heun’s scheme, as in [[ZRS16](../../../references/references.md#id34)].

\[\begin{split}\begin{aligned}
r_n&=\dot{d}(d_n, \psi^+_n)\\
d_{n+1}^*&=min(1, d_n + \Delta t \,r_n)\\
(\psi^+_{n+1}, \ddot{\t{u}}_{n+1}, \dot{\t{u}}_{n+1}, ...)&=time\_integration\_of\_the\_mechanical\_problem(\Delta t, d_{n+1}^*)\\
r_{n+1}^*&=\dot{d}(d_{n+1}^*, \psi^+_{n+1})\\
d_{n+1} &=min(1, d_n + \frac{\Delta t}{2} \left(r_n+r_{n+1}^*)\right)
\end{aligned}\end{split}\]

To access this integrator, the following include is needed:

```c++
#include "manta/components-fem_phasefield_damage/phasefield_time_integrator.h"
```

and the usage:

Constructor
:   ```c++
        PhaseFieldHeunTimeIntegrator timeIntegrator(
            damageExplicitForm, // ①
            dSystem, // ②
            D, Dvar, // ③
            CentralDifferenceTimeIntegrator(uSystem, {Gvar, {U, V, G}})); // ④
    ```

    - instance of `PhaseFieldDamageExplicitFormulation`
    - (diagonal) linear system whose solution is \(\dot{d}\)
    - The damage field as a 1x1 *node field*
    - Time integrator for the mechanical problem which must expose a
      method `advanceOneStep(Real dt)` which integrates the mechanical
      problem over a time step `dt`

Integrate one time step
:   ```c++
        AdvancedExitStatus s=timeIntegrator.advanceOneStep(ctx, dt);
    ```

    this integrates both the mechanical and damage problem over a time
    increment `dt`.

    Warning

    For the integration to be stable, the input time increment
    \(\Delta t\) passed to this function must be such that
    \(\Delta t \leq min(\Delta t_c^d, \Delta t_c^u)\), where
    \(\Delta t_c^d\) and \(\Delta t_c^u\) are the critical
    time step for the mechanical and damage problem respectively.

## PhaseFieldSubCyclingTimeIntegrator

This integrator is of interest when the critical time step for the
damage problem is signicantly lower than the critical time step of the
mechanical problem: it integrates the mechanical problem using a time
step close to the mechanical stability critical time step, and at each
time increment of the mechanical problem, it performs several time
increments (sub-cycles) for the damage problem with a time step which
divides the mechnical time step and smaller than the critical time step
of the damage problem. The following algorithm is used:

\[\begin{split}\begin{aligned}
k&=\lceil{\Delta t}^u/(cfl^d\,{\Delta t}_c^d)\rceil\\
{\Delta t}^d&={\Delta t}^u/k\\
d_{n,0}&=d_{n}\\
r_{n,m}&=\dot{d}(d_{n,m}, \psi^+_n)\\
d_{n,m+1}&=min(1, d_{n,m} + {\Delta t}^d \,r_{n,m})\\
d_{n+1/2}&=d_{n,\lfloor k/2 \rfloor}\\
(\psi^+_{n+1}, \ddot{\t{u}}_{n+1}, \dot{\t{u}}_{n+1}, ...)&=time\_integration\_of\_the\_mechanical\_problem(\Delta t, d_{n+1/2})\\
d_{n+1/2,0}&=d_{n+1/2}\\
r_{n+1,m}&=\dot{d}(d_{n+1/2,m}, \psi^+_{n+1})\\
d_{n+1/2,m+1}&=min(1, d_{n+1/2,m} + {\Delta t}^d \,r_{n+1,m})\\
d_{n+1}&=d_{n+1/2,\lceil k/2 \rceil}
\end{aligned}\end{split}\]

where \(k\) is the number of subcycles. A simple forward Euler
scheme is used at each sub-cycle for the damage problem.

Constructor
:   ```c++
        PhaseFieldSubCyclingTimeIntegrator timeIntegrator(
            damageExplicitForm, // ①
            dSystem, // ②
            D, Dvar, // ③
            dCfl, // ④
            CentralDifferenceTimeIntegrator(uSystem, {Gvar, {U, V, G}})); // ⑤
    ```

    - instance of `PhaseFieldDamageExplicitFormulation`
    - (diagonal) linear system whose solution is \(\dot{d}\)
    - The damage field as a 1x1 *node field*
    - The security coefficient with respect to the critical time step
      for the damage problem
    - Time integrator for the mechanical problem which must expose a
      method `advanceOneStep(Real dt)` which integrates the mechanical
      problem over a time step `dt`

Integrate one time step
:   ```c++
        AdvancedExitStatus s=timeIntegrator.advanceOneStep(ctx, uDt); // ①
    ```

    - time step increment (whose critical stability value is defined by
      the mechanical problem)

    this integrates both the mechanical and damage problem over a time
    increment `uDt`.

    Warning

    For the integration to be stable, the input time increment
    \(\Delta t\) passed to this function must be such that
    \(\Delta t \leq \Delta t_c^u\), where \(\Delta t_c^u\) is
    the critical time step for the mechanical problem.
