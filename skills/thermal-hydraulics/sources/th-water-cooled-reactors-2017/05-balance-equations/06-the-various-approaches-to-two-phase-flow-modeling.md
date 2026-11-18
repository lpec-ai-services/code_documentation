# The various approaches to two-phase flow modeling
<!-- source PDF pages 30-36 -->

<!-- page 196 (PDF 30) -->
principal variables (P, V, H) is sufficient to model the process. Moreover algebraic
expressions are most often used without partial derivatives. This corresponds to the
assumption of a quasi-steady quasi-established flow. The quasi-steady approximation
is a reasonable approach when time scales of the process are small compared to time
scale for variations of principal variables. The quasi-established flow is a reasonable
approach in case of a regular geometry after some distance from entry (say Z/D > 50)
when radial profiles of velocity and temperature are similar (not dependent on
abscissa). It also requires that time scales of the process are small compared to transit
time scales V/L.
The set of equation is able to give very good predictions of many 1-phase flows
with heat transfers. Main limitations are:
l
If the flow is not really one-dimensional, i.e., if the direction of the flow is not unique
in a section of the duct, for example, when buoyancy forces induce natural circulation cells
in the duct, pressure, and temperature field cannot be precisely described by 1-D
equations;
l
Closure laws for τw and qw are available for a simple geometry like a circular pipe, a square
or rectangular duct, an annulus, but predictive capabilities in more complex geometry (rod
bundle) may require that specific closure laws are established based on prototypical
experiments.
l
In case of a local complex geometry, no universal model can predict singular pressure losses.
Specific form loss coefficients have to be used depending on the geometry, but the 1-D
model cannot predict it by itself. The geometrical effects on wall heat transfer may also
be very important. Usually any perturbation of the flow which increases turbulence may
increase heat transfer coefficient. 1-D model cannot predict this effect by itself.
l
Rapid transient conditions may require more sophisticated wall momentum and heat transfers
depending on partial derivatives of V, H, and Tw.
l
Nonestablished flow exist in a significant part of any industrial systems and using classical
closure laws for established flow may involve some inaccuracy of predictions.
5.6
The various approaches to two-phase flow modeling
One can classify two-phase modeling approaches (Bestion et al., 2011) in a similar
way as was done for single phase in Section 5.3. Classification is made with regard
to the space dimension of the model, considering 0-D, 1-D, 2-D, and 3-D models.
Then, to be more specific on may consider the type of time and/or space averaging
which is used. 3-D models of two- or multiphase flow are often called computational
multifluid dynamics (CMFD). They are split first into 3-D for porous body and 3-D
CFD in an open medium approach.
RANS-type time-averaged models, LES-type space-filtered models, and DNS type
models are the three main categories of two-phase CFD models in open medium (see
Table 5.3). Due to a much higher complexity of two-phase flow compared to
single-phase flow, 1-D models are the most mature and commonly used in nuclear
reactor applications. 3-D RANS models are also progressively used for some reactor

<!-- page 197 (PDF 31) -->
Table 5.3 Classification of Eulerian fluid dynamic simulation approaches for two-phase CFD
Treatment of equations
Pseudo DNS
Scale/eddy-resolving approaches
RANS URANS
Time or ensemble averaging
No
No
No
No
Yes
Space filtering
No
Yes
Yes
Yes
No
Multiplication by phase (field)
characteristic functions
Nb of phases or fields
No
1-Fluid
No
1-Fluid
Yes
2-fluid
n-field
Yes
2-fluid
n-field
Yes
2-fluid
n-field
TM or Interface
Recognition/reconstruction (IR)
Statistical Interfaces
Deterministic Interfaces
Filtered Interfaces
ITM
deterministic
interfaces
ITM
deterministic
interfaces
IRM filtered and
statistical interfaces
No statistical
interfaces
No (IRM) statistical
(and filtered
interfaces)
Type of approach
Pseudo DNS
LES with
deterministic
interfaces
Hybrid LES with
filtered and statistical
interfaces
LES with
statistical
interfaces
RANS URANS
statistical and filtered
Interfaces)
Required modeling effort
ε
X
XXXXX
XX
XXXX
Locality—universality of the
modeling
*****
****
***
***
*

<!-- page 198 (PDF 32) -->
issues, but there is no mature 3-D CMFD model in an open medium covering all flow
regimes. A modeling covering all flow regimes is still a challenge (see Bestion, 2014).

## 5.6.1 Time space and phase averaging in two-phase flow

Phase averaging means that a multiplication of local instantaneous equations by a
phase indicator function (or phase characteristic function) is made before a time or
a space averaging.
Let χk be the phase indicator function (see Fig. 5.3) of phase k:
χk x, y, z, t
ð
Þ = 1 if point (x, y, z) is occupied by phase k at time t
χk x, y, z, t
ð
Þ = 0 if point (x, y, z) is not occupied by phase k at time t
In a two-phase flow, with liquid and gas χg + χl = 1
A two-phase flow canbe split into several fields including, for example, a continuous
liquid field, a continuous gas field, one or Nb bubble fields, and one or Nd droplet fields.
In this case, a field averaging means that local instantaneous equations are multiplied by
field indicator (or characteristic) functions before a time or a space averaging.
Let us define some useful quantities and operators.
1-D space averaging:
fh iL≜1
L
ð
L
fdl
Area averaging:
fh iS≜1
A
ð
A
f ds
Volume averaging:
fh iV≜1
V
ð
V
fdv
Volume filtering:
f x, y, z, t
ð
Þ
h
iδv≜
ððð
R3g x0 −x,y0 −y,z0 −z,t
ð
Þ· f x0,y0,z0,t
ð
Þdx0dy0dz0
with
ððð
R3g x, y, z
ð
Þdxdydz = 1
t
xk (x,t)
Fig. 5.3 Definition of time fractions for phase k.

<!-- page 199 (PDF 33) -->
The filter function g may be a uniform function over a distance δf
Time averaging:
⟨f ≜1
T
ð
T
fdt
Time fraction of phase or field k:
εk ≜χk = 1
T
ð
T
χk dt = Tk
T
Phase or field space (surface) averaging:
⟩f k
k≜
ð
A
χkfkds
ARk
One can notice:
Rk ⟩f k
k = χk fk
h
iS
Phase or field time averaging:
⟨f k≜
ð
T
χkfkdt
ð
T
χkdt
Space-time averaging (time-area averaging)
^⟨f≜⟨f
□ □S
Mass-weighted space-time averaging
⟩⟨f≜ρ⟨f
□
□S
ρ
h iS
Phase or field space-time averaging
b⟨f k
k
≜χkfk
□
□S
αk
Mass-weighted phase space-time averaging
⟩
⟨f k
k≜χkρkfk
□
□S
χkρk
h
iS =
d
ρkfk
k
c
ρk
k

## 5.6.2 CMFD models

Five types of Eulerian two-phase CFD approaches for open medium are distinguished
in Table 5.3. They differ by the treatment applied to basic mass, momentum and
energy balance equations. The four successive choices can be made successively:
1. Multiplication or not of mass momentum an energy equations by the phase indicator
functions (for each phase in the two-fluid approach) or multiplication by the field indicator
functions (for each field for a multifield approach)
2. Time averaging or not
3. Space filtering or not
4. Addition of an interface tracking method (ITM) or interface reconstruction technique (IRT)
for some or all interfaces or not
These choices allow to distinguishing various methods according to the following
aspects:
l
Phase averaging or field averaging:
−
Mixture model under Homogeneous and Algebraic Slip
−
Two-fluid model
−
Multifield models

<!-- page 200 (PDF 34) -->
l
Filtering turbulent scales and two-phase intermittency scales:
−
All turbulent and two-phase scales are filtered (RANS type models)
−
Only some scales are filtered (LES type models)
−
All scales are predicted or simulated (DNS type models)
l
Treatment of Interfaces
−
Use of ITM
−
Use of Interface Reconstruction method
−
Use of a pure statistical treatment of interfaces
As a result of the various choices three kinds of interface treatment are possible:
l
Deterministic interface: or simulated interface: an interface is said “deterministically
treated” when its space and time position is simulated or actually predicted without any
simplification. This requires the use of an ITM.
l
Statistical Interface: An interface is said “Statistically treated” when a space or time
averaging or filtering procedure does not allow to predicting its space and time position.
Only statistical or averaged information on several interfaces may be predicted through
quantities such as a void fraction, or an interfacial area density. This is the case for small
bubble and droplet interfaces of Figs. 5.3 and 5.4.
l
Filtered interface: An interface is considered as “Filtered Interface” when its space and time
position is predicted with some filtering of the smaller scale deformations. This filtering may
result either from space filter or time averaging.
The modeling of wall transfers, interfacial transfers, interfield transfers, and turbulent
transfers depends on the approach. Each approach is described in short here below.

### 5.6.2.1 The pseudo-DNS method

The pseudo-DNS does not apply any space or time averaging of the equations. However
some ITM is required to tracking the interface. A one-fluid approach is used.
Additional models are often required, for example, for implementing a film splitting
criterion when two bubbles coalesce or for the contact angles at a triple line
solid-liquid-gas. Such additional models are the reason why in two-phase flow the
word DNS must be replaced by pseudo-DNS since some very small scale physics
is not solved but only modeled.
Phase f
Phase g
vni
vti
ng
nf
Fig. 5.4 Interface between phases f and g.

<!-- page 201 (PDF 35) -->
Since no averaging or filtering is used, pseudo-DNS should be able to simulate all
interfaces including the smaller-scale interface deformations and to predict the
smaller-scale eddies up to the Kolmogorov dissipative scale. Since even pseudo-
DNS requires extremely expensive CPU cost, its use is restricted to the investigation
of very small scale flow processes as a complement to experimental investigations and
as a support for the modeling and validation of more macroscopic approaches.
The pseudo-DNS can in principle simulate all flow regimes but is in practice
limited by the extremely expensive CPU time which is required.

### 5.6.2.2 The RANS method

The RANS method (or U-RANS) is the most simple, the cheapest (in terms of CPU),
the most advanced, and the most used available two-phase CFD method. All turbulent
scales and all two-phase intermittency scales are filtered. All interfaces are statistically
treated. The method is applied to steady flows or quasi-steady (U-RANS) flows
when the time scales of variation of mean variables are larger than the largest time
scales of turbulence and two-phase intermittency (time between passage of two interfaces
at a given point).
In case of stratified flow or annular flow, large interfaces (free surface or film interface
) can be treated as “filtered interfaces.” RANS is in principle compatible with all
two-phase flow regimes provided that they are steady or quasi-steady. For dispersed
bubbly flow or dispersed droplet flow, the condition is easy to satisfy. For separatephase
flows (stratified flow, annular flow), the averaging filters interfacial waves in a
way which is not fully clear: although the RANS modeling of turbulent diffusion prevents
simulation of large eddies it does not prevent irrotational waves to be predicted
resulting from Kelvin-Helmholtz instability. Therefore RANS and URANS are compatible
with the statistical interfaces and to some filtered interfaces.
For slug and churn flow regimes with large bubbles (either Taylor bubbles in slug
flow or distorted large bubbles in churn flow) the intermittency due to the passage of
these bubbles corresponds to rather large time scales. Since the RANS filters even
these large scales it is not able to predict this intermittency, but the average behavior
can be predicted.
RANS is compatible with all the possible choices for the number of fields, including
single-fluid, two-fluid, and all kinds of multifield models.

### 5.6.2.3 The LES with deterministic interface

The LES with deterministic interface combines a filtering of turbulent fluctuations
with an ITM used for all interfaces. This method was first proposed by Toutant
et al. (2009a,b), Bois et al. (2010), Magdeleine et al. (2010), Lakehal (2008), and
Lakehal et al. (2008), for free surface flow. The concept has been since then better
reformulated by Lakehal and Labois (2011), who refer to it as LEIS, short for
large-eddy and interface simulation (LEIS).

<!-- page 202 (PDF 36) -->
### 5.6.2.4 The LES with statistical interfaces

When the largest interfacial scale is rather small and significantly smaller than the
largest turbulent eddies, a LES method is applicable with a filters scale smaller than
the larger eddies but larger than the two-phase scale to allow a statistical treatment.
The idea was first developed by Lakehal (2002), who put the filtered two-fluid equations
on firmer grounds and proposed a bubble-induced diffusion model incorporated
within the Dynamic Procedure of Lilly and Germano (see Lilly, 1991). It was since
then applied with some success to some turbulent dispersed flow by Dhotre et al.
(2007), Dhotre et al. (2008), Niceno et al. (2008), and Nicˇeno et al. (2009).
Such a method is clearly much less CPU consuming than the pseudo-DNS and the
LES with deterministic interface, but it is restricted to some flow situations, typically
the dispersed bubble or dispersed drops where the large eddies are much larger than
the largest bubbles or eddies. In slug or churn flow where the largest bubbles and the
largest eddies are of the size of the geometrical dimensions of the flow (such as a
Hydraulic diameter) this method is clearly not applicable.
This method is compatible with the two-fluid model and multifield models where
the dispersed bubbles or droplets may be treated by size groups.

### 5.6.2.5 The hybrid LES method with both filtered and statistical interfaces

This hybrid method filters the smaller eddies and treats statistically the small droplets
or small bubbles, while the other interfaces are simply filtered and treated as large
interfaces. The space filter eliminates the smaller bubbles which are treated statistically
, and it thickens and filters the interface of the large bubble which may be
reconstructed with a simplification of the shape.
Lakehal (2010) discussed the difficulties of this method in comparison to the LES
with simulated interfaces.
It may be a promising way of modeling the most complex two-phase flow (such as
churn or slug flow) at a reasonable CPU cost without filtering the large two-phase
structures like RANS does. However the closure issue is rather complex, and the present
state of the art is not very well advanced.
This method is compatible with the two-fluid approach and with multifield models.
A fourfield model with a continuous gas field, a continuous liquid field, a dispersed
bubble field, and dispersed droplet field may help to reconstruct the large filtered
interfaces and to model the mass transfers between continuous and dispersed fields.
This method includes much more closure terms to model than the LES with deterministic
interfaces. In particular the effects due to subgrid waves of large interfaces
have to be modeled.
It was observed that many applications which use an ITM pretend to be of the LES
type with deterministic interfaces although they are actually hybrid methods. The
interface tracking by the ITM is “underresolved” and simulated interfaces are
“filtered interfaces” instead of “deterministic interfaces.” All effects due to subgrid
waves of large interfaces should be added in the modeling.
