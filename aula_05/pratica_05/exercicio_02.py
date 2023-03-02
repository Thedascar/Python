def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


print('#--------------------#')
print('|  Menu de Cadastro  |')
print('|--------------------|')
print('|Meus Games Favorites|')
print('#--------------------#')



arquivo = 'games.txt'

while True:
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1,3)
    if op == 1:
        print('Cadastrar game')
    elif op == 2:
        print('Listar Games')
    elif op == 3:
        print('Sair')
        break
