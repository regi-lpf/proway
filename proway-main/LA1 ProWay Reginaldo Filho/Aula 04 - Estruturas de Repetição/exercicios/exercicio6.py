soma = 0
for i in range(5):
    soma += float(input(f"Digite a nota {i + 1}: "))
    media = float(soma / 5)
print(f'''
Soma: {soma}
Média: {media}''')