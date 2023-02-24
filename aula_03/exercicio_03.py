ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
minha_idade_e = ano_atual - ano_de_nascimento
print(f"A sua idade é {minha_idade_e}")
if minha_idade_e >= 18:
    print("Você já tem mais de 18 anos !!!!!!")
else:
    print("Você tem menos de 18 anos :(")