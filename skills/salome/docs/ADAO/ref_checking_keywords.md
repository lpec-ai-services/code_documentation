<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/ref_checking_keywords.html -->

# 14.15. List of commands and keywords for an ADAO checking case

We summarize here all the commands and keywords available to describe a
checking case, by avoiding the particularities of each algorithm. It is
therefore a common inventory of commands.

A special term allow to choose explicitly a checking. In the graphical user
interface, this choice is done by the command “*CHECKING_STUDY*”.

All the possible terms, nested or not, are listed by alphabetical order. They
are not required for all the algorithms. The commands or keywords available are
the following

AlgorithmParameters
:   *Dictionary*. This variable indicates the data assimilation or optimization
    algorithm chosen by the keyword “*Algorithm*”, and its potential optional
    parameters. The potential choices by this keyword “*Algorithm*” are available
    through the graphical interface or in the reference documentation containing
    a specific sub-section for each of them. There are for example the “3DVAR”,
    the “Blue”, etc. Optionally, the command also allows to add parameters to
    control the chosen algorithm. Their values are defined either explicitly or
    in a “*Dict*” type object. See the
    [Description of options of an algorithm by “AlgorithmParameters”](ref_options_AlgorithmParameters.md#section-ref-options-algorithm-parameters) for the detailed use of this
    command part.

BackgroundError
:   *Matrix*. This indicates the background error covariance matrix, previously
    noted as $\mathbf{B}$. Its value is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

CheckingPoint
:   *Vector*. The variable indicates the vector used as the state around which to
    perform the required check, noted $\mathbf{x}$ and similar to the
    background $\mathbf{x}^b$. It is defined as a “*Vector*” or
    “*VectorSerie*” type object. Its availability in output is conditioned by the
    boolean “*Stored*” associated with input.

**CHECKING_STUDY**
:   *Required command*. This is the general command describing the checking
    case. It hierarchically contains all the other commands.

Debug
:   *Boolean value*. This variable define the level of trace and intermediary
    debug information. The choices are limited between 0 (for False) and 1 (for
    True).

    Example :
    `{"Debug":False}`

ExecuteInContainer
:   *String*. This variable allows to choose the execution mode in YACS in a
    specific container. In its absence or if its value is “No”, no separate
    container is used for execution and it runs in the main YACS process. If its
    value is “Mono”, a specific YACS container is created and it is used to host
    the execution of all nodes in the same process. If its value is “Multi”, a
    specific YACS container is created and it is used to host the execution of
    each node in a specific process. The default value is “No”, and the possible
    choices are “No”, “Mono” and “Multi”.

    Warning

    In its present version, this command is experimental, and therefore remains
    subject to changes in future versions.

Observation
:   *List of vectors*. The variable indicates the observation vector used for
    data assimilation or optimization, and usually noted $\mathbf{y}^o$.
    Its value is defined as an object of type “*Vector*” if it is a single
    observation (temporal or not) or “*VectorSeries*” if it is a succession of
    observations. Its availability in output is conditioned by the boolean
    “*Stored*” associated in input.

ObservationError
:   *Matrix*. The variable indicates the observation error covariance matrix,
    usually noted as $\mathbf{R}$. It is defined as a “*Matrix*” type
    object, a “*ScalarSparseMatrix*” type object, or a “*DiagonalSparseMatrix*”
    type object, as described in detail in the section
    [Requirements to describe covariance matrices](ref_covariance_requirements.md#section-ref-covariance-requirements). Its availability in output is
    conditioned by the boolean “*Stored*” associated with input.

ObservationOperator
:   *Operator*. The variable indicates the observation operator, usually noted as
    $H$, which transforms the input parameters $\mathbf{x}$ to
    results $\mathbf{y}$ to be compared to observations
    $\mathbf{y}^o$. Its value is defined as a “*Function*” type object or a
    “*Matrix*” type one. In the case of “*Function*” type, different functional
    forms can be used, as described in the section
    [Requirements for functions describing an operator](ref_operator_requirements.md#section-ref-operator-requirements). If there is some control $U$
    included in the observation, the operator has to be applied to a pair
    $(X,U)$.

Observers
:   *List of functions linked to variables*. This command allows to set internal
    observers, that are functions linked with a particular variable, which will
    be executed each time this variable is modified. It is a convenient way to
    monitor variables of interest during the data assimilation or optimization
    process, by printing or plotting it, etc. Common templates are provided to
    help the user to start or to quickly make his case.

StudyName
:   *String*. This variable is an open string to identify or describe the ADAO
    study by a name or a sentence.

StudyRepertory
:   *String*. If available, the directory specified by this string is used as
    base name for calculation, and also used to find all the script files given
    by name without path, that can define some other commands by scripts.

UserDataInit
:   *Script name*. This variable allows to initialize some parameters or
    data automatically before algorithm input processing. It indicates a script
    file name to be executed before entering in initialization phase of chosen
    variables.
