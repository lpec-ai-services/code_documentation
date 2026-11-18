<!-- source: modules/javert/formatter.rst -->

# `formatter` – Abstract class for formatters

This module contains the `Formatter` abstract base class. All other formatters must derive from it.

### `class valjean.javert.formatter.Formatter  — bases: ABC`

Abstract base class for any formatter.

#### `Formatter.header(self, name, depth)`

Format a section header.

#### `Formatter.text(self, text)`

Format some text.

#### `Formatter.template(self, item)`

Convert an item to the relevant format.
