"""
Alterei o método nodo para que os filhos, sejam nodos armazenados numa lista.
"""

class Nodo23:
    def __init__(self, chave=None, chave2=None):
        self.chave = [chave, chave2]
        self.filhos = [None, None, None]
        
class Arvore23:
    def __init__(self, chave):
        self.raiz = Nodo23(chave)
    
    def inserir(self, raiz, chave):
        if raiz.chave[0] is None:
            raiz.chave[0] = chave
        elif raiz.chave[1] is None and chave > raiz.chave[0]:
            raiz.chave[1] = chave
        elif raiz.chave[0] > chave and raiz.chave[1] is None:
            aux = raiz.chave[0]
            raiz.chave[0] = chave
            raiz.chave[1] = aux
        else:
            if chave > raiz.chave[0] and chave < raiz.chave[1]:
                if raiz.filhos[1] is None:
                    raiz.filhos[1] = Nodo23(chave)
                else:
                    self.inserir(raiz.filhos[1], chave)
            elif chave < raiz.chave[0] and chave < raiz.chave[1]:
                if raiz.filhos[0] is None:
                    raiz.filhos[0] = Nodo23(chave)
                else:
                    self.inserir(raiz.filhos[0], chave)
            
            elif chave > raiz.chave[0] and chave > raiz.chave[1]:
                if raiz.filhos[2] is None:
                    raiz.filhos[2] = Nodo23(chave)
                else:
                    self.inserir(raiz.filhos[2], chave)
            else:
                print("raiz já existente na árvore")

if __name__ == "__main__":

    arvore = Arvore23(1)
    arvore.inserir(arvore.raiz, 3)
    arvore.inserir(arvore.raiz, 2)
    arvore.inserir(arvore.raiz, 4)
    arvore.inserir(arvore.raiz, 5)
    arvore.inserir(arvore.raiz, 6)
    print(arvore.raiz.filhos[2].filhos[2].chave)
"""
 #Todos vazios
            if raiz.filhos[0] is None and raiz.filhos[1] is None and raiz.filhos[2] is None:
                raiz.chave[1] = chave
            #O segundo e o ultimo vazios
            elif raiz.filhos[0] is not None and raiz.filhos[1] is None and raiz.filhos[2] is None:
                if raiz.filhos[0].chave[0] < chave or raiz.filhos[0].chave[1] < chave:
                    if raiz.
            # o primeiro e segundo vazios
            elif raiz.filhos[0] is not None and raiz.filhos[1] is None and raiz.filhos[2] is None:
            
            #o primeiro e o ultimo vazios
            elif raiz.filhos[0] is not None and raiz.filhos[1] is None and raiz.filhos[2] is not None:
            
            # o segundo vazio
            elif raiz.filhos[0] is not None and raiz.filhos[1] is None and raiz.filhos[2] is not None:
            
            #o ultimo vazio
            elif raiz.filhos[0] is not None and raiz.filhos[1] is not None and raiz.filhos[2] is  None:
            
            # o primeiro vazio
            elif raiz.filhos[0] is None and raiz.filhos[1] is not None and raiz.filhos[2] is not None:
            
            #todos cheios
            elif raiz.filhos[0] is not None and raiz.filhos[1] is not None and raiz.filhos[2] is not None:
"""
