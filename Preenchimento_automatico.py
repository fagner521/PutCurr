import requests
import pycurl

index_sitesarquivos = 0
sitesarquivos = open("sitesarquivo.txt", "r").readlines()
siteslista = []
numerador = 0

for contador in sitesarquivos:
    siteslista.append(str(contador))
    acessartexto = requests.get(contador, verify=False)
    print(acessartexto)
    print(contador)
    quit()


