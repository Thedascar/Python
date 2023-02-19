d = int(input("Digite os dias : "))
h = int(input("Digite as horas : "))
m = int(input("Digite os minutos : "))
s = int(input("Digite os segundos : "))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 * 60)

print('O total de segundos é {} '.format(total))