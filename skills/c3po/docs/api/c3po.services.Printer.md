<!-- source: c3po/services/Printer.py -->

# `c3po.services.Printer`

Contain the class Printer.

### `class c3po.services.Printer.Printer(printLevel)  — bases: object`

INTERNAL.

`Printer` writes strings in the standard output.

#### `Printer.setPrintLevel(self, level)`

Set the print level (0: None, 1: written lines are overwritten by the following ones, 2: usual printing).

## Parameters

level : int  
Integer in range \[0;2\].

#### `Printer.getPrintLevel(self)`

Return the print level previously set.

## Returns

int  
The print level.

#### `Printer.print(self, toPrint, tmplevel=None)`

Write the provided string in standard output.

## Parameters

toPrint : str  
String to print.

tmplevel : int  
Printing level to apply to this printing only.

#### `Printer.reprint(self, tmplevel=None)`

Rewrite the last printed string in standard output.

## Parameters

tmplevel : int  
Printing level to apply to this printing only.

### `c3po.services.Printer.warning(message)`

Write a warning message.

## Parameters

message : str  
Message of the warning.
