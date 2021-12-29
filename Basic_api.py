import requests
from .Gptj import generate


def simple_completion(prompt, length, temp, top=1.0):
    try:
        Prompt = str(prompt)
        assert isinstance(temp, float), "temperature most be float value"
        assert isinstance(top, float), "top_p most be float value"
        if Prompt != "":
            return generate(Prompt, length, temperature=temp, top_p=top).strip()
        else:
            return "Empty Prompt detected"
    except requests.HTTPError:
        print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")
