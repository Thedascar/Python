games = {'nome':[],'videogame':[],'ano':[]}
for i in range(0,1,1):
    nome = input('Qual nome: ')
    videogame = input('Qual videogame: ')
    ano = int(input('Qual ano: '))
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)

for i in games.values():
    print(i)