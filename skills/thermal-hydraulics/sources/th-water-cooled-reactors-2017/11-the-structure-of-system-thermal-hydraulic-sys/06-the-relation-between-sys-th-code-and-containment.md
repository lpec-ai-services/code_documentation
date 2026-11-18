# The relation between SYS-TH code and containment
<!-- source PDF pages 28-28 -->

<!-- page 666 (PDF 28) -->
many transfer terms of the equations like wall friction and interfacial friction can induce
sufficient dissipation to stabilize the low frequency void waves. This point of view requires
cells large enough to prevent instability through numerical diffusion. However, when
decreasing the mesh size, numerical diffusion is decreased and the possible unstable nature
of equation is revealed. In this approach, no convergence in cell size is possible.
l
CATHARE and ATHLET use hyperbolic equations (this is demonstrated at least for the 1-D
module). Using the added mass force the fi
∂αv
∂z term is justified by the physics of two-phase
flow. The expression for fi is clearly derived in stratified flow (Bestion and Serre, 2012) and
plays an important role. It is not well known for all two-phase flow regimes and can only be
approximated. A condition is added that these terms make the system hyperbolic. This
method guaranties the well posedness and allows mesh convergence without creating
instabilities.
This question is still a subject of controversy between two communities.
l
A mathematical community does not accept the numerical regularization adopted in some
codes and do not accept the physical regularization by imposing an “arbitrary” condition on
the fi
∂αv
∂z term. Some of them prefer to use a two-pressure seven-equation model which is
unconditionally hyperbolic.
l
The engineering community accepts either the numerical or the physical regularization. The
advocates of the physical regularization argue that the differential closure terms are physically
based even if no universal model exists, and that it is nonsense to study the hyperbolicity
of the six-equation single pressure model or the two-pressure seven-equation
model without considering any of the differential closure terms.
SYS-TH code developers belong to the second community which did not observe
any code failure due to predicted instabilities which could be attributed to
nonhyperbolicity after having simulated a huge number of real two-phase flow situations
during decades. They prefer to focus on many other real difficult problems they
are obliged to face in two-phase flow modeling. Some consider discussions on hyperbolicity
are like discussions on “How many angels can dance on the head of a pin?”
(in France one would say “discussions on the gender of angels”).
11.6
The relation between SYS-TH code and containment
Safety analyses should prove that the containment integrity is preserved. This may be
challenged by a high internal pressure, by external events, such as earthquakes,
flooding, tsunamis, plane crash, and fire. In the case of severe accidents, there may
be hydrogen explosion, steam explosion, and corium-concrete interaction.
As far as DBA are concerned, containment thermalhydraulics is often decoupled
from reactor thermalhydraulics, at least during the short-term cooling. In all LOCAs,
as long as the break flow is a choked flow, it is independent from the containment
pressure. One can then simulate the reactor behavior with a system code, then simulate
the containment behavior using dedicated containment codes, the break flow being a
