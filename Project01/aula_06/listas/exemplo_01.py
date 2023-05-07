
mochila1 = ('Machado','Camisa','Bacon','Abacate')
print(f'Tupla: {mochila1}')

mochila2 = ['Machado','Camisa','Bacon','Abacate']
print(f'Lista: {mochila2}')

mochila2[1] = 'Cachorro'
print(f'Lista_Modificada: {mochila2}')

mochila2.append('Ovos')
print(f'Lista_Append: {mochila2}')

mochila2.insert(0,'Bob')
print(f'Lista_Insert: {mochila2}')

del mochila2[0]
print(f'Lista_Del: {mochila2}')

mochila2.remove('Ovos')
print(f'Lista_Remove: {mochila2}')
