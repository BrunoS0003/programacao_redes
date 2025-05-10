porta = int(input("digite uma porta TCP "))

#Portas válidas (conhecidas)
if porta >= 1 and porta <= 1024:
    print("Porta conhecida")
    print(porta, "É uma porta válida")
else:
    print("Porta desconhecida")    