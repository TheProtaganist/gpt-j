import requests


def generate(context, token_max_length, temperature, top_p, top_k, rep):
    assert isinstance(token_max_length, int), "Max token most be integer value"
    assert isinstance(temperature, float), "temperature most be float value"
    assert isinstance(top_p, float), "top_p most be float value"
    assert isinstance(top_k, int), "top_k most be integer value"
    assert isinstance(rep, float), "rep most be float value"
    payload = {"text": str(context), "length": token_max_length, "temperature": temperature, "topP": top_p, "topK": top_k, "rep": rep}
    URL = requests.post("https://playground-api.forefront.link/", json=payload)
    result = URL.json()
    return result["result"][0]["completion"]
