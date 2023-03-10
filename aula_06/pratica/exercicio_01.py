notas_init = [9,7,7,10,12,3,9,6,6,2]
notas = [9,7,7,10,3,9,6,6,2]
print('-----------------------------------')
print('Ocorrência de 7: ',notas.count(7))
print('-----------------------------------')
notas[8] = 4
print('Alterada: ',notas)
print('-----------------------------------')
maior = 0
for i in notas_init:
    if i > maior:
        maior = i
print('A maior nota da lista é: ',maior)
print('-----------------------------------')
notas.sort()
print('Lista Ordenada: ',notas)
print('-----------------------------------')

soma = 0
for i in notas:
    soma += i
print(soma)
print(f'A média é: {soma/len(notas):2.2f}')


