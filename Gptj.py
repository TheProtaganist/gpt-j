import json
import requests


def generate(prompt, temperature, top_p, top_k=40, seed=0, stream=True):
    words = prompt.split(" ")
    assert isinstance(temperature, float), "temperature most be float value"
    assert temperature > 0.1, "temperature must be greater than 0.1"
    assert temperature <= 10.0, "temperature must be less than 10.0"
    assert isinstance(top_p, float), "top_p most be float value"
    assert top_p > 0.0, "top_p must be greater than 0.0"
    assert top_p <= 1.0, "top_p must be less than or equal to 1.0"
    assert isinstance(top_k, int), "top_k most be integer value"
    assert top_k >= 1, "top_k must be greater than or equal to 1"
    assert top_k <= 1000, "top_k must be less than or equal to 1000"
    assert isinstance(seed, int), "seed most be integer value"
    assert seed >= 0, "seed must be greater than or equal to 0"
    assert seed <= 1215752191, "seed must be less than or equal to 1215752191"
    assert isinstance(stream, bool), "stream most be boolean value"
    assert len(words) <= 2048, "prompt must be less than or equal to 2048 words"
    payload = {"prompt": str(prompt), "temperature": temperature, "top_p": top_p, "top_k": top_k, "seed": seed, "stream": stream}
    URL = requests.post("https://bellard.org/textsynth/api/v1/engines/gptj_6B/completions", json=payload)
    text = URL.text

    format_the_text = text.split("\n\n")
    if format_the_text[-1] == '':
        del format_the_text[-1]
    else:
        format_the_text = format_the_text

    create_text = []
    for line in format_the_text:
        json_line = json.loads(line)
        text = json_line["text"]
        create_text.append(text)

    initial_response = "".join(create_text)
    response = initial_response.replace("\n\n", "\n")
    return response.strip()
