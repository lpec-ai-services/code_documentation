# Use-cases in Python — Macros MetaModelOptim
<!-- source PDF pages 440-441 -->

<!-- page 433 (PDF 440) -->
note that this version is really faster than the previous one, avoiding creation and manipulation of many TDataServer.

## 13.10 Macros MetaModelOptim

### 13.10.1 Macro “metamodoptEgoHimmel.py”

#### 13.10.1.1 Objective

The objective of this macro is to optimize a function using the Efficient Global Optimization algorithm (EGO). EGO is
well suited for problem when solution evaluations are expensive (efficient) and when problem has local minima (global).
In our example, evaluations are parallelized with threads to point out the standard context of its use.
The user function is inspired by an academic function, Himmelblau. It is a multimodal function used to point out the
global search that is realized. The problem have 5 parameters and 8 optimal solutions.

#### 13.10.1.2 Macro Uranie

This macro follows the structure of an reoptimizer macro (see previous chapter) and we take a quick look at generic part.
Only specific codes are explained in more details.

```python
import ROOT
from ROOT.URANIE import DataServer as DataServer
from ROOT.URANIE import Relauncher as Relauncher
from ROOT.URANIE import MetaModelOptim as Ego
# user choice
krigingStep = 50
cpus = 6
optimStop = 360
# user optim fonction
def userfun(x1, x2, x3, x4, x5):
    ret = 0.
    tabx = [x1, x2, x3, x4, x5]
    tmp = x1*x1 - x2 - 6
    ret += tmp * tmp
    for i in range(1, 5):
        if i % 2:
            tmp = tabx[i]*tabx[i] - tabx[i-1] - 6
        else:
            tmp = tabx[i] - tabx[i-1]
        ret += tmp*tmp
    return [ret, ]
# optim procedure
def ego_test():
    # variables
    inputname = ["x1", "x2", "x3", "x4", "x5"]
    inputs = [DataServer.TUniformDistribution(str, -8., 8.) for str in inputname]
    output = DataServer.TAttribute("y")
```

<!-- page 434 (PDF 441) -->
```python
    # optim function
    fun = Relauncher.TPythonEval(userfun)
    for i in inputs:
        fun.addInput(i)
    fun.addOutput(output)
    # runner
    run = Relauncher.TThreadedRun(fun, cpus+1)
    run.startSlave()
    if (run.onMaster()):
        tds = DataServer.TDataServer("tds", "ego tds")
        for i in inputs:
            tds.addAttribute(i)
        kmod = Ego.TEgoKBModeler()
        kmod.setModel("matern7/2", "const", 1.0e-8)
        kmod.setSolver("ML", "Bobyqa", 300, 800)
        hjsolver = Ego.TEgoHjDynSolver()
        hjsolver.setSize(64, 16)
        egosolv = Ego.TEGO(tds, run)
        egosolv.setSize(krigingStep, optimStop)
        egosolv.setModeler(kmod)
        egosolv.setSolver(hjsolver)
        egosolv.addObjective(output)
        egosolv.solverLoop()
        tds.exportData("egoPy.dat")
        run.stopSlave()
# run test
ego_test()
```

At beginning, some constant values are defined.
• cpus value defines the number of threads that are used for evaluation.
• krigingStep and optimStop values define respectively the number of evalutions needed before creating a first
surrogate model and the maximum number of evaluation allowed.
The userfun function defines the user function, and ego_test the optimisation to realize. The latter follows usual
structure: It defines the problem variables, a TPythonEval to describes the user function, a TThreadRun to use thread
parallelism. In the master block, a working TDataServer is defined, and optimization classes.
Notice that the input variables are defined with a TUniformDistribution (not just a TAttribute with minimum
and maximum values). The TDataServer is empty, and a sampler is run implicitely to be able to create a first surrogate
model. It may be unuseful when the TDataServer is filled by the fileDataRead method.
EGO uses two different solvers : one for surrogate model construction, one for EI optimisation :
• for surrogate model only one class is provided (TKBModeler). It allows to configure which kriging model to use
(setModel), and how it is constructed (setSolver)
• for maximizing EI, a TEgoHjDynSolver is defined, meaning it uses dynamic optimization with the HJMA al-
