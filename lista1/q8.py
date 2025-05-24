latencias = []
while True:
    latencia = input("Latência: ")
    if latencia == "-1":
        break
    latencias.append(float(latencia))

print("A menor latência é: " + str(min(latencias)))