# USING COMMENTS AND INSERTING FILES
<!-- source PDF pages 45-46 -->

<!-- page 45 -->
Chapter 6
USING COMMENTS AND INSERTING FILES

## 6.1 COMMENTS

In the TRIPOLI-4® code, there are now three syntaxes for comments.
Comments can be placed inside any command, subject to the following limitations.

### 6.1.1 COMMENTS USING COMMENT

Comments can be inserted using the old syntax:
COMMENT
Comment
COMMENT
It is not possible to have nested comments using this type of comment alone.

### 6.1.2 C TYPE COMMENTS

Comments can also be added by placing them between /* and */. This new syntax makes it possible to nest comments within a
comment.
Example:
/* First comment
* -------------------
/*
* Nested comment
*/
End of first comment
*/
This can be used to comment a part of a set of data containing comments (this part can include all possible types of comments).

<!-- page 46 -->
### 6.1.3 C++ TYPE COMMENTS

Finally, it is possible to insert a line of characters preceded by //. This type of comment can be added at the end of a line, the rest
of which is then ignored in the execution of the code.
Example:
DATA
// Comment

### 6.1.4 RESTRICTIONS

Whatever syntax is used, the comment must precede a keyword (or name of a composition, grid etc.). This is because it is only at
the time when the keywords are decoded that the comments are eliminated. In a geometry command, the comments must be given
after the title.
If the keyword KEYWORD is to be followed by a number (for instance the volume), the syntax
// Read expected keyword
KEYWORD 1
is correct, whereas
KEYWORD // Read number expected
1
is not.

## 6.2 INSERTING FILES

It is possible to insert one (or more) commands using:
FILE
name(file)
where name(file) is the name of the file (and possibly its path, e.g. /home/user/T4/Data) that contains the part of the data-set to
be inserted.
It is not possible to insert part of a command.
It is thus possible to load a geometry derived from another code (in a suitable format), a list of compositions derived from PEPIN,
etc.
It is worth noting that, when using the keyword FILE, only the line of insertion will be copied in the output file, which can be a
solution of memory sparing in case of numerous lines (e.g. for the geometry definition).
