valor = 0
cont = 0
soma = 0
while True:
    valor = int(input('Digite um valor inteiro maior que zero : '))
    if valor < 0 :
        continue
    if not valor:
        break
    soma += valor
    cont += 1

media = soma/cont
print(media)