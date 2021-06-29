# gpt-j
A Gpt-j api to use with python

# Parameters
context: the prompt you wish to give to the model

tokens: the number of tokens to generate (values 2048 or less are recommended)

tempurature: controls the ramdomness of the model. higher values will be more random (suggestest to keep under 1.0 or less, something like 0.3 works)

top_p: top probability will use the most likely tokens

# Usage
```python
from gptj import GPTJ

g = GPTJ()

sample_dialog = """user: Hi
bot: Hi how are you?
user: I'm doing well
bot: Just wondering about life
user: that's nice
bot: yeah
user: Cya
bot: Have a nice day"""

text = input("Enter text: ")

response = g.generate(f"{sample_dialog}. user: {text}", 100, 0.3, 0.6)
answer = response.replace("bot: ", "")
list_of_char = answer.split('user: ', 1)
answer2 = list_of_char[0]
answer3 = answer2.split("\n")
final_answer = "".join(answer3) 
print(final_answer)
```
Note: There will be periods of the beggining of the response gpt-j doesn't have any stop tokens so this is all we can do for now...
