<!-- source: https://docs.salome-platform.org/latest/gui/YACS/salome.html -->

# SALOME component

## Principle

A SALOME component is a CORBA component as described in the previous chapter, using services of the SALOME kernel.
This component also has to be “declared” to SALOME (i.e. SALOME resource files need to be supplied or completed with
information about this component). The following operations need to be carried out:

1. adapt the IDL file
2. declare the component to the SALOME modules catalog
3. modify the implementation class (C++ or python) to

   - monitor adaptation of the IDL file (point 1)
   - enable supervision of the component by SALOME, in the different component services
   - prepare use of the notification service (send messages to monitor execution of calculations in the component) – optional (but useful)
4. Declare any graphic resources

## IDL file

### Principle

The IDL description is similar to the description of a standard CORBA component with the following special features:

- the component must form part of the basic `Engines` module (CORBA)
- the component must inherit from the SALOME basic component: `Engines::EngineComponent` (defined in the IDL `“SALOME_Component.idl”` file)
- the services of the component may have `in`, `out` parameters and /or a return value, but no `inout` parameters.

**Notes**

1. The `Engines` module includes all SALOME components other than the SALOME central components
2. The `Engines::EngineComponent` basic component avoids the need to redefine common services (stop, restart, etc.) for each
   component added to the system
3. This is not a limitation, an `inout` parameter can be decoupled into an `in` parameter and an `out`
   parameter (in any case, this is the form in which python clients will see it).

### Example 9 (start)

We will reuse the `alglin.idl` file and adapt it:

`alglin.idl`

```python
#include "SALOME_Component.idl"

module Engines {

  typedef sequence<double> vecteur;
  
  interface AlgLin : EngineComponent
  {
    void    addvec(out vecteur C, in vecteur A, in vecteur B);
    double  prdscl(in vecteur A, in vecteur B);
  };
  
};
```

**Note**
:   It is important to take care when structures are defined in the IDL (like the `vecteur` structure in `algin.idl`).
    The chosen name `vecteur` might be “reserved” by another SALOME component.

### Example 10 (start)

Similar modifications are made on the IDL `FreeFem.idl` file:

`FreeFem.idl`

```python
#include "SALOME_Component.idl"

module Solveur {

  struct Bord {
    string X;
    string Y;
    long   n;
  };
  typedef sequence<Bord> seqBords;

  interface FreeFemComponent : Engines::EngineComponent
{
    
    void Bords(in seqBords B);
    void Flux(in string u1, in string u2);

    void Convection(in string cond_init, in double dt, in long n);

  };

};
```

## Registration into the modules catalog

Before they can be used in SALOME, components must be registered in one of the SALOME modules catalogs. This catalog is
distributed in several files (general catalog, user catalog). It will be assumed that the component will be declared in
a user’s personal catalog. The component catalog file is an XML file that contains:

1. the list of services of the component and their parameters
2. the name of the file containing the icon of the component, version information, comments, default service, etc. (this information is optional).

This catalog can be completed by hand or a utility supplied by SALOME can be used that generates information in
point 1 above (nevertheless, this file must be edited to enter information in point 2). This tool is available in
the SALOME graphic interface (`Tools->Catalog Generator` menu) indicating the name of the catalog (XML file) and
the name of the IDL file of the component.

## C++ implementation class

**In this section, it will be assumed that the IDL file defines a CORBA class: A and that the C++ implementation class A_impl will be used.**

### Making conforming with the component IDL

Proceed as follows to adapt the standard CORBA / C++ implementation classes (as seen in the previous chapter):

1. Insert the `SALOMEconfig.h` file that contains a number of useful definitions to make the code of the implementation
   class independent from the CORBA version used:

   ```python
   #include <SALOMEconfig.h>
   ```
2. then insert the `SALOME_Component_i.hxx` file that contains the interface of the C++ implementation class of the SALOME basic component:

   ```python
   #include "SALOME_Component_i.hxx"
   ```
3. for the CORBA class that is implemented, add the following line:

   ```python
   #include CORBA_SERVER_HEADER(A)
   ```

   `CORBA_SERVER_HEADER` is a macro defined in `SALOMEconfig.h` that makes CORBA inclusion file names independent
   from the CORBA implementation used.
4. for each CORBA class used in the implementation class, add the following line:

   ```python
   #include CORBA_CLIENT_HEADER(<CORBA class name>)
   ```

   `CORBA_CLIENT_HEADER` is a macro defined in `SALOMEconfig.h` that makes CORBA inclusion file names independent
   from the CORBA implementation used.
5. derive the implementation class from the class of the basic SALOME component:

   ```python
   class A_impl :
        public POA_Engines::A,
        public Engines_Component_i {
   ```
6. define the (sole) constructor as follows in the C++ header file (.hxx):

   ```python
   A_impl(CORBA::ORB_ptr orb,
          PortableServer::POA_ptr poa,
          PortableServer::ObjectId * contId,
          const char *instanceName,
          const char *interfaceName);
   ```

   and in the C++ implementation file (.cxx):

   ```python
   A_impl:: A_impl
             (CORBA::ORB_ptr orb,
              PortableServer::POA_ptr poa,
              PortableServer::ObjectId * contId,
              const char *instanceName,
              const char *interfaceName) :
        Engines_Component_i(orb, poa, contId,
                            instanceName, interfaceName)
   {
     _thisObj = this ;
     _id = _poa->activate_object(_thisObj);
   }
   ```

   This constructor may possibly be responsible for creation and initialisation of the internal object associated with the CORBA component.
7. If structures are defined by the IDL file in the Engines module, adapt declarations of the implementation class methods.

The above example illustrates the modifications made on example 6.

### Enable component supervision

The following needs to be inserted in each service of the component (i.e. in each method of the implementation class
called during a CORBA request), before the component can be controlled from supervision.

- at the beginning, the instruction:

  ```python
  beginService(<nom du service>);
  ```
- at the end, the instruction:

  ```python
  endService(<nom du service>);
  ```

These two instructions notify the SALOME supervision that the component service has actually received the CORBA request (beginService)
and that execution of the service has actually terminated (endService).

**Note**
:   Put beginService and endService in the methods of the implementation class of a component declares to SALOME that the component
    is “supervisable”. This is not an assurance that this component can be used without precautions in the case in which the
    component has an internal state modified by one or more services.

    **Example**:
    :   Consider a component with an internal variable `Quantity` and two services:

        - `S1(x):  Quantity = Quantity + x;` returns `Quantity` and
        - `S2(x) :  Quantity = Quantity * x ;` returns `Quantity`.

        *A priori*, it is impossible to know the value of `Quantity` after the calculation graph on the following figure has been executed.

![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/parallele.png)

**Calculation graph containing parallel branches**

### Using the notification

The constructor of the implementation class must be modified as follows, so as to signal use of the notification (that will
cause opening of a connection to an events channel):

```python
A_impl:: A_impl
          (CORBA::ORB_ptr orb,
           PortableServer::POA_ptr poa,
           PortableServer::ObjectId * contId,
           const char *instanceName,
           const char *interfaceName) :
     Engines_Component_i(orb, poa, contId,
                         instanceName, interfaceName, 1)
{
  _thisObj = this ;
  _id = _poa->activate_object(_thisObj);
}
```

in which the parameter “1” has been added to the end of the call to the `Engines_Component_i` of the constructor.
The component can then use the instruction:

```python
void sendMessage(const char *event_type, const char *message);
```

to send messages indicating progress with the calculation or an abnormal situation, etc. These messages will be visible to the
SALOME user. The first parameter indicates the message type (“warning”, “step”, “trace”, “verbose”), and the second parameter
indicates the message contents (character string).

### Connection to the “factory” object of a container

A “C” function has to be provided with an imposed name and code, for a component to be loaded and initialised by a container:

```python
extern "C"
{
  PortableServer::ObjectId * <nom du composant>Engine_factory(
                               CORBA::ORB_ptr orb,
                               PortableServer::POA_ptr poa,
                               PortableServer::ObjectId * contId,
                               const char *instanceName,
                               const char *interfaceName)
  {
    <classe d'implementation> * O
      = new <classe d'implementation>(orb, poa, contId,
                                      instanceName, interfaceName);
    return O->getId() ;
  }
}
```

`<component name>` (or CORBA class name, `A` in this case) and `<implementation class>` (`A_impl` here) are specific
to each component. This function is called by the container when a component is loaded. It creates a CORBA object that
will receive requests to the component and will forward them to the different services of the component.

### Example 9 (continued)

We will use the implementation files `algin_i.hxx` and `algin_i.cxx` again and adapt them:

`alglin_i.hxx`

```python
#ifndef ALGLIN_I_
#define ALGLIN_I_

#include "alglin.hxx"
#include <SALOMEconfig.h>
#include CORBA_SERVER_HEADER(alglin)
#include "SALOME_Component_i.hxx"

class AlgLin_i : public POA_Engines::AlgLin,
                 public Engines_Component_i {

private:

  alglin A_interne;

public:

  AlgLin_i(CORBA::ORB_ptr orb,
           PortableServer::POA_ptr poa,
           PortableServer::ObjectId * contId, 
           const char *instanceName,
           const char *interfaceName);

  virtual ~AlgLin_i();

  void addvec(Engines::vecteur_out C, 
              const Engines::vecteur& A, 
              const Engines::vecteur& B);

  CORBA::Double prdscl(const Engines::vecteur& A, 
                       const Engines::vecteur& B);

  Engines::vecteur* create_vector(CORBA::Long n);
  void destroy_vector(const Engines::vecteur& V);
  
};

extern "C"
PortableServer::ObjectId * 
     AlgLinEngine_factory(CORBA::ORB_ptr orb ,
                          PortableServer::POA_ptr poa , 
                          PortableServer::ObjectId * contId ,
                          const char *instanceName ,
                          const char *interfaceName );

#endif
```

`alglin_i.cxx`

```python
#include "alglin_i.hxx"
#include <iostream>

AlgLin_i:: AlgLin_i(CORBA::ORB_ptr orb,
                    PortableServer::POA_ptr poa,
                    PortableServer::ObjectId * contId, 
                    const char *instanceName, 
                    const char *interfaceName) :
  Engines_Component_i(orb, poa, contId, instanceName, interfaceName, 1)
{
  MESSAGE("activate object");
  _thisObj = this ;
  _id = _poa->activate_object(_thisObj);
}

AlgLin_i::~AlgLin_i()
{
}

void AlgLin_i::addvec(Engines::vecteur_out C,
                      const Engines::vecteur& A, 
                      const Engines::vecteur& B)
{
  beginService("addvec");

  long i, n = A.length();

  if (n != B.length())
    sendMessage("warning", "vecteurs de longueur differente");

  vecteur A_(n);
  vecteur B_(n);
  vecteur C_(n);

  double *xA = A_.x();
  double *xB = B_.x();
  double *xC = C_.x();

  for (i=0; i<n; i++) {
    xA[i] = A[i];
    xB[i] = B[i];
  }

  A_interne.addvec(&C_, &A_, &B_);

  C = new Engines::vecteur;
  C->length(n);
  for (i=0; i<n; i++) {
    (*C)[i] = xC[i];
  }

  endService("addvec");
}

CORBA::Double AlgLin_i::prdscl(const Engines::vecteur& A, 
                               const Engines::vecteur& B)
{
  beginService("prdscl");

  long i, n = A.length();

  if (n != B.length())
    sendMessage("warning", "vecteurs de longueur differente");

  vecteur A_(n);
  vecteur B_(n);

  double *xA = A_.x();
  double *xB = B_.x();

  for (i=0; i<n; i++) {
    xA[i] = A[i];
    xB[i] = B[i];
  }

  CORBA::Double d =  A_interne.prdscl(&A_, &B_); 

  endService("prdscl");
  return d;
}

extern "C"
{
  PortableServer::ObjectId * AlgLinEngine_factory(
                               CORBA::ORB_ptr orb,
                               PortableServer::POA_ptr poa,
                               PortableServer::ObjectId * contId,
                               const char *instanceName,
                               const char *interfaceName)
  {
    MESSAGE("PortableServer::ObjectId * AlgLinEngine_factory()");
    AlgLin_i * O
      = new AlgLin_i(orb, poa, contId, instanceName, interfaceName);
    return O->getId() ;
  }
}
```

## Python implementation class

**In this section, it is assumed that the IDL file defines a CORBA class: B and that we will use the python implementation class: B.**

The procedure is similar to the case of the C++ server interface:

### Making conforming with the component IDL

1. import the class of the basic component:

   ```python
   from SALOME_ComponentPy import *
   ```
2. derive the implementation class from the class of the basic SALOME component:

   ```python
   class B(Engines__POA.B,
           SALOME_ComponentPy_i):
   ```
3. The constructor of the implementation class must begin by:

   ```python
   def __init__(self, orb, poa, this, containerName,
                instanceName, interfaceName):
       SALOME_ComponentPy_i.__init__(self, orb, poa, this,
                                     containerName, instanceName,
                                     interfaceName, False)
   ```

### Enable supervision of the component

Before the component can be controlled from supervision, the following have to be inserted in each service of the
component (i.e. in each method of the implementation class called during a CORBA request).

- at the beginning, the instruction:

  ```python
  beginService(<service name>);
  ```
- at the end, the instruction:

  ```python
  endService(<service name>);
  ```

These two instructions notify the SALOME supervision that the component service has actually received the CORBA
request (beginService) and that execution of the service has actually terminated (endService).
Same comment as in the C++ case ([Enable component supervision](#remsuper)).

### Using the notification

The implementation class constructor should be modified as follows to signal use of the notification:

```python
def __init__(self, orb, poa, this, containerName,
             instanceName, interfaceName):
    SALOME_ComponentPy_i.__init__(self, orb, poa, this,
                                  containerName, instanceName,
                                  interfaceName, True)
```

in which the parameter “1” is added to the end of the call to the `SALOME_ComponentPy_i` of the constructor.
The component can then use the following instruction:

```python
sendMessage(event_type, message);
```

to send messages providing information about progress with the calculation or an abnormal situation, etc.
These messages will be visible to the SALOME user. The first parameter indicates the message
type (“warning”, “step”, “trace”, “verbose”), and the second parameter indicates the message contents (character string).

### Example 10 (continued)

Consider the `FreeFem.py` implementation file and adapt it:

`FreeFemComponent.py`

```python
from SALOME_ComponentPy import *

import FreeFem

class FreeFemComponent(Engines__POA.FreeFemComponent,
                       SALOME_ComponentPy_i):

    def __init__(self, orb, poa, this, containerName,
                 instanceName, interfaceName):
        SALOME_ComponentPy_i.__init__(self, orb, poa, this, containerName,
                                      instanceName, interfaceName, False)
        self.F = FreeFem.FreeFem();

    def Bords(self, b):
        self.F.Bords(b);

    def Flux(self, u1, u2):
        self.F.Flux(u1, u2);

    def Convection(self, cond_init, dt, n):
        self.F.Convection(cond_init, dt, n)
```

## Using the SALOME compilation and execution environment

Autotools like SALOME will be used.

## Using data structures provided by SALOME or returned by the component

This part will be done with reference to CORBA [[CORBA]](references.md#corba) specifications, and particularly IDL specifications – languages [[LANG]](references.md#lang)
or the different CORBA manuals, for example [[HENVIN]](references.md#henvin) (C++) and [[PyCorba]](references.md#pycorba) (python).

### Meshes and MED fields

This part will be done with reference to MED and MEDMemory documentation [[MEDDoc]](references.md#meddoc) and [[MEDMemory]](references.md#medmemory).
