# Appendix F Introduction to Laplace Transforms
<!-- source PDF pages 733-738 -->

<!-- page 717 (PDF 733) -->
# Appendix F Introduction to Laplace Transforms

F.1

## Motivation

Differential equations play a central role in the description of most scientific
phenomena. Moreover, in many cases these phenomena can be approximately
described by a particularly simple type of differential equation – namely, those
with constant coefficients. In this appendix we will try to develop one of the most
powerful tools for solving such equations: the application of integral transforms,
and more specifically, the use of Laplace transforms to solve differential
equations.
The analogy between the use of transform methods to solve differential
equations and the use of logarithms to simplify arithmetic operations is quite
striking. Suppose we wish to multiply two complicated numbers a and b together.
Then an easy way to do this is to use logarithms
a ! log a
a □ b !
“Transform”
! log a + log b !
“Invert”
! e(log a+log b) = a □ b
That is, by first taking logs we have simplified the original problem, reducing it to
a simple sum.
This is essentially the idea behind integral transform techniques. Suppose we
symbolically represent the transform operation on a function as
f (t) ! ~f (s)
Then the idea is to transform the differential equation of interest:
df
dt + ∙∙∙!
Transform
! s~f (s) + ∙∙∙!
Invert
! f (t)
In this manner, the integral transform can be used to convert this differential
equation into a simpler problem (frequently an algebraic equation) that can then
be solved rather easily for the transformed solution. We then must somehow
“invert” the transform to obtain the actual solution of interest.
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 718 (PDF 734) -->
### Example

Consider the very simple ordinary differential equation (familiar from
prompt neutron reactor kinetics):
dn
dt □
ρ
Λ

n(t) = 0;
n(0) = n0
(F.1)
Now define the Laplace transform of n(t) as
~n(s) = ∫
dte□stn(t) ≡ Lfng
(F.2)
To transform the ordinary differential equation (F.1), multiply by e□st and
integrate over t:
∫
dte□st dn
dt □
ρ
Λ

∫
dte□stn(t) = 0
or using integration by parts
s~n(s) □ n(0) □ (ρ=Λ)~n(s) = 0
but this is now just an algebraic equation that can be easily solved for
~n(s) =
n0
s □ (ρ=Λ)
(F.3)
We must now “invert” ñ(s) to find
n(t) = L□1f~n(s)g
(F.4)
By noting that
L e□at

= ∫
dte□ste□at =
s + a ) L□1
s + a

= e□at
we find
n(t) = n0L□1
s □ (ρ=Λ)

= n0exp (ρ=Λ)t

(F.5)

### Example

Integral transforms can also be applied to the solution of partial
differential equations. Consider, for example, the initial value problem for a
nonmultiplying slab in one-speed diffusion theory:
υ
@ϕ
@t = D @2ϕ
@x2 □
X
aϕ(x; t)
Intital condition :
ϕ(x; 0) = ϕ0(x)
Boundary condition :
ϕ(0; t) = ϕ(l; t) = 0
I
(F.6)
Define the Laplace transform of ϕ (x, t) with respect to t by
~ϕ(x; s) = ∫
dte□stϕ(x; t)
(F.7)

<!-- page 719 (PDF 735) -->
Now multiplying (F.6) by e□st and integrating over all times t, we find the
transformed partial differential equation becomes
υ s~ϕ(x; s) □ ϕ(x; 0)

= D d2~ϕ
dx2 □
X
a~ϕ(x; s)
Since the boundary conditions also depend on time, we must transform them to
find
~ϕ(0; s) = ~ϕ(l; s) = 0
Hence, if we regard s only as a parameter, the application of Laplace transforms
has reduced our original partial differential equation (F.6) to an inhomogeneous
ordinary differential equation in x:
D d2~ϕ
dx2 □
X
a + s
υ

~ϕ(x; s) = ϕ0(x)
Boundary condition : ~ϕ(0; s) = ~ϕ(l; s) = 0
(F.8)
We can now solve this in any of the standard ways (e.g., eigenfunction expansions
or Green’s functions) to find ~ϕ(x; s), and then invert to find
ϕ(x; t) = L□1 ~ϕ(x; s)

(F.9)
Hence, as should be apparent from these simple examples, Laplace transforms
can be used to greatly simplify the solution of differential equations by (a)
transforming the original differential equation, (b) solving the transformed
equation (which is now presumably a simpler equation such as an algebraic
equation or ordinary differential equation) for the transformed solution, and (c)
finally inverting the transformed solution to obtain the desired solution of the
original equation. It is usually a straightforward task to complete the first two
steps. The final step, that of inversion, can frequently be accomplished in a
“cookbook” fashion by merely looking up the inverse in a table of Laplace
transforms that some other fellow has had to work out. The general theory of
how to perform such inversions from scratch is important however, since the
inverses of many of the functions one encounters in practice are not tabulated.
However, since it is heavily steeped in the theory of functions of a complex
variable, we will avoid a detailed discussion of Laplace transform inversion via
contour integration here and simply refer the reader to one of several standard
texts (see Refs. [1–3]).
F.2

## “Cookbook” Laplace Transforms

We will now set up the recipes for solving differential equations with Laplace
transforms. First, we must determine just what types of equations we can consider:
a) This can be any linear differential equation (ordinary or partial) in which the
variable to be transformed runs from 0 to 1 (such as an initial value problem
in time or a half-space problem in space).

<!-- page 720 (PDF 736) -->
b) We will further restrict ourselves to the study of differential equations with
constant coefficients (i.e., the coefficients in the equation do not depend on the
variable to which we are applying the transform). This restriction can
sometimes be relaxed; however, we will not consider the more general
problem of differential equations with variable coefficients here.
We will define the Laplace transform of a function f(t) by
~f (s) = ∫
dte□stf (t)
(F.10)
There are of course some restrictions on the type of function f(t) and the ranges of
values of s for which this integral will be properly defined, but let us not worry
about details at this stage of the game.
The general scheme for transforming the differential equation we are interested
in solving is the same as before – namely, multiply by e□st and integrate over all t,
using liberal integration by parts. One then solves the resulting transformed
equation and attempts to invert the solution.
To facilitate in the preparation of a table of Laplace transforms (a cookbook),
one merely takes the transforms of as many different functions as possible. Several
useful transforms of general functions are (see Refs. [4,5]) as follows:

## □ Derivatives:

L df
dt

= s~f (s) □ f (0)
(F.11)
Recall that we obtained this by integration by parts. Further integration by parts
yields
L dnf
dtn

= sn~f (s) □ sn□1f (0) □ sn□2f ´(0) □ ∙∙∙□ f [n□1](0)
(F.12)

## □ Integration:

L ∫
t
dt´f (t´)

= 1
s
~f (s)
(F.13)

### Proof:

L ∫
t
dt´ f (t´)

= ∫
dte□st
∫
t
dt´f (t´)
= □ e□st
s ∫
t
dt´f (t´)
+ 1
s ∫
dte□stf (t)
= 1
s
~f (s)

## □ Differentiation by s:

L tf (t)
f
g = □ d~f
ds
(F.14)

<!-- page 721 (PDF 737) -->
### Proof:

d~f
ds = ∫
dtf (t) d
ds (e□st) = □∫
dte□st[tf (t)]

## □ Complex translation:

L eatf (t)

= ~f (s □ a)
(F.15)

### Proof:

∫
dteate□stf (t) = ∫
dte□(s□a)tf (t) = ~f (s □ a)

## □ Real translation:

L f (t □ a)Θ(t □ a)
f
g = e□as~f (s)
(F.16)
where Θ(t) is the step function:
Θ(t) =
1;
t □ 0
0;
t < 0

Several examples of more specific transform pairs are presented in Table F.1.
Table F.1 Some Useful Transforms
f (t)
~f (s)
s
e□at
s + a
δ(t)
δ(t □ t1)
e□st1
tn
n!
sn+1
tn□1e□at
(n □ 1)!
(s + a)n
(e□bt □ e□at)
a □ b
(s + a)(s + b)
(be□bt □ ae□at)
(b □ a)
s
(s + a)(s + b)
sin at
a
(s2 + a2)
cos at
s
(s2 + a2)
tsin at
2as
(s2 + a2)2
tcos at
(s2 □ a2)
(s2 + a2)2
Θ(t)
s

<!-- page 722 (PDF 738) -->
Several other very useful relations (see Refs. [4,5]) are as follows:

## □ Convolution theorem:

L ∫
t
dτf (t □ τ)g(τ)

= ~t(s) = f (s)g(s)
(F.17)
(This result is useful for relating the inverse of the product of two transformed
functions.)

## □ Initial value theorem:

lim
t!0 f (t) = lim
s!1 s~f (s)
(F.18)

## □ Final value theorem:

lim
t!1 f (t) = lim
s!0 s~f (s)
(F.19)
There are a number of reasonably complete tables of such transform pairs (see
Refs. [4,5]). After obtaining the transformed solution, one can then turn to such
tables in an effort to locate the desired inverse. However, in many cases it will be
necessary to proceed with a direct inversion calculation.

## References

1 P. M. MORSE and H. FESHBACH, Methods of Theoretical Physics, Vol. 1, McGraw
Hill, New York (1953), Chapter 4.
2 W. KAPLAN, Operational Methods for Linear Systems, Addison-Wesley, Reading,
MA (1962).
3 H. S. CARSLAW and J. C. JAEGAR, Operational Methods in Applied Mathematics,
Dover, New York (1948).
4 P. A. MCCOLLUM and B. F. BROWN, Laplace Transform Tables and Theorems, Holt,
Rinehart, and Winston, New York (1965).
5 F. E. NIXON, Handbook of Laplace Transforms, Prentice-Hall, Englewood Cliffs, NJ
(1960).
