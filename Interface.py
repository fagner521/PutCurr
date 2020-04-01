from sys import argv as arg
from Acessar_google import Pesquisa

# Nome
# Completo
# Telefone
# Email
# Curriculo
# Profissão
# Cidade
# Todos
# os
# empregos
# da
# área? sim
# ou
# não
# se
# sim - sem
# filto
# se
# não - com
# filtro
# filtro = afsafasf

"""""""""

2019..2020 -vagaemprego.com.br -vagas.com -linkedin -folhape -jooble -noticias -noticia -indeed -infojobs -faculdade -matricula -trabalhabrasil -universidade -aprenda (cidade) "profissao" currículo OR curriculum OR contrato OR contratamos OR contato "Trabalhe Conosco"

"""""""""
"""""""""
arquivoindese = open('arquivoindesejado.txt', 'r')
arquivoindese = arquivoindese.readlines()
sitesarquivo = open('sitesarquivo.txt','r')
sitesarquivo = sitesarquivo.readlines()

for urlarq in sitesarquivo:
    for termoindese in arquivoindese:
        condicionador = termoindese in urlarq
        print(termoindese)
        if condicionador == True:
            retirado = sitesarquivo.pop(sitesarquivo.index(urlarq))
            print("%s \nFiltrei %s" % (termoindese, retirado))
        else:
            continue

quit()
"""""""""
argumentos = arg[1:]
print(argumentos)
try:
    index_nome = argumentos.index("-n") +1
except:
    print(
        "Essa é uma ferramenta que pesquisa, na internet, oportunidades de trabalho, filtrando sites de vaga de emprego \nque intermedia a comunicação com a empresa. Esta ferramenta visa possibilitar uma comunicação direta com o contratante\n \nPara tal:\n  Insira: -n Nome Completo\n  Insira: -c Cidade\n  Insira: -p Profissão\n  Insira: -t Telefone \n  Insira: -e Email\n  Insira: -a Arquivo")
    quit()
nome = []
numerador = 0
for palavra in argumentos[index_nome:]:
    numerador = numerador + 1

    bolean = "-" in palavra
    if bolean == True:

        break
    else:

        nome.append(str(palavra))

numerador = 0



termos = {}
#limpeza do nome logo a baixo
nome = ' '.join(nome)
termos["-n"] = nome
print("O nome completo é : " + termos["-n"])

try:
    index_nome = argumentos.index("-c") +1
except:
    print("Insira: -n e logo depois 'seu nome', -c e logo depois 'sua cidade'")
    quit()

index_cidade = argumentos.index("-c") + 1
cidade = []
for palavra1 in argumentos[index_cidade:]:
    numerador = numerador + 1

    bolean = "-" in palavra1
    if bolean == True:

        break
    else:

        cidade.append(str(palavra1))

numerador = 0
cidade = ' '.join(cidade)
termos["-c"] = cidade


print("A cidade é : "  +  str(cidade))

try:
    index_profissão = argumentos.index("-p") +1
except:
    print("Insira: -n e logo depois 'seu nome', -c e logo depois 'sua cidade', -p e logo depois 'sua profissão'")
    quit()

profissão = []
for palavra2 in argumentos[index_profissão:]:
    numerador = numerador + 1

    bolean = "-" in palavra2
    if bolean == True:

        break
    else:

        profissão.append(str(palavra2))

numerador = 0
profissão = ' '.join(profissão)
termos["-p"] = profissão


print("A profissão é : "  +  str(profissão))

try:
    index_telefone = argumentos.index("-t") +1
except:
    print("Insira: -n e logo depois 'seu nome', -c e logo depois 'sua cidade', -p e logo depois 'sua profissão', e logo depois 'seu telefone'")
    quit()

telefone = []
for palavra3 in argumentos[index_telefone:]:
    numerador = numerador + 1
    bolean = "-" in palavra3
    if bolean == True:

        break
    else:

        telefone.append(str(palavra3))



numerador = 0
telefone = ' '.join(telefone)
termos["-t"] = telefone


print("A telefone é : "  +  str(telefone))

try:
    index_email = argumentos.index("-e") +1
except:
    print("Insira: -n e logo depois 'seu nome', -c e logo depois 'sua cidade', -p e logo depois 'sua profissão', -t e logo depois 'seu telefone', -e e logo depois 'seu email")
    quit()


email =  argumentos[index_email]
print("A email é : "  +  email)

index_arquivo = argumentos.index("-a") + 1
arquivo =  argumentos[index_arquivo]
print("O arquivo é : "  +  arquivo)


termo = '-gov.br -vagas.com -catho -neuvoo -empregos.com.br -careerjet -trovit -glassdoor -jooble -jobbydoo -blogs -curso' \
        ' -revista -noticias -indeed -infojobs  -matricula -trabalhabrasil -universidade' + cidade + ' ' + profissão + \
        ' "currículo OR curriculum OR contato OR contratamos OR "Trabalhe Conosco""'
print(termo)

Pesquisa.search(termo)

#>>>>>>> Branch-testes
quit()


'''''''''
while (nome_completo != "-d")
    index_nome = argumentos.index("-n") + 1 + contador
    nome_completo = argumentos[index_nome] + 1 + contador
    print(nome_completo[])
    contador  = contador + 1
Cidade = argumentos.index("-d") + 1Interface.py -n fagner -p  -c recife -t 123123 -e fagner@ -a .cms
print(Cidade)
'''''''''
