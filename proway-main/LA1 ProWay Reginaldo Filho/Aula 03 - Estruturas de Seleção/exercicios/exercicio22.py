# salario = float(input("Insira o salário: "))

# if salario <= 600:
#     print(f"Salário Líquido: R${salario}")
# elif salario > 600 and salario <= 1200:
#     salario_liquido = float((salario * 0.80))
#     print(f"Salário Líquido: R${salario_liquido}")
# elif salario > 1200 and salario <= 2100:
#     salario_liquido = float((salario * 0.75))
#     print(f"Salário Líquido: R${salario_liquido}")
# elif salario > 2100:
#     salario_liquido = float((salario * 0.70))
#     print(f"Salário Líquido: R${salario_liquido}")
# else:
#     print("Valor Inválido!")

#     salario = float(input("Insira o salário: "))


salario = float(input("Insira o salário: "))

salario_liquido = 0;
if salario <= 0:
    salario_liquido = "Valor inválido"
elif salario <= 600:
    salario_liquido = salario
elif salario <= 1200:
    salario_liquido = float((salario * 0.80))
elif salario <= 2100:
    salario_liquido = float((salario * 0.75))
else:
    salario_liquido = float((salario * 0.70))
    
print(salario_liquido)