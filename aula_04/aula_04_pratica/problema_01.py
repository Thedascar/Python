print("Calculadora")
print("Qual operação deseja realizar ?")
while True:
    op = input("Digite uma operação: ")
    if op == "+" or op == "-" or op == "/" or op == "*":
        a = int(input("Digite o 1º valor: "))
        b = int(input("Digite o 2º valor: "))

    if op == "+":
        res = a + b
        print(f"A operação entre {a} {op} {b} é igual a: {res}")
        continue
    elif op == "-":
        res = a - b
        print(f"A operação entre {a} {op} {b} é igual a: {res}")
        continue
    elif op == "*":
        res = a * b
        print(f"A operação entre {a} {op} {b} é igual a: {res}")
        continue
    elif op == "/":
        res = a / b
        print(f"A operação entre {a} {op} {b} é igual a: {res}")
        continue
    elif op == "sair":
        break
    else:
        print("Operador inválido")
print('Software encerrado !!!')
