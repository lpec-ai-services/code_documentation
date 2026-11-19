# Index of pages

Each entry: file — title, then its main headings.


## (root)

- `changelog.md` — **Changelog** (1 kB)
- `devs.md` — **For developers** (1 kB)
- `getting_started.md` — **Getting started** (1 kB)
- `index.md` — **The valjean documentation** (1 kB)
- `modules.md` — **Package API** (1 kB)
- `todo.md` — **TODO list** (1 kB)
- `what.md` — **What is valjean?** (1 kB)

## devs

- `devs/documentation.md` — **Building the documentation** (3 kB)
  - Version numbering weirdness · Extensions · Checking references · Checking external links · Building the documentation for the tests · tox` integration
- `devs/linting.md` — **Linting** (1 kB)
  - Suppressing linter warnings · tox` integration
- `devs/release_checklist.md` — **Release checklist** (2 kB)
- `devs/sdist.md` — **Distributing the code** (2 kB)
  - Source distribution · Creation · Installation · Conda package · Creation · Installation · Documentation package · Creation · Installation
- `devs/setup.md` — **Installation and setup** (1 kB)
  - Dependency management
- `devs/testing.md` — **Testing** (4 kB)
  - Unit tests · Property-based testing and the [hypothesis](https://hypothesis.readthedocs.io/en/latest/) package · Testing example docstrings with [pytest](https://docs.pytest.org/en/latest) · tox` integration
- `devs/tox.md` — **Using `tox` for continuous integration** (1 kB)
  - Configuration · Available test environments · Additional environments · Using `tox` from the command line

## examples

- `examples/README.md` — **Valjean-demo #** (2 kB)
  - Installation from git ## · Prerequisites ## · Description of the package ## · Examples using *valjean* directly in python ### · Examples using *valjean* executable ###
- `examples/examples.md` — **Examples (in French)** (1 kB)
  - Notebooks · Jobs
- `examples/jobs/spherical_cows/job.md` — **Vaches sphériques** (14 kB)
  - Fichier `job.py · Imports · Définitions des chemins et des paramètres · Systèmes à tester · Définition de la fonction `job() · Comparaison TRIPOLI-4/MCNP pour un système donné · Fonctions auxiliaires · Exécution
- `examples/notebooks/ap3_reader/ap3_picker.md` — **Lecture des fichiers *rates* d'Apollo3 grâce au `Picker`** (4 kB)
  - Le `Picker` : résumé · Inspection du fichier HDF5 · Sélection des résultats · Exemple sur les $k_{eff}$ · Exemple sur les flux (arrays) · Comparaison de résultats
- `examples/notebooks/ap3_reader/ap3_reader.md` — **Lecture des fichiers *rates* d'Apollo3 : le `Reader`** (9 kB)
  - Le `Reader` : résumé · Inspection du fichier · Sélection des résultats · Comparaison de résultats · Import du test et des représentations (voir les autres notebooks) · Comparaison des aborptions pour différents isotopes · Comparaison de la diffusion pour les différentes valeurs d'anisotropie · Comparaison des courants entrants et sortants
- `examples/notebooks/dataset_representation/meshes_with_scatter_plots.md` — **Représentation de scores sur maillages** (12 kB)
  - Les imports par défaut · Quelques fonctions · Sélection des intervalles · Représentation des mailles individuelles · Cas d'une maille cartésienne alignée sur les axes · Cas d'une maille cartésienne dont les axes ont été tournés
- `examples/notebooks/godiva_keff/godiva_keff.md` — **Godiva : analyse de $k_\mathrm{eff}$** (7 kB)
  - Parsing du jeu de données et exploration des résultats · Sélection des $k_\mathrm{eff}$ · $k_\mathrm{eff}$ "génériques" · $k_\mathrm{eff}$ "automatiques" · Exemples de comparaison de $k_\mathrm{eff}$
- `examples/notebooks/livermore_exps/spheres_example.md` — **Sphères de Livermore** (14 kB)
  - Description rapide de l'expérience · Parsing des résultats Tripoli-4 et récupération du spectre · Parser les résultats · Sélection du résultat · Transformation des données en `Dataset · Normalisation du spectre · Réarrangement des intervalles · Résultats expérimentaux · Comparaison entre données et expérience · Comparaisons numériques … (+2)
- `examples/notebooks/replica/replica_example.md` — **Benchmark REPLICA : exemples de parsing** (16 kB)
  - Principe du parsing des sorties Tripoli-4 standard · Exemple de parsing, jeu de données `fast_neutron.t4 · Présentation du jeu de données · Étape 1 : scan puis parsing du résultat · Étape 2 : sélection des données grâce au `Browser · Étape 3 : utilisation d'un `Dataset · Étape 4 : faire un test et le représenter, exemple du test de Student
- `examples/notebooks/sensitivities/sensitivities_example.md` — **Parsing des sensibilités** (15 kB)
  - Exemples de sélection · Sélection 1 : réponses correspondant à l'U238 · Sélection 2 : réponses correspondant à des sections efficaces · Sélection 3 : réponses correspondant au code de section efficace 52 ($n \rightarrow \gamma$ absorption) · Sélection 4 : première réponse (0) : les $k_\mathrm{eff}$ · Sélection 5 : boucle sur toutes les réponses · Exemples de comparaison de $k_\mathrm{eff}$ · Représentation avec le `TestStudent · Représentation avec le `TestApproxEqual · Représentation avec `TestEqual

## getting_started

- `getting_started/doc.md` — **Documentation** (1 kB)
- `getting_started/exe.md` — **The `valjean` executable** (1 kB)
- `getting_started/install.md` — **Installing `valjean`** (4 kB)
  - Requirements · Getting the code · Quick start · Using virtual environments · Prerequisites · Using conda · Checking package integrity

## modules

- `modules/cambronne.md` — **cambronne — Commandes, Actions et MoBilisation Rapide des OpératioNs Exécutables** (1 kB)
- `modules/cambronne/commands/env.md` — **`env` — The `env` subcommand** (1 kB)
  - class valjean.cambronne.commands.env.EnvCommand  — bases: Command
- `modules/cambronne/commands/graph.md` — **`graph` — The `graph` subcommand** (1 kB)
  - class valjean.cambronne.commands.graph.GraphCommand  — bases: JobCommand
- `modules/cambronne/commands/run.md` — **`run` — The `run` subcommand** (1 kB)
  - class valjean.cambronne.commands.run.RunCommand  — bases: JobCommand · valjean.cambronne.commands.run.schedule(*, hard_graph, soft_graph, env, config=None, workers=1)
- `modules/cambronne/common.md` — **`common` — Common tools for the `valjean` executable** (3 kB)
  - class valjean.cambronne.common.Command · class valjean.cambronne.common.DictKwargAction  — bases: argparse.Action · class valjean.cambronne.common.JobCommand  — bases: Command · valjean.cambronne.common.run_job(job_file, job_args, job_kwargs) · valjean.cambronne.common.check_unique_task_names(tasks) · valjean.cambronne.common.collect_tasks(job_file, job_args, job_kwargs) · valjean.cambronne.common.build_graphs(args) · valjean.cambronne.common.read_env(*, root, names, filename, fmt) · valjean.cambronne.common.write_env(env, *, filename, fmt)
- `modules/cambronne/main.md` — **`main` — Main executable** (1 kB)
  - valjean.cambronne.main.main(argv=None) · valjean.cambronne.main.make_parser() · valjean.cambronne.main.process_options(args)
- `modules/cosette.md` — **cosette — COnStruction et ExécuTion de TâchEs** (1 kB)
- `modules/cosette/code.md` — **`code` — Tools for checking out and building code** (4 kB)
  - class valjean.cosette.code.CheckoutTask(name, *, repository, checkout_root=None, log_root=None, flags=None, ref=None, vcs='git', deps=None, soft_deps=None)  — bases: PythonTask · class valjean.cosette.code.BuildTask(name, source, *, build_root=None, log_root=None, targets=None, build_system='cmake', configure_flags=None, build_flags=None, deps=None, soft_deps=None)  — bases: PythonTask
- `modules/cosette/depgraph.md` — **`depgraph` — Dependency graphs** (11 kB)
  - Building · Querying · Merging, sorting and other operations · Grafting sub-graph nodes into the graph itself · Caveats · class valjean.cosette.depgraph.DepGraphError  — bases: Exception · class valjean.cosette.depgraph.DepGraph(nodes=None, edges=None)
- `modules/cosette/env.md` — **`env` — Environment for task execution** (5 kB)
  - class valjean.cosette.env.EnvError  — bases: Exception · class valjean.cosette.env.Env(dictionary=None)  — bases: MutableMapping
- `modules/cosette/pythontask.md` — **`pythontask` — Wrap Python code in a task** (8 kB)
  - PythonTask` objects · Passing arguments via the environment · Passing arguments via the environment: a more complex example · Passing arguments via the configuration · Module API · class valjean.cosette.pythontask.TaskException(reason='unknown')  — bases: Exception · class valjean.cosette.pythontask.PythonTask(name, func, *, args=None, kwargs=None, env_kwarg=None, config_kwarg=None, deps=None, soft_deps=None)  — bases: Task
- `modules/cosette/rlist.md` — **`rlist` — Reversible lists** (4 kB)
  - class valjean.cosette.rlist.RList(args=None, *, key=id)  — bases: MutableSequence
- `modules/cosette/run.md` — **`run` — Task for generic command execution** (12 kB)
  - Spawning external processes · Creating tasks using a factory · Caching · Module API · valjean.cosette.run.run(clis, stdout, stderr, **subprocess_args) · valjean.cosette.run.make_cap_paths(base_path) · class valjean.cosette.run.RunTask(name, clis_closure, *, deps=None, soft_deps=None, **subprocess_args)  — bases: PythonTask · class valjean.cosette.run.RunTaskFactory(make_closure, *, deps=None, soft_deps=None, name, **kwargs)
- `modules/cosette/scheduler.md` — **`scheduler` — Task scheduling and dependency handling** (4 kB)
  - class valjean.cosette.scheduler.SchedulerError  — bases: Exception · class valjean.cosette.scheduler.Scheduler(*, hard_graph, soft_graph=None, backend=None) · queue` — Producer-consumer-queue backend · class valjean.cosette.backends.queue.QueueScheduling(n_workers=10)
- `modules/cosette/task.md` — **`task` — Task specification** (2 kB)
  - class valjean.cosette.task.TaskError  — bases: Exception · class valjean.cosette.task.Task(name, *, deps=None, soft_deps=None)  — bases: ABC · class valjean.cosette.task.DelayTask(name, delay=1.0)  — bases: Task · valjean.cosette.task.det_hash(*args) · valjean.cosette.task.close_dependency_graph(tasks)
- `modules/cosette/use.md` — **`use` — Integrate Python functions in `DepGraph` objects** (20 kB)
  - An example · Use` objects are wrappers · Argument injection via the `using` decorator · Injecting multiple arguments · Keyword arguments · Modifying an existing `Use` decorator · Injecting arguments into tasks created by a `RunTaskFactory · Pipelines · Module API · valjean.cosette.use.from_env(*, env, task_name, key) … (+3)
- `modules/eponine.md` — **eponine — ExPloratiON et INtErfaçage** (1 kB)
- `modules/eponine/apollo3.md` — **`apollo3` – Data reading for Apollo3** (1 kB)
  - Main modules
- `modules/eponine/apollo3/hdf5_picker.md` — **`hdf5_picker` – Pick results in HDF5 from Apollo3** (6 kB)
  - Picking results with `Picker · Quick exploration with `Picker · class valjean.eponine.apollo3.hdf5_picker.Picker(fname, error_value=np.nan) · class valjean.eponine.apollo3.hdf5_picker.PickerException  — bases: Exception
- `modules/eponine/apollo3/hdf5_reader.md` — **`hdf5_reader` – Read an Apollo3 HDF5 and store the results** (13 kB)
  - Data models of Apollo3 HDF5 files · Use of `Reader · valjean.eponine.apollo3.hdf5_reader.hdf_to_browser(*args, **kwargs) · class valjean.eponine.apollo3.hdf5_reader.Reader(fname, error_value=np.nan) · valjean.eponine.apollo3.hdf5_reader.extract_geometry(geometry) · valjean.eponine.apollo3.hdf5_reader.extract_info(info) · valjean.eponine.apollo3.hdf5_reader.extract_standard_values(val, ngroups, error) · valjean.eponine.apollo3.hdf5_reader.extract_user_values(val, error) · valjean.eponine.apollo3.hdf5_reader.extract_localvalues(lnames, lvals, error) · valjean.eponine.apollo3.hdf5_reader.loop_over_std_values(lres, ngroups, error) … (+10)
- `modules/eponine/browser.md` — **`browser` – Indexing results stored as lists of dictionaries** (13 kB)
  - The `Index` class · The `Browser` class · Building the browser · Selection of a given items or of a list of items from content · Module API · class valjean.eponine.browser.Index()  — bases: Mapping · class valjean.eponine.browser.Browser(content, data_key='results', global_vars=None)  — bases: Container · class valjean.eponine.browser.TooManyItemsBrowserError  — bases: LookupError · class valjean.eponine.browser.NoItemBrowserError  — bases: LookupError
- `modules/eponine/dataset.md` — **`dataset` – Unified data format** (25 kB)
  - Dataset definition and initialisation · Squeezing a dataset · Operations available on Datasets · Addition and subtraction · Multiplication and division · Comparisons · Indexing and slicing · Getting a subset of the `Dataset · All dimensions have to be present in the slice · Masked datasets … (+3)
- `modules/eponine/tripoli4.md` — **`tripoli4` – Parsing for Tripoli-4** (2 kB)
  - Introduction · Main modules · More details on parsing
- `modules/eponine/tripoli4/common.md` — **`common` – Common methods to build numpy arrays from dictionaries and lists** (41 kB)
  - Goal · Spectrum and meshes · Generalities · Initialization · Filling arrays and bins · Result and use in the framework · Other available arrays · Green bands · Adjoint results · Nu and (Z,A) spectrum … (+40)
- `modules/eponine/tripoli4/data_convertor.md` — **`data_convertor` – Convert Tripoli-4 results to `Dataset`** (6 kB)
  - valjean.eponine.tripoli4.data_convertor.bins_reduction(def_bins, reduced_dims) · valjean.eponine.tripoli4.data_convertor.special_array(array, score, bins, array_key='array', name='', what='') · valjean.eponine.tripoli4.data_convertor.array_result(farray_res, res_type, name='', what='', array_key='array', score='score') · valjean.eponine.tripoli4.data_convertor.masked_array_result(farray_res, res_type, name='', what='', array_key='array', score='score') · valjean.eponine.tripoli4.data_convertor.integrated_result(result, res_type='integrated', name='', what='', score='score', sigma='sigma') · valjean.eponine.tripoli4.data_convertor.results_wo_error(result, res_type, name='', what='', score=None) · valjean.eponine.tripoli4.data_convertor.result_wo_error(result, res_type, name='', what='') · valjean.eponine.tripoli4.data_convertor.result_with_error(result, res_type, name='', what='', score='score', sigma='sigma') · valjean.eponine.tripoli4.data_convertor.unbinned_result(result, res_type, name='', what='', score=None, sigma=None) · valjean.eponine.tripoli4.data_convertor.nan_result(name='', what='') … (+1)
- `modules/eponine/tripoli4/depletion.md` — **`depletion` – Read Tripoli-4 depletion results** (6 kB)
  - valjean.eponine.tripoli4.depletion.title_to_snake_case(word) · valjean.eponine.tripoli4.depletion.generic_docstrings(res_type, *list_params) · valjean.eponine.tripoli4.depletion.add_accessors(dict_res) · class valjean.eponine.tripoli4.depletion.DepletionReader(mbr) · class valjean.eponine.tripoli4.depletion.DepletionReaderException  — bases: Exception
- `modules/eponine/tripoli4/grammar.md` — **`grammar` – Pyparsing grammar** (7 kB)
  - Generalitites · Organisation · Main parsers blocks · Response block, parser `response · Other parsers
- `modules/eponine/tripoli4/parse.md` — **`parse` – Parse Tripoli-4 outputs** (2 kB)
  - class valjean.eponine.tripoli4.parse.ParserException  — bases: Exception · class valjean.eponine.tripoli4.parse.Parser(jddname) · class valjean.eponine.tripoli4.parse.ParseResult(parse_res, scan_vars, name='')
- `modules/eponine/tripoli4/parse_debug.md` — **`parse_debug` – Debug parsing of Tripoli-4 outputs** (1 kB)
  - class valjean.eponine.tripoli4.parse_debug.ParserDebug(jddname, *, end_flag='', ofile='')  — bases: Parser
- `modules/eponine/tripoli4/scan.md` — **`scan` – Scan Tripoli-4 outputs and select relevant results** (7 kB)
  - Summary · Use of `scan · Caveats · Beginning and end of results sections · Module API · class valjean.eponine.tripoli4.scan.PhEmEpBalanceOutput() · class valjean.eponine.tripoli4.scan.HomogMatOutput() · class valjean.eponine.tripoli4.scan.BatchResultScanner(current_batch, para, line) · class valjean.eponine.tripoli4.scan.ScannerException  — bases: Exception · class valjean.eponine.tripoli4.scan.Scanner(fname, end_flag='')  — bases: Mapping
- `modules/eponine/tripoli4/transform.md` — **`transform` – Transform pyparsing result** (14 kB)
  - valjean.eponine.tripoli4.transform.compose2(f, g) · valjean.eponine.tripoli4.transform.compose(*fs) · valjean.eponine.tripoli4.transform.convert_spectrum(toks, spectrum_type) · valjean.eponine.tripoli4.transform.convert_mesh(toks) · valjean.eponine.tripoli4.transform.convert_green_bands(toks) · valjean.eponine.tripoli4.transform.convert_correspondence_table(toks) · valjean.eponine.tripoli4.transform.convert_scoring_zone_id(toks) · valjean.eponine.tripoli4.transform.convert_list_to_tuple(toks) · valjean.eponine.tripoli4.transform.convert_batch_numbers(score) · valjean.eponine.tripoli4.transform.convert_score(toks) … (+22)
- `modules/eponine/tripoli4/use.md` — **`use` – Inject parsing results into free functions** (9 kB)
  - Injecting the raw parse results · Using a `Browser · Module API · valjean.eponine.tripoli4.use.partial(func, *args, **kwargs) · valjean.eponine.tripoli4.use.make_parser(filename) · valjean.eponine.tripoli4.use.parse_batch_number(parser, *, batch_number) · valjean.eponine.tripoli4.use.parse_batch_index(parser, *, batch_index=-1) · valjean.eponine.tripoli4.use.using_parser(factory) · valjean.eponine.tripoli4.use.using_parse_result(factory, batch_number) · valjean.eponine.tripoli4.use.using_last_parse_result(factory) … (+3)
- `modules/gavroche.md` — **gavroche — Gestion AVancée de Routines et Oracles en CHaînE (nom temporaire)** (1 kB)
- `modules/gavroche/diagnostics.md` — **`diagnostics` – Diagnostic tests** (16 kB)
  - valjean.gavroche.diagnostics.stats.stats_worker(test_fn, name, description, tasks, **kwargs) · valjean.gavroche.diagnostics.stats.task_stats(*, name, description='', labels=None, tasks) · class valjean.gavroche.diagnostics.stats.NameFingerprint(name, fingerprint=None) · class valjean.gavroche.diagnostics.stats.TestStatsTasks(*, name, description='', labels=None, task_results)  — bases: Test · class valjean.gavroche.diagnostics.stats.TestResultStatsTasks(*, test, classify)  — bases: TestResult · class valjean.gavroche.diagnostics.stats.TestOutcome  — bases: Enum · valjean.gavroche.diagnostics.stats.test_stats(*, name, description='', labels=None, tasks) · class valjean.gavroche.diagnostics.stats.TestStatsTests(*, name, description='', labels=None, task_results)  — bases: Test · class valjean.gavroche.diagnostics.stats.TestResultStatsTests  — bases: TestResultStatsTasks · valjean.gavroche.diagnostics.stats.test_stats_by_labels(*, name, description='', labels=None, tasks, by_labels) … (+7)
- `modules/gavroche/eval_test_task.md` — **`eval_test_task` – One task to evaluate them all** (1 kB)
  - valjean.gavroche.eval_test_task.actually_eval_test(test) · class valjean.gavroche.eval_test_task.EvalTestTask(name, test_task_name, *, deps=None, soft_deps=None)  — bases: PythonTask · valjean.gavroche.eval_test_task.evaluate_tests(test_fn, name=None)
- `modules/gavroche/stat_tests.md` — **`stat_tests` – Statistical tests for datasets comparisons** (37 kB)
  - Modules · student` — Student's t-test · Test interpretation · Code implementation · Examples · class valjean.gavroche.stat_tests.student.TestResultStudent(test, tstud, pvalue=None)  — bases: TestResult · class valjean.gavroche.stat_tests.student.TestStudent(dsref, *datasets, name, description='', labels=None, alpha=0.01, ndf=None)  — bases: TestDataset · Statistical interpretation · Code implementation · Examples of the test … (+15)
- `modules/gavroche/test.md` — **`test` – Domain-specific language for writing tests** (4 kB)
  - class valjean.gavroche.test.CheckBinsException  — bases: Exception · valjean.gavroche.test.same_arrays(arr1, arr2) · valjean.gavroche.test.same_bins(bins1, bins2) · valjean.gavroche.test.same_bins_datasets(*datasets) · valjean.gavroche.test.check_bins(*datasets) · class valjean.gavroche.test.Test(*, name, description='', labels=None)  — bases: ABC · class valjean.gavroche.test.TestDataset(dsref, *datasets, name, description='', labels=None)  — bases: Test · class valjean.gavroche.test.TestResult(test)  — bases: ABC · class valjean.gavroche.test.TestResultFailed(test, msg)  — bases: TestResult · class valjean.gavroche.test.TestResultEqual(test, equal)  — bases: TestResult … (+3)
- `modules/javert.md` — **javert — Journal Automatique de VÉRificaTion** (1 kB)
- `modules/javert/formatter.md` — **`formatter` – Abstract class for formatters** (1 kB)
  - class valjean.javert.formatter.Formatter  — bases: ABC
- `modules/javert/mpl.md` — **`mpl` – Convert templates to plots** (19 kB)
  - Style setup · General style · Colors and markers · Legends · 2D plots · Customization · Strings as bins · Pie plot · Bar plots · Module API … (+3)
- `modules/javert/plot_repr.md` — **`plot_repr` – Transform test results into `PlotTemplate`** (11 kB)
  - valjean.javert.plot_repr.dimensions_from_array(array_shape) · valjean.javert.plot_repr.dimensions_and_bins(bins, array_shape) · valjean.javert.plot_repr.trim_range(bins, max_ratio=1000) · valjean.javert.plot_repr.fit_curve_ranges(curves, threshold=0.0) · valjean.javert.plot_repr.ranges_union(ranges, union_axis=0, minmax_axis=-1) · valjean.javert.plot_repr.curve_limits(curve, threshold=0.0) · valjean.javert.plot_repr.pad_range(limits, log, padding=0.05) · valjean.javert.plot_repr.post_treatment(templates, result) · valjean.javert.plot_repr.build_plot_template_with_dim(curves, axnames) · valjean.javert.plot_repr.repr_datasets_values(result) … (+15)
- `modules/javert/representation.md` — **`representation` – Transform test results into items** (7 kB)
  - class valjean.javert.representation.Representation(representer, verbosity=Verbosity.DEFAULT) · class valjean.javert.representation.Representer · class valjean.javert.representation.ExternalRepresenter · class valjean.javert.representation.TableRepresenter  — bases: Representer · class valjean.javert.representation.FullTableRepresenter  — bases: TableRepresenter · class valjean.javert.representation.PlotRepresenter(post='default')  — bases: Representer · class valjean.javert.representation.FullPlotRepresenter  — bases: PlotRepresenter · class valjean.javert.representation.EmptyRepresenter  — bases: Representer · class valjean.javert.representation.FullRepresenter(post=plot_repr.post_treatment)  — bases: Representer
- `modules/javert/rst.md` — **`rst` – Convert items to rst format** (14 kB)
  - class valjean.javert.rst.Rst(representation, *, n_workers=None) · class valjean.javert.rst.RstFormatter  — bases: Formatter · class valjean.javert.rst.RstTable(table, num_fmt='{:11.6g}') · class valjean.javert.rst.RstPlot(plot) · class valjean.javert.rst.RstText(text) · class valjean.javert.rst.FormattedRst(*, author, title, version, tree_dict, text_dict, plots, n_workers=None) · class valjean.javert.rst.RstTestReportTask(name, *, report_task, representation, author, version, deps=None, soft_deps=None)  — bases: PythonTask
- `modules/javert/table_repr.md` — **`table_repr` – Transform test results into `TableTemplate`** (12 kB)
  - valjean.javert.table_repr.repr_bins(dsref) · valjean.javert.table_repr.repr_testresultequal(result, verbosity=Verbosity.DEFAULT) · valjean.javert.table_repr.repr_equal_summary(result) · valjean.javert.table_repr.repr_equal(result) · valjean.javert.table_repr.repr_testresultapproxequal(result, verbosity=Verbosity.DEFAULT) · valjean.javert.table_repr.repr_approx_equal_summary(result) · valjean.javert.table_repr.repr_approx_equal(result) · valjean.javert.table_repr.repr_testresultstudent(result, verbosity=Verbosity.DEFAULT) · valjean.javert.table_repr.repr_student(result) · valjean.javert.table_repr.repr_student_silent(_result) … (+23)
- `modules/javert/templates.md` — **`templates` – Things that can be put in the report** (15 kB)
  - class valjean.javert.templates.TableTemplate(*columns, headers=None, units=None, highlights=None) · class valjean.javert.templates.CurveElements(values, bins, legend, *, index=0, errors=None) · class valjean.javert.templates.SubPlotAttributes(dim) · class valjean.javert.templates.SubPlotElementsException  — bases: Exception · class valjean.javert.templates.SubPlotElements(*, curves, axnames=('', ''), ptype='1D') · class valjean.javert.templates.PlotTemplate(*, subplots, small_subplots=True, suppress_xaxes=False, suppress_legends=False, backend_kw=None) · class valjean.javert.templates.TextTemplate(text) · valjean.javert.templates.join(*templates)
- `modules/javert/test_external.md` — **`test_external` – Class to import external test** (1 kB)
  - class valjean.javert.test_external.TestResultExternal  — bases: TestResult · class valjean.javert.test_external.TestExternal(*templates, name, description='', labels=None, success=True)  — bases: Test
- `modules/javert/test_report.md` — **`test_report` – Classes modelling a test report** (1 kB)
  - class valjean.javert.test_report.TestReport(*, title, text='', content=None) · class valjean.javert.test_report.TestReportTask(name, *, make_report, eval_tasks, kwargs=None)  — bases: PythonTask
- `modules/javert/verbosity.md` — **`verbosity` – Verbosity levels** (1 kB)
  - class valjean.javert.verbosity.Verbosity  — bases: Enum
- `modules/valjean.md` — **valjean — VALidation, Journal d'Évolution et ANalyse** (1 kB)
  - valjean.note(self, message, *args, **kwargs) · class valjean.ValjeanFormatter(fmt) · valjean.set_log_level(level) · valjean.get_logger(module) · valjean.set_logger_level(module, level=logging.INFO) · valjean.local_logger_level(module, level)
- `modules/valjean/chrono.md` — **`chrono` — A context manager to time code sections** (1 kB)
  - class valjean.chrono.Chrono()
- `modules/valjean/config.md` — **`config` — Configuration object** (1 kB)
  - Module API · class valjean.config.Config(dictionary=None)  — bases: MutableMapping
- `modules/valjean/dyn_import.md` — **`dyn_import` — Utilities for dynamically importing Python modules** (1 kB)
  - valjean.dyn_import.split_module_path(file_name) · valjean.dyn_import.dyn_import(file_name)
- `modules/valjean/path.md` — **`path` — Utilities for accessing the filesystem** (1 kB)
  - valjean.path.ensure(*paths, is_dir=False) · valjean.path.sanitize_filename(name)
