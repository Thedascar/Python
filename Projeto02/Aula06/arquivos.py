arq = open("Projeto02/Aula06/arquivos/arquivo1.txt","r") # r = read
type(arq)
print(arq.read())
print(arq.tell())
print(arq.seek(0,0))
print(arq.read(23))

arq2 = open("Projeto02/Aula06/arquivos/arquivo2.txt","w") # w = write
arq2.write("Python e vida")
arq2.close()
arq2 = open("Projeto02/Aula06/arquivos/arquivo2.txt","r")
print(arq2.read())


arq2 = open("Projeto02/Aula06/arquivos/arquivo2.txt","a") # a = append acrescentar
arq2.write(" Uma linguagem facil de aprende e muito legal")
arq2.close()
arq2 = open("Projeto02/Aula06/arquivos/arquivo2.txt","r")
print(arq2.read())

