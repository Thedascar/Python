def maior(v1=0,v2=0,v3=0):
    if v1 > v2 and v1 > v3:
        if v2 > v3:
            print(f'Ordem crescente: {v3},{v2},{v1}')
        else:
            print(f'Ordem crescente: {v2},{v3},{v1}')
    elif v2 > v1 and v2 > v3:
        if v1 > v3:
            print(f'Ordem crescente: {v3},{v1},{v2}')
        else:
            print(f'Ordem crescente: {v1},{v3},{v2}')
    elif v3 > v1 and v3 > v2:
        if v1 > v2:
            print(f'Ordem crescente: {v2},{v1},{v3}')
        else:
            print(f'Ordem crescente: {v1},{v2},{v3}')

maior(45,2,4)