from sys import argv as arg

print("-n Nome\n -d Aquivo\n -p profissão\n")
argumentos = arg[1:]
print(argumentos)
profissao = argumentos.index("-p") + 1
print(argumentos[profissao])

