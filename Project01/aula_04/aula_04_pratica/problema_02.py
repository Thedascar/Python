valor= int(input('Digite um valor em R$: '))

while True:
    if valor > 100:
        nota100 = valor // 100
        valor -= nota100 * 100
        print(f'Cédulas de $100 =  {nota100}')
        if not valor:
            break
    if valor > 50:
        nota50 = valor // 50
        valor -= nota50 * 50
        print(f'Cédulas de $50 =  {nota50}')
        if not valor:
            break
    if valor > 20:
        nota20 = valor // 20
        valor -= nota20 * 20
        print(f'Cédulas de $20 =  {nota20}')
        if not valor:
            break
    if valor > 10:
        nota10 = valor // 10
        valor -= nota10 * 10
        print(f'Cédulas de $10 = {nota10}')
        if not valor:
            break
    if valor > 5:
        nota5 = valor // 5
        valor -= nota5 * 5
        print(f'Cédulas de $5 = {nota5}')
        if not valor:
            break
    if valor > 1:
        nota1 = valor // 1
        valor -= nota1 * 1
        print(f'Cédulas de $1 = {nota1}')
        break