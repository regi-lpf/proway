lado1 = int(input("Insira a medida do Lado 1: "))
lado2 = int(input("Insira a medida do Lado 2: "))
lado3 = int(input("Insira a medida do Lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Triângulo Equilátero")
elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado1 != lado2) or (lado3 == lado1 and lado3 != lado2):
    print("Triângulo Isóceles")
else:
    print("Triângulo Escaleno")