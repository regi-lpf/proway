valores = []

for i in range(8):
    valor = int(input("Insira um valor: "))
    valores.append(valor)

while True:
    X = int(input("Digite o valor de X: "))
    Y = int(input("Digite o valor de Y: "))
    
    if (0 <= X < 8) and (0 <= Y < 8):
        break

    print("Valores inválidos! Digite novamente")

soma = valores[X] + valores[Y]
print(soma)

