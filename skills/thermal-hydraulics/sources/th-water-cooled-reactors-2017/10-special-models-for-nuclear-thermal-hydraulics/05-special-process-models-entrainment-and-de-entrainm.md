# Special process models — Entrainment and de-entrainment
<!-- source PDF pages 13-15 -->

<!-- page 607 (PDF 13) -->
many phenomena including the depressurization rate, the TPCF at the break, the
pressure drops inside the vessel and the heat transfer from the reactor pressure vessel
(RPV) walls. The last phenomenon is also known as the “hot wall delay.” The
design of ECCS and its capability to cool the core became of concern in reference
to the inability to cool the core during the LBLOCA fast depressurization observed
in the experiment. Subsequent deep analyses with continuous experimental support
continued until the availability of the full-scale UPTF experiments in Germany
(Damerell and Simons, 1992).

## 10.2.3 Entrainment and de-entrainment

Nuclear reactor system has entrainment and de-entrainment phenomena taking place
in different components such as core, steam generators, steam separator in BWR, and
suppression pool. There are three scenarios—one in which the gas bubbles out from
the interface, second, where the gas flows parallel to the interface and third, where
water is separated by centrifugal forces such as in BWR separator/dryer and steam
generator secondary side.
The phenomena of entrainment and de-entrainment are important as they affect the
distribution of liquid in gas phase, and affect the interfacial energy, mass, and momentum
transfer through the shape and size of the interface. These phenomena occur at the
interface between gas and liquid phases. The mechanism for entrainment and
de-entrainment is different. The entrainment occurs due to relative velocity between
gas and liquid leading to instabilities at the interface. The peaks in the waves are broken
by the gas phase and results in liquid entrainment. This captured liquid may break
up further until stable drop size is achieved.
–6500
–6000
–5500
–5000
–4500
–4000
–3500
–3000
–2500
–2000
–1500
–1000
–500
90°
360°
Height (mm)
BR
270°
180°
Fig. 10.5 Flow in downcomer detected in UPTF.

<!-- page 608 (PDF 14) -->
There are many mechanisms of de-entrainment. In the case of horizontal flow of
gas and droplet over an interface, any decrease in air velocity will decrease the shear
between the gas and droplets, leading the droplets to be deposited on the interface. In
the case of vertical flows, there is continuous impingement of droplets on the interface
along with creation of entrainment from wavy interface. As gas slows down,
the waviness will decrease, the entrainment will decrease, with a net effect of
de-entrainment exceeding entrainment. In addition, if there are many steps or barriers
in flow direction, the droplet will impinge and separate from the gas-droplet
mixture. While gas can change direction, the droplets due to larger momentum cannot
easily change the direction and impinge on the barriers. Grid spacers in the core
act as a separator for droplets. These droplets impinge on solid surfaces of heated
rods during accidents, providing precursor cooling prior to full-scale reflood. The
phenomena of entrainment are at localized process level and generally not modeled
by first principle in the system codes. Instead, the codes use correlations for net
entrainment.
The system codes such as TRACE and RELAP5 have correlation for entrainment
fraction, E∞based on Ishii and Mishima correlation (Ishii and Mishima, 1989):
E∞= tanh 7:25*10□7We1:25
g
Re0:25
f
h
i
where
Weg =
ρgj2
gDh
σ
Δρ
ρg
!1=3
Ref = 1□α
ð
ÞρlVlDh
μl
As can be seen the entrainment is based on local Weber number and Reynolds
number, and depends on the diameter of the tube. The interface instabilities generally
depend on the thickness of the film. Film thickness will be larger for larger
diameter pipes for same void fraction and is more likely to have instability at the
interface.
The other mechanism of entrainment is when gas bubbles emerge from the interface
and as they leave the interface, a liquid filament is created that breaks and leads to
drops. The drops have some momentum from the gas phase. However, some of the
drops can fall back to the interface. A good review of this type of entrainment was
provided by Bagul et al. (2013) and Ishii and Kataoka (1984). As in this situation,
the liquid phase is stagnant except for activity at the interface, the entrainment ratio,
Efg (h, Jg), is defined differently (see Fig. 10.6). It is the ratio of gas phase supplied and
liquid entrained above the interface. The ratio of liquid entrainment and gas flow is
shown here as function of gas space height, h. Droplets can fall back for large gas
space above interface.

<!-- page 609 (PDF 15) -->
Near interface,
Efg h, Jg
□
□
= 4:84*10□3
ρg
Δρ
□
□□1
Deposition controlled region
Efg h, Jg
□
□
= 7:13*10□4J*3
g N0:5
μg
ρg
Δρ
□
□□0:31
exp □0:205 h
Dh
□
□
For intermediate region, the entrainment depends on momentum exchange and the
rate is given for three different gas flow rates. For high gas flows the correlation near
the interface applies.
For low flows the correlation is as follows.
Efg h, Jg
□
□
= 2:21N1:5
μg *D*1:25
h
ρg
Δρ
□
□□0:31
J*
gh*□1
Forintermediateflows,J*
gh*□1 > 6:39*10□4,adifferentcorrelationwasrecommended:
Efg h, Jg
□
□
= 5:42*106J*3
g N0:5
μg
ρg
Δρ
□
□□0:31
D*1:25
h
Deposition controlled region
Near surface region
(without deposition)
h ⇒
Efg (h, Jg) ⇑
Momentum controlled region
(with deposition)
Fig. 10.6 Regions of entrainment above the separation interface.
Taken from Ishii, M., Kataoka, I., 1984. Mechanistic modeling of pool entrainment
phenomenon. Int. J. Heat Mass Transf. 27 (11), 1999–2014.
