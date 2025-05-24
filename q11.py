import os
pasta = r""

conteudoArquivos = os.listdir(pasta)

for arquivo in conteudoArquivos:
    print(arquivo)