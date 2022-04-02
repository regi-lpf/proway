salario = int(input("Insira o valor do salário: "))
prestacao = int(input("Insira o valor da prestação do empréstimo: "))

if prestacao > (salario / 5):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")