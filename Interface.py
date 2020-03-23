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

print("-n Nome Completo\n -c Cidade \n -p profissão\n -t Telefone \n -e Email\n -a Arquivo")
argumentos = arg[1:]
print(argumentos)
index_nome = argumentos.index("-n") +1
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


index_profissão = argumentos.index("-p") + 1
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


index_telefone = argumentos.index("-t") + 1
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


index_email = argumentos.index("-e") + 1
email =  argumentos[index_email]
print("A email é : "  +  email)

index_arquivo = argumentos.index("-a") + 1
arquivo =  argumentos[index_arquivo]
print("A arquivo é : "  +  arquivo)


termo = '2019..2020 -vagaemprego.com.br -vagas.com -linkedin -folhape -jooble -noticias -noticia -indeed' \
        ' -infojobs -faculdade -matricula -trabalhabrasil -universidade -aprenda ' + cidade + ' "' + profissão + '"' + \
        ' currículo OR curriculum OR contrato OR contratamos OR contato "Trabalhe Conosco"'
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
Cidade = argumentos.index("-d") + 1
print(Cidade)
'''''''''
