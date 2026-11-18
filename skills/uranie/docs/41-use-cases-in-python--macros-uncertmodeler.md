# Use-cases in Python — Macros UncertModeler
<!-- source PDF pages 486-487 -->

<!-- page 479 (PDF 486) -->
## 13.12 Macros UncertModeler

### 13.12.1 Macro “uncertModelerTestsYoungsModulus.py”

#### 13.12.1.1 Objective

The objective of the macro is to pass the 3 tests of fit based on Empirical Distribution Function (EDF) statistics
(Kolmogorov-Smirnov (D), Cramer-VonMises (W2) and Anderson-Darling (A2)) on the attribute “E” in the
"youngsmodulus" dataset. The tested law is the “normal” distribution when both the mean (30576) and variance
(1450) are set or when both are defined either from the sample.

#### 13.12.1.2 Macro Uranie

```python
"""
Example of distribution testing with quality criteria on data
"""
from URANIE import DataServer, UncertModeler
import ROOT
tds = DataServer.TDataServer()
tds.fileDataRead("youngsmodulus.dat")
c = ROOT.TCanvas("c1", "Test on youngsmodulus dataset", 13, 38, 1210, 1874)
pad = ROOT.TPad("pad", "pad", 0, 0.03, 1, 1)
pad.Draw()
pad.Divide(1, 3)
tks = UncertModeler.TTestKolmogorovSmirnov(tds, "E")
pad.cd(1)
tks.computeScore("normal:normal(30576,1450)")
tcvm = UncertModeler.TTestCramerVonMises(tds, "E")
pad.cd(2)
tcvm.computeScore("normal:normal(30576,1450)")
tad = UncertModeler.TTestAndersonDarling(tds, "E")
pad.cd(3)
tad.computeScore("normal:normal(30576,1450)")
```

<!-- page 480 (PDF 487) -->
#### 13.12.1.3 Graph

Figure 13.75: Graph of the macro “uncertModelerTestsYoungsModulus.py”
