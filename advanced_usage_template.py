from GPTJ.gptj_api import Completion

# Context is a string that is a description of the conversation
context = "This is a calculator bot that will answer basic math questions"

# Examples should be a dictionary of {user query: the way the model should respond to the given query} list of examples
# Queries are to the left while target responses should be to the right
# Here we can see the user is asking the model math related questions
# The way the model should respond if given on the right
examples = {
    "5 + 5": "10",
    "6 - 2": "4",
    "4 * 15": "60",
    "10 / 5": "2",
    "144 / 24": "6",
    "7 + 1": "8"}

# Here you pass in the context and the examples
context_setting = Completion(context, examples)

# Enter a prompt relevant to previous defined user queries
prompt = "48 / 6"

# Pick a name relevant to what you are doing
# Below you can change student to "Task" for example and get similar results
User = "Student"

# Name your imaginary friend anything you want
Bot = "Calculator"

# Max tokens is the maximum length of the output response
max_tokens = 40

# Temperature controls the randomness of the model
# A low temperature means the model will take less changes when completing a prompt
# A high temperature will make the model more creative and produce more random outputs
# Note both temperature and top probability most be a float
temperature = 0.09

# Top probability is an alternative way to control the randomness of the model
# If you are using it set temperature one
# If you are using temperature set top probability to one
top_probability = 1.0

# Set simply set all the give all the parameters
# Unfilled parameters will be default values
# I recommend all parameters are filled for better results
# Once everything is done execute the the code below
response = context_setting.completion(prompt,
                                      user=User,
                                      bot=Bot,
                                      max_tokens=max_tokens,
                                      temperature=temperature,
                                      top_p=top_probability)

# Last but not least print the response
# Please be patient depending the given parameters it will take longer sometimes
# For quick responses just use the Basic API which is a simplified version
print(response)
