from collections import defaultdict

class Vertice:
    def __init__(self, habilidade = [], time = []):
        self.dado = habilidade # informação contida no vertice
        self.vizinho = list() # vertice que esta conectado ao vertice explorado
        self.nome = time
    
    def insereVizinho(self, vertice):
        if vertice not in self.vizinho:
            self.vizinho.append(vertice)
            self.vizinho.sort()

class Grafo:
    def __init__(self): 
        self.grafo = defaultdict(list) 
  
    def insereAresta(self, origem, destino): 
        self.grafo[origem].append(destino) 
  
    def BFS(self, vertice): 
        visitado = [False] * (len(self.grafo))   
        fila = []
        fila.append(vertice) 
        visitado[vertice] = True
  
        while fila: 
            vertice = fila.pop(0) 
            print ("Vertice:", vertice, end = " ")

            for i in self.grafo[vertice]: 
                if visitado[i] == False: 
                    fila.append(i) 
                    visitado[i] = True