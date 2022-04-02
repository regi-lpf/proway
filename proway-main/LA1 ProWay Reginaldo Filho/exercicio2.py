from ast import And


matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j: 
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for linha in (matriz):
    for valor in (linha):
        print(valor, end=" ")
    print()