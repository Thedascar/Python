
def define_par(num):
    if num % 2 == 0:
        return 'Par'
    return 'ímpar'


num = int(input('Digite um valor inteiro: '))
res = define_par(num)
print(res)