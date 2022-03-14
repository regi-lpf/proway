idade = int(input("Insira sua idade: "))
idade_doacao = bool(idade >= 18 and idade <= 67)

if idade_doacao == True:
    print("Você pode doar sangue")
else:
    print("Você não pode doar sangue") 