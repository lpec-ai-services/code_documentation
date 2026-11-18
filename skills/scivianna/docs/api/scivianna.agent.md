<!-- source: api/scivianna.agent.rst -->

# scivianna.agent package

# Scivianna Agent Module

The `agent` module provides AI/LLM integration capabilities for Scivianna, enabling intelligent data manipulation and visualization assistance.

## Files

| File | Description |
|------|-------------|
| `__init__.py` | Package initialization file |
| `data_2d_worker.py` | Worker module for handling 2D data operations in agent context |
| `instructions.md` | Prompt instructions and examples for LLM agent interaction |
| `llm_model.py` | LLM model integration for AI-assisted visualization |

## Purpose

This module enables users to interact with Scivianna using natural language. The LLM agent can:

- Modify cell colors based on user requests
- Adjust transparency/alpha values to highlight or dim areas
- Filter and manipulate data based on value conditions
- Generate Python code to transform visualization properties

## Usage Example

```python
from scivianna.agent.data_2d_worker import LLMModel
from scivianna.data.data2d import Data2D

data_2d: Data2D = ...
# Create agent with access to 2D data
agent = Data2DWorker(data_2d)

# Request natural language transformations
agent("Color in red the highest value cell")
agent("Hide zeros, highlight highest values, dim the rest")
```

## Key Features

- **Data2D Access**: Agent has programmatic access to cell values, colors, and alpha channels
- **Code Generation**: Generates executable Python code snippets for data manipulation
- **NumPy Integration**: Full NumPy support for array operations
- **Instruction Templates**: Pre-defined instruction patterns for common tasks Submodules ----------

## scivianna.agent.data_2d_worker module

LLM agent worker that generates and tests code operating on a Data2D.

### `scivianna.agent.data_2d_worker.extract_python_code(text)`

Extract the content of a python code block from an LLM response.

### `class scivianna.agent.data_2d_worker.Data2DWorker(data2d: Data2D)  — bases: Data2DWorker`

Worker that receives a Data2D object and works with it.

#### `Data2DWorker.extract_exectute_code(self, text: str) -> str`

Extract the last execute_code call from an agent trace

## Parameters

text : str  
LLM return text

## Returns

str  
Generated code

#### `Data2DWorker.execute_code(self, code_to_execute: str)`

Applies a code string to the current object. Used to repeat an already processed prompt.

## Parameters

code_to_execute : str  
Code to execute in the Data2DWorker scivianna.agent.llm_model module ---------------------------------

This file contains the variables used to call the LLM:

- LLM_MODEL_ID: Identifier for the specific large language model being used.
- LLM_API_BASE: Base URL endpoint for the LLM's API service.
- LLM_API_KEY: Authentication key used to access the LLM API, required for authorization and usage tracking.

This file can be overwriten to hard write the values.

### `scivianna.agent.llm_model.get_env_variable(var_name: str) -> str`

Retrieves an environment variable with error if it does not exist.

## Parameters

var_name : str  
Name of the environment variable

## Returns

str  
Value of the environment variable or default value

## Raises

ValueError  
If the variable is missing

### `scivianna.agent.llm_model.call_llm(prompt: str, instructions: str) -> str`

Sends a request to the server model to get a piece of code that responds to the prompt considering the instructions.

## Parameters

prompt : str  
User defined need

instructions : str  
Instructions for the LLM

## Returns

str  
Code returned by the server Module contents ---------------

LLM agent tools for Scivianna.

Subpackage providing an LLM-driven worker that can modify a Data2D object based on natural-language instructions (requires the "agent" extra).
