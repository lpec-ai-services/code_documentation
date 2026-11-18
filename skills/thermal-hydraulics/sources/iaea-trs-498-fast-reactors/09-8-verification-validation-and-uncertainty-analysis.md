# 8. VERIFICATION, VALIDATION AND UNCERTAINTY ANALYSIS
<!-- source PDF pages 60-67 -->

<!-- page 48 (PDF 60) -->
# 8. VERIFICATION, VALIDATION AND UNCERTAINTY ANALYSIS

## 8.1. INTRODUCTION TO VERIFICATION, VALIDATION AND

UNCERTAINTY ANALYSIS
This section focuses on the verification, validation and uncertainty
analysis of computer codes used in LMFRs, including SFRs and lead and LBE
cooled fast reactors (or LFRs). Track 6 of the Technical Meeting on State-ofthe
-art Thermal Hydraulics of Fast Reactors [2] presented four papers covering
verification, validation and uncertainty analysis. D. de Luca presented the NINE
thermal hydraulic contribution to IAEA Coordinated Research Projects (CRPs)
focused on SFRs [160]. J. Yanez presented his work “Reduced order model
for thermal hydraulics problems: Towards uncertainty quantification for CFD
simulations” [161]. J. Liao highlighted achievements in the work focused on
enhancing the applicability of the SAS4A/SASSYS-1 computer code to LFR
systems [162]. O. Bovati delivered the last presentation, “Validation of RANS
and LES simulations on a 61-pin wire wrapped fast-reactor fuel assembly” [163].
The topic of verification, validation and uncertainty analysis is also addressed in
other tracks, such as Track 2 and Track 3.
This section presents the state of the art in verification, validation,
uncertainty and sensitivity analysis, and lessons learned from international
benchmarks of LMFR based on the publications in Track 6 and open literature.

## 8.2. VERIFICATION AND VALIDATION

Computer codes used in nuclear engineering, after the development phase,
will pass through V&V to ensure the pedigree of the code. Verification is the
process of ensuring that the products and processes of each major activity of
the life cycle meet the standards for the products and objectives of that major
activity. The verification of computer code usually involves a comparison
against an idealized problem or analytical solution to justify the functionality of
the code. Validation is the process of demonstrating that the as built software
meets its requirements. Validation is usually performed via benchmarking against
experimental results or a system performance. The purpose of these assessments
is to validate the models in the safety analysis code of nuclear reactors and to
determine the bias and uncertainty of these models.

<!-- page 49 (PDF 61) -->
The computer codes used in the assessment of LMFR range from system level
and component level computer codes to codes for high resolution CFD. Notable
system level computer codes for LMFR include RELAP5 MOD3.3, RELAP5-
3D, SAS4A/SASSYS-1, TRACE, HYDRA-IBRAE/LM and SPECTRA, as well
as the subchannel computer codes of COBRA, CTF and ANTEO+. The CFD
codes include STAR-CCM+, OpenFOAM and ANSYS Fluent.
In the computer code validation, the performance of the code is assessed
against important phenomena for a defined scenario, such as normal operations,
anticipated operational occurrences, DBAs and beyond DBAs in nuclear reactors.
These phenomena could be identified and their significance assigned in the PIRT.
The PIRT, the requirements for V&V and the uncertainty quantification are
usually defined within a framework of best estimate plus uncertainty (BEPU).
A typical framework that has been widely used in the nuclear industry is the
Evaluation Model Development and Assessment Process developed by the
United States Nuclear Regulatory Commission [164], as illustrated in Fig.  7.
Other frameworks, for example SAPIUM [165], have been developed with
the support of OECD/NEA and the code scaling, applicability and uncertainty
(CSAU) methodology [166].
The assessment matrices for these computer codes are usually established
with applicable SETs and integral effects tests based on phenomena identified in
the PIRT of the corresponding accident scenarios. The SETs are used to assess
groups of empirical correlations and other closure models in the safety analysis
code associated with each important phenomenon. The assessment against SETs
can also produce the uncertainty range of modelling of a specific phenomenon.
The integral effects tests are used to assess system interactions and global
code capabilities.
Extensive testing campaigns over the last 60 years have provided a large
thermal hydraulic experimental database for the validation of thermal hydraulic
computer codes for LMFR. The IAEA Catalogue of Facilities in Support of
LMFNS database [167, 168] provides a list of existing sodium and Pb/LBE test
facilities, and this list has continued to expand in recent years, especially for
Pb/LBE test facilities. The IAEA database includes a comprehensive collection
of global Pb/LBE test facilities, along with a brief description of each. There are
195 Pb/LBE facilities located in 14 countries and the EU [167], and 107 sodium
facilities in ten countries [168]. These facilities are expected to provide valuable
experimental data for the validation of thermal hydraulic computer codes.
Caramello et al. [56] presented the testing campaign supporting ALFRED
LFR development. The testing programme generated a large amount of
experimental data to validate the numerical simulation computer codes for
thermal hydraulic analysis of the reactor coolant pool, reactor core and safety
systems. The numerical simulations utilized both system codes and CFD tools.

<!-- page 50 (PDF 62) -->
A series of experiments was carried out at the ENEA Brasimone laboratory in
the CIRCE large pool integral facility to investigate relevant thermal hydraulic
phenomena occurring under normal and abnormal operating conditions. CIRCE
is a non-nuclear (electrical) experimental platform on a scale representative of
pool type LFRs. The experimental data obtained from the CIRCE pin bundle
were compared with numerical simulations, and the comparison showed good
agreement with the Nusselt number values, which were close to the values
computed using fuel bundle heat transfer correlations and the results obtained
from the CFD analysis.
The water–LBE interaction is an important phenomenon in postulated
steam generator tube rupture accidents. An experiment was performed in the
CIRCE facility, and a simulation was carried out with the SIMMER-IV computer
code. Because of the limitations of computational resources, only the CIRCE
main vessel was modelled, and the upstream and downstream components
were substituted with experimental pressure time trends imposed as boundary
conditions in the SIMMER-IV calculation. The obtained numerical results
showed good agreement with the measured main vessel pressure and temperature
time trends. Furthermore, the prediction from RELAP5-3D is benchmarked
against test results from the SIRIO decay heat removal facility, which is a scaled
test facility for the safety system of ALFRED.
Roelofs et al. [64] summarized the R&D on fast reactor thermal
hydraulics in the Dutch PIONEER programme. Within the programme, system
 FIG. 7. Illustration of evaluation model development and assessment process [164].

<!-- page 51 (PDF 63) -->
thermal hydraulic computer codes (SPECTRA), CFD codes and multiphysics
simulations are benchmarked against liquid metal experimental data, ranging
from fundamental turbulent heat transfer to core, pool and reactor system thermal
hydraulics. These validations enhance the pedigree of these codes in their
application to liquid metal reactors. However, Roelofs et al. [64] also concludes
that the validation basis for liquid metal reactors is limited and that more
experiments are needed to generate sufficient data to support this validation.
Liao et al. [162] presented an applicability enhancement of the
safety analysis computer codes used in the Westinghouse LFR analysis:
SAS4A/SASSYS-1 for the reactor core and reactor vessel, and GOTHIC for
the passive heat removal system. A V&V matrix for SAS4A/SASSYS-1 was
developed, including verification cases covering both SFRs and LFRs, and it
contains over 300 test cases. The validation cases of SAS4A/SASSYS-1 include
SFR experiments performed over the past 50 years, such as reactor data from
EBR-II, Phénix, and FFTF; the NSTF SET; and oxide fuel performance/failure
tests in SFRs. A validation of the integral effects of the CIRCE-HERO loss of
flow test enhances the applicability of SAS4A/SASSYS-1 to LFR systems.
Additional V&V cases are planned to address the validation gaps identified in
the Westinghouse LFR PIRT using experimental data from the VLF and PHRF
facilities, as well as the IAEA CRP on NACIE loss of flow tests.
Lorusso et al. [169] reported on the state of the art of the thermal hydraulic
system code RELAP5 for heavy liquid metal (Pb/LBE) applications. The
RELAP5 application has been extended from LWRs to heavy liquid metal
reactors through further improvements made by ENEA. The improved RELAP5
code is benchmarked against various lead and LBE experiments conducted at
the ENEA research centre, such as CHEOPE, CIRCE and NACIE, as well as
the international programmes MEGAPIE and LACANES. The benchmarking
of RELAP5 against other computer codes was performed. These validations
improved the qualification of the RELAP5 code for supporting reactor design
and for use as a safety analysis tool for heavy liquid metal pool type reactors.

## 8.3. UNCERTAINTY AND SENSITIVITY ANALYSIS

In any safety analysis methodology, uncertainty quantification is of
critical importance in determining the final prediction and safety margin, and it
is required in the regulatory guidance for safety analysis [164, 170]. Sources of
uncertainty in the safety analysis framework include uncertainties arising from
the computer code, from user input, from measurement errors in the experiments
and from scaling. The uncertainty of computation is obtained by benchmarking

<!-- page 52 (PDF 64) -->
against experimental data, primarily the data from SETs designed for the
important phenomena identified in PIRT.
The safety analysis methodology and the uncertainty quantification for
pressurized water reactor loss of coolant accident analysis and boiling water
reactors are relatively mature, as they are part of regulatory approved BEPU
evaluation models [171–173]. The first generation of best estimate loss of coolant
accident analysis methodology was based on the CSAU approach [170]. The
approach endorses the response surface method to address uncertainties in the
best estimate loss of coolant accident analysis. Generally, a response surface is
developed to act as a surrogate for the computer codes used in estimating the total
uncertainty. The response surface can then be extensively Monte Carlo sampled
to determine the total uncertainty. The use of limited computer calculations to
develop an accurate response surface is followed by sufficient Monte Carlo
sampling of the response surface in an effort to be as thorough as necessary, yet
as economical as possible.
However, the shortcomings of the response surface method were identified
in its early applications. Since then, direct Monte Carlo methods and the use of
non-parametric statistics have prevailed in best estimate loss of coolant accident
safety analyses [174]. The implementation of the direct Monte Carlo method is
straightforward; it simply requires sampling the input distributions n times and
then using the computer code directly to generate n outputs, which are used to
estimate the actual distribution. Even though there are many statistical methods
to address total uncertainty, the non-parametric statistical sampling technique
is commonly accepted by nuclear regulators. The non-parametric statistical
sampling technique is sometimes referred to as ‘distribution free’. It is possible to
determine the tolerance limits from unknown distributions by randomly sampling
the characteristic in question. The consideration of non-parametric tolerance
limits was originally proposed in Ref. [175].
Besides the response surface method and the non-parametric statistical
method used in the licensed safety analysis method, there are other emerging
uncertainty methods or BEPU frameworks. For example, the OECD
supported Best Estimate Methods Uncertainty and Sensitivity Evaluation
(BEMUSE) [176] and Post-BEMUSE Reflood Models Input Uncertainty
Methods (PREMIUM) [177]. SAPIUM [165] is a generic framework for the
quantification of the input uncertainty of thermal hydraulic computer code.
The BEPU frameworks and uncertainty methods, although they were not
initially developed for LMFR safety analysis, are applied to the best estimate
safety analysis of LMFR, which is envisioned as an extension with small
adjustments. De Luca et al. [160] presented NINE’s simulation models, which
comply with the best estimate principle and demonstrated their applicability to
SFR thermal hydraulic analysis.

<!-- page 53 (PDF 65) -->
## 8.4. LESSONS LEARNED FROM INTERNATIONAL BENCHMARKS

The IAEA supports international benchmarking against liquid metal
fast reactor experimental data, focusing on sources ranging from experimental
reactors to thermal hydraulic testing facilities via various CRPs. These CRPs
address the technical challenges in LMFR modelling and simulation using
system analysis codes, CFD and subchannel analysis codes. They also identify
additional opportunities for R&D work to further develop liquid metal cooled
reactor technology. They have led to extensive benchmarking and numerous
publications, including IAEA reports as well as conference and journal papers
based on this benchmarking work. The relevant CRPs on thermal hydraulics
benchmarking activities are listed below and discussed in this section:
— Benchmark Analyses on the Natural Circulation Test Performed During the
Phénix End-of-life Experiments [178];
— Benchmark Analyses of Sodium Natural Convection in the Upper Plenum
of the Monju Reactor Vessel [179];
— Benchmark Analysis of EBR-II Shutdown Heat Removal Tests [180];
— Benchmark Analysis of FFTF Loss of Flow Without Scram Test [181];
— Benchmark of Transition from Forced to Natural Circulation Experiment
with Heavy Liquid Metal Loop [182].
The IAEA CRP Benchmark Analyses on the Natural Circulation Test
Performed During the Phénix End-of-life Experiments [178] started to provide
benchmarking analyses on natural circulation tests in 2007, before the reactor
was shut down in 2009. A total of eight organizations from nine countries
participated in the CRP, using various computer codes, including system analysis
codes, neutronics codes and CFD. The Phénix Natural Circulation Benchmark
Test examined a protected loss of heat sink transient from 35% power and
70%  flow conditions with the objective of demonstrating the effectiveness of
natural circulation in the primary system and the effect of dynamic heat rejection
via secondary cooling systems. Approximately three hours after pump trips in the
primary and secondary systems, heat rejection of the total system was augmented
by air cooling of the steam generators, the effects of which were evident from
the temperature conditions of the primary and secondary systems. Although
reasonable predictions can be obtained from various computer codes, accurate
prediction of natural circulation remains a challenge as the core flow pattern is
complicated. A key recommendation is to develop a complete validation process
for the numerical codes used in the prediction of natural convection decay heat
removal, including analytical tests, reduced scale testing and real reactor testing.

<!-- page 54 (PDF 66) -->
The IAEA CRP Benchmark Analyses of Sodium Natural Convection in
the Upper Plenum of the Monju Reactor Vessel [179] was initiated in 2008 with
the objective of improving analytical capabilities in SFR thermal hydraulics,
specifically regarding the thermal stratification phenomenon in the upper
plenum of the reactor vessel. A total of eight organizations from seven countries
participated in the CRP. CFD tools were employed to simulate the thermal
stratification of sodium observed in the Monju reactor vessel during a turbine
trip test at 40% of rated electrical power conducted in December 1995, during
the original startup experiments. Monju is a nuclear power plant that breeds
fuel using fast neutrons and is cooled by sodium. The main cooling system of
the reactor consists of three loops. The thermal output is 714 MW(th) and the
electric output is 280 MW(e) due to the high thermal efficiency. CRP participants
concluded that the analytical capabilities in the field of in-vessel sodium thermal
hydraulics, especially in the areas of meshing and algorithm selection criteria,
had improved, despite the challenging issue of the complex geometry of Monju.
The IAEA CRP Benchmark Analysis of EBR-II Shutdown Heat Removal
Tests [180] was initiated in 2012 with the objective of improving the state of the
art SFR computer codes by extending their validation to include comparisons
against whole plant data recorded during shutdown heat removal tests (SHRTs)
conducted at Argonne’s EBR-II in the 1980s. A total of 19 organizations from
11 countries participated in the CRP using various computer codes, including
system analysis codes, neutronics codes, CFD and subchannel codes. The
benchmark activity focused on the analysis of the SHRT-17 and SHRT-45R
tests. The objective of SHRT-17 was to demonstrate the effectiveness of natural
circulation in the reactor, whereas the objective of SHRT-45R was to demonstrate
the ability of passive reactivity feedback to reduce the reactor power to decay
heat power levels. Key phenomena exhibited during these tests include flow
coastdown behaviour, the development of natural circulation flow regimes,
thermal stratification in pool volumes and the Z-pipe and inherent reactivity
feedback mechanisms (primarily fuel/core expansion, Doppler effects and
coolant feedback effects).
Even though details of the plant design were only partially available, and
there were possible measurement deficits in the intermediate heat exchanger inlet
temperature measurement, the CRP participants collectively showed significant
modelling progress over the course of the CRP and were able to predict most
plant parameters with acceptable accuracy. The CRP also provided an opportunity
to apply the SCCRED6 qualification process to a fast reactor system. The major
lessons learned from this CRP benchmarking were captured in the IAEA report
(see Ref. [180]).
6	 Standardized Consolidated Calculated and Reference Experimental Database.

<!-- page 55 (PDF 67) -->
The IAEA CRP Benchmark Analysis of FFTF Loss of Flow Without Scram
Test [181] focused on the benchmark analysis of one of the unprotected passive
safety demonstration tests performed at the FFTF. It was launched in 2018 to
support collaborative efforts within international partnerships on the validation
of simulation tools and models in the area of SFR cooled passive safety. The
FFTF was a 400 MW(th) thermal loop type SFR prototype with mixed oxide
fuel, built at the Hanford site in the USA to assist in the development and testing
of advanced fuels and materials for fast breeder reactors. FFTF reached its first
criticality in 1980 and operated until 1992. The benchmark activity focused on
the analysis of Loss of Flow Without Scram tests at power levels up to 50%,
commonly referred to as unprotected loss of flow tests, along with the passive
safety system of gas expansion modules, which provides negative reactivity
insertion to protect the reactor core during transients. The computer codes
included system analysis codes, neutronics codes, CFD and subchannel codes.
According to De Luca et al. [160], the FFTF Loss of Flow Without Scram Test
#13 was initiated when the primary pumps tripped simultaneously. Then the
increase in core temperatures, together with the drop in the sodium level in the
gas expansion module, introduced a large negative reactivity feedback, causing
power to decrease faster than the primary flow rate. The simulation results were in
good agreement with the experimental data for the entire duration of the transient.
In particular, the timing of the occurrence of the two coolant temperature peaks
was captured very well by the simulation.
Although the SFR CRPs focused on benchmarking with nuclear test
facilities, LFR benchmarking is performed using electric powered integral
effects test facilities. In computer code validation, there are advantages and
disadvantages to both nuclear test facilities and electric powered test facilities.
The IAEA CRP Benchmark of Transition from Forced to Natural Circulation
Experiment with Heavy Liquid Metal Loop [182] is ongoing and focuses on
benchmark analyses of loss of flow transients, covering forced flow to natural
circulation flow in the NACIE loop test facility (Fig. 8) at the ENEA site in
Brasimone, Italy [31]. The NACIE facility features a rectangular LBE flow loop.
It contains a wire spaced 19 pin fuel pin simulator with a power output of 250 kW.
Transient analysis of thermal hydraulic phenomena in NACIE loop tests provides
an excellent opportunity for the validation of physical and mathematical models,
as well as numerical simulation codes for lead or LBE cooled reactors, using
actual experimental data. Various computer codes, including system analysis
codes, subchannel codes and CFD, are applied in the benchmarking. The CRP
is expected to enhance the benchmarking of these computer codes in the lead
and LBE reactors.
