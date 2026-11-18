# The Uncertainty modeler module
<!-- source PDF pages 197-199 -->

<!-- page 190 (PDF 197) -->
THE UNCERTAINTY MODELER MODULE
Abstract This chapter presents the features of the UncertModeler module of Uranie - version v4.11.0. The namespace
of this library is URANIE::UncertModeler.

## 12.1 Tests based on the Empirical Distribution Function (“EDF tests”)

The implemented tests are the Kolmogorov-Smirnov (𝐷) test, the Cramer-VonMises (𝑊2) test and the
Anderson-Darling (𝐴2) test. Their aim is to compare a given attribute to a bunch of implemented laws among the
following list: the normal, lognormal and uniform law. The details of the computation is given in [Bla17]. The following
piece of code gives an example of what can be achieved using these three classes and the usage of their options defined
in the summary block below. Figure 12.1 shows the results of such a script.

```python
"""
Example of distribution testing with different quality criteria
"""
from URANIE import DataServer, Sampler, UncertModeler
import ROOT
# Create a TDS with 3 kind of distributions
tds0 = DataServer.TDataServer()
tds0.addAttribute(DataServer.TNormalDistribution("n", 1.3, 4.5))
tds0.addAttribute(DataServer.TLogNormalDistribution("ln", 1.3, 4.5))
tds0.addAttribute(DataServer.TUniformDistribution("u", -1.3, 4.5))
# Create the sample
fsamp = Sampler.TBasicSampling(tds0, "lhs", 1000)
fsamp.generateSample()
# Create the canvas
c = ROOT.TCanvas("c1", "", 5, 20, 1300, 600)
apad = ROOT.TPad("apad", "apad", 0, 0.03, 1, 1)
apad.Draw()
apad.cd()
apad.Divide(3)
apad.cd(1)
tks_n = UncertModeler.TTestKolmogorovSmirnov(tds0, "n")
tcvm_n = UncertModeler.TTestCramerVonMises(tds0, "n")
tad_n = UncertModeler.TTestAndersonDarling(tds0, "n")
```

<!-- page 191 (PDF 198) -->
```python
# Test wrt to a normal distribution whose mu and sigma are taken from
# the original distribution
tks_n.computeScore("same:normal")
tad_n.computeScore("same:normal(0.8,4.5))")
                                             # put wrong mu
tcvm_n.computeScore("same:normal(1.3,5.5)")
                                             # put wrong sigma
apad.cd(2)
tks_ln = UncertModeler.TTestKolmogorovSmirnov(tds0, "ln")
tcvm_ln = UncertModeler.TTestCramerVonMises(tds0, "ln")
tad_ln = UncertModeler.TTestAndersonDarling(tds0, "ln")
# Test wrt to a lognormal distribution whose mu and sigma are taken from
# the original distribution
tks_ln.computeScore("same:lognormal")
tad_ln.computeScore("same:lognormal(1.2,4.5))")
                                                 # put wrong mu
tcvm_ln.computeScore("same:lognormal(1.3,3.5)")
                                                 # put wrong sigma
apad.cd(3)
tks_u = UncertModeler.TTestKolmogorovSmirnov(tds0, "u")
tcvm_u = UncertModeler.TTestCramerVonMises(tds0, "u")
tad_u = UncertModeler.TTestAndersonDarling(tds0, "u")
# Test wrt to an uniform distribution whose min and max are taken from
# the original distribution (and compared to a normal as well, for fun)
tks_u.computeScore("same:uniform")
tad_u.computeScore("same:uniform(-1.2,4.5)")
                                              # put wrong min
tcvm_u.computeScore("same:uniform(-1.3,4.6)")
                                               # put wrong max
```

Figure 12.1: Results of the macro defined previously to produce variety of test of already implemented distributions
INFO-CIRCLE Summary: Tests based on the EDF (TTestKolmogorovSmirnov, TTestCramerVonMises and TTest
AndersonDarling classes)

<!-- page 192 (PDF 199) -->
• TTestKolmogorovSmirnov(TDataServer tds, const char * sAtt, Option_t * option=””)
Define the Kolmogorov-Smirnov (D) test for the attribute sAtt. No option is used.
• TTestCramerVonMises(TDataServer tds, const char * sAtt, Option_t * option=””)
Define the Cramer-VonMises (W2) test for the attribute sAtt. No option is used.
• TTestAndersonDarling(TDataServer tds, const char * sAtt, Option_t * option=””)
Define the Anderson-Darling (A2) test for the attribute sAtt. No option is used.
• computeScore(Option_t* option=””)
Compute the score for the current test ( D, W2 and A2) with laws defined in the option parameter. The laws are
separated by the “:” character. If the parameters of the law are defined by the user, they are defined in brackets
“()” as normal(30576,1450). If the parameters must be estimated by the algorithm, do not use the brackets as
normal. Actually, the laws implemented are the normal and lognormal laws.
