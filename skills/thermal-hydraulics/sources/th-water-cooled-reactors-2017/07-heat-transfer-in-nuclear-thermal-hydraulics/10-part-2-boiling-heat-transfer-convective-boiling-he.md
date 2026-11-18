# Part 2: Boiling Heat Transfer — Convective boiling heat transfer in channels — Boiling modes in flow channels
<!-- source PDF pages 92-97 -->

<!-- page 448 (PDF 92) -->
p—pressure; b =
TS −Te
2 1−ρg=ρf
□
□ is the coefficient taking into account the effect of pressure
and subcooling; Φ =
we=0:61
ð
Þ0:47 for we □ 0:61m=s
1:0
for we < 0:61m=s
□
is the coefficient reflecting the
effectsofthedetachmentspeedanddiameterd;we—velocityofthewater;F1 = n πd4=4
□
□
isthe
fraction of the surface projected by the vapor bubbles; n—number of vapor bubbles on the unit
surface: n = 1
d2
2σTS
TW −TS
ð
ÞρgΔhfg
"
#−4:4
f ρ*
ð
Þ, where ρ* = ρf −ρg
□
□
=ρg = ρf =ρg
□
□
−1; Δhfg
is
the
heat
of
vaporization;
f ρ*
ð
Þ = 2:157□10−7 ρ*
ð
Þ−3:2 1 + 0:0049ρ*
ð
Þ4:13;
and
a =
q−αf Tw −Te
ð
Þ
□1=2λ
2c1=3Δhfg
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
πλf = ρf cpf
□
□
q
ρg
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
λWρWcpW
λf ρf cpf
s
; c = Δhfgμf cp=0:013Δhfg · Pr1:7
□3
σ=Δρg
ð
Þ0:5
.
3. The amount of heat used for the evaporation:
Qe = nf π
6d3
□
□
Δhfgρg:
(7.145)
4. The amount of heat being carried by turbulent flow natural convection:
Qc = St · ρf cpf we Tw −Tf
□
□
1−F1
ð
Þ:
(7.146)
From experiment Tw=f(τ)—the transient surface temperature measurement enables
calculation of the heat transfer coefficient α=f(τ), due to α □ ∂ Tw −Tf
□
□
∂τ
. Qualitatively
, a variation of the heat transfer coefficient is shown in Fig. 7.51 (Gilles
et al., 2002).

## 7.8 Convective boiling heat transfer in channels

### 7.8.1 Boiling modes in flow channels

Different types of flow regimes and modes of heat transfer in a vertical heated tube are
shown in Figs. 7.52 and 7.53. Fig. 7.52 shows the flow conditions and heat transfer
modes in a uniformly heated tube (q=const). The figure has been cited in many
reports and books on two-phase flow and heat transfer (e.g., Wallis, 1972;
Mandhane et al., 1974; Butterworth and Hewitt, 1977), which was adopted originally
from Tong (1965). Fig. 7.52 is from its second edition by Tong and Tang (1997), and is
self-explanatory, as it contains all the necessary information in the figure.
Fig. 7.53 shows a change in the flow patterns of two-phase flow in a long pipe with
increasing heat flux from left to right, with the fluid inlet temperature and mass
flow rate and the system pressure constant. In the single-phase flow region (region
1), while the liquid on the wall surface may be heated up to the saturation temperature,
the wall temperature is still below the value required for vaporization in the presence
of the convective heat transfer. Just downstream of the region 1, the fluid at the wall
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 449 (PDF 93) -->
becomes superheated such that evaporation occurs in the micro cavity centers,
although the bulk flow is still subcooled, i.e., below the saturation temperature. This
is an area of nucleate boiling of the subcooled liquid (2a). The difference between the
saturation temperature and the mass-average temperature of the liquid is called subcooling
TS −Tf = ΔTsub. The upper boundary of the region 2a in Fig. 7.53 corresponds
to the vapor quality x=0. This portion of the liquid is heated to the saturation temperature
so that the average liquid-vapor flow enthalpy is equal to that of saturated
liquid (hf,sat). In the nucleate boiling of the saturated liquid region (2b) as well as
in the subcooled boiling region, equilibrium steam quality (or relative enthalpy) at
a distance z is determined by the heat balance x zð Þ = h zð Þ−hf,sat
=Δhfg where
h(z) is the mixture enthalpy and Δhfg is the latent heat. With this definition, it may
have a negative or positive value.
With increasing steam quality, plug or slug flow regime prevails (region 2c). The
upper boundary of this region is in transition to the dispersed-annular flow regime
(region 3) where there is a change in the mechanism of heat transfer. There the process
of boiling is mostly replaced by evaporation. While the boiling can be observed within
a thick liquid film, the bubble generation in the thin liquid film is usually suppressed
and the process of heat transfer cannot be referred to as boiling. The heat is transferred
by the convection from the wall to the interface between liquid and the vapor core
where evaporation takes place. The upper boundary of the region 3 in Fig. 7.53 corresponds
to the complete evaporation of the liquid film and there dominates a
a
Tw,°C
t, s
t, s
Fig. 7.51 Dependence of Tw(τ) and α(τ): 1—film boiling mode; 2—bubbly mode;
3—convective cooling mode.

<!-- page 450 (PDF 94) -->
“Dryout”
Fluid temp
Wall and fluid
temp variation
Flow
patterns
Heat transfer
regions
Vapor
core temp
Wall
temp
Drop
flow
 Singlephase

vapor
Convective
heat transfer
to vapor
Liquid deficient
region
Fluid temp
Subcooled boiling
Slug
flow
Bubbly
flow
Annular
flow
Liquid
core temp
Wall temp
Sat temp
Singlephase

liquid
Convective
heat transfer
to liquid
Saturated
nucleate
boiling
Forced
convective heat
transfer thro
liquid flim
Annular
flow with
entrainment
Fluid
temp
x=0
x=1
H
G
E
F
D
A
B
C
Fig. 7.52 Flow patterns and modes of heat exchange (q=const) (Tong and Tang, 1997).
Regions of heat transfer in convective boiling in a heated channel with constant heat flux; the
regions A–H are further described in Fig. 7.54.
From Ahmada, M., et al., 2013. Phenomenological modeling of critical heat flux: the GRAMP
code and its validation. Nucl. Eng. Des. 254, 280–290.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 451 (PDF 95) -->
dispersed flow mode with gradual evaporation of droplets in the superheated steam
(region 4), which shifts into the single-phase vapor flow convection mode—region 5.
At the location of the film dry-out, the heat transfer coefficient drops sharply where
with the high heat flux the wall surface temperature may reach unacceptable values
(burnout, crisis). This heat flux is called critical heat flux (qcr). The line between the
areas 3 and 4 corresponds to the critical heat flux associated with the dry-out of the
liquid film.
When q>qcr, the mechanism of the heat transfer varies depending on the boiling
regime, i.e., either DNB, the formation of a conglomerate of bubbles of steam
shielding the surface of the bulk liquid from the heated wall, or the boiling transition
(BT), the liquid film dry-out. Film boiling under the forced convection mode is basically
similar to that observed in the pool boiling. Heated surface is covered with a
vapor film that is of low heat conduction through which the heat must be transferred.
Dependency of the two-phase forced convection heat transfer regimes on the quality
(vertical axis) and heat flux (horizontal axis) is shown in Fig. 7.54 (taken from
Collier and Thome, 1980).
It should be borne in mind that, in Fig. 7.54, the equilibrium quality x reflects only
qualitatively the border areas. Therefore, when x>1 (area 6) a thermodynamically
nonequilibrium vapor flow is possible in the presence of liquid droplets. Then the
boundary between the regions 9 and 6 moves to the right.
Since the void fraction (φ) in the flow determines the flow and heat transfer modes,
it is advisable to consider the actual steam quality that takes into account the nature of
Fig. 7.53 Different flow patterns of two-phase flow in a long pipe (constant: pressure, mass
flow rate, inlet enthalpy) by Hewitt and Hall Taylor (1972): 1—single-phase liquid flow;
2—bubbly, slug; 3—annular-dispersed; 4—mist; 5—single-phase vapor flow.

<!-- page 452 (PDF 96) -->
the change in φ along the channel (for example, q=const), instead of the equilibrium
steam quality xe, as depicted in Fig. 7.55.
First, vapor bubbles appear at the location “ib.” Moving through, or migrating away
from the thin boundary layer near the wall surface, the vapor bubbles condense in a
bulk of highly subcooled liquid. Here, the void fraction is low, because the growth of
bubble layer is limited by the high level subcooling. As a result, the subcooling
decreases in the flow core and gradually attains the conditions under which the rate
of vapor generation exceeds that of vapor condensation in the stream. From this point
the void fraction begins to increase rapidly, which is considered the beginning of the
vapor generation—nvg (net vapor generation).
The equilibrium quality can be zero (xe=0) in the nucleate boiling (beginning)
region even with significantly high values of the void fraction (φ≫0). Thus, this
mode is under thermodynamically nonequilibrium condition, i.e., where the flow contains
a significant amount of vapor (by volume) in the subcooled liquid as a whole.
A simple calculation assumes that the undeveloped surface boiling starts in the section
in which the surface temperature is saturation temperature TS. Then a magnitude of the
relative enthalpy xib = Δh=Δhfg (i.e., quality) can be evaluated by the convective heat
transfer coefficients αc:
[A]
Single-phase
flowRegion A
Subcooled
nucleate
boiling
Region B [B]
Regions
C and D
Saturated
nucleate
boiling
Two-phase
FC heat transfer
Regions E and F
Liquid
deficient
Region G
Superheated
vapor forced
convection
Region H
Subcooled
Saturated
Superheat
Saturated
film boiling
q
[D]
[C]
x = 0
x = 1
x
Subcooled
film boiling
Fig. 7.54 Heat transfer regions in forced convection; Regions A—H in Fig. 7.52.
1—Single-phase fluid flow; 2—subcooled nucleate boiling (Tf<Ts); 3—saturated nucleate
boiling Tf=Ts; 4—two-phase forced convection heat transfer; 5—liquid deficient region
(degraded heat transfer); 6—superheated vapor forced convection; 7—subcooled film boiling
(Tf<Ts); 8—saturated film boiling Tf=Ts; 9—liquid deficient and heat transfer crisis;
[A]—subcooled CHF by DNB; [B]—saturated CHF by DNB (Tf=Ts); [C]—typical burnout
locus; [D]—CHF by film dry-out.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 453 (PDF 97) -->
–
For longitudinal flow inside and outside a tube or pipe, xib = Δh=Δhfg = −qcp= αcΔhfg
□
□
since Δh = −q cp=αc
□
□
, where q is the heat flux, cp is the heat capacity, αc is calculated
on the basis of the formulas for the single-phase convective heat transfer, Δhfg the latent
heat; and
–
For transverse flow across tube bundles, xib = −6:17Re0:18qcp= αcΔhfg
□
□
, where Reynolds
number (Re) is calculated from the velocity at the narrow gap; αc is the convective heat
transfer coefficient for cross-flows in the bundle.
Recently proposed method of calculating the heat transfer in the boiling channels
consists of the following three modes (Kandlikar, 1990, 1991, 1998):
–
Partial (or undeveloped) boiling at qualities xib < x < xdnb (region 2 in Fig. 7.55) where xib
corresponds to the quality at beginning of nucleate boiling and xdnb the developed nucleate
boiling;
–
Fully developed boiling at x > xdnb (region 3 in Fig. 7.55);
–
Mode of a high steam quality for x > xnvg, starting from the point of beginning net vapor
generation (xnvg) where
Distance from the inlet (z)
Flow rw
Uniform heat flux q
ib
nvg
dnb
Quality (x)
xe=xa
zEq
zdnb
zxe=0
zib
xa
xe
xe=0
x=0
Fig. 7.55 Vapor quality, flow conditions and heat transfer. xa—actual vapor quality;
xe—equilibrium quality; 1—single-phase flow forced convection; 2—nucleate boiling
(developing); 3—developed nucleate boiling; 4—subcooled boiling; 5—saturated boiling
(thermally equilibrium for z > zEQ). ib—incipient boiling initiation; nvg—net vapor generation;
dnb—developed nucleate boiling; zxe =0—distance from the heated section inlet to the point
xe = 0 at which saturated nucleate boiling to begin, but the liquid is still below the saturation
temperature. zEq—distance to the point of xa = xe where all the liquid is at the saturation
temperature.
FiguremodifiedbasedonCollier,J.G.,1981.ConvectiveBoilingandCondensation.McGraw-Hill,
New York.
