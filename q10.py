import os

nome_pasta = input("Digite o nome da pasta que deseja criar: ")

try:
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso!")
except FileExistsError:
    print(f"A pasta '{nome_pasta}' já existe.")
except Exception as e:
    print(f"Ocorreu um erro ao criar a pasta: {e}")
