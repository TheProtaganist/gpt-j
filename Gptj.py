import requests


def generate(context, token_max_length, temperature, top_p):
    assert isinstance(token_max_length, int), "Max token most be integer value"
    assert isinstance(temperature, float), "temperature most be float value"
    assert isinstance(top_p, float), "top_p most be float value"
    payload = {"context": str(context), "token_max_length": token_max_length, "temperature": temperature, "top_p": top_p}
    URL = requests.post("http://api.vicgalle.net:5000/generate", params=payload)
    text = URL.json()
    return str(text["text"])
