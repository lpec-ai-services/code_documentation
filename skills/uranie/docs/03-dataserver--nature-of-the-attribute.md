# The DataServer module — The TAttribute class — Nature of the attribute … Examples of use of the class TAttribute
<!-- source PDF pages 30-34 -->

<!-- page 23 (PDF 30) -->
The creation of a TDataServer (with many construction, from ASCII to ROOT files) is discussed in Data handling
before discussing the basic statistical treatment (in Statistical treatments and operations) and the dedicated visualisation
tool (in Visualisation dedicated to uncertainties).
Lightbulb Tip
An important point to know for the use of Uranie: all options are not case sensitive. Actually, the treatment of these
options is taken anyway as lowercase. The following instructions are equivalent:

```python
tdsGeyser.draw("x1","","Nclass=Sturges")
tdsGeyser.draw("x2","","nclass=Sturges")
tdsGeyser.draw("x2","","nclass=sturges")
tdsGeyser.draw("x2","","NCLASS=STURGES")
```

##  2.2 The TAttribute class

The TAttribute class (as its inherited classes, some of which are discussed here as well), is also a crucial part of any
analysis performed through Uranie. It describes any variable (input, output, or internal variable such as iterator) that are
passed to the other modules. It does not really contain the data, but it has the statistical information (in case methods such
as computeStatistic or computeQuantile have been called, see Statistical treatments and operations

### 2.2.1 Nature of the attribute

Unlike previous Uranie-version where all attribute were double-precision float values, the implementation done from
v3.10.0 allows to handle two other types of attribute: string and vector.
There are several ways to define the
new attribute nature, following the chosen construction process, but all these methods will affect the enumerator
URANIE::DataServer::EType whose value can be:
• kDefault: the default one which is equal to kReal
• kString: in the case of text input (assuming that this text is no split into more than one word, unless extra-cautions
are taken)
• kVector: for vectors of double-precision values. Even though the number of elements within this vector can
change from one pattern to the other, many useful methods discussed in the following sections and chapters will
required (in order to make sense) to have a constant number of elements (at least for a sub-selection of patterns).
This is particularly true for all mathematical methods and sensitivity analysis. The code should complain if this
requirement is needed and not fulfilled.
This new implementation is bringing changes in the way some information are handled, as for the attribute is concerned,
but all the resulting modification have been checked to be backward compatible. Default settings are made assuming
that attributes are double-precision ones, unless specified otherwise (to be sure that all previous script will work).
The corresponding modifications are discussed throughout this documentation.

### 2.2.2 List of variable information

We will present in this section the list of information contained in a TAttribute of Uranie.

<!-- page 24 (PDF 31) -->
Figure 2.2: Attributes of TAttribute class
Name: Variable name
It should be a short name as this information is needed to use this variable (mathematical expressions, graphics,
scan, …).
Title: Variable title.
This information is only needed for graphical display.
Unit: Variable units.
This information is only needed for graphical display.
Note: Variable note.
description of the variable, this is not currently used.
Min, Max, Mean and Std: Minimum, maximum, averaged and standard deviation values.
These information are now vectors and their usage is discussed in Computing the elementary statistic
vquantile: Vector of map containing value of the quantile computed using the key in argument.
These information are now stored in the attribute itself their usage is discussed in The quantile computation
defaultValue: Default value.
This default value will be considered either by the code launcher or during a parameter optimisation. In the case
of a code launcher, this means either that the code failed to proceed or that the code did not return the value.
At this level, there is no notion of random variable. Attributes are variables with a name, a label, a unit, a variation
domain (bounded or belonging to R). Despite the large amount of possible combinations to instantiate a variable (name,
name+label, name+boundary, name+label+boundary), only a small number of constructors are implemented. Some
methods like setTitle, setFileKey, setUnity allow to precise the missing information.
The four constructors currently implemented are the following:
• Name: since this constructor only knows the name of the variable, the 3 piece of information title, label and key
are strictly identical. This variable is not bounded. An example of use, already seen before, is:

```python
px = DataServer.TAttribute("x")
```

A random variable “x” (where px denotes a pointer to x) exists and it has its label also equal to x. Thus, if this
variable is visualised on a graph, the default label will also be its title i.e “x”.
• Name + title: constructor defined from the name and the title of the variable

<!-- page 25 (PDF 32) -->
```python
psdp = DataServer.TAttribute("sdp", "#sigma_{#Delta P}")
psdp.setUnity("M^{2}")
```

A pointer psdp to a variable “sdp” is available with title being #sigma_{#Delta P}. The command setUnity()
precises the unit. In this case, by default, the field key is identical to the field name. We will use the ability
given by ROOT to write LaTeX expressions in graphics to improve graphics rendering without weighing down the
manipulation of variables: as a matter of fact, we can plot the histogram of the variable sdp by:

```python
tdsGeyser.addAttribute("sdp", "x2", "#sigma_{#Delta P}", "M^{2}")
tdsGeyser.draw("sdp")
```

The result of this piece of code is shown in Figure 2.3.
Figure 2.3: Graph of the variable sdp
• Name + variation boundary: constructor defined by the name of the variable and the lower and upper boundaries.
The two other pieces of information, label and key remain equal to the title. An example of use is

```python
x = DataServer.TAttribute("x", -2.0, 4.0)
```

• Name + EType: constructor defined by the name of the variable and nature of the corresponding attribute . An
example of use is

```python
xvec = DataServer.TAttribute("x", DataServer.TAttribute.kVector)
```

Setter methods allow to fill the other fields (title, key, etc ) generally by calling set and the name of the information to be
modified (a restricted list of available methods being given below). For instance, the plot “x2:x1” of TDataServer data
tdsGeyser (whose data file geyser.dat can be found in the Uranie-macros folder) can be considered again and we can
replace the fields title and unit with new values by using LaTeX instructions. For instance, let us consider once again the
graph of TDataServer data tdsGeyser:

```python
px1 = tdsGeyser.getAttribute("x1")
px1.setTitle("#Delta P^{#sigma}")
                                   # Change the title
px1.setUnity("#frac{mm^{2}}{s}")
                                  # Change the unit
tdsGeyser.draw("x2:x1") # Draw the plot
```

<!-- page 26 (PDF 33) -->
The first line consists in retrieving the attribute pointer x1, while the others are self explanatory. This results in a new
graph (scatterplot) of x2 versus x1 for the TDataServer constructed from the geyser file with updated field title and unit
values, shown in Figure 2.4.
Figure 2.4: Scatterplot x2 versus x1 for the geyser data with modification of fields title and unit
Most of the information can be modified by “setter” methods. Here is a short list of the most relevant one starting with
simple and already discussed attribute properties:
• setTitle(TString str): assigns the character string str passed as argument to the field title;
• setUnity(TString str: assigns the character string str passed as argument to the field unity;
• setNote(TString str): assigns the character string str passed as argument to the field note;
• setUpperBound/setLowerBound/setDefaultValue(double val): assigns or changes (if it already existed) respectively
the upper, lower or default value for this attribute.
• setDataType(EType thetype or TString str): changes the nature of the attribute given the enumerator value or a
character chain (case insensitive). In the latter case, the enumerator is set to:
– kReal: str = “double” or “real” or “d”;
– kString: str = “string” or “s”
– kVector: str = “vector” or “v”
Given the new nature of attributes (meaning vectors and strings) a more generic method has been created to put default
values to all type. The generic methods takes only one argument, a string containing values whatever the type. In cas of
doubt, dedicated methods have also been created, with dedicated prototypes:
• kReal: both setDefault(TString value) and Bool_t setDefaultValue(Double_t val) can be used
as shown below

```python
real = DataServer.TAttribute("real")
real_value=1.23456789
real.setDefaultValue(real_value)
                                  # Default with double value
real.setDefault("1.23456789")
                               # Default with generic method
```

<!-- page 27 (PDF 34) -->
• kVector: both setDefault(TString
value) and setDefaultVectorvector<double>
&vec) can be
used as shown below

```python
import numpy as np
vector = DataServer.TAttribute("vector", DataServer.TAttribute.kVector)
v_value = ROOT.std.vector("double")([1.2, 2.3, 3.4])
vector.setDefaultVector(v_value)
                                  # Default with double value
vector.setDefault("1.2,2.3,3.4")
                                  # Default with generic method
```

• kString: both setDefault(TString value) and setDefaultString(TString val) can be used as shown
below

```python
string = DataServer.TAttribute("string", DataServer.TAttribute.kString)
str_value = "chocolat"
string.setDefaultString(str_value)
                                    # Default with double value
string.setDefault(str_value)
                              # Default with generic method
```

There are also important setters, used to connect attributes to ASCII files. Most of the time, ASCII files are indeed used
to communicate with an external code and Uranie must know in this case where to find the useful information for the
corresponding attributes (either to write a new value that would be used as input to perform a calculation or to read the
output of another computation). This is more carefully detailed in Code input and output files.
• setFileKey(TString sfile, TString skey,TString sformatToSubstitute, TAttributeFileKey::EFileType sFileType): allows
to specify for an attribute a file sfile, a key linked to this file skey, a writing format of the value of this key in
the previous file sformatToSubstitute, and also the type of the file sFileType. This is heavily discussed in The
Launcher module.

### 2.2.3 Examples of use of the class TAttribute

The following instruction defines a pointer px to an unbounded variable x.

```python
px = DataServer.TAttribute("x")
```

The following instruction defines a pointer px to a variable x bounded between 0. and 1.

```python
px = DataServer.TAttribute("x", 0., 1.)
```

The following instruction defines a pointer px to a variable x bounded between -2. and 4. with Δ𝑃𝐹𝑖𝑠𝑜
𝑒
as label:

```python
px = DataServer.TAttribute("x", -2.0, 4.0)
px.setTitle("#Delta P_{e}^{F_{iso}}")
```

The following instruction defines a pointer px to a variable x that describes string

```python
px = DataServer.TAttribute("x", DataServer.TAttribute.kString)
```

###  2.2.4 Adding TAttribute when data are already available

It is possible to add new attribute in a given TDataServer object that would contain data using two different methods.
The first one rely on the already existing data to create a new variable by simply writting the equation, which internally
is calling a TAttributeFormula object. The following piece of code shows how to create a third variable from the
geyser.dat file, simply as an equation from the existing variables:
