numeroSwitchs = int(input("digite o número de switchs da rede: "))

switchs = []
for i in range(numeroSwitchs):
    portas = int(input("Digite o número de portas do switch " + str(i+1) + "? "))
    switchs.append(portas)

for switch in switchs:
    print("Número de portas: " + str(switch))    
