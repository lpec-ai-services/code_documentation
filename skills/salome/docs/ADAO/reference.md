<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/reference.html -->

# 10. **[DocR]** Reference description of the ADAO commands and keywords

The following sections present the reference description of the ADAO commands
and keywords available through the textual interface (TUI), the graphical
interface (GUI) or through scripts. Two first common sections present the
[[DocR] General entries and outputs](#section-reference-entry) and the [[DocR] Special entries: measurements, functions, matrices, “observer”, post-processing](#section-reference-special-entry).
After that, one describes successively the
[[DocR] Data assimilation or optimization calculation cases](#section-reference-assimilation) and the
[[DocR] Checking cases](#section-reference-checking).

Each command or keyword to be defined through the ADAO TUI or GUI has some
properties. The first property is to be *required*, *optional* or only factual,
describing a type of input. The second property is to be an “open” variable
with a fixed type but with any value allowed by the type, or a “restricted”
variable, limited to some specified values. The embedded case editor GUI having
build-in validating capacities, the properties of the commands or keywords
given through this interface are automatically correct.

# 11. **[DocR]** General entries and outputs

This section describes in a very general way the different options of input
types and output variables. The mathematical notations used are explained in
section [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory).

- [11.1. List of possible input types](ref_entry_types.md)
- [11.2. Description of options of an algorithm by “*AlgorithmParameters*”](ref_options_AlgorithmParameters.md)
- [11.3. Variables and information available at the output](ref_output_variables.md)

# 12. **[DocR]** Special entries: measurements, functions, matrices, “*observer*”, post-processing

This section describes special inputs, such as functional or matrix forms, and
the requirements for using them. The mathematical concepts and notations
related to these inputs are explained in section [[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory).

- [12.1. Requirements for observation or experimental measurements description](ref_observations_requirements.md)
- [12.2. Requirements for functions describing an operator](ref_operator_requirements.md)
- [12.3. Requirements to describe covariance matrices](ref_covariance_requirements.md)
- [12.4. Requirements for describing a state sampling](ref_sampling_requirements.md)
- [12.5. Requirements for functions describing an “*observer*”](ref_observers_requirements.md)
- [12.6. Requirements to describe a post-processing after an ADAO calculation](ref_userpostanalysis_requirements.md)

# 13. **[DocR]** Data assimilation or optimization calculation cases

This section describes algorithmic choices to use data assimilation methods,
optimization methods or methods with reduction, available in ADAO, detailing
their characteristics and their options.

Some examples on these commands usage are available in the section of
[[DocU] Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md#section-tutorials-in-salome),
in the section of
[[DocU] Tutorials on using the ADAO module in Python](tutorials_in_python.md#section-tutorials-in-python),
in the section of
[[DocU] Examples of ADAO use](examples.md#section-docu-examples),
and in the sample files installed with ADAO. The mathematical concepts and
notations used are explained in the general section providing
[[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory).

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

# 14. **[DocR]** Checking cases

This section describes the checking algorithms, available in ADAO, detailing
their usage characteristics and their options.

Some examples on these commands usage are available in the section of
[[DocU] Tutorials on using the ADAO module in SALOME](tutorials_in_salome.md#section-tutorials-in-salome),
in the section of
[[DocU] Tutorials on using the ADAO module in Python](tutorials_in_python.md#section-tutorials-in-python),
in the section of
[[DocU] Examples of ADAO use](examples.md#section-docu-examples),
and in the sample files installed with ADAO. The mathematical concepts and
notations used are explained in the general section providing
[[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory).

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

# 15. **[DocR]** Dedicated tasks or study oriented cases

This section describes the dedicated task or study oriented cases, available in
ADAO, detailing their usage characteristics and their options.

These tasks use algorithms from data assimilation methods, optimization methods
or methods with reduction. We refer to the general section providing
[[DocT] A brief introduction to Data Assimilation and Optimization](theory.md#section-theory) section and to the [[DocR] Data assimilation or optimization calculation cases](#section-reference-assimilation)
section for the underlying algorithmic details.

- [15.1. Task algorithm “*EnsembleOfSimulationGenerationTask*”](ref_algorithm_EnsembleOfSimulationGenerationTask.md)
- [15.2. Task algorithm “*InterpolationByReducedModelTask*”](ref_algorithm_InterpolationByReducedModelTask.md)
- [15.3. Task algorithm “*MeasurementsOptimalPositioningTask*”](ref_algorithm_MeasurementsOptimalPositioningTask.md)
- [15.4. Task algorithm “*ParameterCalibrationTask*”](ref_algorithm_ParameterCalibrationTask.md)
- [15.5. List of commands and keywords for a dedicated task or study oriented case](ref_task_keywords.md)
