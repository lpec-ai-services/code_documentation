<!-- source: https://docs.salome-platform.org/latest/gui/ADAO/en/notations.html -->

# 17. Notations and common conventions

In all this documentation, we use standard notations of linear algebra, data
assimilation (as described in [[Ide97]](bibliography.md#ide97)) and optimization.

For algebraic formulations, **vectors** are written horizontally or vertically
without making a difference. **Matrices** can be written either normally as a
serie of number series, either in text condensed notation, consisting in the
use of a space to separate the values, and a “`;`” to separate the rows of
the matrix, in a continuous line.

**Files** can be indicated by an absolute or relative path. For some old or
shared file systems, the full name, including the path, must not contain more
than 256 characters. In the case of Python files, it is advisable not to use
dots in the name apart for the extension, to prevent difficulties in using it
that are then complicated to diagnose.

**File type and naming conventions** rely heavily on the extensions of the
files themselves. Some of them are briefly specified here, without being
exhaustive:

- extension `.py` : data or commands text file of Python type
- extension `.comm` : commands text file of ADAO EFICAS type
- extension `.xml` : data text file of XML type or commands (for YACS, not exclusive)
- extension `.txt` : data text file with space separator
- extension `.dat` : data text file with space separator
- extension `.csv` : data text file with comma or semicolon separator
- extension `.tsv` : data text file with tab separator
- extension `.npy` : data binary file of type Numpy mono-variable
- extension `.npz` : data binary file of type Numpy multi-variables
- extension `.sdf` : data binary file of type Scientific Data Format

For the use of some of these files, one can refer to the keyword “*DataFile*”
as [Pseudo-types of digital data description](ref_entry_types.md#section-ref-entry-types-info).

Bibliographical references:

- [[Asch16]](bibliography.md#asch16)
- [[Bouttier99]](bibliography.md#bouttier99)
- [[Ide97]](bibliography.md#ide97)
- [[WikipediaMO]](bibliography.md#wikipediamo)
