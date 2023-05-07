while True:
    texto = input('Digite seu nome: ')
    if texto != 'Lucas':
        continue
    senha = input('Digite sua senha: ')
    if senha == 'Ramon':
        break
print('Login Feito com Sucesso')