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
        contador = 0
        global urls
        global sitesarquivo
        sitesarquivo = open('sitesarquivo.txt', 'w')
        urls = []
        while contador < 50:
            requisicao = rq.get('https://www.google.com/search?q=' + self + '&start=' + str(contador))
            global page
            contador = contador + 10
            print(contador)
            page = requisicao.text
            #print(requisicao.text)
            def url_lists(page):
                start = str(page).find('"/url?q=')


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
                global sites
                sites = ' \n'.join(urls[:length-1])






            url_lists(page)
        print(sites)


        sitesarquivo.write(sites)
        sitesarquivo.close()
        arquivoindese = open('arquivoindesejado.txt')
        sitesarquivo = open('sitesarquivo.txt','r')
        sitesarquivol = [sitesarquivo]
        print(sitesarquivol)


'''''''''''
        try:
            numerador = 0
            while 1 == 1 :
                site = sitesarquivo.readlines()[numerador]
                indesejado = arquivo1.readlines()[numerador]
                boloeano = indesejado in site
                print()
                if boloeano == True:
                    sitesarquivo = open('sitesarquivo.txt', 'w')
                    sitesarquivo.writelines()[numerador] = "Limpo---------------------------------------------------\n"
                    sitesarquivo.close()
                else:
                    continue
        except:
            print("Ok")
'''''''''''

