# The Modeler Module
<!-- source PDF pages 131-132 -->

<!-- page 124 (PDF 131) -->
THE MODELER MODULE
This is a description of the Modeler module whose main goal is to produce a surrogate model from a database stored in
a TDataServer.

## 5.1 Introduction

This is a test: The Modeler module
The Modeler module discusses the generation of surrogate models which aim to provide a simpler, and hence faster,
model in order to emulate the specified output of a more complex model (and generally time and memory consuming) as
a function of its inputs and parameters, provided through a TDataServer. The input dataset can either be an existing set
of elements (provided by someone else, resulting from simulations or experiments) or it can be a design of experiments
generated on purpose, for the sake of the ongoing study.
The meta-model generation is encoded in Uranie with several different kinds of surrogate models, and also different kinds
of possible output format. Once created, the resulting model can indeed be transmitted to another code and re-used within
or without Uranie, in order to avoid regeneration but also to keep track of achieved performances, as these models can
sometimes be created based on a certain randomness (as discussed in the few sections below).
There are several predefined surrogate-models proposed in the Uranie platform:
• The linear regression, discussed in The TLinearRegression Class.

## 5.2 The TLinearRegression Class

When using the TLinearRegression class, one assumes that there is only one output variable and at least one input
variable.

<!-- page 125 (PDF 132) -->
## 5.3 Chaos polynomial expansion

### 5.3.1 Nisp in a nutshell

#### 5.3.1.1 The integration method

## 5.4 The kriging method

### 5.4.1 Construction of a kriging model

#### 5.4.1.1 Example: construction of a simple Kriging model

#### 5.4.1.2 Deterministic trend and bayesian prior

#### 5.4.1.3 Choice of the initial point of the optimisation

### 5.4.2 Usage of a Kriging model

#### 5.4.2.1 Prediction of a new data set, one-by-one approach

#### 5.4.2.2 Prediction of a new data set, global approach
