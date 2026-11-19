# Appendix D Some Properties of Special Functions
<!-- source PDF pages 725-728 -->

<!-- page 709 (PDF 725) -->
# Appendix D Some Properties of Special Functions

1) Legendre Functions:
a) Defining equation:
(1 − x2) f ´´ − 2xf ´ + l(l+1)f = 0;
l = integer
(D.1)
b) Representation:
Pl(x) = 1
2ll!
dl
dxl (x2 − 1)l
(D.2)
c) Properties:
P0(x) = 1;
P1(x) = x;
P2(x) = 1
2 (3x2 − 1);
P3 = 1
2 (5x3 − 3x);
. . .
(D.3)
Z +1
−1
Pl(x)Pl´(x)dx =
2l + 1 δll´
(D.4)
d) Recurrence relations:
P´
l+1(x) − xP´
l(x) = (l + 1)Pl(x)
(D.5)
(l + 1)Pl+1(x) − (2l + 1)xPl(x) + lPl−1(x) = 0
(D.6)
2) Associated Legendre Polynomials:
a) Defining equation:
(1 − x2) f ´´ − 2xf ´ + l(l + 1) −
m2
1 − x2

f = 0
(D.7)
b) Representation:
Pm
l (x) = (1 − x2)(m=2) dm
dxm Pl(x)
(D.8)
c) Spherical harmonics:
Y lm(Ω) = (2l + 1)(l − m)!
4π(l + m)!

(1=2)
Pl(cos θ)eimϕ
(D.9)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 710 (PDF 726) -->
d) Properties:
Z
4π
dΩY ∗
lm(Ω)Y l´m´(Ω) = δll´δmm´
(D.10)
Pl(Ω ? Ω´) =
4π
(2l+1)
X
l
m=−l
Y ∗
lm(Ω)Y lm(Ω´)
(D.11)
3) Bessel Functions:
a) Defining equation:
x2f ´´ + xf ´ + (x2 − n2)f = 0
(D.12)
b) Solution:
Jn(x), Bessel function of first kind
Yn(x), Bessel function of second kind
c) Representation:
Jn(x) =
X
k=0
(−1)k
Γ(k+1)Γ(k + n+1)
x
 n+2k
Y n(x) = Jn(x)cos (nπ) − J−n(x)
sin nπ
(D.13)
d) Hankel functions:
H(1)
n (x) = Jn(x) + iY n(x)
(D.14)
H(2)
n (x) = Jn(x) − iY n(x)
(D.15)
4) Modified Bessel Functions:
a) Defining equation:
x2f ´´ + xf ´ − (x2 + n2)f = 0
(D.16)
b) Solution:
In(x), modified Bessel function of first kind
Kn(x), modified Bessel function of second kind
c) Representation:
In(x) = i−nJn(ix) = inJn(−ix)
K n(x) = π
2 in+1H(1)
n (ix) = π
2 i−n−1H(2)
n (−ix)
(D.17)
5) Useful Expansion of Bessel Functions for small x:
J0(x) = 1 − x2
4 + x4
64 − x6
2304 + ∙∙∙
(D.18)
J1(x) = x
2 − x3
16 + x5
384 − ∙∙∙
(D.19)
Y 0(x) = 2
π
γ+ln x

J0(x) + x2
4 + ∙∙∙

;
γ ≡ 0:577216
(D.20)
Y 1(x) = 2
π
γ+ln x

J1(x) − 1
x − x
4 + ∙∙∙

(D.21)

<!-- page 711 (PDF 727) -->
I0(x) = 1 + x2
4 + x4
64 + x6
2304 + ∙∙∙
(D.22)
I1(x) = x
2 + x3
16 + x5
384 + ∙∙∙
(D.23)
K 0(x) = − γ + ln x

I0(x) + x2
4 + 3x4
128 + ∙∙∙
(D.24)
K 1(x) =
γ + ln x

I1(x) + 1
x − x
4 − 5x3
64 + ∙∙∙
(D.25)
a) Asymptotic expansions for large x:
I0(x) =
ex
ffiffiffiffiffiffiffi
2πx
p
1 + 1
8x + ∙∙∙

(D.26)
I1(x) =
ex
ffiffiffiffiffiffiffi
2πx
p
1 − 3
8x + ∙∙∙

(D.27)
K 0(x) =
ffiffiffiffiffiπ
2x
r
e−x 1 − 1
8x + ∙∙∙

(D.28)
K 1(x) =
ffiffiffiffiffiπ
2x
r
e−x 1 + 3
8x + ∙∙∙

(D.29)
b) Recurrence relations:
xJ´
n = nJn − xJn+1 = −nJn + xJn+1
(D.30)
2nJn = xJn−1 + xJn+1
(D.31)
xI´
n = nIn + xIn+1 = −nIn + xIn−1
(D.32)
x´
n = nK n − xK n+1 = −nK n − xK n−1
(D.33)
J´
0 = −J1;
Y ´
0 = −Y 1;
I´
0 = I1;
K´
0 = −K1
(D.34)
c) Integrals:
Z
xnJn−1(x)dx = xnJn;
Z
xnY n−1(x)dx = xnY n
(D.35)
Z
xnIn−1dx = xnIn;
Z
xnK n−1dx = −xnKn
(D.36)
6) Gamma Function:
a) Definition:
Γ(z) =
Z 1
dte−ttz−1
(D.37)
b) Properties:
Γ(z + 1) = zΓ(z)
Γ(1=2)
=
ffiffiffi
π
p
;
Γ(0) = 1;
Γ(1) = 1; . . . ; Γ(n) = (n − 1)!
(D.38)

<!-- page 712 (PDF 728) -->
7) Error Function:
a) Definition:
erf(x) = 2ffiffiffi
π
p
Z x
dte−t2
(D.39)
b) Complementary error function:
erfc(x) = 1 − erf(x) = 2ffiffiffi
π
p
Z 1
dte−t2
(D.40)
8) Exponential Integrals:
a) Definition:
En(x) =
Z 1
dt e−xt
tn ;
E1(x) =
Z 1
dt e−xt
t
=
Z 1
x
dt e−t
t
(D.41)
b) Properties:
E0(x) = e−x
x
(D.42)
E´
n(x) = −En−1(x)
(D.43)
En(x) =
n − 1 e−x − xEn−1(x)
[
];
n > 1
(D.44)
E1(x) = −γ − lnx −
X
n=1
(−1)nxn
nn!
(D.45)

## References

1 M. ABRAMOWITZ and I. STEGUN (eds.), Handbook of Mathematical Functions,
Dover, New York (1965).
2 H. MARGENAU and G. M. MURPHY, The Mathematics of Physics and Chemistry,
2nd ed., Vol. I, Van Nostrand, Princeton, NJ (1956).
3 I. S. GRADSHTEYN and I. M. RYZHIK, Table of Integrals, Series, and Products, 4th ed.,
Academic Press, New York (1965).
4 P. M. MORSE and H. FESHBACH, Methods of Theoretical Physics, Vols. I and II,
McGraw Hill, New York (1953).
