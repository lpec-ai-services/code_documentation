# THE ADAPTIVE MULTILEVEL SPLITTING VARIANCE REDUCTION TECHNIQUE
<!-- source PDF pages 262-270 -->

<!-- page 262 -->
Chapter 18
THE ADAPTIVE MULTILEVEL SPLITTING
VARIANCE REDUCTION TECHNIQUE
The Adaptive Multilevel Splitting (AMS) method [74] is a variance reduction method, based on splitting
operations, which can be used as an alternative to the standard variance reduction techniques of TRIPOLI-4®
presented in Chapter 17. It is based on an iterative process performed for each batch of the simulation. During
each iteration, particle trajectories are simulated in an analog way (pure analog or possibly including the
implicit capture default option of TRIPOLI-4®), then those particles are sorted with respect to the maximum
of an importance function evaluated along the trajectories. For each iteration of the algorithm, the sorting
process allows for the definition of a splitting level, which adaptively distinguishes the most interesting
particles from the others. All trajectories below the splitting level are removed from the simulation, and
resampled by duplicating some of the better ranking trajectories at their intersection with the current splitting
level. Finally, a multiplicative correction is applied to the usual Monte Carlo tally, taking into account the
number of completed AMS iterations.
Notes:
• The AMS can be used either for single-particle problems or for coupled problems including neutrons and
photons, or photons, electrons and positrons.
• It can be used together with gamma spectrometry scores, which is even the only way with TRIPOLI-4®
to perform variance reduction with the DEPOSITED_SPECTRUM response.

<!-- page 263 -->
## 18.1 SYNTAX

AMS
TARGET <target_definition>
SPLIT proportion
CROSS_SPLIT <flag>
RESAMPLE_COLLISIONS <flag>
IMPORTANCE
Description of the importance function
END_IMPORTANCE
END_AMS
Within the AMS block, the mandatory keywords are TARGET and IMPORTANCE. The default values for other
parameters are specified in the following sections.

## 18.2 TARGET DEFINITON

The keyword TARGET is used to define the volume of interest for the simulation (typically a detector). It is the
responsibility of the user to ensure that the defined target is in accordance with the importance function used
during the simulation.
There are two ways of defining the target of the simulation: either with a single target or with multiple targets.

### 18.2.1 SINGLE TARGET

The syntax is as follows:
TARGET volume_id
where volume_id is either the volume number or name.

### 18.2.2 MULTIPLE TARGETS

AMS can handle a list of volumes as target, enabling the user to divide the target in multiple volumes. It
should be kept in mind that the smallest variance for a given volume will be achieved with an AMS simulation
using this particular volume as single target.
The syntax is as follows:

<!-- page 264 -->
TARGET LIST nb(vol)
volume_id(1) ... volume_id(n))
where volume_id(i) is either a volume number or name.

### 18.2.3 SCORING OUTSIDE TARGETS

AMS is capable of returning an unbiased estimator of any score within the geometry. However, a variance
reduction can only be expected for scores which are estimated either around the target(s) or on the path of the
particles between their emission point(s) and the target(s).

## 18.3 SPLITTING PROPORTION

The keyword SPLIT allows the user to change the proportion of particles to be split at each AMS iteration.
According to experiment, this parameter has no noticeable influence on efficiency as long as it remains
greater than 0.5%. On the other hand, it seems unreasonable in terms of correlations to split more than half
of the particles per iteration, which is why it is recommended to keep this proportion below 50%.
If SPLIT is not specified, a value of 1% is assumed.
The syntax is as follows:
SPLIT proportion
where proportion is expressed in percent.

## 18.4 AMS OPTIONS

### 18.4.1 CROSSING POINTS SPLITTING

In order to have a more precise estimation of the importance of a particle during its transport through the
geometry, the AMS algorithm can evaluate its importance when it crosses frontiers between volumes. This
allows the method to classify and split particles at crossing points, which are treated in the exact same way
as collision points. This functionality is controlled by a flag which can take the value 1 (activated) or 0
(disabled):
CROSS_SPLIT <flag>
The default value for this flag is 1, but it can be useful to disable crossing points if the geometry is composed
of many volumes, which can significantly increase computation time.

<!-- page 265 -->
### 18.4.2 COLLISION RESAMPLING

There are two ways of performing particle splitting with AMS.
Either the particles importances are evaluated just after collision points, in which case the particles are duplicated
by copying the particles characteristics outgoing a collision.
Or, in some cases such as simulations with highly absorbing materials or importance functions with poor or
no account of the particles direction, it may be interesting to evaluate importance before collisions, and to
duplicate particles at collision sites by resampling collisions.
The syntax for enabling/disabling collision resampling is as follows:
RESAMPLE_COLLISIONS <flag>
The default value for this flag is 0.

## 18.5 IMPORTANCE FUNCTION

The AMS algorithm uses an importance function to determine which particle tracks are the most interesting
. The keyword IMPORTANCE has to be followed by the particle type (NEUTRON, PHOTON, ELECTRON or
POSITRON). The corresponding particles will be taken into account by the AMS algorithm with the importance
defined inside the block.
Obviously, the AMS cannot perform variance reduction on particles that are not in the simulation. If a single
particle type is present in the simulation, this type should be given after IMPORTANCE. If multiple particle
types are simulated, an IMPORTANCE block has to be given for each particle type that the AMS should take
into account. The particles that do not have a corresponding importance will be left out of the AMS variance
reduction algorithm.
To apply the same importance function to all particle types present in the simulation, ALL_PARTICLE can be
used as particle type.

### 18.5.1 IMPORTANCE MAPS

When parametrized with MAP, the AMS uses an importance map computed by the INIPOND module (see
Section 17.2). Note that this map can also be an external map, possibly coming from another code.
Therefore, it requires the VARIANCE_REDUCTION command block in the same data file (and in the case of
an external map, the option USE_FILE has to be used). The AMS takes into account every option available
to other variance reduction techniques, such as the manual modification of the bias parameters k (i.e. DATA
option of INIPOND command) or the importance monitoring.
The keyword MAP has to be followed by the type of particle type (either NEUTRON or PHOTON) corresponding
to one of the types specified in the VARIANCE_REDUCTION command block. This allows for example to use a

<!-- page 266 -->
photon importance while performing AMS on neutrons. The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
MAP <PARTICLE_TYPE>
END_IMPORTANCE
NOTE: There is no evidence that importance monitoring (see Section 22.2) improves the efficiency of the
AMS. Its use forces the first batches of the simulation to run without AMS, which may lead the simulation to
freeze the same way it would if another variance reduction technique was used. This is why it is recommended
to disable importance monitoring by adding the line MONITORING 0 to the SIMULATION block.

### 18.5.2 SPATIAL IMPORTANCES

The keywords FROM, TOWARDS and PATH allow the user to set a spatial importance. The importance of a point
is in this case computed regarding to a POINT, LINE, PLANE, SPHERE, CYLINDER or PATH.

#### 18.5.2.1 POINT

The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
<MODE> POINT X Y Z
END_IMPORTANCE
The importance of a given point is defined according to the distance d between this point and the point
(X,Y,Z). MODE is either FROM or TOWARDS. Using FROM, the importance is d, which causes the particles to be
pushed away from the point (X,Y,Z), regardless of the geometry. With TOWARDS, the importance is 1
d, which
causes the particles to be attracted to (X,Y,Z).

#### 18.5.2.2 LINE

The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
<MODE> LINE
POINT X Y Z
VECTOR VX VY VZ
END_IMPORTANCE

<!-- page 267 -->
The importance of a given point is defined according to the shorter distance dL between this point and the line
passing through point (X,Y,Z) and parallel to direction vector (VX,VY,VZ). MODE is either FROM or TOWARDS.
Using FROM, the importance is dL, which causes the particles to be pushed away from the line. With TOWARDS,
the importance is 1
dL, which causes the particles to be attracted to the line.

#### 18.5.2.3 PLANE

The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
<MODE> PLANE
POINT X Y Z
VECTOR VX VY VZ
END_IMPORTANCE
The importance of a given point is defined according to the shorter distance dP between this point and the
plane passing through point (X,Y,Z) with normal vector (VX,VY,VZ). MODE is either FROM or TOWARDS. Using
FROM, the importance is dP, which causes the particles to be pushed away from the plane. With TOWARDS, the
importance is 1
dP, which causes the particles to be attracted to the plane.

#### 18.5.2.4 SPHERE

The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
<MODE> SPHERE R
POINT X Y Z
END_IMPORTANCE
The importance of a given point is defined according to the distance dS between this point and the sphere
of radius R and center (X,Y,Z). MODE is either FROM or TOWARDS. Using FROM, the importance is dS, which
causes the particles to be pushed away from the sphere surface regardless of the geometry. With TOWARDS,
the importance is 1
dS, which causes the particles to be attracted towards the sphere surface.

#### 18.5.2.5 CYLINDER

The syntax is as follows:

<!-- page 268 -->
IMPORTANCE <PARTICLE_TYPE>
<MODE> CYLINDER R
POINT X Y Z
VECTOR VX VY VZ
END_IMPORTANCE
The importance of a given point is defined according to the distance dC between this point and the surface
of the infinite cylinder with radius R which axis passes through point (X,Y,Z) and is directed by vector
(VX,VY,VZ). MODE is either FROM or TOWARDS. Using FROM, the importance is dC, which causes the particles to
be pushed away from the cylinder surface. With TOWARDS, the importance is 1
dC , which causes the particles to
be attracted towards the cylinder.

#### 18.5.2.6 RING

The syntax is as follows:
IMPORTANCE <PARTICLE_TYPE>
<MODE> RING R
POINT X Y Z
VECTOR VX VY VZ
END_IMPORTANCE
The importance of a given point is defined according to the distance dR between this point and the ring of
radius R and center (X,Y,Z), which axis is directed by vector (VX,VY,VZ) and is directed by vector (VX,VY,VZ).
MODE is either FROM or TOWARDS. Using FROM, the importance is dR, which causes the particles to be pushed
away from the ring. With TOWARDS, the importance is 1
dC , which causes the particles to be attracted towards
the ring.

#### 18.5.2.7 PATH

The syntax is as follows:

<!-- page 269 -->
IMPORTANCE <PARTICLE_TYPE>
PATH
POINT LIST nb(points)
X1 Y1 Z1
...
Xn Yn Zn
STRENGTH s
END_PATH
END_IMPORTANCE
A path is defined as an ordered sequence of points. The importance of a point outside the path is defined
using the minimal distance from the point to the path d⊥, and the distance along the path from the first point
of the path to the orthogonal projection of the point on the path d∥. The importance is defined as
I = d∥−s.d⊥
so that it increases with the distance along the path and decreases with the distance to the path. The parameter
s represents the attraction strength of the path, which influences the slope of the importance function around
the path. By default, this parameter is set to 1. If needed, the optional keyword STRENGTH must be placed
after the list of points coordinates.

#### 18.5.2.8 VOLUME IMPORTANCE WEIGHTING

In addition to the importance function, each volume of the geometry carries an importance factor that weights
the importance of any point within its boundaries. By default, this value is set to 1. The user can change the
weight of any number of volumes using the following syntax:
IMPORTANCE <PARTICLE_TYPE>
...
VOLUME num(vol1) ... num(voln) WEIGHT w
END_IMPORTANCE

## 18.6 RELATED OPTIONS IN OTHER COMMAND BLOCKS

Some existing options of the SIMULATION command block (see Section 22.2) and the VARIANCE_REDUCTION
(see Chapter 17) command block can be used alongside the AMS and have an impact on the algorithm behaviour
.

<!-- page 270 -->
### 18.6.1 ANALOG

During the AMS iterations, particle transport is unbiased. However, the implicit capture may also be used
without altering the unbiasedness of the AMS algorithm. It is recalled that the implicit capture is activated by
default in TRIPOLI-4®. For a pure analog transport during the AMS iterations, the user has to use the ANALOG
option of the SIMULATION command block, which deactivates the implicit capture.

### 18.6.2 MONITORING

When using the importance map from the VARIANCE_REDUCTION block, the AMS is by default deactivated
during the 5 first batches, thus enabling TRIPOLI-4® to monitor importance and adjust energy-group biasing
. The monitoring process may eventually be quite expensive, and there is no assurance that the resulting
importance map is any better for the AMS use. Therefore, we recommend to deactivate this feature using the
optional line MONITORING 0 in the SIMULATION command block.

### 18.6.3 SMOOTHING

The INIPOND (see Section 17.2) module is designed to compute importance maps optimized for the use of
the Exponential Transform variance reduction technique. Amongst other optimizations, INIPOND smoothes
importance values to prevent weight discrepancies in the simulation. However, this process has no benefits
if the importance is used to perform AMS. In fact, importance map smoothing is inherently linked to a loss of
information. When using the AMS with an importance map computed by INIPOND module, it is advised to
disable importance smoothing using the optional line SMOOTHING 0 in the INIPOND command block.

## 18.7 RESTRICTIONS AND FORBIDDEN OPTIONS

When using the AMS, the simulation mode of the SIMULATION command block (see Section 22.2) must be
SHIELDING (which is the default option) or FIXED_SOURCES_CRITICALITY.
Some options are forbidden when used together with the AMS: PACKET_LENGTH option (see Section 22.2) and
score filtering (see Section 15.6).
