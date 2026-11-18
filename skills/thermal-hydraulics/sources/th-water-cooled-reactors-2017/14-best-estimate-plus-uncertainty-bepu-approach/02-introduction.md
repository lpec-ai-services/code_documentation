# Introduction
<!-- source PDF pages 4-6 -->

<!-- page 908 (PDF 4) -->
Assessment (DSA) and Probabilistic Safety Assessment (PSA): DSA concepts are
part of other chapters of the book; so some fundamental PSA concepts are discussed
in this chapter.
14.1
Introduction
The words Best Estimate Plus Uncertainty, i.e., BEPU, since their origin, constituted
the attribute of a calculation performed by a SYS TH code. Three items provide a pedagogic
definition of BEPU:
(a) Best Estimate (BE) versus Conservative: The word Conservative has been always used in
engineering calculations to mask a lack of knowledge, or, in some cases to achieve resistance
capabilities and strengths of a system higher than what is strictly needed by the
design. The words “Best Estimate” do not imply the removal of the conservatism; rather
they impose the minimum conservatism consistent with the actual technological
knowledge.
(b) Limitations of system codes: Thermal-hydraulic system codes constitute the reference computational
tools for the application of BEPU. The features and the capabilities of those
codes are such to envisage an unavoidable error in any prediction. This is specifically true
for the application of codes to the transient analysis of accidents in NPPs.
(c) Uncertainty: The unavoidable errors expected from the application of computational tools
in thermal hydraulics (also referred above) need to be quantified to determine their acceptability
. Then, the word “uncertainty” appears: uncertainty is the prediction of the error
expected in NPP calculation results. Specific methods, or procedures or methodologies,
are needed and have been developed and qualified to determine the uncertainty; acceptability
or the error (i.e., of the uncertainty) is directly or indirectly linked with uncertainty
evaluation.
Historical appearance of the acronym BEPU occurred toward the end of 1990s; at that
time both the SYS TH codes and the uncertainty methods were thought mature enough
to allow practical applications. Unfortunately, the presumed achievement of maturity
for codes and uncertainty methods was not a common understanding at the time and is
still debated today within the scientific and the technological community engaged in
the nuclear reactor safety area.
Progresses in proving the capabilities of the codes continued during the current millennium
as well as in further demonstrating the qualification level of uncertainty
methods. In the same period institutions in the area of nuclear reactor safety issued
documents, i.e., IAEA (2002), IAEA (2010a), and USNRC (2005), opening or promoting
the application of BEPU, as further discussed in Section 14.2.1 and in Chapters
2 and 13, see also D’Auria et al. (2006). Practical applications of BEPU for the new
NPPs, even due to the very small number of new units entered in operation in the
period 2000–15, are restricted to two pioneering efforts:
l
Final Safety Analysis Report (FSAR), Chapter 15—Accident Analysis—large break loss of
coolant accident (LBLOCA), in Angra-2 NPP in Brazil (KWU-Siemens, 1997).
l
FSAR, Chapter 15—Accident Analysis—all transients where analytical support is needed,
in Atucha-2 NPP in Argentina, UNIPI-GRNSPG (2008), e.g., UNIPI-GRNSPG (2008).

<!-- page 909 (PDF 5) -->
BEPU also constituted the topic of international conferences like ANS (2000) and
ANS (2004), and of literature papers, e.g., Martin and Nutt (2011), D’Auria et al.
(2012a), and D’Auria et al. (2012b).
Notwithstanding the promising situation depicted in the previous statements,
BEPU never became a spread technology or an internationally recognized technology
at all, so far. This is the framework within which this chapter is prepared. For the benefit
of the reader, this statement must be supplemented by the consideration that
almost any topic discussed in the book is functional or essential for the implementation
of BEPU.
Therefore driving motivations, constraints, and objectives (see also below) for this
chapter are to collect important elements of BEPU and to avoid restating what already
presented in different chapters of the book.
Thus, BEPU constitutes the natural evolution of the initially adopted conservative
approach
and
one
potentially
productive
star
system
part
of
the
nuclear
thermal-hydraulics universe (see Chapter 1). Namely, BEPU is suitable to impact
nuclear reactor safety and to contribute to establish the safety and the acceptability
of NPP (D’Auria, 2012; see also Menzel et al., 2015 and Menzel et al., 2016). The
BEPU is also the only possible framework where the knowledge gained in the development
and the validation of SYS TH codes as well as in setting up and qualifying
uncertainty methods is exploited.

## 14.1.1 The licensing framework

Licensing (of nuclear plants) establishes the legal aspects of (nuclear) reactor safety.
Requirements including acceptance criteria and assumptions to perform analyses are
part of the licensing process. The licensing environment (ENV) is responsibility of
regulatory authorities in individual countries: it does not contain explicit or implicit
obstacles to the adoption of BEPU, e.g., see USNRC (2013) (continuously updated
NUREG-0800 document, or Standard Review Plan, or suggestions to the staff of regulators
to perform the review of accident analysis) for details.
While the originating words BE and uncertainty have a traceable/evident physical
and technological meaning, the acronym BEPU implies or fits with a licensing ENV
better than its originating words. This is because of the natural mission of the BEPU
approach to establish actual safety margins (SM) from NPP assessment activity, i.e.,
considering the errors and the approximations in current understanding, and in accordance
with requirements. “Independence-of-the-analysis,” or independence between
licensors and licensees in relation to the evaluation of NPP safety, constitutes by itself
a safety requirement and an intrinsic feature for BEPU analysis. Thus, in the common
understanding:
BEPU = connection between accident analysis & licensing:
The favorable picture for BEPU is again not consistent with the lack of, or the inadequate
, exploitation of BEPU strengths within the licensing ENV at the time when this
book is published.

<!-- page 910 (PDF 6) -->
## 14.1.2 Objective and structure

The objective of this chapter is to collect relevant elements and attributes of BEPU
avoiding emphasis in the description of those concepts which are part of other chapters
of the book. So, description of individual pieces of a puzzle is concerned rather than
attempting an organized array of the puzzle and providing an overall vision, not justifiable
by current progress and by the interest from nuclear technology stakeholders
(list of “nuclear technology stakeholder” is provided in the Chapter 2 making reference
to nuclear thermal hydraulics).
An outline of the connection between other chapters of the book and BEPU, or
what is discussed in relation to BEPU in this chapter, is given below:
l
Chapter 1 presents the universe of nuclear thermal hydraulics, which is the framework where
BEPU has been developed.
l
Chapter 2 deals with the history in nuclear thermal hydraulics. The appearance of the BEPU
acronym is identified together with the expected timeframe for its applications.
l
The definitions in Chapter 3 are consistent with the definitions needed for introducing the
BEPU concepts.
l
The nuclear technology needs, Chapter 4, including design and safety, shall be used to justify
the development and the application of the BEPU approach.
l
Chapters 5, 7, 8, 9, and 10 deal with selected models and selected equations, which are part of
a BE SYS TH code. The concerned codes, adopted for accident analysis, play a pivot role in
the application of a BEPU approach.
l
Chapter 6, dealing with expected phenomena within the Design Basis Accident (DBA) envelope
, is embedded into the series of Chapters 5–10: phenomena constitute an input for the
development of the SYS TH code. At the same time, identification and characterization of
phenomena are directly relevant to uncertainty evaluation and to the application of BEPU
approach.
l
The structure of SYS TH codes and of Computational Fluid Dynamics (CFD) codes,
Chapters 11 and 12, respectively, discuss computational tools needed for the BEPU
approach.
l
Verification and validation (V & V), scaling, and uncertainty methods are key elements for
the application of a BE SYS TH code within the BEPU approach and are discussed in
Chapter 13.
l
Chapter 15 deals with the description of accident scenarios. The related analyses are not necessarily
performed by pursuing a BEPU approach; however, the discussed ones are results
expected from the application of a BEPU process. Uncertainty evaluation is not (necessarily)
part of the analyses.
l
BE analyses are used to support the description of occurred accidents in NPP, Chapter 16.
Typically, no uncertainty evaluation is performed for those accidents and concerned situations
are beyond DBA types. Therefore little or no interest from the side of the BEPU
approach results from this chapter, unless some contribution for the validation of the
SYS TH codes.
The structure of this chapter is based upon the objective stated above and upon the
content of other chapters. Therefore,
l
“Bases and Background,” Chapter 2 in the following, aims at providing a picture of issues
from nuclear technology which may originate BEPU. Noticeably, various possible definitions
for BEPU are given in Section 14.2.3.
