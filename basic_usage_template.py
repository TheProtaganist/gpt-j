from gptj.Basic_api import SimpleCompletion
# In the prompt enter something you want to generate
prompt = "def perfect_square(num):"

# The maximum lenght of the output response
max_length = 100

# Temperature controls the creativity of the model
# A low temperature means the model will take less changes when completing a prompt
# A high temperature will make the model more creative
# Both temperature and top probability most be a float
temperature = 1.0

# top probability is an alternative way to control the randomness of the model
# If you are using top probability set temperature one
# If you are using temperature set top probability to one
top_probability = 0.6

# Initializing the SimpleCompletion class
# Here you set query equal to the desired values
# Note values higher that 512 tend to take more time to generate
query = SimpleCompletion(prompt, length=max_length, t=temperature, top=top_probability)

# Finally you assign a variable the function simple completion
query.simple_completion()
