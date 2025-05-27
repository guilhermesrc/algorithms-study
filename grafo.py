from collections import deque
grafo = {}
grafo["voce"] = ["alice","bob","claire"]
grafo["bob"] = ["anuj","peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom","jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == "m"
fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]
a = True
while a:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print(pessoa + " é um vendedor de manga!")
        a=False
    else:
        fila_de_pesquisa+=grafo[pessoa]
