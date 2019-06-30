class Vertice:
    def __init__(self, habilidade, time):
        self.dado = habilidade # informação contida no vertice
        self.vizinho = list() # vertice que esta conectado ao vertice explorado
        self.nome = time
    
    def insereVizinho(self, vertice):
        if vertice not in self.vizinho:
            self.vizinho.append(vertice)
            self.vizinho.sort()

class Grafo:
    vertices = {}

    def insereVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.dado not in self.vertices:
            self.vertices[vertice.dado] = vertice
            return True
        else:
            return False

    def insereAresta(self, sub, vertice):
        if sub in self.vertices and vertice in self.vertices:
            for chave, valor in self.vertices.items():
                if chave == sub:
                    valor.insereVizinho(vertice)
                if chave == vertice:
                    valor.insereVizinho(sub)
            return True
        else:
            return False