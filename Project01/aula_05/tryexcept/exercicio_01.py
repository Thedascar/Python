while True:
    try:
        x = int(input('Digite un número inteiro: '))
        break
    except ValueError:
        print('Número inválido')
