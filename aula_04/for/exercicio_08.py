print('Números Primos')
for i in range(2,100,1):
    flag = 0
    for j in range(2,i,1):
        if i % j == 0:
            flag = 1
            break
    if not flag:
        print(i)