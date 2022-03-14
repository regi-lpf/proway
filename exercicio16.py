idade = int(input("Informe sua idade: "))

if idade >= 16:
    if idade >= 18:
        print("Voto obrigatório")
    else:
        print("Voto opcional")
else:
    print("Não vota")