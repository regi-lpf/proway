negativo = int(0)

for i in range(0, 5):
    numero = int(input("Insira um número: "))
    if numero < 0:
        negativo += 1

print(negativo)