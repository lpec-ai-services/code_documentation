# Chapter foreword
<!-- source PDF pages 3-33 -->

<!-- page 3 (PDF 3) -->
UVUT
unequal velocities unequal temperatures
UVUTUP
UVUT plus unequal pressures
VVER (or WWER)
water-cooled, water-moderated energy reactors
WNA
World Nuclear Association
Chapter foreword
Top
level
researchers
involved
with
applications
and
developments
in
thermal-hydraulics from all over the world cooperated to write the book.
Any scientist involved with nuclear thermal-hydraulics may take benefit from
reading the book.
Reading this chapter is a prerequisite (not sufficient) for getting acquainted with
the book.
Memorizing the authors of documents cited in Chapter 1 and the topics, connected
with thermal-hydraulics which are not discussed in the book (but are listed in Chapter 1)
will be of great help for understanding the contents of the book.
1.1
The composed word thermal-hydraulics, here preferred to thermo-hydraulics,
thermal-hydraulics, and thermalhydraulics, derives from two Greek terms also used
by Romans, which indicate heat and water, respectively. Thus, thermal-hydraulics
is the discipline which studies the transient evolution of engineering systems where
(hot-heated) water is the coolant fluid and, typically, heating and cooling or boiling
and condensing processes occur.
Nuclear thermal-hydraulics addresses the performance of water-cooled reactors,
typically water-moderated, i.e., the majority of research reactors (RR) and power
plants. Selected features for the discipline can be listed as follows:
l
design and safety of nuclear reactors highly depend upon thermal-hydraulics: this has been
established since the beginning of the nuclear technology era;
l
looking at the numerical simulation of phenomena,
−
it shares with fluid-dynamics and gas-dynamics the difficulty associated with turbulence:
in thermal-hydraulics the problem is even more complex because of the presence of
two-phases;
−
time and space averaging is unavoidable: discontinuities including the interface between
the phases are solved by continuum equations;
l
approximation of results from numerical models and the need to bound the errors of calculations
, i.e., the uncertainty, are a consequence of what written above;
l
experiments are necessary and highly dependent upon geometric configurations: they are not
conclusive for a suitable knowledge because performed at reduced scale in the case when
power reactors are concerned;
l
controversy in judging the quality, the applicability and the acceptability of experimental
and numerical data to situations of technological interest is not surprising.

<!-- page 4 (PDF 4) -->
Thus, nuclear thermal-hydraulics can be considered as a sliding and lapsing technology
. On the one hand, expertise based on decades of activity may reveal not sufficient
to address targets put by design and safety of a variety of nuclear installations and, on
the other hand a book built on weak foundations may not be justified. The former issue
remains open. Otherwise, the present endeavor is an attempt to address the latter issue:
technologists and scientists deeply involved with nuclear thermal-hydraulics after
three dozen years activity (or more) are invited to be coauthors. The plan is to present
an as far as comprehensive vision of modern nuclear thermal-hydraulics assuming that
rudimentary-established knowledge is available to readers.
The word nuclear associated with thermal-hydraulics testifies of the progress in
knowledge achieved within the development of nuclear technology. Furthermore,
the words system thermal-hydraulics (SYS TH) which should be seen as nuclear
SYS TH, where proposed during the planning of the framework of the Specialists
Meeting on Transient Two-Phase Flow—System Thermal-hydraulics organized by
the Organization of Economic Cooperation and Development/Nuclear Energy
Agency/Committee on the Safety of Nuclear Installations (OECD/NEA/CSNI), held
in Aix-en-Provence (OECD/NEA/CSNI, 1992). The SYS TH acronym reflects the
connection between the thermal-hydraulics and the nuclear system, namely the size
of the concerned system and the interaction among phenomena which occur or are
expected in complex geometrical configurations and in transient conditions during
postulated accidents in nuclear reactors.
SYS TH, seen as an evolution of fundamental thermal-hydraulics and covering
nuclear thermal-hydraulics, constitutes the topic and the framework for the book.
The computational tools named SYS TH codes, which represent the baskets of
expertise in the area, are the direct or the indirect target for individual chapters:
emphasis is given to the development, the qualification, and the application of those
codes for demonstrating the safety and the acceptability of nuclear installations. The
bases, the applicability of the computational fluid-dynamics (CFDs), and its role in
nuclear reactor safety and design are described to complement the vision provided
for nuclear thermal-hydraulics.

### 1.1.1 Scope and framework

A as far as possible comprehensive list of topics is introduced hereafter to define the
framework of thermal-hydraulics. The necessarily reduced scope and framework for
the textbook are discussed in the last paragraph of the section.

#### 1.1.1.1 Origin of nuclear thermal-hydraulics

The word thermal-hydraulics has been associated with water and heat from its etymology
. This already limited the scope of the book to water-cooled nuclear reactors. However
, the word heat embeds concepts like material thermal properties, (thermal)
energy balance, thermodynamic efficiency, and energy dissipation. Owing to this
and based on the historical use of the word thermal-hydraulic, any process connected
with heat generation and transfer has been considered as part of the discipline called
thermal-hydraulics. Noticeably, thermal energy transport in sodium and gas-cooled

<!-- page 5 (PDF 5) -->
reactors, natural circulation, and thermal mixing of lead-bismuth systems are important
fragments in nuclear thermal-hydraulics.
Here inthe book, theetymological originof thewordiskept,and atthe same timethe
connection with the nuclear world is formally established. To the last aim, reference is
made to the facility constructed by E. Fermi in Chicago to show the sustainability of the
fission chain reaction. The nuclear thermal-hydraulics was born on Dec. 2, 1942 when
Fermi triggered the fission reaction within the multiton graphite bricks pile. This
ensured, other than neutron energy moderation capability and protection from radiations
, suitable thermal capacity and heat sink to accommodate the fission power.
In Jul. 1951 the Congress of United States authorized the construction of the
nuclear submarine which entered the sea on Jan. 17, 1955. In the mean time, according
to World Nuclear Association (WNA, 2014) the first nuclear reactor to produce electricity
, albeit in the amount of a few hundred watt, was the liquid metal-cooled EBR-1
reactor in Idaho: on Dec. 20, 1951 (Michal, 2001) “the liquid metal flowed into
water-jacketed pipes to form steam that turned a turbine.” The first substantial production
of nuclear electricity, i.e., 5 MW, happened in Soviet Union by the water-cooled
and graphite-moderated reactor called AM-1: the world first nuclear power electricity
generator began the operation in Obninsk on Jun. 27, 1954.
So, nuclear thermal-hydraulics is unavoidable part of nuclear technology: the fission
power heats up a material, i.e., typically the nuclear fuel, and processes are
needed to transport the generated energy for application purposes, i.e., toward heat
exchangers for the use of thermal power, toward the turbine for electricity for electricity
or propulsion.

#### 1.1.1.2 Single- and two-phase flows

Liquid-water or gas-water is commonly referred as liquid and steam or vapor, in the
latter case leaving the word gas for superheated conditions. The thermodynamic evolutions
of both individual liquid and steam fluids (1-phase or 1Φ) as well as of their
mixtures, or two-phase flows (2-phases or 2Φ), constitute the topic of interest for
nuclear thermal-hydraulics (e.g., Ishii, 1975; Yadigaroglu and Lahey, 1976). Furthermore
, steam flows can be associated with noncondensable gas species of substances
other than water, and liquid flows may transport solid particles like impurities including
solid fission products or high-temperature boiling boric acid (typically measured
in parts-per-million, ppm).
So, nuclear thermal-hydraulics deals with 1Φ and 2Φ water flows, plus noncondensable
,plussolidimpuritieswithouttreating thechemicalinteractions.However,
as a noticeable exception, the metal-water chemical reaction which creates hydrogen at
high temperature of a typically heating surface is within the boundary of interest.

#### 1.1.1.3 Prominent scientists and textbooks

Technology needs associated with single- and two-phase flows occurred well before
the nuclear era. The transition from horse power on the land or wind power on the sea
to steam moved machinery imposed gathering expertise in thermal-hydraulics since
the nineteen or even the late 18th century.

<!-- page 6 (PDF 6) -->
Following the creation of modern physics by G. Galilei (1564–1642), I. Newton
(1642–1727), and L. Euler (1707–1783), selected prominent scientists who contributed
to the development of thermodynamics at the basis of the modern
thermal-hydraulics are J. Watt (1736–1819), J.B.J. Fourier (1768–1830), C.L. Navier
(1785–1836), J.P. Joule (1818–1889), G. G. Stokes (1819–1903), J.A. Froude
(1818–1894), H. von Helmholtz (1821–1894), W.T. Kelvin (1824–1907), F. Grashof
(1826–1893), O. Reynolds (1842–1912, e.g., see Reynolds, 1896), and M. Planck
(1858–1947, see e.g., Planck, 1923). More recently, L. Prandtl (1875–1953, e.g.,
see Prandtl, 1956), T. von Ka´rma´n (1881–1963), K.E.W. Nusselt (1882–1957, e.g.,
see Nusselt, 1943), S. Nukiyama (1896–1983, e.g., see Nukiyama, 1966), A. Kolmogorov
(1903–1987), L.D. Landau (1908–1968), A. V. Lykov (1910–1974, see, e.g.,
Lykov, 1958), and S. S. Kutateladze (1914–1986, see, e.g., Kutateladze, 1963)
directly contributed to the bases of thermal-hydraulics even without taking a leadership
in the application of the discipline to the nuclear technology.
Parallel to nuclear engineering and with limited interactions with it (i.e., at least in
three cases before the start of the nuclear era, here fixed as 1942), thermal and fluid
engineering/physics evolved during the first half of the 20th century. Fundamentals in
those areas are also fixed by the textbooks by Gr€ober and Erk (1933), Reichardt
(1941), Jakob (1949), Landau and Lifchitz (1954), Lykov and Mikhailov (1961),
Bird et al. (1960), Spalding (1963), Sparrow and Cess (1966), and of Patankar and
Spalding (1967) in addition to the references already listed in the previous section.
Rudimentary thermal-hydraulics, or elements and concepts in thermal-hydraulics,
can be found in the pioneering nuclear engineering textbooks by Glasstone and Edlund
(1952), Schultz (1955), Glasstone and Sesonske (1955), Stephenson (1958), and
Etherington (1958), and later on by Lamarsh (1966), as well as by Margoulova
(1969) in the former Soviet Union.
Nuclear thermal-hydraulics was inspired by the rudiments in the nuclear engineering
textbooks rather than the textbooks in thermal and fluid engineering. Professor
El-Wakil made the first effort to gather the concepts of nuclear thermal-hydraulics
into a textbook (El-Wakil, 1962, 1971a,b).
The modern nuclear thermal-hydraulics can be associated with a couple dozen textbooks
which are internationally spread and recognized. A representative and nonexhaustive
list of those textbooks (reported in the order of publication date)
includes names of key scientists in the area: Tong (1965), Wallis (1970), Tong and
Weisman (1970), Collier (1975), Ishii (1975) (see also, Ishii and Hibiki (2006)),
Incropera and Dewitt (1981), Delhaye et al. (1981), Fenech (1981), Cumo (1982),
Hsu and Graham (1986), Todreas and Kazimi (1990), Hewitt et al. (1992), Lahey
and Moody (1993), Levy (1999), and Kirillov et al. (2010, 2013, 2014).
In order to complete, as far as possible, the current picture for reference books and
scientists in nuclear thermal-hydraulics, the following needs to be considered:
l
the reports issued by OECD/NEA and International Atomic Energy Agency (IAEA) dealing
with application and needs in nuclear thermal-hydraulics (e.g., Aksan et al. (1987) and Lewis
et al. (1989), from the side of OECD/NEA/CSNI and Allison et al. (2002) from the side
of IAEA)

<!-- page 7 (PDF 7) -->
l
the reports (code manuals) and the support papers describing SYS TH computer codes (e.g.,
starting from RELAP2, Moore and Rettig, 1968, to Berry et al., 2015) dealing with the
RELAP7 under development now, and Bestion, 1990, dealing with the closure laws of
the CATHARE code
l
the CFD technology and the related CFD (and direct numerical simulation, DNS) codes (e.g.,
Hassan, 2005)
l
the textbooks dealing with topics other than SYS TH in nuclear reactors where
thermal-hydraulics has a key role, like Nuclear Plants (e.g., Knief, 2008; Cacuci, 2010;
Oka, 2014; Murray and Holbert, 2014; Sjoden, 2015); nuclear fuel subchannel analysis
(e.g., Ninokata and Aritomi, 1992); industrial plant safety (e.g., Banerjee, 2003); investigations
into selected phenomena (e.g., Yadigaroglu, 1975); fluid-structure interactions (FSIs)
(e.g., Paı¨doussis et al., 2014); thermal-hydraulic instrumentation (e.g., Mayinger, 1994);
design of key components for nuclear and thermal plants (e.g., Cumo and Naviglio,
1990); even focused on centrifugal pumps (e.g., G€ulich, 2010); steam generators (e.g.,
Annaratone, 2008); and turbines (e.g., Bloch and Singh, 2009)
l
edited open access textbooks have been issued (e.g., Guillen, 2013), but focusing on CFD
applications
l
there are scientists who published outstanding papers during a time-span longer than half-acentury
like Novak Zuber (see e.g., Zuber, 1958; Zuber, 2010) or scientists who published
one paper which remained important for half-a-century, like Yamanouchi in relation to the
reflood modeling idea (see, e.g., Yamanouchi, 1968) or scientists who devoted their half-acentury
working life to a single thermal-hydraulic phenomenon like D.C. Groeneveld in relation
to critical heat flux (see, e.g., Groeneveld, 1996)
l
the integrated vision proposed by N. Kolev, with a series of five volumes dealing with
multiphase flow dynamics (Kolev, 2015). This is the outcome of a lifetime effort for the
author. Basilar physical phenomena are considered in the attempt to reconstruct complex
system performance from the knowledge and the modeling of local interactions among substances
: not only water but also molten materials interactions are concerned to deal with the
severe accident conditions in NPP
The textbooks referenced in this section provide a snapshot idea, still narrow and
incomplete, of the complexity of the nuclear thermal-hydraulics and, all together, constitute
a challenge for the present book. Otherwise, links and interconnections between
nuclear thermal-hydraulics and various topics including other disciplines relevant in
nuclear technology and safety are considered below.

#### 1.1.1.4 Journals, conferences, and the web

Nuclear thermal-hydraulics, like a variety of disciplines, has its space and interest in
devoted journals, national and international conferences, and the web. Namely the
web is not only a mirror for journal and conference papers but may include much
more, like master theses, PhD dissertations, documents issued by institutions and companies
, and lectures by professors and experts.
Providing lists of journals or conferences dealing with nuclear thermal-hydraulics
is not the purpose here. Rather, the purpose here is to give an idea of the overall number
of papers in the area and their rate of growth.

<!-- page 8 (PDF 8) -->
Starting from the 1950s and considering the exponential growth of the number of
publications after the advent of computers and the internet, roughly 10,000–20,000
papers have been published within the nuclear thermal-hydraulics area. The current
growth rate is around 1000 (papers)/year considering journals and conferences. This
may also give an idea of the effort needed to follow or interpret developments in
the area.

#### 1.1.1.5 Education and training

Nuclear thermal-hydraulics is also the topic of education at universities, undergraduate
, graduate, and PhD courses. Several tens of universities all over the world offer
nuclear thermal-hydraulics courses: one may estimate in a few thousands of students
per year, however largely changing in each country each year.
Specialized training courses exist, covering fundamentals and application topics in
thermal-hydraulics (see the course organized in Zurich by Prof. G. Yadigaroglu) and
the technology of using SYS TH codes (e.g., see Petruzzi et al., 2008).
The material in the book can be used for training and education in nuclear
thermal-hydraulics.

#### 1.1.1.6 The target NPP and the RR types, the structures, system, and components for concerned nuclear installations

The construction and the operation of Nuclear Power Plants shall be seen as the result
of one among the most complex endeavors of the human minds: discoveries and technological
applications from a variety of technological sectors are needed to design,
construct, operate, and evaluate the safety of NPP.
The exploitation of fission reactions to produce thermal energy and, after proper
transformation, mechanical or electrical power, is not exclusively connected with
water. A variety of options are available, including gas or liquid metal as coolant,
graphite as moderator, or even dissolving the nuclear fuel into the coolant, i.e., homogeneous
reactors. However, strategic, financial, marketing, and technological reasons
brought to the current (2016) situation where 99% of the operated NPP are cooled by
water and more than 95% are cooled and moderated by water, whatever light or heavy.
The use of water as coolant brought to the high pressure for the cooling loop encasing
the nuclear core, e.g., in the range of 7–15 MPa, to ensure suitable thermal efficiency.
The high pressure, the high operational power (up to 4500 MWt), and the power density
(up to 100 kW/dm3 in core region, or 50 kW/m linear power for fuel pin) impose:
(a) large geometry (up to around 300 m3) for the overall cooling system and
(b) equivalent diameter of flow channels in the range around 0.01 m in the core region.
All of this, combined with:
l
possible neutron flux (reactivity) excursions translating into thermal power pulses
l
unavoidable production of decay power (which cannot be stopped)
l
unavoidable production of radioactive products (dangerous for humans and environment)
which are kept into the fuel material part of the core
is at the basis of the needs or requirements for nuclear thermal-hydraulics at the levels of the
design and the safety demonstration of nuclear installations.

<!-- page 9 (PDF 9) -->
The operational conditions and the system configuration of water-cooled RR, compared
with NPP are characterized by: (a) much lower power (usually in the range of a
few kW and anyway less than about 30 MW); (b) low-pressure values (in the large
majority of cases, close to atmospheric values); and (c) much smaller geometric
dimensions. However, challenges for nuclear thermal-hydraulics are not smaller than
in the case of NPP, e.g., the predictions of margins to subcooled nucleate boiling and
the natural circulation flowrate under flow reversal conditions.
The terms systems, structures, and components (SSC) include any hardware piece
part of NPP or RR which is functional for the operation or to guarantee the safety. The
SSC may have features either geometric or in terms of ranges of key variables which
require specific thermal-hydraulic modeling capabilities, like centrifugal pumps,
steam separators, and containment. In the last case a specific paragraph below can
be found.

#### 1.1.1.7 Experiments and instrumentation

Any progress in 2Φ nuclear thermal-hydraulics has been made possible by experiments
. Experiments can be basic, like pressure drops in a cylindrical pipe and heat
transfer between a wire and surrounding fluid, or make reference to NPP and RR,
including SSC. Nonbasic experiments are generated from either separate-effect test
facilities (SETF) or integral test facility (ITF) (e.g., Umminger and Del Nevo,
2012). Key issues for the experiments are the measurement errors, the time or space
averaging, the perturbation introduced by the sensors, the difficulty to deal with heat
losses, the role of radiation heat transfer when solid-surface temperatures overpass the
threshold of about 500°C, the reproducibility mainly of transient experiments, the
variance of measured data, and the suitability of needed scaling processes to demonstrate
the similarity or the correspondence between gathered data and data expected in
prototype systems.
Adopted instrumentation can be very simple and not expensive, like a thermocouple
of the cost of 1 USD, or complex and expensive like gamma-densitometers and
laser-doppler anemometry having costs up to 106 USD per single instrument.
A few textbooks are aimed or restricted to experiments and instrumentation in
nuclear thermal-hydraulics (e.g., Cumo, 1982); however, the majority of textbooks
from previous paragraphs makes reference and gives proper consideration to
experimental data.
Recently, following the OECD/CSNI Specialists Meeting on Advanced Instrumentation
and Measurement Techniques held in Santa-Barbara, CA, USA,
OECD/NEA/CSNI (1997), the Specialists Workshop on Advanced Instrumentation
and Measurement Techniques for Nuclear Reactor Thermal Hydraulics (SWINTH)
was organized in Livorno, Italy, Jun. 2016. This is going to be reflected in a special
issue of the Journal of Nuclear Engineering and Design to be published in 2017–18,
and constitutes the first of a kind of future workshops supported by NEA/CSNI also
including the subject of instrumentation for the characterization of severe accidents
(see e.g., Moretti, 2016). Issues related to experiments are marginally and occasionally
considered in the book (e.g., Chapter 15).

<!-- page 10 (PDF 10) -->
#### 1.1.1.8 Numerical methods and computer science

Nuclear thermal-hydraulics models and equations are typically nonlinear and need
numerical methods to achieve solutions (e.g., Patankar, 1980). Programming of equations
and achieving solutions need proper competence in computer science (e.g.,
Ferziger and Peri⟨c, 1999): numerical solution methods may affect substantially simulated
performance of thermal-hydraulic systems (e.g., Ferreri and Ambrosini, 2002).
The design and the use of SYS TH codes are discussed in Chapter 11 and related
verification and validation (V&V) and application are presented in subsequent chapters
: all of this needs consideration and competence in the areas of numerical methods
and computer science. However, numerical methods and computer science are outside
the domain of interest for the book.

#### 1.1.1.9 Nuclear safety, the licensing process, and the DBA (moving) boundaries

Nuclear reactor safety constitutes the essential technology for the exploitation of
nuclear energy (e.g., Lewis, 1978). Furthermore, licensing shall be seen as the legal
part of nuclear reactor safety: already in 1981, Prof. Okrent published a related book
(Okrent, 1981). The key objective is to protect the humans and the environment from
the radiations or from the contact with the radioactive nuclei mostly generated by fissions
. Principles are established to this aim and are supported by regulatory requirements
which become mandatory within the licensing process. Safety barriers and
safety functions connect those requirements with the hardware of nuclear installations
within a virtual environment known as Defense in Depth. Thermal-hydraulic parameters
like pressure, fluid temperatures, and velocities must be under control to protect
the barriers and safety functions.
As noticeable examples, the fuel clads and containments constitute barriers which
can be broken due to high temperature and/or high pressure. High temperature in the
core materials may be a consequence of inadequate cooling for the concerned fission
power level. High pressure inside the clad and containment may derive by gas release
from nuclear fuel or from loss of pressurized coolant from primary circuit, respectively
. Ensuring protection of the barriers implies the design of the so-called
engineered safety features (ESF), including the emergency core cooling systems
(ECCSs) and the demonstration of related capabilities.
Key issue in this context is the determination of safety margins, or of the space
which separates the safe operation from potentially dangerous conditions during
the course of an accident. This is done by introducing the postulated accidents and,
shortly, the related design basis accident (DBA).
The ensemble of all hypothetical situations, and/or accidents and/or transients,
against which a nuclear installation (typically a NPP) must be protected is called
DBA envelope. The probability of the occurrence of any event plays a role in determining
the envelope (see also below). The importance of the DBA envelope is associated
with the regulatory requirements: whatever is inside the envelope must be
known with the highest quality available at the time. This sets the boundary for
thermal-hydraulics and for the present book. Thus, the book covers situations

<!-- page 11 (PDF 11) -->
pertaining to the design and the nominal operating conditions of NPP and RR as well
as accident situations until the loss of geometric integrity for the core. This also
implies a space of knowledge outside the DBA envelope which is covered by accident
management (AM) (see below).
Modern thermal-hydraulics received a decisive impulse from requirements set by
regulatory authorities in each country (e.g., Reocreux, 1994, see also Chapter 2 of the
book). Namely, requirements impose the demonstration of acceptability of ECCS in
transient conditions; then, system and geometry complexities prevent the possibility
of human mind solutions without the support of experiments and computational science
; this opened the way to complex SYS TH codes; then, the issues came in relation
to scaling, scaled experiments, V&V for computational tools and the uncertainty
which characterizes the predictions by computational tools.
SYS TH may be seen as a key sector for nuclear safety and the mentioned topics are
discussed in the book.

#### 1.1.1.10 Severe accidents

Severe accidents did occur and may occur in NPP as well as in RR. Those events may
imply damage to the core, the primary circuit, and eventually the containment. Severe
accidents may cause serious damage to humans and the environment (see the fundamental
book by Prof. Sehgal (2012)).
Other than proper competences and efforts, specific regulatory requirements exist
and are needed to prevent severe accident evolutions and mitigate the consequences.
Furthermore nuclear designers must be capable of demonstrating licensing acceptability
of NPP and RR in relation to severe accident, and operators must be in the conditions
to take decisions in case severe accidents occur.
Thermal-hydraulics has a key role in relation to the overall severe accident topic:
namely a “pure” thermal-hydraulics analysis is needed to analyze any transient since
its beginning till the moment when core degradation occurs. However, severe accidents
conditions and evolutions are beyond the domain of interest for the book.

#### 1.1.1.11 Containment and RCS

The reactor coolant system (RCS) of any NPP is embedded into a protective structure
called containment which also constitutes a safety barrier as already discussed.
Unavoidably RCS and containment interact should an accident occur: in case of break
occurrence in the RCS, the counter-pressure which develops in the containment caused
by the release of steam water mixtures from RCS affects the flow-rate at the break;
the fluid temperature and the liquid level in the sump affect the injection of ECCS in
the long-term cooling period; in the case of boiling water reactors (BWRs) the role of
the sump is taken by the pool of the wet-well region. Furthermore, hydrogen diffusion
and transport may occur inside the containment also affected by temperature stratification
and steam condensation at the walls. The last two phenomena are relevant for
pressure build-up, containment cooling, and possible controlled releases to the
environment.

<!-- page 12 (PDF 12) -->
The role of containment is essential should an accident occur. In the case of some
advanced reactor designs like the advanced pressurized water reactor (PWR), or the
AP-1000 (still prototypical design), the core cooling is ensured by the gravity and
affected by the condensation phenomena (see also passive systems, below) occurring
in the containment.
Thermal-hydraulic capabilities are needed to predict the containment performance.

#### 1.1.1.12 Passive systems, reliability, and stability issues

Following the events of Three-Mile Island (TMI) in 1979 and more noticeably of
Chernobyl in 1986, the so-called passive systems gained importance in the design
and, recently, in the construction and operation of NPP. Components like accumulators
and containments are already passive systems part of NPP design since the beginning
of the nuclear era. Then, passive systems here are meant those systems introduced
in the aftermath of the Chernobyl accident.
Noticeably, the original idea was that natural forces, gravity in particular, improve
the reliability of core cooling (other than reducing the construction and the maintenance
cost). Researches performed since the year 2000 showed that this is not correct
(e.g., D’Auria and Galassi, 2000; Jafari et al., 2003; Marques et al., 2005). Reasons for
this are:
l
Passive systems, namely based on natural circulation involving a heat sink and a heat source
at different elevations, never operate under (perfect) steady-state conditions: temperature,
and/or pressure, and/or level, and/or exchanged/removed power change with time. Difficulties
arise in demonstrating the reliability of passive systems because of the wide ranges of
variations for governing parameters shall be investigated, and the combination of selected
parameter values, even though in narrow ranges, may cause malfunctions.
l
Boiling and condensation processes cannot be avoided in the majority of passive systems:
the density changes associated with both processes makes those systems prone to instability.
l
Minor changes in boundary conditions which are uninfluent upon system performance when
pumps are installed, like ·1° inclination of horizontal pipes (specifically carrying two-phase
mixtures), small leakages (unavoidable if large valves are present to isolate a large pressurized
pipe), and heat losses (e.g., in the region where steam or two-phase flows are present)
challenge the system performance and may largely reduce the reliability of the system.
l
A stable natural circulation system characterized by a fixed power heat source may become
unstable when the heat source power is generated by another natural circulation system, i.e.,
when the heat sink of a natural circulation system also constitutes the heat source for a downstream
natural circulation system. This is the case when a passive cooling system is associated
to the steam generator of a PWR. In this situation, oscillations in the passive system, i.e.,
downstream the steam generator may reflect in oscillations in the core flowrate, thus endangering
core cooling.
Nuclear thermal-hydraulics is essential for the design of passive systems and for
assessing the operational range of parameters.

#### 1.1.1.13 Accident phenomenology

The knowledge in thermal-hydraulics evolved according to the given notes, see also
Chapter 2, and complex phenomena occurring in case of accidents in NPP (i.e., the
way they are understood today) had not a major role at the beginning of the nuclear

<!-- page 13 (PDF 13) -->
era (year up to around 1970). However, the logical path for nuclear thermal-hydraulics
became (starting from around 1970): [NPP-geometry-and-operating-conditions-&-
design-requirements]+[DBA
envelope]⃗[phenomena]⃗[range-of-variation-ofparameters
-of-interest]⃗[requirements-&-development-for-thermal-hydraulics].
This (virtual) view is pursued in the book, where phenomena discussed in Chapter 6
have the central role.
Scaling is the key issue here: the derivation of phenomena, their evolutions and the
related variation ranges of important parameters, are based upon data measured in
small size facilities compared with NPP, apart from a few exceptions. Ensuring a reasonable
understanding, including predictive capabilities, of phenomena part of the
DBA
envelope
in
NPP,
constitute
the
challenge
for
the
specialists
in
thermal-hydraulics. This is a starting point for the definition of the objective of the
book in Section 1.1.2.

#### 1.1.1.14 Role of start-up and shutdown phenomena

Toward the end of 1980s it was realized that the risk of NPP during start-up and shutdown
periods was not negligible compared with the risk during power operation. This
triggered research and developments in various areas including thermal-hydraulics.
A distinction is made hereafter between nuclear thermal-hydraulics issues after
power operation postulated initiating event (PIE) and after shutdown or start-up
PIE: both situation types may have a relation with the DBA envelope.
l
In the former case the problem to be addressed is the demonstration of adequacy of ECCS in
satisfying licensing criteria for core cooling: components like centrifugal pumps injecting
ECCS water are assumed to function properly even though failures are possible according
to specifications from reliability analyses. Thermal-hydraulic competences are essential to
provide a solution in terms of safety and licensing.
l
In the latter case the problem is to determine what happens following the failure of residual
heat removal (RHR) pumps typically starting from zero fission power operation. In this case
thermal-hydraulic calculations also focus on determining the time available to operators
before irreversible damage of the core. The solution is an improved design for pumps or
of related operating conditions, rather than the outcome of a thermal-hydraulic calculation.
Thermal-hydraulic conditions challenging the RHR operation in the long term of accidents
and the shutdown in NPP are in some cases similar in terms of range of variations
for pressure, temperatures, and mass flows. This is also true in relation to RR
operating conditions.

#### 1.1.1.15 The accident management and the AM procedures (AMP)

The terms AM and AMP have been introduced in the 1990s. They indicate not only the
possibility but also the need and the capability for the NPP operators to manage or
drive any accident evolution. This is true for situations outside the DBA envelope,
i.e., beyond design basis accident (BDBA) conditions, while for DBA conditions
emergency operating procedures (EOP) are planned to support the operator actions.
Two categories can be distinguished for AMP in the concerned (BDBA) domain,
respectively, aiming at preventing massive core degradation and mitigating the

<!-- page 14 (PDF 14) -->
consequences of core melt including recovery of the plant. The phenomena expected
to be relevant for the first category are considered in Chapter 6 and discussed in
Chapter 15.
1.1.1.16
Connection with neutron physics, probabilistic safety
assessment (PSA), radioprotection, chemistry, mechanics,
nuclear fuel, electronics including instrumentation and
control (I&C)
The application of thermal-hydraulics within NPP technology and nuclear reactor
safety is not possible without an interaction with different disciplines: exceptions
(i.e., thermal-hydraulics applications alone) also exist but are not universal and do
not allow an overall safety assessment. In addition to textbooks dealing with other
disciplines already cited in this chapter, in the following examples are given of connections
between thermal-hydraulics and selected disciplines. The description below
is not exhaustive or systematic: rather, it provides an idea of complexity in application
of thermal-hydraulics to needs in NPP and RR technologies.
Neutron Physics. Thermal power is generated by neutrons and induced fissions.
The neutron flux depends, among the other parameters upon temperature of moderator
and fuel and, noticeably, upon density of moderator-coolant. Thus, fuel temperature
and moderator density and temperature are calculated by thermal-hydraulics and
affect instantaneous fission power. So any NPP or RR core-related analysis implies
coupled neutron physics thermal-hydraulics calculations. A zero-dimensional neutron
kinetics model was embedded into the primitive SYS TH codes since the end of 1960s
(e.g., Lamarsh and Baratta, 2011). Toward the end of 1990s, three-dimensional core
physics models were coupled with thermal-hydraulics codes (e.g., Ivanov and Baratta,
1999; see also D’Auria et al., 2004). This opened the way to the analysis of core transients
involving local reactivity changes like those associated with boron mixing (e.g.,
Pla et al., 2010) and control rod ejection (e.g., Avvakumov et al., 2007).
PSA. Probabilistic safety assessment constitutes by itself a developed technology
(e.g., see Apostolakis and Moieni, 1987; Fulwood, 2000; Arkadov et al., 2012). Identification
of all interactions between thermal-hydraulics and PSA is, again, beyond the
scope here. In order to give an idea of the tight connection between PSA and
thermal-hydraulics it is sufficient to recall that: (a) the transients part of the DBA
envelope, i.e., those analyzed by thermal-hydraulics as given in Chapter 15 of the
book, need specifications for probability of occurrence; this also determines the
acceptability criteria (e.g., IAEA, 2010a); (b) a transient thermal-hydraulic analysis
is needed to determine the consequences of any accident relevant to PSA (e.g.,
IAEA, 2010b).
Radioprotection. Radioactivity and doses (e.g., Knoll, 2010) are concerned with
the application of thermal-hydraulics. The amount of radioactivity releases from
the core (or the source term calculation, e.g., Herviou, 2005), should an accident
occur, and the possible paths to doses to humans or to radioactivity impact for environment
need thermal-hydraulic calculations. One may also state that the atmospheric

<!-- page 15 (PDF 15) -->
dispersion calculation for radioactive products (e.g., Thielen et al., 2007) is part of a
nuclear reactor safety analysis based on thermal-hydraulics.
Chemistry. Chemistry of the coolant and, noticeably, the control and the transport
of boron are needed for the long-term reactivity control or the fuel burn-up compensation
of any NPP (e.g., Benedict et al., 1981): a devoted system called chemical and
volume control system (CVCS) is designed, installed, and operated in each NPP. Time
delays for boron arriving in the core since the injection time and mixing in regions like
the down-comer or the lower plenum of the vessel need a thermal-hydraulic calculation
(e.g., Theophanous and Shabana, 1991; Cheng et al., 2014). This is particularly
true in case of anticipated transient without scram (ATWS). The calculation of the
amount of hydrogen produced by the metal-water reaction (e.g., Baker and Just,
1962) and the transport of the H2 gas into the containment (e.g., Camp et al., 1983;
Royl et al., 2009; Xiao and Travis, 2013) need specific thermal-hydraulic analyses
even in relation to accidents within the DBA envelope.
Mechanics. Eight examples are given hereafter of the interaction between mechanics
and thermal-hydraulics (without having the target to provide a comprehensive
view): (1) main coolant pump (MCP) transient operation, including the consideration
of two-phase flows, cavitation and vibrations, and net positive suction head (NPSH)
(e.g., Tuzson, 2000): various coupled set of mechanics and thermal-hydraulics equations
are needed to address the MCP simulation; (2) Flap valve operation with changing
pressure differences at the boundaries (e.g., Abu-Zeid, 2013): the inertia of the flap
body (mechanics) is correlated with the pressure difference calculated by
thermal-hydraulics; (3) pressurized thermal shock (PTS) stresses are caused by imperfect
mixing of cold liquid from ECCS injected in cold leg and challenge the reactor
pressure vessel (RPV) integrity. PTS constitutes an example of multidisciplinary topic
also involving, other than local thermal stresses, long-term damage to the vessel by
neutron radiations (also affected by water density), material aging and embrittlement,
welding technologies, crack growth and propagation, or fracture mechanics (e.g.,
IAEA, 2010c, see also Araneo and D’Auria, 2012); (4) condensation-induced water
hammer (CIWH): the fast condensation causes the movement of liquid slug which
may determine a dynamic load on piping and restraints (e.g., Schultz et al., 2001;
Barna et al., 2010); (5) Thermal fatigue: this constitutes a long-term degradation
mechanism important in NPP aging caused by fluid temperature stratification and turbulent
mixing effects. Those effects induce continuous (e.g., during the life of the system
) local mass flows of fluid having different temperatures which is at the origin of
thermal stresses in the structures (see, e.g., Courtin, 2013); (6) Loads on RPV internals
originated by pressure wave propagation from postulated break (e.g., Sokolowski and
Koszela, 2012); (7) fluid-structure interaction: FSI constitutes a scientific and technological
area dealing with loads on RPV internals caused by pressure wave (previous
topic) as well as vibrations (e.g., Bungartz and Sch€afer, 2006; see also the textbook by
Paı¨doussis et al., 2014) already mentioned; (8) Jet impingement (and jet thrust) and
pipe whip: the break of a pipe causes the release of the elastic energy stored in the
pressurized structures (e.g., piping) which adds to the fluid-dynamic loads generated
by the flow motion exiting the break. This generates (see, e.g., Vigni and D’Auria,
1979; D’Auria and Vigni, 1981): (a) loads on restraints; (b) mechanical and thermal

<!-- page 16 (PDF 16) -->
loads by the jet impinging on close surfaces; (c) potential missiles including parts of
components like rotor of a pump, blade of turbine, and pieces of broken material; and
(d) pipe whip involving the displacement of piping.
Nuclear fuel. Any analytical simulation of NPP or of RR requires the modeling of
nuclear fuel. Issues and challenges are connected with fuel, geometric, mechanical
and physical or material properties which continuously change during the fuel life
in the core. This is due to burn-up. Furthermore, the values of those properties depend
upon thermal-hydraulic parameters, noticeably pressure and temperatures of the coolant
and moderator (e.g., OECD/NEA/CSNI, 2010; see also Lisovvy et al., 2015).
Electronics including I&C. A wide number of parameters are continuously monitored
during the operation of NPP. Connected systems, also identified as part of
the I&C, have a role in determining the evolution of accidents, i.e., impacting the
thermal-hydraulic performance of the system and the thermal-hydraulic modeling
(see, e.g., D’Auria et al., 2012b).

#### 1.1.1.17 Scope and framework for the textbook

The huge space of interest, or scope and framework for nuclear thermal-hydraulics
and SYS TH derives from the nonsystematic summary in the previous section.
A textbook covering with sufficient detail each of the mentioned topics is well beyond
the planning of the present effort. Nevertheless any of those topics may have a connection
with what is discussed in the book. An attempt is made hereafter to summarize
what of the considered topics is or is not part of the book.
l
Origin of nuclear thermal-hydraulics: Chapter 2 deals with a vision of the history of SYS TH.
l
Single- and two-phase flows: these are of main concern in Chapters 3–11; however, key concepts
in fluid-dynamics and gas-dynamics are not discussed.
l
Prominent scientists and textbooks: the idea is to not replicate the structure of any of the
existing textbooks; the reader could derive from cited references the contributions to the
knowledge in thermal-hydraulics by prominent scientists. However, partial duplication of
fundamental concept cannot be avoided for subjects like definitions, balance equations, pressure
drops, and heat transfer, e.g., Chapters 3, 5, 7, and 8. International reports issued by
OECD/NEA and IAEA as well as reports documenting the features of SYS TH and of
CFD codes constitute key references for the present book with related details in Chapters 9
and 11–15.
l
Journals, conferences, and the web: a systematic review of publications (journals, conferences
, and web) is beyond the scope for this textbook. However, latest developments in
selected areas are considered.
l
Education and training: the consideration of existing education and training courses is
beyond the scope for the book. However, the book itself may become a reference for education
and training courses.
l
The target NPP and the RR types, the SSC for concerned nuclear installations: the reader of
the book is expected to be familiar with the features of concerned NPP, RR, and SSC including
containment. No devoted descriptions are part of the book.
l
Experiments and instrumentation: experiments are unavoidable for the progress of nuclear
thermal-hydraulics as already mentioned. Phenomena concerned in Chapter 6 are derived
from SETF and ITF experiments. However, description of experiments is not of direct interest
. Instrumentation is also outside the scope for the book.

<!-- page 17 (PDF 17) -->
l
Numerical methods and computer science: notwithstanding the need for numerical methods
and competence in computer science for the development and the application of SYS TH
codes, those topics are outside the scope for the book.
l
Nuclear Safety, the licensing process, and the DBA (moving) boundaries: the reader of the
book is expected to have fundamental knowledge of the nuclear reactor safety technology;
otherwise, an idea of the licensing process can be derived from cited references. In Chapter 4
the needs from nuclear safety are considered, and results of application of thermal-hydraulics
to nuclear safety are discussed in Chapters 14–16. The scope for the book in the concerned
context is clarified by the statements at the following item.
l
Severe accidents: the book does not cover severe accidents, i.e., the boundary of interest is
set to the time of any accident or the reactor configuration when the core starts to be
degraded. Two key reasons for this:
−
to keep as small as possible the size of the book (i.e., to avoid an encyclopedia),
−
the licensing requirements, the capabilities, the rigor and the quality of computational
tools, and the amount of experimental investigations are different between the areas
of thermal-hydraulics and severe accident.
l
Containment and RCS: Containment is part of NPP and containment response is part of
accident analysis (AA). Thus thermal-hydraulics of containment is part of the book,
e.g., Chapter 4 in relation to needs for thermal-hydraulics, Chapter 6 in relation to occurring
phenomena, Chapter 7 in relation to condensation heat transfer, and Chapter 15 in relation to
containment performance in case of accidents.
l
Passive systems, reliability, and stability issues: thermal-hydraulic phenomena expected due
to the operation of passive systems are presented in Chapter 6. Furthermore, the SYS TH
codes, Chapter 11, are capable to predict the transient performance of passive systems.
Because of the mentioned complexities passive system deserves specific attention from
the thermal-hydraulic community: this is out of the scope for the present book although passive
system operation is considered in Chapter 15.
l
The accident phenomenology: for the current vision, phenomena expected in NPP following
off-normal conditions are at the bottom of the pyramid of knowledge for nuclear
thermal-hydraulics. Phenomena are presented in Chapter 6.
l
Role of start-up and shutdown phenomena: phenomena during RHR operation including
start-up and shutdown in NPP are considered in Chapters 6 and 15. Reliability of
RHR-related pumps and the best design of cooling loops are outside the scope for the book.
l
The AM and the AM procedures (AMP): AM phenomena occurring to prevent severe core
degradation are part of the scope of the book and discussed in Chapter 15.
l
Connection with neutron physics, PSA, radioprotection, chemistry, mechanics, nuclear fuel,
electronics including I&C: the application of nuclear thermal-hydraulics to safety and
design of NPP and RR is not possible without the support of other disciplines, as it also
derives from the cited references. However, technological and scientific aspects dealing with
the connection between thermal-hydraulics and other disciplines as well as details related to
any of those disciplines are beyond the scope of the book. An exception is constituted by
Chapters 14 and 15. Namely Chapter 14 deals with best estimate plus uncertainty
(BEPU) approach to the AA: details are provided in this chapter in relation to the connection
between thermal-hydraulics and other disciplines. In a few cases, results of accident analyses
discussed in Chapter 15 deal with “other disciplines.”
Computer codes in SYS TH (e.g., Miro et al., 1990) and CFD areas are within the
scope and the framework of the book even though not explicitly part of the given list
of topics. The computational tools, mainly the SYS TH codes, constitute the end

<!-- page 18 (PDF 18) -->
product of the knowledge and the expertise in nuclear thermal-hydraulics: the related
technology includes code development (e.g., Bestion, 1990; Jeong et al., 2010); code
V&V (e.g., D’Auria et al., 2012a); code scaling (e.g., Glaeser and Karwat, 1993;
D’Auria and Galassi, 2010; Rohatgi, 2015); and code application (e.g., Revento´s
et al., 2010); in this case, the evaluation of uncertainty in code predictions (e.g.,
D’Auria et al., 2008) is a requisite for the proper consideration of applications in
nuclear reactor safety. Therefore, any concept or information reported in the book
should be considered as relevant to the SYS TH code development or application processes
(see also Section 1.1.3).

### 1.1.2 Objectives and target readers

Nuclear thermal-hydraulics appears like a universe of matters and themes: galaxies
and planetary systems of topics and skills can be distinguished and are needed for
the proper comprehension of the discipline. In such a universe vision of
thermal-hydraulics, Dr. Zuber already introduced the concept of quanta to deal with
scaling (Zuber, 2010). Here we may add that black-holes in the knowledge of
thermal-hydraulics still exist and may be associated with the modeling of turbulence
at either the microscale or the macroscale levels including the occurrence of boiling
and condensation in multifluid systems.
Then, a systematic and comprehensive treatment of all the matters and themes is
not realistic or possible, and an encyclopedia, or a series of books, is needed to ensure
reasonable covering of each matter. Rather one may note that a variety of textbooks
(some of those included in the list of references) exist which address one or more individual
topics in nuclear thermal-hydraulics: in this case, it is difficult to exceed their
quality and novelty.
Here what are not the objectives of the present book can be stated: not to have a
comprehensive covering or even mentioning of each important matter or theme in
nuclear thermal-hydraulics; not moving the boundary of knowledge by considering
quanta and black-holes mentioned above; not to replicate any existing textbook, rather
referencing those books.
A number of requirements are identified hereafter. The objective for the book can
be fixed as fulfilling those requirements.
l
A novel approach, or a new vision, for nuclear thermalhydraulics is envisaged or attempted.
l
Topics are discussed covering from fundamentals in thermal-hydraulics, i.e., mostly by
referencing appropriate literature (e.g., textbooks), to applications in NPP design and safety
technologies, including RR to the extent it is possible.
l
The impulse given to the knowledge by needs of nuclear reactor safety, unavoidably connected
with licensing rules, shall be recognized. The simplified chain is considered: regulatory
goals⃗accident analysis⃗phenomena⃗transient thermal-hydraulic needs.
l
From a logical view point and not necessarily connected with the order of chapters, a
topdown approach is pursued: then, needs come first (basically Chapter 4) and applications
are expected at the end (e.g., Chapters 15 and 16): noticeably, phenomena of interest come
after the needs (e.g., Chapters 4 and 6, respectively).

<!-- page 19 (PDF 19) -->
l
The technology impact is considered in each chapter (e.g., at least in introductory or closing
remarks).
l
The SYS TH code is seen throughout the book as the main/key repository of expertise in the
area. This implies consideration of code development (namely thermal-hydraulic bases for
development, e.g., Chapters 9–11), code V&V including the role of scaling and the evaluation
of uncertainty (e.g., Chapter 13), the code application to NPP design and safety (e.g.,
Chapter 14 dealing with the BEPU approach), and the results from AA (e.g., Chapters 15
and 16).
The innovation introduced with the book, other than transpiring from the requirements
, is: (a) to shed light on the connection between fundamentals of
thermal-hydraulics and application in nuclear technology; (b) to give emphasis to
the V&V, scaling, and uncertainty evaluation including related motivations and procedures
; (c) an as far as possible consistent formulation for the BEPU approach where
the pivot role of nuclear thermal-hydraulics is established: this includes an integrated
and nonconflicting role for DSA and PSA. Furthermore, the book has been written
having in mind the targets to promote the application of SYS TH codes within the
licensing process of existing and new nuclear reactors and to disseminate various steps
of the BEPU approach to software technologies different from SYS TH.
An alternative and consistent formulation of the requirements/objectives and innovation
introduced or expected for the book can be derived from the following
statements.

#### 1.1.2.1 Reformulation of the objective for the textbook

It is well clear that no numerical tool has the capability to predict the movement,
growth, and collapse of a single bubble moving inside a liquid when condensation
and evaporation processes take place. Similarly, there is no capability to simulate
all the effects of turbulence even in single-phase flows, e.g., in predicting pressure
drop at geometric discontinuity with an error which is acceptable for the design of
thermal-hydraulic systems. Prediction capabilities are even poorer or nonexisting
when a few bubbles move together and interact or when two-phase turbulence is considered
, respectively. Decades of development since now, e.g., in the area of
two-phase CFD, have not been sufficient to achieve a solution for the concerned computational
challenges. So, the obvious question arises: how is it possible to predict
transient two-phase mixture evolutions in complex geometrical systems like NPP
or RR? Then the objective of the book is to address such a question.
The instant-simplified answer is as follows and may be seen as the reformulated
objective for the book.
Time and space averaging is adopted in SYS TH codes, or approximate equations
are solved by approximate numerical methods: the impacts of approximations upon
the results, or the errors, are unknown. However, V&V procedures supported by
experimental data and suitable scaling analyses allow the quantification of those
errors. Qualified (as far as possible) uncertainty methods are established to this
aim. In different terms, one may state that expertise including the knowledge of data

<!-- page 20 (PDF 20) -->
measured in transient experiments is necessary to achieve qualified calculation results
from application of thermal-hydraulics.
Definitely, side objectives for the book are on the one hand to recognize the irreplaceable
role for SYS TH codes when establishing the safety of nuclear installations
(i.e., determined on transients which involve two-phase fluid mixtures time evolutions
) and on the other hand to clarify that rigorous V&V is needed and that any valuable
set of SYS TH calculation results must be supported by an uncertainty evaluation.

#### 1.1.2.2 To whom the book is addressed

Any scientist involved with nuclear thermal-hydraulics may take benefit from the
book (as already mentioned in “Chapter foreword”). This is specifically true for code
developers, nuclear thermal-hydraulic analysts, AA specialists including their supervisors
and, more in general, nuclear safety technologists.
Students in the last years of engineering courses and masters or PhD student/
researchers
are
expected
to
get
acquainted
with
the
vision
of
nuclear
thermal-hydraulics from the reading of the book.
In all cases the knowledge of thermodynamics and nuclear thermal-hydraulics fundamentals
is desirable, although not essential, for the comprehension of the concepts
in the book.

### 1.1.3 Content

Nuclear SYS TH constitutes the content and the subject for the book (according to the
title). Having recognized that it is not possible even to mention all important topics, a
selection of themes and matters has been assembled to form the content. This shall be
seen as a break-through of the universe of matters and themes mentioned in
Section 1.1.1. Then, an attempt is made to link bases and applications of nuclear
thermal-hydraulics; however, connections with other disciplines are recognized as
essential within the framework of applications and are not discussed in the book.
The sketch in Fig. 1.1, with short title for each chapter, provides an overall view
for the content including the roadmap and the strategy for the book. The top row of the
sketch synthesizes the framework for the book, i.e., the water-cooled NPP and
RR configurations, plus the academic disciplines thermodynamics and thermalhydraulics
, plus the needs from (NPP and RR) design and safety technologies. Then
the book is subdivided into three main parts, consistently with the objective in
Section 1.1.2: Part One introduces the background and aims at clarifying the current
vision for nuclear thermal-hydraulics, Part Two deals with features of the current SYS
TH codes, and procedures for the consistent application of SYS TH codes and results
are discussed in Part Three. Part Two has been further subdivided into two parts in the
Contents to distinguish between connections of thermal-hydraulics and modeling.
Motivations and rationale for each chapter are given below (a short title for each
chapter is also given, according to the boxes in Fig. 1.1). This also includes the discussion
of critical aspects where applicable and (unfortunately) unavoidable repetitions
of concepts.

<!-- page 21 (PDF 21) -->
#### 1.1.3.1 Chapter 1: Introduction

The framework of nuclear thermal-hydraulics used for the planning and the issuing of
the book is discussed in the present chapter.

#### 1.1.3.2 Chapter 2: Historical remarks

The nuclear thermal-hydraulics discipline was developed following the need to demonstrate
the NPP safety and, to a more limited extent, the NPP and the RR design. As
in all other fields where analytical methods are involved, nuclear thermal-hydraulics
took benefit of the development of computers. Thermodynamics, rather than
fluid-dynamics, is at the basis of the development of nuclear thermal-hydraulics
together with experiments in complex two-phase situations, namely geometry, high
power density, and pressure.
Mandatory licensing requirements originated by safety needs pushed huge investments
in research which drove the developments in the area. All of this created a
unique technology where highly geometry-dependent transient phenomena, sophisticate
two-phase flow modeling, continuously advancing numerics science, and
unavoidable empiricism derived from experiments are merged. This forms the iceberg
knowledge which needs to be mastered and managed also for the use of new generation
of scientists.
Fig. 1.1 Structure and content for the book.

<!-- page 22 (PDF 22) -->
The objective and the motivation for this chapter are to trace the history of the discipline
which is deemed necessary for its understanding and creating the perspectives
for development.

#### 1.1.3.3 Chapter 3: Definitions

Definitions may appear not necessary for an established discipline like nuclear
thermal-hydraulics: all terms should have a consolidated meaning within the myriad
and the variety of publications mentioned in Section 1.1.1. Unfortunately this is not
the case, one reason being the complexity of the discipline which reflects in the difficulty
of conjugating basic concepts like the principles of thermodynamics and complex
displays like subcooled void appearance during depressurization which impact
heat transfer and fission-generated power.
Then, objective and motivation for the chapter is to show the complexity of the
nuclear thermal-hydraulics discipline from the point of view of what are called
“definitions” (see below): then the chapter is complementary to the discussion in
Section 1.1.1.
“Definitions” here imply in most cases providing a message which shows the difficulty
associated with the concerned term. For instance, in the case of convection heat
transfer coefficient (HTC), the huge number of variables which affect HTC are balanced
by the simplicity of its correlation with heat flux and temperatures; in the case of
turbulence, the lack of any direct predictive capability or the current status of the DNS
is stressed; in the case of pressure drops at geometric discontinuity difficulties in measuring
a free-from-(large or not-acceptable)-error value for the local coefficient arise
because of need to distinguish between reversible and irreversible contributions to the
total pressure change: the problem becomes more complex when proper consideration
must be given to the condition of fully developed flow.
Three categories of definitions are envisaged:
(A) Variables
(B) Phenomena
(C) Concepts
The variables include the fundamental quantities which are also part of balance equations
, like temperature, pressure, velocity, material properties. Errors characterizing
or expected from the measurement and the prediction by analytical tools of those
quantities
are
outlined.
The
void
fraction
is
introduced
to
characterize
thermal-hydraulics. Furthermore non-dimensional quantities like Re, Pr, Nu, Fr are
also part of this class. The derivation of key non-dimensional quantities in
thermal-hydraulics and their physical meaning are discussed. Difficulties to apply
those quantities in scaling analysis are mentioned: e.g., during a transient, at a given
time, different Re values apply to different locations of the loop and a comprehensive
mapping of Re values in the entire loop may not be possible with a scaling method
alone not supported by a system code calculation.
Examples of discussed phenomena or concepts in thermal-hydraulics include natural
circulation, two-phase critical flow (TPCF), Critical Heat Flux, blow-down,

<!-- page 23 (PDF 23) -->
reflood and rewet, friction pressure drop (empirical) with main reference to two-phase
flow multiplier, conduction heat transfer (theoretical, but utilizing the empirical/
approximate Fourier law), convection heat transfer (empirical), and radiation heat
transfer (supported by theory, but needing empirical parameters). Aspects connected
with NPP and RR technology are emphasized.
The considered concepts encompass a variety of subjects and themes of the nuclear
thermal-hydraulics universe, ranging from phenomena-modeling terms like drift flux
formulation, to the characterization of equations like balance or conservation equations
, constitutive or closure equations, state equations, to approaches to perform a
calculation like conservative or best estimate, to modeling approaches like lumped
parameter model or UVUT (unequal velocities unequal temperatures) model dealing
with balance equations. Widely adopted terms like PIE, DBA, BDBA, and AM are
clarified.
Within the class of concepts, a connection is created between nuclear
thermal-hydraulics and fluid-dynamics and gas-dynamics, i.e., by including suitable
definitions. Then, the concept of turbulence can be used to connect thermal-hydraulics
with fluid-dynamics and gas-dynamics emphasizing the added complexity, as far as
turbulence is concerned associated with void fraction: flow-regimes (bubbly, slug,
churn, annular, etc.) can be seen as the connection between turbulence and
two-phase flows.

#### 1.1.3.4 Chapter 4: Needs

The development of nuclear thermal-hydraulics has several origins and motivations
including thermodynamics and fluid-dynamics sciences: nuclear technology had an
important role. In this chapter a reverse approach is pursued: starting points are the
existing configurations, operating conditions, and safety aspects of NPP and RR; then
an attempt is made to establish what capabilities are requested for nuclear
thermal-hydraulics.
In order to accomplish this goal the following sectors, not independent among each
other, are considered and reported hereafter together with examples of the origins of
needs:
l
Reactor coolant system for NPP: all water-cooled power reactor designs are included. Needs
are identified which are associated with the design of core and other RPV internals, steam
generators, separators, dryers (in the last two cases with main reference to BWRs), main
coolant pumps, pressurizer, recirculation legs.
l
Nonnuclear part of the NPP also known as balance of plant (BoP). The BoP has similar features
for NPP and oil or coal fueled plants for electricity generation. However in the case of
NPP the size of components, like turbines and condenser, may be larger than in conventional
plants and the attention originally devoted (e.g., in the 1950s and 1960s) to maximize the
thermal efficiency might have been lower (because of the smaller impact of the fuel upon
the cost of the produced electricity). So, needs may derive from the modernization or revamping
projects for existing NPP like decreasing pressure drops in the steam lines
l
Containment: the designs of tight (or zero leakage target after DBA) containment for almost
all NPP and of vented containments in “not-the-latest-generation” of Russian reactors need
thermal-hydraulic capabilities. Interesting to note that controlled venting became a desirable

<!-- page 24 (PDF 24) -->
feature after the Fukushima event in 2011. Containments equipped with pressure suppression
pool of liquid need deep thermal-hydraulics competence (e.g., estimation of vibrations
and loads on compartment walls).
l
RR designs: a variety of designs characterize the few hundreds RR now in operation. RR are
equipped with highly enriched uranium (HEU) core or, the larger number, by low enriched
uranium (LEU) core. Pool type or forced circulation RR are distinguished. Challenging
topics for nuclear thermal-hydraulics are the evaluation of margins available to the onset
of nucleate boiling (ONB) even during possible flow reversal consequence of main coolant
pump trip, i.e., the pathway from downward forced circulation to upward natural circulation.
The narrow passage for fluid across flat plate fuel elements also puts challenges to nuclear
thermal-hydraulics.
l
Safety analysis of water-cooled reactors: the needs for thermal-hydraulics primarily come
from the licensing requirements, e.g., the ECCS design criteria. Updating of requirements
and creating the link with computational capabilities constitute challenges for nuclear
thermal-hydraulics applications. Needs and challenges for nuclear thermal-hydraulics are
unavoidably defined outside the subject boundaries for the book: namely, the connection
between nuclear thermal-hydraulics and neutron physics, nuclear fuel (modeling), chemistry
(e.g., H2 production), mechanics (e.g., FSIs, modeling of flap or inertia valves, modeling of
the inertia of pump rotor, etc.), radioprotection (e.g., transport of radioactivity from core to
containment) are at the origin of needs.
Addressing the listed topics constitutes motivation and objective for the chapter.

#### 1.1.3.5 Chapter 5: Balance equations

Balance equations constitute the seed around which the predictive capabilities of
nuclear thermal-hydraulics have been built with main reference to transient
two-phase flow evolutions. This is the motivation for the chapter: predictive capabilities
in thermal-hydraulics do not exist without these equations. Balance equations,
synonymous of conservation equations, are established from the principles of science
and technology: mass and energy balance are derived from mass conservation and the
first principle of thermodynamics, and the momentum balance is derived from the first
principle of mechanics. Nuclear reactor thermalhydraulics may be studied using a
large variety of models which simplify more or less the physical reality.
The first problem of an engineer when investigating a reactor issue is to select the
right degree of simplification depending on the situation and the required accuracy
and reliability of the solution. Simplifications may result from the space and time resolution
and simulation tools include several scales from lumped parameter models to
CFD and CMFD. 0-D, 1-D, 2-D, and 3-D models are available for single- and
two-phase flow that use either time averaging or combined space-time averaging.
Each approach uses a set of balance equations for mass, momentum, and energy,
and the derivation of these equations may need complex mathematical developments
which will not be presented in detail for all modeling scales, since reference books
exist which may be referred to for readers who want to know more. Attention will
be drawn on the physical assumptions and simplifications used at some steps of the
derivation of equations and on the resulting limitations of the predictive capabilities.

<!-- page 25 (PDF 25) -->
The objective of this chapter is then to give a picture of all the available models
with an evaluation of the predictive capabilities and limitations, on the degree of accuracy
and reliability, and on the maturity of each model. More information will be given
on 1-D models since they are the most currently used in design and safety studies using
system codes. However 3-D models are also increasingly used, and the balance equations
are also presented to introduce CFD and CMFD.

#### 1.1.3.6 Chapter 6: Phenomena

The transient performance of NPP following plausible initiating events or accidents
and also changes in operating conditions (e.g., start-up and shutdown) brings to the
identification of phenomena. Phenomena are characterized by ranges of variations
of significant parameters and may involve steady-state or transient conditions.
Thermal-hydraulic phenomena are important owing (at least) to the following
reasons:
(1) Experiments in thermal-hydraulics either “integral” or “separate-effect” type must be
designed and executed in order to characterize the phenomena.
(2) A variety of empirical or non-first-principle-derived formulations needs to be developed
making reference to phenomena, e.g., including special models discussed in Chapter 10.
(3) A comprehensive list of phenomena properly characterized by significant parameters is
needed to ensure suitable validation for SYS TH codes as discussed in Chapter 13.
International activities performed at OECD/NEA/CSNI and by IAEA brought to the
identification of phenomena in the following conditions (sample list):
l
LBLOCA in PWR and VVER
l
SBLOCA in PWR and VVER
l
LOCA in BWR
l
Separate-effect phenomena in BWR and PWR
l
Shutdown conditions in PWR
l
AM in PWR
l
Containment response in PWR and BWR
l
Performance of passive systems characterizing the coming reactor design
l
Phenomena associated with RR
The motivation for the chapter derives from the needs (Chapter 4), and the objective is
to create a comprehensive list of phenomena which are described in a (as far as possible
) homogeneous way.

#### 1.1.3.7 Chapter 7: Heat transfer

Heat transfer and pressure drops are the main targets within the design of
thermal-hydraulics systems and a wide variety of approaches and precision needs have
been established and are available.
Chapters 7 and 8 are planned to constitute a bridge between the past and the future
for nuclear thermal-hydraulics: the evaluation of convection HTC has been among the
most important research targets since the beginning of the nuclear era and is among the
most important targets for the future with needs for increased calculation precision.

<!-- page 26 (PDF 26) -->
Selected important issues in the area which also constitute the motivation for the
chapter are outlined hereafter. Those issues may imply the need for further development
, for achieving common understanding and/or fixing precision goals for
calculations.
l
The convection HTC is defined on the basis of an empirical equation also known as Newton
law. This makes possible the quantitative evaluation from experiments but implies the existence
of a multidimensional surface where HTC is a function of dozens variables.
l
Reflood heat transfer implies the definition of a HTC which assumes (very) high values for a
few millimeter around the quench front; the reflood occurrence is associated with the quench
front propagation and may be associated with a surface temperature also called minimum
film boiling (MFB); in some situations, e.g., when a short (a few decimeters length) piece
of fuel rods remains to be quenched, a sort of homogeneous-instantaneous reflood
takes place.
l
Heat transfer from fuel clad surface at high temperature in the conditions of interest for
nuclear thermal-hydraulics on the one hand includes radiation and on the other hand may
occur toward different fields of the same phase, i.e., liquid film and droplets. Modeling
of both radiation heat transfer and liquid fields heat transfer poses challenges: the presence
of spacer grids causes additional complexity to the modeling.
l
Wall condensation occurs in containment during postulated accident conditions. Condensation
is affected by the presence of noncondensable gases including H2 and determines global
convection motion of the fluid which at its time governs H2 concentration, again putting a
challenge to nuclear thermal-hydraulics.
l
Conjugate heat transfer, in rough words connecting convection and conduction heat transfer,
has already been known since decades; however related analytical formulations have not
achieved maturity applicable to problems of technological interest.
The objective for the chapter is to present the current status and the vision for the
future in this (selected) area of the thermal-hydraulic science.

#### 1.1.3.8 Chapter 8: Pressure drops

Pressure drops and heat transfer are the main targets within the design of
thermal-hydraulics systems and a wide variety of approaches and precision needs have
been established and are available.
Chapters 7 and 8 are planned in the book also to constitute a bridge between the past
and the future for nuclear thermal-hydraulics: the evaluation of pressure drops, at geometric
discontinuities and in two-phase conditions, has been among the first targets
since the beginning of the nuclear era and is among the most important targets for
the future with needs for increased calculation precision.
Selected important issues in the area which also constitute the motivation for the
chapter are outlined below. Those issues may imply the need for further development
, for achieving common understanding and/or fixing precision goals for
calculations.
l
Modeling of friction pressure drop in single-phase flows is based upon an empirical approach
widely validated by experimental and theoretical data. This is not the case for two-phase
flows where the ancient approach characterized by two-phase flow multiplier is adopted:

<!-- page 27 (PDF 27) -->
this approach may have validity when fully developed flow conditions are established, i.e., a
situation never verified when accident conditions in NPP are calculated.
l
Pressure drops at geometric discontinuities in either in single- or two-phase conditions are
currently modeled by the application of empirically based coefficients. Assumptions are
needed to determine those coefficients from experiments and, usually, no dependence is
available from Reynolds number and void fractions: the impact of assumptions and of
the lack of specification of dependencies upon results of prediction is unknown. This
may largely contribute to the uncertainty of SYS TH code predictions.
l
Evaluation of pressure drop in case of sonic and supersonic velocity conditions implying
formation of shock waves.
l
Evaluation of acceleration pressure drops in a (not necessarily) closed boiling and condensing
system where irreversibility of the thermodynamic process may add up in terms of
complexity.
The objective for the chapter is to present the current status and the vision for the
future in this (selected) area of the thermal-hydraulic science.

#### 1.1.3.9 Chapter 9: Constitutive equations

Principles of thermodynamics and mechanics imply conservation of mass energy and
momentum which give origin to the balance equations (Chapter 5). However, the same
principles do not allow the characterization of the interactions between the phases also
including the appearance of geometry-dependent flow patterns.
Thus, constitutive equations are needed to model the interactions between the
phases and between each phase or field and the environment. As a target, the constitutive
equations must account of all possible conditions and phenomena expected in
NPP (and RR) within the DBA boundaries.
Selected important issues in the area which also constitute the motivation for
the chapter are outlined below. Those issues may imply the need for further development
, for achieving common understanding and/or fixing precision goals for
calculations.
l
The words “closure equations” are also used and may embed the constitutive equations or
may identify a class of equations having a mere numerical formulation which is focused at
achieving hyperbolic solutions from balance equations.
l
Water physical properties including derivatives are not usually classified as constitutive
equations: nevertheless tight interactions are established between water properties and constitutive
equations.
l
Constitutive and/or closure equations may have an empirical nature where measurement
errors and scatter of data are unavoidable: characterizing the impact of those errors and scatters
upon the results obtained from solving balance equations coupled with constitutive
equations may not have a commonly agreed answer.
l
Assumptions are needed to create solvable sets of closure equations. As an example, reference
can be made to the subdivision of wall heat flux, i.e., a unique value derived from experiments
, into contribution terms to liquid, steam, and, in some cases, steam-liquid interface.
Arbitrariness in the repartition is mitigated by consistency checks and partially validated
“a-posteriori” making use of experimental data independent from those used to generate
the original repartition.

<!-- page 28 (PDF 28) -->
l
An additional level of arbitrariness and complexity, following-up to the item above (assumptions
to create solvable sets of constitutive equations) occurs when either three fields or three
dimensions are part of the concerned thermal-hydraulic model.
Objective for the chapter is to provide the current status in the areas of development
and applications of constitutive equations and to provide evaluations or discussion
upon the topics listed above.

#### 1.1.3.10 Chapter 10: Special models

Reference is made here to the prediction of transient scenarios occurring in the concerned
water-cooled reactors, i.e., NPP and RR. The physical systems, or the physical
processes, or the phenomena which are not (or cannot be) modeled by what are called
constitutive equations embedded into balance equations are considered in the category
of special models. Namely, two broad categories of special models are distinguished,
related to:
(A) components and
(B) physical processes or phenomena
Examples in the former category are: centrifugal pump, jet pump, steam separator,
steam dryer, valves (various configurations), turbine.
Examples in the latter category are: pressure drop coefficients at geometric discontinuities
(also discussed in Chapter 8), flooding and counter-current flow limitation
(CCFL), TPCF when not derived from the set of balance and constitutive equations
which are standard for a given SYS TH code, direct contact condensation typically
at ECC port.
The motivation of the chapter is the importance of concerned components and
physical processes or phenomena in the frame of the prediction of transient scenarios.
The objective of the chapter is the description of models which constitute essential
parts of the SYS TH codes.

#### 1.1.3.11 Chapter 11: SYS TH codes

The envisaged role of the SYS TH codes within the nuclear thermal-hydraulics and the
pivot role for the same codes in the present book are discussed in this chapter.
As it may be derived from the notes in Section 1.1.1, the development of a SYS TH
code needs a variety of expertise, or matter and themes of the thermal-hydraulic universe
, including numerics, neutron physics, computer science, etc. Only thermalhydraulics
topics are discussed in Chapter 11.
Important aspects for best estimate SYS TH codes are (the last item below shall be
considered a consequence of the previous ones):
l
Demonstration of the qualification level
l
User effect upon the results of the calculation
l
Justification of the reason why approximate modeling may produce acceptable results
l
Need and way to evaluate the uncertainty
l
Acceptability by regulatory authorities

<!-- page 29 (PDF 29) -->
The motivation for Chapter 11 is the importance of the SYS TH code. The objectives
are a contribution to establish the capabilities of the codes based on the
thermal-hydraulics modeling and, as a consequence, in making robust the applications
to NPP and RR technology.

#### 1.1.3.12 Chapter 12: CFD codes

The computational fluid-dynamics (CFD) matter is apparently outside the main path
across the nuclear thermal-hydraulics universe selected for the book. However, at least
two reasons suggested the consideration of CFD codes in Chapter 12:
(1) CFD technology has potential for further development in the future also connected with
more powerful computing machines.
(2) Currently the application of CFD codes provides an irreplaceable role to support SYS TH
codes calculations in a large number of situations; examples of those situations are: PTS,
boron mixing and transport, temperature stratification, H2 transport in the containment.
CFD technology was born well before the advent of computers at the end of the 19th
century; however only the availability of powerful computers after the 1970s, during
the 20th century, allowed the application of CFD codes to problems of industrial interest
. Key differences between SYS TH codes and CFD codes are connected with the
turbulence modeling which is direct in the case of CFD and the averaging process
(e.g., at cross section or volume levels) which in principle is not needed in the case
of CFD codes. Namely convergence of results is expected with reduction in mesh sizes
in CFD codes, while the same goal cannot be demonstrated in a general situation in the
case of SYS TH codes. Moreover, in the case of CFD codes, attempts are made to
reduce the dependence upon the empiricism which characterizes the modeling of
SYS TH codes.
Currently debated aspects within the CFD technology are:
l
Results are still mesh dependent: i.e., not only the convergence of results cannot be
established in each application, but also changes in the mesh topology causes differences
in results.
l
Wall functions are needed, e.g., to take into account of friction or HTCs: this implies
reintroduction of empiricism, contrary to the no-empiricism target which characterizes
the development of CFD codes.
l
Maturity and/or robustness of solutions for single-phase applications in nuclear reactor
safety are claimed by code developers. However, this is not the case for two-phase
applications.
l
V&V methods including qualitative and quantitative acceptability targets are under discussion
within the scientific community.
l
Precision targets, as in the case of the SYS TH codes technology area, e.g., for punctual
velocity vectors, pressure drop scalar between two positions, punctual mixing scalar, etc.,
are not established.
All of the above shall be seen as a framework for the motivation of the chapter. The
objective of Chapter 12 is to present the current status of the development of CFD
codes focusing on modeling, capabilities, and perspectives.

<!-- page 30 (PDF 30) -->
#### 1.1.3.13 Chapter 13: Verification, validation, scaling, and uncertainty

This chapter can be characterized by the words “putting the right perspectives for
exploiting the current capabilities of SYS TH codes.” This means addressing the areas
of V&V, Scaling, and Uncertainty. Making use of some oversimplification, one may
state that scaling (and scaling needs, see also “Glossary” below) is an outcome of
V&V needs, as well as Uncertainty evaluation becomes a need following the evaluation
of V&V results.
If one uses the human body to create a parallel with nuclear thermal-hydraulics
where the body movement constitutes the application of the discipline, then the
SYS TH code is the hearth of the body and V&V including scaling and Uncertainty
constitutes the blood.
V&V, scaling, and uncertainty are the bridge between SYS TH codes development
and the application in nuclear technology. As a result of decades of R&D (as already
discussed) qualified numerical tools are available including capability to evaluate the
uncertainty; however, applications in the licensing process do not exploit those capabilities
and simplified (so-called conservative) methods are used. This situation may
appear controversial.
Then, objectives and motivations for the chapter are to show the robustness of the
processes and the methodologies adopted for V&V, scaling, and uncertainty.

#### 1.1.3.14 Chapter 14: BEPU approach

Several ways can be adopted to define BEPU, one of this being “BEPU=connection
between SYS TH code development and V&V, Scaling, Uncertainty on the one side and
licensing process on the other side.” Then, “BEPU is the application of SYS TH
codes.”
The BEPU process shall be associated with the licensing process. The licensing
process noticeably includes the PSA together with a number of methods not discussed
in the present book; those methods including PSA need a cross-link with BEPU. AA is
part of the licensing process.
Among the general attributes of AA, the first one shall be the compliance with the
established regulatory requirements.
The second attribute deals with the adequacy and the completeness of the selected
spectrum of events. The achievement of the spectrum of events (or envelope) shall be
the result of the combined applications of deterministic and probabilistic methods.
The third attribute is connected with the knowledge base including that captured by
the qualified computational tools and analytical procedures suitable for the analysis of
transient conditions envisaged for individual (concerned) NPP.
The complexity of a NPP and/or the accident scenarios may prove challenging for a
conservative analysis, thus justifying the choice for a BEPU approach. This implies
two main needs for nuclear thermal-hydraulics: (a) to adopt the current computational
tools, proving (to the regulatory authority) an adequate quality via suitable V&V and
(b) to adopt a qualified uncertainty method.

<!-- page 31 (PDF 31) -->
The motivation for Chapter 14 is to establish a role for BEPU within science and
technology, breaking the isolation which restricts now BEPU knowledge to a narrow
group of specialists. The idea is to consider BEPU as an essential piece of nuclear
thermal-hydraulics thus facilitating and spreading the application of SYS TH codes.
The objective of the chapter is to provide a suitable overview of the techniques and
the procedures part of BEPU, giving proper emphasis to the benefits expected from its
application.

#### 1.1.3.15 Chapter 15: DBA calculations

AA constitutes one key branch of nuclear reactor safety and of NPP (and RR) safety
demonstration as already mentioned. PIEs are at the origin of AA. The internal PIE
need transient calculations: the most powerful tool to perform transient calculation is
the SYS TH code. This constitutes the motivation for Chapter 15.
Answering the question “what calculations must be performed?” constitutes the
preliminary question to be addressed before the application of SYS TH codes to
the transient analysis. Addressing the questions brings to the DBA envelope for categories
of NPP. Grouping of the events part of the DBA envelope by principal cause of
the initiating events brings to the following list (categories of events):
l
Reactivity anomalies due to control rod malfunctions
l
Reactivity anomalies due to boron dilution or cold water injection
l
Coast-down of the main circulation pumps
l
Loss of primary system integrity (LOCA)
l
Interfacing systems LOCA
l
Loss of integrity of secondary system
l
Loss of power supply
l
Malfunctions in the primary systems
l
Malfunctions in the secondary systems
l
ATWS
l
Accidents in fuel handling
l
Accidents in auxiliary systems
l
Accidents due to external events
The objective of Chapter 15 is to discuss results of sample NPP transient analyses performed
by SYS TH codes. Results of calculations are synthesized by time trends, and a
connection is established with phenomena presented in Chapter 6.

#### 1.1.3.16 Chapter 16: Occurred NPP accidents: the thermal-hydraulics

Accidents have occurred in NPP (and RR) and are part of the history of nuclear technology
. Those accidents had a noticeable impact upon the development of the technology
and, unfortunately, a negative impact upon the exploitation of the technology
for electricity production. This constitutes the motivation for Chapter 16 although this
is an unexpected chapter for those who planned the development of nuclear
thermal-hydraulics till the late 1970s of the previous century.

<!-- page 32 (PDF 32) -->
The considered nuclear events are listed below together with implications in
nuclear thermal-hydraulics although recognizing in advance the low role that
thermal-hydraulics competences and expertise had in the occurrence of the event
or mitigating their consequences (where applicable).
Implications signify changes in the importance of sectors of thermal-hydraulics
and investments to better address new challenges for nuclear technology derived from
those accidents, i.e., lessons learned.
l
TMI, Unit 2 (TMI-2), LOFW-SBLOCA combined event, March 1979. As a consequence
of the event, focus of investigation in nuclear thermal-hydraulics was shifted from LBLOCA
to SBLOCA: this means the shift from homogeneous conditions in the vessel to stratified
conditions. This can also be translated as shift from HEM or EVET modeling to UVUT
modeling. The TMI-2 event also triggered huge investments for experiments in
large-scale ITFs.
l
La Salle, Unit 2, and Oskarshamn, Unit 2, BWR stability events, respectively, Mar. 1988 and
Feb. 1999. As a consequence of the first event, a systematic reevaluation of the capabilities to
predict density wave instability (DWI) phenomena took place. This basically brought to
understanding that DWI depend upon a large number of factors including their combined
effect, and upon minor changes of each factor that are difficult to predict. However, DWI
events appear to have an incubation period which is detectable making mild or negligible
the safety impact of possible modeling inadequacies.
l
Chernobyl, Unit 4, neutron flux and thermal power excursion event, April 1986. As a consequence
of the event operator independent systems became a fashion in the new design.
Thus the event triggered the appearance of passive systems and both new-generation
PWR and BWR were equipped by passive systems, noticeably AP-600 (later on
AP-1000) and SBWR (later on ESBWR).
l
Fukushima, Units 1-3, LOOSP event, Mar. 2011. As a consequence of the event, controlled
containment venting, already introduced in Germany (a concept already part of the design of
the early Soviet Union reactors to avoid the construction of containment walls resistant to the
full pressure caused, e.g., by a LOCA) became of interest. The event also solicited more
attention to low-probability situations (e.g., high-intensity earthquake in the deep water
of ocean) which once occurred may reveal precursor with high probability of dangerous scenarios
for the plant (e.g., the tsunami).
The objective for the chapter is to describe the transient thermal-hydraulic scenarios
occurred during the concerned events. Some emphasis is given to consequences in the
development of thermal-hydraulics.

#### 1.1.3.17 Chapters interconnections

Chapters 1–4 are directly or indirectly connected among each other (namely chapter 1 is
connected to Chapters 2–4 and connections exists between Chapters 3 and 4) and to all
remaining chapters.
Chapters 5–10 are directly connected to Chapter 11 (SYS TH code).
Chapter 11 (SYS TH code) is at the origin of Chapters 13–16. Thus, Chapter 11 plays a pivot
role in the present book as already emphasized.

<!-- page 33 (PDF 33) -->
Additional key connections among chapters are:
l
Chapters 4 and 6: the knowledge of thermal-hydraulic phenomena (Chapter 6) constitutes a
need which is clarified in Chapter 4.
l
Chapter 5 (balance equations) constitutes the framework and the basis for Chapters 9 and 10:
namely, in case of Chapter 10 (special models), the situations which cannot be calculated
by balance equations shall be dealt by special models; furthermore constitutive equations
(Chapter 9) must be integrated into balance equations (Chapter 5). All together, Chapters
5, 9, and 10 constitute the input for Chapter 11 (SYS TH code). Chapter 5 shall also be seen
as providing (partial) input to Chapter 12 (CFD code).
l
Chapter 6 (phenomena) has direct connection and interrelation with Chapters 11, 13, and 15:
the development of SYS TH codes (Chapter 11) needs the knowledge of phenomena; the
validation of SYS TH codes (Chapter 13) must be based upon the phenomena; finally, phenomena
must be derived from the envelope of DBA (Chapter 15).
l
The knowledge of subjects from Chapter 7 (heat transfer) and Chapter 8 (pressure drop) is
embedded into the SYS TH code, thus creating a direct connection between those Chapters
and Chapter 11.
l
Chapter 9 (constitutive equations) shall be seen as a necessary support for (the solution of )
balance equations discussed in Chapter 5. Both Chapters 5 and 9 provide input to the development
of SYS TH code discussed in Chapter 11. Duplication of concepts appears unavoidable
between Chapters 5 and 9 from the one side and Chapter 11 from the other side.
However the authors made an effort to present complementary information and different
viewpoints.
l
The knowledge and the subjects from Chapter 10 (special models) are embedded into the
SYS TH code thus creating a direct connection between this Chapter and Chapter 11. Furthermore
pressure drop at geometric discontinuities are also discussed in Chapter 8.
l
Chapter 11 (SYS TH code) is the end product of scientific competence and knowledge from
Part Two of the book and, in a weaker sense, from Part One: the role of this chapter has
already been discussed.
l
Chapter 12 (CFD codes) has key connection in the book with Chapter 5 (balance equations)
and Chapter 11 (SYS TH codes). In this last case, the connection is not only to provide support
to the SYS TH code calculations but also to establish strategic difference in the two
modeling approaches.
l
Chapter 13 (V&V, scaling, and uncertainty) constitutes the articulated joint between Chapter
11 (SYS TH codes) and Chapter 15 (codes application to NPP), see also role of BEPU
approach (Chapter 14).
l
Chapter 14 (BEPU approach) shall be seen as having the upstream interface with Chapter 13
(V&V, scaling, and uncertainty) and the downstream interface with Chapter 15 (DBA calculations
) when the licensing process is concerned.
l
Chapter 15 (DBA calculations) is possible because of SYS TH (Chapter 11) codes application
. In addition a like is established with phenomena in Chapter 6.
l
Chapter
16,
i.e.,
occurred
NPP
accidents,
has
weak
connections
with
nuclear
thermal-hydraulics. Rather, the nuclear thermal-hydraulics discipline and, noticeably, the
SYS TH codes allowed or facilitated the understanding of the progression of the events.
An attempt is made in Chapter 16 to establish the connection between nuclear
thermal-hydraulics and those NPP accidents.
