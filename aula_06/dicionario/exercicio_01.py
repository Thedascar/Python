aluno = {}

aluno['nome'] = input('Digite o seu nome: ')
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
aluno['media'] = (nota1 + nota2 + nota3) / 3

if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['status'] = 'Em exame'
else:
    aluno['status'] = 'Reprovado'

for i,j in aluno.items():
    print(f'{i} = {j}')