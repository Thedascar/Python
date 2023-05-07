a = int(input("Digite o 1º lado do triângulo: "))
b = int(input("Digite o 2º lado do triângulo: "))
c = int(input("Digite o 3º lado do triângulo: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print("Triângulo Escaleno")
        elif a == b and b == c:
            print("Triângulo Equilátero")
        else:
          print("Isóceles")
else:
    print("Triângulo inválido")