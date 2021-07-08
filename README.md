## gpt-j
A Gpt-j api to use with python

# Parameters
context: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 2048 or less are recommended)

tempurature: controls the ramdomness of the model. higher values will be more random (suggestest to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

## Basic Usage

# In the prompt enter something you want to generate
```python
from Basic_api import SimpleCompletion

prompt = "def perfect_square(num):"
```



Note: There will be periods of the beggining of the response gpt-j doesn't have any stop tokens so this is all we can do for now...
