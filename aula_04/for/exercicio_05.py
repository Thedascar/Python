soma = 0
cont = 0
for i in range(1,101):
    if i % 2 == 0:
        soma += i
        cont += 1
res = soma / cont
print(res)