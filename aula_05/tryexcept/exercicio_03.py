def divisao():
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite um número: '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Divisão por zero não né')
    except:
        print('Algo deu errado')
    else:
        return res
    finally:
        print('Programa liso')


print(divisao())