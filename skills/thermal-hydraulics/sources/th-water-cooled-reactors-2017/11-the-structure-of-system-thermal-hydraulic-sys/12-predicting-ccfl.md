# Predicting CCFL
<!-- source PDF pages 64-65 -->

<!-- page 702 (PDF 64) -->
4. The semiempirical approach: Compared to the previous method, weaker assumptions are
made, which allow to deriving expressions theoretically with some free parameters to tune
with experimental data. The interfacial friction in bubbly-slug and churn flow regimes in
pipes and rod bundle developed for the CATHARE code (Bestion, 1990a,b) are of this type.
Interfacial heat transfer expressions for direct contact condensation at ECCS are also of this
type (Janicot and Bestion, 1993).
First versions of the system codes used mainly the mechanistic approach but, after an
extensive validation, the degree of empiricism of closure relations was progressively
increased reflecting the lack of knowledge and the complexity and diversity of the
physical mechanisms involved in such a large variety of two-phase flows. Therefore,
the quality and reliability of the closure laws are mainly the result of an extensive validation
database in the most representative experiments. Extrapolation beyond the validated
domain remains somewhat hazardous.
Looking at closure laws in current system codes, one can observe the following:
l
Codes rarely selected the same correlation for the same transfer. First versions of the codes
used many academic mechanistic models which were often modified through empirical corrections
after comparison with experimental data of the validation.
l
Even when the various codes do not use the same basic correlation, they often converged to
the same degree of empiricism in the selected final correlation. The level of empiricism just
reflects the degree of understanding of basic processes or the lack of knowledge.
l
A high accuracy is not required for all models and more attention was paid to the most sensitive
models in accidental transients and an effort was made to improve them using corrections
based on experimental validation. The sensitivity of transient scenarios of interest
being not equal for all the models, it results that the accuracy and reliability of the models
is not equal for all the models. As a consequence, when a new situation is investigated with
different sensitivities, it is often necessary to pay more attention to some closure laws which
are found not accurate enough.
11.12
Predicting CCFL
The two-fluid model either with a drift flux model or with two-momentum equations
is able to predict the CCFL and a flooding limit. It results from the force balance with
dominant effects of gravity, acceleration, and interfacial friction forces. However, this
does not guaranty that the CCFL will be predicted correctly in a reactor transient since
it is likely to occur in complex geometries within the reactor circuits where standard
interfacial friction laws are no more valid due to local geometrical effects. For example
in a PWR, CCFL is likely to occur at the following locations (see Fig. 11.23):
l
Upper tie plate in a PWR core
l
SG tube inlet in a PWR
l
HL bend of a PWR
All system codes developed local treatment to obtain a predetermined flooding curve
(WallistypeorKutateladzetype).Suchfloodingcorrelationcanbeputonageneralform:
J
*1)
g
Bo
ε=4 + M J
*1)
l
Bo
ε=4 = C

<!-- page 703 (PDF 65) -->
When the exponent of the Bond is zero, it is a Wallis type correlation and when it is 1 it
is a Kutateladze type correlation.
A drift flux model was made consistent with a flooding correlation in the ATHLET
code (Sonnenburg, 1989)
VCCFL
gj
= C2
Coα 1≡Coα
ð
Þ
ρg
gΔρD
□
(1)
Bo
ε=2Coα + M2
ρl
gΔρD
□
(1)
Bo
ε=2 1≡Coα
ð
Þ
An interfacial friction model was made consistent with a flooding correlation in the
CATHARE code (Freitas and Bestion, 1993)
τCCFL
i
= α 1≡α
ð
Þ
Boε
Co2C4D Coα
ffiffiffiffi
ρg
p
+ M2 1≡α
ð
Þ
ffiffiffiffiρl
p
h
i
Vg ≡Co 1≡α
ð
Þ
1≡Coα
ð
ÞVl
□
□2
CCFL
Fig. 11.23 Example of locations where CCFL may occur in accidental transients of a PWR.
