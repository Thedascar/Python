# variavel e lista global
lista_de_pecas = []
codigo = 1


# funcao cadastrar
def cadastrarPeca(codigo):
    print('Menu de Cadastro')
    print(f'Código do Produto: {codigo}')
    nome = input('Nome da Peça: ')
    fabricante = input('Fabricante da Peça: ')
    valor = float(input('Valor da Peça R$: '))
    dicionario_peca = {'Código': codigo,  # adicionando os valores dentro do dicionário com key and value
                       'Nome': nome,
                       'Fabricante': fabricante,
                       'Valor': valor
                       }
    lista_de_pecas.append(dicionario_peca.copy())  # adicionando dicionário dentro de uma lista


# funcao consultar
def consultarPeca():
    print('Menu Consulta')
    while True:
        try:  # tratamento de exeções
            menu_consulta = int(input('1- Consultar todas as Peça\n' +
                                      '2- Consultar peça por código\n' +
                                      '3- Consultar peça por fabricante\n' +
                                      '4 -Retornar\n' +
                                      'Digite a sua opção: '))
            if menu_consulta == 1:
                print('Consultar todas as peças')
                for pecas in lista_de_pecas:  # uso de for para percorrer a lista e o dicionário
                    for chave, valor in pecas.items():
                        print(f'{chave} : {valor}')

            elif menu_consulta == 2:
                print('Consultar peça por código')
                codigo_produto = int(input('Digite o código do produto: '))
                for pecas in lista_de_pecas:
                    if codigo_produto == pecas['Código']:
                        for chave, valor in pecas.items():
                            print(f'{chave} : {valor}')


            elif menu_consulta == 3:
                print('Consultar por fabricante')
                fabricante_produto = input('Digite a fabricante do produto: ')
                for pecas in lista_de_pecas:
                    if fabricante_produto == pecas['Fabricante']:
                        for chave, valor in pecas.items():
                            print(f'{chave} : {valor}')
            else:
                return  # caso seja opção 4 retorna para o menu principal
        except ValueError:
            print('Valores Inválidos')

        # funcao remover


def removerPeca():
    print('Menu Remover Produto')
    codigo_remover = int(input('Digite o código do produto: '))
    for peca in lista_de_pecas:
        if codigo_remover == peca['Código']:
            lista_de_pecas.remove(peca)  # remove a peça por código
            print('Produto Removido')

        # apresentação da empresa


print('Seja Bem Vindo a Bicicletaria')
print('Sou Lucas Ramon Campos Assunção')

while True:
    try:
        menu = int(input('1- Cadastrar Peça\n' +
                         '2- Consultar Peça\n' +
                         '3- Remover Peça\n' +
                         '4- Sair\n' +
                         'Digite a sua opção: '))
        if menu > 0 and menu < 5:
            if menu == 1:
                cadastrarPeca(codigo)
                codigo = codigo + 1
            elif menu == 2:
                consultarPeca()
            elif menu == 3:
                removerPeca()
            else:
                print('Saindo')
                break
    except ValueError:
        print('Valores Inválidos')