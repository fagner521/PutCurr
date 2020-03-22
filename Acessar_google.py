import requests

requisicao = requests.get("https://www.google.com/")
print(requisicao.text)