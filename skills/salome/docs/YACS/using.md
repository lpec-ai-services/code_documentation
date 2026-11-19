<!-- source: https://docs.salome-platform.org/latest/gui/YACS/using.html -->

# The YACS User Guide

There is an increasing need for multidisciplinary parametric simulations in various research and engineering fields.
Examples are fluid-structure interaction and thermal coupling.
The simulation tools have become very sophisticated in their own domains, so multidisciplinary simulation can be achieved
by coupling the existing codes.

YACS is a tool for managing multidisciplinary simulations through calculation schemes.

The YACS module can be used to build and execute calculation schemes. A calculation scheme is a more or less complex
assembly of calculation components (SALOME components or calculation codes or python scripts).
Therefore, a calculation scheme provides a means of defining a chain or coupling of calculation codes (see [YACS general principles](principes.md#principes)).

![figure](https://docs.salome-platform.org/latest/gui/YACS/_images/ihm.png)

**YACS GUI**

A calculation scheme can be built either using a graphic tool (see [Using YACS with the graphical user interface (GUI)](gui.md#gui)),
or by editing an XML file directly (see [Defining a calculation scheme in the XML format](schemaxml.md#schemaxml)), or by using
an application programming interface (API) in Python (see [Defining a calculation scheme with the Python programming interface](schemapy.md#schemapy)).
In this phase, chaining of components is defined with the associated dataflows.

Many examples of YACS schemas are installed with SALOME. They can be found in
the directory SALOME_APPLICATION/share/salome/yacssample (SALOME_APPLICATION
is the path where SALOME application is installed).

The calculation scheme can be executed from the graphic tool (see [Execution of a schema](execution.md#execution)), but also in console
mode (see [Executing a calculation scheme in console mode](execxml.md#execxml)), or by using the Python interface (see [Execution of a calculation scheme with the Python programming interface](execpy.md#execpy)).

Executing a calculation scheme includes:

> - running and distributing components
> - managing data distribution
> - monitoring execution
> - stopping / suspending / restarting the execution

A calculation scheme can also be executed using a batch system such as LSF or PBS (see [Starting a SALOME application in a batch manager](batch.md#batch)).

Finally, it is essential that calculation codes should be transformed into SALOME components, so that they can
be coupled with YACS. In general, this operation requires good knowledge of SALOME principles (see [Integration of components into SALOME for YACS](integration.md#integration)).

For C++ calculation codes, the [hxx2salome : a SALOME component generator](hxx2salome.md#hxx2salome) tool automates this operation to a large extent.

- [Reminders about the SALOME platform](rappels.md)
  - [Definitions](rappels.md#definitions)
  - [SALOME modules and components](rappels.md#salome-modules-and-components)
  - [Containers](rappels.md#containers)
  - [Construction and use of a SALOME application](rappels.md#construction-and-use-of-a-salome-application)
- [YACS general principles](principes.md)
  - [Data types](principes.md#data-types)
  - [Ports](principes.md#ports)
  - [Elementary calculation nodes](principes.md#elementary-calculation-nodes)
  - [Connections](principes.md#connections)
  - [Composite nodes](principes.md#composite-nodes)
  - [Containers](principes.md#containers)
  - [States of a node](principes.md#states-of-a-node)
  - [Context sensitive naming of nodes](principes.md#context-sensitive-naming-of-nodes)
  - [Error report](principes.md#error-report)
  - [Execution trace files](principes.md#execution-trace-files)
  - [Schema shutdown](principes.md#schema-shutdown)
  - [YACS general architecture](principes.md#yacs-general-architecture)
- [Using YACS with the graphical user interface (GUI)](gui.md)
  - [YACS GUI description](gui.md#yacs-gui-description)
  - [Functionality list](gui.md#functionality-list)
  - [YACS schema examples](gui.md#yacs-schema-examples)
- [Using YACS in console mode](console.md)
  - [Defining a calculation scheme in the XML format](schemaxml.md)
  - [Executing a calculation scheme in console mode](execxml.md)
- [Using YACS with the python interface (TUI)](python.md)
  - [Defining a calculation scheme with the Python programming interface](schemapy.md)
  - [Execution of a calculation scheme with the Python programming interface](execpy.md)
  - [Advanced use of the Python programming interface](advancepy.md)
- [Starting a SALOME application in a batch manager](batch.md)
  - [Principles](batch.md#principles)
  - [Description of the cluster using the CatalogResource.xml file](batch.md#description-of-the-cluster-using-the-catalogresource-xml-file)
  - [Using the Launcher service](batch.md#using-the-launcher-service)
  - [SALOME on the batch cluster](batch.md#salome-on-the-batch-cluster)
  - [SALOME constraints on batch managers](batch.md#salome-constraints-on-batch-managers)
- [Definition of an algorithm for the OptimizerLoop](optimizer.md)
  - [Synchronous algorithm](optimizer.md#synchronous-algorithm)
  - [Asynchronous algorithm](optimizer.md#asynchronous-algorithm)
  - [Managing the pool of samples](optimizer.md#managing-the-pool-of-samples)
  - [C++ algorithm calling Python code](optimizer.md#c-algorithm-calling-python-code)
- [Concurrent branches and multiple machine execution](resource.md)
  - [Execution of concurrent branches](resource.md#execution-of-concurrent-branches)
  - [Execution on multiple machines](resource.md#execution-on-multiple-machines)
  - [Execution on multiple machines with mutliples HP container types](resource.md#execution-on-multiple-machines-with-mutliples-hp-container-types)
- [Loading and executing a PMML file](pmml.md)
  - [Authorized PMML model types](pmml.md#authorized-pmml-model-types)
  - [Description of PyLoadPMML](pmml.md#description-of-pyloadpmml)
  - [Example of model execution](pmml.md#example-of-model-execution)
