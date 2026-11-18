# 3-Field models in system codes
<!-- source PDF pages 72-74 -->

<!-- page 238 (PDF 72) -->
## 5.13.5 Polydispersed dynamic modeling with a multifield approach

Another approach for modeling polydispersion is the multisize group (MUSIG)
method where mass balance equations are written for different size groups of bubbles
or drops with all transfers between groups being modeled. This provides a discrete
function f. The MUSIG model was developed and validated (Krepper et al., 2011)
to describe the bubble size polydispersion, where the disperse phase is divided into
a number of groups, each group being characterized by its volume fraction and velocity
field by writing several mass and momentum equations. This approach has already
proven good capabilities to capture the different behavior of small and large bubbles
and the influence on the formation of a certain flow pattern.

## 5.13.6 Predictive capabilities of the monodispersed and polydispersed approaches

Using a simple algebraic model for the interfacial area provides an average bubble
size—the Sauter mean diameter—which cannot take all effects into account. Coalescence
and break-up may have rather long relaxation times so that equilibrium between
them is not reached in the situation of interest. Moreover boiling and condensation
may affect the size and depart from equilibrium.
Using a transport equation for either the bubble number density or the IA may
improve the prediction of coalescence and break-up. However there are common limitations
of both algebraic and dynamic “monodispersed” bubble size models since
almost all dispersed flow of interest in reactor thermalhydraulics have a rather large
bubble and drop size distribution.
Inordertogobeyondtheselimitations,polydispersedmodelsoffermuchbetterinherent
capabilities but require a huge effort for modeling coalescence and fragmentation
A state of the art in using monodispersed or polydispersed approaches can be found
in Krepper et al. (2011), for CMFD and status and perspective for TIA in system codes
was presented by Bestion and Serre (2013). Some conclusions are:
l
TIA models available today cover only a very small fraction of the flow situations of interest.
l
The analysis of some flow regimes with new measurement giving access to IA and bubble size
distribution has confirmed that almost all flow are nonestablished flows. In such condition an
algebraic IA modeling has many limitations, a TIA equation brings some added value.
l
A polydispersion modeling would be necessary to get a very significant progress.
5.14
3-Field models in system codes
When a phase is present in both a dispersed field and a continuous field it may happen
that both fields have very different behaviors. Using a simple mass, momentum, and
energy equation for both fields may not be able to predict important phenomena. This
was identified in nuclear reactor thermalhydraulics particularly for annular-mist flow
where the liquid is present with droplets in the core steam flow and films along the
walls. A similar situation may exist in horizontal pipes when there is a free surface

<!-- page 239 (PDF 73) -->
and a steam flow carrying droplets above. This may be encountered in a boiling water
reactor (BWR) core in normal and abnormal situation and in some accidental situations
in a pressurized water reactor (PWR). 3-field models were then developed to better
capture the physics of the flow. Film velocity is usually small (of the order of a few
cm/s or mm/s), whereas droplets may be entrained at higher velocities (several m/s)
in the gas phase. It may happen that both liquid fields are countercurrent with falling
films and upward flowing droplets. The interest of a 3-field model for a large break loss
of coolant accident (LBLOCA) simulation was presented by Valette et al. (2009).
1-D 3-field equations are derived following the same method as for the two-fluid by
multiplying by field characteristic functions of vapor χv, continuous liquid χcl and dispersed
liquid χdl before applying time and space averaging.
New transfers are defined:
Γvcl = −Γclv is the interfacial mass transfer from continuous liquid to vapour (kg/m3/s)
Γvdl = −Γdlv is the interfacial mass transfer from dispersed liquid to vapour (kg/m3/s)
Γd is the mass transfer from dispersed to continuous liquid by droplet deposition (kg/m3/s)
Γe is the mass transfer from continuous to dispersed liquid by droplet entrainment (kg/m3/s)
qidl is the heat flux per unit volume from interface to droplet (W/m3)
qivdl is the heat flux per unit volume from vapour to interface of droplet (W/m3)
qicl is the heat flux per unit volume from interface to continuous liquid (W/m3)
qivcl is the heat flux per unit volume from vapour to interface of continuous liquid (W/m3)
Vidl is the interfacial axial velocity at dispersed liquid interface (m/s)
Vicl is the interfacial axial velocity at continuous liquid interface (m/s)
The term Afivcl
∂αcl
∂z
may be modeled as the equivalent term in two-fluid for
stratified flow
The term Afivdl
∂αdl
∂z
may be modeled as the equivalent term in two-fluid for
dispersed flow
An added mass term AFv
AM is used for interactions between gas in bubbly flow and
continuous liquid, but there is no need to use such a term for interactions between
droplets and gas which would have a minor effect on droplet behavior.
It is assumed that there is no direct contact between dispersed liquid and walls since
drops would deposit in pre-CHF conditions and would bounce in post-CHF conditions
. Then there is no wall friction for droplets, no wall direct heat transfer for droplets
, no gdl
∂A
∂z term, and no Aαdl
δPdlsing
δz
term.
The set of equation is given below for the case where axial diffusion-dispersion
terms are neglected.
1-D 3-field equations for gas-continuous liquid-droplets
Principal variables: αv,αcl, P, Vv, Vcl, Vdl, Hv, Hcl, Hdl
A∂αvϱv
∂t
+ ∂AαvϱvVv
∂z
= AΓvcl + AΓvdl
A∂αclϱcl
∂t
+ ∂AαclϱclVcl
∂z
= AΓclv + AΓd −AΓe

<!-- page 240 (PDF 74) -->
A∂αdlϱdl
∂t
+ ∂AαdlϱdlVdl
∂z
= AΓdlv −AΓd + AΓe
A∂αvϱvVv
∂t
+ ∂AαvϱvVvVv
∂z
+ Aαv
∂P
∂z − Afivcl
∂αcl
∂z − Afivdl
∂αdl
∂z + gv
∂A
∂z
= Aαvϱvgz −Aτivcl −Aτivdl −Cvτwv −Aαv
δPvsing
δz
+ AFAM
v
+ AΓvclVicl + AΓvdlVidl
A∂αclϱclVcl
∂t
+ ∂AαclϱclVclVcl
∂z
+ Aαcl
∂P
∂z + Afivcl
∂αcl
∂z + gcl
∂A
∂z
= Aαclϱclgz −Aτiclv −Cclτwcl −Aαcl
δPclsing
δz
+ AFAM
cl + AΓclvVicl + AΓdVdl −AΓeVcl
A∂αdlϱdlVdl
∂t
+ ∂AαdlϱdlVdlVdl
∂z
+ Aαdl
∂P
∂z + Afivdl
∂αdl
∂z
= Aαdlϱdlgz −Aτidlv + AΓdlvVidl −AΓdVdl + AΓeVcl
A
∂αvϱv
Hv + Vv
(
∂t
+
∂AαvϱvVv
Hv + Vv
(
∂z
− Aαv
∂P
∂t
= AαvϱvgzVv + Cvqwv + Aqidl + Aqivdl + AΓvdl
Hv + Vidl
(
+ Γvcl
Hv + Vicl
(
+ Aqextv
A
∂αclϱcl
Hcl + Vcl
(
∂t
+
∂AαclϱclVcl
Hcl + Vcl
(
∂z
− Aαcl
∂P
∂t
= AαclϱclgzVlc + Cclqwcl + Aqicl + AΓvcl
Hcl + Vicl
(
− Γe Hcl + Vcl
(
+ Γd
Hdl + Vdl
(
+ Aqextcl
A
∂αdlϱdl
Hdl + Vdl
(
∂t
+
∂AαdlϱdlVdl
Hdl + Vdl
(
∂z
− Aαdl
∂P
∂t
= AαdlϱdlgzVlc + Cdlqwdl + Aqidl
+ AΓvdl
Hdl + Vidl
(
+ Γe Hcl + Vcl
(
−Γd
Hdl + Vdl
(
+ Aqextdl
Γvdl = −Γdlv = qidl + qivdl
hvl
;Γvcl = −Γclv = qicl + qivcl
hvl
; τivcl = −τiclv;τidlv = −τivdl;FAM
v
= −FAM
cl
αv + αcl + αdl = 1; ϱk = ρk P, Hk
ð
Þ;Tk = Tk P, Hk
ð
Þ;μk = μk P, Hk
ð
Þ;λk = λk P, Hk
ð
Þ
+ expressions for Γe,Γd,fivdl, fivcl,gv, gcl τidlv,τivcl,qicl, qivcl, qidl, qivdl Ck,τwk,qwk,δPksing, F v
AM, Vicl, Vidl
