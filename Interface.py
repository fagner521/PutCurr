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
Nome_Completo = argumentos.index("-n") + 1
print(Nome_Completo)
Cidade = argumentos.index("-d") + 1
print(Cidade)

