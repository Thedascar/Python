# função para medir o volume
def dimensoesObjeto():
    while True:
        try:  # try usado para tratar uma exceção para não permitir digitar os dados inválidos
            altura = float(input('Digite a altura do objeto (cm): '))
            comprimeto = float(input('Digite o comprimento do objeto (cm): '))
            largura = float(input('Digite a largura do objeto (cm): '))
            volume = altura * largura * comprimeto
            print(f'Volume em (cm³) : {volume:.2f}')
            if volume < 1000:
                return 10
            elif volume >= 1000 and volume < 10000:
                return 20
            elif volume >= 10000 and volume < 30000:
                return 30
            elif volume >= 30000 and volume < 100000:
                return 50
            else:
                print('Acima da dimensão permitida !!!!')
        except ValueError:  # final do tratamento com uma mensagem e volta para o menu do while infinito
            print('Apenas números são aceitos')

        # funcao para receber o multiplicador de peso


def pesoObjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto (KG): '))
            if peso < 0.1:
                return 1
            elif peso >= 0.1 and peso < 1:
                return 1.5
            elif peso >= 1 and peso < 10:
                return 2
            elif peso >= 10 and peso < 30:
                return 3
            else:
                print('Acima do peso permitido !!!!')
        except ValueError:
            print('Apenas números são aceitos')

        # função para o multiplicador de rota


def rotaObjeto():
    while True:
        try:
            print('RS - De Rio de Janeiro até São Paulo \n' +
                  'SR - De Sã Paulo até Rio de Janeiro \n' +
                  'BS - De Brasília até São Paulo \n' +
                  'SB - De São Paulo até Brasília \n' +
                  'BR - De Brasília até Rio De Janeiro \n' +
                  'RB - De Rio De Janeiro até Brasília')

            rota = input('Digite a rota desejada: ')
            rota = rota.upper()
            if rota == 'RS' or rota == 'SR':
                return 1
            elif rota == 'BS' or rota == 'SB':
                return 1.2
            elif rota == 'BR' or rota == 'RB':
                return 1.5
            else:
                print('Rota Inexistente')
        except ValueError:
            print('Apenas as siglas são aceitas')

        # presentação da empresa


print('Bem vindo a empresa de logistica Lucas Ramon Campos Assunção')
# variaveis globais que recebem as funções
dimensao_valor = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensao_valor * peso * rota
# saida para o console
print(f'(Dimensão: {dimensao_valor}) * (Peso: {peso}) * (Rota: {rota})')
print(f'Valor total: R${total:.2f}')




