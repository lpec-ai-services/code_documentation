# Current uncertainty methods — International validation of uncertainty methods — Post-BEMUSE REflood Model Input Uncertainty Methods Programme
<!-- source PDF pages 64-66 -->

<!-- page 894 (PDF 64) -->
assumptions must be well justified. This has been the experience from the UMS
Study already. An important basis to determine code model uncertainties is the
experience from code validation. This is mainly provided by experts performing
the validation. Appropriate experimental data are needed. More effort, specific
procedures, and judgment should be focused on the determination of input
uncertainties.
This last point has been an issue of recommendation for further work. Especially,
the method used to select and quantify computer code model uncertainties and
compare their effects on the uncertainty of the results are studied in a common international
investigation using different computer codes, the CSNI Post-BEMUSE
REflood Model Input Uncertainty Methods (PREMIUM) programme (CSNI, 2016a).

### 13.4.3.3 Post-BEMUSE REflood Model Input Uncertainty Methods Programme

The objective of the PREMIUM exercise was to find a better means than coarse expert
judgment in order to quantify the uncertainty ranges and distributions of relevant
model input parameters. The PREMIUM benchmark application was focused on
determination of uncertainties of the physical models involved in the prediction of
the core reflood, which is an important phase during a loss of coolant-accident
(LOCA) scenario (CSNI, 2016a). PREMIUM generally addresses the solution of
inverse problems in modeling and simulation, where model input parameters are
estimated including their uncertainty from values of model output magnitudes. The
solution of the inverse problem includes the processes of model calibration (adapting
a model by a correction) and model uncertainty quantification. PREMIUM is focused
on the last topic. PREMIUM has been organized in five consecutive phases.
In Phase I (coordinated by UPC and CSN, Spain), the participants presented and
described their methods of model uncertainty quantification. Two methods were
offered to the participants (including assistance for their application): CIRC⟨E, developed
by CEA, France and FFTBM, developed by University of Pisa, Italy. Several
participants used these methods, and others used their own quantification methods,
like iteration of several input model parameters to bound relevant experimental
parameters. The features of the two series of reflood experiments FEBA and PERI-
CLES were also described in this phase.
In Phase II (coordinated by University of Pisa, Italy) participants identified
influential code input parameters, from the point of view of reflood, and made a
preliminary quantification of their variation range. Phase II coordinators proposed
a methodology for the identification of influential parameters, based on a set of
quantitative criteria, and presented a preliminary list of possibly influential parameters
on reflood. Some participants modified the proposed criteria or established
their own criteria.
Each participant obtained a list of influential model parameters to be quantified,
assigning ranges of variation to the parameters, based on sensitivity calculations of
test 216 of FEBA, and using as responses cladding temperatures and quench front
propagation. The influential model parameters obtained by the participants were

<!-- page 895 (PDF 65) -->
typically wall and interfacial heat transfer coefficients, interfacial friction coefficient,
heat transfer enhancement at the quench front, and droplet diameter.
In Phase III (coordinated by GRS, Germany), the uncertainty of influential input
parameters (identified in Phase II) was quantified. Participants obtained uncertainties
in the form of ranges or probability distributions. The uncertainties obtained depend
strongly on the quantification method. Additionally, they depend on:
–
The responses used for quantification of input uncertainties
–
The set of input parameters being quantified
–
The TH code and the specific model being used
The dependency on the quantification method was stronger than on the used TH code.
The results exhibited a significant user effect and a large variability and discrepancy
among participants. In some cases, extremely small uncertainty ranges were found for
model parameters, which are physically nonrealistic. They were obtained by participants
who performed a calibration of the code models, additionally to the uncertainty
quantification, i.e., by a majority of users of the CIRC⟨E method.
In Phase IV (coordinated by CEA and IRSN, France), uncertainties calculated for
model parameters in Phase III were propagated through the code simulation for the
selected tests of FEBA and PERICLES experiments and compared to the experimental
results. The objective was to confirm (using FEBA) and validate (using PERICLES)
the model uncertainties.
For FEBA tests, most of participants obtained by propagation, uncertainty bands
enveloping the experimental values. The width of the bands varied significantly
among the participants. The uncertainty bands were highly influenced by the
responses used in the quantification and the selected input parameters.
For PERICLES tests, the results were less satisfactory. Considering all the contributions
, the fraction of experimental values, which were enveloped by uncertainty
bands, was clearly lower than for FEBA, and far from the expected value. Therefore,
the direct extrapolation of the model uncertainties calculated for FEBA to PERICLES
gave poor results. This result can be explained in terms of significant differences
between the two facilities and the analyzed tests.
The quality of the nominal calculation was found important in the final results of
the propagation calculations. A good nominal calculation facilitated enveloping the
experimental data by the calculated uncertainty bands. Reasons for deviations
between nominal calculation and experimental value should be clarified.
The results were highly dependent on the parameter uncertainties derived in
Phase III, and therefore were strongly related to the quantification method, rather than
to the TH code.
Quantification methods may have the option of performing calibration, as well as
quantification, of the models. Applying such option means a calibration of the code
models. Some participants in Phase IV compared results with and without the calibration
option for the FEBA application, concluding that results improve for PERICLES
when there is no calibration. This outcome is completely in line with the validation
strategy of “best estimate” TH codes to include several experiments of one test
facility, and of differently scaled test facilities.

<!-- page 896 (PDF 66) -->
As in Phase III, a user effect was observed in Phase IV results. Participants using
the same method and the same version of the same system code obtained uncertainty
bands, which were significantly different. Differences in the input deck, influential on
the nominal calculations, and in the choice of input parameters and responses, could
account for the discrepancies.
In Phase V (coordinated by CSN and UPC, Spain), the main conclusions, lessons
learned, and recommendations have been collected, and the final report of PREMIUM
has been produced (CSNI, 2016a).
A majority of CIRC⟨E users obtained envelop calculations, which were globally
satisfactory for FEBA results, but not for PERICLES results. For the nominal calculation
, most participants predict a too rapid quench front progression for FEBA.
However, a majority of participants predict a too slow quench front progression for
PERICLES.
CIRC⟨E users estimate median values for their input parameters, different from the
nominal values. The median values produce what is called a “calibrated calculation.”
This corresponds to a “calibration” of models of the system code. Theoretically, this
action corrects systematic deviations of the nominal calculation with respect to the
experiment used for the quantification. This effect can be especially observed for
the prediction of the quench front progression.
The calibrated value of the input parameters found for FEBA is applied to
PERICLES. But the prediction of the quench front progression is often different
for FEBA and PERICLES. Therefore, the calibrated calculation leads to a deviation
to the measured quench front on PERICLES. In addition, the intention of CIRC⟨E is to
derive narrow uncertainty bands. In order to get more representative ranges and distributions
, more suitable experiments should be included for deriving the input
uncertainties.
The intention of PREMIUM was to use one or a series of six experiments of the
same test facility (FEBA) to derive model input uncertainties and use these for the
uncertainty evaluation of another experiment (PERICLES). Using only one experimental
facility is not recommended for a validation strategy and to derive input model
uncertainties based on the experience from that validation. In the case of PREMIUM,
an application of methods to derive input uncertainties inversely from output magnitudes
was the objective, and it was considered that it can be extrapolated to a similar
experiment, PERICLES. That assumption failed obviously because of differences of
the two experimental facilities.
In order to get more representative ranges and distributions of model input parameters
, more suitable experiments should be considered for deriving the input uncertainties
. Very well known BEPU framework like the CSAU (Boyack et al., 1990)
or the evaluation model development and assessment process (EMDAP) (NRC,
2005b) should be taken into account in the task, see also Section 13.4.2.1 of this chapter
. Two issues are important here:
l
A strategy to collect experimental databases for TH code model input uncertainty evaluation
l
Combine results of input uncertainty quantification from several experiments
