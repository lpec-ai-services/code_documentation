# PARALLELISM
<!-- source PDF pages 392-399 -->

<!-- page 392 -->
Chapter 33
PARALLELISM
A parallel version of the TRIPOLI-4® code can be used. It is possible to use a number of separate machines
for a single simulation, or to carry out parallel calculation on several processors on a massively parallel
machine.
IMPORTANT: As of version 12, the TRIPOLI-4 code is launched in parallel using utilities as mpirun or
srun (as MPI codes). See the example in the section 33.3.2 for the new launch procedure. To adapt with
the parallel launching tool (mpirun, srun), the user will want to use the ’-m’ command line argument (see
introduction in section 33.1).

## 33.1 INTRODUCTION

A parallel application is executed in the same way as a conventional one. The code manages execution of the
different processes.
It is, however, also necessary to indicate:
• a parallelism file,
• the type of communication,
and, for this reason, the launch syntax for a calculation becomes:

<!-- page 393 -->
tripoli4
-d <data_file>
-s <format>
-c <dictionary_file>
-l <language>
-o <results_file>
-p <parallelism_file>
-t <communication_type>
-m <parallel_rank_variable_name>
-i <nb_processes>
-M <MTU_SIZE>
-S
-E
Where:
• <parallelism_file> is the name of the file containing hosts to be used for parallelism and whose
syntax is given in a following section (see 33.3).
• <communication_type> can now only be bsd. It means the communications are using the internal
communication library coded with BSD TCP sockets.
• <parallel_rank_variable_name> is the name of the environment variable containing the rank of
the parallel process. This variable depends on the utility used for launching TRIPOLI-44 in parallel.
Usual launchers are mpirun or srun. Common names of this environment variable are : RMS_RANK,
SLURM_PROCID, MPIRUN_RANK, OMPI_COMM_WORLD_RANK
• <nb_processes> sets the number of simultaneously initializing processes (which is currently 64 by
default).
• MTU_SIZE is the maximum size in bytes of packets in TCP communication. This tuning is available
only in bsd mode and can be useful to increase performance of parallel mode on computer clusters. The
correct parameter is to be derived from the specifications of the network interfaces of the cluster. A too
small value yields to parallelism low performance due to too much lag between communication packets.
Warning: A too big value can lead to incorrect results or parallelism instability.
• option -S: dispatches equal active charge (ie same number of batches) among all simulators if possible
. If the number of simulators divide the number of batches asked in the block SIMULATION, each
simulator will have the same number of batches which is the required number of batches divided by the
number of simulators. Otherwise, the first simulators will process one more batch. If DISCARD is asked,
the same number of active (non-discarded) batches are dispatched among simulators. Using -S is not
recommended in shielding mode with variance-reduction as a batch canceled due to too much splitting
among the first 4 will lead to missing batches and thus to a dead lock (all processes blocked waiting for
the others to make next action).

<!-- page 394 -->
• option -E: the input deck is no longer given in simulator output files. However, the command line option
-E is now available if the input deck is still needed.
The process executed by the user is called the monitor.
It is essential that the name of the monitor machine coincides with the name of the execution machine.
Its role is to monitor the proper execution of the parallel application.
Regarding the other processes, one of them, the collector (whose output is written in the file with the postfix
1th_task), has the function of collecting all the results. The other processes, called simulators (whose output
is written in the files with the postfixes 2th_task, 3th_task, etc.), carry out independent simulations which
all start with the same data (that given in the input file), but use a different sequence of the random number
generator. At the end of each batch, each simulator send its batch results to the collector. When the collector
has collected the number of batches demanded by the user in the input file, it tells the monitor to stop all the
simulators.
Care must be paid for criticality calculations, since the number of discarded batches indicated by the user in
the input file applies to each simulator, while the total number of batches refers to the whole simulation (see
complements in section 33.4).

## 33.2 LAUNCHING TOOLS

As of version 12, the TRIPOLI-4 code is launched in parallel using utilities as mpirun or srun (as MPI codes).

### 33.2.1 MPIRUN OR SRUN TOOLS

To use TRIPOLI-4 with mpirun or srun, you must first install it (if not available) on your Linux distribution using
your package manager (apt, yum...). The specific tool man page will guide you for running the executable.
You must get the name of the rank environment variable and declare it to TRIPOLI-4 (using -m argument, see
above). Usual names are:
• SLURM_PROCID for SLURM;
• OMPI_COMM_WORLD_RANK for OpenMPI;
• MPIRUN_RANK or RMS_RANK.
To help you finding this environment variable, you may use the command
mpirun -n 2 env | grep RANK
You must also prepare a graphe file coherent with the usage of the mpirun (or srun) tool. Especially, the
number of hosts declared in the graphe file must be the same as the number of hosts asked to mpirun (or
srun).

<!-- page 395 -->
### 33.2.2 LPAR* TOOLS

lpar is a tool for launching in parallel. Since the version 12, the command name has to be changed to lparm
as the default build of TRIPOLI-4 is suitable for use on large clusters (the underlying TRIPOLI-4 is using
the mpirun tool or equivalent). It allows the user to run TRIPOLI-4 in parallel on a node with multiple
CPUs without having to prepare the parallelism host file. The user must only provide the command line in
mono-processor and the number of CPUs to be used for the calculation. It is greatly recommended, as a
preliminary test, to process a few batches (3-5) in mono-processor.
Then, the calculation can be launched in parallel using the following command line
lparm -n <number_of_processors> <command_line_in_monoprocessor>
In the previous command, the exact same command as in mono-processor can be used (reducing error possibilities
).

## 33.3 THE PARALLELISM FILE

The syntax of the file is as follows:
PROCESS
nb(process)
process monitor <program> <machine(m)>
process <name(collector)> <program> <machine(0)>
process <name(simulator1)> <program> <machine(1)>
...
process <name(simulatorN)> <program> <machine(N)>
RUN_DIRECTORY
name(directory)
GRAPH
name(collector) < −> name(simulator1)
...
name(collector) < −> name(simulatorN)
END
where:
• <program> is the name of the executable (possibly with its path), tripoli4 for instance,
• <machine(m)> is the name of the machine on which the monitor is located,
• <name(collector)> and <machine(0)> relate to the collector,
• <name(simulatori)> and <machine(i)> relate to the i-th simulator

<!-- page 396 -->
• <name(directory)> is the directory in which the tasks are run (from which certain task files can be
recovered. It can, therefore, be suitable to give the working directory, as the code uses $HOME by
default).

### 33.3.1 HETEROGENEOUS CLUSTERS

It is possible to run the simulation on a cluster of completely heterogeneous computers, including hardware
by SUN, HP, etc.). The monitor runs the batches on the different processors.

### 33.3.2 CALCULATION ON A MACHINE WITH A RESOURCE MANAGER

The process for using TRIPOLI4 on a machine with resource manager (for example SLURM) is quite similar.
It is, however, necessary to create a parallelism file named graphe.save (for the launch procedure):
PROCESS <N>
process monitor
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 1th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 2th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 3th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 4th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 5th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
process 6th_task
/home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
...
process <N-1>th_task /home/tripoli4/tripoli4.11/CODE/bin/irene/static_tripoli4
irene
GRAPH
1th_task <->
2th_task
1th_task <->
3th_task
1th_task <->
4th_task
1th_task <->
5th_task
1th_task <->
6th_task
...
1th_task
<->
<N-1>th_task
FIN
It should be noted that the name of the node on which each task is to run is not specified. It is the code that,
depending on the number of nodes allocated to it by the launch shell, creates a filename graphe.port, which
needs to be destroyed after execution, and an execution file (tache.csh):
#!/bin/sh
#BSUB -W 0:15
#BSUB -n 6
cd <working_directory>

<!-- page 397 -->
# cleanup
\rm -f *.update graphe graphe.port last_simulation*
# new graph file done by script inigraphlsb
inigraphlsb $PROG
#execution
srun /home/tripoli4/tripoli4.9/CODE/bin/linux-intel-64/static_tripoli4 -d <data_file>\
-s NJOY -c <dictionary_file> -p graphe -t bsd
# cleanup
\rm -f *.update graphe graphe.port last_simulation*
All that is then required is to submit the task to the parallel machine:
bsub < tache.sh

#### 33.3.2.1 Results

At launch time, filenames
last_simulation.<process_name>.res
are created. It is in these files that are written any errors encountered during the initialisation phase of the
parallel simulation.
When the simulation starts, other files are created
<data_file>.<process_name>.res
.
For the collector, the file contains the results of the different printouts requested. For the simulators, the
file contains the characteristics for the simulation for each batch processed. The printouts are created as the
results are collected by the collector and as simulation proceeds for the simulators.
As for file results_file (see chapter 1), it contains the results of the monitor (not affected by the results
of the simulation). It contains information on parallelisation, process initialisation, communication statistics,
etc.

#### 33.3.2.2 Advices regarding execution

• Remember that the monitor machine must be the same one that launches the execution.
• The traffic (i.e., the number of messages exchanged), must not be prohibitively large. As the processors
send a message to the collector at the end of each batch, it is better if the running time of each batch
is not too short. In particular, the number of particles per batch must not be too small. Otherwise,
the traffic can prevent communication and crash the machines involved in the simulation (the operating
system buffers being full), and even bring the entire network down.

<!-- page 398 -->
It is possible to use the PACKET_LENGTH option defined in chapter 22 in order to reduce the amount of
communications.
• Moreover, it is highly recommended to launch exactly one process per processor. This also includes the
monitor and the collector, even if they do not seem to use as much CPU resources as a simulator. They
are communicating with all processes, so that too much delay receiving some messages can result in a
loss of the whole calculation. Their role is critical for the computation.
• When launching several multi-processor calculations, it is highly recommended to run each case in
separate directories otherwise that may lead to failure.
33.4
DIFFERENCES
BETWEEN
DISCARD
PROCESSING
IN
MONO-PROCESSOR AND PARALLEL CALCULATIONS
Due to both theoretical and practical considerations, the discard processing in criticality between the
mono-processor and parallel modes are different.
In the criticality mode, the whole calculation is a fix point algorithm initialized by the user (specifying the
initial source). The first part of the calculation must dispatch the sources according to the fundamental mode
of the critical Boltzmann equation. The accumulation of scores only starts after this first part is finished.
A second reason to discard this part is for the Central Limit theorem. The Central Limit theorem allows to
calculate the standard deviation of the mean and have confidence intervals. One hypothesis of this theorem is
the stationarity of the series on which it applies.
Multiple discards are used depending on the aim. All are, of course, used to ensure the stationarity of the
series of the results. However, they apply on different parts of the calculation:
• source convergence discard: either in manual mode (keyword DISCARD) or in automatic mode (no keyword
DISCARD), it applies on the collecting of the scores. In mono-processor mode, no score except
Keffs is calculated before the end of this part. In parallel, no scores at all is sent before the end of this
part. For the automatic mode, when the fluctuations of the kcoll is considered stabilized, the sources are
supposed to be converged and the message "kcoll is converged at batch" is displayed.
• discards on the series of results. Results consists of 2 kinds of scores which are processed differently.
Mainly, we have Keffs and the other scores.
– "Best discard" is used for Keffs. An evaluation is done on the first third of the simulation to find the
"best discard" which will yield the minimal standard deviation.
– DISCARD (or automatic discard) is used again for scores.
We gather in the following table the application of every discard depending on the calculation part.

<!-- page 399 -->
Calculation part
auto discard
manual discard
best discard
Source convergence
yes
yes
no
Fluxes, reaction rates...
yes
yes
no
Global scores (Beta, global, etc...)
yes
yes
no
Keffs
Mono/no
Mono/no
yes
Para/yes
Para/yes
yes

## 33.5 INCOMPATIBILITIES

The following options or commands are not available in parallelism mode:
• Option -j (NJOY, see chapter 1);
• SOURCE_STORAGE (see section 12.6.2);
• Green’s function files exploitation (see chapter 35);
• RANDOM option with DRAND48_RANDOM random number generator: only the MT19937_RANDOM
Mersenne Twister random number generator is allowed (see chapter 22).
• GRAPH_CONTOURS or GRAPH_NO_CONTOUR command in the AUTO_COUPLING option (see section 17.7);
• GRAPH option in VARIANCE_REDUCTION command (see section 17.8);
• Display of collisions sites (see chapter 25);
• The IDT block in the VARIANCE_REDUCTION block (see chapter 20);
• Command line option -S in shielding mode with variance reduction (see above);
• Entropy calculation (however, the user can alternatively study the source convergence in monoprocessor
mode and use the result for its parallel run, see subsection 15.9.2).
