print("Calculadora")
print("Qual operação deseja realizar ?")
op = input("Digite uma operação: ")
if op != 's':
    a = int(input("Digite o 1º valor: "))
    b = int(input("Digite o 2º valor: "))
else:
    print('Bye')

while op != 's':

    if op == "+":
        res = a + b
        op = "+"
    elif op == "-":
        res = a - b
        op = "-"
    elif op == "*":
        res = a * b
        op = "*"
    elif op == "/":
        res = a / b
        op = "/"
    else:
        res = print("Operador inválido")

    print(f"A operação entre {a} {op} {b} é igual a: {res}")

    op = input("Digite uma operação: ")
    if op != 's':
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))
    else:
        print('Bye')




