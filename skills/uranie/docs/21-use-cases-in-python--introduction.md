# Use-cases in Python — Introduction … Macros Python HowTo
<!-- source PDF pages 200-208 -->

<!-- page 193 (PDF 200) -->
USE-CASES IN PYTHON

## 13.1 Introduction

Several use-cases of Uranie are described in this chapter with a small description of the implemented methods in the
Uranie platform. These macros are located in the sub-directory “/share/uranie/macros” of the installation folder of Uranie
($URANIESYS).
In this chapter, inside each macro, the Uranie specific namespaces might not always be specified anymore. These specifications
are gathered in the rootlogon.py file, introduced in Uranie namespace, which is automatically loaded when
executing python. An example would be:

```python
import ROOT
# Create shortcuts if uranie exists
urasys = ROOT.TString(ROOT.gSystem.Getenv("URANIESYS"))
if not urasys.EqualTo(""):
    from ROOT.URANIE import DataServer as DataServer
    from ROOT.URANIE import Sampler as Sampler
    from ROOT.URANIE import Launcher as Launcher
    from ROOT.URANIE import Relauncher as Relauncher
    from ROOT.URANIE import Reoptimizer as Reoptimizer
    from ROOT.URANIE import Sensitivity as Sensitivity
    from ROOT.URANIE import Optimizer as Optimizer
    from ROOT.URANIE import Modeler as Modeler
    from ROOT.URANIE import Calibration as Calibration
    from ROOT.URANIE import UncertModeler as UncertModeler
    from ROOT.URANIE import Reliability as Reliability
    from ROOT.URANIE import XMLProblem as XMLProblem
    from ROOT.URANIE import MpiRelauncher as MpiRelauncher
    pass
# General graphical style
white = 0
# PlotStyle
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptDate(21)
# Legend
ROOT.gStyle.SetLegendBorderSize(0)
ROOT.gStyle.SetFillStyle(0)
```

<!-- page 194 (PDF 201) -->
```python
# Pads
ROOT.gStyle.SetPadColor(white)
ROOT.gStyle.SetTitleFillColor(white)
ROOT.gStyle.SetStatColor(white)
   ====================
                         Hint ====================
     Might be practical to store this in a convenient place (for instance
     the ".python" folder in your home directory) or any other place where
     your $PYTHONPATH is pointing.
     example : export PYTHONPATH=$PYTHONPATH:${HOME}/.mypython/
     It should then be called as "from rootlogon import " + the list of module
     This would replace the shortcuts created and import done in the rest of
     the scripts
     Many style issue can be set once and for all here.
     toto=DataServer.TDataServer()
```

All the use case macros, shown in this chapter, are tested with pylint to check their consistency with python standard,
such as PEP-8, most of which obtains now (from version 4.8.0) a score of 10 out of 10. To do this, three options are
used:
• --module-naming-style=camelCase: this option is used so that evey file name can be written as their C++
counterpart (in order to overcome the default sneak_case);
• --const-naming-style=any: since our use-case macros are standalone scripts (meaning without classes) all
their variables are global ones and should be written in upper case according to pylint default. We choose not to
follow this convention;
• --ignored-module=ROOT: as ROOT is loaded from the $PYTHONPATH and not installed as a system library, many
error might pop-up from the use of ROOT;

<!-- page 195 (PDF 202) -->
Figure 13.1: Distribution of the pylint score for the following use-case macros

## 13.2 Macros Python HowTo

In this section we propose to explain how to handle some of the ROOT or C++-based object in python. The idea is just
to breakdown the already provided pieces of code shown in FAQ: a Python handbook to interact with Uranie.

### 13.2.1 Macro “howtoConvertTDataServerArray.py”

#### 13.2.1.1 Objective

The goal of this macro is only to show how to convert a TDataServer into a numpy.array and vice-versa.

#### 13.2.1.2 Macro Uranie

```python
"""
Example of TDataServer into numpy array converter
"""
import numpy as np
from URANIE import DataServer
# import data into a dataserver
tds = DataServer.TDataServer("tds", "pouet")
tds.fileDataRead("myData.dat")
print("Dumping tds")
tds.scan()
# Define the list of variable to be read
VarList = "x:y"
```

<!-- page 196 (PDF 203) -->
```python
# Create an array by defining the shape and the type (this array is a matrix)
TdsData = np.empty(shape=(tds.getNPatterns(), len(VarList.split(":"))),
                   dtype=np.float64)
# Dump the data into the created array (the last field empty unless a select is done␣
```

˓→on the sample)

```python
tds.getTuple().extractData(TdsData, TdsData.size, VarList, tds.getCut().GetTitle())
# Check the content
print("Dumping the array")
print(TdsData)
# Create a new Dataserver and feed it
tds2 = DataServer.TDataServer("brandnew", "pouet")
# Add the attribute in the dataserver and create the tuple
for name in VarList.split(":"):
    index = VarList.split(":").index(name)
    VarData = np.ascontiguousarray(TdsData.transpose()[index])
    tds2.addAttributeUsingData(name, VarData, VarData.size)
print("Dumping new tds")
tds2.Scan("*")
```

The first block reads an input file myData.dat and store the data in the TDataServer as usually done. The new block
is what we recommend: define the list of variable that one wants to store

```python
VarList = "x:y"
```

Once done, the np.array has to be constructed by defining its content and size. Thanks to the TDataServer object
and the list of variable this can be done easily as

```python
TdsData = np.empty(shape=(tds.getNPatterns(), len(VarList.split(":"))),
                   dtype=np.float64)
```

Finally, the extractData method is called with the given created array and list of variables.

```python
tds.getTuple().extractData(TdsData, TdsData.size, VarList, tds.getCut().GetTitle())
```

The second part consists in creating a brand new TDataServer from a np.array, which basically will consist in our
case in re-creatting the original TDataServer with a different name and title. To do so, one starts by creating the

```python
TDataServer
tds2 = DataServer.TDataServer("brandnew", "pouet")
```

Then, one loops over the list of variable and in the loop two things are done :
• a new array is created by transposing the data, selecting the proper array of data and construct this as an
memory-continuous array (for C++-consistency)
• a new attribute is created using the method addAttributeUsingData that needs the name of the attribute, the
buffer and the size of the array provded

```python
for name in VarList.split(":"):
    index = VarList.split(":").index(name)
```

<!-- page 197 (PDF 204) -->
```python
VarData = np.ascontiguousarray(TdsData.transpose()[index])
tds2.addAttributeUsingData(name, VarData, VarData.size)
```

The output of this macro is shown in Console.

#### 13.2.1.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
Dumping tds
************************************************
*
     Row
           * tds__n__i *
                               x.x *
                                           y.y *
************************************************
*
         0 *
                     1 *
                                -5 *
                                            25 *
*
         1 *
                     2 *
                                -4 *
                                            16 *
*
         2 *
                     3 *
                                -3 *
                                             9 *
*
         3 *
                     4 *
                                -2 *
                                             4 *
*
         4 *
                     5 *
                                -1 *
                                             1 *
*
         5 *
                     6 *
                                 0 *
                                             0 *
*
         6 *
                     7 *
                                 1 *
                                             1 *
*
         7 *
                     8 *
                                 2 *
                                             4 *
*
         8 *
                     9 *
                                 3 *
                                             9 *
*
         9 *
                    10 *
                                 4 *
                                            16 *
*
        10 *
                    11 *
                                 5 *
                                            25 *
************************************************
Dumping the array
[[-5. 25.]
 [-4. 16.]
 [-3.
       9.]
 [-2.
       4.]
 [-1.
       1.]
 [ 0.
       0.]
 [ 1.
       1.]
 [ 2.
       4.]
 [ 3.
       9.]
 [ 4. 16.]
 [ 5. 25.]]
Dumping new tds
************************************************
*
     Row
           * brandnew_ *
                               x.x *
                                           y.y *
************************************************
*
         0 *
                     1 *
                                -5 *
                                            25 *
*
         1 *
                     2 *
                                -4 *
                                            16 *
*
         2 *
                     3 *
                                -3 *
                                             9 *
*
         3 *
                     4 *
                                -2 *
                                             4 *
*
         4 *
                     5 *
                                -1 *
                                             1 *
*
         5 *
                     6 *
                                 0 *
                                             0 *
*
         6 *
                     7 *
                                 1 *
                                             1 *
*
         7 *
                     8 *
                                 2 *
                                             4 *
```

<!-- page 198 (PDF 205) -->
```python
*
         8 *
                     9 *
                                 3 *
                                             9 *
*
         9 *
                    10 *
                                 4 *
                                            16 *
*
        10 *
                    11 *
                                 5 *
                                            25 *
************************************************
```

###  13.2.2 Macro “howtoConvertTMatrixDArray.py”

####  13.2.2.1 Objective

The goal of this macro is only to show how to convert a TMatrixD object into a numpy.array and vice-versa.

#### 13.2.2.2 Macro Uranie

```python
"""
Example of TMatrix into numpy array conversion
"""
import numpy as np
import ROOT
# define the number of rows and columns
nrow = 3
ncol = 5
# Initialise and fill a TMatrixD
InMat = ROOT.TMatrixD(nrow, ncol)
for i in range(nrow):
    for j in range(ncol):
        InMat[i][j] = ROOT.gRandom.Gaus(0, 1)
print("Original TMatrixD")
InMat.Print()
# Create the ndarray with the good shape
mat_version = np.frombuffer(InMat.GetMatrixArray(), dtype=np.float64,
                            count=nrow*ncol).reshape(nrow, ncol)
print("Numpy array transformation")
print(mat_version)
# Back to another TMatrixD
OutMat = ROOT.TMatrixD(nrow, ncol)
OutMat.SetMatrixArray(mat_version)
print("\nRecreated TMatrixD")
OutMat.Print()
```

The first block simply defines the size of the matrix to be created and creates along, from scratch, a TMatrixD with a
random gaussian content. Once done, the conversion into a np.array is done in a single line manner below that would
be breakdown to get the full picture:

```python
mat_version = np.frombuffer(InMat.GetMatrixArray(), dtype=np.float64,
                            count=nrow*ncol).reshape(nrow, ncol)
```

The content of the original TMatrixD can be accessed by calling GetMatrixArray(). This returns a pointer to the first
element’s address, so it can be used by the lowest level array object of numpy, the np.frombuffer which also needs the

<!-- page 199 (PDF 206) -->
type of data and the number of elements. This is important as the memory will be scanned given these two information.
The last step is to call, on this newly created object the reshape method to create a properly organised np.array.
The second part consists in creating a brand new TMatrixD from the newly created np.array. The idea is simply to
create the object empty and use the SetMatrixArray method to dump the array content into the matrix, as done below.

```python
OutMat = ROOT.TMatrixD(nrow, ncol)
OutMat.SetMatrixArray(mat_version)
```

The output of this macro is shown in Console.

#### 13.2.2.3 Console

```python
Original TMatrixD
3x5 matrix is as follows
     |
                 |
                             |
                                         |
                                                     |
                                                                 |
----------------------------------------------------------------------
   0 |
           0.9989
                      -0.4348
                                   0.7818
                                             -0.03005
                                                           0.8243
   1 |
         -0.05672
                      -0.9009
                                  -0.0747
                                             0.007912
                                                          -0.4108
   2 |
            1.391
                      -0.9851
                                 -0.04894
                                               -1.443
                                                           -1.061
Numpy array transformation
[[ 0.99893272 -0.43476439
                           0.78179626 -0.03005277
                                                   0.82426369]
 [-0.05671733 -0.90087599 -0.07470447
                                       0.00791221 -0.41076317]
 [ 1.39119397 -0.98506611 -0.04894054 -1.44333537 -1.06067041]]
Recreated TMatrixD
3x5 matrix is as follows
     |
                 |
                             |
                                         |
                                                     |
                                                                 |
----------------------------------------------------------------------
   0 |
           0.9989
                      -0.4348
                                   0.7818
                                             -0.03005
                                                           0.8243
   1 |
         -0.05672
                      -0.9009
                                  -0.0747
                                             0.007912
                                                          -0.4108
   2 |
            1.391
                      -0.9851
                                 -0.04894
                                               -1.443
                                                           -1.061
```

###  13.2.3 Macro “howtoLoadFunction.py”

####  13.2.3.1 Objective

The goal of this macro is only to show how to load a C++ function in python as this could be of use for instance when
producing a surrogate model (all of them can be exported in C++ and even though the recommended way to handle these
is through the Uranie classes, it might happen that one wants to put one’s hand on it).
Our example is taken from the UserFunction.C file provided with the Uranie sources (look for it in the the
"$URANIESYS/share/uranie/macros" folder). The operation function only compute the product, ratio, sum
and difference between two provided inputs (just checking for consistency that the denominator of the ratio is not equal
to zero). The code is shown here for illustration purpose.

```python
void operation(double *x, Double_t *y)
{
```

<!-- page 200 (PDF 207) -->
```python
  Double_t x1 = x[0], x2 = x[1];
  // product
  y[0] = x1 * x2;
  // divide
  y[1] = ((x2!=0) ? x1 / x2 : -999);
  // sum
  y[2] = x1 + x2;
  // diff
  y[3] = x1 - x2;
}
```

####  13.2.3.2 Macro Uranie

```python
"""
Example of C++ function in python
"""
import numpy as np
import ROOT
# Loading a function
ROOT.gROOT.LoadMacro("UserFunctions.C")
# Preparing inputs and outputs
inp = np.array([1.2, 0.8])
                            # input values
out = np.zeros(4)
                   # output values initialise with 4 zeros
# Call the method, through the ROOT interface
ROOT.operation(inp, out)
# Print the result
print("Results are")
print(out)
```

The first block simply loads the input file UserFunctions.C through the ROOT’s interface.

```python
ROOT.gROOT.LoadMacro("UserFunctions.C")
```

Once done, the input and output np.array object are created, the former with provided values to be tested, the latter
only filled with zeros. Calling the function is simply done by providing input and output arrays to the function operator
that is now stored within ROOT by doing:

```python
ROOT.operation(inp, out)
```

The output of this macro is shown in Console.

#### 13.2.3.3 Console

```python
Results are
[0.96 1.5
           2.
                0.4 ]
```

<!-- page 201 (PDF 208) -->
### 13.2.4 Macro “howtoPassReference.py”

#### 13.2.4.1 Objective

The goal of this macro is to show how to use function that would have been defined using the “by-reference” prototype,
which is specific to C++. A simple exemple in Uranie is provided when considering the computeQuantile method:
the second argument is a double in which the result will be stored.

#### 13.2.4.2 Macro Uranie

```python
"""
Example of C++style reference usage
"""
from ctypes import c_double
                             # for ROOT version greater or equal to 6.20
from URANIE import DataServer
# create a dataserver and read data
tds = DataServer.TDataServer("pouet", "foo")
tds.fileDataRead("myData.dat")
# compute quantile (this method get the results 'by reference')
proba = 0.9
             # ROOT.Double(0.9) for ROOT version lower than 6.20
quant = c_double(0.0)
                       # ROOT.Double(0.0) for ROOT version lower than 6.20
# Compute the quantile and dump the value returned by reference
tds.computeQuantile("x", proba, quant)
print("Result is ")
print(quant.value)
```

It starts by calling the ctypes module in order to get the c_double interface. This is only for ROOT version greater
than 6.20. For older version, the solution relied on ROOT only (calling another interface discussed later-on).

```python
from ctypes import c_double
                             # for ROOT version greater or equal to 6.20
```

Once done, a TDataServer object is created and filled from the myData.dat file. One then wants to estimate the 90%
quantile, which can be done by calling the computeQuantile method, which requires two double as input, both passed
“by-reference”. To do so, one has to create two specific objects as below:

```python
proba = 0.9
             # ROOT.Double(0.9) for ROOT version lower than 6.20
quant = c_double(0.0)
                       # ROOT.Double(0.0) for ROOT version lower than 6.20
```

Once done, the method is called and the result is displayed by getting the value of the c_double object

```python
print(quant.value)
```

The output of this macro is shown in Console.

#### 13.2.4.3 Console

```python
--- Uranie v4.11/0 --- Developed with ROOT (6.36.06)
                      Copyright (C) 2013-2026 CEA/DES
                      Contact: support-uranie@cea.fr
                      Date: Thu Feb 12, 2026
```
