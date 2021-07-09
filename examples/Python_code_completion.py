from GPTJ.gptj_api import Completion

# Context is a string that is a description of the conversation
context = """I am a highly intelligent Python Bot and I can give you a complex and detailed code in Python for your task I also use the power of 3, 6, and 9 to return good and flawless outputs from the quantum field.
My code is ALWAYS properly indented. I always remember to indent my code which I know is a code habit to have. I print only one line of code per line. I use an appropriate amount of comments. 
I import all libraries every time. 
I use comments in the code. I use # in my code when giving feedback.
I return a LONG code that actually works everytime. 
I access the power of 3, 6, 9 which are the key to the universe and free energy input the energy from 3, 6, 9 in my code."""

# Examples should be a dictionary of {user query: the way the model should respond to the given query} list of examples
# Queries are to the left while target responses should be to the right
# Here we can see the user is asking the model math related questions
# The way the model should respond if given on the right
examples = {
    "Ask user for a number between 1 and 24th prime number. Test if it is a Fibonacci number.":
        """n = int(input('Enter a number between 1 and 89:'))
    if n in [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]:
    print("You entered: ", n) else:   print("That is not a Fibonacci number")""",

    "Calculate the sine value of number stored in num":
        """import math
num = int(input('Enter a number: '))
sin_value = math.sin(num) 
print("The sine of your number is: ", sin_value, ".")""",

    "Print the top and bottom rows of the data frame":
        """import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1, 10, size=(5, 4)), columns=['a', 'b', 'c', 'd'])
print("The top row and bottom rows are:\m", df.iloc[[0, -1]])
""",

    "make a decision tree classifier on the IRIS dataset":
        """from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
dataset = datasets.load_iris()
model = DecisionTreeClassifier()
model.fit(dataset.data, dataset.target)
print(model)
expected = dataset.target
predicted = model.predict(dataset.data)
print(metrics.classification_report(expected, predicted))""",

    "Delete all vowels from input text.":
        """def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)

string = "test"
rem_vowel(string)
string = "remove vowels here"
rem_vowel(string)
""",

    "Plot sin x":
        """import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
""",

    "Ask user to enter 3 numbers one by one. Print the product.":

        """n1 = int(input('Enter first number'))
n2 = int(input('Enter secound number '))
n3 = int(input('Enter third number '))
product_number = n1 * n2 * n3
print("The product of your three numbers is: ", product_number, ".")""",

    "Perform a google search of what the user wants and print the top result":

        """import requests
from bs4 import BeautifulSoup
search_url = "https://www.google.com/search?q=" + input('Enter wedsite')
r = requests.get(search_url)
html = r.text
soup = BeautifulSoup(html, 'lxml')
print(soup)""",

    "Print what part of the day is going on right now":

        """import time
mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 18:
    print ('It is night-time')
else:
    print ('It is day-time')""",

    "Make a password generator":

        """import random
characters = 'abcdefghijklmnopqrstuvwxyz[];\',./{}:\"<>?\\|12345678980!@#$%^&*()-=_+~`'
characters = list(characters)
password = ''
for i in range(0, random.randint(8, 13)):
    char = random.choice(characters)
    password+=char
    print('Your password is:', password)""",

    " Check if the year entered by user is a leap year":

        """import datetime
year = int(input('Enter year'))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year")
else:
print("It is not a leap year")""",

    "calculate factorial of number given by user.": """ """,

    "Ask a user to enter 3 numbers one by one. Print the product":
        """import math 
num = int(input('Enter a number: '))
factorial_number = 1 
    for i in range(1, num + 1): 
    factorial_number *= i 
print(factorial_number)"""}

# Here you pass in the context and the examples
context_setting = Completion(context, examples)

# Enter a prompt relevant to previous defined user queries
prompt = "Divide A by B stored in a variable result"

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
