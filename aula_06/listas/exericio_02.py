def buscaSequencial(lista,dado):
    x = 0
    while x < len(lista):
        if lista[x] == dado:
            return x
        x += 1
    return -1

teste = [1,2,3,78,6,8,9,3]
dado = int(input('Digite um valor inteiro: '))
res = buscaSequencial(teste,dado)
if res >= 0:
    print(f'Posição onde o {dado} foi encontrado {res + 1}')
else:
    print('cade')