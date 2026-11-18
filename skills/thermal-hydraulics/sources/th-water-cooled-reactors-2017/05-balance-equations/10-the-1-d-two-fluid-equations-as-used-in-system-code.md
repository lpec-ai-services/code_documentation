# The 1-D two-fluid equations as used in system codes
<!-- source PDF pages 56-56 -->

<!-- page 222 (PDF 56) -->
A∂αkϱkVk
∂t
+ ∂AαkϱkVkVk
∂z
+ Aαk
∂P
∂z + Afi
∂αk
∂z + gk
∂A
∂z
= A αkϱkgz +
∂ARk Tt
kz + Td
kz
□
□
∂z
−Aτik −Ckτwk −Aαk
δPksing
δz
+ AFAM
k
+ AΓikVi
A
∂αkϱk Hk + Vk
(
∂t
+
∂AαkϱkVk Hk + Vk
(
∂z
−Aαk
∂P
∂t = −
∂A αk qkz + qt
kz + qd
kz
□
□
∂z
+ AαkϱkgzVk + Ckqwk + Aqik + AΓik HK + Vi2
(
+ A τikVi + Aqkext
X
k
αk = 1;
X
k
Γik = 0;
X
k
τik = 0;
X
k
FAM
k
= 0;
X
k
qik + ΓikHk
½
□ = 0;
qkz + qt
kz + qd
kz = −λeff
k rTk
ϱk = ρk P, Hk
ð
Þ;Tk = Tk P, Hk
ð
Þ;μk = μk P, Hk
ð
Þ;λk = λk P, Hk
ð
Þ
+ expressions or equations for τik,Tt
kz,Td
kz, qik, q
⃗t
k, Ck,τwk,qwk, δPksing, FAM
k , λeff
k
5.10
The 1-D two-fluid equations as used in system codes
System codes such as CATHARE (Bestion, 1990), RELAP-5 (RELAP5/MOD3,
1998), and TRACE (TRACE V5.0, 2007) use the 1-D two-fluid equations as in
Section 5.9 below with some differences. TRACE writes volume-averaged equations
on a part of a duct between two sections. Equations are somewhat similar to the discretized
form of 1-D equations when a staggered grid is used.
Axial diffusion and dispersion terms of momentum are never modeled and may be
partly modeled through the singular pressure loss term.
Momentum equation may be written using the secondary form (CATHARE,
RELAP-5) instead of the conservative form:
Aαkϱk
∂Vk
∂t + AαkϱkVk
∂Vk
∂z + Aαk
∂P
∂z + Afi
∂αk
∂z + gk
∂A
∂z
= A αkϱkgz −Aτik −Ckτwk −Aαk
δPksing
δz
+ AFAM
k
+ AΓik Vi −Vk
ð
Þ
The term gk
∂A
∂z is not present in all codes and may be present (in the Cathare code)
only for stratified flow for which an expression was derived.
The term fi
∂αk
∂z is present in all codes for stratified flow and may be present (in the
Cathare code) for all flow regimes.
