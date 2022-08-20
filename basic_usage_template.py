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

# top_k is the number of top responses to return
# This is the number of responses the model will return
top_k = 1

# Rep is the number of times the model will repeat itself
# This is the number of times the model will repeat itself when generating a response
rep = 1.0

# Here you set query equal to the desired values
# Note values higher that 512 tend to take more time to generate
res = simple_completion(prompt, length=Max, temp=temperature, top_p=top_probability, top_k=k, rep=rep)

# Finally we print the result
print(res)
