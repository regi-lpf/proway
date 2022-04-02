gols1 = int(input("Informe os gols do time 1: "))
gols2 = int(input("Informe os gols do time 2: "))

if gols1 == gols2:
    print("Empate")
elif gols1 > gols2:
    print("Vitória do time 1")
else:
    print("Vitória do time 2")