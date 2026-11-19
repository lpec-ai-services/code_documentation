<!-- source: https://docs.salome-platform.org/latest/gui/YACS/annexe_common.html -->

# Appendix: processing of fortran commons and C / C++ global variables

## Fortran common

This section is the result of studies carried out by Marc Boucker, Alexandre Douce, Céline Béchaud and Marc Tajchman
(for further details, see [[COMMON]](references.md#common)). We do not aim to present a complete state of possible situations in this description.
The fortran 77 codes that are to be controlled from the python interpreter or from Corba / SALOME often define memory zones
shared between the different fortran functions, called “common”.
For example, functions `f1` and `f2` use the same memory zone `a` in common `C`.

`f1.f`

```python
      real function f1(x)
      real x
C
      real a
      common / C / a
C
      f1 = x / a
      return
      end
```

`f2.f`

```python
      real function f2(x)
      real x
C
      real a
      common / C / a
C
      f2 = x * a
      return
      end
```

If the two functions are contained in the same component and common `C` is not used by functions of other components, the
common is not visible from outside the component and “everything takes place properly” (see
figure [Using a common in a component](#figcommon0)). If the component designer wants to allow common to be read or
written from the python and/or CORBA layer, he will easily be able to write access functions (for example `setCommon` and
`getCommon` functions in the following example).

`common.f`

```python
      subroutine setcom(b)
      real b
C
      real a
      common / C / a
C
      a = b
C
      return
      end

      subroutine getcom(b)
      real b
C
      real a
      common / C / a
C
      b = a
C
      return
      end
```

![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/common0.png)

**Using a common in a component**

The following is an example encapsulation in C++, then in python (through swig):

`f.hxx`

```python

extern "C" float f1(float *);
extern "C" float f2(float *);
extern "C" void setcom(float *);
extern "C" void getcom(float *);

class f {

public:

  f() {
    float y = 1.0;
    setcom(&y);
  }

  void setCommon(float x) {
    setcom(&x);
  }

  float getCommon() {
    float x;
    getcom(&x);
    return x;
  }

  float f1(float x) {
    return ::f1(&x);
  }

  float f2(float x) {
    return ::f2(&x);
  }
};
```

`modf.i`

```python
%module modf

%{
#include "f.hxx"
%}

class f {

public:

  void setCommon(float x);
  float getCommon();
  float f1(float x);
  float f2(float x);
};
```

A practical example:

```python
>>> import modf
>>> f = modf.f();
>>> f.init(3.0)
>>> print f.f1(1)
0.333333343267
>>> print f.f2(1)
3.0
>>> print f.f1(f.f2(1))
1.0
```

If common `C` is used in several dynamic libraries, management is more difficult. In general, it is impossible
to assume that the common used by each library is located at the same memory address. There are two typical
situations that can arise:

1. The two components are installed locally from the same python interpreter:

   > ![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/common1.png)
   >
   > **Using a common shared between two libraries – Local version**
2. The two components are installed in different memory zones (on the same machine or on different machines) through
   the SALOME mechanism (containers):

   > ![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/common2.png)
   >
   > **Using a common shared between two libraries – distributed version**

Synchronization functions are necessary in both cases (for example using functions to read / write commons
from the python and/or SALOME command layer). The adaptation to the case of two local components loaded from a
python interpreter is written as follows:

1. For the first component:

   `f1.hxx`

   ```python
   extern "C" float f1(float *);
   extern "C" void setcom(float *);
   extern "C" void getcom(float *);

   class f {

   public:

     f() {
       float y = 1.0;
       setcom(&y);
     }
     void setCommon(float x) {
       setcom(&x);
     }
     float getCommon() {
       float x;
       getcom(&x);
       return x;
     }
     float f1(float x) {
       return ::f1(&x);
     }
   };
   ```

   `modf1.i`

   ```python
   %module modf1

   %{
   #include "f1.hxx"
   %}

   class f {

   public:

     f();
     float f1(float x);
     void setCommon(float x);
     float getCommon();
   };
   ```
2. For the second component:

   `f2.hxx`

   ```python

   extern "C" float f2(float *);
   extern "C" void setcom(float *);
   extern "C" void getcom(float *);

   class f {

   public:

     f() {
       float y = 1.0;
       setcom(&y);
     }
     void setCommon(float x) {
       setcom(&x);
     }
     float getCommon() {
       float x;
       getcom(&x);
       return x;
     }
     float f2(float x) {
       return ::f2(&x);
     }
   };
   ```

   `modf2.i`

   ```python
   %module modf2

   %{
   #include "f2.hxx"
   %}

   class f {

   public:

     f();
     float f2(float x);
     void setCommon(float x);
     float getCommon();
   };
   ```
3. Read and write functions for the common will be included in each component.

A practical example

```python
>>> import modf1
>>> import modf2
>>> f1 = modf1.f();
>>> f2 = modf2.f();
>>> f1.setCommon(2.0)
>>> print "f1(1) = ", f1.f1(1.0)
f1(1) =  0.5
>>> print "avant synchronisation"
avant synchronisation
>>> print "f2(1) = ", f2.f2(1.0)
f2(1) =  1.0
>>> f2.setCommon(f1.getCommon())
>>> print "après synchronisation"
après synchronisation
>>> print "f2(1) = ", f2.f2(1.0)
f2(1) =  2.0
```

In summary, if an existing code comprising commons has to be broken down into several components, it is possible to either:

- modify the code by removing the commons and transferring information through lists of function parameters;
- write functions to provide read/write access to the commons and use these read/write functions from layers higher
  than components, so as to synchronize the internal states of the different components.

The first solution requires that in-depth action is taken in the fortran code, while the second requires that the
user explicitely synchronises commons in the different components. It is strongly recommended that commons should not be
used in new fortran codes.

## C/C++ global variables

The situation is similar to the case of commons: each component will have its own set of global variables.
A method is necessary to assure that these different sets of variables are consistant.
