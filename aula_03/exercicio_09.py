print("Bem vindo(a) a Feira")
print("Selecio uma opção")
print("1 - Maça")
print("2 - Laranja")
print("3 - Banana")
produto = int(input("Qual é sua escolha: "))
peso_produto = int(input("Qual a quantidade: "))

if produto == 1:
    fruta = "Maça"
    total = peso_produto * 2.30
    if(produto == 2):
        fruta = "Laranja"
        total = peso_produto * 2.60
else:
    fruta = "Banana"
    total = peso_produto * 1.85

print(f"Você comprou {peso_produto} Kg de {fruta}, o total a pagar é de R${total}")