import numpy as np
import random
usuarios = {}
usuarios["ana"] = {"comedia": 3, "acao": 4, "drama": 4, "terror": 1, "romance": 4}
usuarios["bruno"] = {"comedia": 5, "acao": 2, "drama": 3, "terror": 4, "romance": 1}
usuarios["carla"] = {"comedia": 2, "acao": 5, "drama": 3, "terror": 2, "romance": 4}
usuarios["daniel"] = {"comedia": 1, "acao": 4, "drama": 5, "terror": 3, "romance": 2}
usuarios["elisa"] = {"comedia": 4, "acao": 3, "drama": 4, "terror": 2, "romance": 5}
usuarios["felipe"] = {"comedia": 3, "acao": 5, "drama": 2, "terror": 3, "romance": 1}
usuarios["giulia"] = {"comedia": 5, "acao": 2, "drama": 5, "terror": 1, "romance": 4}
usuarios["henrique"] = {"comedia": 2, "acao": 4, "drama": 4, "terror": 5, "romance": 1}
usuarios["isabela"] = {"comedia": 4, "acao": 3, "drama": 5, "terror": 2, "romance": 3}
usuarios["joao"] = {"comedia": 3, "acao": 4, "drama": 2, "terror": 4, "romance": 5}
usuarios["karen"] = {"comedia": 4, "acao": 3, "drama": 5, "terror": 2, "romance": 4}
usuarios["lucas"] = {"comedia": 5, "acao": 4, "drama": 2, "terror": 3, "romance": 2}
usuarios["mariana"] = {"comedia": 3, "acao": 5, "drama": 3, "terror": 2, "romance": 5}
usuarios["nicolas"] = {"comedia": 2, "acao": 3, "drama": 4, "terror": 4, "romance": 1}
usuarios["olivia"] = {"comedia": 4, "acao": 2, "drama": 5, "terror": 1, "romance": 5}
usuarios["paulo"] = {"comedia": 3, "acao": 4, "drama": 2, "terror": 5, "romance": 2}
usuarios["quiteria"] = {"comedia": 2, "acao": 5, "drama": 4, "terror": 3, "romance": 3}
usuarios["rafael"] = {"comedia": 5, "acao": 2, "drama": 3, "terror": 4, "romance": 4}
usuarios["sabrina"] = {"comedia": 3, "acao": 3, "drama": 5, "terror": 1, "romance": 5}
usuarios["tiago"] = {"comedia": 4, "acao": 4, "drama": 2, "terror": 3, "romance": 3}

filmes = {}
filmes["as aventuras de pi"] = ["comedia", "acao"]
filmes["um amor para recordar"] = ["romance", "drama"]
filmes["velozes e furiosos"] = ["acao", "aventura"]
filmes["invocacao do mal"] = ["terror", "suspense"]
filmes["o diabo veste prada"] = ["comedia", "drama"]
filmes["a origem"] = ["acao", "ficcao"]
filmes["extraordinario"] = ["drama", "familia"]
filmes["deadpool"] = ["comedia", "acao"]
filmes["it: a coisa"] = ["terror", "drama"]
filmes["la la land"] = ["musical", "romance"]

gostou = {}
gostou["ana"] = ["as aventuras de pi", "um amor para recordar", "extraordinario"]
gostou["bruno"] = ["velozes e furiosos", "invocacao do mal", "deadpool"]
gostou["carla"] = ["o diabo veste prada", "deadpool", "la la land"]
gostou["daniel"] = ["um amor para recordar", "a origem", "it: a coisa"]
gostou["elisa"] = ["as aventuras de pi", "la la land", "o diabo veste prada"]
gostou["felipe"] = ["velozes e furiosos", "a origem", "deadpool"]
gostou["giulia"] = ["extraordinario", "um amor para recordar", "la la land"]
gostou["henrique"] = ["invocacao do mal", "it: a coisa", "deadpool"]
gostou["isabela"] = ["extraordinario", "as aventuras de pi", "o diabo veste prada"]
gostou["joao"] = ["la la land", "velozes e furiosos", "deadpool"]
gostou["karen"] = ["extraordinario", "um amor para recordar", "la la land"]
gostou["lucas"] = ["velozes e furiosos", "deadpool", "a origem"]
gostou["mariana"] = ["o diabo veste prada", "la la land", "as aventuras de pi"]
gostou["nicolas"] = ["invocacao do mal", "it: a coisa", "velozes e furiosos"]
gostou["olivia"] = ["um amor para recordar", "la la land", "extraordinario"]
gostou["paulo"] = ["deadpool", "velozes e furiosos", "invocacao do mal"]
gostou["quiteria"] = ["a origem", "velozes e furiosos", "deadpool"]
gostou["rafael"] = ["o diabo veste prada", "as aventuras de pi", "la la land"]
gostou["sabrina"] = ["extraordinario", "um amor para recordar", "la la land"]
gostou["tiago"] = ["velozes e furiosos", "deadpool", "a origem"]

def calcula_n_vizinhos(usuario):
    N = int(np.sqrt(len(usuarios)))
    valor_usuario = []
    for gosto in usuarios[usuario]:
            valor_usuario.append(usuarios[usuario][gosto])
    valor_usuario = np.array(valor_usuario)
    proximidades = {}
    for vizinho in usuarios.keys():
        if vizinho != usuario:
            lista_vizinho = []
            for gosto in usuarios[vizinho]:
                lista_vizinho.append(usuarios[vizinho][gosto])
            lista_vizinho = np.array(lista_vizinho)
            distancia = float(np.linalg.norm(valor_usuario - lista_vizinho))
            proximidades[vizinho] = distancia
    p = {k: v for k, v in sorted(proximidades.items(), key=lambda item: item[1])}
    return list(p.items())[:N]

def recomenda_filme(usuario):
    vizinhos = calcula_n_vizinhos(usuario)
    filmes = []
    for v in vizinhos:
        for f in gostou[v[0]]:
            if f not in filmes:
                filmes.append(f)
        print(v[0])
    print(filmes)
    return filmes[random.randint(0,len(filmes)-1)]

print(recomenda_filme("tiago"))