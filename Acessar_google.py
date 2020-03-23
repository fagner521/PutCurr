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
        global page
        page = requisicao.text
        #print(requisicao.text)
        def url_lists(page):
            start = str(page).find('"/url?q=')
            global urls
            urls = []
            while start != -1:
                start = str(page).find('"/url?q=')
                #print(start)
                fim = str(page)[start:].find('">')
                #print(fim)
                url = str(page)[start + 8:start + fim]
                urlfim = url.find("&amp;")
                url = url[:urlfim]
                page = page[fim:]
                verificacao = url in urls
                if verificacao == False:
                    verific = "google.com" in url
                    if verific == False:
                        urls.append(url)
                    else:
                        continue
                else:
                    continue
            length = len(urls)
            print(' \n'.join(urls[:length-1]))
            quit()
        url_lists(page)

