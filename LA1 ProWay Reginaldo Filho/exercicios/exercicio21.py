valor_produto = float(input("Insira o valor do produto: "))
percentual_desconto = float(input("Insira o '%' do desconto: "))

desconto = (valor_produto / 100) * (percentual_desconto)
produto_desconto = valor_produto - desconto

print("Total: ",produto_desconto)
print("Desconto: ",desconto)
