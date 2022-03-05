'''Variáveis

As variáveis são espaços na memória que sua aplicação utiliza para armazenar os dados em tempo de execução.

Regras de nomenclatura:
    * Não pode começar com símbolos (exceto _) e números.
    * Os nomes devem ser descritivos e de simples entendimento.
    * Cada nova palavra de variável deve ser separada por _. (Python)

Linguagens dinamicamente tipadas x Linguagens estaticamente tipadas'''

from re import A


nome: str = "Reginaldo"
cpf: str = "123456789-00"
idade: int = 14
altura: float = 1.83
presente: bool = True
vazio = None

print("Nome:",nome)
print("CPF:",cpf)
print("Idade:",idade)
print("Altura:",altura)
print("Presente:",presente)

print(hex(id(cpf)))

VALOR1, VALOR2 = 10, 20

print(VALOR1, VALOR2)

a, b = 1, 2
auxiliar = a # a = 1, b = 2, auxiliar = 1
a = b # a = 2, b = 2, auxiliar = 1
b = auxiliar # a = 2, b = 1, auxiliar = 1
print(a, b)

# Isso é exclusivo do Python
c, d = 1, 2
d, c = c, d
print(c, d)