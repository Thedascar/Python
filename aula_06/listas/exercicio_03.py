pessoa = []
imc = lambda peso,altura:peso/(altura * altura)
total_cadastros = 1
while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))
    x = imc(peso,altura)
    pessoa.append([nome,peso,altura,x])
    res = input('Para sair digite N.')
    if res in 'nN':
        break
    else:
        total_cadastros += 1
print(f'Pessoas Cadastradas: {pessoa}')
print(f'Quantidade de pessoas cadastradas: {total_cadastros}')

maior = 0
menor = 99
cont = 0
for i in range(0,len(pessoa),1):
    if pessoa[i][3] > maior:
        maior = pessoa[i][3]
        pessoa1 = pessoa[i]
    if pessoa[i][3] < menor:
        menor = pessoa[i][3]
        pessoa2 = pessoa[i]
print(f'Maior imc: {maior} {pessoa1}')
print(f'Menor imc: {menor} {pessoa2}')
