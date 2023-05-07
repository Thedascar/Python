mochila2 = ['Machado','Camisa','Bacon','Abacate']
print(f'Lista: {mochila2}')

x = mochila2[:] # Utilizamos [:] para fazer uma cópia por valor e não referência!!!!

x.remove('Machado')

print('Original: ',mochila2)
print('Cópia Alterada: ',x)