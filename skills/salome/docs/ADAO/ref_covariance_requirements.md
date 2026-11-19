<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_covariance_requirements.html -->

# 12.3. Requirements to describe covariance matrices

In general, a variance-covariance matrix, generally called a covariance matrix,
has to be squared, symmetric and semi-definite positive. Each of its terms
describes the covariance of the two random variables corresponding to its
position in the matrix. The normalized form of the covariance is the linear
correlation. One can express the following relation, between a covariance
matrix $\mathbf{M}$ and its corresponding correlation matrix
$\mathbf{C}$ (full matrix) and standard deviation matrix
$\mathbf{\Sigma}$ (diagonal matrix):

$$\mathbf{M} = \mathbf{\Sigma} * \mathbf{C} * \mathbf{\Sigma}$$

Various covariance matrices are required to implement the data assimilation or
optimization procedures. The main ones are the background error covariance
matrix, noted as $\mathbf{B}$, and the observation error covariance matrix,
noted as $\mathbf{R}$.

In the graphical interface EFICAS of ADAO, there are 3 practical methods for
the user to provide a covariance matrix. The method is chosen by the
“*INPUT_TYPE*” keyword of each defined covariance matrix, as shown by the
following figure:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_covariance_matrix.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/eficas_covariance_matrix.png)
>
> ****Choosing covariance matrix representation****

In the textual interface (TUI) of ADAO (see the part [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui)), the
same information can be given with the right command “*setBackgroundError*”,
“*setObservationError*” or “*setEvolutionError*” depending on the physical
quantity to define. The other arguments “*Matrix*”, “*ScalarSparseMatrix*” and
“*DiagonalSparseMatrix*” of the command allow to define it as described in the
following sub-parts. These information can also be given as a script in an
external file (argument “*Script*”).

## 12.3.1. First matrix form: using “*Matrix*” representation

This first form is the default and more general one. The covariance matrix
$\mathbf{M}$ has to be fully specified. Even if the matrix is symmetric by
nature, the entire $\mathbf{M}$ matrix has to be given.

$$\mathbf{M} = \begin{pmatrix}
m_{11} & m_{12} & \cdots & m_{1n} \\
m_{21} & m_{22} & \cdots & m_{2n} \\
\vdots & \vdots & \vdots & \vdots \\
m_{n1} & \cdots & m_{nn-1} & m_{nn}
\end{pmatrix}$$

It can be either a Python Numpy array or a matrix, or a list of lists of values
(that is, a list of rows). For example, a simple diagonal unitary background
error covariance matrix $\mathbf{B}$ can be described in a Python script
file as:

```python
BackgroundError = [[1, 0 ... 0], [0, 1 ... 0] ... [0, 0 ... 1]]
```

or:

```python
BackgroundError = numpy.eye(...)
```

## 12.3.2. Second matrix form: using “*ScalarSparseMatrix*” representation

On the opposite, this second form is a very simplified method to provide a
matrix. The covariance matrix $\mathbf{M}$ is supposed to be a positive
multiple of the identity matrix. This matrix can then be specified in a unique
way by the multiplier $m$:

$$\mathbf{M} = m \times \begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots \\
0 & \cdots & 0 & 1
\end{pmatrix}$$

The multiplier $m$ has to be a floating point or integer positive value
(if it is negative, which is impossible for a positive covariance matrix, it is
converted to positive value). For example, a simple diagonal unitary background
error covariance matrix $\mathbf{B}$ can be described in a python script
file as:

```python
BackgroundError = 1.
```

or, better, by a “*String*” directly in the graphical or textual ADAO case.

## 12.3.3. Third matrix form: using “*DiagonalSparseMatrix*” representation

This third form is also a simplified method to provide a matrix, but a little
more powerful than the second one. The covariance matrix $\mathbf{M}$ is
already supposed to be diagonal, but the user has to specify all the positive
diagonal values. The matrix can then be specified only by a vector
$\mathbf{V}$ which will be set on a diagonal matrix:

$$\mathbf{M} = \begin{pmatrix}
v_{1} & 0 & \cdots & 0 \\
0 & v_{2} & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots \\
0 & \cdots & 0 & v_{n}
\end{pmatrix}$$

It can be either a Python Numpy array or a matrix, or a list or a list of list
of positive values (in all cases, if some are negative, which is impossible,
they are converted to positive values). For example, a simple diagonal unitary
background error covariance matrix $\mathbf{B}$ can be described in a
python script file as:

```python
BackgroundError = [1, 1 ... 1]
```

or:

```python
BackgroundError = numpy.ones(...)
```

As previously indicated, one can also define this matrix by a “*String*”
directly in the graphical or textual ADAO case.
