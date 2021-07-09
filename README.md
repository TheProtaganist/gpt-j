# GPT-J
A Gpt-j api to use with python

## Installing gpt-j
```
pip install gptj
```

## Parameters
prompt: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 2048 or less are recommended)

tempurature: controls the ramdomness of the model. higher values will be more random (suggestest to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

## Advanced Parameters 
user: the speaker the person who is giving gpt-j a prompt 

bot: an imaginary character of your choice

context: the part of the prompt that explains what is happening in the dialog

examples: a dictionary of user intentions and how the bot should respond


# Basic Usage

## In the prompt enter something you want to generate
```python
from Basic_api import SimpleCompletion

prompt = "def perfect_square(num):"
```

## The maximum lenght of the output response
```python
max_lenght = 100
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
query = SimpleCompletion(prompt, lenght=max_lenght, t=temperature, top=top_probability)
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

# Advanced Usage 

## Context is a string that is a description of the conversation
```python
context = "This is a calculator bot that will answer basic math questions"
```

## Examples should be a dictionary of {user query: the way the model should respond to the given query} list of examples
Queries are to the left while target responses should be to the right
Here we can see the user is asking the model math related questions
The way the model should respond if given on the right

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

## Max tokens is the maximum lenght of the output response
```python
max_tokens = 50
```

## Temperature controls the randomness of the model
A low temperature means the model will take less changes when completing a prompt
A high temperature will make the model more creative and produce more random outputs
A Note both temperature and top probability most be a float

```python
temperature = 0.09
```

## Top probability is an alternative way to control the randomness of the model
If you are using it set temperature one
If you are using temperature set top probability to one

```python
top_probability = 1.0
```

## Set simply set all the give all the parameters
Unfilled parameters will be default values
I recommend all parameters are filled for better results
Once everything is done execute the the code below

```python
response = context_setting.completion(prompt,
              user=User,
              bot=Bot,
              max_tokens=max_tokens,
              temperature=temperature,
              top_p=top_probability)
```

## Last but not least print the response
Please be patient depending the given parameters it will take longer sometimes
For quick responses just use the Basic API which is a simplified version

```python
print(response)
```

Note: This a very small model of 6B paramters and won't always produce accurate results

## License and copyright 
© Michael D Arana

licensed under the [MIT License](LICENSE).
