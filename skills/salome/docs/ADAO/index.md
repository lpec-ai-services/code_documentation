<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/index.html -->

# ADAO documentation

![ADAO logo](https://docs.salome-platform.org/latest/gui/ADAO/en/_images/ADAO_logo.png)

**The ADAO module provides data assimilation and optimization** features in
Python [[Python]](bibliography.md#python) or SALOME context [[Salome]](bibliography.md#salome).

Briefly stated, Data Assimilation is a methodological framework to compute the
optimal estimate of the inaccessible true value of a system state, eventually
over time. It uses information coming from experimental measurements or
observations, and from numerical *a priori* models, including information about
their errors. Some methods that are parts of the framework are also known under
the names of
*adjustment*,
*calibration*,
*state estimation*,
*parameter estimation*,
*parameter adjustment*,
*inverse problems*,
*inverse methods*,
*inversion*,
*Bayesian estimation*,
*optimal interpolation*,
*optimal learning*,
*mathematical regularization*,
*meta-heuristics* for optimization,
*model reduction*,
*assimilation in reduced space*,
*data smoothing*,
etc.
More details can be found in the section [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory). The ADAO module
currently offers more than 150 different algorithmic methods and allows the
study of more than 300 distinct applied problems.

The documentation for this module is divided into several major categories,
related to the **theoretical documentation** (indicated in the section title by
**[DocT]**), to the **user documentation** (indicated in the section title by
**[DocU]**), and to the **reference documentation** (indicated in the section
title by **[DocR]**).

The first part is the [Introduction to ADAO](intro.md#section-intro). The second part introduces
[[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory), and their concepts, and the next part describes the
[[DocT] Methodology to elaborate a Data Assimilation or Optimization study](methodology.md#section-methodology). For a standard user, the next parts describe some
[[DocU] Examples of ADAO use](examples.md#section-docu-examples), quickly accessible by the collection of pointers
to the subsections. Didactic presentations are detailed in
[[DocU] Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md#section-tutorials-in-salome) or [[DocU] Tutorials on using the ADAO module in Python](tutorials_in_python.md#section-tutorials-in-python),
supplemented by information on the [[DocU] Advanced usage of the ADAO module and interoperability](advanced.md#section-advanced) with how to obtain
additional information or how to use non-GUI command execution scripting.

Users interested in quick access to the module can stop before reading the
remaining parts, but a valuable use of the module requires reading and
returning to these parts regularly. The following parts describe
[[DocR] Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md#section-gui-in-salome) and [[DocR] Textual User Interface for ADAO (TUI/API)](tui.md#section-tui). The last main part gives a
detailed [[DocR] Reference description of the ADAO commands and keywords](reference.md#section-reference), with three essential main sub-parts
describing the details of commands and options of the algorithms. A
[Glossary](glossary.md#section-glossary), some [Notations and common conventions](notations.md#section-notations), a
[Bibliography](bibliography.md#section-bibliography), some elements about [Versions of ADAO and external compatibility](versions.md#section-versions), and
an extensive index are included in the document. And, to comply with the module
requirements, be sure to read the part [License and requirements](license.md#section-license).

Table of contents

- [1. Introduction to ADAO](intro.md)
- [2. **[DocT]** A brief introduction to Data Assimilation and Optimization](theory.md)
  - [2.1. Fields reconstruction or measures interpolation](theory.md#fields-reconstruction-or-measures-interpolation)
  - [2.2. Parameters identification, models adjustment, or calibration](theory.md#parameters-identification-models-adjustment-or-calibration)
  - [2.3. Joint estimation of states and parameters](theory.md#joint-estimation-of-states-and-parameters)
  - [2.4. Simple description of the data assimilation methodological framework](theory.md#simple-description-of-the-data-assimilation-methodological-framework)
  - [2.5. A schematic view of Data Assimilation and Optimization approaches](theory.md#a-schematic-view-of-data-assimilation-and-optimization-approaches)
  - [2.6. An overview of reduction methods and of reduced optimization](theory.md#an-overview-of-reduction-methods-and-of-reduced-optimization)
  - [2.7. Going further in the data assimilation framework](theory.md#going-further-in-the-data-assimilation-framework)
  - [2.8. Going further in the state estimation by optimization methods](theory.md#going-further-in-the-state-estimation-by-optimization-methods)
  - [2.9. Going further in data assimilation for dynamics](theory.md#going-further-in-data-assimilation-for-dynamics)
- [3. **[DocT]** Methodology to elaborate a Data Assimilation or Optimization study](methodology.md)
  - [3.1. Logical procedure for a study](methodology.md#logical-procedure-for-a-study)
  - [3.2. Detailed procedure for a study](methodology.md#detailed-procedure-for-a-study)
  - [3.3. To test a data assimilation chain: the twin experiments](methodology.md#to-test-a-data-assimilation-chain-the-twin-experiments)
- [4. **[DocU]** Examples of ADAO use](examples.md)
  - [4.1. General usage guidelines](examples.md#general-usage-guidelines)
  - [4.2. Tutorials](examples.md#tutorials)
  - [4.3. Calculation algorithms uses](examples.md#calculation-algorithms-uses)
  - [4.4. Checking algorithms uses](examples.md#checking-algorithms-uses)
  - [4.5. Dedicated tasks or study oriented cases uses](examples.md#dedicated-tasks-or-study-oriented-cases-uses)
  - [4.6. Comprehensive studies and use case examples](examples.md#comprehensive-studies-and-use-case-examples)
  - [4.7. Advanced uses](examples.md#advanced-uses)
- [5. **[DocU]** Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md)
  - [5.1. Building an estimation case with explicit data definition](tutorials_in_salome.md#building-an-estimation-case-with-explicit-data-definition)
  - [5.2. Building an estimation case with external data definition by scripts](tutorials_in_salome.md#building-an-estimation-case-with-external-data-definition-by-scripts)
  - [5.3. Adding parameters to control the data assimilation algorithm](tutorials_in_salome.md#adding-parameters-to-control-the-data-assimilation-algorithm)
  - [5.4. Building a complex case with external data definition by scripts](tutorials_in_salome.md#building-a-complex-case-with-external-data-definition-by-scripts)
- [6. **[DocU]** Tutorials on using the ADAO module in Python](tutorials_in_python.md)
  - [6.1. Building an estimation case with explicit data definition](tutorials_in_python.md#building-an-estimation-case-with-explicit-data-definition)
  - [6.2. Building an estimation case with external data definition by scripts](tutorials_in_python.md#building-an-estimation-case-with-external-data-definition-by-scripts)
- [7. **[DocU]** Advanced usage of the ADAO module and interoperability](advanced.md)
  - [7.1. Converting and executing an ADAO command file (JDC) using a Shell script](advanced.md#converting-and-executing-an-adao-command-file-jdc-using-a-shell-script)
  - [7.2. Running an ADAO calculation scheme in YACS using the text user mode (YACS TUI)](advanced.md#running-an-adao-calculation-scheme-in-yacs-using-the-text-user-mode-yacs-tui)
  - [7.3. Running an ADAO calculation in R environment using the TUI ADAO interface](advanced.md#running-an-adao-calculation-in-r-environment-using-the-tui-adao-interface)
  - [7.4. Using the ADAO EFICAS graphical interface as an ADAO TUI command](advanced.md#using-the-adao-eficas-graphical-interface-as-an-adao-tui-command)
  - [7.5. Change the default execution mode of nodes in YACS](advanced.md#change-the-default-execution-mode-of-nodes-in-yacs)
  - [7.6. Getting information on special variables during the ADAO calculation](advanced.md#getting-information-on-special-variables-during-the-adao-calculation)
  - [7.7. Getting more information when running a calculation](advanced.md#getting-more-information-when-running-a-calculation)
  - [7.8. Accelerating numerical derivatives calculations by using a parallel mode](advanced.md#accelerating-numerical-derivatives-calculations-by-using-a-parallel-mode)
  - [7.9. Convergence control for calculation cases and iterative algorithms](advanced.md#convergence-control-for-calculation-cases-and-iterative-algorithms)
- [8. **[DocR]** Graphical User Interface for ADAO (GUI/EFICAS)](gui_in_salome.md)
  - [8.1. Logical procedure to build an ADAO case](gui_in_salome.md#logical-procedure-to-build-an-adao-case)
  - [8.2. Detailed procedure to build an ADAO case](gui_in_salome.md#detailed-procedure-to-build-an-adao-case)
- [9. **[DocR]** Textual User Interface for ADAO (TUI/API)](tui.md)
  - [9.1. Creation of ADAO TUI calculation case and examples](tui.md#creation-of-adao-tui-calculation-case-and-examples)
  - [9.2. Set of available commands in text user interface TUI](tui.md#set-of-available-commands-in-text-user-interface-tui)
  - [9.3. More advanced examples of ADAO TUI calculation case](tui.md#more-advanced-examples-of-adao-tui-calculation-case)
- [10. **[DocR]** Reference description of the ADAO commands and keywords](reference.md)
- [11. **[DocR]** General entries and outputs](reference.md#docr-general-entries-and-outputs)
  - [11.1. List of possible input types](ref_entry_types.md)
  - [11.2. Description of options of an algorithm by “*AlgorithmParameters*”](ref_options_AlgorithmParameters.md)
  - [11.3. Variables and information available at the output](ref_output_variables.md)
- [12. **[DocR]** Special entries: measurements, functions, matrices, “*observer*”, post-processing](reference.md#docr-special-entries-measurements-functions-matrices-observer-post-processing)
  - [12.1. Requirements for observation or experimental measurements description](ref_observations_requirements.md)
  - [12.2. Requirements for functions describing an operator](ref_operator_requirements.md)
  - [12.3. Requirements to describe covariance matrices](ref_covariance_requirements.md)
  - [12.4. Requirements for describing a state sampling](ref_sampling_requirements.md)
  - [12.5. Requirements for functions describing an “*observer*”](ref_observers_requirements.md)
  - [12.6. Requirements to describe a post-processing after an ADAO calculation](ref_userpostanalysis_requirements.md)
- [13. **[DocR]** Data assimilation or optimization calculation cases](reference.md#docr-data-assimilation-or-optimization-calculation-cases)
  - [13.1. Calculation algorithm “*3DVAR*”](ref_algorithm_3DVAR.md)
  - [13.2. Calculation algorithm “*4DVAR*”](ref_algorithm_4DVAR.md)
  - [13.3. Calculation algorithm “*Blue*”](ref_algorithm_Blue.md)
  - [13.4. Calculation algorithm “*DerivativeFreeOptimization*”](ref_algorithm_DerivativeFreeOptimization.md)
  - [13.5. Calculation algorithm “*DifferentialEvolution*”](ref_algorithm_DifferentialEvolution.md)
  - [13.6. Calculation algorithm “*EnsembleBlue*”](ref_algorithm_EnsembleBlue.md)
  - [13.7. Calculation algorithm “*EnsembleKalmanFilter*”](ref_algorithm_EnsembleKalmanFilter.md)
  - [13.8. Calculation algorithm “*ExtendedBlue*”](ref_algorithm_ExtendedBlue.md)
  - [13.9. Calculation algorithm “*ExtendedKalmanFilter*”](ref_algorithm_ExtendedKalmanFilter.md)
  - [13.10. Calculation algorithm “*KalmanFilter*”](ref_algorithm_KalmanFilter.md)
  - [13.11. Calculation algorithm “*LinearLeastSquares*”](ref_algorithm_LinearLeastSquares.md)
  - [13.12. Calculation algorithm “*NonLinearLeastSquares*”](ref_algorithm_NonLinearLeastSquares.md)
  - [13.13. Calculation algorithm “*ParticleSwarmOptimization*”](ref_algorithm_ParticleSwarmOptimization.md)
  - [13.14. Calculation algorithm “*QuantileRegression*”](ref_algorithm_QuantileRegression.md)
  - [13.15. Calculation algorithm “*SimulatedAnnealing*”](ref_algorithm_SimulatedAnnealing.md)
  - [13.16. Calculation algorithm “*TabuSearch*”](ref_algorithm_TabuSearch.md)
  - [13.17. Calculation algorithm “*UnscentedKalmanFilter*”](ref_algorithm_UnscentedKalmanFilter.md)
  - [13.18. List of commands and keywords for data assimilation or optimization case](ref_assimilation_keywords.md)
- [14. **[DocR]** Checking cases](reference.md#docr-checking-cases)
  - [14.1. Checking algorithm “*AdjointTest*”](ref_algorithm_AdjointTest.md)
  - [14.2. Checking algorithm “*ControledFunctionTest*”](ref_algorithm_ControledFunctionTest.md)
  - [14.3. Checking algorithm “*FunctionTest*”](ref_algorithm_FunctionTest.md)
  - [14.4. Checking algorithm “*GradientTest*”](ref_algorithm_GradientTest.md)
  - [14.5. Checking algorithm “*InputValuesTest*”](ref_algorithm_InputValuesTest.md)
  - [14.6. Checking algorithm “*InterpolationByReducedModelTest*”](ref_algorithm_InterpolationByReducedModelTest.md)
  - [14.7. Checking algorithm “*LinearityTest*”](ref_algorithm_LinearityTest.md)
  - [14.8. Checking algorithm “*LocalSensitivityTest*”](ref_algorithm_LocalSensitivityTest.md)
  - [14.9. Checking algorithm “*ObservationSimulationComparisonTest*”](ref_algorithm_ObservationSimulationComparisonTest.md)
  - [14.10. Checking algorithm “*ObserverTest*”](ref_algorithm_ObserverTest.md)
  - [14.11. Checking algorithm “*ParallelFunctionTest*”](ref_algorithm_ParallelFunctionTest.md)
  - [14.12. Checking algorithm “*ReducedModelingTest*”](ref_algorithm_ReducedModelingTest.md)
  - [14.13. Checking algorithm “*SamplingTest*”](ref_algorithm_SamplingTest.md)
  - [14.14. Checking algorithm “*TangentTest*”](ref_algorithm_TangentTest.md)
  - [14.15. List of commands and keywords for an ADAO checking case](ref_checking_keywords.md)
- [15. **[DocR]** Dedicated tasks or study oriented cases](reference.md#docr-dedicated-tasks-or-study-oriented-cases)
  - [15.1. Task algorithm “*EnsembleOfSimulationGenerationTask*”](ref_algorithm_EnsembleOfSimulationGenerationTask.md)
  - [15.2. Task algorithm “*InterpolationByReducedModelTask*”](ref_algorithm_InterpolationByReducedModelTask.md)
  - [15.3. Task algorithm “*MeasurementsOptimalPositioningTask*”](ref_algorithm_MeasurementsOptimalPositioningTask.md)
  - [15.4. Task algorithm “*ParameterCalibrationTask*”](ref_algorithm_ParameterCalibrationTask.md)
  - [15.5. List of commands and keywords for a dedicated task or study oriented case](ref_task_keywords.md)
- [16. Versions of ADAO and external compatibility](versions.md)
  - [16.1. Switching from a version of ADAO to a newer one](versions.md#switching-from-a-version-of-adao-to-a-newer-one)
  - [16.2. Versions of ADAO compatibility with support tools](versions.md#versions-of-adao-compatibility-with-support-tools)
- [17. Notations and common conventions](notations.md)
- [18. License and requirements](license.md)
- [19. Bibliography](bibliography.md)
- [20. Glossary](glossary.md)
- [Index](genindex.md)

- [Search Page](search.md)
