# Concepts involved in heat transfer developments
<!-- source PDF pages 16-20 -->

<!-- page 104 (PDF 16) -->
two phases to have unequal velocities and temperatures and it has the capability of
building a more accurate picture of the thermal-hydraulic behavior of the scenario.
This is the approach followed in most of the system codes used today.
Summarizing, since the so-called system codes are considered to be the main repository
of expertise in the field of thermal hydraulics of nuclear systems, they are a reliable
picture of the current option in the area. Such codes usually employ quite
complex techniques that are nonhomogeneous and nonequilibrium two-phase flow
models. Their two-fluid equations are formulated using volume and time-averaged
parameters of the flow. Friction and heat transfer are formulated using bulk properties
and empirical heat transfer coefficients. Flow regime information is supported by
empirical results and accurately implemented.
3.3
Concepts involved in heat transfer developments

## 3.3.1 Context

### 3.3.1.1 Importance of heat transfer developments

The analysis of water reactors thermal hydraulics needs to consider heat transfer
mainly in fuel elements in order to produce results needed by safety analysis
(Kutateladze, 1963). Predictions of temperature distributions in fuel pins and reactor
structures must be accurate since acceptance criteria of safety analysis are defined by
means of limiting values of thermal parameters.

### 3.3.1.2 Scope

Most of the results needed by safety analysis and dealing with heat transfer are related
to fuel. As a consequence, most of the efforts dedicated to improve predicting capabilities
are also devoted to fuel. Heat transfer in fuel includes heat conduction, heat
convection, and heat radiation.
Other areas and components of power plants are also needed for heat transfer
calculations, among them: passive heat structures, electrical heaters, heat losses to
environment, and heat exchangers.
Passive heat structures are usually metallic structures like the internals of reactor
vessel or vessel walls or others in contact with the fluid of the analyzed system.
Despite being passive, which means that they are not generating heat, the need of
taking them into account is that they have an impact on certain scenarios storing thermal
energy in certain periods of the transient and releasing it later.
Electrical heaters, like pressurizer heaters, are important for energy balances and
for controlling pressure.
Heat losses to environment are sometimes negligible, for instance in a full size
plant, but in experimental facilities this is not the case.
Finally, heat exchangers, mainly SGs, are crucial in many scenarios. Sometimes they
are the essential components useful to perform an emergency function, and sometimes
they are the components in which the initiator takes place, like in SG tube rupture.

<!-- page 105 (PDF 17) -->
### 3.3.1.3 1D/3D

The decision of using 1D or 3D option for a given calculation is rarely straightforward.
3D options could be better as a general statement since they are more detailed but
sometimes it is not the case either because they do not add any specific interesting
output to the established engineering goals or because their validation process is
not complete and so their results are uncertain.
Heat transfer in nuclear fuel is a case in which 1D options work properly for many
significant scenarios. Given the geometry and dimensions of a fuel rod, it is quite
correct to consider that heat is transferred following the radial direction and almost
no axial transfer takes place. This statement is valid for most of the involved scenarios.
Reflood situations are identified as different. During the reflood cold water fills only
the lower part of the vessel while most of the core is noncooled and at high temperature
. The axial temperature gradient is high and axial heat conduction is considerable,
so a 3D option is needed.
Using 1D or 3D option is a decision to be made case by case.

### 3.3.2 3.3.2.1 Related to power generation

Three different parameters are helpful for dealing with power generated or transferred:
volumetric power, heat flux, and linear power.
Volumetric power (q000) is the thermal energy generation rate per unit of volume.
Usually defined for the fuel pin, it is used in the general equation of heat conduction.
Heat flux (q00) is the rate of thermal energy transferred through a surface per unit of
area. Usually defined for cladding surface, it is used to evaluate heat transfer by
convection.
Linear power (q0) is the thermal energy generation rate per unit of length of fuel
rod. It is often used in safety statements.

### 3.3.2.2 Related to heat conduction

The general equation of heat conduction is obtained combining Fourier’s law
Heat flux = □K temperature gradient
ð
Þ
q00 = □KrT
with a balance equation
q000 r, t
ð
Þ□rq00 = δ=δt ρcT
ð
Þ
q000 r, t
ð
Þ□r □Kr T r, t
ð
Þ
ð
Þ
ð
Þ = δ=δt ρcT
ð
Þ
where K is the thermal conductivity and c is the specific heat of the solid where
generation and conduction take place.

<!-- page 106 (PDF 18) -->
Usually the medium is isotropic and so, K is a scalar, in many cases only dependent
on temperature. If the medium is not isotropic, K becomes a tensor and more complex
options have to be considered.
If the equation is applied to fuel, q000 6=0 and the general equation will be integrated
after calculating it as it follows:
l
At power, it will be supplied by neutron physics formulation:
q000 r, z
ð
Þ = KfΣfΦ r, z
ð
Þ
where ΣfΦ is fission rate at r, z location and Kf is the factor converting fissions/s in W.
l
After a scram, either by a devoted table (like ANS79):
q000=q000
0 = f tf , ta
□
□
where tf=irradiation time and ta=cooling time or by a specific code dealing with
decay heat.
If the equation is applied to gap, q000 =0 and the general equation will be integrated
considering it as a region with a given thermal resistance. The evaluation of such resistance
is rather complex and usually is not performed on line since it is based on the
results of thermal-mechanical analysis of fuel rods as function of fuel burn-up.
If the equation is applied to cladding, q000 =0 and the general equation will be
integrated accordingly.
3.3.2.3
Related to heat convection—general aspects
Heat convection is a mechanism of heat extraction from a hot wall by means of a fluid
having a certain movement. The mechanism involves also molecular diffusion and the
movement of the fluid could be forced (forced convection) or free (natural convection
). Heat flux extracted by convection follows Newton’s law:
q00 = hs Twall □Tbulk
ð
Þ
where hs=convection heat transfer coefficient; Twall=temperature of the hot wall
(cladding) and Tbulk=average temperature of the fluid in the considered area.
Evaluating the convection heat transfer coefficient is rather complex and has been
the object of important experimental activities. On the one hand, it depends on the
convection mode (in some code manuals ambiguously called heat transfer mode),
and on the other hand, its range of variation is very wide. Its units are W/(K m2)
and some approximate values can be between 35,000 and 55,000 in a PWR nominal
steady state and up to 5000 in one-phase natural circulation or 50 or less in a dry-out
situation.
Convection mode depends on the mechanism of heat extraction. Besides the
already mentioned conditions of movement and diffusion, there is another relevant
aspect that becomes an additional difficulty in evaluating the coefficient; this is the
vicinity of saturation. The convection modes resulting from this vicinity have a certain
relation or proximity with flow regimes but they are essentially something different.

<!-- page 107 (PDF 19) -->
The goal of the former is calculating heat transfer coefficient while that of the latter is
allowing two-phase flow detailed studies.
Establishing a correlation for each and every heat transfer coefficient using data
produced in specific experiments culminates the activities devoted to evaluate them.
3.3.2.4
Related to heat convection—pre-CHF convection modes
Convection to single phase liquid is the basic convection mode occurring when bulk
temperature is far from saturation. It takes place in PWR at nominal steady state for
most of the fuel rods mainly nearby core inlet and also for pins having a medium or
low linear power (see Fig. 3.3).
If bulk temperature is close to saturation (if ΔTSUB is about a few °K) and that of the
wall is about saturation, bubbles could be built up in contact with the hot wall extracting
the needed latent heat from it. Since fluid is subcooled, the built up bubble could easily
mix with liquid water and thus help general heat extraction. This mechanism occurs
under certain conditions and is extremely positive since it helps heat transfer. As a consequence
the temperature of the wall could stabilize at a lower value. This mechanism is
called nucleate boiling (or subcooled nucleate boiling) and the heat transfer coefficient
is greater than in previous situation. This convection mode takes place in PWR at nominal
steady-state fuel rods having a higher linear power (see Fig. 3.4).
If bulk temperature is saturation (and so ΔTSUB is 0) and that of the wall is slightly
higher than saturation, bubbles in contact will be built up easily. Similarly bubbles
could easily mix with liquid water and also help general heat extraction. The mechanism
is then called saturated nucleate boiling. This convection mode takes place in
most of the fuel rods of a BWR at nominal steady state as well as in accidental
scenarios progression.
Nucleate
boiling
Liquid
forced
convection
High
Nominal
steady state
Nominal
steady state
heat
heat
flux
flux
Low
Coolant
Fig. 3.3 Convection heat transfer modes at a PWR nominal steady state. Notes of lecture
“First approach to reactor case” F. Reventos. UPC Master of Nuclear Engineering.

<!-- page 108 (PDF 20) -->
3.3.2.5
Related to heat convection—CHF/boiling crisis/post-CHF
convection modes
The progress of the built up of bubbles at the hot wall and its subsequent coalesce produces
a partial film covering its surface with the result of a strong reduction of heat
transfer coefficient (Arias, 2009; Arias et al., 2009; Arias and Reventos, 2010). This
phenomenon is known by many authors as boiling crisis and the value of heat flux at
which it appears is called critical heat flux. The phenomenon could take place under
three different circumstances. When previous heat transfer mode is nucleate boiling at
a subcooled bulk temperature, it is called “departure from subcooled nucleate boiling”
(DNB subcooled); when previous heat transfer mode is nucleate boiling at a saturated
bulk temperature, it is called “departure from saturated nucleate boiling” (DNB
saturated); and finally at liquid high enthalpy, it is called “dry-out.”
It is a phenomenon of high relevance for safety. When it takes place, the sudden
reduction of heat transfer could produce the so-called burnout or physical destruction
of the hot surface.
A huge amount of experiments have been performed to clarify the physics of the
phenomenon itself and also to characterize the post-CHF heat transfer modes. Again
the results of such experiments have been useful to establish correlations and look-up
tables valid for the corresponding predictions.
3.3.2.6
Prandtl and N€usselt numbers
Besides Reynolds and Froude numbers already introduced in a previous section the
most used dimensionless numbers in heat transfer developments are Prandtl number
(Pr) and N€usselt number (Nu).
Liquid
Coolant
Steam
DNB
Film
boiling
Nucleate
boiling
High
heat
flux
heat
Low
Accident
scenario
Accident
scenario
flux
Fig. 3.4 Convection heat
transfer modes in an accident
scenario. Notes of lecture
“First approach to reactor
case” F. Reventos. UPC
Master of Nuclear
Engineering.
