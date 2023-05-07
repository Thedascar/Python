# apresentação da loja
print('Bem Vindos a Lanchonete ' +
      'do Lucas Ramon Campos Assunção')

# cardápio
print('--------------------MENU--------------------|')
print('Código|     Descrição         | Valor(R$)   |')
print('  100 |     Dog-Simples       |   R$ 9,00   |')
print('  101 |     Dog-Duplo         |   R$ 11,00  |')
print('  102 |     X-Egg             |   R$ 12,00  |')
print('  103 |     X-Salada          |   R$ 13,00  |')
print('  104 |     X-Bacon           |   R$ 14,00  |')
print('  105 |     X-Tudo            |   R$ 17,00  |')
print('  200 |     Refrigerante Lata |   R$ 5,00   |')
print('  201 |     Chá Gelado        |   R$ 4,00   |')

# variáveis globais
lanche = ''
valor = 0
total_pedido = 0
soma_total = 0

# Tela de seleção dos pedidos
while True:  # loop para repetição indefinida
    # validação dos pedidos
    pedido = int(input('Escolha o seu pedido: '))
    if pedido < 100 or pedido > 201:  # validação das opções de pedido,se estiver correto ele continua
        print('Pedido Inválido')
        continue
    elif pedido == 100:
        valor = 9.00
        lanche = 'Dog-Simples'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 101:
        valor = 11.00
        lanche = 'Dog-Duplo'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 102:
        valor = 12.00
        lanche = 'X-Egg'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 103:
        valor = 13.00
        lanche = 'X-Salada'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 104:
        valor = 14.00
        lanche = 'X-Bacon'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 105:
        valor = 17.00
        lanche = 'X-Tudo'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    elif pedido == 200:
        valor = 5.00
        lanche = 'Refrigerante Lata'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')
    else:
        valor = 4.00
        lanche = 'Chá Gelado'
        print(f'Você pediu um {lanche} com valor de R$ {valor:.2f}')

        # contadores
    total_pedido += 1
    soma_total += valor

    # Validação da tela para adicionar mais produtos
    print('Você deseja pedir mais alguma coisa ?')
    print('1 - Sim')
    print('0 - Não')
    mais_pedido = int(input('Digite a sua opção: '))
    if mais_pedido > -1 and mais_pedido < 2:  # validação de deseja continuar ou não
        if mais_pedido == 1:
            continue  # volta para menu de seleção
        else:
            break

        # saida do console
print(f'Você fez {total_pedido} pedidos')
print(f'O total do seu pedido foi: R$ {soma_total:.2f}')