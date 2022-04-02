contador_pares = 0
A = []

while contador_pares < 6:
    valor = int(input("Insira um número: "))
    
    if valor % 2 != 0:
        print("O valor não é par")
        continue

    A.append(valor)
    contador_pares += 1

print(A)
