# Validation of constitutive equations
<!-- source PDF pages 37-38 -->

<!-- page 585 (PDF 37) -->
where the friction factor, f2Φ,l, is calculated with
Re2Φ, f = Gf
Dh
μf
= 1·α
ð
Þρf Vf
Dh
μf
:
(9.64)
The wall drag coefficient is then
Cwf = Φ2
f
f2Φ, f 1·α
ð
Þ2ρf
2Dh
"
:
(9.65)
To complete the specification of the wall drag for the pre-CHF regimes, it remains to
specify the two-phase multiplier, Φ2
f , and the friction factor, f2Φ,f. In TRACE code the
two-phase multiplier Φ2
f is a function of void fraction only, where the function
depends on the flow regime. The friction factor is also dependent on the flow regime.
For two-phase flows with nucleate boiling, the pressure drop data by Ferrell and
Bylund (1966) show that the two-phase multiplier when boiling is present is both significantly
higher and contains a pronounced mass flux effect. Thus, an additional multiplier
is devised to account for the effect.
In horizontal stratified flow, both the liquid and gas phases are in contact with the
pipe wall, so the wall drag coefficient is specified for both phases. For the “inverted”
post-CHF flow regimes, the wall surface temperature is beyond the minimum stable
film boiling temperature, so only the gas phase is in contact with the wall. Consequently
, wall-fluid shear only occurs for the gas phase and Cwf should be zero.
For the pre-CHF flow regimes, the two-phase frictional pressure drop models of the
RELAP5 and TRACE codes are similar to each other, but the partition methods are
different. In RELAP5, the wall friction is partitioned to each phase. Meanwhile, in
TRACE and CATHARE 2, the wall friction is applied to the liquid phase alone for
all the pre-CHF flow regimes. From a physical point of view the latter approach seems
reasonable because the vapor phase does not directly touch the wall. But, this may lead
to the prediction of unphysical results. For example, in the case of a steady-state bubble
flow in a horizontal pipe, simple algebraic operations of the phasic momentum
equations lead to the result that the vapor-phase velocity is greater than the
liquid-phase velocity if Cwg = 0 (Kim et al., 2014). However, the RELAP5 approach,
where Cwg is a nonzero coefficient, yields more reasonable results in this case. Further
study is needed to improve its implementation method.
The two-phase wall friction models for bends, sudden area changes, and helically
coiled tubes need further improvement (Hsu et al., 2015; Colombo et al., 2015),
requiring experimental data and correlations for an extended range of validity.
9.8
Validation of constitutive equations
The V&V process of system TH codes is discussed in detail in Chapter 13. In this
section, validation of constitutive equations is briefly presented.

<!-- page 586 (PDF 38) -->
A system TH code usually adopts a number of mechanistic models and constitutive
equations to represent various two-phase flow phenomena that may be expected to
occur during design-basis accidents or anticipated transients in an light water reactor
(LWR). For example, RELAP5/MOD3.3 adopts more than 200 correlations to represent
two-phase flow and heat transfer processes (USNRC, 1998b). These correlations
have crucial effects on the applicability and accuracy of the code and, thus, all the
correlations should be validated appropriately.
As concerns the validation of the correlations, it should be noted that the calculation
of any two-phase flow process usually needs several relevant correlations. For
example, to predict the subcooled boiling in a vertical pipe, three correlations are
involved at least: wall heat partition, interfacial drag, and interfacial heat transfer. This
indicates the validation or assessment of a correlation cannot be completely separate
but rather synthetic. In addition, we need to be aware that:
(i) Each correlation was developed to represent a single phenomenon based on limited experimental
data set. This leads to the limited range of its applicability.
(ii) The code developers adopt one or several correlations (and combine them) to represent a
phenomenon at all possible flow conditions that may be expected to occur during a transient
. Interpolation of two or more correlations and extrapolated use of a correlation,
although not desirable, might be sometimes inevitable.
(iii) The code users use the codes for their own purposes. When they calculate a specific transient
or accident, the physical phenomena of great interest may change as time goes on
(i.e., as the transient advances). This means the importance of a correlation changes
according to the transient advancement.
These features imply that constitutive equations should be validated in a synthetic
approach. In this regard, the validation of constitutive equations is carried out in
the framework of the code validation using separate effect tests (SETs), where key
two-phase flow and heat transfer phenomena are identified first and thereafter the
code (or the correlations in practice) is systematically assessed against a set of relevant
experimental data.
An internationally agreed SET validation matrix for system TH codes has been
established by the OECD/NEA Committee on Safety of Nuclear Installations
(OECD/NEA, 1993; Aksan, 2008). The construction of such a matrix was an attempt
to collect together in a systematic way the best sets of openly available test data
for code validation, assessment and improvement and also for quantitative code
assessment. The experts identified 67 phenomena relevant to two-phase flow in relation
to LOCAs and transients in LWRs and set up a catalog of information sheets
on the experimental facilities, as a basis for the selection of the facilities and specific
tests. The 67 phenomena involve 9 basic phenomena, which are evaporation due to
depressurization, evaporation due to heat input, condensation due to pressurization,
condensation due to heat removal, interfacial friction in vertical flow, interfacial friction
in horizontal flow, wall to fluid friction, pressure drops at geometric discontinuities
, and pressure wave propagation. All these are related with the constitutive
equations introduced in Section 9.1–9.6. The other 58 phenomena are related with
component-specific two-phase flow phenomena. Finally, they established the SET
cross-reference matrix suitable for the developmental assessment of system TH
