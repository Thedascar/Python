try:
    print('Média de Notas')
    print('Digite -1 para sair ;)')
    Listanotas = []
    nota = float(input('Digite a sua nota: '))
    while nota > 0:
        Listanotas.append(nota)
        nota = float(input('Digite a sua nota: '))
    soma = 0
    for i in Listanotas:
        soma += i
    media = soma/len(Listanotas)

    print(f'Notas: {Listanotas}')
    print(f'Sua média foi de: {media}')
except ZeroDivisionError:
    print('Divisão por zero não é permitido')
finally:
    print('Acabou')




