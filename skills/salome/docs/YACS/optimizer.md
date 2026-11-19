<!-- source: https://docs.salome-platform.org/latest/gui/YACS/optimizer.html -->

# Definition of an algorithm for the OptimizerLoop

The definition of the optimization algorithm is done by way of plugin.
The plugin can be a C++ plugin implemented in a dynamic library (.so file) or a Python plugin implemented in a Python module (.py).
It is possible to implement two kinds of algorithm : synchronous or asynchronous.

The algorithm uses a pool of samples to be evaluated.
When all the samples of the pool are evaluated, the algorithm stops.

## Synchronous algorithm

In synchronous mode, the OptimizerLoop calls the algorithm to know what are the types of the input port (sample sent to the internal node),
and of the output port (data returned by the internal node). Then it calls the algorithm to initialize
it. At each iteration, it calls the algorithm to produce new sample or to stop the iteration. Finally, it calls the algorithm
to finalize the optimization process.

A synchronous algorithm is implemented in a class derived from the base class OptimizerAlgSync with several methods that
must be implemented and some optional methods (in C++ and in Python):

- **getTCForIn**, this method must return the YACS type of the input port of the internal node
- **getTCForOut**, this method must return the YACS type of the output port of the internal node
- **getTCForAlgoInit** (optional), this method returns the type of the “algoInit” port, string if undefined
- **getTCForAlgoResult** (optional), this method returns the type of the “algoResult” port, string if undefined
- **initialize** (optional), this method is called during the algorithm initialization
- **start**, this method is called at the beginning of iterations
- **takeDecision**, this method is called at each iteration
- **finish** (optional), this method is called to finish the algorithm at the end of the iteration process
- **getAlgoResult** (optional), this method returns the value of the “algoResult” port, “NULL” if undefined

In Python you need to implement another method:

- **setPool**, this method is used to set the data pool that is used to exchange data

### C++ plugin example

Here is a small example of a C++ synchronous algorithm:

```cpp
// Copyright (C) 2006-2026  CEA, EDF
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
//
// See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
//

#include <cmath>
#include <iostream>

#include "OptimizerAlg.hxx"

#include <iostream>
//using namespace YACS::ENGINE;

extern "C"
{
  YACS::ENGINE::OptimizerAlgBase * createOptimizerAlgSyncExample(YACS::ENGINE::Pool * pool);
}

class OptimizerAlgSyncExample : public YACS::ENGINE::OptimizerAlgSync
{
  private:
    int _iter;
    YACS::ENGINE::TypeCode *_tcInt;
    YACS::ENGINE::TypeCode *_tcDouble;
  public:
    OptimizerAlgSyncExample(YACS::ENGINE::Pool *pool);
    virtual ~OptimizerAlgSyncExample();
    
    //! returns typecode of type expected as Input. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForIn() const;
    //! returns typecode of type expected as Output. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForOut() const;
    //! returns typecode of type expected for algo initialization. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForAlgoInit() const;
    //! returns typecode of type expected as algo result. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForAlgoResult() const;
    virtual void initialize(const YACS::ENGINE::Any *input);
    virtual void start(); //! Update _pool attribute before performing anything.
    virtual void takeDecision();//! _pool->getCurrentId gives the \b id at the origin of this call.
                                //! Perform the job of analysing to know what new jobs to do (_pool->pushInSample)
                                //! or in case of convergence _pool->destroyAll
    virtual void finish();//! Called when optimization has succeed.
    virtual YACS::ENGINE::Any * getAlgoResult();
};

OptimizerAlgSyncExample::OptimizerAlgSyncExample(YACS::ENGINE::Pool *pool)
  : YACS::ENGINE::OptimizerAlgSync(pool), _tcInt(0), _tcDouble(0), _iter(0)
{
  _tcDouble = new YACS::ENGINE::TypeCode(YACS::ENGINE::Double);
  _tcInt    = new YACS::ENGINE::TypeCode(YACS::ENGINE::Int);
}

OptimizerAlgSyncExample::~OptimizerAlgSyncExample()
{
  _tcDouble->decrRef();
  _tcInt->decrRef();
}

//! Return the typecode of the expected input of the internal node
YACS::ENGINE::TypeCode * OptimizerAlgSyncExample::getTCForIn() const
{
  return _tcDouble;
}

//! Return the typecode of the expected output of the internal node
YACS::ENGINE::TypeCode * OptimizerAlgSyncExample::getTCForOut() const
{
  return _tcInt;
}

//! Return the typecode of the expected input of the algorithm (algoInit port)
YACS::ENGINE::TypeCode * OptimizerAlgSyncExample::getTCForAlgoInit() const
{
  return _tcInt;
}

//! Return the typecode of the expected output of the algorithm (algoResult port)
YACS::ENGINE::TypeCode * OptimizerAlgSyncExample::getTCForAlgoResult() const
{
  return _tcInt;
}

//! Optional method to initialize the algorithm.
/*!
 *  For now, the parameter input is always NULL. It might be used in the
 *  future to initialize an algorithm with custom data.
 */
void OptimizerAlgSyncExample::initialize(const YACS::ENGINE::Any *input)
{
  std::cout << "Algo initialize, input = " << input->getIntValue() << std::endl;
}

//! Start to fill the pool with samples to evaluate
void OptimizerAlgSyncExample::start()
{
  std::cout << "Algo start " << std::endl;
  _iter=0;
  YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(0.5);
  _pool->pushInSample(_iter,val);
}

//! This method is called each time a sample has been evaluated.
/*!
 *  It can either add new samples to evaluate in the pool, do nothing (wait
 *  for more samples), or empty the pool to finish the evaluation.
 */
void OptimizerAlgSyncExample::takeDecision()
{
  int currentId = _pool->getCurrentId();
  double valIn  = _pool->getCurrentInSample()->getDoubleValue();
  int valOut    = _pool->getCurrentOutSample()->getIntValue();
  
  std::cout << "Algo takeDecision currentId=" << currentId;
  std::cout << ", valIn=" << valIn;
  std::cout << ", valOut=" << valOut << std::endl;
  
  _iter++;
  if(_iter < 3)
  {
    YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(valIn + 1);
    _pool->pushInSample(_iter, val);
  }
}

/*!
 *  Optional method called when the algorithm has finished, successfully or
 *  not, to perform any necessary clean up.
 */
void OptimizerAlgSyncExample::finish()
{
  std::cout << "Algo finish" << std::endl;
  _pool->destroyAll();
}

/*!
 *  Return the value of the algoResult port.
 */
YACS::ENGINE::Any * OptimizerAlgSyncExample::getAlgoResult()
{
  YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(42);
  return val;
}

//! Factory method to create the algorithm.
YACS::ENGINE::OptimizerAlgBase * createOptimizerAlgSyncExample(YACS::ENGINE::Pool *pool)
{
  return new OptimizerAlgSyncExample(pool);
}
```

Here, the entry point in the dynamic library is the name of the factory function : createOptimizerAlgSyncExample
that returns an instance of the OptimizerAlgSyncExample class that implements the algorithm.

### Python plugin example

Here, the same example of a synchronous algorithm in Python:

```python
# Copyright (C) 2006-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

import SALOMERuntime

class myalgosync(SALOMERuntime.OptimizerAlgSync):
  def __init__(self):
    SALOMERuntime.OptimizerAlgSync.__init__(self, None)
    r=SALOMERuntime.getSALOMERuntime()
    self.tin=r.getTypeCode("double")
    self.tout=r.getTypeCode("int")
    self.tAlgoInit=r.getTypeCode("int")
    self.tAlgoResult=r.getTypeCode("int")

  def setPool(self,pool):
    """Must be implemented to set the pool"""
    self.pool=pool

  def getTCForIn(self):
    """return typecode of type expected as Input of the internal node """
    return self.tin

  def getTCForOut(self):
    """return typecode of type expected as Output of the internal node"""
    return self.tout

  def getTCForAlgoInit(self):
    """return typecode of type expected as input for initialize """
    return self.tAlgoInit

  def getTCForAlgoResult(self):
    """return typecode of type expected as output of the algorithm """
    return self.tAlgoResult

  def initialize(self,input):
    """Optional method called on initialization.
       The type of "input" is returned by "getTCForAlgoInit"
    """
    print("Algo initialize, input = ", input.getIntValue())

  def start(self):
    """Start to fill the pool with samples to evaluate."""
    print("Algo start ")
    self.iter=0
    # pushInSample(id, value)
    self.pool.pushInSample(self.iter, 0.5)

  def takeDecision(self):
    """ This method is called each time a sample has been evaluated. It can
        either add new samples to evaluate in the pool, do nothing (wait for
        more samples), or empty the pool to finish the evaluation.
    """
    currentId=self.pool.getCurrentId()
    valIn = self.pool.getCurrentInSample().getDoubleValue()
    valOut = self.pool.getCurrentOutSample().getIntValue()
    print("Algo takeDecision currentId=%s, valIn=%s, valOut=%s" % (currentId, valIn, valOut))

    self.iter=self.iter+1
    if self.iter < 3:
      # continue
      nextSample = valIn + 1
      self.pool.pushInSample(self.iter, nextSample)

  def finish(self):
    """Optional method called when the algorithm has finished, successfully
       or not, to perform any necessary clean up."""
    print("Algo finish")
    self.pool.destroyAll()

  def getAlgoResult(self):
    """return the result of the algorithm.
       The object returned is of type indicated by getTCForAlgoResult.
    """
    return 42
```

Here, the entry point in the Python module is directly the name of the class that implements the algorithm : myalgosync.

## Asynchronous algorithm

In asynchronous mode, all is the same except that after the initialization phase, the OptimizerLoop calls the algorithm only one time
to start it in a separate thread.

An asynchronous algorithm is implemented in a class derived from the base class OptimizerAlgASync with several methods that
must be implemented and some optional methods (in C++ and in Python):

- **getTCForIn**, this method must return the YACS type of the input port of the internal node
- **getTCForOut**, this method must return the YACS type of the output port of the internal node
- **getTCForAlgoInit** (optional), this method returns the type of the “algoInit” port, string if undefined
- **getTCForAlgoResult** (optional), this method returns the type of the “algoResult” port, string if undefined
- **initialize** (optional), this method is called during the algorithm initialization
- **startToTakeDecision**, this method is called to start the iteration process in a separate thread. It is the body of the algorithm.
- **finish** (optional), this method is called to finish the algorithm at the end of the iteration process
- **getAlgoResult** (optional), this method returns the value of the “algoResult” port, “NULL” if undefined

In Python you need to implement another method:

- **setPool**, this method is used to set the data pool that is used to exchange data

### C++ plugin example

Here is a small example of a C++ asynchronous algorithm:

```cpp
// Copyright (C) 2006-2026  CEA, EDF
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
//
// See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
//

#include "OptimizerAlg.hxx"

#include <iostream>
//using namespace YACS::ENGINE;

extern "C"
{
  YACS::ENGINE::OptimizerAlgBase * createOptimizerAlgASyncExample(YACS::ENGINE::Pool * pool);
}

class OptimizerAlgASyncExample : public YACS::ENGINE::OptimizerAlgASync
{
  private:
    YACS::ENGINE::TypeCode *_tcInt;
    YACS::ENGINE::TypeCode *_tcDouble;
  public:
    OptimizerAlgASyncExample(YACS::ENGINE::Pool *pool);
    virtual ~OptimizerAlgASyncExample();
    
    //! returns typecode of type expected as Input. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForIn() const;
    //! returns typecode of type expected as Output. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForOut() const;
    //! returns typecode of type expected for algo initialization. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForAlgoInit() const;
    //! returns typecode of type expected as algo result. OwnerShip of returned pointer is held by this.
    virtual YACS::ENGINE::TypeCode *getTCForAlgoResult() const;
    virtual void initialize(const YACS::ENGINE::Any *input);
    virtual void startToTakeDecision();
    virtual void finish();//! Called when optimization has succeed.
    virtual YACS::ENGINE::Any * getAlgoResult();
};

OptimizerAlgASyncExample::OptimizerAlgASyncExample(YACS::ENGINE::Pool *pool)
  : YACS::ENGINE::OptimizerAlgASync(pool), _tcInt(0), _tcDouble(0)
{
  _tcDouble = new YACS::ENGINE::TypeCode(YACS::ENGINE::Double);
  _tcInt    = new YACS::ENGINE::TypeCode(YACS::ENGINE::Int);
}

OptimizerAlgASyncExample::~OptimizerAlgASyncExample()
{
  _tcDouble->decrRef();
  _tcInt->decrRef();
}

//! Return the typecode of the expected input of the internal node
YACS::ENGINE::TypeCode * OptimizerAlgASyncExample::getTCForIn() const
{
  return _tcDouble;
}

//! Return the typecode of the expected output of the internal node
YACS::ENGINE::TypeCode * OptimizerAlgASyncExample::getTCForOut() const
{
  return _tcInt;
}

//! Return the typecode of the expected input of the algorithm (algoInit port)
YACS::ENGINE::TypeCode * OptimizerAlgASyncExample::getTCForAlgoInit() const
{
  return _tcInt;
}

//! Return the typecode of the expected output of the algorithm (algoResult port)
YACS::ENGINE::TypeCode * OptimizerAlgASyncExample::getTCForAlgoResult() const
{
  return _tcInt;
}

//! Optional method to initialize the algorithm.
/*!
 *  For now, the parameter input is always NULL. It might be used in the
 *  future to initialize an algorithm with custom data.
 */
void OptimizerAlgASyncExample::initialize(const YACS::ENGINE::Any *input)
{
  std::cout << "Algo initialize, input = " << input->getIntValue() << std::endl;
}

//! This method is called only once to launch the algorithm.
/*!
 *  It must first fill the pool with samples to evaluate and call
 *  signalMasterAndWait() to block until a sample has been evaluated. When
 *  returning from this method, it MUST check for an eventual termination
 *  request (with the method isTerminationRequested()). If the termination
 *  is requested, the method must perform any necessary cleanup and return
 *  as soon as possible. Otherwise it can either add new samples to evaluate
 *  in the pool, do nothing (wait for more samples), or empty the pool and
 *  return to finish the evaluation.
 */
void OptimizerAlgASyncExample::startToTakeDecision()
{
  std::cout << "startToTakeDecision" << std::endl;
  int iter = 0;
  YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(0.5);
  _pool->pushInSample(iter, val);
  
  signalMasterAndWait();
  while(!isTerminationRequested())
  {
    int currentId = _pool->getCurrentId();
    double valIn  = _pool->getCurrentInSample()->getDoubleValue();
    int valOut    = _pool->getCurrentOutSample()->getIntValue();
    
    std::cout << "Compute currentId=" << currentId;
    std::cout << ", valIn=" << valIn;
    std::cout << ", valOut=" << valOut << std::endl;
    
    iter++;
    if(iter < 3)
    {
      YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(valIn + 1);
      _pool->pushInSample(iter, val);
    }
    signalMasterAndWait();
  }
}

/*!
 *  Optional method called when the algorithm has finished, successfully or
 *  not, to perform any necessary clean up.
 */
void OptimizerAlgASyncExample::finish()
{
  std::cout << "Algo finish" << std::endl;
  _pool->destroyAll();
}

/*!
 *  Return the value of the algoResult port.
 */
YACS::ENGINE::Any * OptimizerAlgASyncExample::getAlgoResult()
{
  YACS::ENGINE::Any *val=YACS::ENGINE::AtomAny::New(42);
  return val;
}

//! Factory method to create the algorithm.
YACS::ENGINE::OptimizerAlgBase * createOptimizerAlgASyncExample(YACS::ENGINE::Pool *pool)
{
  return new OptimizerAlgASyncExample(pool);
}
```

Here, the entry point in the dynamic library is the name of the factory function : createOptimizerAlgASyncExample
that returns an instance of the OptimizerAlgASyncExample class that implements the algorithm.

### Python plugin example

Here is an example of an asynchronous algorithm implemented in Python:

```python
# Copyright (C) 2006-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

import SALOMERuntime

class myalgoasync(SALOMERuntime.OptimizerAlgASync):
  def __init__(self):
    SALOMERuntime.OptimizerAlgASync.__init__(self, None)
    r=SALOMERuntime.getSALOMERuntime()
    self.tin=r.getTypeCode("double")
    self.tout=r.getTypeCode("int")
    self.tAlgoInit=r.getTypeCode("int")
    self.tAlgoResult=r.getTypeCode("int")

  def setPool(self,pool):
    """Must be implemented to set the pool"""
    self.pool=pool

  def getTCForIn(self):
    """return typecode of type expected as Input of the internal node """
    return self.tin

  def getTCForOut(self):
    """return typecode of type expected as Output of the internal node"""
    return self.tout

  def getTCForAlgoInit(self):
    """return typecode of type expected as input for initialize """
    return self.tAlgoInit

  def getTCForAlgoResult(self):
    """return typecode of type expected as output of the algorithm """
    return self.tAlgoResult

  def initialize(self,input):
    """Optional method called on initialization.
       The type of "input" is returned by "getTCForAlgoInit"
    """
    print("Algo initialize, input = ", input.getIntValue())

  def startToTakeDecision(self):
    """This method is called only once to launch the algorithm. It must
       first fill the pool with samples to evaluate and call
       self.signalMasterAndWait() to block until a sample has been
       evaluated. When returning from this method, it MUST check for an
       eventual termination request (with the method
       self.isTerminationRequested()). If the termination is requested, the
       method must perform any necessary cleanup and return as soon as
       possible. Otherwise it can either add new samples to evaluate in the
       pool, do nothing (wait for more samples), or empty the pool and
       return to finish the evaluation.
    """
    print("startToTakeDecision")
    # fill the pool with samples
    iter=0
    self.pool.pushInSample(0, 0.5)
    
    # 
    self.signalMasterAndWait()
    while not self.isTerminationRequested():
      currentId=self.pool.getCurrentId()
      valIn = self.pool.getCurrentInSample().getDoubleValue()
      valOut = self.pool.getCurrentOutSample().getIntValue()
      print("Compute currentId=%s, valIn=%s, valOut=%s" % (currentId, valIn, valOut))
      iter=iter+1
      
      if iter < 3:
        nextSample = valIn + 1
        self.pool.pushInSample(iter, nextSample)
        
      self.signalMasterAndWait()

  def finish(self):
    """Optional method called when the algorithm has finished, successfully
       or not, to perform any necessary clean up."""
    print("Algo finish")
    self.pool.destroyAll()

  def getAlgoResult(self):
    """return the result of the algorithm.
       The object returned is of type indicated by getTCForAlgoResult.
    """
    return 42
```

Here, the entry point in the Python module is directly the name of the class that implements the algorithm : myalgoasync.

## Managing the pool of samples

Samples can be added to the pool at the initialization of the algorithm or
every time a sample is evaluated (while “taking decision”).
The algorithm stops to take decisions when every sample is evaluated.

A sample has:

- an identifier - *Id*
- a priority - it is used to choose the order of evaluation
- a value - *In*
- an evaluated or computed value - *Out*

The current sample is the sample used by the latest terminated evaluation.

These are the methods needed to manage the pool of samples:

```cpp
class Pool
{
    //...
  public:
    //For algorithm use
    int getCurrentId() const ;
    Any *getCurrentInSample() const ;
    Any *getCurrentOutSample() const ;
    Any *getOutSample(int id);
    void pushInSample(int id, Any *inSample, unsigned char priority = 0);
    void destroyAll();
    //...
}
```

In C++, the samples are of type `YACS::ENGINE::Any`, in order to support any
type supported by YACS. For conversion to standard types, use:

- `getIntValue`
- `getBoolValue`
- `getDoubleValue`
- `getStringValue`

It is possible to create a pointer to a new object with:

- `YACS::ENGINE::AtomAny::New`

For further information, see [include/salome/Any.hxx](file:../../../../../include/salome/Any.hxx).

## C++ algorithm calling Python code

In some cases, it can be necessary to implement the algorithm as a C++ class but
nevertheless to call some Python code from this class. This is also possible with the
OptimizerLoop and even quite simple. To achieve this, your C++ class should inherit from
PyOptimizerAlgSync for a synchronous algorithm or from PyOptimizerAlgASync for an
asynchronous algorithm. The guidelines for developing the algorithm are the same as in
the C++ case, but you can also call any method from the Python C API. You don’t need to
take care of the Python global interpreter lock or of thread states because this is
already done in the PyOptimizerAlg classes. An example of this kind of algorithm is the
class OpenTURNSScriptLauncher that can be found in the module OPENTURNS_SRC.
