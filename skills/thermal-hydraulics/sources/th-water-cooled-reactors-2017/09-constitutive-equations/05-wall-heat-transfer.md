# Wall heat transfer
<!-- source PDF pages 29-32 -->

<!-- page 577 (PDF 29) -->
For nonvertical slug flow, slug flow for nonvertical geometry is modeled as a series
of Taylor bubbles separated by liquid slugs containing small bubbles. The effects of
Taylor bubbles and the small bubbles are separately modeled (see also Table 9.2 for
the IAC). The drag coefficient for the Taylor bubbles in nonvertical slug flow is given
by Ishii and Chawla (1979):
CD = 10:9 D0
D
□
□
1·αb
ð
Þ3,
(9.44)
where D0 is the Taylor bubble diameter and αb is the void fraction of a single Taylor
bubble in the total mixture. The drag coefficient for small bubbles in nonvertical slug
flow is again given by Eq. (9.42).
Similarly, annular-mist flow is characterized by a liquid film along the wall and a
vapor core containing entrained liquid droplets. The IAC model is presented in
Table 9.2. The interfacial friction factor of the liquid film is described by a standard
correlation in the laminar region and is based on Wallis’s correlation in the turbulent
region. The values of CD are
CD
=
Reg
for Reg □ 500,
1500·Reg
□
□ 64
Reg
+
Reg ·500
□
□
0:02 1 + 150 1· 1·αff
□
□1=2
□
for 500 < Reg < 1500,
0:02 1 + 150 1· 1·αff
□
□1=2
□
for Reg □ 1500,
>
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
>
:
(9.45)
where
Reg = ρg Vg ·Vf
Dg
μg
,
Dg = α1=2
g D is the equivalent wetted diameter.
The drag coefficient for droplets is again given by Ishii and Chawla by Eq. (9.42).
9.6
Wall heat transfer
The constitutive equations to represent wall heat transfer are of great significance in
system TH codes. They link the governing equations for two-phase flow and the heat
conduction equations for fuel rods, heat exchangers, and structures. The constitutive
equations for radiation heat transfer are not discussed here, which becomes increasingly
important in film boiling, particularly when surface temperature is greater than
≡1000 K.
Wall heat transfer is dependent on the flow channel geometry, flow regime, relative
wall temperature, etc., which results in very complicated logics for selecting

<!-- page 578 (PDF 30) -->
appropriate heat transfer models. Roth and Aydogan (2014b) outlined the wall heat
transfer models of various system TH codes. RELAP5-3D implements specific
models for pipes, parallel plates, rod bundles, swirl tubes, horizontal plate, and annuli.
TRACE has specific correlations for four geometries: rods, plates, cylinders, and tube
bundles. RELAP5-3D uses 31 heat transfer models to represent 12 heat transfer
modes. On the other hand, TRACE has 20 heat transfer models for 11 heat transfer
modes. CATHARE 2 takes a relatively simple approach—eight heat transfer models
for six heat transfer modes, considering three geometries of rods, plates, and cylinders.
Considering the complexity of the wall heat transfer models, RELAP5 was selected
here to illustrate how they are implemented in a system TH code.
In RELAP5, the total wall heat flux q00
W
□
(
is the heat flux to the vapor plus the heat
flux to the liquid:
q00
W = hwg TW ·Tref,g
□
(
+ hwf TW ·Tref, f
□
(
,
(9.46)
where
hwg is the heat transfer coefficient to gas,
hwf is the heat transfer coefficient to liquid,
Tw is the wall temperature,
Trefg is the gas reference temperature,
Treff is the liquid reference temperature.
The reference temperatures can be the local gas or liquid temperature or the saturation
temperature, depending on the heat transfer coefficient correlation being used.
The RELAP5 wall heat transfer correlations are based mainly on internal flow in
pipes. Additional geometries considered are vertical parallel plates, vertical and horizontal
tube bundles and horizontal flat plates. RELAP5 has a reflood heat transfer
model developed by the Paul Scherrer Institute in Switzerland (Analytis, 1996).
For a reflood heat structure where heat conduction to both axial and radial directions
is allowed, the same wall heat transfer logic is used as for other surfaces.
A boiling curve is used in RELAP5 to select the wall heat transfer correlations
when the wall surface temperature is above the saturation temperature (superheated
relative to the saturation temperature based on total pressure). When a hydraulic volume
is voided and the adjacent surface temperature is subcooled, steam condensation
on the surface is predicted. If noncondensable gases are present, the phenomena are
more complex, because while boiling is a function of the wall superheat based on the
total pressure, condensation is based on the partial pressure of steam. When the wall
temperature is less than the saturation temperature based on total pressure, but greater
than the saturation temperature based on steam partial pressure, a convection condition
exists. Fig. 9.11 illustrates these three regions.

## 9.6.1 Convection region

In the convection region, the heat transfer coefficient to liquid is the maximum among
those for forced convection, laminar convection, and natural convection. The correlations
are by Dittus and Boelter (1930), Kays (1955), and Churchill and Chu (1975a,b),

<!-- page 579 (PDF 31) -->
respectively. For parallel plates the Petukhov correlation (Petukhov, 1970) is used in
place of the Dittus-Boelter correlation, and the Elenbaas correlation (Incropera and
DeWitt, 1990) is used instead of the Churchill-Chu correlation.
For vertical bundles, the turbulent convection coefficient is multiplied by the
tube pitch-to-diameter ratio as suggested by Inayatov (1975). Horizontal bundles in
RELAP5 differ from pipes in their nucleate boiling, critical heat flux, and natural
convection prediction methods. Nucleate boiling predictions follow the Polley-
Ralston-Grant method (Polley et al., 1981) and the prediction of critical heat flux uses
the Folkin-Goldberg method (Folkin and Goldberg, 1980). Horizontal bundles use the
Churchill and Chu (1975a,b) horizontal cylinder correlation.

## 9.6.2 Boiling region

The boiling curve uses the Chen (1966) boiling correlation up to the critical heat flux
point. A table lookup method developed by Groeneveld et al. (1986) is used for the
prediction of the critical heat flux. When the wall superheat exceeds the critical value,
the heat flux for both the transition boiling and the film boiling regimes are calculated
and the maximum value is used. This eliminates the need to predict a minimum film
boiling temperature. The Chen-Sundaram-Ozkaynak correlation (Chen et al., 1977) is
used for transition boiling and a modified Bromley correlation (Bromley, 1950) is
used for film boiling.
The post-CHF heat transfer regimes mainly determine the PCT at the reflood phase
of an LOCA in a PWR (Choi and No, 2012). They, besides droplet behaviors at that
time, still have great uncertainties.
When the wall temperature exceeds that for the onset of nucleate boiling, but the
bulk liquid is subcooled, subcooled nucleate boiling occurs. In this situation, the wall
Condensing region
Convection region
Heat flux
Nucleate
Transition
Film
Boiling region
CHF
point
Fig. 9.11 The RELAP5 wall heat transfer curves.

<!-- page 580 (PDF 32) -->
heat can be transferred to liquid phase only in the two-fluid formulation, but a portion
of the wall heat flux is spent for vapor generation in the boundary layer near the wall.
To obtain the fraction of the heat flux which causes vapor generation near a superheated
wall, the Lahey method (Lahey, 1978) is used in RELAP5. The resulting vapor
generation rate is given by:
Γw =
q00Aw
h0
g ·h0
f
□
□Mul,
(9.47)
where
q00 is the total wall heat flux,
Aw is the wall surface area,
V is the cell volume,
Mul =
hf ·hcr
hs
f ·hcr
□
□
1 + ε
ð
Þ
,
hcr is the critical enthalpy for net voids calculated using the Saha-Zuber correlation (Saha
and Zuber, 1974),
ε =
ρf hs
f · min hf , hs
f
□
□
h
i
ρghfg
, a pumping factor.
It was shown by Hari and Hassan (2002) that the Lahey’s formulation underpredicts
void fraction at low-pressure conditions. They recommended the Bowring’s and
Zeitoun and Shoukri’s pumping factor formulations (Collier and Thome, 1994) for
low-pressure conditions.

## 9.6.3 Condensing region

There are two methods available for calculating the condensation heat transfer
coefficients for all geometries. The default method uses the maximum of Nusselt
(1916) and Shah (1979). When noncondensable gases are present, the default method
uses the Colburn and Hougen (1934) iteration method to solve for the interface temperature
between the steam and liquid, and uses this value in the heat flux calculation.
The alternate method uses Nusselt’s laminar film coefficient modified for gas turbulence
and noncondensable gases, using the multipliers developed by Vierow and
Schrock (1992).
In the TRACE code, the total wall heat flux q00
W
□
(
is represented by
q00
W = hwf TW ·Tf
□
(
+ hwsat TW ·Tsat
ð
Þ + hwg TW ·Tg
□
(
:
(9.48)
The second term in the right-hand side is used to represent the subcooled boiling,
where the Lahey model is adopted. In Eq. (9.46), the wall heat transfer to liquid
contains the subcooled boiling effect. Thus, Eqs. (9.46), (9.48) are actually
the same.
