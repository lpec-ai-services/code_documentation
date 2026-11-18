# The Sampler module — Introduction … The random fields
<!-- source PDF pages 107-120 -->

<!-- page 100 (PDF 107) -->
THE SAMPLER MODULE
Abstract
This is a description of the Sampler module whose main goal is to produce a design-of-experiments, starting
from the description of the model provided by the user, and that would be used to investigate the sensitivity and/or
propagate uncertainty for the requested analysis.
The source files are in souRCE.git/meTIER/sampler/souRCE and the corresponding namespace is URANIE::Sampler
.

## 3.1 Introduction

The Sampler module is used to produce design-of-experiments knowing the expected behaviour of the input variables for
the problem under consideration. The framework of our approach can be illustrated in the following schematic view:
Figure 3.1: Schematic view of the input/output relation through a code
• We will denote as 𝒞the studied computational code which, generally, has two types of inputs:
– The constant parameters which are gathered in the vector c ∈IR𝑛𝐶. They represent constants.
– The uncertain parameters which are gathered in the vector X ∈IR𝑛𝑋
It shall be noticed that these parameters are supposed to be uncertain either because of a lack of knowledge
on their actual value or because of their intrinsic random nature.
• The result of the code 𝒞for a given set of parameters (c, X) gives the vector 𝑦∈IR𝑛𝑌= 𝒞(c, X) which contains
all the output variables of the analysis.

<!-- page 101 (PDF 108) -->
Different methods exist to obtain a design-of-experiments from uncertain parameters which can be classified into two
categories:
1. stochastic methods (see The Stochastic methods). These methods consist in using a random number generator to
produce new samples. This is also called Monte-Carlo.
2. deterministic methods (see QMC method). Two distinct calls with the same parameters will always give the same
point in a design-of-experiments. Some of these methods (those discussed below) are sequences which are sometimes
called quasi-Monte Carlo (qMC).

## 3.2 The Stochastic methods

### 3.2.1 Introduction

The stochastic classes all inherit from the TSampler class through the TSamplerStochastic one. In these classes the
knowledge (or mis-knowledge) of the model is encoded in the choice of probability law used to describe the inputs 𝑥𝑖,
for 𝑖∈[0, 𝑛𝑋]. These laws are usually defined by:
• a range that describes the possible values of 𝑥𝑖
• the nature of the law, which has to be taken in the list of TStochasticAttribute already presented in Introducing
the TStochasticAttribute classes
A choice has frequently to be made between two implemented methods of drawing:
SRS (Simple Random Sampling):
This method consists in independently generating the samples for each parameter following its own probability
density function. The obtained parameter variance is rather high, meaning that the precision of the estimation is
poor leading to a need for many repetitions in order to reach a satisfactory precision. An example of this sampling
when having two independent random variables (uniform and normal one) is shown in Figure 3.3-left.
LHS (Latin Hypercube Sampling):
this method [MBC00] consists in partitioning the interval of each parameter so as to obtain segments of equal
probabilities, and afterwards in selecting, for each segment, a value representing this segment. An example of this
sampling when having two independent random variables (uniform and normal one) is shown in Figure 3.3-right.
Both
methods
consist
in
generating
a
𝑁calc-sample
represented
by
a
matrix
𝑈
called
matrix
of
the
design-of-experiments.
The number of columns of the matrix 𝑈correspond to the number of uncertain parameters
𝑛𝑋, and the number of lines is equal to the size of the sample 𝑁calc.
The first method is fine when the computation time of a simulation is “satisfactory”. As a matter of fact, it has the advantage
of being easy to implement and to explain; and it produces estimators with good properties not only for the mean value
but also for the variance. Naturally, it is necessary to be careful in the sense to be given to the term “satisfactory”. If
the objective is to obtain quantiles for extreme probability values 𝛼(i.e. 𝛼= 0.99999 for instance), even for a very low
computation time, the size of the sample would be too large for this method to be used. When a computation time
becomes important, the LHS sampling method is preferable to get robust results even with small-size samples (i.e. 𝑁calc
= 50 to 200) [HD02]. On the other hand, it is rather trivial to double the size of an existing SRS sampling, as no extra
caution has to be taken apart from the random seed.
In Figure 3.2, we present two samples of size 𝑁calc = 8 coming from these two sampling methods for two random variables
𝑈1 according to a gaussian law, and 𝑈2 a uniform law. To make the comparison easier, we have represented on both figures
the partition grid of equiprobable segments of the LHS method, keeping in mind that it is not used by the SRS method.
These figures clearly show that for LHS method each variable is represented on the whole domain of variation, which is
not the case for the SRS method. This latter gives samples that are concentrated around the mean vector; the extremes of
distribution being, by definition, rare.
Concerning the LHS method (right figure), once a point has been chosen in a segment of the first variable 𝑈1, no other
point of this segment will be picked up later, which is hinted by the vertical red bar. It is the same thing for all other
variables, and this process is repeated until the 𝑁calc points are obtained. This elementary principle will ensure that the

<!-- page 102 (PDF 109) -->
domain of variation of each variable is totally covered in a homogeneous way. On the other hand, it is absolutely not
possible to remove or add points to a LHS sampling without having to regenerate it completely. A more realistic picture
is draw in Figure 3.3 with the same laws, both for SRS on the left and LHS on the right. The “tufte” representation
(presented in Graph 2D “Tufte”) clearly shows the difference between both methods when considering one-dimensional
distribution.
Figure 3.2: Comparison of the two sampling methods SRS (left) and LHS (right) with samples of size 8.
Figure 3.3: Comparison of deterministic design-of-experiments obtained using either SRS (left) or LHS (right) algorithm,
when having two independent random variables (uniform and normal one)

<!-- page 103 (PDF 110) -->
There are two different sub-categories of LHS design-of-experiments discussed here and whose goal might slightly differs
from the main LHS design discussed above:
• the maximin LHS: this category is the result of an optimisation whose purpose is to maximise the minimal distance
between any sets of two locations. This is discussed later-on in The main sampler classes.
• the constrained LHS: this category is defined by the fact that someone wants to have a design-of-experiments
fulfilling all properties of a Latin Hypercube Design but adding one or more constraints on the input space definition
(generally inducing correlation between varibles). This is also further discussed in The main sampler classes and in
TConstrLHS example.
Once the nature of the law is chosen, along with a variation range, for all inputs 𝑥𝑖, the correlation between these variables
has to be taken into account. This is further discussed in Description of a correlation

### 3.2.2 The main sampler classes

The sampler classes are built with the same skeleton. They consist in a three steps procedure: init, generateSample
and terminate. There are five different types of Stochastic sampler that can be used:
• TSampling: general sampler where the sampling is done with the Iman and Conover methods ([IC82]) that uses a
double Cholesky decomposition in order to respect the requested correlation matrix. This methods has the drawback
of asking a number of samples at least twice as large as the number of attribute.
• TBasicSampling: very simple implementation of the random sampling that can, as well, produce stratified sampling
. As it is fairly simple, there is no lower limit in the number of random samples that can be generated and
generation is much faster when dealing with a large number of attributes than with the TSampling. On the other
hand, even though a correlation can be imposed between the variables, it will be done in a simple way that cannot
by construction respect the stratified aspect (if requested, see [Bla17] explanations).
• TMaxiMinLHS: class recently introduced to produced maximin LHS, whose purpose is to get the best coverage of
the input space (for a deeper discussion on the motivation, see [Bla17]). It can be used with a provided LHS drawing
or it can start from scratch (using the TSampling class to get the starting point). The result of this procedure can
be seen in Figure 13.14 which was procuded with the macro introduced in Macro “samplingMaxiMinLHSFromLHS-
Grid.py”;
Lightbulb Tip
The optimisation to get a maximin LHS is done on the mindist criterion: let 𝐷= [x1, · · · , x𝑁] ⊂[0, 1]𝑑be a
design-of-experiments with 𝑁points. The mindist criterion is written as: min𝑖,𝑗||x𝑖−x𝑗||2 where ||.||2 is the
euclidian norm.
This information can be computed on any grid, by calling the static function

```python
mindist = Sampler.TMaxiMinLHS.getMinDist(LHSgrid)
```

• TConstrLHS: class recently introduced to produced constrained LHS, whose purpose is to get nicely covered
marginal laws while respecting one or more constraints imposed by the user. It can be used with a provided LHS
drawing or it can start from scratch (using the TSampling class to get the starting point) and it is discussed a bit
further in TConstrLHS example. The result of this procedure can be seen in Figure 13.15 which was procuded with
the macro introduced in Macro “samplingConstrLHSLinear.py”;
• TGaussianSampling: very basic sampler specially done for cases composed with only normal distributions. It
relies on the drawing of a sample 𝐴(𝑛𝑆, 𝑛𝑋) 𝑛𝑆being the number of sample and 𝑛𝑋the number of inputs.
The sample is transformed to account for correlation (see [Bla17]) and shifted by the requested mean (for every
variables).

<!-- page 104 (PDF 111) -->
• TImportanceSampling: use the same method as TSampling but should be used when one TAttribute has a
son. In this case the range for the considered attribute is the sub-range used to define the son and there is specific
reweighting procedure to take into account the fact that the authorised range is reduced. LHS is therefore used by
default.

### 3.2.3 Simple example

The following piece shows how to generate a sample using the TSampling class.

```python
xunif = DataServer.TUniformDistribution("x1", 3., 4.)
                                                       # 1
xnorm = DataServer.TNormalDistribution("x2", 0.5, 1.5)
                                                        # 2
tds = DataServer.TDataServer("tdsSampling", "Demonstration Sampling")
tds.addAttribute(xunif)
tds.addAttribute(xnorm)
# Generate the sampling from the TDataServer object
sampling = Sampler.TSampling(tds, "lhs", 1000)
                                                # 3
sampling.generateSample()
                           # 4
tds.drawTufte("x1:x2")
                        # 5
```

Generation of a design-of-experiments with stochastic attributes
1. Generating a uniform random variable in [3., 4.]
2. Generating a gaussian random variable with a mean of 0.5 and a standard deviation of 1.5
3. Construct the sampler object requesting a sample of 1000 events, using the Lhs algorithm.
4. Method to generate the sample.
5. Draw the plot as the right side of Figure 3.3

### 3.2.4 TConstrLHS example

This section will discuss the way to produce a constrained LHS design-of-experiments from scratch, focusing on the main
problematic part: defining one or more constraints and on which variable to apply them. The logic behind the heuristic
is supposed to be known, so if it’s not the case, please have a look at the dedicated section in [Bla17]. This section will
mostly rely on the way to define the constraints and the variables on which these should be applied on which are specified
by the method addConstraint. This methods takes 4 arguments:
1. a pointer to the function that will compute the constraints values;
2. the number of constraint defined in the function discussed above;
3. the number of parameters that are provided to the function discussed above;
4. the values of the parameters that are provided to the function discussed above;
The main object is indeed the constraint function and the way it is defined is discussed here. It is a C++ function (for
convenience as the platform is C++-coded) but this should not be an issue even for python users. The followings lines are
showing the example of the constraint function used to produce the plot in Macro “samplingConstrLHSLinear.py”.

```python
void Linear(double *p, double *y)
{
    double p1=p[0], p2=p[1];
    double p3=p[2], p4=p[3];
    // Linear constaint
```

<!-- page 105 (PDF 112) -->
```python
    y[0] = (( (p1 + p2>=2.5) || (p1-p2<=0) ) ? 0 : 1);
    y[1] = ((p3 - p4<0) ? 0 : 1);
}
```

Here are few elements to discuss and explain this function:
• its prototype is the usual C++-ROOT one with a pointer to the input parameter p and a pointer to the output (here
the constraint results) y;
• the first lines are defining the parameters, meaning the couples (𝑥𝑟𝑜𝑤, 𝑥𝑐𝑜𝑙) for all the constraints. By convention,
the first element of every line (𝑝1 and 𝑝3) are of the row type (they will not change in the design-of-experiments
through this constraint, see [Bla17] for clarification) while the second parameters (𝑝2 and 𝑝4) are of the column
type, meaning their order in the design-of-experiments will change through permutations through this constraint.
• the rest of the lines are showing the way to compute the constraints and to interpret them thanks to the trilinear
operator (even though the classical if, else would perfectly do the trick as well. Let’s focus first on the second
constraint:

```python
y[1] = ((p3 - p4<0) ? 0 : 1);
```

if p3 is lower than p4 (p3-p4<0) then the function will put 0 in y[1] (stating that this configuration is not fulfilling
the constraint), and it will put 1 otherwise (stating that the constraint is fulfilled). The other line is defining another
constraint which is composed of two tests on the same couple of variables:

```python
y[0] = (( (p1 + p2>=2.5) || (p1-p2<=0) ) ? 0 : 1);
```

Here, two constraints are combined in once, as they affect the same couple of variables, the configuration will be
rejected either if p1+p2 is greater than 2.5 or if p1 is lower than p2.
Once done, this function needs to be plugged into our code in order to state what variables are p1, p2, p3 and p4 so that
the rest of the procedure discussed in [Bla17] can be run. This is done in the addConstraint method, thanks to the third
and fourth paramaters which are taken from a single object: a vector<int> in C++ and a numpy.array in python.
It defines a list of indices (integers) that corresponds to the number of the input attributes as it is has been added into
the TDataServer object. For instance in our case, the list of input attributes is "x0:x1:x2" while the constraints are
coupling (𝑥1, 𝑥0) and (𝑥2, 𝑥1) respectively. Once translated in term of indices, the constraints are coupling respectively
(1, 0) and (2, 1), so the list of parameter should reflect this which is shown below:

```python
inputs = numpy.array([1, 0, 2, 1], dtype='i')
constrlhs.addConstraint(ROOT.Linear, 2, len(inputs), inputs)
```

Exclamation-Triangle Warning
The consistency between the function and the list of parameters is up to you and you should keep a carefull watch
over it. It is true that an inequality can be written in two ways, as
𝑥1 −𝑥0 < 0
⇔
𝑥0 −𝑥1 > 0
but when the constraint is defined as

```python
y[0] = ((p[0] - p[1]<0) ? 0 : 1);
```

the results will be drastically different if the list of parameters is (1, 0) (which should fulfill the constraint shown above)
or (0, 1) which would results in the exact opposite behaviour (and might make the heuristic crash if the constraint
cannot be fulfilled).

<!-- page 106 (PDF 113) -->
## 3.3 Description of a correlation

We will describe in this section how to precise in Uranie the necessary information to take into account the correlations
between variables. There are two ways to specify this: setting the correlation coefficient by hand or couple the two
considered attributes with a copula. Both methods are described below.

### 3.3.1 Imposing the correlation coefficients

It is possible to set the correlation coefficient by hand, using the setUserCorrelation method of both TSampling
and TBasicSampling.

```python
xunif = DataServer.TUniformDistribution("x1", 3., 4.)
                                                       # 1
xnorm = DataServer.TNormalDistribution("x2", 0.5, 1.5)
                                                        # 2
tds = DataServer.TDataServer("tdsSampling", "Demonstration Sampling")
tds.addAttribute(xunif)
tds.addAttribute(xnorm)
# Generate the sampling from the TDataServer object
sampling = Sampler.TSampling(tds, "lhs", 1000)
sampling.setUserCorrelation(xunif, xnorm, 0.90)
                                                 # 3
sampling.generateSample()
                           # 4
tds.Draw("x2:x1", "", "")
```

Specification of a correlation
1. Generating a uniform random variable in [3., 4.]
2. Generating a gaussian random variable with 0.5 as mean value 1.5 as standard deviation.
3. Specification of correlation of 0.90 between the two attributes xunif and xnorm.
4. Generate the sample by calling the generateSample method in TSampling (respectively the generate-
CorrSample method in TBasicSampling).
The coefficient provided is changing the correlation between the two considered attributes (for a more general discussion on
this, see [Bla17]). As an example, Figure 3.4 and Figure 3.5 show the design-of-experiments created with the TSampling
class, using a normal and uniform distribution, using three different correlation coefficient values: 0, 0.45 and 0.9. The
first one is showing the obtained 2D plan and their corresponding projections, while the second one is showing the same
information but displaying their rank instead of their values (this is further discussed in [Bla17]).

<!-- page 107 (PDF 114) -->
Figure 3.4: Tufte plot of the design-of-experiments created using a normal and uniform distribution, with a LHS method
with three correlation coefficient: 0, 0.45 and 0.9
Figure 3.5: Tufte plot of the rank of the design-of-experiments created using a normal and uniform distribution, with a
LHS method with three correlation coefficient: 0, 0.45 and 0.9
Instead of provided one-by-one the correlation factors, one can provide the correlation matrix using the setCorrelation
Matrix method of both TSampling and TBasicSampling. This method ask for a TMatrixD input and it will
check that:
• the dimension is correct : (𝑛𝑋, 𝑛𝑋).
• the coefficient are all in the range [−1, 1]

<!-- page 108 (PDF 115) -->
• the diagonal term are exactly at one (if not it sets them to this value).

#### 3.3.1.1 Case of singular correlation matrix

In the case where the correlation matrix injected (at once or component by component) happen to be singular, the default
method used to correlate variables will failed and complains in this way (taking the TBasicSampling as an example):

```python
<URANIE::ERROR>
<URANIE::ERROR> *** URANIE ERROR ***
<URANIE::ERROR> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TBasicSampling.cxx]␣
```

˓→Line[427]

```python
<URANIE::ERROR> TBasicSampling::generateCorrSample: the cholesky decomposition of the␣
```

˓→user correlation matrix is not good.

```python
<URANIE::ERROR>
                 Maybe you can try with SVD decomposition.
<URANIE::ERROR> *** END of URANIE ERROR ***
<URANIE::ERROR>
```

There is a workaround, provided by Uranie and heavily discussed in [Bla17]. The idea in a nutshell is to remplace the
Cholesky operation by a SVD one, to decompose the target correlation matrix. This can be done adding “svd” in the
Option_t *option field of either the constructor of the class or the generator method call. Here is an example for the
TBasicSampling class:

```python
tbs = Sampler.TBasicSampling(tds, "lhs;svd", 100)
                                                   # example at constructor
# .. or ..
tbs.generateCorrSample("svd")
                               # example with generator function call
```

Here comes its equivalent piece of code for the TSampling class:

```python
ts = Sampler.TSampling(tds, "lhs;svd", 100)
                                             # example at constructor
# .. or ..
ts.generateSample("svd")
                          # example with generator function call
```

In both cases, the use of this workaround should print this message to warn you about this.

```python
<URANIE::INFO>
<URANIE::INFO> *** URANIE INFORMATION ***
<URANIE::INFO> *** File[${SOURCEDIR}/meTIER/sampler/souRCE/TBasicSampling.cxx]␣
```

˓→Line[371]

```python
<URANIE::INFO> TBasicSampling::generateCorrSample: you've asked to use SVD instead of␣
```

˓→Cholesky to decompose the correlation matrix.

```python
<URANIE::INFO> *** END of URANIE INFORMATION ***
<URANIE::INFO>
```

An example of how to use this in real condition (with a proper singular correlation matrix) is shown in Macro “sampling
SingularCorrelationCase.py”.

### 3.3.2 The copula classes

Instead of using samplers with correlation matrix in the case of intricate variables, one can use classes relying on Copula,
in order to describe the dependencies. These classes inherit from the TCopula class successively through the TSampler
Stochastic and the TSampler classes. The idea of a copula is to define the interaction of variables using a
parametric-function that can allow a broader range of entanglement than only using a correlation matrix (various shapes
can be done). There are two kinds of copulas provided in the Uranie platform:
• TArchimedian
with
pre-defined
parametrisation:
Ali-Mikhail-Haq
(TAMHCopula),
Clayton
(TClaytonCopula), Frank (TFrankCopula) and Plackett (TPlackettCopula).
These copulas, which

<!-- page 109 (PDF 116) -->
depend only on the input variables and a parameter 𝜃, are shown from Figure 3.6 to Figure 3.9 for different 𝜃
values along with the formula of the corresponding parametric function.
• TElliptical: it is a class to interface the TGaussian copula method.
Figure 3.6: Example of sampling done with half million points and two uniform attributes (from 0 to 1), using AMH
copula and varying the parameter value.
Figure 3.7: Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Clayton
copula and varying the parameter value.

<!-- page 110 (PDF 117) -->
Figure 3.8: Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Frank
copula and varying the parameter value.
Figure 3.9: Example of sampling done with half million points and two uniform attributes (from 0 to 1), using Plackett
copula and varying the parameter value.
The following example shows how to create a copula and to use it in order to get a correlated sample.

```python
xunif = DataServer.TUniformDistribution("x1", 3., 4.)
xnorm = DataServer.TNormalDistribution("x2", 0.5, 1.5)
tds = DataServer.TDataServer("tdsSampling", "Demonstration Sampling")
tds.addAttribute(xunif)
tds.addAttribute(xnorm)
```

<!-- page 111 (PDF 118) -->
```python
# Generate the sampling from the TDataServer object
tamh = Sampler.TAMHCopula(tds, 0.75, 1000)
tamh.generateSample()
tds.Draw("x2:x1", "", "colZ")
```

##  3.4 QMC method

The deterministic samplings can produce design-of-experiments with well defined properties, that can be very useful in
specific cases such as:
• to cover at best the space of the input variables
• to explore the extreme cases
• to study combined or non-linearity effect
There are two kinds of quasi Monte-Carlo sampling methods implemented in Uranie: the regular ones and the sparse grid
ones. On the first hand, the former can be generated using two different sequences:
1. Sequences of Sobol [Sobol67]
2. Sequences of Halton [Hal64]
Figure 3.10 shows a comparison of the design-of-experiments obtained with both sequences, along with the ones produced
with a basic stochastic sampling, following the LHS and SRS “recipes”, all when dealing with two uniform attributes.
The coverage is clearly more regular in the case of quasi Monte-Carlo sequences which is the origin of their name:
low-discrepancy sequences. There are plenty definitions for the notion of discrepancy (see litterature for them) but they
all quantify how close the sequence is to a perfect equidistribution of points.
Exclamation-Triangle Warning
The Halton sequence has been designed initially to deal with uniform probability law. Extending their use to all
probability laws, particularly to infinite-based, it is crucial to set at least lower-bound to these. The Halton sequence
first value is indeed 0 and this means that going back from probability space to physical one, would imply −∞value
if not properly bounded.
From version 4.3.0, the TQMC will complain about infinite-based law if lower-bounded and from version 4.6.0 it will
be fully deprecated.
Figure 3.10: Comparison of both quasi Monte-Carlo sequences with both LHS and SRS sampling when dealing with two
uniform attributes.

<!-- page 112 (PDF 119) -->
On the other hand, the sparse grid sampling can be very useful for integration purposes and can be used in some of
the meta-modelling definition, see, for instance, in The integration method. In Uranie we can used the Petras algorithm
[Pet01] to produce these sparse grids, shown for different levels in Figure 3.11, that can be compared to regular algorithms
ones in Figure 3.10 (in both cases, the problem is described with two uniform attributes).
Figure 3.11: Comparison of design-of-experiments made with Petras algorithm, using different level values, when dealing
with two uniform attributes.
In the case of regular sequence, the selected sequence is specified with the second argument option of the class constructor
TQMC:

```python
TQMC(tds, option, nCalcul )
```

First, a pointer to a TDataServer is constructed

```python
tdsqmc = DataServer.TDataServer("tdsQMC", "Test for qMC")
tdsqmc.addAttribute(DataServer.TAttribute("x_{1}", -1.0 , 2.))
tdsqmc.addAttribute(DataServer.TNormalDistribution("x_{2}",
                                                             0.0 , 3.))
tdsqmc.addAttribute(DataServer.TAttribute("x_{3}",
                                                    1.0, 1.5))
```

Then, a pointer to a TQMC object is constructed from a TDataServer, of the opted sequence among (“sobol”|”halton
”), with the wished size. At the end, the method generateSample() is applied

```python
qmc = Sampler.TQMC(tdsqmc, "sobol", 300)
qmc.generateSample()
```

##  3.5 The random fields

The random fields allow to take into account the spatial characteristics of a random variable.
A TDataServer is associated to a spatial random variable from IR, IR2 or IR3 in IR. Currently only one Spectral method,
with two types of variograms (Gaussian and Sine Cardinal), is available in Uranie.
For instance, Uranie code is:

```python
# Define the DataServer
tds = DataServer.TDataServer("TDSField", "Weight as Field")
tds.addAttribute(DataServer.TAttribute("x", 1, 51))
tds.addAttribute(DataServer.TAttribute("y", 1, 51))
tds.addAttribute(DataServer.TAttribute("Weight"))
```

<!-- page 113 (PDF 120) -->
```python
# Gaussian Sampler Field
tsf = Sampler.TSamplerField(tds)
                                  # 1
tsf.SetScaleFactor(10.0)
tsf.SetRandomFunction(1000)
tsf.setVariogram("gauss")
tsf.SetVariance(1.0)
tsf.generateSample()
                      # 2
# Graphic
canvas = ROOT.TCanvas()
canvas.Divide(1,2)
canvas.cd(1)
tds.Draw("Weight:y:x")
canvas.Modified()
canvas.Update()
canvas.cd(2)
tsf.Draw2D("x", "y", "tri2Z")
                               # 3
```

1. Allocation of a pointer of a random variable sampler with variables described in the TDataServer “tds” that
is based on a “gaussian” variogram type. The constructor prototype is TSamplerField(tds,

```python
option
        =
```

"Gauss").
2. The generateSample() method generates a sample which will be saved in the TDataServer.
3. This step, along with the other drawing method few line earlier, gives the results shown in Figure 3.12.
Figure 3.12: Gaussian Random Field
It is possible to vary the value of the parameters used to construct the field, leading to different shapes. Examples of this
are shown for the two implemented types of variograms, Gaussian in Figure 3.13 and for Sine Cardinal in Figure 3.14.
