
def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x

def intervalo(inicio,fim):
    soma = 0
    while inicio <= fim:
        soma += inicio
        inicio += 1
    return soma

inicio = valida_int('Digite um valor inteiro entre (0-10): ',0,10)
fim = valida_int('Digite um valor inteiro entre (0-10): ',0,10)
print(f'A somato entre {inicio} e {fim} é : {intervalo(inicio,fim)}')