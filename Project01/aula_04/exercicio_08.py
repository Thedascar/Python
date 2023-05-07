inicio = 0
fim = 10
qtd_positivo = 0
soma_positivo = 0

qtd_par = 0
soma_par = 0

qtd_impar = 0
soma_impar = 0

media_positivo = 0
media_par = 0
media_impar = 0
while inicio <= fim:
    if inicio > 0:
        qtd_positivo += 1
        soma_positivo += inicio
    if inicio % 2 == 0:
        qtd_par += 1
        soma_par += inicio
    else:
        qtd_impar += 1
        soma_impar += inicio
    inicio += 1

media_positivo = soma_positivo/qtd_positivo
media_par = soma_par/qtd_par
media_impar = soma_impar/qtd_impar

print(f" q pos {qtd_positivo}")
print(f" soma pos {soma_positivo}")
print(f" media pos {media_positivo}")
print(f"q par {qtd_par}")
print(f"soma par {soma_par}")
print(f" media par {media_par}")
print(f"q impar {qtd_impar}")
print(f"soma impar {soma_impar}")
print(f" media impar {media_impar}")