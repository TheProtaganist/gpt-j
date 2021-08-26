import requests
from .security import check_for_insults
from .Gptj import generate

class SimpleCompletion:

    def __init__(self, prompt, length=200, t=0.09, top=1.0):
        self.basic_prompt = str(prompt)
        self.L = length
        self.T = t
        self.probability = top
        self.complete = ""
        self.given_prompt = ""
        self.value = ""
        def simple_completion(user_input, length_max, temp, p):
            try:
                behavior = check_for_user_conduct = check_for_insults(user_input)
                assert isinstance(length_max, int), "Max token most be integer value"
                assert isinstance(temp, float), "temperature most be float value"
                assert isinstance(p, float), "top_p most be float value"
                if behavior == "":
                    completion = generate(prompt, length, t, top)
                    return completion
                else:
                    simple_result = ""
                    simple_result += check_for_user_conduct
                    return simple_result
            except requests.HTTPError:
                print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")
        def return_value():
            Complete = simple_completion(self.basic_prompt, self.L, self.T, self.probability)
            return Complete
        self.given_prompt = return_value()
    def simple_completion(self):
        print(self.given_prompt)
        return self.given_prompt