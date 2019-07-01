class Clube:
    def __init__(self):
        self.nome = None
        self.habilidade = None
    
    def setNome(self, nome):
        self.nome = nome
 
    def getNome(self):
        return self.nome

    def setHabilidade(self, habilidade):
        self.habilidade = habilidade
    
    def getHabilidade(self):
        return self.habilidade