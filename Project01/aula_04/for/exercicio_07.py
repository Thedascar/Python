idade = int(input('Digite a sua idade: '))
while idade > 0:
    sexo = input('Qual o seu sexo (M) ou (F): ')
    if sexo == 'F' or sexo == 'f':
        print(f'Boa noite, Senhora sua idade é {idade}')
    elif sexo == 'M' or sexo == 'm':
        print(f'Boa noite, Senhor sua idade é {idade}')
    else:
        print('Sexo inválido')
    idade = int(input('Digite a sua idade: '))

print('Software encerrado !!!!')