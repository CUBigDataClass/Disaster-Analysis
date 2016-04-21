import requests

payload = {'text':'New Delhi','demonyms': 'false'}
r = requests.post("http://cliff.mediameter.org/process", data=payload)
print(r.text)
