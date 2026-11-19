<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/glossary.html -->

# 20. Glossary

Analysis
:   It is the optimal state estimated through a data assimilation or
    optimization procedure.

APosterioriCorrelations
:   Keyword to indicate the correlation matrix of *a posteriori* analysis
    errors.

APosterioriCovariance
:   Keyword to indicate the covariance matrix of *a posteriori* analysis
    errors.

APosterioriStandardDeviations
:   Keyword to indicate the standard errors diagonal matrix of *a posteriori*
    analysis errors.

APosterioriVariances
:   Keyword to indicate the variances diagonal matrix of *a posteriori*
    analysis errors.

Background
:   It is a part (chosen to be modified) of the system state representation,
    representation known *a priori* or initial one, which is not optimal, and
    which is used as a rough estimate, or a “best estimate”, before an
    optimal estimation.

BMA
:   The acronym means *Background minus Analysis*. It is the difference
    between the background state and the optimal state estimation,
    corresponding to the mathematical expression $\mathbf{x}^b -
    \mathbf{x}^a$.

Boundary conditions
:   These are particular input and control variables of the simulator, which
    characterize the description of the system’s behavior at the border of
    the simulation spatial domain.

Case
:   One ADAO case is defined by a set of data and of choices, packed together
    through the user interface of the module (in TUI as in GUI). The data are
    physical measurements that have technically to be available before or
    during the case execution. The simulation code(s) and the data
    assimilation or optimization method, and their parameters, has to be
    chosen, they define the execution properties of the case.

CostFunctionJ
:   Keyword to indicate the minimization function, noted as $J$.

CostFunctionJb
:   Keyword to indicate the background part of the minimization function,
    noted as $J^b$.

CostFunctionJo
:   Keyword to indicate the observation part of the minimization function,
    noted as $J^o$.

CurrentState
:   Keyword to indicate the current state used during an optimization
    algorithm procedure.

Digital simulator
:   All the numerical relationships and equations characterizing the physical
    system studied.

Initial conditions
:   These are specific simulator input and control variables that
    characterize the description of the system’s behavior at the initial edge
    of the simulation time domain.

Innovation
:   Difference between the observations and the result of the simulation based
    on the background state, filtered to be compatible with the observation.
    It is similar with OMB in static cases.

Iteration (internal)
:   An (internal) iteration takes place when using iterative optimization
    methods (e.g. for the 3DVAR algorithm). Internal iterations are performed
    within each iterative optimization operation. The iterative behavior is
    fully integrated into the execution of the iterative algorithms, and is
    only apparent to the user when his observation is explicitly requested
    using “*Observer*” attached to computational variables. See also
    [Step (of assimilation)](#term-Step-of-assimilation).

MahalanobisConsistency
:   Keyword to indicate the Mahalanobis parameter measuring the consistency of
    the data assimilation optimal state estimation. Its value can be compared
    to 1, a “good” estimation leading to a parameter “close” to 1.

Numerical simulation
:   Computational implementation of the set composed of the numerical
    simulator and a particular set of all the input and control variables of
    the simulator. These variables enable the digital simulator to be able to
    numerically represent the system’s behavior.

Observation operator
:   It is a transformation of the simulated state into a set of quantities
    explicitly comparable to the observations.

Observations or measurements
:   These are quantities that come from measuring instruments and
    characterize the physical system to be studied. These quantities can vary
    in space or time, can be punctual or integrated. They are themselves
    characterized by their measurement nature, size, etc.

OMA
:   The acronym means *Observation minus Analysis*. It is the difference
    between the observations and the result of the simulation based on the
    optimal state estimation, the analysis, filtered to be compatible with
    the observation, corresponding to the mathematical expression
    $\mathbf{y}^o - \mathbf{H}\mathbf{x}^a$.

OMB
:   The acronym means *Observation minus Background*. It is the difference
    between the observations and the result of the simulation based on the
    background state, filtered to be compatible with the observation,
    corresponding to the mathematical expression $\mathbf{y}^o -
    \mathbf{H}\mathbf{x}^b$.

Physical system
:   This is the object of study that will be represented by numerical
    simulation and observed by measurements.

SigmaBck2
:   Keyword to indicate the Desroziers-Ivanov parameter measuring the
    background part consistency of the data assimilation optimal state
    estimation. Its value can be compared to 1, a “good” estimation leading to
    a parameter “close” to 1.

SigmaObs2
:   Keyword to indicate the Desroziers-Ivanov parameter measuring the
    observation part consistency of the data assimilation optimal state
    estimation. Its value can be compared to 1, a “good” estimation leading to
    a parameter “close” to 1.

Step (of assimilation)
:   An assimilation step takes place when a new observation, or a new set of
    observations, is used, for example to follow the temporal course of a
    dynamic system. Remark: a *single step* of assimilation can contain by
    nature *several iterations* of optimization when the assimilation uses an
    iterative optimization method. See also [Iteration (internal)](#term-Iteration-internal).
