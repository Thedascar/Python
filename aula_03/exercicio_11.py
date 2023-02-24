print("Calculadora")
a = int(input("Digite o 1º valor: "))
b = int(input("Digite o 2º valor: "))
print("Qual operação deseja realizar ?")
op = input("Digite uma operação: ")
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
    print("Operador inválido")

print(f"A operação entre {a} {op} {b} é igual a: {res}")