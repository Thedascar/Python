game = {}
games = []


for i in range(0,1  ,1):
    game['nome'] = input('Digite nome do seu game: ')
    game['videogame'] = input('Digite o videogame: ')
    game['ano'] = int(input('Ano de criação: '))
    games.append(game.copy())
print(games)

for e in games:
    for i,j in e.items():
        print(f'Campo {i} tem valor {j}')