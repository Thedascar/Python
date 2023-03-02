i = 0
while True:
    try:
        nome = input('Digite seu nome: ')
        num = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Nome inválido')
    except IndexError:
        print('Número inválido')
    finally:
        print(f'Tentativa: {i}')
        i += 1