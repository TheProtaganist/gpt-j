# GPT-J
A Gpt-j api to use with python

## Parameters
context: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 2048 or less are recommended)

tempurature: controls the ramdomness of the model. higher values will be more random (suggestest to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

# Basic Usage

## In the prompt enter something you want to generate

```python
from Basic_api import SimpleCompletion

prompt = "def perfect_square(num):"
```

## The maximum lenght of the output response
```python
max_length = 100
```

## Temperature controls the creativity of the model

A low temperature means the model will take less changes when completing a prompt
A high temperature will make the model more creative
Both temperature and top probability most be a float

```python
temperature = 0.09
```

## top probability is an alternative way to control the randomness of the model
If you are using top probability set temperature one
If you are using temperature set top probability to one

```python
top_probability = 1.0
```

## Initializing the SimpleCompletion class
Here you set query equal to the desired values
Note values higher that 512 tend to take more time to generate

```python
query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)
```

## Finally run the function below

```python
query.simple_completion()
```

## optional
You can assign the results to a string
```python
Query = query.simple_completion()

print(Query)
```

Note: This a a very small model of 6B paramters and won't always produce accurate results
