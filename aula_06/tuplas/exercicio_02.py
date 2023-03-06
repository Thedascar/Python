def maior(msg,*num):
    maior = 0
    for i in range(0,len(num),1):
        if num[i] > maior:
            maior = num[i]
    print(msg,maior)

maior('Maior: ',1,2,3,78,45,79,115,2,4,233)