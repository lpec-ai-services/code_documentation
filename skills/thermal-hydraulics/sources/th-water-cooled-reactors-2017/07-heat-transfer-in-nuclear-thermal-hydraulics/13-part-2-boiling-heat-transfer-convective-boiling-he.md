# Part 2: Boiling Heat Transfer — Convective boiling heat transfer in channels — Developed boiling in channels in subcooled to saturated region
<!-- source PDF pages 100-101 -->

<!-- page 456 (PDF 100) -->
Nu = αid
λf
= 0:166Re0:66Pr0:33 μf =μw
□
□0:14:
The heat transfer coefficient for the flow of subcooled (x=−0.3□0) fluid is given by:
α=αi = 4:13 + 53:89x + 381:38x2 + 1257x3 + 1572:7x4:
From this it follows that when x=0, α=4.13αi; at x=−0.1, α=1.44αi; at x=−0.2,
α=1.04αi.

### 7.8.4 Developed boiling in channels in subcooled to saturated region

The heat transfer coefficient of the forced flow boiling is influenced mainly by two
processes—convection and boiling. It is well understood that the former process
can suppress the latter. There, a magnitude of the heat transfer coefficient can be similar
to that of the convection heat transfer coefficient αc at low heat flux and high
velocity, and the pool boiling heat transfer coefficient α0 at high heat flux and
moderate velocity.
The method proposed by Kutateladze (1979) allows you to take into account the
influences of the flow velocity and heat flux without relying on complicated criteria.
First, heat transfer rates α0 at boiling and αc for turbulent flow convection of the liquid
Fig. 7.56 Boiling onset with different wall temperature peaks (Wadekar, 1993). Temperatures:
□—wall; □—the average flow; l—saturation; - - - calculated temperature profile.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 457 (PDF 101) -->
at TS are compared. That is, depending on the ratio α0/αc the following equations are to
be used:
α0=αc < 0, α = αc;
(7.150)
0:5 < α0=αc < 3, α=αc =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + Cα=αc
ð
Þ2
q
;
(7.151)
α0=αc > 3, α = α0 or α = 0:9α0:
(7.152)
Here α is the heat transfer coefficient for the considered mode, αc is the convective
heat transfer coefficient calculated according to the formulae. In Eq. (7.151), C
is a function of p and, for p<15 MPa, is 0.8–0.9. According to Kutateladze,
Eq. (7.152) is applicable to the nucleate boiling of water at TS and to the subcooled
boiling. Eqs. (7.150)–(7.152) are applicable for p=2–20 MPa and are accurate within
□35%. A similar approach is found in Wadekar (1990).
Instead of the formula (7.151), Yagov et al. (1998) recommended a formula that
gives the best agreement with experiment for the case of boiling in a large volume
of water:
α=αc =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
α0=αc
ð
Þ3 + 1 + ΔTS=ΔT
ð
Þ3
3q
;
(7.153)
ΔTS = TS −Tf ; ΔT = Tw −Tf :
When a two-phase mixture flows in a pipe or annular channel, heat transfer coefficients
are calculated according to the formula obtained in CKTI4 by Borishanskii
et al. (1973) and Handbook (1986):
α = α1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + 7□10−9 Δhfgρf Jcм
q
□
(3=2 0:7α0
α1
□
(
s
,
(7.154)
where α1 =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
α2
c + 0:7α0
ð
Þ2
q
, αc is the heat transfer coefficient of single-phase flow at
the velocity w0 in a pipe or channel; α0 is the heat transfer coefficient of the pool boiling;
JCM = Jf0 + Jg0 isthemixturevolumetricfluxwhereJf0 = G 1−x
ð
Þ=ρf and Jg0 = Gx=ρg;
x is the mass quality. The range of application for water is p=0.2–17 MPa;
Jcм=1–300 m/s; q=0.08–6 MW/m2.
Influence of the mixture velocity becomes notable, when the following relation is
true:
Δhfgρf JCM=q
□
□
· 0:7α0=α1
ð
Þ4=3 > 5□104. In this case the heat transfer coefficient
is in proportion to the mass flux to the 0.8th power, i.e., α □ W0:8. At lower values
4Former CKTI, Central Boiler and Turbine Institution in Russia (http://english.ckti.ru/about.html),
Currently, I.I.Polzunov Scientific and Development Association on Research and Design of Power
Equipment.
