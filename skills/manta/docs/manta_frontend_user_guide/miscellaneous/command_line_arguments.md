<!-- source: https://manta-project.gitlab.io/manta/manta_frontend_user_guide/miscellaneous/command_line_arguments.html -->

# Handling of command line arguments

This section is devoted to how command line arguments are handled by the
manta::init function and also describes the usage of some built-in
command line arguments.

## Treatment of command line arguments

Command line arguments begins by two minus signs `-`, as in
`--help`.

Shorthands for the most common command line arguments begins with one
minus sign, as in `-h` which is the shorthand for `--help`.

Some command line arguments require options, which are passed using the
following syntax:

```
--<argument_name>=<option>
```

If a shorthand is used, the following syntax is used to passed the option:

```
-<argument_short_hand> <option>
```

## Default command line arguments

Table 3 Main command line arguments

| Command line argument | Description |
| --- | --- |
| `--petsc-options` | specify options passed to `PETSc`, separated by commas. |
| `--petsc-options-file` | specify a file used to initialize `PETSc`. |
| `--floating-point-exceptions`, `-fpe` | handle trapping of floating point exceptions through SIGFPE  signals. |
| `--parameter` | specify a parameter on the command line. The option of the  command line argument must have the form key:value. This option  is interpreted as the following JSON file `{"key": value}`. Note  that a parameter specified using `--parameter` always overrides  the parameters defined in parameters files (see  `--parameters-file`), even if the parameters file is specified  after `--parameter`. Successive calls to `--parameter` with the  same key overwrite the parameter.  Another valid syntax is the form `key:value[index]`. ** `index` must  be a non-negative integer. Otherwise, the behavior is undefined.**. This  syntax is interpreted as acessing the n-th object (n being `index`  here) of the `value` json array. For instance, given the json file  `{"name": "arr": [0, 1 ,2]}`, the command line argument  `--parameter=name:arr[0]=9` overrides the first element of `arr` to  `9`, so that `arr` is now `[9, 1 ,2]`. **WARNING** Please read the  pitfall section associated with this option, below. |
| `--parameters-file` | specify a JSON input file that can be used to initialize the  computations. It results in parsing the given JSON file and  converts it to an instance of the Parameters class , which is  returned by the init function. Parameters can be overriden if  another parameter file is specified or if the parameter are  explicitly given using the --parameter command line argument.  Wether the content of the parameters file is used depends on the  executable. Some may use that information when others simply  discard it. |
| `--log-file` | specify the base name of the log files. A different log file will  be used for each MPI process. The MPI process number and the  extension '.log' are automatically appended to the given base  name. |
| `--version`, `-v` | display the version of Manta, the git hash of the source commit used  to build Manta, some build type information, and exits. |
| `--verbose-level` | set the verbose level. The following options are accepted:    - `quiet`: minimal outputs.  - `level0`: display only the main steps of the computation.  - `level1`: display information at the coupling scheme level.  - `level2`: display information at the model level.  - `level3`: display information at the iteration level.  - `debug`: display debuggin information. |
| `--help`, `-h` | display the list of supported command line arguments and exits. |

[Table 3](#tab-default-command-line-arguments) lists the default command line
arguments supported by defaults by executables built on top of MANTA.

Note

Executables based on MANTA can freely add support for other command
line arguments. The list of supported command line arguments and their
description is always given by `--help`.

## Pitfalls

### `--parameter`

When providing to the `--parameter` a key-value pair, with value
being a string, the `"` characters surrounding the value must
be escaped by the shell or the interpreter of the command.
For instance, on a `bash` interpreter, to associate the string `"file.txt"`
to the key `"filename"`,

```bash
./main --parameter=filename:'"file.txt"'
```

will be interpreted correctly.

Other quotings may **not** be interpreted correctly. For instantce:

```bash
./main --parameter=filename:"file.txt"
```

will result in a parsing error as the double-quotes are escaped. The dot
symbol in `file.txt` is then an invalid character.

### `--petsc-options-file`

If a `petscrc` file is present in the current directory, it is used
over whatever file path given with the `--petsc-options-file` command
line argument.
