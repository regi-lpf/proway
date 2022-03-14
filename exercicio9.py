A = int(input("Insira o valor A: "))
B = int(input("Insira o valor B: "))
C = int(input("Insira o valor C: "))

if A > B and A > C:
    print("O maior valor é ",A)
else:
    if B > A and B > C:
        print("O maior valor é ",B)
    else:
        print("O maior valor é ",C)