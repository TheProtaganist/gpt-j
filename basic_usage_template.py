from gpt_j.Basic_api import simple_completion
# In the prompt enter something you want to generate
prompt = "def perfect_square(num):"

# Max length of completion 
Max = 200

# Temperature controls the creativity of the model
# A low temperature means the model will take less changes when completing a prompt 
# A high temperature will make the model more creative
# Both temperature and top probability must be a float

temperature = 0.6

# top probability is an alternative way to control the randomness of the model
top_probability = 1.0

# Here you set query equal to the desired values
# Note values higher that 512 tend to take more time to generate
res = simple_completion(prompt, length=Max, temp=temperature, top=top_probability, top_k=k)

# Finally we print the result
print(res)
