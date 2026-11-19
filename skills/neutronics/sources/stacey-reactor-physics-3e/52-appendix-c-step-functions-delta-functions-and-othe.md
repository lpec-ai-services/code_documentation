# Appendix C Step Functions, Delta Functions, and Other Functions
<!-- source PDF pages 722-724 -->

<!-- page 705 (PDF 722) -->
# Appendix C Step Functions, Delta Functions, and Other Functions

C.1

## Introduction

Consider the discontinuous function Θ(x) defined by the properties
Θ(x) =
0;
x < 0
1;
x □ 0

Θ(x)
x
Θ(x)is the unit “step function” introduced by Heaviside in his development of
operational calculus (now known as integral transform analysis). One can
perform numerous operations on Θ(x). In particular, it can be integrated to
yield the ramp function:
η(x) = ∫
x
−1
dx´Θ(x´) =
0;
x < 0
x;
x □ 0

x
η(x)
Let us try something a bit more unusual by taking the derivative of Θ(x).
Clearly, this is ridiculous, because this derivative, call it δ(x), is undefined at x = 0
because Θ(x) is discontinuous at this point:
δ(x) = Θ´(x) = lim
ε!0
Θ(x + ε) − Θ(x)
ε

=
0;
x ≠0
1;
x = 0

(C.3)
Nevertheless, Dirac, Heaviside, and others have made very good use of this strange
“function.” To be more specific, the Dirac δ-function, δ(x), has the properties
δ(x − x0) =
0;
x ≠x0;
1;
x = x0;

∫
−1
dxδ(x − x0) = 1
(C.4)
(C.2)
(C.1)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 706 (PDF 723) -->
In a sense, it resembles a generalization of the Kronecker δ-function:
δmn =
0;
m ≠n
1;
m = n

The most useful property of the Dirac δ-function occurs when it is integrated
along with a well-behaved function, say f(x):
∫dxf (x)δ(x − x0) = f (x0)
(C.5)
This property is not only very interesting but also extremely useful in mathematical
physics. Unfortunately, the proof of this property – and, indeed, all of the
theory of such generalized functions – requires a rather potent dose of mathematics
. [Such generalized functions are really not functions at all, but rather a
class of linear functionals called “distributions” defined on some set of suitable
test functions (which are “infinitely differentiable with compact support”).]
Fortunately, one does not need all of this high-powered mathematics in order
to use δ-functions. Only a knowledge of their properties is necessary.
C.2

## Properties of the Dirac δ-Function

A. Alternative Representations:
δ(x − x0) = 1
π lim
λ!1
sin λ(x − x0)
(x − x0)
(C.6)
δ(x − x0) = 1
π lim
ε!0+
ε
(x − x0)2 + ε2
(C.7)
B. Properties:
δ(x) = δ(−x)
(C.8)
δ(ax) = 1
jaj δ(x);
a ≠0
(C.9)
δ g(x)

=
X
n
jg´(xn)j δ(x − xn) g(xn) = 0; g´(xn) ≠0

(C.10)
xδ(x) = 0
(C.11)
f (x)δ(x − a) = f (a)δ(x − a)
(C.12)
∫δ(x − y)δ(y − a)dy = δ(x − a)
(C.13)
δ(x) = 1
2π ∫
−1
dkeikx
(C.14)
Actually, these properties only make sense when inserted in an integral. For
example, property (C.8) really should be interpreted as
∫dxf (x)δ(x) = ∫dxf (x)δ(−x) = f (0)
(C.15)

<!-- page 708 (PDF 724) -->
C. Derivatives
One can differentiate a δ-function as many times as one wishes. The mth
derivative is defined by
∫
−1
δ[m](x − a)f (x)dx = (−1)mdmf
dxm

x=a
(C.16)
One can show
δ[m](x) = (−1)mδ[m](−x)
(C.17)
∫δ[m](x − y)δ[n](y − a)dy = δ[m+n](x − a)
(C.18)
xm+1δ[m](x) = 0
(C.19)
Perhaps of more direct use is the application of these properties to the first
derivative:
∫
−1
δ´(x)f (x)dx = −f ´(0)
(C.20)
δ´(x) = −δ´(−x)
(C.21)
∫δ´(x − y)δ(y − a)dy = δ´(x − a)
(C.22)
xδ´(x) = −δ(x)
(C.23)
One can generalize the concept of a δ-function to several dimensions. For
example, we would define the three-dimensional δ-function by
∫d3r´δ(r´ − r)f (r´) = f (r)
(C.24)
Note that we could write this in Cartesian coordinates as
δ(r − r´) = δ(x − x´)δ(y − y´)δ(z − z´)
(C.25)
Such multidimensional δ-functions are of very considerable use in vector
calculus.
More detailed discussions of the Dirac δ-function and its relatives are found
in the following references.

## Further Readings

DETTMAN J. W., Mathematical Methods in Physics and Engineering, 2nd ed.,
McGraw-Hill, New York (1969).
LIGHTHILL M. J., Fourier Analysis and Generalized Functions, Cambridge University
Press, Cambridge (1959).
MESSIAH A., Quantum Mechanics, Vol. I, Wiley, New York (1965), pp. 468–470.
