# GPT-J
A GPT-J API to use with python

## Installing gpt-j
```
pip install gptj
```

## Parameters
prompt: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 204 or less are recommended)

temperature: controls the randomness of the model. higher values will be more random (suggestest to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

top_k: Top k probability

rep: The likely hood of the model repeating the same tokens lower values are more repetative

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

## The maximum length of the output response
```python
max_length = 100
```

## Temperature controls the creativity of the model
A low temperature means the model will take less changes when completing a prompt

A high temperature will make the model more creative

Both temperature and top probability must be a float

```python
temperature = 0.09
```

## top probability is an alternative way to control the randomness of the model
If you are using top probability set temperature one

If you are using temperature set top probability to one

```python
top_probability = 1.0
```

## top k is an integer value that controls part of the model
```python
top_k = 40
```

## Repetition penalty will result in less repetative results
```python
repetition = 0.216
```

## Initializing the SimpleCompletion class
Here you set query equal to the desired values

Note values higher than 512 tend to take more time to generate

```python
query = simple_completion(prompt, length=max_length, temp=temperature, top_p=top_probability, top_k=top_k, rep=repetition)
```

## Finally run the function below
```python
print(query)
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

## Max tokens is the maximum length of the output response
```python
max_tokens = 50
```

## Temperature controls the randomness of the model
A low temperature means the model will take less changes when completing a prompt

A high temperature will make the model more creative and produce more random outputs

A Note both temperature and top probability must be a float

```python
temperature = 0.09
```

## Top probability is an alternative way to control the randomness of the model
If you are using it set temperature one

If you are using temperature set top probability to one

```python
top_probability = 1.0
```

## top k is an integer value that controls part of the model
```python
top_k = 40
```

## Repetition penalty will result in less repetative results
```python
repetition = 0.216
```

## Simply set all the give all the parameters
Unfilled parameters will be default values

I recommend all parameters are filled for better results

Once everything is done execute the code below

```python
response = context_setting.completion(prompt,
              user=User,
              bot=Bot,
              max_tokens=max_tokens,
              temperature=temperature,
              top_p=top_probability,
              top_k=top_k,
              rep=reptition)
```

## Last but not least print the response
Please be patient depending on the given parameters it will take longer sometimes

For quick responses just use the Basic API which is a simplified version

```python
print(response)
```

Note: This a very small model of 6B parameters and won't always produce accurate results

## Disclaimer

I have removed the security from the API, please don't use for unethical use!
I am not responsible for anything you do with the API

# License and copyright 

## Credit 
This is all possible thanks to https://github.com/vicgalle/gpt-j-api

Feel free to check out the original API

## License
© Michael D Arana

licensed under the [MIT License](LICENSE).
