
def soma(n1,n2):
   print(f'Soma: {n1 + n2}')
    
def subtracao(n1,n2):
    print(f'Subtração: {n1 - n2}')

def divisao(n1,n2):
    print(f'Divisão: {n1 / n2}')

def multiplicacao(n1,n2):
    print(f'Multiplicação: {n1 * n2}')
    
def menu(escolha,n1,n2):
    if escolha == '+':
        soma(n1,n2)
    elif escolha == '-':
        subtracao(n1,n2)
    elif escolha == '*':
        multiplicacao(n1,n2)
    elif escolha == '/':
        divisao(n1,n2)
    else:
        print('Operação inválida !!')
    
print('Bem Vindo a Calc Animal')
n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
print('Selecio a opção desejada (+,-,*,/)')
escolha = input("Escolha a operação: ")
menu(escolha,n1,n2)