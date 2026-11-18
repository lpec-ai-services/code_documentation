# Wall friction
<!-- source PDF pages 33-36 -->

<!-- page 581 (PDF 33) -->
For the default CHF model in TRACE, the 1995 AECL-IPPE CHF lookup table
(Groeneveld et al., 1996) was selected. It is based on an extensive database of
CHF values obtained in tubes with a vertical upflow of a steam-water mixture, and
provides the value of the critical heat flux as a function of the local conditions. This
method was selected because of its reasonably good accuracy and wide range of
applicability.
The wall heat transfer models play a crucial role in the system TH codes, requiring
continuous improvement. It is well known that the model uncertainties of post-CHF
heat transfer and condensation under the presence of noncondensable gases are still
great, thus leading to continuous development of new models (Chatzikyriakou
et al., 2010; Chikhi and Fichot, 2010; Wu et al., 2012; Huang et al., 2015). The implementation
of a new model into a system TH code, however, requires very careful
approach. The wall heat transfer package in a code consists of many specific models.
For example, RELAP5-3D uses 31 heat transfer models. A change in one of the
models, which was proved to be advanced based on the assessment against separate
effect tests, may not yield expected results in a transient calculation for an integral
effect test or a nuclear power plant because it may change the transient sequence,
may not be used as intended, or may affect the wall heat transfer at a transition region
by interpolation. Thus, a systematic assessment using integral effect tests is needed
also. This causes significant delay between a new model development and its implementation
in a system TH code.
9.7
Wall friction
Frictional pressure losses in a system TH code are usually divided into wall friction
and form loss (or called form drag). The former models the fluid-wall shear using a
friction factor approach. The latter models geometry-specific pressure losses at a sudden
area change (expansion and contraction), orifice, elbow, bend, or complicated
flow passage geometries, using an additive loss coefficient, of which form loss factor
is usually input by the user.
Various wall friction models were introduced in Chapter 8. This chapter puts an
emphasis on the method to implement the wall friction models into a system TH code.
In the two-fluid formulation, the phasic pressure gradient due to wall friction can be
given by
dP
dx
□
□
fr, f
= ·Cwf Vf
Vf
(9.49)
and
dP
dx
□
□
fr,g
= ·Cwg Vg
Vg,
(9.50)

<!-- page 582 (PDF 34) -->
where Cwf and Cwg are the wall friction coefficients for wall-liquid and wall-gas shear,
respectively.

## 9.7.1 Single-phase flow

In the case of a single-phase flow, the wall friction coefficients of k-phase is
defined by
Cwk = λD
ρk
2D,
(9.51)
where the subscript k indicates the fluid phase (f or g) and λD is the friction factor. To
obtain the friction factor, RELAP5 uses correlations for laminar and turbulent flows
with interpolation in the transition regime. It is calculated as
λD =
ReΦs
for 0 □ Re □ 2200,
3:75·8250
Re
□
□
λT,3000 ·λL,2200
ð
Þ + λL,2200
for 2200 < Re < 3000,
·2 log10
ε
3:7D + 2:51
Re
1:14·2 log10
ε
D·21:25
Re0:9
□
□
□
□
□·2
for Re □ 3000,
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
(9.52)
where
Re is the Reynolds number,
ΦS is a user-input shape factor for noncircular flow channels,
λL,2200 is the laminar factor at a Reynolds number of 2200,
λT,3000 is the turbulent friction factor at a Reynolds number of 3000,
ε is the surface roughness.
The turbulent friction factor is given by the Zigrang and Sylvester (1985) approximation
to the Colebrook-White correlation (Colebrook, 1939). It has the advantage that it
is an explicit relation for the friction factor, while the Colebrook-White correlation is a
transcendental function requiring iteration for the determination of the friction factor.
The friction model applies to unheated surfaces. The isothermal friction factor can be
corrected for the variation of the fluid viscosity near a heated surface using the relationship
used in the VIPRE code (Stewart, 1985).
In TRACE, the Churchill formula (Churchill, 1977) for the friction factor is used
because it applies to all three flow regimes—laminar, transition, and turbulent:
λD = 8
Re
□
□12
+
a + b
ð
Þ3=2
"
#1=12
,
(9.53)

<!-- page 583 (PDF 35) -->
where
a =
2:457 □ ln
Re
□
□0:9
+ 0:27
ε
Dh
□
□
>
>
>
<
>
>
>
:
>
>
>
=
>
>
>
;
,
b =
3:753	104
Re
□
□16
,
Rek = max
10, ρk Vk
j
jDh
μk
□
□
.
Its predictions for the laminar regime are in agreement with Eq. (9.52). The predictions
for transition flow are subject to some uncertainty. However, its accuracy for turbulent
flow(Ebadian andDong,1998) shows amaximum deviationfromtheColebrook-White
equation of about 3.2% for 4000 < Re < 108 and 10·8 < R =D < 0:05.

## 9.7.2 Two-phase flow

For a two-phase flow, the wall friction model based on a two-phase multiplier
approach is used in RELAP5. For the normal pre-CHF flow regimes, the
Lockhart-Martinelli model computes the overall friction pressure drop in terms of
the liquid-alone wall friction pressure drop
dP
dx
□
□
fr,2ϕ
= ϕ2
f
dP
dx
□
□
fr, f
(9.54)
or the vapor-alone wall friction pressure drop
dP
dx
□
□
fr,2ϕ
= ϕ2
g
dP
dx
□
□
fr,g
,
(9.55)
where ϕf and ϕg are the liquid-alone and vapor-alone two-phase Darcy-Weisbach friction
multipliers, respectively. The phasic wall friction pressure gradients are
expressed as
dP
dx
□
□
fr, f
= λ0
f Re0
f
□
□
_m2
f
2Dρf A2
(9.56)
for the liquid alone, and
dP
dx
□
□
fr,g
= λ0
g Re0
g
□
□
_m2
g
2DρgA2
(9.57)

<!-- page 584 (PDF 36) -->
for the vapor alone, where λk0 indicates the liquid- and vapor-alone Darcy-Weisbach
friction factors, calculated at the respective Reynolds numbers
Re0
f = _mf D
μf A
(9.58)
and
Re0
g = _mgD
μgA :
(9.59)
The liquid and vapor mass flow rates, respectively, are defined as
_mf = αf ρf Vf A
(9.60)
and
_mg = αgρgVgA:
(9.61)
The two-phase multiplier ϕf and ϕg is calculated from the Heat Transfer and Fluid
Flow Service (HTFS)-modified Baroczy correlation (Chaxton et al., 1972) in
RELAP5. The individual phasic wall friction components are calculated by apportioning
the two-phase friction between the phases using a technique derived by
Chisholm (1967) from the Lockhart and Martinelli (1949) model. The partitioning
model is based on the assumption that the frictional pressure drop may be calculated
using a quasisteady form of the momentum equation and the effect of individual flow
regime is separately modeled. For example, in a bubbly flow at pre-CHF flow regime,
the void fraction at the wall (αwg) is approximated as the bulk vapor volume fraction
(αg). The wall friction coefficient for wall-gas shear (Cwg) is a function of αwg. This
indicates that the wall friction is partitioned to both liquid and vapor phases in a
bubbly flow.
In TRACE, a similar approach is used for the calculation of wall friction. However,
for the normal pre-CHF flow regimes (bubbly/slug and annular/mist), all of the
wall drag is applied to the liquid phase alone. This is different from that in RELAP5.
Thus,
dP
dx
□
□
fr, f
= ·Cwf Vf
Vf ,
(9.62)
or, in terms of the two-phase multiplier for the liquid phase considered to flow alone in
the channel,
dP
dx
□
□
fr, f
= ·Φ2
f
f2Φ, f Gf
Gf
2Dhρf
"
,
(9.63)
