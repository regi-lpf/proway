valor_a = int(input("Insira o valor A: "))
valor_b = int(input("Insira o valor B: "))
valor_c = int(input("Insira o valor C: "))

if valor_a > valor_b and valor_a > valor_c:
        print("O maior valor é ",valor_a)
elif valor_b > valor_c:
        print("O maior valor é ",valor_b)
else:
        print("O maior valor é ",valor_c)