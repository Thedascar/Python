


def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1 ,1):
        fat *= i
    return fat

x = int(input('Digite um valor inteiro: '))
print(f'O fatorial de {x} é {fatorial(x)}')