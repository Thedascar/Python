game = {'nome':'Gow4',
     'desenvolvedora':'Santa Monica',
     'ano': 2018}

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())


for i in game.values():
    print('value_com for: ',i)


print(game.keys())

for i in game.keys():
    print('key_com for: ',i)

print(game.items())

for i,j in game.items():
    print(f'{i} = {j}')