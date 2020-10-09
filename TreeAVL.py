"""
Árvore AVL baseada no código apresentado em aula pelo professor Hanseclever
"""
class AVL:
    def balanceada(self):
        if (arvore.raiz.balanco < 2) and (arvore.raiz.balanco > -2):
            return True
        else:
            return False

    def calcula_altura(self, recursao=True):
        if not self.raiz is None:
            if recursao:
                if self.raiz.esquerda != None:
                    self.raiz.esquerda.calcula_altura()
                if self.raiz.direita != None:
                    self.raiz.direita.calcula_altura()

            self.altura = max(self.raiz.esquerda.altura,
                              self.raiz.direita.altura) + 1
        else:
            self.altura = -1
    
    def calcula_balanceamento(self, recurse=True):
        if not self.raiz is None:
            if recurse:
                if self.raiz.esquerda != None:
                    self.raiz.esquerda.calcula_balanceamento()
                if self.raiz.direita != None:
                    self.raiz.direita.calcula_balanceamento()

            self.balanco = self.raiz.esquerda.altura - self.raiz.direita.altura
        else:
            self.balanco = 0
    
    def gira_direita(self):
        raiz = self.raiz
        filho_esquerda = self.raiz.esquerda.raiz
        filho_esquerda_direita = filho_esquerda.direita.raiz
        self.raiz = filho_esquerda
        filho_esquerda.direita.raiz = raiz
        raiz.esquerda.raiz = filho_esquerda_direita
    
    def gira_esquerda(self):
        raiz = self.raiz
        filho_direita = self.raiz.direita.raiz
        filho_direita_esquerda = B.esquerda.raiz
        self.raiz = filho_direita
        filho_direita.esquerda.raiz = raiz
        raiz.direita.raiz = filho_direita_esquerda
    
    def balancear(self):

        self.calcula_altura(False)
        self.calcula_balanceamento(False)
        while abs(self.balanco) > 1:
            if self.balanco > 1:
                if self.raiz.esquerda.balanco < 0:
                    self.raiz.esquerda.gira_esquerda()  
                    self.calcula_altura()
                    self.calcula_balanceamento()
                self.gira_direita()

            if self.balanco < -1:
                if self.raiz.direita.balanco > 0:
                    self.raiz.direita.gira_direita() 
                    self.calcula_altura()
                    self.calcula_balanceamento()
                self.gira_esquerda()

            self.calcula_altura()
            self.calcula_balanceamento()

class Ponteiro:
    def __init__(self, lista):

        self.tamanho = len(lista)
        self.lista = lista
        self.indice = 0

    def __next__(self):
        if (self.indice < self.tamanho):
        
            posicao = self.lista[self.indice]
            self.indice += 1
            return posicao

        else:

            raise StopIteration("StopIt")

    def _iter_(self):
        return self
