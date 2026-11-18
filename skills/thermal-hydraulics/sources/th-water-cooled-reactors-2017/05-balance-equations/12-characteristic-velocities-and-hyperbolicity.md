# Characteristic velocities and hyperbolicity
<!-- source PDF pages 65-67 -->

<!-- page 231 (PDF 65) -->
equation are valid. When some simplifications are not justified a full two-fluid
6-equation model may have better capabilities.
In situations where inertial forces are not negligible compared to buoyancy, drag,
and friction forces, the drift flux may be significantly worse that the full 6-equation
model. For example:
l
Droplet flow: a water droplet created at a quench front during a core reflooding process is
entrained by steam but it does not reach an equilibrium slip within the core.
l
Stratified flow: in a stratified flow, due to a weak coupling between phases, many situations
cannot be predicted precisely by an algebraic slip since the Afi
∂αv
∂z term is not negligible and
also some acceleration terms may play a significant role in the phase slip.
l
Transient flow: when ∂
∂t ffi0 is no more valid in cross-momentum equation, the algebraic slip
relation is not valid.
l
Nonestablished flow: when ∂αv
∂z ffi0; ∂Vk
∂z ffi0 is no more valid in cross-momentum equation,
the algebraic slip relation is not valid.
l
High condensation and flashing flows: such flows are usually accelerating flows and the
term ΓivVi is no more negligible.
5.12
Characteristic velocities and hyperbolicity
The notion of well-posedness was introduced by Hadamard in his analysis of the
nature
of
mathematical
modeling.
According
to
Hadamard’s
classification,
well-posedness requires the existence and uniqueness of the solution of the model
and that the solution depends in continuous fashion on the initial and boundary data.
This requisite is induced by the fact that it is necessary to ensure that a small perturbation
in the data should give rise to a small variation of the solution at any point of the
domain at a finite distance from the boundaries.
A first-order conservative set of PDE is well posed if and only if it is hyperbolic
. As shown in Sections 5.4 and 5.7 the 1-D systems of equations for single
phase and for two-phase flow are not first order since there are diffusion terms.
However, they are often neglected, and the system becomes a first-order conservative
set of PDE.
A set of PDEs as a function of time and space is said hyperbolic when all the roots
of the characteristic equation are real.
More precisely, let a 1-D system of equation be written in the following form:
A∂X
∂t + B∂X
∂z = C
X is the vector of state variables; A, B are matrices and C is the vector of sources/sinks.
The characteristic equation is
Det B−λA
ð
Þ = 0

<!-- page 232 (PDF 66) -->
In the 1-D 1-phase 3-equation model this is a third-order polynomial function with
three roots:
λ1 = V is the transport velocity of enthalpy
λ2,3 = V □Cs are the propagation velocities of pressure (sound) waves.
Cs2 =
∂ρ
∂P
(
S
is the celerity is related to the compressibility of the fluid and is usually considered
as an isentropic compressibility since time scales of pressure fluctuations are small
compared to heat conduction time scales.
In the 1-D two-fluid 6-equation model this is a sixth order polynomial function with
six roots.
When solving this equation for a 1-D two-fluid 6-equation model, one obtains:
λ1 = Vg is the transport velocity of gas enthalpy,
λ2 = Vl is the transport velocity of liquid enthalpy,
λ3,4 = Wα □Cα are the propagation velocities of void waves,
λ5,6 = Ws □Cs are the propagation velocities of pressure (sound) waves.
A problem was raised when the two-fluid single pressure set of equation was found not
hyperbolic when no closure law uses partial derivatives. In particular the propagation
velocities of void waves may be imaginary. This may induce an unstable void wave
which increases in amplitude very rapidly. Such a system could not be used in any
numerical tool.
Then it was observed that terms like the added mass force or the fi
∂αv
∂z term can
change the nature of the system and make it hyperbolic. It was also found that a nonhyperbolic
system of equations could be solved in some codes without being unstable.
From the initial problem two new problems arise:
1. Should a nonhyperbolic system of equations be prohibited in two-fluid modeling?
2. What way should be followed to make the two-fluid model hyperbolic?
Different answers were given to both questions.
The second-order diffusive terms that have been neglected in the establishment of
the 6-equation model would have made the system parabolic and thus probably well
posed. At least they can stabilize highest frequency waves. Also many transfer terms
of the equations like wall friction and interfacial friction can induce dissipation which
may stabilize the lower frequency waves but it is not demonstrated that this is sufficient
. A complex stability analysis would be necessary which is not currently available
. Two answers to question 1 were given:
l
A very pragmatic point of view has been developed: the second-order diffusive terms that
have been neglected in 6-equation model are small compared to numerical diffusion, and the
cell size used is such that there is no need to add this second-order terms. This point of view
requires cells large enough to prevent instability through numerical diffusion. However,
when decreasing the mesh size, numerical diffusion is decreased and the possible unstable
nature of equation is revealed. In this approach, no convergence in cell size is possible.
l
Although diffusion terms could stabilize high-frequency waves, it is more convenient to use
a system of equation which is hyperbolic without diffusion.

<!-- page 233 (PDF 67) -->
For the second answer to question 1 there are also two answers to question 2:
l
Using the added mass force and the fi
∂αv
∂z to guaranty the hyperbolicity is artificial and one
should use an unconditionally hyperbolic system of equation without such closure differential
terms. For example a 7-equation model with two phasic pressures is unconditionally
hyperbolic. A seventh equation is added (usually a void fraction equation) leading to a
new and very difficult closure problem which can be understood as finding a model for a
relaxation time to the single pressure model, this relaxation time being very difficult to
understand and to measure.
l
Using the added mass force and the fi
∂αv
∂z term is justified by the physics of two-phase flow.
However, the expression for fi is not known for all flow regimes in two-phase flow and can
only be approximated after some simplifying assumptions are made. Adding a condition that
these terms make the system hyperbolic may be justified if the condition remains compatible
with the limited understanding of the complex physics. This position is illustrated here below.
The characteristic equation of the CATHARE 1-D 6-equation model was calculated
by making some simplifying assumptions.
Both the added mass force (with a coefficient β) and the fi
∂αv
∂z terms are used in
momentum equations. When calculating the two characteristic velocities relative to
void fraction waves, it was assumed that the two densities are constant, (infinite sound
speed) and only mass and momentum equations are used. The following velocities
were found:
λ3,4 = W □Cα
Wα =
αlρam
g VG + αGρam
l Vl
αlρam
g + αGρam
l
Cα
2 =
fiρam
m −α 1−α
ð
Þρam
l ρam
g
VG −Vl
ð
Þ2
ρam2
m
With:
ρam
k = ρK + βρm
ρm = αGρG + αLρL
ρam
m = αLρam
g + αGρam
l
One can see that the void waves velocities can only be real if Cα2 > 0 which gives the
condition:
fi > fihyp =
α 1−α
ð
Þρam
l ρam
g
VG −Vl
ð
Þ2
ρam
m
