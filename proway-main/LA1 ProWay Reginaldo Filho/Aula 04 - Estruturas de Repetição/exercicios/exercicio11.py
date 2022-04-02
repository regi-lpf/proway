numero = int(1)
intervalo = int(0)
nao_intervalo = int(0)

while numero > 0:
    numero = int(input("Insira um número: "))
    if numero >= 10 and numero <= 20:
        intervalo += 1
    else:
        break
print(f'''
{nao_intervalo} números estão no intervalo
{intervalo} números estão fora do intervalo 
''')