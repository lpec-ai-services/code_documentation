# Front matter
<!-- source PDF pages 1-3 -->

<!-- page 831 (PDF 1) -->
Verification and validation of
system thermal-hydraulic
computer codes, scaling and
uncertainty evaluation of
calculated code results
H. Glaeser
GRS, Garching, Germany
Abstract
The approximations of system thermal-hydraulic (SYS TH) codes necessitate proper
verification and validation (V&V) processes. Validation by predictions of complex
phenomena can only be performed after the availability of relevant experimental data.
Since many experiments used to validate a code are in small scale compared with a
nuclear reactor, the scaling effects have to be considered. Therefore, scaling effects or
addressing the scaling issues must be part of the validation activity. Deviations between
calculation results and experimental data are observed. Consequently, various sources of
uncertainty are identified and uncertainty methods for their quantification have been
developed. International programs highlighted the validation, scaling and qualification
of uncertainty methods. The chapter discusses V&V, scaling and the evaluation of uncertainty
including the effects of the code users.
Nomenclature
AEA/AEAT
Atomic Energy Agency/Technology (UK)
AEKI
Atomic Energy Agency (Hungary)
ANS
American Nuclear Society
BEMUSE
Best Estimate Methods—Uncertainty and Sensitivity Evaluation
BWR
boiling water reactor
CCFL
counter-current flow limitation
CEA
Commissariat a L’Energie Atomique (France)
CFD
computational fluid dynamics
CFR
Code of Federal Regulation
CIAU
code with the capability of internal assessment of uncertainty
CSAU
code scaling, applicability, and uncertainty
CSNI
Committee on the Safety of Nuclear Installations
DVI
direct vessel injection (line)
DSA
deterministic safety analysis
Thermal Hydraulics in Water-Cooled Nuclear Reactors. http://dx.doi.org/10.1016/B978-0-08-100662-7.00013-0
© 2017 Elsevier Ltd. All rights reserved.

<!-- page 832 (PDF 2) -->
ECC
emergency core cooling
ECCS
emergency core cooling systems
EMDAP
evaluation model development and assessment process
ENUSA
Empresa Nacional del Uranio, SA (Spain)
FCM
fractional change metric
FFTBM
fast Fourier transform-based method
FRC
fractional rate of change
FSA
fractional scaling analysis
GRS
Gesellschaft f€ur Anlagen- und Reaktorsicherheit (Germany)
H2TS
hierarchical two-tiered scaling
IAEA
International Atomic Energy Agency
IPSN
Institut de Protection et de Suˆret⟨e Nucl⟨eaire (France)
IRSN
Institut de Radioprotection et Suˆret⟨e Nucl⟨eaire (France)
IRWST
in-containment refuelling water storage tank
ISP
International Standard Problem
IT
integral test
ITF
integral test facility
I/O
input/output
JNES
Japan Nuclear Energy Safety Organization
KAERI
Korean Atomic Energy Research Institute
KINS
Korean Institute for Nuclear Safety
LB
large break
LOCA
loss of coolant accident
LWR
light water reactor
NPP
nuclear power plant
NRC
Nuclear Regulatory Commission (USA)
NRI
Nuclear Research Institute (Czech Republic)
OECD
Organization for Economic Cooperation and Development
PDF
probability density function
PIRT
phenomena identification and ranking table
PREMIUM
Post-BEMUSE REflood Model Input Uncertainty Methods
PSI
Paul Scherrer Institute (Switzerland)
PWR
pressurized water reactor
QAM
quantity accuracy matrix
SB
small break
SET
separate effects test
SYS
System
TH
Thermal-Hydraulics
UMAE
uncertainty method based on accuracy extrapolation
UMS
uncertainty method study
UNIPI
University of Pisa (Italy)
UPC
University of Barcelona (Spain)
USNRC
United States Nuclear Regulatory Commission (see also NRC, USA)
V&V
WWER
water-cooled and water-moderated energy reactor

<!-- page 833 (PDF 3) -->
Symbols
J _X =
_MX
ρXADC
ρX
gW ρW □ρs
ð
Þ
½
·
Wallis number=dimensionless superficial velocity based on
downcomer annulus circumference
K _X =
_MX
ρXADC
ρX
gσ ρW □ρs
ð
Þ
½
·
Kutateladze number=dimensionless superficial velocity based
on surface tension
ADC
flow cross section of downcomer
Bo
Bond number
dav
downcomer average diameter
douter
downcomer outer diameter
Fr
Froude number
g
gravity
L
characteristic geometrical length
M
mass flow rate
W
average downcomer annulus circumference
θECC-BCL
angle between ECC injection leg and broken loop
ν
kinematic viscosity
ρ
density
σ
surface tension
Subscripts
g
vapor
l
liquid
s
steam
w
water
x
either steam or water
Chapter foreword
Validation (and verification, i.e., what is included in the acronym V&V), scaling, and
uncertainty constitute crosscutting issues from development to application in system
thermal-hydraulics (SYS THs). The unavoidable approximations introduced at the
development level of any code model, including the lack of direct consideration
of turbulence, the averaging, and the application of theorems from mechanics of
continuum to the noncontinuum two-phase flows impose a validation process. The
difficulty to perform experiments (even to be used for validation) at the same conditions
(size, geometry, pressure, and power) of the prototype nuclear power plants
(NPPs) needs to deal with the scaling issue. Differences between measured and
calculated values of transient variables and consequently expected deviations in
predicting accident scenarios in NPPs are a reason to deal with uncertainty.
Thus, this chapter is connected with Chapters 5, 9, and 10 of the book where modeling
features are discussed in addition to Chapters 7 and 8. The chapter is also connected
with Chapter 11 where system code validation, scaling, and uncertainty
