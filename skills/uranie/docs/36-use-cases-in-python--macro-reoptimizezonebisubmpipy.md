# Use-cases in Python — Macros Reoptimizer — Macro “reoptimizeZoneBiSubMpi.py” … Macro “reoptimizeZoneBiFunMpi.py”
<!-- source PDF pages 431-439 -->

<!-- page 424 (PDF 431) -->
The rest of this macro plays the role of the user in front of a ROOT-console (its python interplay of course). It defines
the correct namespace, loads the function file and destroys previously existing genetic.dump files. From there it runs
the LaunchVizir function as many times as needed (thanks to the boolean returned) as the used would do, by restarting
the macro, even after exiting the ROOT console.
The plot shown below represent the Pareto front every time the genetic algorithm stops (at the fourth run, it finally
converges !).

#### 13.9.5.3 Graph

Figure 13.57: Graph of the macro “reoptimizeHollowBarVizirSplitRuns.py”

### 13.9.6 Macro “reoptimizeZoneBiSubMpi.py”

#### 13.9.6.1 Objective

The objective of the macro is to show an example of a two level parallelism program using the Mpi paradigm.
• At the top level, an optimization loop parallelizes its evaluations
• At low level, each optimizer evaluation are a launcher loop who parallelizes its own sequential evaluations
These example is inspired from a zoning problem of a small plant core with square assemblies. However, the physics
embeded in it is reduced to none (sorry), and the problem is simplified. With symetries, the core is defined by 10 different
assemblies presented on the following figure. For production purpose, only 5 assembly types are allowed, defined by an
emission value.

<!-- page 425 (PDF 432) -->
Figure 13.58: The core and its assemblies
To simplify the problem, some constraints are put :
• most assemblies belong to a default zone
• other zone is restricted to one assembly (or two for 4 and 5, and for 8 and 9 for symetrical reason)
• one zone is imposed with the 8th et 9th external assemblies.
• the total of assembly emission is defined.
For each assembly, a reception value is defined depending on the emission from itself and its neighbour’s (just 8 neightbours
are taken in account, the 4 nearest neighbours and 4 secondary neighbours). The global objective is to minimize the
difference between the biggest and the smallest reception value.
Optimisation works on 4 emission values (the fifth value, affected to the external zone, is set, and all values are normalized
with the total emission value) and each evaluation loops over the 35 possible arrangements (choose 3 zones from 7). A
single evaluation take emission values and the selected zones and return the maximum reception difference.

#### 13.9.6.2 Macro Uranie

This macro is splited in 2 files : the first one defines the low level evaluation function and is reused in the next reoptimizer
example. It is quite a mock function, and is given to be complete, but is not needed to understand how to implement the
two level MPI parallelism

```python
#!/usr/bin/env python
# the different zones
# 6 9
# 3 5 7
# 1 2 4 8
# 0 1 3 6
# 1 2 5 9
# 4 primary neighbours of a zone
near1 = [
    [1, 1, 1, 1],
                   # 0
    [0, 2, 2, 3],
    [1, 1, 4, 5],
    [1, 4, 5, 6],
                   # 3
```

<!-- page 426 (PDF 433) -->
```python
    [2, 3, 7, 8],
    [2, 3, 7, 9],
    [3, 8, 9, 10],
                    # 6
    [4, 5, 10, 10],
    [4, 6, 10, 10],
    [5, 6, 10, 10]
                    # 9
]
# 4 secondary neighbours
near2 = [
    [2, 2, 2, 2],
                   # 0
    [1, 1, 4, 5],
    [0, 3, 3, 7],
    [2, 2, 8, 9],
                   # 3
    [1, 5, 6, 10],
    [1, 4, 6, 10],
    [4, 5, 10, 10],
                     # 6
    [2, 8, 9, 10],
    [3, 7, 10, 10],
    [3, 7, 10, 10]
                    # 9
]
# low level evaluation
def lowfun(edft, e_1, e_2, e_3, a_1, a_2, a_3):
    """ evaluate a zoning """
    def fill(loc, vid, val):
        """ fill a zone with an emission value """
        l_id = int(vid)
        loc[l_id] = val
        if l_id == 4:
            loc[5] = val
    def reception(loc, l_id):
        """ calculate reception in a zone """
        ret = loc[l_id]
        for l_iter in near1[l_id]:
            ret += loc[l_iter] / 8
        for l_iter in near2[l_id]:
            ret += loc[l_iter]/16
        return ret
    # init dft
    loc = [edft for i in range(11)]
    loc[8] = 0.8
    loc[9] = 0.8
    loc[10] = 0.0
    # init spec
    fill(loc, a_1, e_1)
    fill(loc, a_2, e_2)
    fill(loc, a_3, e_3)
    # normalize
    loc_all = loc[0] / 4
    for i in loc[1:]:
```

<!-- page 427 (PDF 434) -->
```python
    loc_all += i
locn = [i*10/loc_all for i in loc]
# max diff
loc_max = reception(locn, 0)
loc_min = loc_max
for i_id in range(1, 10):
    next_var = reception(locn, i_id)
    if next_var < loc_min:
        loc_min = next_var
    elif next_var > loc_max:
        loc_max = next_var
# output
ret = [loc_max - loc_min]
for i in locn[:-1]:
    ret.append(i)
return ret
```

The lowfun function deals, as expected, with the low level evaluation. In inputs it has the 4 emission values (default,
zone1, zone2, zone3) and 3 indicators defining the zone affected by the extra emission value. It returns the maximal
difference between two zone reception values and the 9 normalized emission values (informative data). Two arrays are
used to define the neighbourhood
With the second file, the two level MPI parallelism is defined.

```python
#!/usr/bin/env python
import ROOT
import URANIE.DataServer as DataServer
import URANIE.Relauncher as Relauncher
import URANIE.Reoptimizer as Reoptimizer
import URANIE.MpiRelauncher as MpiRelauncher
from reoptimizeZoneCore import lowfun
# resume from tds
def tds_resume(tds, attr):
    """ get the best zoning from tds """
    def get_in_tds(tds, leaf, l_id):
        """ get a zoning objective """
        tds.GetTuple().GetEntry(l_id)
        return leaf.GetValue(0)
    siz = tds.GetTuple().GetEntries()
    leaves = [tds.GetTuple().GetLeaf(a.GetName()) for a in attr]
    # search min
    k = 0
    loc_min = get_in_tds(tds, leaves[0], 0)
    for i in range(1, siz):
        cur = get_in_tds(tds, leaves[0], i)
        if (cur < loc_min):
            loc_min = cur
```

<!-- page 428 (PDF 435) -->
```python
            k = i
    # all results
    tds.GetTuple().GetEntry(k)
    return [l.GetValue(0) for l in leaves]
# top level evaluation
def doefun(edft, ezon1, ezon2, ezon3) :
    """ find the best zoning for a given emission values """
    # inputs
    azon0 = DataServer.TAttribute("zon0", 0., 1.)
    azon1 = DataServer.TAttribute("zon1", 0., 1.)
    azon2 = DataServer.TAttribute("zon2", 0., 1.)
    azon3 = DataServer.TAttribute("zon3", 0., 1.)
    adef1 = DataServer.TAttribute("a1")
    adef2 = DataServer.TAttribute("a2")
    adef3 = DataServer.TAttribute("a3")
    funi = [azon0, azon1, azon2, azon3, adef1, adef2, adef3]
    # outputs
    namo = ["diff", "v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"]
    funo = [DataServer.TAttribute(n) for n in namo]
    # low fun
    fun = Relauncher.TPythonEval(lowfun)
    for inp in funi:
        fun.addInput(inp)
    for out in funo:
        fun.addOutput(out)
    # runner
    # run = Relauncher.TSequentialRun(fun)
    run = MpiRelauncher.TSubMpiRun(fun)
    run.startSlave()
    if run.onMaster():
        # doe def
        data = DataServer.TDataServer("doe", "tds4doe")
        data.keepFinalTuple(False)
        for i in funi[4:7]:
            data.addAttribute(i)
        data.fileDataRead("reoptimizeZoneDoe.dat", False, True, "quiet")
        # realize doe
        launch = Relauncher.TLauncher2(data, run)
        launch.addConstantValue(azon0, edft)
        launch.addConstantValue(azon1, ezon1)
        launch.addConstantValue(azon2, ezon2)
        launch.addConstantValue(azon3, ezon3)
        launch.solverLoop()
        # get objective
        ret = tds_resume(data, funo)
        # clean
        run.stopSlave()
        ROOT.SetOwnership(run, True)
        ROOT.SetOwnership(data, True)
        return ret
```

<!-- page 429 (PDF 436) -->
```python
    else:
        # return something to avoid warning
        # output number should be coherent
        return [0. for i in namo]
# top level control
def coeurR():
    """ optimization on emission values """
    # inputs
    nami = ["zone1", "zone2", "zone3", "zone4"]
    funi = [DataServer.TAttribute(n, 0., 1.) for n in nami]
    # outputs
    namo = ["diff", "v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"]
    funo = [DataServer.TAttribute(n) for n in namo]
    # top fun
    fun = Relauncher.TPythonEval(doefun)
    for inp in funi:
        fun.addInput(inp)
    for out in funo:
        fun.addOutput(out)
    fun.setMpi()
    # runner
    # run = Relauncher.TSequentialRun(fun)
    run = MpiRelauncher.TBiMpiRun(fun, 3)
    run.startSlave()
    if run.onMaster():
        # data
        data = DataServer.TDataServer("tdsvzr", "tds4optim")
        fun.addAllInputs(data)
        # optim
        gen = Reoptimizer.TVizirGenetic()
        gen.setSize(300, 200000, 100)
        viz = Reoptimizer.TVizir2(data, run, gen)
        viz.addObjective(funo[0])
        viz.solverLoop()
        # results
        data.exportData("__coeurPy__.dat")
        # clean
        run.stopSlave()
        ROOT.SetOwnership(run, True)
#ROOT.EnableThreadSafety()
coeurR()
```

This script is structured with 3 functions :
• function tds_resume is used by the intermediate function. It receives the TDataServer filled, loops on its items
and returns an synthetic value. In our case, the minimum value of the reception difference, and the 9 normalized
emission values
• function doefun is the intermediate evaluation function. It runs the design of experiments containing all 35 possible
arrangements and extract the best one. It receives the 4 emission values and used them to complete the

<!-- page 430 (PDF 437) -->
TDataServer using the addConstantValue method.
• function reoptimizeZoneBiSubMpi is the top level function who solve the zoning problem
TBiMpiRun and TSubMpiRun are used to allocate cpus between intermediate and low level. TBiMpiRun is used in
reoptimizeZoneBiSubMpi (top) with an integer argument specifying the number of CPUs dedicated to each intermediate
level. In our case (3), with 16 resources request to MPI, they are divided in 5 groups of 3 CPUs, and one CPU
is left for the top level master (take care that the number of CPUs requested matches group size (16 % 3 == 1)). The top
level Master sees 5 resources for his evaluations. TSubMpiRun is used in doefun function and gives access to the 3 own
resources reserved in top level function.
Running the script is done as usual with MPI :

```python
mpirun -n 16 python reoptimizeZoneBiSubMpi.py
```

At the begining of reoptimizeZoneBiSubMpi function there is a call to ROOT::EnableThreadSafety. It is unusefull
in this case, but if we parallelize with threads instead of MPI. If you want to use both threads and MPI, it is
recommended to use MPI at top level.

### 13.9.7 Macro “reoptimizeZoneBiFunMpi.py”

#### 13.9.7.1 Objective

The objective of the macro is to give another example of a two level parallelism program using MPI paradigm. In the
former example MPI function call is implicit using Uranie facilities. In this one, explicit calls to MPI functions is done.
It’s presented to illustrate the case when the user evaluation fonction is an MPI function.
It takes the former example of zoning problem and adapts it. The intermediate level does not use a TLauncher2 to run
all different arrangements, but encodes it. Each Mpi ressources evaluates different possible arrangements keeping its best
one, and Mpi reduce these results to the final result.
Exclamation-Triangle Warning
To be run, the code need the mpi4py python module to be installed. This dependancy is not tested when Uranie is
installed

#### 13.9.7.2 Macro Uranie

The low level evaluation function is the same than in previous example and is not shown again.

```python
#!/usr/bin/env python
import ROOT
import URANIE.DataServer as DataServer
import URANIE.Relauncher as Relauncher
import URANIE.Reoptimizer as Reoptimizer
import URANIE.MpiRelauncher as MpiRelauncher
from mpi4py import MPI
import ctypes
from reoptimizeZoneCore import lowfun
# mpi4py helpers
def getCalculMpiComm() :
```

<!-- page 431 (PDF 438) -->
```python
    """ convert C MPI_Comm to python """
    typemap = {
        ctypes.sizeof(ctypes.c_int) : ctypes.c_int, #mpich
        ctypes.sizeof(ctypes.c_void_p) : ctypes.c_void_p, #openmpi
    }
    comm = MPI.Comm()
    handle_t = typemap[MPI._sizeof(comm)]
    handle_new = handle_t.from_address(MPI._addressof(comm))
    handle_new.value = MpiRelauncher.TBiMpiRun.getCalculMpiCommPy()
    return comm
# doe
doe = [
    [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 6], [4, 6, 7], [0, 6, 7], [0, 1, 7], # 7
    [0, 1, 3], [1, 2, 4], [2, 3, 6], [3, 4, 7], [0, 4, 6], [1, 6, 7], [0, 2, 7], # 14
    [0, 1, 4], [1, 2, 6], [2, 3, 7], [0, 3, 4], [1, 4, 6], [2, 6, 7], [0, 3, 7], # 21
    [0, 1, 6], [1, 2, 7], [0, 2, 3], [1, 3, 4], [2, 4, 6], [3, 6, 7], [0, 4, 7], # 28
    [0, 2, 4], [1, 3, 6], [2, 4, 7], [0, 3, 6], [1, 4, 7], [0, 2, 6], [1, 3, 7], # 35
]
# doe fun
def doefun(emz0, emz1, emz2, emz3) :
    """ find the best zoning for a given emission values """
    # mpi context
    comm = getCalculMpiComm()
    rank = comm.Get_rank()
    size = comm.Get_size()
    # search local best
    ind = rank
    idz1 = doe[ind][0]
    idz2 = doe[ind][1]
    idz3 = doe[ind][2]
    memo = lowfun(emz0, emz1, emz2, emz3, idz1, idz2, idz3)
    for next in range(rank, len(doe), size) :
        idz1 = doe[next][0]
        idz2 = doe[next][1]
        idz3 = doe[next][2]
        curr = lowfun(emz0, emz1, emz2, emz3, idz1, idz2, idz3)
        if curr[0] < memo[0] :
            memo = curr
    # global best
    # where is min
    ret = (memo[0], rank)
    (val, fid) = comm.allreduce(ret, op=MPI.MINLOC)
    # get all min value
    rval = memo
    if fid != 0 :
        if rank == fid :
            comm.send(memo, dest=0, tag=0)
        elif rank == 0 :
            rval = comm.recv(source=fid, tag=0)
```

<!-- page 432 (PDF 439) -->
```python
    return rval
# top level control
def coeurMpi():
    """ optimization on emission values """
    # inputs
    nami = ["zone1", "zone2", "zone3", "zone4"]
    funi = [DataServer.TAttribute(n, 0., 1.) for n in nami]
    # outputs
    namo = ["diff", "v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9"]
    funo = [DataServer.TAttribute(n) for n in namo]
    # top fun
    fun = Relauncher.TPythonEval(doefun)
    for inp in funi:
        fun.addInput(inp)
    for out in funo:
        fun.addOutput(out)
    fun.setMpi()
    # runner
    # run = Relauncher.TSequentialRun(fun)
    run = MpiRelauncher.TBiMpiRun(fun, 3, False)
    run.startSlave()
    if run.onMaster():
        # data
        data = DataServer.TDataServer("tdsvzr", "tds4optim")
        fun.addAllInputs(data)
        # optim
        gen = Reoptimizer.TVizirGenetic()
        gen.setSize(300, 200000, 100)
        viz = Reoptimizer.TVizir2(data, run, gen)
        viz.addObjective(funo[0])
        viz.solverLoop()
        # results
        data.exportData("__coeurMpy__.dat")
        # clean
        run.stopSlave()
        #ROOT.SetOwnership(run, True)
#ROOT.EnableThreadSafety()
coeurMpi()
```

The top level function (coeurMpi) does not change from the previous example. The only difference is in the creation of
the TBiMpiRun instances, which is done with an extra parameter set to False. This tell the constructor to avoid calling
MPI_Init function. With mpi4py, this call is already done when the module is imported
The evaluation MPI fonction (doefun) is totaly different. It uses the function getCalculMpiComm to get the MPI
Communicator object (MPI.Comm) dedicated to the calcul ressources. With it, different call to its method can be done :
Get_rank and Get_size to get the context ; allreduce, send and recv to communicate between calculs ressources.
Function getCalculMpiComm is an helper function use to convert the MPI communicator get from Uranie
MpiRelauncher.TBiMpiRun.getCalculMpiCommPy class method to the mpi4py equivalent object
You may run this script the same way as the precedent example, with the same constraint on the ressource number. Also
