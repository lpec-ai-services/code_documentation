# `ICoCoExceptions.hxx`


## class `WrongContext`

```cpp
class WrongContext : public std::exception
```

Exception raised when an ICoCo method is called at the wrong place.

This exception is raised whenver an ICoCo method is called when it shouldn't.
This is for example the case if the Problem::initTimeStep() method is called when
Problem::initialize() hasn't been called yet.


### `WrongContext`

```cpp
WrongContext(const std::string& prob, const std::string& method, const std::string& precondition);
```

Constructor.


- **prob**: problem name

- **method**: name of the method where the exception occurred

- **precondition**: detail of the condition that wasn't met


### `~WrongContext`

```cpp
~WrongContext() throw();
```

Destructor


### `what`

```cpp
virtual const char* what() const throw();
```

Gets the exception message.

**Returns:** the exception full message.


## class `WrongArgument`

```cpp
class WrongArgument : public std::exception
```

Exception raised when an ICoCo method is called with an invalid argument.

This exception is raised whenver an ICoCo method is called with inappropriate arguments.
This is for example the case if the Problem::getOutputField() is called with a non-existing field
name.


### `WrongArgument`

```cpp
WrongArgument(const std::string& prob, const std::string& method, const std::string& arg, const std::string& condition);
```

Constructor.


- **prob**: problem name

- **method**: name of the method where the exception occurred

- **arg**: name of the faulty argument

- **condition**: detail of the condition that wasn't met


### `~WrongArgument`

```cpp
~WrongArgument() throw();
```

Destructor


### `what`

```cpp
virtual const char* what() const throw();
```

Gets the exception message.

**Returns:** the exception full message.


## class `NotImplemented`

```cpp
class NotImplemented : public std::exception
```

Exception raised when one tries to call an ICoCo method which is not implemented.

By default all ICoCo methods raise this exception. The code implementing the norm
should derive the Problem class and override (at least partially) this default
implementation.


### `NotImplemented`

```cpp
NotImplemented(const std::string& prob, const std::string& method);
```

Constructor.


- **prob**: problem name

- **method**: name of the method where the exception occurred


### `~NotImplemented`

```cpp
~NotImplemented() throw();
```

Destructor


### `what`

```cpp
virtual const char* what() const throw();
```

Gets the exception message.

**Returns:** the exception full message.
