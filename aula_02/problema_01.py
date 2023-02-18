preco = int(input('Qual preço do produto: '))
desconto = int(input('Qual percentual de desconto: '))

d = preco * (desconto / 100)
valor_final = preco - d
print('O desconto foi de {} e o valor final é de {}'.format(d,valor_final))