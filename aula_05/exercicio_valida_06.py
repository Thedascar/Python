def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

print('Digite um valor de 0 a 10 !!!!!!')
x = valida_int('Digite um valor inteiro: ',0,10)

print(f'Você digitou {x}, good bye....')