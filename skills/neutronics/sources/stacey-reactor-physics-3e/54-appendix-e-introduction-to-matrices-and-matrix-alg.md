# Appendix E Introduction to Matrices and Matrix Algebra
<!-- source PDF pages 729-732 -->

<!-- page 713 (PDF 729) -->
# Appendix E Introduction to Matrices and Matrix Algebra

E.1

## Some Definitions

One defines a matrix of order (m × n) to be a rectangular array of m rows and n
columns:
A =
a11
a12
a13
∙∙∙
a1n
a21
...
...
...
...
..
.
..
.
aij
..
.
..
.
am1
∙∙∙
∙∙∙
∙∙∙
amn
(E.1)
The matrix elements aij will be identified by subscripts denoting their row i and
column j. If the matrix has the same number of rows as columns, it is said to be a
square matrix; for example,
A =
a11
a12
a13
a21
a22
a23
a31
a32
a33
@
A
(E.2)
A diagonal matrix has nonzero elements only along its main diagonal:
a11
a22
a33
A =
(E.3)
A tridiagonal matrix would have nonzero elements only along its central three
diagonals:
a
a
a
a
a
a
a
a
...
...
...
...
...
...
A =
(E.4)
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 714 (PDF 730) -->
The unit matrix is the diagonal matrix with elements aij = 1, i = j:
I =
∙∙∙
∙∙∙
∙∙∙
...
...
...
(E.5)
For two matrices to be equal, each of their matrix elements must be equal:
A =
a11
a12
a13
∙∙∙
a21
a22
∙∙∙
..
.
75 =
b11
b12
b13
∙∙∙
b21
b22
∙∙∙
..
.
..
.
75 = B
(E.6)
The transpose of a matrix is obtained by interchanging its rows and columns:
AT

ij = A
[ ]ji
(E.7)
or
AT=
a11
a12
a13
. . .
a21
O
a31
..
.
7775 =
a11
a21
a31
. . .
a12
O
a13
..
.
(E.8)
The determinant of a matrix is formed by taking the determinant of the
elements of the matrix:
det A ≡ A
j j =
a11
a12
a13
∙∙∙
a21
..
.
a31
...

(E.9)
Of course, the determinant of a matrix is a scalar – that is, just a number.
One defines the cofactor of a square matrix for an element aij by deleting the ith
row and jth column, calculating the determinant of the remaining array, and
multiplying by (−1)i+j:
(cof A)
...
...
...
...
...
...
...
...
...
...
...
...
...
...
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
=cof
=(–1)i+j
(E.10)

<!-- page 715 (PDF 731) -->
We can construct the adjoint or Hermitean conjugate of a matrix by complexconjugating
each of its elements and then transposing as
Ay = (A∗)T or(aij)y = (a∗
ji)
(E.11)
For example,
Ay =
a11
a12
a21
a22

y
=
a∗
a∗
a∗
a∗
!T
=
a∗
a∗
a∗
a∗
!
If the determinant of a matrix vanishes, det(A) = 0, then the matrix A is said to be
singular. If det(A) ≠0, the matrix is said to be nonsingular.
E.2

## Matrix Algebra

Two matrices of the same order may be added by adding their corresponding
elements (the same holds for subtraction):
A + B
=
a11
a12
∙∙∙
a21
...
7775 +
b11
b12
∙∙∙
b21
...
=
a11 + b11
a12 + b12
∙∙∙
a21 + b21
..
.
(E.12)
In order for matrix multiplication to be possible, the number of columns of the
first matrix must equal the number of rows of the second matrix. One then
calculates the matrix elements of C = A □ B as
cij =
X
n
k=1
aikbkj
(E.13)
or more explicitly
b
...
...
...
...
...
...
...
...
...
...
...
...
...
b
b
a
a
a
b
b
b
a
a
a
b
b
b
a
a
a
a11b11 a12b21
b
a
b
a
=
+
+
+
+
A . B=
(E.14)

<!-- page 716 (PDF 732) -->
Notice that matrix multiplication is not commutative – that is, A □ B ≠B □ A in
general.
A very important matrix concept is the inverse of a square matrix, A−1, which is
defined by the relation
A−1 ? A = A ? A−1 = I
(E.15)
The inverse can be calculated as
A−1 = 1
A
j j
(cof A)T
(E.16)
For example, consider
A =
−1

Then,
A
j j = 3
while
(cof A)T =
−1

T
=
−1

Hence,
A−1 = 1
−1

=
− 1
B
B
@
C
C
A
Notice that if a matrix is singular, that is, det(A) = 0, then it has no inverse.
