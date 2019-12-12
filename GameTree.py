

from Wild import *
from Misere import *
from TicTacToe import *

class Vertice:
    def __init__(self, info):
        self.info = info
        # busca em profundidade
        self.visitado = False
        self.valor = 0

class GameTree:
    def __init__(self, nomeJogo):
        self.mapVertices = {}  # Mapeia cada vértice com sua classe Vertice()
        self.dicVertices = {}  # Dicionário de vértices do grafo -> {vertice: {verticeAdjacente: peso}}
        self.nomeJogo = nomeJogo  # Auxilia no calculo de pesos das arestas, pois dependendo do jogo a regra muda
        self.qntArestas = 0

    def mapeiaVertice(self, verticeString):
        """Recebe uma string e caso ela esteja presente no grafo, retorna o objeto da mesma, caso não esteja presente, cria e retorna um objeto Vertice"""
        if verticeString in self.mapVertices:
            verticeObj = self.mapVertices[verticeString]
        else:
            verticeObj = Vertice(verticeString)
            self.mapVertices[verticeString] = verticeObj
            self.dicVertices[verticeObj] = {}
        return verticeObj

    def addAdjacents(self, vertice, adjacentes, peso):
        """Recebe um vertice e liga ele à todos os adjacentes do parâmetro adjacents, que é uma lista de vertices"""
        vertice = self.mapeiaVertice(vertice)
        for adjacente in adjacentes:
            adjacente = self.mapeiaVertice(adjacente)
            self.dicVertices[vertice][adjacente] = peso
            self.qntArestas += 1

    def add(self, vertice1, vertice2, peso):
        """Adiciona aresta no dicionário de vértices. Se os vértices não existirem no grafo, são adicionados"""
        vertice1 = self.mapeiaVertice(vertice1)
        vertice2 = self.mapeiaVertice(vertice2)
        if vertice2 not in self.dicVertices[vertice1]:
            self.dicVertices[vertice1][vertice2] = peso
            self.qntArestas += 1

    def __str__(self):
        string = ''
        for vertice in self.dicVertices:
            adjacentes = []
            for adjacente in self.dicVertices[vertice]:
                adjacentes.append((adjacente.info, self.dicVertices[vertice][adjacente]))
            string += str(vertice.info) + ": " + str(adjacentes) + '\n'
        return string

    def checaVitoriaVertice(self, vertice, maquinaInicia):
        """Checa se um vértice representa vitória, dependendo do nome do jogo se a maquina iniciou"""
        qntSimbolos = 0
        for caractere in vertice.info:
            if caractere != '0':
                qntSimbolos += 1
        if qntSimbolos % 2 == 0:
            qntSimbolos = 'par'
        else:
            qntSimbolos = 'impar'
        if self.nomeJogo == 'Wild':
            jogo = Wild()
        elif self.nomeJogo == 'Misere':
            jogo = Misere()
        else:
            jogo = TicTacToe()
        jogo.tabuleiro.tabuleiro = vertice.info
        ganhador = jogo.tabuleiroFinalizado()
        if ganhador:
            if self.nomeJogo == 'Misere' and maquinaInicia and qntSimbolos == 'par':
                return 'Vitoria'
            elif self.nomeJogo == 'Misere' and not maquinaInicia and qntSimbolos == 'impar':
                return 'Vitoria'
            elif self.nomeJogo == 'Wild' and maquinaInicia and qntSimbolos == 'impar':
                return 'Vitoria'
            elif self.nomeJogo == 'Wild' and not maquinaInicia and qntSimbolos == 'par':
                return 'Vitoria'
            elif self.nomeJogo == 'TicTacToe' and maquinaInicia and ganhador == 'X':
                return 'Vitoria'
            elif self.nomeJogo == 'TicTacToe' and not maquinaInicia and ganhador == 'O':
                return 'Vitoria'
            else:
                return 'Derrota'
        else:
            return 'Empate'

    def existeLigacao(self, tabuleiro1, tabuleiro2):
        '''Checa se o tabuleiro2 é adjacente ao tabuleiro1'''
        tabuleiro1 = self.mapeiaVertice(tabuleiro1)
        tabuleiro2 = self.mapeiaVertice(tabuleiro2)
        if tabuleiro1 in self.dicVertices:
            if tabuleiro2 in self.dicVertices[tabuleiro1]:
                return True
        return False

    def preBuscaProfundidade(self, vertice, vez, maquinaInicia):
        """Inicializa a busca em profundidade, colocando os valores padrões para todos os vértices"""
        for v in self.dicVertices:
            v.visitado = False
            v.valor = 0
        self.buscaProfundidade(vertice, vez, maquinaInicia)

    def buscaProfundidade(self, vertice, vez, maquinaInicia):
        """Dado um vertice, faz a busca em profundidade, atualizando todos os valores das arestas de baixo para cima.
          O atributo vertice.valor representa o valor do vertice, tal que se "v2" é adjacente a "v1", a aresta "v1" -> "v2" tem peso v2.valor """
        vertice.visitado = True
        vertice.valor = float('inf') if vez == 'Maquina' else -float('inf')
        vezProximo = 'Oponente' if vez == 'Maquina' else 'Maquina'
        for adjacente in self.dicVertices[vertice]:
            if not adjacente.visitado:
                self.buscaProfundidade(adjacente, vezProximo, maquinaInicia)
            if adjacente.valor == float('inf'):
                if vez == 'Oponente':
                    vertice.valor = 1000
                self.dicVertices[vertice][adjacente] = float('inf')
            elif adjacente.valor == -float('inf'):
                if vez == 'Maquina':
                    vertice.valor = -1000
                self.dicVertices[vertice][adjacente] = -float('inf')
            else:
                if vez == 'Oponente' and adjacente.valor > vertice.valor:
                    vertice.valor = adjacente.valor-1
                elif vez == 'Maquina' and adjacente.valor < vertice.valor:
                    vertice.valor = adjacente.valor+1
                self.dicVertices[vertice][adjacente] = adjacente.valor

        # Quando o vértice não tem adjacentes, ele representa o fim de jogo
        if self.dicVertices[vertice] == {}:
            # Checa vitória ou derrota
            condicao = self.checaVitoriaVertice(vertice, maquinaInicia)
            if condicao == 'Vitoria':
                vertice.valor = -float('inf')
            elif condicao == 'Empate':
                vertice.valor = 0
            else:
                vertice.valor = float('inf')

