salario = float(input("Digite seu sálario: "))
ano_admissao = int(input("Digite o ano de contratação: "))
ano_atual = int(input("Digite o ano em que estamos: "))
tempo_empresa = ano_atual - ano_admissao
if tempo_empresa >= 5:
    bonus = salario + salario * 0.2
    print(f"Seu tempo de empresa é de {tempo_empresa} anos")
    print(f"Parabéns pelo aumento seu novo salário será de R${bonus}")
else:
    bonus = salario + salario * 0.1
    print(f"Você tem {tempo_empresa} anos de empresa e seu novo salário é de {bonus}")

