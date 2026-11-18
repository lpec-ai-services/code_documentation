# Two-fluid equations and constitutive equations
<!-- source PDF pages 3-5 -->

<!-- page 551 (PDF 3) -->
entrainment/deposition and the mass, energy, and momentum exchanges at the
droplets-to-vapor interface. These are not discussed here.
9.2
Two-fluid equations and constitutive equations
The basic field equations for a one-dimensional two-fluid model consist of two phasic
continuity equations, two phasic momentum equations, and two phasic energy equations
. The following equations, which may differ in various system TH codes, were
selected to illustrate both the basic form and constitutive terms of a two-fluid model:
l
Continuity equation of k-phase
∂
∂t αkρk
ð
Þ + ∂
∂x αkρkVk
ð
Þ = Γk,
(9.1)
where k=f or g (liquid or vapor phase).
l
Momentum equation of k-phase
∂ αkρkVk
½
□
∂t
+ ∂
∂x αkρkVkVk
ð
Þ =·αkrPk + Fik + Fvm,k
·Fwk + αρkg + ΓkVik + pi
∂
∂xαk:
(9.2)
l
Energy equation of k-phase
∂
∂t αkρkuk
ð
Þ + ∂
∂x αkρkVkuk
ð
Þ = ·P∂αk
∂t ·P ∂
∂x αkVk
ð
Þ + Qwk + Qik + Γkh*
ik:
(9.3)
In the right-hand side of Eqs. (9.1)–(9.3), we need to identify 14 transfer terms at least
that require constitutive relations (D’Auria et al., 2012). These include:
l
Wall transfers
–
Liquid-wall friction (Fwf)
–
Gas-wall friction (Fwg)
–
Wall-to-liquid heat transfer (Qwf)
–
Wall-to-gas heat transfer (Qwg)
l
Interfacial transfers
–
Interfacial mass transfer (Γk, vaporization or condensation; Γf = ·Γg)
–
Liquid to interface heat flux (Qif)
–
Gas to interface heat flux (Qig)
–
Energy transfer to liquid due to interfacial mass transfer
Γf h*
if
□
□
,
–
Energy transfer to gas due to interfacial mass transfer
Γgh*
ig
□
□
,
–
Interfacial momentum transfers:
□
Interfacial friction (Fik),
□
Virtual mass force (Fvm,k),
□
Differential terms of momentum equations related to pressure differences between
phases and interface
pi
∂
∂xαk
□
□
□
Momentum transfer to liquid due to interfacial mass transfer (ΓfVif),
□
Momentum transfer to gas due to interfacial mass transfer (ΓgVig)

<!-- page 552 (PDF 4) -->
As can be seen in Eqs. (9.1)–(9.3), the two-fluid equations are formulated in one dimensioninthedirectionoftheflow
.Thismeanscross-sectionaveragedflowvariablesareused
in the governing equations. Thus the constitutive equations for the thermal-hydraulic
phenomena at the wall and the two-fluid interface should be developed in terms of the
cross-section averaged properties using empirical or semiempirical formulations.
All the constitutive equations in a system TH code should be developed so that
they will be applicable to a wide range of flow conditions (USNRC, 1987) that
may occur during design-basis accidents of light water reactors:
l
pressures from 0.1 to ≡20 MPa,
l
temperatures up to 1500 K,
l
various flow passage geometries, including pipe, rod bundle, and annulus with equivalent
diameters from 0.01 to ≡1.3 m,
l
subcooled liquid, two-phase mixture, and superheated vapor flows,
l
various flow regimes in horizontal, vertical, and inclined ducts,
l
pre-CHF and post-CHF wall heat transfer.
However, in general, most constitutive equations have been developed using experimental
data from a limited range of flow conditions and parameters at reduced-scale
facilities, leading to the scaling issue and uncertainties. Thus the constitutive equations
are one of the key modules in a system TH code that determine overall code
accuracy (Ahn et al., 2015). For example, it is known that about 50% of the uncertainties
of peak cladding temperature (PCT) for a loss-of-coolant accident (LOCA)
in a pressurized water reactor (PWR) come from those of interfacial and wall heat
transfer models (Choi and No, 2012).
Among the 14 terms listed above, the virtual mass force (or added mass force) and
differential terms of momentum equations related to the pressure differences between
phases and interface are briefly discussed first.
In the CATHARE 2, TRACE, and RELAP5 codes, the virtual mass terms have
been implemented as follows:
Fvm,k =
·1
ð
ÞkCvmαf αgρm
dVg
dt ·dVf
dt
□
□
in CATHARE 2,
·1
ð
ÞkCvmαf αgρm
∂Vg
∂t + Vf
∂Vg
∂z ·∂Vf
∂t ·Vg
∂Vf
∂z
□
□
in TRACE,
·1
ð
ÞkCvmαf αgρm
∂Vg
∂t ·∂Vf
∂t
□
□
inRELAP5,
>
>
>
>
>
>
>
>
<
>
>
>
>
>
>
>
>
:
(9.4)
where
·1
ð
Þk =
·1
for k = g
for k = l
□
,
Cvm: the virtual mass which depends on the flow regime,
ρm = αgρg + αf ρf ,
d/dt is the material derivative.

<!-- page 553 (PDF 5) -->
In RELAP5, the spatial derivative terms in the virtual mass force were neglected
(Anderson et al., 1977; USNRC, 1998a,b). The reason for this change is that inaccuracies
in approximating the spatial derivative portion of the term for the relatively
coarse nodalizations used in system representations can lead to nonphysical characteristics
in the numerical solution. Meanwhile, in TRACE (USNRC, 2013), the virtual
mass terms have been ignored in the momentum equations because there is no evidence
of significance in reactor safety problems, and they create a significant increase
in the complexity of the solution procedure. They will reconsider virtual mass terms if
higher order numerical methods are introduced into a future version of TRACE and a
well-posed set of partial differential equations becomes important. However, for the
critical flow model, the effects of virtual mass terms are considered separately. In
CATHARE 2, the virtual mass term was well preserved for the well-posedness of
two-fluid governing equations (Bestion, 1990, see also Chapter 5).
This difference in the three codes indicates that the virtual mass is not of primary
concern from a physical point of view. The primary effects of the virtual mass are on
the mixture sound speed and temporal acceleration of phasic slip. The simplified form
might be adequate in the system of governing equations or it may be neglected.
Most system TH codes, such as RELAP5, TRACE, and CATHARE 2, assume the
two phases have equal pressures in the mass and energy equations. This assumption is
relaxed in the momentum equations in the case of horizontally stratified flow in
RELAP5 and TRACE. However, CATHARE 2 always considers the effect of unequal
pressures in the momentum equations by adding (or subtracting) piA∂αg=∂z into the
interfacial stress terms, where
pi =
αgαf ρf ·ρg
□
□
gD
for the stratified flow
αgαf ρf ρg
αgρf + αf ρg
Vg ·Vf
□
(2
for the nonstratified flows:
>
<
>
:
(9.5)
In nonstratified flows the expression for pi was simply chosen to provide the hyperbolicity
of the system of equations. It is known that the term piA∂αg=∂z has less physical
significance but enhances stability in the CATHARE numerical solution method.
Then, the remaining 12 terms among the 14 listed above can be reduced to the following
four groups: (i) interfacial heat and mass transfer, (ii) interfacial drag, (iii) wall
heat transfer, and (iv) wall friction. The last two were already discussed in Chapters 7
and 8, respectively, in terms of physical phenomena and models. In the remainder of
this chapter, they are discussed again as the constitutive equations.
Two-phase flow may exist under various flow regimes characterized by specific
phase repartitions. Every flow regime has its internal structure and its transfer mechanisms
. This makes it necessary to use a flow regime map (or flow pattern map) and to
develop flow-regime-dependent constitutive relations for interface and wall transfers.
Thus the flow regime map is discussed first in Section 9.3 followed by a discussion
of the interfacial heat and mass transfer, interfacial drag, wall heat transfer, and wall
friction. The effects of noncondensable gases are not included for simplicity of
explanation.
