# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — Conclusions and recommendations
<!-- source PDF pages 90-93 -->

<!-- page 818 (PDF 90) -->
The extrapolation to a reactor situation made by a single-phase CFD tool introduces
several new aspects and raises several questions:
l
How to guarantee that a CFD code can extrapolate from a reduced-scale validation experiment
to the full-scale application?
l
How to extrapolate nodalization from a reduced-scale validation experiment to the full-scale
application?
l
How to extrapolate:
–
from one fluid to another?
–
to a different value of the Re number and/or to a different value of any other
nondimensional number important in the physical processes taking place?
l
In any case, numerical simulation of scaled experiments has a given accuracy defined by the
error on some target parameters, and one should determine how the code error changes when
extrapolating to the reactor situation.
Therefore, scaling associated with a CFD application is part of the CFD code uncertainty
evaluation, and is a necessary preliminary step in this uncertainty evaluation.
Both scaling and uncertainty are closely related to the process of Validation and Verification
. The definition of a metric for the validation is also part of the issue.

## 12.13 Conclusions and recommendations

12.13.1
Conclusions of OECD/NEA/CSNI report (OECD/NEA/CSNI/
R(2014)3, 2014)
Hereafter conclusions are reported that have been agreed within a wide scientific
community (OECD/NEA/CSNI) in relation to the CFD technology. The reported
conclusions are (obviously) consistent with the text of the chapter. Minor editorial
changes are introduced, namely to adapt the original text to the content of this chapter.
The use of computational methods for performing safety analyses of reactor
systems has been established for nearly 40 years. Reliable codes have been developed
for analyzing the primary system in particular, and results from these analyses are
often used to support the safety assessment of nuclear power systems undertaken
by the regulatory authorities. Similarly, but to a lesser extent, programs have also been
written for containment and severe accident analyses. Such codes are based on
networks of 1D or even 0D cells. However, the flow in many reactor primary
components is essentially 3D in nature, as is natural circulation, mixing, and stratification
in containments. CFD has the potential to treat flows of this type and to handle
geometries of almost arbitrary complexity. Already, CFD has been successfully
applied to such flows, and to a limited extent has made up for a lack of applicable test
data in better quantifying safety margins. Consequently, CFD is expected to feature
more prominently in reactor safety analyses in the future.
The traditional approaches to nuclear reactor safety analysis, using system codes
for example, take advantage of the very large database of mass, momentum, and
energy exchange correlations that have been built into them. The correlations have

<!-- page 819 (PDF 91) -->
been formulated from essentially 1D special-effects experiments, and their range of
validity is well known, and (as far as possible) controlled internally within the numerical
algorithms. Herein lays the trustworthiness of the numerical predictions of such
codes. Analogous databases for 3D flows are very sparse by comparison, and the issue
of the trust and reliability of CFD codes for use in NRS applications has therefore to be
addressed before the use of CFD can be considered as trustworthy.
A list of NRS problems for which it is considered CFD analysis is required or its
application is expected to result in positive benefits in terms of better understanding
and improved safety margins is provided in OECD/NEA/CSNI (2014) and also
discussed in this chapter. The list contains safety issues of relevance to fluid flows
in the core, primary circuit and containment, both under normal and off-normal operating
conditions including accident sequences. The list contains both single-phase and
two-phase safety items, though in the latter case reference is made to the document
dealing with the Extension of CFD Codes to Two-Phase Flow Nuclear Reactor Safety
Problems, Mahaffy et al. (2007a,b) and OECD/NEA/CSNI (2014) (see also Bestion
et al., 2016).
Recognizing that CFD is already an established technology outside of the nuclear
community, a list of the existing assessment bases from other application areas has
also been included in OECD/NEA/CSNI (2014) and their relevance to NRS issues
discussed in the same report. It is shown that these databases are principally of two
types: those concerned with aspects of trustworthiness of CFD code predictions in
general industrial applications (ERCOFTAC, QNET-CFD, FLOWNET), and those
focused on specialized topics (MARNET, NPARC, AIAA). The usefulness and
relevance of these databases to NRS have been assessed. In addition, most CFD codes
currently being used for NRS analysis have their own, custom-built assessment bases,
the data being provided from both within and external to the nuclear community.
Application of CFD to NRS problems can benefit indirectly from these databases.
The continuing efforts to extend them can lead to a well-maintained NRS-specific
database, a valuable addition.
Descriptions of the existing CFD assessment bases have been established specifically
within the nuclear domain and their usefulness discussed. Typical examples
are experiments devoted to the boron dilution and in-vessel mixing issues (ISP-43,
ROCOM, Vattenfall 1/5th Scale Benchmark, UPTF TRAM C3), pressurized thermal
shock (UPTF TRAM C2), and thermal fatigue in pipes (THERFAT, Forsmarks), all of
which have already been the subject of benchmarking activities. The EU Framework
Programs, such as ASTAR, ECORA, EUBORA, FLOWMIX-R and ASCHLIM, have
also provided direct NRS-specific data and/or have each focused on relevant aspects
of the CFD modeling.
The technology gaps which need to be closed to make CFD a more trustworthy
analytical tool have also been identified in OECD/NEA/CSNI (2014). These include,
for example, lack of a proper uncertainty methodology; limitations in the range of
application of turbulence models, for example in stratified and buoyant flows;
coupling of CFD with neutronics and system codes, needed to keep simulations to
a manageable size; and generally computer power limitations in simulating long
transients. Particular application areas for which CFD simulations need to be

<!-- page 820 (PDF 92) -->
improved are in stratified flows, containment modeling, aerosol transport and deposition
, and liquid-metal heat transfer. In other areas, such as in-vessel mixing, the
models may be adequate but grid resolution is inadequate due to the current lack
of machine power, a situation that will certainly improve with time.
The computational overhead of performing CFD simulations in comparison with
system code transient computations may still be regarded as a definite limitation of
the potential for directly using CFD in licensing procedures, even for single-phase
applications for which the underlying models are well established. The uncertainty
quantification methodology for system codes generally requires 50–100 computations
to be carried out, and the statistical method of Latin Hypercube Sampling (LHS) is
becoming widespread in order to optimize the efficiency of the random parameter
sampling. This cannot, at the present time, be mirrored with CFD, and until it can,
a different methodology needs to be established. However, in the spirit of BPGs, at
least mesh independency must be demonstrated, and some limited study of sensitivity
to input parameters should be attempted. The issue of access to the source code of CFD
software, particularly in regard to the commercial codes, will also have to be
addressed before CFD is accepted as an analysis tool by the regulatory bodies.
There is a distinct lack of quality validation data for aerosol transport, even though
the phenomenon was identified as a key process in containment modeling, and one
that can only be treated mechanistically by the use of CFD. The experiments carried
out at the PHEBUS facility as part of the EU 5th Framework Programme PHEBEN
produced only data of an integral nature, and as such very limited in regard to
validating CFD models. Comprehensive, local aerosol deposition data appear only
to be available for pipes (straight and elbowed), and for some nonnuclear applications,
such as atmospheric pollution. This is one key area where future CFD assessment
needs to be focused.
Important new information has been provided by the material presented at the
CFD4NRS series of Workshops (here listed in the Foreword), in which numerical
simulations with a strong emphasis on validation were particularly encouraged, and
the reporting of experiments which provided high-quality data suitable for CFD
validation. Participation in the workshops has enabled a list of existing databases
to be assembled of possible candidates for future benchmarking activities for:
(1) primary circuits,
(2) core-flow regions,
(3) containments,
in relation to which data of the type needed for CFD benchmarking already exists or
are likely to be available in the near future.
This updated document represents a continuing process in establishing an assessment
database for the application of CFD to NRS problems, but in many places
reflects the time and manpower restriction for issuing the concerned OECD/NEA/
CSNI report (this also applies to this chapter), and considerable further work still
needs to be done in terms of both presentation and technical content. Sections of
the OECD/NEA/CSNI report, as well as of this chapter, remain unbalanced in terms
of detail, reflecting not only the subjective inputs of the authors but also whether the

<!-- page 821 (PDF 93) -->
safety issue being addressed is of a country-specific nature or of more common
concern. Part of the recommended obligation to regularly update the provided information
shall include an attempt to equilibrate the information level. In addition,
similar information appears in different sections of the report and of the chapter. This
was done to avoid excessive page turning or scrolling, but gives the OECD/NEA/
CSNI document (and this chapter) an appearance of disjointedness if read in a
continuous manner.
CFD remains a very dynamic technology, and with its increasing use within the
nuclear domain there will be ever greater demands to document current capabilities
and prove their trustworthiness by means of validation exercises. It is therefore
expected that any existing list of specific assessment databases will soon require
further updating. In order to prevent the important information assembled in the
OECD/NEA/CSNI document and in this chapter from becoming obsolete, the following
recommendations are made:
l
Extend the process of consolidating the information contained here through continuous
updating. This process is necessary to ensure that the NRS assessment database is readily
accessible to all, and as dynamic and mobile as the CFD technology itself.
l
Set up a forum for numerical analysts and experimentalists to exchange information in the
field of NRS-related activities relevant to CFD validation, e.g., like the one provided by the
series of CFD4NRS workshops (see e.g., Foreword to this chapter).
l
New blind CFD benchmarking exercises should be defined, both to encourage the release of
previously restricted CFD-grade data from experiments, to test the skills of the CFD
practitioners, and perhaps persuade the software developers to improve their models, where
these have proved lacking. To this end, it is encouraging to note that representatives of the
large commercial software houses actively participate in the benchmarks.
Finally, it seems worthwhile to extend the alarm given in the following statement of
OECD/NEA/CSNI (2014) report to this chapter. The Special CFD Group, which was
first set up in 2007 and initially comprised of the chairmen of the original three Writing
Groups (WG) together with the NEA secretariat, can continue to act as the central
organizing bodies for the above activities provided new members are appointed to
replace the “old guard.” The timescale for this process is (i) overdue for the WG1
chairman (J. H. Mahaffy reached pensionable age in 2009); (ii) imminent for the
WG2 chairman (B. L. Smith reached pensionable age in 2012); and within sight
for the WG3 chairman (D. Bestion will reach pensionable age in 2017). It is important
to ensure a smooth transition to a new group membership before the existing expertise
is lost.

### 12.13.2 Final-summary remarks

The complex CFD subject is discussed in this, work-in-progress type (see the
Chapter foreword), chapter: question marks and identification of critical issues are
part of the text; however, an attempt is made to clarify some important topics in
relation to nuclear thermal hydraulics. Any reader who has completed the reading
of the chapter should not believe he has acquired the understanding of the CFD
