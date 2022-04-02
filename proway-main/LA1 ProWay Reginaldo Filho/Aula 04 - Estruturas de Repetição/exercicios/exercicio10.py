par = int(0)
impar = int(0)

for i in range(0, 10):
    numero = int(input("Insira um número: "))
    if numero % 2 != 0:
        impar += 1
    else:
        par += 1
print(f'''
Pares: {par}
Ímpares: {impar}
''')