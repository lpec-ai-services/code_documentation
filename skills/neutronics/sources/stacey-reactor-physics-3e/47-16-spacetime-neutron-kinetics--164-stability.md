# 16 Space–Time Neutron Kinetics — 16.4 Stability
<!-- source PDF pages 668-683 -->

<!-- page 651 (PDF 668) -->
## 16.4 Stability

In a nuclear reactor operating at steady-state conditions, an equilibrium obtains
among the interacting neutronic, thermodynamic, hydrodynamic, thermal,
xenon, and so on, phenomena. The state of the reactor is defined in terms of
the values of the state functions1 associated with each of these phenomena (e.g.,
the neutron flux, the coolant enthalpy, the coolant pressure). If a reactor is
perturbed from an equilibrium state, will the ensuing state (1) remain bounded
within some specified domain of the state functions, (2) return to the equilibrium
state after a sufficiently long time, or (3) diverge from the equilibrium state in that
one or more of the state functions takes on a shape outside a specified domain of
state functions? This is the question of stability.
In this section we extend the concepts of Section 5.9 to outline a theory
appropriate for the stability analysis of spatially dependent reactor models. First,
we consider the stability analysis of the coupled system of ordinary differential
equations that results when the spatial dependence is discretized by a finitedifference
, nodal, or other approximation. Then the extended Lyapunov theory
for the stability analysis of the coupled partial differential equations that describe
spatially continuous systems is discussed.

### Classical Linear Stability Analysis

The finite-difference, time-synthesis, nodal, or point kinetics approximations, and
the corresponding approximations to the other state function equations, may be
written as a coupled set of ordinary differential equations relating the discrete
state variables yi:
_yi(t) = f i(yi(t); . . . ; yN(t));
i = 1; . . . ; N
(16.121)
where, for instance, yi may be the neutron flux at node i and yI+j may be the
coolant enthalpy at node j. The coupling among the equations arises because the
cross sections in the neutronics equations depend on the local temperature,
density, and xenon concentration, because the temperature, density, and xenon
concentration depend on the local flux, and because neutron and heat diffusion
and coolant transport introduces a coupling among the value of the state variables
at different locations.
Equations (16.121) may be written as a vector equation,
_y(t) = f (y(t))
(16.122)
1 In a spatially dependent system, such as a nuclear reactor, the state of the system is defined in
terms of spatially dependent state functions. When the spatial dependence is discretized by one of
the approximations discussed in previous sections, the state of the system is defined in terms of
discrete state variables.

<!-- page 652 (PDF 669) -->
where the components of the column vectors y and f are the yi and fi, respectively.
The equilibrium state ye satisfies
f (ye) = 0
(16.123)
If the solution of Eq. (16.122) is expanded about ye,
y(t) = ye + ^y(t)
(16.124)
and the part of the right-hand side of Eq. (16.122) that is linear in ^y is separated
out, Eq. (16.122) may be written as
_^y(t) = h(ye)^y(t) + g(ye; ^y(t))
(16.125)
The matrix h has constant elements, some of which may depend on the
equilibrium state.
Classical linear stability analysis proceeds by ignoring the nonlinear term g in
Eq. (16.125). It is readily shown that the condition for the stability of the linearized
equations is that the real part of all eigenvalues of the matrix h are negative. To
illustrate this, apply a permutation transformation that diagonalizes h to the linear
approximation to Eq. (16.125):
PT^_y(t)P = PThPPT^y(t)P
(16.126)
since
PTP = PPT = I
(16.127)
Define X(t) = PT^y(y)P. Then the transformed equations are decoupled:
_Xi(t) = ωiXi(t);
i = 1; . . . ; N
(16.128)
where ωi are the eigenvalues of h. The solutions of these equations subject to
Xi(0) = Xi0 are
Xi(t) = Xi0eωit;
i = 1; . . . ; N
(16.129)
which may be written in vector notation as
X(t) = Γ(t)Xi0
(16.130)
where Γ(t) = diag(exp(ωit)). Hence
^y(t) = PX(t)PT = PΓ(t)Xi0PT
(16.131)
If Re{ωi} < 0, limt!1^y(t) = 0 (i.e., the state of the system returns to the
equilibrium state). If Re{ωi} > 0, one or more of the components of ^y approach
1 as t →1, and the system is unstable. Thus, stability analysis of the linearized

<!-- page 653 (PDF 670) -->
equations amounts to determining if the eigenvalues of the h matrix are in the left
(stable) or right (unstable)-half complex plane. This determination may be
accomplished most readily by Laplace transforming the linearized equation
into the frequency domain and then applying one of the methods of linear
control theory (e.g., Bode, Nyquist, root locus, Hurwitz) that have been developed
explicitly for this purpose. This methodology was applied in the stability analyses
of Chapter 5.

### Lyapunov’s Method

The method of Lyapunov attempts to draw certain conclusions about the stability
of the solution of Eq. (16.125) without any knowledge of this solution. Essential to
this method is the choice of a scalar function V(^y) that is a measure of a metric
distance of the state y = ye + ^y from the equilibrium state ye. Let ^yft; ^y0) be the
solution of Eq. (16.125) for the initial condition ^y(t = 0) = ^y0. If it can be shown
that V(^y(t; ^y0)) will be small when V(^y0) is small, then ye is a stable equilibrium
state. If, in addition, it can be shown that V(^y(t; ^y0)) approaches zero for large
times, ye is an asymptotically stable equilibrium state.
Define a scalar function V(^y) that depends on all the state variables ^yi and
which has the following properties in some region R about the equilibrium
state ye:
1) V(^y) is positive definite (i.e., V(^y) > 0 if ^y ≠0, V(^y) = 0 if ^y = 0)
2) lim^y!0V(^y) = 0, lim^y!0V(^y) = 1.
3) V(^y) is continuous in all its partial derivatives (i.e., @V/@yi exist and are
continuous for i = 1, . . . , N).
4)
_V(^y) evaluated along the solution of Eq. (16.125) is nonpositive; that is,
_V(^y) =
X
M
i=1
@V
@^yi
_^yj =
X
N
i=1
@V
@^yi
f i ≤ 0
(16.132)
A scalar function V(^y) satisfying properties 1–4 is a Lyapunov function.
Three theorems based on the Lyapunov function can be stated about the
equilibrium solution of Eq. (16.125).

### Theorem 16.1 (Stability Theorem)

If a Lyapunov function exists in some region
R about ye, this equilibrium state is stable for all initial perturbations in R (i.e., for
all initial perturbations^y0 in R, the solution of Eq. (16.125), y(t; ^y0), remains within
the region R for all t > 0).

### Theorem 16.2 (Asymptotic Stability Theorem)

If a Lyapunov function exists
in some region R about ye, and in addition _V evaluated along the solution of
Eq. (16.125) is negative definite ( _V < 0 if ^y ≠0,
_V = 0 if ^y = 0) in R, this
equilibrium state is asymptotically stable for all initial perturbations in R (i.e.,
for all initial perturbations ^y0 in R, the solution of Eq. (16.125) is ^y(t; ^y0) = 0 after a
sufficiently long time).

<!-- page 654 (PDF 671) -->
### Theorem 16.3 (Instability Theorem)

If a scalar function V(^y) which has
properties 1 to 3 exists in a region R, and _V evaluated along the solution of Eq.
(16.125) does not have a definite sign, the equilibrium state ye is unstable for initial
perturbations in R (i.e., for initial perturbations^y0 in R, the solution of Eq. (16.125),
^y(t; ^y0), does not remain in R for all t > 0).
Mathematical proofs of these theorems can be constructed. Rather than repeat
these proofs, which may be found in the literature (e.g., Ref. [2]), it is more
informative to consider a topological argument. Properties 1 to 3 define a concave
upward surface (the function V) in the phase space defined by the ^yi. This surface
has a minimum within the region R at ^y1 = ∙∙∙= ^yN = 0 by property 1, and
increases monotonically in value as the ^yi increase, by properties 2 and 3. Thus
contours can be drawn in the hyperplane of the ^yi representing the locus of points
at which V has a given value. These contours are concentric about the equilibrium
state ^yi = 0, i = 1, . . . , N. Proceeding outward from this origin, the value of V
associated with each contour is greater than the value associated with the previous
contour. In other words, V (y) is a bowl in the hyperspace of the yi, with center at
^yi = 0, i = 1, . . . , N.
The outward normal to those contours is
X
N
i=1
@V
@^yi
i
where i denotes the unit vector in the direction in phase space associated with the
state variable ^yi. The direction in which the state of the system is moving in phase
space is given by
X
N
i=1
_yii =
X
N
i=1
f ii
(16.133)
For stability, the direction in which the state of the system is moving must
never be toward regions in which V is larger (i.e., never away from the equilibrium
state):
X
N
i=1
@V
@^yi
i
!
?
X
N
j=1
f jj
!
=
X
N
i=1
@V
@^yi
f i ≤ 0
(16.134)
For asymptotic stability, the state of the system must always move toward
regions in which V is smaller (i.e., always move toward the equilibrium state).
Thus the inequality must always obtain in the foregoing relation. If the system can
move away from the equilibrium state into regions of larger V, the ≤ is replaced by
>in the foregoing relation and the equilibrium state is unstable.

<!-- page 655 (PDF 672) -->
The Lyapunov method yields the same results obtained in the preceding
section in the limit in which the nonlinear terms are small. The function
V(^y) = ^yT^y =
X
N
i=1
(^yi)2
(16.135)
satisfies properties 1 to 3. Making use of Eq. (16.125) yields
V_(^y) =
X
N
i=1
@V
@^yi
^yi = 2
X
N
i=1
^yi _^yi = 2^yT _^y = 2 ^yTh^y + ^yTg

(16.136)
If the region R is defined such that
j^yTh^yj > j^yTgj
a sufficient condition for _V to be negative definite in R is that ^yTh^y is negative
definite, a sufficient condition for which is that the eigenvalues of h have negative
real parts. This is the same result obtained in the linear analysis of the preceding
section. In this case, the Lyapunov method provides, in addition, the region R
within which the linear analysis is valid.
In applying the Lyapunov method, construction of a suitable Lyapunov
function is the main consideration. Because the Lyapunov function for a system
of equations is not unique, the analysis yields sufficient, but not necessary,
conditions for stability.

### Lyapunov’s Method for Distributed Parameter Systems

A more basic characterization of a reactor system is in terms of spatially
distributed state functions, rather than discrete state variables. These state
functions satisfy coupled partial differential equations, which may be written
_yi(r; t) = f i y1(r; t); . . . ; yN(r; t); r

;
i = 1; . . . N
(16.137)
where yi is a state function (e.g., neutron group flux) and fi denotes a spatially
dependent operation involving scalars and spatial derivatives on the state
functions. These equations may be written
_y(r; t) = f (y(r; t); r)
(16.138)
where y is a column vector of the yi and f is a column vector of the operations
denoted by the fi.
The extension of Lyapunov’s methods to systems described by state functions
involves the choice of a functional that provides a measure of the distance of the
vector of state functions y from a specified equilibrium state, yeq. The distance
between two states ya and yb, d[ya, yb], is defined as the metric on the product

<!-- page 656 (PDF 673) -->
state function space consisting of all possible functions of position that the
component state functions can take on.
An equilibrium state yeq(r) satisfying
f (yeq(r); r) = 0
(16.139)
is stable if, for any number ε > 0, it is possible to find a number δ > 0 such that
when
d[y0(r); yeq(r)] < δ
then
d[y(r; t; y0)]; yeq(r)] < ε
for t □ 0
(16.140)
where y(r, t; y0) is the solution of Eq. (16.138) with the initial condition
y(r, 0) = y0(r). If in the limit of large t, the distance d[y(r, t; y0), yeq] approaches
zero, then yeq is asymptotically stable.

### Theorem 16.4 (Stability Theorem)

For an equilibrium state yeq(r) to be
stable, it is necessary and sufficient that in some neighborhood of yeq(r) that
includes the equilibrium state there exists a functional V [y] with the following
properties:
1) V is positive definite with respect to d [y, yeq]; that is, for any C1 > 0, there exists
a C2 > 0 depending on C1 such that when d[y, yeq] > C1, then V[y] > C2 for all
t □ 0, and limd[y;yeq]!0V[y] = 0.
2) V is continuous with respect to d[y, yeq]; that is, for any real ε > 0, there exists a
real δ > 0 such that V [y ] < ε for all y in the state function space for 0 < t < 1,
when d [y0, yeq ] < δ0.
3) V [y] evaluated along any solution y of Eq. (16.138) is nonincreasing in time for
all t > 0 provided that d[y0, yeq] < δ0, where δ0 is a sufficiently small positive
number.

### Theorem 16.5 (Asymptotic Stability Theorem)

If, in addition to these three
conditions, V [y] evaluated along any solution to Eq. (16.138) approaches zero for
large t, the equilibrium state is asymptotically stable.
The same type of topological arguments made above in support of the
theorems for the discrete representation of spatial dependence by coupled
ODES are appropriate here, if the state space is generalized to a state function
space. Construction of a suitable Lyapunov functional is the essential aspect of
applying the theory of this section. Although the conditions cited in the theorems
are necessary and sufficient for stability, the V-functional chosen may result in
more restrictive stability criteria than would be obtained from another V-
functional. Thus, stability analyses employing Lyapunov functionals yield only
sufficient conditions for stability.

<!-- page 657 (PDF 674) -->
### Control

An intended change in the operating state of a nuclear reactor is produced by a
control action (e.g., withdrawing a bank of control rods, increasing the coolant
flow). The nature of the change in operating state depends on the control action,
of course, and a great deal of practical experience exists on how to effect a desired
change. However, in some cases the intuitive control action can exacerbate, rather
than correct, a problem – the control-induced xenon spatial oscillations in the
large production reactors being a good example. The methodology of control
theory has found some application in nuclear reactor control, and a brief review is
provided in this section.

### Variational Methods of Control Theory

When discrete spatial approximations (e.g., nodal, finite-difference) are employed,
the dynamics of a spatially dependent nuclear reactor model are described by a
system of ordinary differential equations
_yi(t) = f i(y1; . . . ; yN; u1; . . . ; uR);
i = 1; . . . ; N
(16.141)
with the initial conditions
yj(t = t0) = yi0;
i = 0; . . . ; N
(16.142)
The yi are the state variables (e.g., nodal neutron flux, temperature) and the ur are
control variables (e.g., control rod cross section in a node). Equation (16.141) may
be written more compactly by defining vector variables y, u, and f:
_y(t) = f (y(t); u(t))
(16.143)
Many problems in control may be formulated as a quest for the control vector
u∗that causes the solution of Eq. (16.143), y∗, to minimize a functional:2
J[y] = ∫
tf
t0
dt F(y(t); _y(t))
(16.144)
This control problem may be formulated within the framework of the classical
calculus of variations by treating the control variables as equivalent to the state
2 Functionals of this form may arise when the objective of the control program is to correct a flux
perturbation in such a manner as to minimize the deviation from the nominal flux distribution, at
the same time minimizing the rate of change of local flux densities. Other typical control problems
are those in which the objective is to attain a given final state in a minimum time; a functional with
F = 1 and an additional term that provides a measure of the deviation from the specified final state is
appropriate in this case.

<!-- page 658 (PDF 675) -->
variables. The theory of the calculus of variations is restricted to variables that are
continuous in time, which limits the admissible set of control variables.
The system equations are treated as constraints or subsidiary conditions, and
are included in the functional with Lagrange multiplier variables:
J´[y; u; λ] = ∫
tf
t0
dt F(y(t); _y(t)) +
X
N
i=1
λi(t)f _yi(t) □ f i(y(t); u(t))g
"
(16.145)
Variations of the modified functional J´ (with respect to each yi and ur) are
required to vanish at the minimum:
δJ´ = 0 = ∫
tf
t0
dt
X
N
i=1
@F
@yi
δyi + @F
@ _yi
δ _yi + λiδ _yi □
X
N
j=1
λi
@f j
@yi
δyi
"
(
□
X
R
r=1
λi
@f i
@ur
δur
#)
(16.146)
Integrating the δ _yi terms by parts and using the initial conditions to set δyi(t0) = 0,
this expression becomes
δJ´ = 0 = ∫
tf
t0
dt
X
N
i=1
@F
@yi
□ @
@t
@F
@ _yi
□ _λi □
X
N
j=1
λi
@f j
@yi
"
δyi □
X
R
r=1
λi
@f i
@ur
δur
(
)
+
X
N
i=1
λi + @F
@ _yi

δyi
t=tf
(16.147)
In order that Eq. (16.147) be satisfied for arbitrary (but continuous) variations
δyi and δur, it is necessary that
_λi(t) = □
X
N
j=1
λj(t)
@f j
@yi
(y; u)
+ @F
@yi
(y; f ) □ @
@t
@F
@ _yi
(y; f )

;
i = 1; . . . ; N
(16.148)
X
N
i=1
λi(t) @f i
@ur
(y; u) = 0;
r = 1; . . . ; R
(16.149)
and that λi satisfy the final conditions
λi(tf ) + @F
@ _yi
tf
= 0;
i = 1; . . . ; N
(16.150)

<!-- page 659 (PDF 676) -->
Equations (16.141), (16.148), and (16.149) and (16.149) must be solved
simultaneously, subject to the initial conditions of Eqs. (16.142) and the final
conditions of Eq. (16.150), for the optimal controls u∗
r (t) and the optimal
solutions y∗
i (t).
In many problems, additional constraints are placed on the allowable values
that may be taken on by the state variables and control variables. Constraints of
the form
ϕm(y(t); u(t)) = 0;
m = 1; . . . ; M < N
or
ϕm(y(t); _y(t); u(t); _u(t)) = 0;
m = 1; . . . ; M < N
may be added to the functional of Eq. (16.144) with Lagrange multiplier variables
and treated in the same fashion as before. Equations for additional Lagrange
multiplier variables and the additional constraint equations are included with
Eqs. (16.141), (16.148), and (16.149) and (16.149) in this case.
When integral constraints of the form
∫
tf
t0
dt ϕm(y(t); _y(t); u(t); _u(t)) = 0;
m = 1; . . . ; M < N
are present, the functional of Eq. (16.144) is modified with Lagrange multiplier
constants ωm,
J ! ^J = ∫
tf
t0
dt
F +
X
M
m=1
ωmϕm
!
= ∫
tf
t0
dt ^F
(16.151)
and the derivation proceeds as before with F ! ^F. In addition to Eqs. (16.141),
(16.148), and (16.149), and (16.149), the constraint equations and expressions for
the ωm are obtained.
Inequality constraints (e.g., maximum control rod shim rates) are encountered
frequently. Although these can sometimes be reduced to equivalent equality
constraints of one of the three types discussed, they generally constitute a class of
problems that are difficult to treat within the framework of the calculus of
variations. Another class of such problems is those for which the optimal control
is discontinuous.

### Dynamic Programming

An alternative treatment of the variational problem that circumvents the requirement
for continuous control variables is provided by dynamic programming.
Consider the problem of determining the control vector u∗(t) that causes the

<!-- page 660 (PDF 677) -->
solution y∗(t) of Eq. (16.143) to minimize the functional of Eq. (16.144), subject to
constraintsontheallowablevaluesofthecontrolvariablethatmayberepresentedby
u(t) ∈Ω(t)
(16.152)
To develop the dynamic programming formalism, consider the functional of
Eq. (16.144) evaluated between a variable lower limit (t, y(t)) and a fixed upper
limit (tf, y(tf)). Define the minimum value of this functional as S, a function of the
lower, variable limit (t, y(t)):
S(t; y(t)) = min
u ∈Ω ∫
tf
t
dt´ F(y(t´); _y(y(t´); u(t´)))
(16.153)
In writing Eq. (16.153), _y is written as an explicit function of y and u to indicate
that Eq. (16.143) must be satisfied in evaluating the integrand.
By definition of S, for Δt > 0,
S(t; y(t)) ≤ S(t + Δt; y(t + Δt)) + ∫
t+Δt
t
dt´F(y(t´); _y(y(t´); u(t´)))
(16.154)
where y(t + Δt) and y(t) are related by Eq. (16.143); that is,
y(t + Δt) = y(t) + Δt f (y(t); u(t)) + O(Δt2)
(16.155)
For the optimal choice of u(t´) = u∗in the interval t ≤ t´ ≤ t + Δt, the equality
obtains in Eq. (16.154). Approximating the integral in Eq. (16.154) by taking the
integrand constant at its value at t, this equation becomes3
S(t; y(t)) =
min
u(t) ∈Ω(t) S(t + Δt; y(t + Δt)) + Δt F y(t); f y(t); u(t)
)
)
[
]
(16.156)
Equation (16.156) can be solved by retrograde calculation, starting with the
final condition
S(tf ; y(tf )) = min
u ∈Ω ∫
tf
tf
dt´ F(y; _y) = 0
(16.157)
In each step of the retrograde solution, the optimal manner to proceed from each
possible state y(t) to time tf is computed. Thus, when the initial time is reached,
3 In Eq. (16.156), the minimization is with respect to the values of the control vector at time t.
These values are assumed constant over the interval t to t + Δt. On the other hand, the minimization
in Eq. (16.153) is with respect to the values taken on by the control vector at all times t´, t ≤ t´ ≤ tf.

<!-- page 661 (PDF 678) -->
the optimal control at each discrete time and the corresponding sequence of
states constituting the optimal trajectory are known.

### Pontryagin’s Maximum Principle

When a Taylor’s series expansion of the first term on the right of Eq. (16.156) is
made, this equation becomes
0 = min
u(t) ∈Ω(t)
@S
@t (t; y(t)) +
X
N
i=1
@S
@yi
(t; y(t))f i(y(t); u(t))
"
+F(y(t); f (y(t); u(t)))]
(16.158)
Define the variables
ψi(t) ≡ □ @S
@yi
(t; y(t));
i = 1; . . . ; N
(16.159)
ψN+1(t) ≡ □ @S
@t (t; y(t))
(16.160)
With these definitions, Eq. (16.158) becomes
0 =
min
u(t) ∈Ω(t) □ψN+1(t) □
X
N
i=1
ψi(t)f i(y(t); u(t)) + F(y(t); f (y(t); u(t)))
"
which may be written as
0 =
max
u(t) ∈Ω(t) ψN+1(t) +
X
N
i=1
ψi(t)f i(y(t); u(t)) □ F(y(t); f (y(t); u(t)))
"
(16.161)
This is the maximum principle of Pontryagin.
When the vector u(t) takes on its optimal value, derivatives of the quantity
within the square brackets with respect to t and yi must vanish, which requires
that
@ψN+1
@yj
+
X
N
i=1
@ψi
@yj
f i = □
X
N
i=1
ψj
@f i
@yj
+
@F
@yj
+
X
N
i=1
@F
@ _yi
@f i
@yj
!
;
j = 1; . . . ; N
@ψN+1
@t
+
X
N
i=1
@ψi
@t f i = □
X
N
i=1
ψi
@f i
@t

<!-- page 662 (PDF 679) -->
Using the identities
dψj
dt = □
X
N
i=1
@2S
@yi@yj
f i □ @2S
@t@yj
=
X
N
i=1
@ψi
@yj
f i + @yN+1
@yj
;
j = 1; . . . ; N
dψN+1
dt
= □
X
N
i=1
@2S
@yi@t f i □ @2S
@t2 =
X
N
i=1
@ψi
@t f i + @ψN+1
@t
these equations become
dψj
dt = □
X
N
i=1
ψi
@f i
@yj
+
@F
@yj
+
X
N
i=1
@F
@ _yi
@f i
@yj
!
;
j = 1; . . . ; N
(16.162)
dψN+1
dt
= □
X
N
i=1
ψi
@f i
@t
(16.163)
Appropriate final conditions for the ψi and ψN+1 can be shown to be
ψ1(tf ) = ∙∙∙= ψN(tf ) = ψN+1(tf ) = 0
(16.164)
Thus, Eqs. (16.141), (16.161), (16.162), and (16.163) are solved simultaneously,
subject to the initial and final conditions of Eqs. (16.142) and (16.164),
respectively.
The computational procedure for solving either the calculus of variations or
maximum principle equations is generally iterative. At t = t0, the yi are known
from the initial conditions. When the maximum principle formulation is used,
initial values of ψi are guessed, and the initial value of the control variables are
determined from Eq. (16.161). Then the yi and ψi are calculated at t0 + Δt from
Eqs. (16.141) and (16.162) and (16.163) and the control is found from Eq. (16.161),
and so on. This procedure is repeated in small time increments until the final time
tj. Then ψi(tf) and ψN+1 (tf) are compared with the final conditions:
ψ1(tf ) = ∙∙∙= ψN(tf ) = ψN+1(tf ) = 0
and the initial values of ψi and ψN+1 are changed and the entire process is
repeated. This is continued until a set of initial values ψi (t0) and ψN+1 (t0) are
found that yield the correct final values.

### Variational Methods for Spatially Dependent Control Problems

The basic description of the transient neutron flux and temperature distributions
within a nuclear reactor is in terms of partial differential equations. It is not clear
that the optimal control computed by first reducing these equations to ordinary

<!-- page 663 (PDF 680) -->
differential equations by discretizing the spatial variable and then using the
methods above is the same as would be obtained if the optimal control were
determined directly from the partial differential equation description of the
reactor dynamics. The variational formalism can be extended to the partial
differential equation description of the reactor dynamics.
The state of the system is specified in terms of state functions yi (r, t) rather than
discrete state variables as previously. The function space Γi, consisting of all
possible functions of position that the state function yi can take on, is a
component function space, and the product space Γ = Γ1 ⊗Γ2 ⊗∙∙∙⊗ΓN
of all such component function spaces is the state function space on which the
vector state function y = (y1, . . . , yN) is defined. Similarly, the vector control
function u = (u1, . . . , uR) is defined on the product space of the component
function spaces defined by all possible functions of position that the control
functions ur can take on. The distance between two states ya and yb is defined as
the metric on Γ.
Equations for nuclear reactor dynamics can be written in the form
_yi(r; t) = Li(r)yi(r; t) + f i(y; u)
yi(r; t0) = yi0(r)
yi(R; t) = 0;
i = 1; . . . ; N
(16.165)
where yi denotes a state function, Li contains a spatial differential operator
acting on yi, and fi is a spatially dependent function of y and u. The outer
boundary of the reactor is denoted by R. These equations may be written in
matrix form:
_y(r; t) = L(r)y(r; t) + f (y; u)
y(r; 0) = y0(r);
y(R; t) = 0
(16.166)
Many control problems may be formulated as the quest for the control
vector function u for which the solution of Eq. (16.165) minimizes a
functional
J[y; u]∫
tf
t0
dt∫V
dr F(y(r; t); _y(r; t))
(16.167)
The standard calculus-of-variations formulation of this problem begins by
adding Eq. (16.166) to the integrand of Eq. (16.167) with a Lagrange multiplier
vector function λ(r, t) = (λi, . . . , λN):
J´[y; u; λ] = ∫
tf
t0
dt∫V
dr[F(y; _y) + λT( _y □ Ly □ f (y; u))]
(16.168)

<!-- page 664 (PDF 681) -->
The control functions ur are treated in the same fashion as the state functions yi.
Next, the variation of J´ is required to vanish:
δJ´ = ∫
tf
t0
dt∫V
dr
X
N
i=1
@F
@yi
δyi + @F
@ _yi
δ _yi + λiδ _yi □ λiLiδyi

□
X
N
j=1
λi
@f i
@yj
δyj □
X
R
r=1
λi
@f i
@ur
δur
!
= 0
Integration by parts of the terms involving δ _yi and Li, δyi
4 and use of the initial
conditions δyi(r, t0) = 0 leads to
δJ´ = ∫
tf
t0
dt∫V
dr
X
N
i=1
δyi
@F
@yi
□ @
@t
@F
@ _yi
□ _λi □ L+
i λi □
X
N
j=1
λj
@f i
@yi
!
"
□
X
R
r=1
λi
@f i
@ur
δur
+ ∫V
dr
X
N
i=1
@F
@ _yi
δyi
t=tf
+∫V
dr
X
N
i=1
λiδyi
t=tf
+ ∫
tf
t0
dt
X
N
i=1
Pi(λi) = 0
(16.169)
In arriving at Eq. (16.169), the adjoint operator L+
i and the bilinear concomitant Pi
are defined by the relation
∫V
dr λiLiδyi = ∫V
dr δyiL+
i λi + Pi(λi)
(16.170)
δJ´ must vanish for arbitrary variations of yi and ur, which requires that the
Lagrange multiplier functions satisfy the partial differential equations
_λi(r; t) = □L+
i (r)λi(r; t) □
X
N
j=1
λj(r; t)
@f j(y; u)
@yi
+ @F(y; _y)
@yi
□ @
@t
@F(y; _y)
@ _yi

;
i = 1; . . . ; N
(16.171)
the final conditions
λi + @F
@ _yi

t=tf
= 0;
i = 1; . . . ; N
(16.172)
4 Commutability of the variational operator δ and the operators @/@t and Li imply an assumption of
continuous variations δyi, as does the existence of the integrals involving these terms.

<!-- page 665 (PDF 682) -->
and the boundary conditions
Pi(λi(R; t)) = 0;
i = 1; . . . ; N
(16.173)
In addition,
X
N
i=1
λi(r; t) @f i(y; u)
@ur
= 0;
r = 1; . . . ; R
(16.174)
must be satisfied.
In this formulation, the ur, as well as the yi, are treated as continuous functions.
This imposes artificial restrictions on the ur. In some problems the control is
discontinuous.

### Dynamic Programming for Spatially Continuous Systems

Proceeding as discussed, the dynamic programming formalism is developed by
considering the minimum value of the functional of Eq. (16.167) evaluated between
a fixed upper limit and a variable lower limit as a function of the lower limit:
S(t; y(r; t)) = min
u ∈Ω ∫
tf
t
dt´
∫V
dr F(y(r; t´); _y(y(r; t´); u(r; t´)))
(16.175)
In writing Eq. (16.175), the dependence of the integrand upon Eq. (16.166) is
shown implicitly, and any constraints on the control vector function are implied
by u ∈Ω. By definition,
S(t; y(r; t)) ≤ S(t + Δt; y(r; t + Δt))
+∫
t+Δt
t
dt´
∫V
dr F(y(r; t´); _y(y(r; t´); u(r; t´)))
For the optimal control, the equality obtains. Approximating the integral over
time, this becomes5
S(t; y(r; t)) = min
u(t) ∈Ω(t) S(t + Δt; y(r; t + Δt))
[
+Δt∫V
dr F(y(r; t); _y(y(r; t); u(r; t)))

(16.176)
Equation (16.176) is the dynamic programming algorithm for the partial differential
equation description of reactor dynamics. It is solved retrogressively, with
5 The minimization in Eq. (16.175) is with respect to the control vector function over the time
interval t ≤ t´ ≤ tf, whereas the minimization in Eq. (16.176) is with respect to the control vector
function evaluated at time t.

<!-- page 666 (PDF 683) -->
the final condition
S(tf ; y(r; t)) = 0
(16.177)
which is apparent from the defining Eq. (16.175).

### Pontryagin’s Maximum Principle for a Spatially Continuous System

Using a Taylor’s series expansion
S(t + Δt; y(r; t + Δt))
= S(t; y(r; t)) + Δt @S
@t (t; y(r; t))
+ Δt∫V
dr
X
N
i=1
@S
@yi
(t; y(r; t)) Li(r)yi(r; t) + f i(y(r; t); u(r; t))

Eq. (16.176) becomes
0 = min
u(t) ∈Ω(t)
@S
@t (t; y(r; t)) +
X
N
i=1 ∫V
dr @S
@yi
(t; y(r; t))
(
□ [Li(r)yi(r; t) + f i(y(r; t); u(r; t))]
+ ∫V
dr F(y(r; t); _y(y(r; t); u(r; t)))

(16.178)
Define the functions
ψi(r; t) = □ @S
@yi
(t; y(r; t));
i = 1; . . . ; N
(16.179)
ψN+1(r; t) = □ @S
@t (t; y(r; t))
(16.180)
Then Eq. (16.178) becomes
0 = maxu(t) ∈Ω(t)
ψN+1(r; t)
(
+
X
N
i=1 ∫V
dr ψi(r; t)[Li(r)yi(r; t) + f i(y(r; t); u(r; t); )]
□ ∫V
dr F(y(r; t); _y(y(r; t); u(r; t)))

(16.181)
