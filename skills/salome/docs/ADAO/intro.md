<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/intro.html -->

# 1. Introduction to ADAO

The aim of the ADAO module is **to help using data assimilation or optimization
methodology, in conjunction with other modules or simulation codes, in Python**
[[Python]](bibliography.md#python) **or SALOME context** [[Salome]](bibliography.md#salome). It provides a simple interface to
many robust and powerful data assimilation or optimization algorithms, with or
without reduction, as well as testing and verification aids. It allows to
integrate these tools in a Python or SALOME study.

Its main objective is to **provide the use of standard and robust data
assimilation or optimization methods, in a usual numerical simulation study
approach, in an efficient way, while remaining easy to setup, and by providing
a simplified approach to help the implementation**. For the end user, who has
previously collected information on his physical problem, the environment
allows him to have an approach centered on the simple declaration of this
information to build a valid ADAO case, to then evaluate it, and to get the
physical results he needs.

The module covers a wide variety of practical applications, in a robust way,
allowing for real world engineering applications, and also for performing quick
methodological experimentation. It is based on the use of other Python or
SALOME modules, in particular YACS and EFICAS if available, and on the use of
an underlying generic data assimilation library and tools. The computational or
simulation user modules must provide one or more specific calling methods in
order to be callable in the Python or SALOME framework. In the SALOME
environment, all native modules can be used through integration in Python or
YACS.
