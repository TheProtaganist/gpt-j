import requests
from .Gptj import generate


def simple_completion(prompt, length, temp=0.3, top_p=1.0, top_k=40, rep=0.216):
    try:
        Prompt = str(prompt)
        assert length < 205, "Length must be less than 205"
        assert isinstance(temp, float), "temperature most be float value"
        assert isinstance(top_p, float), "top_p most be float value"
        assert isinstance(top_k, int), "top_k most be integer value"
        assert isinstance(rep, float), "rep most be float value"
        return generate(Prompt, length, temperature=temp, top_p=top_p, top_k=top_k, rep=rep).strip() if Prompt else "Empty Prompt detected"

    except requests.HTTPError:
        print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, 
        and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")
