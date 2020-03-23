from sys import argv as arg

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

print("-n Nome Completo\n -d Cidade \n -p profissão\n -c Telefone \n -q Email\n -b Arquivo")
argumentos = arg[1:]
print(argumentos)
index_nome = argumentos.index("-n") +1
nome = []
numerador = 0
for palavra in argumentos[index_nome:]:
    numerador = numerador + 1
    print(numerador)
    bolean = "-" in palavra
    if bolean == True:
        print('Saindo')
        break
    else:
        print("listado")
        nome.append(str(palavra))

print(nome)
quit()


'''''''''
while (nome_completo != "-d")
    index_nome = argumentos.index("-n") + 1
    nome_completo = argumentos[index_nome]
    print(nome_completo)
Cidade = argumentos.index("-d") + 1
print(Cidade)
'''''''''
