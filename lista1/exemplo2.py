import datetime


#Desafio calcular a idade do usuário
ano_nascimento = int(input("digite o ano do seu nascimento: "))
ano_atual = data = datetime.date.today().year
idade = ano_atual - ano_nascimento
print("A idade do usuário é: ", idade)
