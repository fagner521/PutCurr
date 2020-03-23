import requests as rq

"""""""""
As Pesuisas do google devem ser feitas por GET incluindo a pesquisa nos parametros q=(termo)&oq=(termo).
Creio que por ser GET tenha de ser transfomada em URL antes de ser feita a requisição.

https://www.google.com/search?q=(Termo)&oq=(Termo)
"""""""""

class Pesquisa():
    def teste_internet(self):
        requisicao = rq.get("https://google.com/")
        codigo = requisicao.status_code
        if codigo == 443:
            print("Voce precisa usar a internet.")
            quit()
    teste_internet("teste")
    def search(self):
        self = str(self).replace(" ", "+")
        requisicao = rq.get('https://www.google.com/search?q=' + self + '&oq=' + self)
        print(requisicao.text)


Pesquisa.search('Chola azul')