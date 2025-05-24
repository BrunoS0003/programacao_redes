import requests

#site = input("Digite o nome de um site: ")
site = "https://www.globo.com/"
conteudo = requests.get(site)

conteudo.encoding = conteudo.apparent_encoding

with open("index.html","w", encoding = conteudo.encoding) as arquivo:
    arquivo.write(conteudo.text)
    arquivo.close()