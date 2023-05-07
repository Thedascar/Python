salario = float(input("Digite seu sálario: "))
ano_admissao = int(input("Digite o ano de contratação: "))
ano_atual = int(input("Digite o ano em que estamos: "))
tempo_empresa = ano_atual - ano_admissao
if(tempo_empresa >= 10):
    bonus = salario + salario * 0.3
    print(f"Você tem {tempo_empresa} anos de empresa seu bônus é de 30% seu novo salário é de {bonus}")
else:
    if tempo_empresa >= 5:
        bonus = salario + salario * 0.2
        print(f"Você tem {tempo_empresa} anos de empresa  seu bônus é de 20% seu novo salário é de {bonus}")
    else:
        bonus = salario + salario * 0.1
        print(f"Você tem {tempo_empresa} anos de empresa  seu bônus é de 10% seu novo salário é de {bonus}")



