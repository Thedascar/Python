cadastro = {'nome':[],'sexo':[],'ano':[]}
mulheres_menos_30 = []
homes_acima_media = []
total_cadastros = 0
soma_idade = 0
media = 0
while True:
    terminar = input('Você deseja fazer mais um cadastro [S/N]: ')
    if terminar in 'Nn':
        break
    if terminar not in 'Ss':
        print('Digite S para SIM ou N para NÃO')
        continue
    nome = input('Qual seu nome: ')
    sexo = input('Qual seu sexo[M/F]: ')
    ano = int(input('Qual seu ano de nascimento: '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo)
    cadastro['ano'].append(ano)
    total_cadastros += 1
    idade = 2023 - ano
    soma_idade += idade
    media = soma_idade/total_cadastros

    if sexo.lower() == 'f' and ano > 1993:
        mulheres_menos_30.append([nome,sexo,ano])
    elif sexo == 'm' and idade > media:
        homes_acima_media.append([nome, sexo, ano])




print('Mulheres menos 30: ',mulheres_menos_30)
print('Homens Acima da média: ',homes_acima_media)
print('A média das idades é: ',media)