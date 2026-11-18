# THE OUTPUT FILE
<!-- source PDF pages 344-348 -->

<!-- page 344 -->
Chapter 26
THE OUTPUT FILE

## 26.1 PRINTING OUT THE OUTPUT FILE

The TRIPOLI-4® output file consists of:
• the name of the dictionary and the data file;
• an echo of the input, for reference;
• if a variance reduction technique is used, intermediate results on cross-sections and k coefficients;
• features of the source;
• the average number of collisions per particle with the associated standard deviation, given batch by
batch;
• the requested results with the required frequencies.

## 26.2 WHEN A VARIANCE REDUCTION TECHNIQUE IS USED

If a variance reduction technique is used, collapsing of the cross-sections of the isotopes making up the
composition is carried out for each composition. Each time the names of the processed isotopes are given,
followed by the matrix of the collapsed scattering cross-sections (upper triangular, as only one group is
retained for the thermal domain) for the material and the type of particle under consideration (neutron or
photon). The matrix elements are macroscopic scattering cross-sections.
Example (with 4 energy groups):
DUMP CONDENSED MATRIX FOR MATERIAL: CONCRETE
PARTICLE: NEUTRON
6.96297e-02 1.03105e-01 1.40319e-02 1.41036e-03
0.00000e+00 2.75304e-01 1.05449e-01 7.52780e-03

<!-- page 345 -->
0.00000e+00 0.00000e+00 5.32216e-01 1.69207e-01
0.00000e+00 0.00000e+00 0.00000e+00 1.29906e+00
The corrected transport cross-sections (total cross-section minus the product of the scattering cross-section
and the cosine of the average deviation angle) are given by biasing group (in decreasing energy).
Example (with 4 energy groups):
transport corrected cross-sections:
2.09351e-01 3.89181e-01 7.01549e-01 1.84914e+00
With automatic biasing, the following lines indicate, only for information, the values of the biasing coefficient
k, calculated using the Placzek equation, for the different values of β (0, 0.1, 0.2, 0.5, and 1.). The value of k
is calculated on the basis of the first detector only. The last value of k printed corresponds to the actual choice
of the value of β made by the user.
Example
placzeck k values , beta = 0.00000e+00
1.10537e-01 5.52686e-02 2.76343e-02 4.14515e-02
placzeck k values , beta = 1.00000e-01
1.45290e-01 1.51002e-01 2.26503e-01 3.39755e-01
placzeck k values , beta = 2.00000e-01
1.64969e-01 1.97704e-01 2.96556e-01 4.44834e-01
placzeck k values , beta = 5.00000e-01
1.88416e-01 2.61919e-01 3.92878e-01 5.89317e-01
number of ponderation groups fixed :
1
placzeck k values , beta = 1.00000e+00
1.88416e-01 2.82624e-01 4.23936e-01 6.35903e-01
number of ponderation groups fixed :
1
placzeck k values , beta = 1.00000e+00
1.88416e-01 2.82624e-01 4.23936e-01 6.35903e-01
number of ponderation groups fixed :
1
The value of k must not exceed 0.9 times the value of the total cross-section. If solving the Placzek equation
gives an excessively large value, k is set to 0.9 times the total cross-section. When this is done, the code prints
a message indicating the number of transport groups for which k has thus been chosen (the line number of
ponderation groups fixed:
1 in the example).
If the monitoring option is selected (the default case), an estimate of splitting (with standard deviation) and
the normalization factor for the biasing groups are supplied. In all cases, biasing statistics are indicated, at
least for the first batch (for the first ones, in the case where a variance reduction technique is specified).

<!-- page 346 -->
The number of collisions in the detector cell is also provided. If it is too low, the biasing parameters need to
be changed. Important: numbering begins at 0 here.
The biasing statistics indicate the number of particles in each group, as well as the ratio of the weight and
the weight imposed by the importance maps (with associated standard deviation). The normalization factor
is used when there is a weighting factor to be applied.
Example
estimation of splitting on 5 trajectories:
mean:
6.00000e-01 sigma_n = 6.00000e-01
..........
edition statisque de ponderation
ponderation group:
0
total population:
0.00000e+00
weight discrepancy:
0.00000e+00
sigma:
0.00000e+00
..........
number of collision in cell of detector 0:
3
group:
0 normalisation factor = 1.00000e+00
..........
Note: If, for a material, the name begins with VOID, the value of k is set at half the smallest value of the other
materials.
In the event of problems with biasing, it is possible, as a last resort, to only consider a single group, with an
assigned coefficient k. In such cases, biasing must be made manually (DATA).

## 26.3 OUTPUTS RELATING TO SOURCES

The printed output file gives the following quantities for each source:
• energy intensity integrated in accordance with the definition;
• energy intensity integrated accounting for restrictions concerning the domain due to the energy cut-offs
Einf and Esup: the source no longer emits beyond [Einf, Esup];
• angular intensity;
• time intensity;
• geometrical intensity;
• total intensity integrated (product of partial intensities), initially without energy bounds;
• then true total intensity integrated (with energy restrictions [Einf, Esup]).

<!-- page 347 -->
The code then indicates the intensity of the source, possibly imposed with INTENSITY, then the intensity of
the source accounting for any global norm (imposed by NORM).
Finally, the total intensity as the sum of the intensity of all the sources is supplied (in particles, after the
words GLOBAL SIMULATION INTENSITY).
In the result part of the output file the code is also displaying the source intensity depending on the mode of
operation (mono-processor or parallel) :
• mono-processor : the code issues a statement “RESULTS ARE GIVEN FOR SOURCE INTENSITY"
then the value of the source intensity
• parallel : the simulators do not send this information to the collector, therefore the collector is indicating
: “RESULTS ARE GIVEN FOR SOURCE INTENSITY : unavailable”, but it is still possible to find the
intensity in each simulator output file (GLOBAL SIMULATION INTENSITY).

## 26.4 OUTPUTS FOR EACH BATCH

This relates to the statistics on the collision, the number of particles, and the number of secondary particles if
any.
Statistics on “mean number of deposited” are also given for each batch in case of use of the standard variance
reduction technique (i.e., the exponential transform) during the simulation. This information gives the mean,
on the source particles of the current batch, of all splitting operations for the particles and their progeny
coming from splitting as well.

## 26.5 COMPLETE OUTPUTS

Complete outputs corresponding to responses are supplied at the requested frequency. Each time, every score
is printed, with a list of its attributes (name of response, type of particles, and estimator). The score is a value
integrated over the energy group. The standard deviation is given with the score.
The results are given in decreasing energy group order. Only results in groups whose values are not zero are
given unless the execution option -a is specified (cf. chapter 1) .
The 99.8% confidence interval is indicated with its minimum value (lower) and maximum value (upper) in
the case of a bootstrap calculation (in which the normal (Gaussian) distribution hypothesis is not applied).

## 26.6 CRITICALITY CALCULATIONS

In criticality mode, if the code has to produce 0.5 neutrons, the calculation algorithm actually produces 1
neutron with a probability of 0.5.
"KEFF at step" first gives the keff tallied by the KSTEP estimator. This printout takes the DISCARD option
into account. It appears before all result edition (just before source intensity).
Then, combined keffs are given after the response part. These keffs take into account the DISCARD option too.
The code prints the values of keff (indicating the number of batches discarded) with three estimators:
• the KSTEP estimator, which accounts for the neutrons produced by the code at each stage;

<!-- page 348 -->
• the KCOLL estimator, which accounts for the average number of neutrons that the code should produce
(estimation based on the collision);
• the KTRACK estimator, which accounts for the average number of neutrons that the code should produce
(estimated using the path).
First the code writes the keffs alone, then edition is done combining them two by two. Then, the code gives
the result of all three keffs combined ("full combined estimator"). All the combined estimators take into
account the inter-estimator correlations to produce an "almost unbiased" mean and standard deviation. In
some conditions (for example with highly correlated estimators), the estimation of the combined estimator is
numerically dangerous. In this case, the output of the value is disabled and replaced by a "not yet converged"
output.
Eventually, the code produces the three previous types of keffs with an automatic discard estimation. This
corresponds to the historic edition of keffs.
All keff estimators should be statistically equivalent.
Remark: refer to the DISCARD option of chapter 22 for more information regarding these estimators.

## 26.7 SUB-CRITICALITY CALCULATIONS

The results are given in the same manner for a sub-critical calculation with sources.
Care is nevertheless required: 1·10−11 must be used as the lower energy value of the simulation. Otherwise,
the two estimators KSTEP and KCOLL will not give the same value. This is because KSTEP, which uses
the neutrons monitored by the code, will undergo the energy cut-off, whereas KCOLL and KTRACK, which
account for the expected neutrons, will not be affected by the cut-off.
