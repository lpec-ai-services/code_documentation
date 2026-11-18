# Interfacial heat and mass transfer
<!-- source PDF pages 16-21 -->

<!-- page 564 (PDF 16) -->
Inthedevelopmentofthetwo-groupIATEs,majordifficultiesarisefromtheexistence
of various types of bubbles and their complicated interactions (Ishii et al., 2005). Interactions
between the bubbles in the same group and those between the bubbles of two different
groups should be modeled, along with intergroup transfer at the group boundary,
due to expansion and compression. It is also important that, in the two-group transport
formulation, the particle distribution function needs to be properly averaged due to the
existence of various types of bubbles in the two-group transport equation.
The source and sink terms of the interfacial area are still being developed, which
are strongly dependent on flow conditions and geometries. So far, most of the experiments
for interfacial area research have been performed in round tubes (Revankar
and Ishii, 1992; Grossetete, 1995; Hibiki et al., 1998, 2001; Hibiki and Ishii, 2000,
2002; Fu, 2001; Ishii and Kim, 2004; Ishii et al., 2005; Yao and Morel, 2004;
Smith et al., 2012a,b), a few in annuli (Hibiki et al., 2003; Jeong et al., 2008; Ozar
et al., 2013a,b; Brooks et al., 2014) and rod bundles (Yang et al., 2013). Experiments
on sudden area changes, elbows, bends, and large volumes are still scarce.
Considering the wide range of flow conditions that the constitutive equations of a system
TH code should cover, it is somewhat premature to use the interfacial area transport
model in a system TH code because of the lack of sufficient data and validated models.
Nevertheless,RETRAN-3D(CS&A,2001)attemptedtoadoptthedynamicflowregime
based ontheIATE,which isdifferent fromEq.(9.18)(Stuhmiller,1986).However,there
has not been sufficient validation work to recommend the model for general use. The
TRACE development roadmap also includes the IATE. In CATHARE 3, the IATE is
under development (Emonot et al., 2009) and to be used when the results are validated
and reliable. It seems that the complete replacement of the flow regime map with IATE
requires substantial work, and will take very long time.
A two-step approach for the future development of IATE is desirable. First, we
need to focus on the in-depth development of the one-group IATE, which allows
us a limited use for a dispersed bubbly flow but brings us enhanced accuracy. Thereafter
, we may proceed with the second step, the development of two-group IATEs,
including the source and sink terms, in parallel with the interfacial area transport
by droplets (Thurgood and George, 1983), to cover all flow regimes. In this step,
the three-field model is naturally to be used at least. Additional efforts are needed
to fit the two-group IATE into the two-fluid or three-field models (Lee et al.,
2013) because only one vapor velocity is defined in the two-fluid model, however,
vapor velocities of two-group bubbles are needed in the two-group IATE. Sun
et al. (2003) and Wang et al. (2011) have suggested some models to implement the
IATE into two-fluid models. These combined efforts will be able to replace the conventional
flow regime map approach with IATEs.
9.4
Interfacial heat and mass transfer
Interfacial heat and mass transfer may occur in the bulk and/or in the thermal
boundary area near the wall (e.g., see Fig. 9.10). The former results from energy
exchange
between
the
two
phases,
determining
the
level
of
thermal

<!-- page 565 (PDF 17) -->
nonequilibrium, while the latter is due to heat transfer at the wall. Even when the
bulk liquid temperature is lower than the local saturation temperature, the liquid
in the thermal boundary layer near the wall can be superheated, which may lead
to subcooled boiling. The same is true for the film-wise condensation at a subcooled
wall. A special model is needed for this, which will be discussed in
Section 9.5. In this section, the interfacial heat and mass transfer in the bulk fluid
is mainly presented. This is one of the two-phase flow phenomena that have great
uncertainties because the fundamental mechanisms are not well understood yet
and direct measurement is nearly impossible.
In the two-fluid six-equation model in RELAP5 (USNRC, 1998a), the total volumetric
vapor generation rate or interfacial mass transfer rate is given by
Γg = Γig + Γw,
(9.20)
where Γg = ·Γf , Γig is the vapor generation rate in the bulk fluid, and Γw is the thermal
boundary area near the wall. Similarly, the vapor-side interfacial heat transfer
rates is given by
Qig = QB
ig + QW
ig:
(9.21)
The liquid vapor-side interfacial heat transfer rate is given by
Qif = QB
if + QW
if :
(9.22)
The bulk interface heat transfer is at the steam-liquid interface in the bulk. This
represents thermal energy exchange between the fluid interface at the saturation
temperature, Ts, and the bulk fluid state. For gas, the bulk interface heat transfer is
given by
QB
ig = Hig Ts ·Tg
□
(
,
(9.23)
Wall
Two-phase flow
Fig. 9.10 Interface heat transfer in
the bulk and near the wall for
subcooled boiling (USNRC, 1998a).

<!-- page 566 (PDF 18) -->
where Hig is the gas interface heat transfer coefficient per unit volume and Tg is the gas
temperature. For liquid, the bulk interface heat transfer is given by
QB
if = Hif Ts ·Tf
□
(
,
(9.24)
where Hif is the liquid interface heat transfer coefficient per unit volume and Tf is the
liquid temperature.
In general, it is assumed for simplicity that the bulk interfacial heat transfer terms
and the near wall energy exchange terms each sum to zero independently. Then,
QB
ig + QB
if + Γig h*
g ·h*
f
□
□
= 0
(9.25)
and
QW
ig + QW
if + Γw h0
g ·h0
f
□
□
= 0,
(9.26)
where h*
g and h*
f are the vapor and liquid enthalpies associated with bulk interface mass
transfer, respectively. They are defined in such a way that the interface energy jump
conditions at the liquid-vapor interface are satisfied. In particular, h*
g and h*
f are chosen
to be hg
s and hf, respectively, for the case of vaporization, and hg and hs
g, respectively,
for the case of condensation, where the superscript s indicates saturation. The same is
true for the phasic enthalpies h0
g and h0
f associated with wall (thermal boundary layer)
interface mass transfer.
It is also assumed that vapor appears (or, is generated) at saturation, and it follows
that QW
ig = 0 for boiling processes in the boundary layer near the wall (i.e., subcooled
boiling). Thus, Eq. (9.26) can then be used to solve for the interface vaporization rate
in the boundary layer near the walls (see Section 9.5):
Γw =
·QW
if
h0
g ·h0
f
:
(9.27)
Similarly, since it is assumed that liquid appears at saturation, it follows that QW
if = 0
for condensation processes in the boundary layer near the wall. Eq. (9.26) can then be
used to solve for the interface condensation rate in the boundary layer near the walls:
Γw =
·QW
ig
h0
g ·h0
f
:
(9.28)
Using the above equations, total interfacial mass transfer rate is then represented by
Γg = ·Hig Ts ·Tg
□
(
+ Hif Ts ·Tf
□
(
h*
g ·h*
f
+ Γw:
(9.29)
Eq. (9.29) shows that the interfacial mass transfer rate is directly related with the interfacial
heat transfer rate.

<!-- page 567 (PDF 19) -->
Note that the interfacial heat transfer coefficient (IHTC) per unit volume (Hik) in
Eq. (9.29) is generally given by
Hik = hikai,
(9.30)
where hik is the IHTC and ai is the IAC. The former requires special models, which are
empirical, semiempirical, or ad hoc. The IAC is mechanistically modeled, which
depends on the flow regime. For the combined flow regimes, such as slug flow or
annular-mist flow, the effects of two flow regimes are separately taken into account.
For example, in the case of annular-mist flow, Hik, is given by
Hik = hfilm
ik afilm
i
+ hdrop
ik
adrop
i
,
(9.31)
where the terms in the right-hand side indicate the contributions by liquid film and
droplets, respectively.
The IAC models are similar in various system TH codes. For bubbly and mist flow
regimes, the model is rather clear. According to Wallis (1969) and Shapiro and
Erickson (1957) the dispersed bubbles or droplets can be assumed to be spherical particles
with a size distribution of the Nukiyama-Tanasawa form (USNRC, 1998a).
Using the Nukiyama-Tanasawa distribution function, the IAC can be obtained as:
ai = 3:6α
do
,
(9.32)
where α = αg for bubbles and α = αf for droplets. The average diameter do is obtained
by assuming that do=dmax/2. The maximum diameter, dmax, is related to the critical
Weber number, We, by
We = dmaxρc vg ·vf
□
(2
σ
,
(9.33)
where σ is the surface tension and ρc is the continuous-phase density. The values for
We are presently taken as
We =
10 for bubbly flow,
for mist-pre-CHF flow,
12 for mist and mist-post-CHF flow:
>
<
>
:
(9.34)
Similarly, the IACs for other regimes can be modeled. For slug flow regime, the
Taylor bubble and small bubbles are separately modeled. For annular-mist flow
regime, liquid film and droplets are separately modeled, where the IAC by droplets
is obtained by using Eqs. (9.32), (9.33). For inverted flow regimes, the effects of liquid
core, liquid slug, and droplets are separately taken into account. Table 9.2 summarizes
the IAC model in the RELAP5 code (USNRC, 1998a).

<!-- page 568 (PDF 20) -->
The IHTCs are rather complicated because of fundamental difficulties in experimental
observation and modeling. In the RELAP5 code, the interfacial heat transfer
is split into four cases for each flow regime based on fluid temperature: superheated
liquid (SHL), subcooled liquid (SCL), superheated gas (SHG), and subcooled gas
(SCG). In each regime, correlations for the four cases are provided and some of
the correlations are reused.
Table 9.2 The IAC model in the RELAP5 code
Flow
regime
Interfaces
Interfacial area concentration (ai)
Bubbly
Small
bubble, ai
ai = 3:6α
d0
, α = αg for bubbles and α = αf for droplets
where
d0=average bubble diameter=(1/2)dmax,
dmax =
Weσ
ρc Vg ·Vf
□
(2, We=10.0.
Slug
Taylor
bubble,
ai,Tb
ai,Tb = αb
L +
3:6αgs
d0
□
□
1·αb
ð
Þ
where
αb = αg ·αgs
1·αgs
,
L: cell length,
αgs = αBS exp ·8
αg ·αBS
αSA ·αBS
□
□
.
Small
bubble,
ai,bub
ai,bub = 3:6α
d0
Annular
mist
Film and
droplets
ai =
4Cann
D
□
□
1·αff
□
(1=2 +
3:6αfd
d0
□
□
1·αff
□
(
where
Cann: roughness parameter
αfd = αf ·αff
1·αff
,
αff =
αf Cf exp ·7:5	10·5 αgvg
uc
□
□6
"
for vertical flow,
αf Cf exp ·4:0	10·5
Vg ·Vf
vgL
□
□6
"
for horizontal flow,
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
:
Cf = 1:0·10·4
αf ρf vf
 D
μf
!0:25
,
uc: the critical entrainment superficial velocity,
vgL: the horizontal stratification critical velocity

<!-- page 569 (PDF 21) -->
In the bubbly flow regime, for a condition of SHL, the interfacial heat transfer is the
larger of either the model for bubble growth developed by Plesset and Zwick (1954) or
the model for convective heat transfer for a spherical bubble (modified by Lee and
Ryley, 1968).
For the bubbly flow regime with a condition of SHG, an IHTC is assumed that is
high enough that the vapor temperature will relax toward the equilibrium (saturation)
condition—hig is set to 104 W/m2 K. The same model is used for the bubbly flow
regime with a condition of SCG.
Analogously, in the mist flow regime for the condition of SHG, a convective heat
transfer model for a spherical droplet (Lee and Ryley, 1968) is used for the IHTC. For
mist flow with SHL, it is assumed that the IHTC is high enough so that the liquid temperature
will relax toward the equilibrium (saturation) condition.
In the bubbly flow regime for the SCL condition, the interfacial heat transfer is
calculated by the modified Unal bubble collapse model (Unal, 1976; Riemke,
1993) and the Lahey model (Lahey, 1978).
In the slug flow regime, the interfacial heat transfers at the Taylor bubbles and the
small bubbles are separately modeled. The large IHTC is used for Taylor bubbles to
bring the vapor phase to saturation quickly. In the annular-mist flow regime, the interfacial
heat transfers at the annular film and droplets are separately modeled. For the
subcooled liquid condition, the interfacial mass transfer is calculated by the modified
Table 9.2 Continued
Flow
regime
Interfaces
Interfacial area concentration (ai)
Horizontal
stratified
Horizontal
surface, ai
ai = 4Cst
sin θ
πD
where Cst: roughness parameter
Inverted
annular
Small
bubble,
ai,bub
ai,bub = 3:6αgb
d0
1·αB
ð
Þ
where
αgb = αg ·αB
1·αB
,
αgb: the vapor/gas void fraction in the liquid core,
d0 : thebubble diameter, We = 10:0,
αB: the fraction of the total area occupied by the vapor/gas
annulus.
Liquid
core, ai,ann
ai,ann = 4
D 1·αB
ð
Þ1=2
Mist
Droplets, ai
ai = 3:6α
d0
where
We = 3:0 and μm =
μg
αg
□
(2:5 for mist pre-CHF,
We = 12:0 and μm = μg for mist and mist post-CHF.
