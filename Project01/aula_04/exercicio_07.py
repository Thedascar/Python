x = int(input("Digite um valor: "))
y = int(input("Digite outro valor: "))
cont = 1
mult = 0
while cont <= x:
    mult += y
    cont += 1
print(f"{x} x {y} = {mult}")