# Introduction
<!-- source PDF pages 6-10 -->

<!-- page 956 (PDF 6) -->
Very many acronyms are used throughout the text (see also Section 15.5.1). In a
number of cases, the acronym is not identified the first time it is used (this is mostly
the case of tables and figures). Although an attempt is made to use acronyms
recognized in the literature, the reader is recommended to become familiar with
the acronyms listed at the end of the chapter.
The present chapter constitutes the tip of the virtual pyramid of knowledge developed
in nuclear thermal-hydraulics. Therefore all chapters of the book have some connection
with the present one. This is specifically true for Chapter 6 where phenomena
are characterized and for Chapter 11 where the features of system codes (i.e., needed
to predict accident scenarios) are discussed. The bases for code application, noticeably
V&V, scaling, and uncertainty discussed in Chapter 13 are also important here. However
, uncertainty of predictions for the transient scenarios presented in this chapter is
not under consideration.
15.1
Introduction
The key motivation for nuclear thermal-hydraulics is the design of nuclear reactors
and the safety demonstration. Water cooled reactors are of concern in the book.
Thermal-hydraulic design of nuclear reactors implies, or has implied, for
thermal-hydraulics support (to other disciplines) in
(a) selecting the components, e.g., core, pumps, steam generators, turbine, condenser, needed
to transform the fission power into electrical power;
(b) fixing the layout of the whole system, e.g., mutual position between core (heat source) and
steam generator (heat sink), pressurizer location also to allow for spray line, pump location
to maximize the Net Positive Suction Head (NPSH) from the loop, condenser location to
optimize the thermal efficiency;
(c) searching for the optimum configuration of individual components, e.g., the core constituted
by thin fuel pins, the helicoidally shaped steam separators to facilitate steam liquid
separation by inertia forces;
(d) fixing the normal operational parameters, like working pressure, maximum and average
linear heat flux for the fuel pins in the core, pressure drops, level in the pressurizer, in
the down-comer of BWR ad of steam generators in PWR;
(e) designing each component, e.g., the fuel pin, the number of tubes in steam generators, the
size of hot and cold legs, the flow paths inside the pressure vessels, as well as the size and
the number so headers (in pressure tubes reactor types like CANDU and RBMK); and
(f) determining expected loads, e.g., pressure and pressure drops including pressure wave
propagation originated by opening/closure of valves, thermal stresses originated by
cooling/heating rates and thermal fatigue.
Safety demonstration of nuclear reactors implies, among the other things:
(g) the calculation of the transient performance of reactors;
(h) namely, the proof of suitable design/construction for emergency core cooling systems
(ECCS), e.g., the volume and the number of accumulators, and, more in general of
engineered safety features (ESF), e.g., the pressure set point for the operation of steam relief
valves (SRV), the closure time for main steam isolation valves (MSIV);
(i) the design of emergency operating procedure (EOP) and the accident management
procedure (AMP);
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 957 (PDF 7) -->
(j) an interaction with safety and licensing processes to fix requirements and procedures for the
related analyses, e.g., list of design basis accidents (DBA), acceptable probability for failures
and demonstration that consequences of failure are within the acceptability domain.
The above list of thermal-hydraulic applications, incomplete and/or not comprehensive
, may be taken as another demonstration, or even one origin, for the universe in
nuclear thermal-hydraulics introduced in the Chapter 1. The impossibility to describe
all applications of nuclear thermal-hydraulics in one chapter (even though in one
book) is also a consequence from the list.
The complexity of some topics, namely those which require the analysis of accident
performances of nuclear reactors, imposed the development of system
thermal-hydraulic (SYS TH) codes as outlined, for instance, in Chapters 2 and 10.
The scope for the present chapter is restricted to the transient analyses in Light
Water Reactors (LWR), i.e., BWR and PWR including evolutionary and similar
design like EPR, AP1000, ABWR, AP1400, and VVER, partly accomplishing the
content of item (g), as listed previously; in a few cases transient analyses of CANDU,
RBMK, and PHWR (Pressurized Heavy Water Reactor equipped with vertical channels
core and pressure vessel) are presented. The scope can be further specified as
“addressing the capabilities of the SYS TH codes (discussed in Chapter 11), constituting
a cross-connection among accident scenarios (DBA area), and results of those
codes and phenomena (discussed in Chapter 6, see also Section 15.1.1).” The consideration
of Beyond DBA (BDBA) conditions is within the scope for the chapter till the
situation where irreversible degradation of core or the loss of geometric integrity
occurs. Therefore, proofs of qualification of the discussed SYS TH code calculated
results and the evaluation of uncertainty of calculations are outside the scope for
the present chapter.

## 15.1.1 The connection with phenomena

Thermal-hydraulic phenomena expected to occur in LWR (and VVER) in DBA conditions
have been classified in the documents OECD/NEA/CSNI (1993) and OECD/
NEA/CSNI (1996a), respectively, related to separate effect test facilities (SETF) and
integral test facilities (ITF), see also OECD/NEA/CSNI (2001), related to VVER (as
also discussed Chapter 2). Containment-related phenomena can be found in the report
OECD/NEA/CSNI (1999). So-called computer code validation matrices (CCVM)
have been created based on the correspondence between phenomena and experiments.
Therefore, the concerned phenomena have been the object of experimental investigations
and are considered in various reports, papers, or textbooks, see for instance, the
report (USNRC, 1988), the CSNI documents dealing with International Standard
Problems (ISP) (e.g., OECD/NEA/CSNI-ISP, 2000, and more recently OECD/
NEA/CSNI-ISP-50, 2012), the textbook (Levy, 1999), and the papers (like D’Auria
and Galassi, 1990a; D’Auria and Ingegneri, 1997; Del Nevo et al., 2012a,b;
Mascari et al., 2012; Reventos et al., 2012).
The idea here is to create a correspondence between thermal-hydraulic phenomena,
variables to characterize the phenomena, and results of code calculations related to
accident analyses.

<!-- page 958 (PDF 8) -->
## 15.1.2 Objective and structure

The objective for this chapter is to close a logical circle, the starting point of the circle
being the definitions and the fundamental concepts given in Chapter 3. These are
followed by needs in nuclear reactor design and safety (Chapter 4), expected
phenomena for DBA in LWR and advanced water cooled designs (Chapter 6), equations
and models (Chapters 5, 7–10), and by computational tools which make use of
the equations and models (e.g., Chapters 11 and 12 where applicable). In this connection
Chapters 1 and 2 provide a general framework suitable for the understanding of
the nuclear thermal-hydraulics discipline; the remaining two chapters discuss the conditions
for the applicability of those codes to the accident analysis, noticeably, the
needs for qualification and the need to supplement the calculation results by uncertainty
(Chapter 13), and the connection with the licensing process (Chapter 14).
Additional objective is to provide essential information to the reader in relation to
the links among phenomena, the predicted accident evolutions in nuclear reactors and
the variables, or time trends or parameters, which are the direct outcomes of SYS TH
code calculations and are suitable for the characterization of phenomena.
Although a complex process is pursued to establish those links, it seems worthwhile
to emphasize that only a narrow sector of system thermal-hydraulics is involved
in this chapter. This is the item (g) from the list above (i.e., safety analysis), supplemented
by one noticeable example from the item (d) (i.e., design analysis) (e.g.,
see Section 15.4.12.1).
Four main tables (plus one) have been created as bases for the document:
l
Table 15.1 deals with a minimum-reasonable list of accidents or transient scenarios resulting
from NPP calculations performed by system thermal-hydraulic codes.
Table 15.1 List of NPP accident scenarios calculated by system
thermal-hydraulics codes
No
Section
Identification
Type
Reactor
Notes and references
15.4.10
ATWS-1
BDBA
ABWR
Ferng et al. (2010)
ATWS-2
BDBA
BWR
Munoz-Cobo et al.
(2014)
ATWS-3
BDBA
PWR
Kliem et al. (2009)
and Chen et al. (2014)
15.4.12.8
BORON-D
DBA
PWR
Jimenez et al. (2015)
and Graffard and
Goux (2006)
15.4.12.1
CHF
N/A
Fundamental study for
core design, Visentini
et al. (2014)
15.4.12.2
CONT-1
AP1000
Hung et al. (2015)
CONT-2
ABWR
Chen and Yuann
(2015)
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 959 (PDF 9) -->
Table 15.1 Continued
No
Section
Identification
Type
Reactor
Notes and references
15.4.9
CRE
DBA
PWR
Part of the RIA class,
Todorova and Ivanov
(2003)
15.4.12.6
FCB
DBA
RBMK
D’Auria et al. (2005)
15.4.8
FWLB
APR1400
Actuation of passive
system, Bae et al.
(2014)
15.4.2 and
15.4.12.12
HEBR-1
DBA
CANDU
Positive reactivity
insertion and fuel
behavior, Rouben
(1997) and Horhoianu
et al. (1998)
15.4.2 and
15.4.11
HEBR+AMP
BDBA
CANDU
Mehedinteanu (2009)
15.4.2
HEBR-2
DBA
RBMK
D’Auria et al. (2005)
LBLOCA-1
DBA
AP1000
Queral et al. (2015)
LBLOCA-2
DBA
BWR
Recirculation line
break, Beckmeyer
et al. (1979)
LBLOCA-3
EPR
Arkoma et al. (2015)
LBLOCA-4
DBA
PHWR
Positive reactivity
insertion, D’Auria
et al. (2008a)
LBLOCA-5
DBA
PWR
Double-Ended
Guillotine Break
(DEGB), OECD/
NEA/CSNI (2009),
and D’Auria and
Galassi (2001)
15.4.12.9
LCC/SW
BDBA
PWR
Connection with PSA,
OECD/NEA/CSNI
(2011)
LOFA
AOO
EPR
AREVA (2014)
15.4.4
LOFW
DBA
PWR
See also LOFA, SBO,
and LOOSP, OECD/
NEA/CSNI (2011)
15.4.6
LOOSP
BDBA
VVER,
BWR,
CANDU
Borisov et al. (2013),
see Fukushima events
in Chapter 16, Tong
et al. (2014) and
D’Auria et al. (2006)
15.4.2
MBLOCA
DBA
PWR
Also identified as
IBLOCA, OECD/
NEA/CSNI (2011)
Continued

<!-- page 960 (PDF 10) -->
Table 15.1 Continued
No
Section
Identification
Type
Reactor
Notes and references
15.4.12.9
MCP-TRIP
AOO
VVER
Groudev and
Stefanova (2006), see
also LOFA
15.4.12.7
MPTR
DBA
RBMK
D’Auria et al. (2005)
15.4.8
MSLB-1
DBA
PWR
Jeong et al. (2006)
MSLB-2
DBA
PWR-O
In PWR equipped with
OTSG, D’Auria et al.
(2003a)
15.4.12.3
MSLB-PTS
PWR
PTS focus, Jang
(2007)
15.4.12.5
MSLB
+SGTR*
BDBA
PWR
* and multiple SGTR
USNRC (1998), Seul
et al. (2003), and
Jimenez et al. (2013)
15.4.12.4
NC
DBA
PWR
Flow map including
PWR-O, PWR-V,
CANDU, etc., and
experiments, IAEA
(2005a) and Cherubini
et al. (2008a)
15.4.7
PRISE+AMP
BDBA
VVER
IAEA (2009b) and
D’Auria et al. (2006)
–
15.4.9
RIA
See CRE. Qualitative overview of RIA in
Section 15.4.9
15.4.5
SBO-1
DBA
APR1400
Supported by
experiments, Yu et al.
(2013)
SBO-2
DBA
PWR
Bittan (2015)
15.4.5 and
15.4.11
SBO+AMP
BDBA
VVER
D’Auria et al. (2006)
15.4.3
SBLOCA-1
DBA
AP1000
Yang et al. (2012a,b)
SBLOCA-2
DBA
APR1400
Focusing on loop seal
clearing, Kim and
Choi (2014)
SBLOCA-3
(B)
DBA
PWR-O,
EPR
Bandini and De Rosa
(2014), Freixa and
Manera (2011)
SBLOCA-4
DBA
BWR
Analytis and
Coddington (2002)
15.4.12.3
SBLOCA-PTS
PWR
PTS focus, Jang
(2007)
15.4.3 and
15.4.11
SBLOCA
+AMP
BDBA
VVER
D’Auria et al. (2006)
15.4.7
SGTR
DBA
PWR
OECD/NEA/CSNI
(1988)
Thermal Hydraulics in Water-Cooled Nuclear Reactors
