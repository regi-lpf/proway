turno = input("Insira seu turno: M-matutino ou V-Vespertino ou N-Noturno.").upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno ==  "N":
    print("Boa noite!")
else:
    print("Valor inválido!")
    