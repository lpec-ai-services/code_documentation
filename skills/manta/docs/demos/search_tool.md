<!-- source: https://manta-project.gitlab.io/manta/demos/search_tool.html -->

# Using the search tool

## Introduction

A search tool is provided as part of the MANTA repository.
This is a command-line tool that allows the user to look for a particular test or example in the MANTA repository.

The actual script is named `search_tool.py` and is located at the root of the repository.
As a consequence, all the commands described in this document assume that the user is in a terminal session and that the current working directory is the root of the MANTA repository.

## Supported Python versions

The search tool is written in Python, but only relies on the standard library so that there is no package to install.
A minimum supported Python version has not been established precisely, but note that Python 3.8 is not supported because the tool uses some type hints features that have been introduced in Python 3.9.
This tool has been tested successfully with Python 3.9.5, so it should work on any subsequent minor release.

## Usage

### Getting some help

As for most command-line utilities, a help message can be obtained by running:

```shell
python search_tool.py --help
```

This should print a message similar to:

```text
usage: search_tool.py [-h] [--key KEYWORD [KEYWORD ...]] [--any] [--output OUTPUT] {list,check,add,rm,update} ...

A program to find examples and tests in the |manta| repo

optional arguments:
  -h, --help            show this help message and exit
  --key KEYWORD [KEYWORD ...], -k KEYWORD [KEYWORD ...]
                        one or more keywords to search for
  --any, -a             list files that match ANY given keyword (by default only files that match ALL the given keywords are listed)
  --output OUTPUT, -o OUTPUT
                        output matches into a text file

subcommands:
  {list,check,add,rm,update} <1>
```

① The list of available subcommands

The search tool provides a main command as well as some subcommands.
However, the only subcommand that users need to know is the `list` subcommand.

### The main command

The main command lists the examples and tests that match the given keyword(s).
These keywords are provided by using the `--key` option (short version: `-k`), either once or multiple times, i.e. this command:

```shell
python search_tool.py --key kw1 --key kw2
```

and this command:

```shell
python search_tool.py --key kw1 kw2
```

are equivalent.

In order to get a list of the available keywords, use the `list` subcommand (see [The list subcommand](#the-list-subcommand)).

By default, the search tool will look for the files that match **all** of the keywords provided.
The `--any` (short version: `-a`) flag can be added to instead look for the files that match **any** of the keywords provided.
This second option will thus yield more results.

### The `list` subcommand

To call the `list` subcommand, simply enter:

```shell
python search_tool.py list
```

in your terminal session.

This will list the keywords grouped by category and in alphabetical order.
Any number of these keywords can then be used to search for examples and tests.

A help message *specific to this command* can be obtained by passing the `--help` flag as follows:

```shell
python search_tool.py list --help
```

In this message, you will see that there are some available flags for the `list` subcommand.
The only one of interest for users is the `--description` (short version: `-d`) flag, which adds a description to the keywords when they are printed in the terminal.
Note that some keywords may not have an available description.
