<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_options_AlgorithmParameters.html -->

# 11.2. Description of options of an algorithm by “*AlgorithmParameters*”

Each algorithm can be controlled using some specific options or parameters. They
are given through the “*Parameters*” optional command included in the mandatory
command “*AlgorithmParameters*”.

There are several convenient methods for providing these options, either using
the ADAO EFICAS graphical interface (GUI) or the textual interface (TUI). The
method is determined as follows:

1. Either in the graphical user interface (GUI), using the “*Parameters*”
   keyword in the “*AlgorithmParameters*” command, which allows you to choose
   between “*Defaults*” (use of explicit keywords pre-populated by the default
   values of the parameters) and “*Dict*” (use of a dictionary to fill in the
   necessary keywords),
2. Or in the graphical user interface (GUI), only in the case “*Dict*” of
   “*Parameters*”, by the included keyword “*FROM*” which allows to choose
   between an entry by string or an entry by Python script file.
3. Or in textual interface (TUI), using the “*Parameters*” keyword in the
   “*AlgorithmParameters*” command, in a similar way to the graphical
   interface, by filling in the explicit keywords described in the
   documentation of each algorithm.
4. Or in textual interface (TUI), using the keyword “*Parameters*” in the
   command “*AlgorithmParameters*”, providing a script containing a dictionary
   similar to methods two and three and compatible with these GUI entries.

These last two options are the ones that can be used in the textual interface
(TUI) in a similar and compatible way to the two previous ones based on the
graphical interface (GUI).

If an option or a parameter is specified by the user for an algorithm that does
not support it, the option is simply ignored (left unused) and don’t stop the
treatment. The meaning of the acronyms or particular names can be found in the
index or the [Glossary](glossary.md#section-glossary).

## 11.2.1. First method (GUI): using explicit pre-filled keywords

To give the parameters values by explicit pre-filled keywords, directly in the
graphical interface, the user selects the type “*Defaults*” in the keyword
“*Parameters*”, then the keywords in the given “*Parameters[Algo]*” list which
appears, linked with the chosen algorithm, as shown in the following figure:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_defaults.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_defaults.png)
>
> ****Using explicit pre-filled keywords for algorithmic parameters****

Each parameter is optional, and it is presented with its default value when it
is selected by the user. One can then modify its value, or fill it in list cases
for example.

It is the recommended way to modify only some algorithmic parameters in a safe
way. This method allows only to define authorized parameters for a given
algorithm, and the defined values are not kept if the user changes the
algorithm.

This method is naturally not usable in TUI interface.

## 11.2.2. Second method(GUI): using a string in the graphical interface

To give the parameters values as a string, directly in the graphical interface,
the user selects the type “*Dict*” in the keyword “*Parameters*”, then the type
“*String*” in the keyword “*FROM*” of the “*Dict*” command which appears, as
shown in the following figure:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_string.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_string.png)
>
> ****Using a string for algorithmic parameters****

In the entry, one must enclose a standard dictionary definition between simple
quotes, as for example:

```python
'{"MaximumNumberOfIterations":25,"SetSeed":1000}'
```

It is the recommended way to define algorithmic parameters. This method allows
in particular to keep options or parameters for other algorithms than the
currently used one. It is then easier to change of algorithm or to keep default
values different of the standard defaults.

## 11.2.3. Third method (GUI): using an external Python script file

To give the parameters values as an external Python script file, the user
selects in the graphical interface the type “*Dict*” in the keyword
“*Parameters*”, then the type “*Script*” in the keyword “*FROM*” of the “*Dict*”
command which appears, as shown in the following figure:

> [![figure](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_script.png)](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/adao_algopar_script.png)
>
> ****Using an external file for algorithmic parameters****

This external Python script file, named for example here `myParameters.py`,
must define a dictionary variable with the imposed name “*Parameters*” or
“*AlgorithmParameters*”, like the following example:

Listing 11.1 myParameters.py: parameters file

```python
AlgorithmParameters = {
    "MaximumNumberOfIterations" : 25,
    "StoreSupplementaryCalculations" : [
        "CurrentState",
        "APosterioriCovariance",
        "OMA",
        ],
    }
```

Moreover, the file can contain other Python commands. This method also allows,
like the previous one, to keep externally options or parameters for other
algorithms than the one we are using.

## 11.2.4. Fourth method (TUI): use explicit documented keywords

In the textual interface (TUI), the control of the algorithms is done by using
the command “*setAlgorithmParameters*”. It allows to fill in or define the
keywords described in the documentation of each ADAO calculation case. Just to
remind you, these keywords are the same as the ones presented in the graphical
interface.

To do this, a dictionary of “keyword/value” pairs can be given as an argument
to the “*Parameters*” keyword of the command. For a TUI calculation case named
for example `case`, the syntax looks like the following code:

```python
[...]
case.setAlgorithmParameters(
    Algorithm='3DVAR',
    Parameters={
        "MaximumNumberOfIterations" : 25,
        "StoreSupplementaryCalculations" : [
            "CurrentState",
            "APosterioriCovariance",
            "OMA",
            ],
        },
    )
[...]
```

The argument values can obviously come from Python evaluations or previously
defined variables, making it easy to insert ADAO commands into the Python
scripting flow of a study.

## 11.2.5. Fifth method (TUI): use an external Python script file

In the textual interface (TUI), a file can be given as argument in the same and
compatible way as the third method dedicated to the graphical interface (GUI).
An external Python script file named `myParameters.py`, and containing for
example the information already mentioned for the third method, is the
following:

Listing 11.2 Simple version of myParameters.py

```python
AlgorithmParameters = {
    "MaximumNumberOfIterations" : 25,
    "StoreSupplementaryCalculations" : [
        "CurrentState",
        "APosterioriCovariance",
        "OMA",
        ],
    }
```

For a TUI computation case named for example `case`, which has to read this
file, the textual interface command uses the argument “*Script*” in the
following form:

```python
[...]
case.setAlgorithmParameters( Algorithm = "3DVAR", Script = "myParameters.py" )
[...]
```

Alternatively and completely equivalently, to comply with the definition
required by the “*setAlgorithmParameters*” command, one can use in the external
Python script `myParameters.py` the name “*Parameters*” instead of
“*AlgorithmParameters*” in the form:

Listing 11.3 Simple version of myParameters.py

```python
Parameters = {
    "MaximumNumberOfIterations" : 25,
    "StoreSupplementaryCalculations" : [
        "CurrentState",
        "APosterioriCovariance",
        "OMA",
        ],
    }
```

The loading command in the textual interface remains the same. One can also add
in the external script the name of the algorithm with its own keyword
“*Algorithm*” (which in this case is required, and cannot be included as an
option in “*AlgorithmParameters*”):

Listing 11.4 Full version of myParameters.py

```python
Algorithm='3DVAR'
Parameters = {
    "MaximumNumberOfIterations" : 25,
    "StoreSupplementaryCalculations" : [
        "CurrentState",
        "APosterioriCovariance",
        "OMA",
        ],
    }
```

The textual interface loading command is then simplified to a single argument:

```python
[...]
case.setAlgorithmParameters(Script = "myParameters.py")
[...]
```

This last form is the simplest way to fully parameterize algorithm inputs in an
external Python script, which can then be controlled or generated by a wider
process of study building including the ADAO commands.
