def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x
def fatorial(num):

    """
    Aqui podemos criar um help para as funções !!!!
    :param num: asasas
    :return: alksjajs
    """
    fat = 1
    for i in range(1,num + 1,1):
        fat *= i
    return fat


res = valida_int('Digite um número inteiro de 1 - 10: ',1,10)
print(f'o fatorial de {res}! é {fatorial(res)}')
help(fatorial)