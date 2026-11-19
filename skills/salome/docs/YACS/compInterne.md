<!-- source: https://docs.salome-platform.org/latest/gui/YACS/compInterne.html -->

# Defining an internal object

In the remainder of this document, it is assumed that an **internal object** is a **C++ or python object** that provides a
first interface to the initial code. The form of this object and communication between the internal object and the
initial code will be different depending on the form of the initial code (executable binary, static or dynamic library,
f77, C, C++ or python source files).

## Object methods and attributes

In each case, the services and the internal state of the internal object will have to be defined. In particular:

- choose the different services of this object
- for each service, define input and output data
- for each input and each output, define the data type and possibly associated pre-conditions and post-conditions (for example positive input data)
- define the internal state of the object and possibly its value before and after the call to different services.

**Services** will be implemented in the form of **public methods** and the **internal state** will be implemented in the form of **attributes**.
If the designer of the object allows the user to access the attributes in read and write, he must provide services to access these attributes.

## Fortran77 routines / C functions / C++ classes

### Principle

In the case of Fortran77 routines, C functions and C++ classes, the integrator will simply add a C++ envelope around
these functions (see figure [C++ internal object](#figobjetinterne)), to obtain the internal object.
Each method in the object:

- extracts information from the input parameters if necessary
- calls the internal routine(s) concerned,
- formats the results of these internal routines in the output parameters.

![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/objintcpp.png)

**C++ internal object**

### Example 1

Consider the following f77 fortran routines performing linear algebra calculations on one dimensional floating tables:

`addvec.f`

```python
       subroutine addvec(C,A,B,n)
       integer i,n
       double precision A(n), B(n), C(n)
C
       do i=1, n
          C(i) = A(i) + B(i)
       enddo
C
       return
       end
```

`prdscl.f`

```python
       double precision function prdscl(A,B,n)
       integer i,n
       double precision A(n), B(n), S
C
       S = 0.0D0
       do i=1, n
          S = S + A(i) * B(i)
       enddo
C
       prdscl = S
       return
       end
```

and a C++ class simulating a (very) rudimentary vector type:

`vecteur.hxx (C++ interface)`

```python
class vecteur {

public:
  vecteur(long n);
  ~vecteur();

  double * x() { return xx; };
  long     n() { return nn; };

private:
  double *xx;
  long nn;
};
```

`vecteur.cxx (C++ implementation)`

```python
#include "vecteur.hxx"

vecteur::vecteur(long n)
{
  xx = new double[n];
  nn = n;
}

vecteur::~vecteur()
{
  delete [] xx;
}
```

The internal object (i.e. the C++ class) in the example is:

`alglin.hxx`

```python
#include "vecteur.hxx"

class alglin {

public:
  void      addvec(vecteur *C, vecteur *A, vecteur *B);
  double    prdscl(vecteur *A, vecteur *B);
  vecteur * create_vector(long n);
  void      destroy_vector(vecteur *V);

};
```

`alglin.cxx`

```python
#include "alglin.hxx"

extern "C" {
  double * valloc(long n);
  void vfree(double *x);
  void addvec_(double *C, double *A, double *B, long *n);
  double prdscl_(double *A, double *B, long *n);
}

void   alglin::addvec(vecteur *C, vecteur *A, vecteur *B) {
  long n = A->n();
  addvec_(C->x(), A->x(), B->x(), &n);
}

double alglin::prdscl(vecteur *A, vecteur *B) {
  long n = A->n();
  return prdscl_(A->x(), B->x(), &n);
}

vecteur * alglin::create_vector(long n) {
  return new vecteur(n);
}

void   alglin::destroy_vector(vecteur *V) {
  delete V;
}
```

**Notes**:

1. The integrator chooses methods, parameter transfers and parameter types (in accordance with the requirements of object users).
   The correspondence between parameters of the internal object and parameters of routines in the initial code is organised
   by the implementation (file `alglin.cxx`, above).
2. In particular, if MED structures [[MED]](references.md#med) are transferred as input arguments, the C++ implementation file will be required to extract
   and format information to be transferred to internal calculation routines (in the form of simple and scalar tables for internal
   fortran routines). For output arguments in the MED format, the implementation will introduce the results of internal routines
   into the MED objects to be returned.

Note the following in the above example:

- the `“C” extern` declaration in front of C++ prototypes of fortran functions
- the “underscore” character added to the C++ name of fortran functions
- the mode of transferring arguments, the rule being that pointers will be transferred apart from exceptions (length of
  character strings). For scalar arguments, the addresses of the scalar arguments will be transferred; for pointer
  arguments (tables), the pointers will be transferred as is.

The internal object can now be used in a C++ code:

```python
  alglin CompInterne;

  long n = 5;
  vecteur *A = CompInterne.create_vector(n);
  vecteur *B = CompInterne.create_vector(n);
  vecteur *C = CompInterne.create_vector(n);

// ...

  CompInterne.addvec(C, A, B);
  cout << CompInterne.prdscl(A, B) << endl;
```

### References

The C / fortran77 encapsulation in a C++ code follows the standard procedure (formats of reals / integers,
routine names, transfer of arguments). For example, further information on this subject is given in [[ForCpp]](references.md#forcpp) or [[ForCpp2]](references.md#forcpp2).

## Python function/classes

### Principle

The principle of encapsulation of python functions / classes in an internal object (python) is the same as in the previous case

> ![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/objintpy.png)
>
> **Python internal object**

### Example 2

An example similar to the previous example starts from Python functions to be encapsulated:

`func.py`

```python
def addvec(x, y):    
    n = len(x)
    z = []
    for i in range(n):
         z.append(x[i] + y[i])
    return z

def prdscl(x, y):
    n = len(x)
    S = 0
    for i in range(n):
         S = S + x[i] * y[i]
    return S
```

It is easy to integrate these functions into a python class:

`compo.py`

```python
import func

class compo:
    def prdscl(self, x, y):
        return func.prdscl(x, y)

    def addvec(self, x, y):
        return func.addvec(x, y)
```

**Note**:
:   In fact, it is not even necessary to embed python functions of `func.py`, but it is “cleaner” (particularly if
    the object has an internal state). The following script uses the Python internal object from a python interpreter:

```python
import compo

x = []
y = []
for i in range(5):
    ii = i+1
    x.append(2*ii)
    y.append(ii*ii)

C = compo.compo()
    
z = C.addvec(x, y)
print('x = ', x)
print('y = ', y)
print('z = ', z)
print(C.prdscl(x,y))
```

## Initial code in the form of executables

### Principle

This case occurs when there are no internal code sources (or when it is not required to integrate these sources
into the internal architecture). It will be assumed that the code is in the form of a binary that can be executed
by the operating system. Communications can be made with the code.

1. In input, either:

> - by one or several files,
> - by the command line,
> - using the keyboard to answer questions from the code

2. In output, either:

> - by one or several files,
> - on-screen display.

Communication with executables is made using commands (available in C++ and in python):

- `system`: start an executable with which input communications are made through files or the command line, and
  output communications are made through files,
- `popen`: same functions as the previous case, also with the possibility of retrieving the standard output (screen)
  for the executable.

The above commands are stored in order of increasing complexity (it is recommended that `system` should be used as much as possible).

### Example 3: Python internal object connected to external executables

It is required to use a “System” object that has 5 services:

- `cd`, that starts from a path (character string) and sets a current directory,
- `cp`, that starts from 2 file names, and copies the first file onto the second in the current directory,
- `touch`, that starts from a file name and updates the date of the file if there is one, and otherwise creates it,
- `rm`, that starts from a file name and destroys the file in the current directory,
- `dir`, that lists the files contained in the current directory.

The internal state of the object will be composed of the name of the current directory in which the services of the
object (that is set by the `cd` service) will work.

In Python, the object class could be written:

`systeme.py`

```python
from os import system, popen
from string import split

class Systeme:
    
    def __init__(self):
        self.repertoire = '.'

    def cd(self, rep):
        self.repertoire = rep

    def cp(self, nom1, nom2):
        system('cp '
               + self.repertoire + '/' + nom1 + ' ' 
               + self.repertoire + '/' + nom2)

    def touch(self, nom):
        system('touch '
               + self.repertoire + '/' + nom)

    def rm(self, nom):
        system('rm '
               + self.repertoire + '/' + nom)
        
    def dir(self):
        f = popen('ls ' + self.repertoire)
        s = f.read()
        f.close()
        return split(s)
```

and its use from the python interpreter:

```python
import systeme

S = systeme.Systeme()

print("create U1 ...")
S.touch('U1')
print("dir : ", S.dir())

print("copy U1 to U2 ...")
S.cp('U1', 'U2')
print("dir : ", S.dir())

print("delete U1 ...")
S.rm('U1')
print("dir : ", S.dir())

print("delete U2 ...")
S.rm('U2')
print("dir : ", S.dir())
```

**Notes**

1. This is given as an example, Python has everything necessary in the standard version to perform these services, without
   the use of system commands (`system` and `popen`).
2. The example illustrates transfer of input arguments through the command line (names transferred as arguments) and the “capture” of
   screen outputs from external executables (`system` that cannot simply recover the standard output from the unix command `ls`, and
   in this case `popen` is used).

### Example 4: Internal object connected to an external executable

This example shows a (very) partial interface of a binary executable *FreeFem* [[FreeFem]](references.md#freefem) in the form of a C++ object.
The interface provides access to the definition of a 2D geometry through its boundary, and the approximate resolution of a
simple equation (forced convection) on this geometry. The different methods of the internal object are:

- a method that records the geometry of the domain,
- a method that records the convecting velocity fields,
- the calculation method that receives the initial condition (in analytic form – character string), the time step and the number of time steps.

The internal state of the object is composed of the geometry and the velocity field.
The calculation method creates a file starting from its parameters and the internal state, and then starts a calculation
loop (by a system call). The object does not recover the calculation results.

**Comments**

1. A complete encapsulation of FreeFem would require far too much effort, this is simply an example.
2. We do not retrieve a result in the C++ object in this example (the change is only displayed by the FreeFem internal graphic
   engine). If it was required to do so, it would be necessary to read the file produced by the external code after the system
   call, and transfer the results in a form that could be understood by the User of the internal object.

Two versions (C++ and python) are listed below.

`FreeFem.hxx`

```python
#include <string>
#include <vector>

struct sBord {
  string X;
  string Y;
  int n;
};

class FreeFem
{
 public:

  void Bords(vector<sBord> &B);
  void Flux(string u1, string u2);
  void Convection(string Cinit, double dt, long n);

 private:

  string VX_, VY_;
  vector<sBord> B_;
};
```

`FreeFem.cxx`

```python
#include "FreeFem.hxx"
#include <fstream>

void FreeFem::Bords(vector<sBord> &B) {
  B_ = B;
}

void FreeFem::Flux(string u1, string u2) {
  VX_ = u1;
  VY_ = u2;
}

void FreeFem::Convection(string Cinit, double dt, long n) {

  ofstream f("/tmp/example.edp");
  
  int i, nB = B_.size();

  for (i=0; i<nB; i++)
    f << "border b" << i << "(t=0,1){" 
      << B_[i].X << "; " << B_[i].Y << "; }" << endl;

  f << "mesh th = buildmesh(";
  for (i=0; i<nB; i++)
    f << "b" << i << "(" << B_[i].n << ")" 
      << ( i<nB-1 ? '+' : ')');
  f << ";" << endl;

  f << "fespace Vh(th,P1);" << endl;
  f << "Vh v = " << Cinit << ";" << endl << "plot(v);" <<endl;
  f << "real dt = " << dt << ", t=0;" << endl;
  f << "Vh u1 = " << VX_ << ", u2 = " << VY_ << ";" << endl;
  f << "int i;" << endl << "Vh vv,vo;" << endl
    << "for ( i=0; i<" << n << "; i++) {" << endl
    << "t += dt;" << endl << "vo=v;" << endl
    << "v=convect([u1,u2],-dt,vo);" << endl
    << "plot(v,wait=0);" << endl << "};" << endl;
 
  f.close();

  system("FreeFem++ /tmp/example.edp");
}
```

`FreeFem.py`

```python
import os

class Bord:
    def __init__(self, X, Y, n):
        self.X = X
        self.Y = Y
        self.n = n
    
class FreeFem:
    def __init__(self):
        self.u1 = "0"
        self.u2 = "0"
        self.bords = [ Bord("x = cos(2*pi*t)", "y = sin(2*pi*t)", 100) ]
        
    def Bords(self, b):
        self.bords = b

    def Flux(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        
    def Convection(self, cond_init, dt, n):

        f = open("/tmp/example.edp", "w")
        s = ""
        ib = 1
        nb = len(self.bords)
        for b in self.bords:
            f.write("border b" + str(ib) + "(t=0,1){" + \
                    b.X + "; " + b.Y + "; };\n");
            s = s + "b" + str(ib) + "(" + str(b.n)+ ")"
            if (ib < nb):
                s = s + "+ "
            else:
                s = s + ");"
            ib = ib+1
            
        f.write("mesh th = buildmesh(" + s + "\n");
        f.write("fespace Vh(th,P1);\n");
        f.write("Vh v = " + cond_init + ";\nplot(v);\n")
        f.write("real dt = " + str(dt) + ", t=0;\n");
        
        f.write("Vh u1 = " + str(self.u1) + \
                ", u2 = " + str(self.u2) + ";\n");
        
        f.write("int i;\nVh vv,vo;\n"
                "for ( i=0; i< " + str(n) + " ; i++) {\n"
                "t += dt;\nvo=v;\nv=convect([u1,u2],-dt,vo);\n"
                "plot(v,wait=0);\n};\n");
        f.close()
        os.system('FreeFem++ /tmp/example.edp');
```

Use from a C++ code or a python interpreter is similar in the 2 versions:

`version C++`

```python
#include "FreeFem.hxx"

int main()
{
  FreeFem C;

  vector<sBord> B(1);
  B[0].X = "x=cos(2*pi*t)";
  B[0].Y = "y=sin(2*pi*t)";
  B[0].n = 100;

  C.Bords(B);
  C.Flux("y", "-x");
  C.Convection("exp(-10*((x-0.3)^2 +(y-0.3)^2))", 0.1, 40);
}
```

`version python`

```python
from FreeFem import *

C = FreeFem()

C.Flux("y", "-x")
C.Bords( [ Bord("x=cos(2*pi*t)", "y=sin(2*pi*t)",  100)] );
C.Convection('exp(-10*((x-0.3)^2 +(y-0.3)^2))', 0.1, 50)
```
