loja = {'cenoura':[100,0.99],
        'brócolis':[50,3.99],
        'batata':[200,0.49],
        'cebola':[75,1.10]
}
pedido = []
while True:
    item_nome = input('Digite o nome do item que deseja comprar: ')
    item_qtd = int(input('Deseja comprar quantos: '))
    pedido.append([item_nome,item_qtd])
    res = input('Deseja adicionar outro item[S:N]: ')
    if res in 'Nn':
        break
total = 0
print('\nVendas')
for item in pedido:
    produto = item[0]
    qtd = item[1]
    preco = loja[produto][1]
    valor_produto = preco * qtd
    print(f'{produto}: {qtd} x {preco} = {valor_produto}')
    loja[produto][0] -= qtd
    total += valor_produto
print(f'Custo total: {total}\n')
print('Estoque')
for i,j in loja.items():
    print('Descrição: ',i)
    print('Quantidade: ',j[0])
    print(f'Preço: {j[1]}\n')
print(loja.items())
