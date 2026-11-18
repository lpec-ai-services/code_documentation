# Chapter foreword
<!-- source PDF pages 4-5 -->

<!-- page 732 (PDF 4) -->
RMS
root mean square
RNG
renormalization group (method to renormalize the NS equations)
RPV
reactor pressure vessel
RSICC
Radiation Safety Information Computational Center
RSM
Reynolds stress model
SA
Spalart-Allmaras (model)
SAS
scale-adaptive simulation
SG
steam generator
SGDH
simple gradient diffusion hypothesis
SGS
subgrid scale
SMC
second moment closure
SP
standard problem (CFD exercise)
SRS
scale resolving simulation
SSG
simple support grids or Speziale-Sarkar-Gatski (related to RSM)
SST
shear stress transport
STAR-CCM+
CFD code
SYS TH
system thermal-hydraulics (codes)
UQ
uncertainty quantification
TAMU
Texas A&M University
TBL
turbulent boundary layer
THERFAT
consortium in EU dealing with CFD
TNT
Kok’s k-ω model for turbulent/nonturbulent interfaces (Hellsten, 2004)
TPCF
two-phase critical flow
T/C
thermocouple
URANS
unsteady RANS
(U)RANS
see URANS
VOF
volume of fluid
VLES
very large eddy simulation
VR
virtual reactor (e.g., by CASL)
V & V
verification and validation
WALE
wall adapting local eddy
WG
working group
WGAMA
working group of OECD/NEA/CSNI
WMLES
wall-modeled LES
ZDES
zonal DES
Chapter foreword
Computational fluid dynamics (CFD) constitutes a self-standing complex technology;
see also the discussion in Chapters 1 and 2. CFD-related technology is a cross-cutting
subject for researches, development, and application in areas like chemistry,
aereonautics, aerospace, military, mechanics (noticeably, car industry), naval,
metereologics including climate and ocean. As such, a huge number of roadmaps
for development can be identified since the time when computer power became
suitable for performing CFD calculation, i.e., around the 1970s of past century.
Furthermore, dozens of textbooks and thousands of CFD-related papers can be found
in the literature.

<!-- page 733 (PDF 5) -->
Thus, a comprehensive state of the art, e.g., documenting CFD model
capabilities and perspectives is a prohibitive task, well beyond the scope for this
chapter.
The nuclear thermal hydraulics was not the origin or the main motivation for CFD.
However, CFD may be seen as the major area where researches and investments are
ongoing in nuclear thermal hydraulics. Namely, making reference to two-phase flows,
the CFD research resembles a building site with work in progress: a number of targets
have been achieved and, at the same time, new directions are identified for
development.
In addition, one may note that:
l
Fundamental or balance equations for CFD, typically identified as Navier-Stokes equations,
derive from principle of thermodynamics and mechanics in the same way as in the case of
system codes (see e.g., Chapters 5 and 11);
l
CFD analyses provide support for, or receive support from, system thermal hydraulics code
calculations for suitable application of the best estimate plus uncertainty (BEPU) approach
as discussed in Chapter 14.
l
CFD analyses are relevant for sectors in nuclear technology other than thermal hydraulics.
Within the area of nuclear thermal hydraulics, large efforts have been made by OECD/
NEA/CSNI, as testified by the CFD4NRS series of Workshops:
(1) CFD Codes for Application to Nuclear Reactor Safety (CFD4NRS), Garching, Sept. 2006,
NEA/CSNI/R(2007)3 to be found in NEA website.
(2) Experiments and CFD Code Application to Nuclear Reactor Safety (XCFD4NRS),
Grenoble, Sept. 2008, NEA/CSNI/R(2009)12, to be found in NEA website.
(3) CFD for Nuclear Reactor Safety Applications (CFD4NRS-3), Bethesda, Sept. 2010, NEA/
CSNI/R(2011)14 to be found in NEA website.
(4) CFD for Nuclear Reactor Safety Applications (CFD4NRS-4), Daejeon, Sept. 2012,
NEA/CSNI/R(2014)4, to be found in NEA website.
(5) CFD for Nuclear Reactor Safety Applications (CFD4NRS-5), Z€urich, Sept. 2014, NEA/
CSNI/R(2016)1, to be found in NEA website.
(6) CFD for Nuclear Reactor Safety Applications (CFD4NRS-6), Cambridge, MA (hosted by
MIT), Sept. 2016, to be found in NEA website.
Additional OECD/NEA/CSNI key documents dealing with CFD are considered in the
text (e.g., Mahaffy et al., 2007a,b; OECD/NEA/CSNI/R(2014)3, 2014; Smith et al.,
2015; Bestion et al., 2016).
Then a CFD chapter in a modern nuclear thermal hydraulics book is essential; other
motivations for this chapter can be found in Chapter 1. However, this chapter shall be
seen as the work-in-progress building site (see the introductory statements in
Section 12.6 for more detail): topics and question marks are listed with an attempt
to provide an evaluation in some cases, rather than picturing a reality which risks
to become obsolete in a few years; this includes mentioning sectors in nuclear
technology, which have a connection with thermal hydraulics (e.g., fretting corrosion
). Furthermore, in a work-in-progress building site, the same component can be
found in different locations; similarly, in this chapter repetitions are not excluded even
though an attempt is made to look at the same topic from different viewpoints.
