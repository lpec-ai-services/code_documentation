# Special process models — Models in system codes
<!-- source PDF pages 7-7 -->

<!-- page 601 (PDF 7) -->
There are few documents (Saha, 1978; Elias and Lellouche, 1994; Levy, 1999;
Sokolowski et al., 2012; Brittain and Karwat, 1982; Miller, 2010; OECD/NEA/
CSNI, 1980) that describe various models and tests available for critical flows.
Elias and Lellouche (1994) listed 66 tests with different lengths, diameters, and pressures
. However, only 42 data sets were usable. The diameter of broken pipe varied
from very small at 4 mm to large at 76 mm. The length varied from no pipe to
1700 mm pipe. Marviken provided a data set that was much closer to reactor system.
The diameter of the pipe varied from 200 to 500 mm and length varied from 166 to
1800 mm. Elias and Lellouche’s study indicated that none of the model did well with
the data. The scatter plots indicated that most of the data were outside of ·10% of
mean line.
Saha (1978) had earlier reviewed various models and concluded the following:
1. The HEM underpredicts the critical flow rates for short pipes and near liquid saturation or
subcooled upstream conditions.
2. The equilibrium slip models of Fauske, Moody, and others, although successful for long
tubes, underpredicted the critical flow rates for short pipes. This is particularly true if the
upstream condition is subcooled or near saturation.
3. Effects of thermal nonequilibrium must be taken into account for short pipes. However, it is
not clear whether the pipe length, L, or the pipe length-to-diameter ratio, L/D, or both are
important in determining the effects of thermal nonequilibrium.
4. At present, there is no general model or correlation for critical flow, which is valid for a
broad range of pipe lengths, pipe diameters, and upstream conditions including subcooled
liquid. The more sophisticated the model used for a more precise design, the more prudent
it is to consider some data benchmarking under similar conditions.
There has not been any systematic scaling study for critical flow phenomenon. The
subphenomena that affect the critical mass flux have been identified but the data
have not been compiled with dimensionless groups representing subcooling, flow
rate, slip, wall friction, nucleation sites, geometry of break, and two-dimensional
effects. Deych and Filipov (1969, Chapter 3) have provided nondimensional analyses
and identified groups that control the flow conditions and critical flow. Their
approach was to nondimensionalize basic two-fluid balance equations with
two-phase transfer terms. They identified Strouhal (transient case), Euler, Reynolds
Froude numbers, Weber, Peclet, Prandtl, Mach, and Nusselt (at interface) numbers
for assessing similarity.

## 10.2.1.1 Models in system codes

The system codes calculate conditions at the break plane based on code models for
wall and interfacial transfer terms that include wall friction. However, flow is
restricted based on correlation for critical two-phase flow. These system codes include
constitutive relationships based on steady-state data and flow near the choke point is
rapidly changing conditions. Therefore, imposed critical flow model on break flow or
possible location of choking will be sufficient.
System codes developed either 0-D or 1-D models for break flow or chocked flow
but in the worst conditions the accuracy of prediction cannot be better than 20% due to
complex geometrical effects and to unpredictable nucleation conditions. Assessment
