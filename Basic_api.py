import requests
from .security import check_for_insults
from .Gptj import generate


def simple_completion(prompt, temp, top=1.0, top_k=40):
    try:
        behavior = check_for_user_conduct = check_for_insults(prompt)
        assert isinstance(temp, float), "temperature most be float value"
        assert isinstance(top, float), "top_p most be float value"
        assert isinstance(top_k, int), "top_k most be integer value"
        if behavior == "":
            return generate(prompt, temperature=temp, top_p=top, top_k=top_k)
        simple_result = ""
        simple_result += check_for_user_conduct
        return simple_result
    except requests.HTTPError:
        print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")

