# SCHEDULER
<!-- source PDF pages 492-494 -->

<!-- page 492 -->
Chapter 44
SCHEDULER
This optional block opens a new way to use TRIPOLI-4. Up to version 10, it was only possible to invoke the
code in the standard way, only one initialisation and then one simulation.
It allows to process parts (initialisation, simulation) of calculations one or more times. It allows to have
multiple SIMULATION blocks (with names) that can be invoked as tasks when needed.
The general syntax for a scheduler block is as follows :
SCHEDULER
INITIALIZE
SIMUi
SIMULATION
SIMUi
LOAD_SOURCES_FROM_KIJ_RESULTS
CLEAN_ALL_RESULTS
END_SCHEDULER
Internally, the calculation has been split into three parts:
1. the reading of the input deck;
2. initialisation of internal structures of a simulation;
3. simulation (transporting particles).
The reading of the input deck is always invoked when the code is launched. If the scheduler block is absent,
the calculation runs as usual going on with the initialisation and simulation. If the scheduler block is present,
then the calculation will be defined by the task included into this block.
WARNING: this feature opens a whole category of calculation schemes which are not currently possible
which TRIPOLI-4. It is recommended to stay within the calculations schemes described in this document.
This capability is being made available in mono-processor mode and in parallel mode.

<!-- page 493 -->
## 44.1 KIJ ACCELERATION OF CRITICAL CALCULATIONS

The scheduler was initially created to implement KIJ acceleration inside a criticality simulation. This acceleration
is indeed a multi-step calculation:
• first, a standard very short simulation is done with KIJ matrix calculation;
• then, the KIJ matrix is diagonalised and the source of the next calculation is initialised with the fundamental
solution;
• then the real simulation is started with new scores.
WARNING: this feature is theoretically longer in mono-processor mode than when using no acceleration.
It is thus recommended not to use this feature in mono-processor mode. Only the parallelism can accelerate
source convergence when using KIJ two steps calculation.
In the context of this development, some junctions between tasks have been developed:
• the capability to clear all scores between tasks;
• the capability to initialise sources from previous results of a KIJ calculation.
The user prepares two critical simulations that he will name SIMU1 and SIMU2.
The first simulation should contain very few batches. The keyword BATCH_PER_SIMULATOR can be easy
to use in this context. 3 to 5 batches per simulator are good number to start with when using for example
50 processors in parallel. This simulation should include a KIJ_MATRIX keyword. The keyword must be
completed by a full KIJ block specifying the mesh to be used for scoring fissions. The first simulation must
be initialised and run.
Then the KIJ matrix must be diagonalised and the fundamental vector must be transferred in the sources. The
keyword LOAD_SOURCES_FROM_KIJ_RESULTS must be invoked here. At this step, it is important to note that
the sources must have the exact same mesh as the KIJ matrix. New keywords (syntaxic sugars) have been
introduced in the sources definition to help the user get the same mesh (UPTO_LIN and REPEAT).
The second simulation SIMU is a normal simulation. It was important here to be able to deactivate the KIJ
matrix calculation in the second simulation as the acceleration gain of the method may easily be lost with a
huge score like KIJ matrices. The user disables the KIJ scoring in the second simulation by not including the
keyword KIJ_MATRIX in the second simulation.
An example of a scheduler block is as follows:
SCHEDULER
INITIALIZE SIMU1
SIMULATION SIMU1
LOAD_SOURCES_FROM_KIJ_RESULTS
CLEAN_ALL_RESULTS
SIMULATION SIMU2
END_SCHEDULER

<!-- page 494 -->
## 44.2 SPECIALISED TASKS

Some tasks have been created to make junctions between initialisation and simulations. Other tasks can be
implemented to create more interesting sequences.

### 44.2.1 CLEANING OF RESULTS

This task cleans all collected results by a previous simulation. The statistics are reset to scores of 0. and 0
batches. The scores currently remain initialized and can be accumulated again in a second simulation without
initialisation.

### 44.2.2 INITIALISING SOURCES FROM KIJ MATRIX FUNDAMENTAL

This task should be invoked when a previous simulation has been done and the sources of the next simulation
are to be initialised with the result of the fundamental calculated from the KIJ matrix.
Important: The KIJ matrix must have been calculated using a EXTENDED_MESH (fissile volumes will not do).
The sources will be declared using cartesian tabulated mesh (CARTESIAN, TABULATED keywords) in which all
matrix elements are provided (F_UVW format) and will have exactly the same structure than the KIJ matrix
(same position, same number of cells in every dimensions).
