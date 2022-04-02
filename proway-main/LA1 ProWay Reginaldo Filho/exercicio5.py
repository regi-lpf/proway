matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o valor na posição [{i}][{j}]: " ))
        linha.append(numero)
    matriz.append(linha)

soma = 0
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if i < j:
            soma += valor

print("Matriz:", matriz)
print("Soma: ", soma)
