mochila = ('machado','camisa','bacon','abacate')
print(mochila)

print("Indexando os dados da lista")
print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])

print('Usando for para manipular a lista')

for item in mochila:
    print(f'Na minha mochila tem: {item}')

print('Adicionado mais arquivos a lista')
upgrade = ('queijo','canivete')

grande_mochila = mochila + upgrade
grande_mochila_invertida = upgrade + mochila
print(grande_mochila)
print(f'Grande mochila invertida {grande_mochila_invertida}')