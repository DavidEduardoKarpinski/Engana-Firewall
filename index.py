#Importação da biblioteca urllib no módulo request:
from urllib import request

#Menu Bem-Vindo:
print(" Olá! Bem-Vindo a ferramenta de Requisições Web engana Firewall!")

#Variável URL:
url = input(">>>> Digite a URL...")
print(url)

#Dicionário Request-Header:
cabecalho = {"User-Agent": input(">>>> Insira o User-Agent"), "Cookie": input(">>>> Insira o cookie") }

#Parte executável do código: A variável req recebe a url e o dicionário cabecalho, que recebeu anteriormente o User-Agent e o Cookie. 
#A resposta utiliza o método urlopen, e recebe req. A variável html recebe req, com o método .read(), que nos permite visualizar o conteúdo HTML da página. Em caso de erros, a ferramente irá retornar o tipo do erro.
try:
    req = request.Request(url, headers=cabecalho)
    resposta = request.urlopen(req)
    html = resposta.read()
    print(html)
except Exception as error:
    print("[*] Ops! Ocorreu um erro inexperado!")
    print(error)
