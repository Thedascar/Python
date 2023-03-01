def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat


x = valida_int('Digite um valor inteiro: ', 0, 10)
print(f'O fatorial de {x} é {fatorial(x)}')
