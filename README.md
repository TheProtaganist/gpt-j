# GPT-J
A GPT-J API to use with python

## Installing gpt-j
```
pip install gptj
```

## Parameters
prompt: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 2048 or less are recommended)

temperature: controls the randomness of the model. higher values will be more random (suggested to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

## Advanced Parameters 
user: the speaker the person who is giving gpt-j a prompt 

bot: an imaginary character of your choice

context: the part of the prompt that explains what is happening in the dialog

examples: a dictionary of user intentions and how the bot should respond


# Basic Usage

## In the prompt enter something you want to generate
```python
from gpt_j.Basic_api import simple_completion

prompt = "def perfect_square(num):"
```

##  Top k 0-D variable
```python
k = 40
```

## Temperature controls the creativity of the model
A low temperature means the model will take less changes when completing a prompt

A high temperature will make the model more creative

Both temperature and top probability must be a float

```python
temperature = 0.101
```

## top probability is an alternative way to control the randomness of the model
If you are using top probability set temperature one

If you are using temperature set top probability to one

```python
top_probability = 0.53
```

## Run the function below
Note: values higher than 512 tend to take more time to generate

```python
res = simple_completion(prompt, temp=temperature, top=top_probability, top_k=k)
print(res)
```

# Advanced Usage 

## Context is a string that is a description of the conversation
```python
from gpt_j.gptj_api import Completion

context = "This is a calculator bot that will answer basic math questions"
```


## Examples should be a dictionary of {user query: the way the model should respond to the given query} list of examples
Queries are to the left while target responses should be to the right

Here we can see the user is asking the model math related questions

The way the model should respond if given on the right

DO NOT USE PERIODS AT THE END OF USER EXAMPLE! 

```python
examples = {
    "5 + 5": "10",
    "6 - 2": "4",
    "4 * 15": "60",
    "10 / 5": "2",
    "144 / 24": "6",
    "7 + 1": "8"}
```

## Here you pass in the context and the examples
```python
context_setting = Completion(context, examples)
```

## Enter a prompt relevant to previous defined user queries
```python
prompt = "48 / 6"
```

## Pick a name relevant to what you are doing

Below you can change student to "Task" for example and get similar results
```python
User = "Student"
```
## Name your imaginary friend anything you want

```python
Bot = "Calculator"
```

## 0-D tensor used to find top k largest entries for the last dimension
```python
K = 40
```

## Temperature controls the randomness of the model
A low temperature means the model will take less changes when completing a prompt

A high temperature will make the model more creative and produce more random outputs

A Note both temperature and top probability must be a float

```python
temperature = 0.101
```

## Top probability is an alternative way to control the randomness of the model
If you are using it set temperature 0.0001

If you are using temperature set top probability to 1.0

```python
top_probability = 1.0
```

## seed is used to reproduce same guarantee result for the model (default = 0)
```python
seed = 0
```

## stream is true by default, leave as true if unsure
```python
stream = True
```

## Simply set all the give all the parameters
Unfilled parameters will be default values

I recommend all parameters are filled for better results

Once everything is done execute the code below

```python
response = context_setting.completion(prompt,
              user=User,
              bot=Bot,
              temperature=temperature,
              top_p=top_probability,
              top_k=K,
              stream=stream)
```

## Last but not least print the response
Please be patient depending on the given parameters it will take longer sometimes

For quick responses just use the Basic API which is a simplified version

```python
print(response)
```

Note: This a very small model of 6B parameters and won't always produce accurate results

Note: Starting from version 3.0.0 and up the max tokens setting has been removed since the api is using a domain to generate text which fixes the 20 queries per 30 minutes issue

# License and copyright 

## Credit 
This is all possible thanks to https://github.com/vicgalle/gpt-j-api

Feel free to check out the original API

## License
© Michael D Arana

licensed under the [MIT License](LICENSE).
