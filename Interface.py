from sys import argv as arg

print("-n Nome\n -d Aquivo\n -p profissão\n")
argumentos = arg[1:]
print(argumentos)
profissao = argumentos.index("-p") + 1
<<<<<<< HEAD
print(argumentos[profissao])

nome = sys.argv[2]
print(nome)
=======
print(argumentos[profissao])
>>>>>>> f888ac8... Sys e menu basico
