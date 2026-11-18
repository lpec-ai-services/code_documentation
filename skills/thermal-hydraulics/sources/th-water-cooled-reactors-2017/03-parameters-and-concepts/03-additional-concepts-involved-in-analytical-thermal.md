# Additional concepts involved in analytical thermal hydraulics
<!-- source PDF pages 21-24 -->

<!-- page 109 (PDF 21) -->
Prandtl number (Pr) is defined as:
Pr = μ · Ce=k
It is the ratio between momentum diffusion and heat diffusion.
N€usselt number (N€u) is defined as:
N€u = hs ·Dh=k
It is the ratio between convective and conduction heat transfer.

### 3.3.2.7 Related to heat radiation

The interest of thermal hydraulics of nuclear systems in radiation heat transfer is limited
to the need of computing the rate of radiation exchanged between hot surfaces in
an advanced phase of an accidental scenario assuming no participating media. Such
interest is limited since disregarding the effect of heat radiation is usually slightly conservative
and traditionally it has been ignored. The surfaces that might cool down by
heat radiation need to have a line-of-sight or a reflection path through which they can
communicate. The central problem is calculating view factors.
3.4
Additional concepts involved in analytical
thermal hydraulics

## 3.4.1 Nuclear factors

Nuclear factors are ratios between parameters related to power generation. They are
useful to understand radial and axial power distortion and helpful to produce a quick
estimation of heat transfer on different areas of the reactor.
Radial nuclear hot channel factor (FR
N) is defined as the ratio between the average
heat flux of the hot channel and the average heat flux of the whole core. A typical
value of such factor at the beginning of cycle in a PWR can be about 1.5. At the
end of cycle such value is clearly reduced. In a similar way, radial nuclear channel
(i) factor is the ratio between the average heat flux of the channel (i) and the average
heat flux of the whole core.
Axial nuclear hot channel factor (FZ
N) is defined as the ratio between the maximum
heat flux of the hot channel and the average heat flux of the hot channel. A typical
value of such factor at the beginning of cycle in a PWR can be about 1.5. At the
end of cycle such value is clearly reduced. In a similar way, axial nuclear channel
(i) factor is the ratio between the maximum heat flux of the channel (i) and the average
heat flux of the channel (i).
Total nuclear heat flux factor is defined as the ratio between the maximum heat flux
of the hot channel and the average heat flux of the whole core. A typical value of such
factor at the beginning of cycle in a PWR can be about 2.25 (obtained as 1.5·1.5).
At the end of cycle such value is clearly reduced.

<!-- page 110 (PDF 22) -->
## 3.4.2 Engineering factors

Engineering factors are ratios between parameters related to two significant engineering
concepts: tolerances and cross-flow paths. They are useful for a quick estimation
on the impact of such phenomena. Engineering tolerances are one of the
sources of uncertainty having an impact on heat transfer; the “engineering tolerances
factor” (FQ
E) is a simple figure that accounts for this. A typical value for FQ
E is 1.03.
Such factor helps computing the so-called total power peaking factor that has a
typical value of 2.32.
FE
Q = Engineering tolerances factor
FQ = Total power peaking factor
FQ = FN
Q ·FE
Q
The “enthalpy-rise hot channel factor” accounts for the effect of cross-flow paths in a
PWR core. The mass interchange between parallel channels results usually in smoothing
enthalpy rise. In an ideal situation assuming that coolant would be strictly associated
to its fuel rod, FΔH and FR
N are identical. In practice cross flows produce a
mixture among channels leading to moderate values of ΔH and then FΔH is slightly
lower than FR
N. Typical values are 1.53 (FΔH) and 1.56 (FR
N).
FΔH = ΔEnthalpyMax=ΔEnthalpyAverage
FΔHi = ΔEnthalpyi=ΔEnthalpyAverage

## 3.4.3 System codes

System codes are devoted to solve six balance equations of mass, momentum, and
energy (for liquid and steam). Such resolution is supplemented by a suitable set of
closure laws. Equations are coupled with heat transfer models and sometimes with
neutron kinetics coding. The two-phase flow field is organized in a number of control
volumes connected by junctions. Thermal-hydraulic components such as separators,
valves, accumulators, or pumps are also coded in order to complete the simulation of
the described system.
Typically, system codes follow a finite difference method based on staggered grids
to avoid the checkerboard problem (artificial pressure oscillations). Depending on the
code, there are many options for temporal discretization. Options are chosen, with the
goal of compromising a relatively large time step and a moderate computational cost.
Spatial discretization is typically defined as a combination of the central difference
and the upwind (donor-like) numerical schemes in order to guarantee maximum
stability of the simulation.

<!-- page 111 (PDF 23) -->
The information describing the plant or the facility is read by the code in a file
called “input deck.” Initial and boundary conditions of the scenario to be analyzed
are also included in the input deck. Nodalization is also in the input deck.
The results produced by code runs could be written down in an ASCII or binary file.
The former can be directly accessed and the latter can be used to produce time trends
of the key parameters or the results of the calculation.
Relap5 (developed by USNRC and USDOE), Cathare (developed by French CEA),
Trace (developed by NRC), and Athlet (developed by German GRS) are the most used
system codes.

## 3.4.4 Closure laws or constitutive equations

Closure laws or constitutive equations are the set of equations that handle mass, momentum
, and energy exchanges between phases and also between each phase and the walls
of the involved control volumes. Such laws, which are rigorously needed for solving the
whole set of equations, are usually obtained empirically and based on separate effect
experiments typically designed specifically for the purpose (Bestion, 1990).
Heat and mass transfer along with friction at the interface and from (or to) the wall
are the most relevant closure laws.

## 3.4.5 Heat transfer correlations/look-up tables

Empirical information, usually about heat transfer, is provided to the code by means of
correlations or look-up tables. Correlations exist for many important parameters of
physical models. Technical literature supports and validates this information. This
is the case of Dittus and Boelter (1930) correlation for heat transfer under forced
convection and also for correlations like those of Kays, Churchill-Chu, Chen
(Chen, 1966), Chen-Sundaram-Ozkaynak (Chen et al., 1977), Bromley (Bromley,
1950), Nusselt, Shah, or Colburn-Hougen. Look-up tables are used in system codes
as another option to supply the values of some empirical information. They fit better
some more complex functions of multiarguments. This is the case of Groeneveld
look-up table for CHF evaluation (Groeneveld, 1973; Groeneveld et al., 1986, 1996).

## 3.4.6 Special models

System codes use to include special models. Such models are called by the main code
when needed and interact with the equations to be solved in order to complete the
description of the simulated scenario. Due to their relevance the following are briefly
mentioned or depicted: choked flow, user-supplied hydrodynamic losses, abrupt area
change, and countercurrent flow limitation (CCFL).
As it has been anticipated in a previous section, most system codes include as special
model a choked flow model. Such model is used to predict if the flow is choked at
the considered junction (usually a break or a nozzle) and to calculate the expected
mass flow under the special conditions established.
The issue of form hydrodynamic losses in junctions is related with what has been
previously said in the section devoted to pressure drop and it is needed of some

<!-- page 112 (PDF 24) -->
flexibility. In order to make available such flexibility, most system codes have a general
user-specified form loss coefficient as an option. User-specified coefficients can
be introduced and used by the code. This special model opens for the user the possibility
of applying form coefficients directly taken from experiments, derived from its
own calculations or from detailed codes.
Another special model, the so-called abrupt area change model, is related to the
previous one. Quite often the code user can be connecting two nodes of different cross
area in a junction having a sharp or abrupt edge. In such sudden enlargement or contraction
of the equivalent pipe the known vena contracta effect will occur. This special
model is often implemented with the purpose of avoiding repetitive calculations of the
corresponding coefficients.
CCFL is a phenomenon that could occur in junctions with a partially closed structure
in a situation having an ascending developed vapor flow and a countercurrent fall-back
liquid. Such structures could include orifices, the upper core tie plate (Glaeser, 1989),
SG tube support plates, or the entrance to the tube sheet in the SG at the inlet plenum. At
low values of vapor mass flow rate, both countercurrent flows are perfectly compatible.
In the event of increasing vapor mass flow, this could limit or even stop the gravity
drainage of liquid.
The special models usually implemented in system codes are providing acceptable
results if the user supplies the needed empirically determined coefficients that use to
be specific for the involved detailed geometry.

## 3.4.7 Special components

System codes use to include special components. Such components are control volumes
or junctions with some specific additional conditions interacting with the equations
to be solved. Such specific conditions dependent on the component itself.
Examples are shown below.
A SG separator works, providing centrifugal separation of liquid and vapor. Some
system codes include a nonmechanistic model that consists of a special volume with
junction flows determined as a function of void fraction. At high void fractions the
vapor junction ejects only vapor; at medium or low void fraction an empirical curve
provides the results.
Valves are special junctions. They can be classified into different kinds, among
them: those that open or close in a time step and those that open or close following
the value of a given variable. Both cited kinds are driven by selected variables that
connect hydrodynamics with protection and controls.
Accumulators are modeled in system codes as lumped-parameter component. Usually
, a simple ideal gas equation of state is used to model the gas behavior during the
discharge.
Pump components are also a special volume. The pump model is connected with
the two-fluid hydrodynamic model and the head term appears in the momentum
equation. Homologous curves provide pump information.
