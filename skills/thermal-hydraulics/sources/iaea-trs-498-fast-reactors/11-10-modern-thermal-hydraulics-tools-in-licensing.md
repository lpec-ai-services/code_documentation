# 10. MODERN THERMAL HYDRAULICS TOOLS IN LICENSING
<!-- source PDF pages 76-80 -->

<!-- page 64 (PDF 76) -->
# 10. MODERN THERMAL HYDRAULICS TOOLS IN LICENSING

## 10.1. SUMMARY

This section discusses the link between experiments, modelling and
simulation (tools) and the licensing process. It is generally agreed that, although
most people tend to think of computational tools, the interaction between
experiments and modelling and simulation is very important for understanding
physical phenomena and for the validation of modelling and simulation tools.
Since modelling and simulation tools are constantly developing in capabilities
and are increasingly able to reveal small details, this drives innovations in
instrumentation and measurement techniques.
A general trend is seen in the increasing use of advanced tools in the design
process. However, it is important to realize that the design process, although
related, is different from the actual licensing process. The design process will
allow the use of advanced tools more easily than the licensing process. In both
cases, however, the user of the tools will have to demonstrate that the tool is
adequate for the purpose for which it is being used and that both the models
and the tools are qualified. Nevertheless, the level of qualification in the design
process and the licensing process may be different.
Despite the fact that increasingly detailed codes like CFD are being used
in the design process, it is important to emphasize that, apart from STH codes,
which are the backbone of safety analyses for licensing, subchannel codes also
play an important role in core cooling analyses. They provide more detail to the
user than STH codes but need much less computational effort than CFD. On top
of that, subchannel codes have a longer history than CFD codes and are therefore
more likely to be accepted by regulatory bodies for safety analyses.
Finally, the licensing framework worldwide is tailored towards large
scale LWRs, which use water as the main coolant. The advanced reactors under
consideration in this publication all deploy coolants that are very different from
water, which poses serious challenges to the licensing process. Sam et al. [199]
describe two generic regulatory framework approaches. The first one, used in
most countries, is the prescriptive based approach. The prescriptive based
approach is rigid and typically contains detailed and measurable requirements
for compliance. This is an efficient licensing approach for standardized reactor
technology, such as large scale nuclear reactors [200]. However, this approach
is likely to lead to overregulation for advanced nuclear technology demonstrator
projects. The second approach is the goal setting approach. This licensing method

<!-- page 65 (PDF 77) -->
is technology neutral and risk informed. It is therefore better placed for dealing
with advanced and innovative features where uncertainties have to be addressed
and supplementary measures or margins may be needed. Instead of predefined
norms for demonstrators, the regulators use the principles of a graded approach
to establish overall performance goals in the form of risk targets.

## 10.2. PHENOMENA REQUIRING MODERN TOOLS

Since the dawn of nuclear power, correlations and STH simulation tools have
been extensively used in the licensing process of nuclear reactors. It is expected
that such tools will remain the backbone of the licensing process. However, it
may also be expected that modern tools will be needed in the licensing process
for certain phenomena. In general, it is noted that CFD tools will be necessary
to fill in gaps in the capabilities of STH codes, especially when 3-D phenomena
are involved. Although STH codes can often be employed in a conservative way,
thereby avoiding the need for 3-D tools, in some cases, more advanced (3-D)
tools cannot’ be avoided. As such, as mentioned before, this will also demand
developments in experiments, measurement techniques and instrumentation for
understanding and validating the physical phenomena involved.
The following phenomena can be identified in particular (but not
exclusively) as requiring modern tools:
— Coolant behaviour in large plena
Particularly large plena, like the hot or cold pools in advanced fast reactor
designs, are known to be difficult to simulate accurately with STH tools
because of the 3-D flow patterns that can and will occur. For example,
these 3-D flow phenomena can lead to thermal stratification, which is hard
to predict in STH tools. Jet behaviour, for instance at the core outlet, can
be even more challenging. However, high cycle thermal fatigue on internal
structures and the reactor vessel wall may also occur as a result of jets
entering a pool.
— The interplay between fuel assemblies and the inter-wrapper flow
The inter-wrapper flow is known to contribute to the cooling of a reactor
under accident conditions. Good understanding and accurate modelling of
the inter-wrapper flow may allow for the removal of conservatisms in the
reactor design, possibly leading to a more economical design.
— Flows with internal heat production
Reactor designs in which the fuel is dissolved in the coolant will include
heat production in the coolant as a result of the nuclear and decay heat
released by the dissolved fuel. Since this is a very peculiar feature that did

<!-- page 66 (PDF 78) -->
not need attention in the case of the widely used LWRs, existing safety tools
need to be adapted or new safety tools need to be developed; in both cases,
the tools need to be validated. This validation is particularly challenging.
— Multiphase and chemistry effects of advanced coolants
Advanced coolants may behave very differently from water when
multiphase (fluid–particle or fluid–gas) conditions are considered because
of the different property ratios (e.g. density, viscosity) involved. Even
though developed approaches may be used in some cases, validation of
these approaches is needed. Chemistry effects, on the other hand, can be
expected to be completely different and will need separate models and/or
parameters, including validation.

## 10.3. EXPERIMENTAL VALIDATION: SEPARATE VERSUS INTEGRAL

EFFECT TESTS
The licensing approach for any type of reactor demands a combination
of separate and integral effect tests. Where SETs are needed to validate new
phenomena and components, the inherent non-linearities in thermal hydraulics
also lead to a requirement for integral type experiments, in which combinations
of two (or more) phenomena are studied. The challenge will be to construct
the integral effect tests in such a way that they validate new phenomena and
components integrated into a generic system, rather than in a specific design.
As mentioned before, experiments are crucial for the development and
validation of safety analysis tools. However, it is important to realize that some
phenomena or components are difficult, or even impossible, to measure. In such
cases, a combination of multiple experiments and additional high resolution
simulations may provide a solution. It is also important not to forget that
experiments have uncertainties and that these need to be identified.

## 10.4. CODE ACCEPTANCE

When a licensee decides to employ a certain tool, the first to accept the
results of that tool is the licensee itself. This entails an initial level of (internal)
quality control. However, the next step is the acceptance of the results of the tool
by the regulatory body. It is important to consider the following:
— Deployment of new tools
In this respect, special challenges can be found in the use of:

<!-- page 67 (PDF 79) -->
•
In-house tools
Although in-house developed codes provide flexibility and improve
understanding of the numerical code, the challenge is to have these
codes accepted by the regulator for licensing. Typically, it is expected
that the regulator will seek to obtain a thorough understanding of the
code, since, as it is an in-house code, the regulator will have much
less knowledge about it than the licensee. It is likely that the regulator
will ask questions to improve their understanding of the code and will
want to see a thorough validation case.
•
Open source tools
Since commercial codes can be very expensive and have limitations
in their use with respect to licensing, many companies are exploring
open source tools for design and preferably also for licensing.
Regulators are aware of this development and are considering how
to accept open source tools. It is expected that a strong validation
case will be needed, along with proof that the code version can be
used for the application at hand. It may be worth considering putting
common effort into the qualification of open source codes to regulator
standards.
In both cases, the regulator will expect the licensee to provide a complete
validation database covering the domain in which the code will be used.
The effort involved in producing this database is significant. It can be
shared (for open source code) or partially shouldered by the provider (for
commercial code).
— Definition of best practice guidelines
It is highly advised, especially with complex codes, to develop best practice
guidelines in order to avoid or minimize the user effect  in code use. The
international community can play an important role in this respect.
— Knowledge and experience at the regulator
Whatever tools are used in the licensing process, the acceptance of the
results of such tools will depend on the knowledge and experience available
at the regulator. Therefore, education and training of the regulatory
workforce in the use and interpretation of the results of the code at hand is
very important.
— Benchmarks
In order to prove that a code is suited to a certain analysis, benchmarking
of the code against other codes or experimental results is necessary. When
such benchmarks are considered, it will be helpful if the regulator or its
technical support organization participates in this benchmark and thus is
directly informed of the capabilities of the code under consideration, rather

<!-- page 68 (PDF 80) -->
than being indirectly informed only after the publication of the summary of
the benchmark results.
— Licensing framework
•
Modernization
It was previously mentioned that the introduction of advanced reactors
will require modernization of the licensing framework. However, in
addition to that, the application of modern simulation tools in the
design and licensing process demands modernization of the licensing
framework in a totally different way.
•
Variation among countries
There is significant variation in the licensing framework from country
to country. Harmonization of these licensing frameworks is often
discussed and pursued, but the realization of such harmonization is
a major challenge. Sam et al. [199] mention that the main roadblock
to converging towards a harmonized regulatory system is the
strong incentive for individual countries to protect their regulatory
independence and national sovereignty in their regulatory practices.
Harmonization becomes especially important when smaller designs
are being considered.
— Validation of instruments and experimental tools
In addition to validating analytical and numerical tools, instrumental and
experimental tool validation is also crucial.

## 10.5. UNCERTAINTIES

When submitting safety analyses in a licensing process, addressing
uncertainties is an important task, but it is not always easy or straightforward.
On the one hand, there are experimental uncertainties related to, among other
factors, geometric simplifications, boundary condition assumptions, geometric
tolerances, instrumentation positions and measurement methods. On the other
hand, analytical and numerical methods and codes involve uncertainties such as
model simplifications, properties, boundary condition assumptions, and so on.
Model uncertainties, in particular, tend to rely on expert judgement. For
LWRs, a consensus on these uncertainties has emerged progressively, thanks
in large part to a series of international benchmarks [201]: UMS (1995–1997),
BEMUSE (2004–2010), PREMIUM (2012–2015) and SAPIUM (2017–2019).
Building a similar consensus for advanced reactor models will probably need a
similar approach.
Methodologies to perform uncertainty analysis have been under
investigation for a long time. Using brute force, hundreds or thousands of
