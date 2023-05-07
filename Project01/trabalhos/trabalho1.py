
# menu principal
print('Bem vindos a StorePy')
print('Prazer Sou Lucas Ramon Campos Assunção,seu Guia!!!')

# variaveis globais
resultado = 0
taxa = 0
pedido = 0

# entrada dos dados
valor_unidade = float(input('Digite o valor unitário do produto: '))
quantidade_produto = int(input('Digite a quantidade desejada: '))

# verificão e validação dos descontos
if quantidade_produto < 10:
    pedido = valor_unidade * quantidade_produto
    taxa = 0
    resultado = valor_unidade * quantidade_produto
elif quantidade_produto > 9 and quantidade_produto < 100:
    pedido = valor_unidade * quantidade_produto
    taxa = 0.05
    resultado = ((valor_unidade * quantidade_produto) * taxa) + pedido
elif quantidade_produto > 99 and quantidade_produto < 1000:
    pedido = valor_unidade * quantidade_produto
    taxa = 0.10
    resultado = ((valor_unidade * quantidade_produto) * taxa) + pedido
else:
    pedido = valor_unidade * quantidade_produto
    taxa = 0.15
    resultado = ((valor_unidade * quantidade_produto) * taxa) + pedido

# saida do console
print(f'O valor total do seu pedido é: {pedido:.2f}')  # usamos .2f para a quantidade de casas decimais após a virgula
print(f'Após o desconto de {taxa * 100:.0f} % seu produto custará: {resultado:.2f}')