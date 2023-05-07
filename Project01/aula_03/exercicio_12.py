print("Compras")
print("1 - À vista")
print("2 - parcelamento em 3x ")
print("3 - parcelamento em 5x ")
print("4 - parcelamento em 10x ")
opcao = int(input("Qual é a opção de parcelamento: "))
preco = float(input("Qual é o valor da mercadoria: "))

if opcao == 1:
    final = preco * 0.95
    print(f"Sua compra à vista de {preco} com desconto de 5% ficará: R$ {final}")
elif opcao == 2:
    parcelado = preco + (preco / 3)
    print(f"Sua compra de {preco} em 3x ficará: R$ {parcelado}")
elif opcao == 3:
    final = preco + (preco * 0.2)
    parcelado = final / 5
    print(f"Sua compra de {preco} em 5x ficará R$ {parcelado} com valor final de R$ {final}")

elif opcao == 4:
    final = (preco + preco) * 0.8
    parcelado = final / 10
    print(f"Sua compra de {preco} em 10x ficará R$ {parcelado} com valor final de R$ {final}")
else:
    print("Opção inválida")



