"""
Universidade Federal de Pernambuco - UFPE
Projeto IF969 - ALGORITMOS E ESTRUTURAS DE DADOS
Curso: Sistemas de Informação
Ultima modificação: 11/12/2019
Autor: Alisson Diego Diniz D. Da Fonseca (adddf@cin.ufpe.br)
"""


import random
from Tabuleiro import *

class Misere:
    def __init__(self, gameTree=None):
        self.tabuleiro = Tabuleiro('Misere')
        self.nomeJogo = 'Misere'
        self.arvore = gameTree
        self.ultimaJogada = (0, 0)  # Ultima jogada serve para checar se o jogo encerrou no método fimDeJogo

    def __str__(self):
        string = ''
        tabuleiro = self.tabuleiro.criarTabuleiro()
        for linha in tabuleiro:
            i = 0
            for elemento in linha:
                if elemento == '':
                    elemento = ' '
                if i < 2:
                    string += elemento + '|'
                else:
                    string += elemento
                i += 1
            string += '\n'
        return string

    def tutorial(self):
        '''Mostra o tutorial do jogo Misere'''
        print('\n\n' + ' ' * 20 + ' Tutorial Miserè ')
        print(
            "\nOlá, para realizar suas jogadas siga a regra abaixo: \n\nVocê deve inserir um número referente a uma das posições disponíveis que serão apresentadas. \nAs posições vão de 1 a 9, que representam em ordem as posições do tabuleiro")
        print('\nExemplos: \n\nEntrada: 1')
        self.tabuleiro.tabuleiro = '100000000'
        print(self)
        print('Entrada: 5')
        self.tabuleiro.tabuleiro = '000010000'
        print(self)
        print('Entrada: 8')
        self.tabuleiro.tabuleiro = '000000010'
        print(self)
        self.tabuleiro.tabuleiro = '000000000'

    def posicoesDisponiveis(self):
        '''Retorna uma lista com as posições disponíveis para jogar no formato de input para o usuário'''
        jogadas = self.jogadasValidas()
        posicoes = []
        for jogada in jogadas:
            if jogada[0] == 0:
                posicoes.append(str(jogada[1] + 1))
            elif jogada[0] == 1:
                posicoes.append(str(jogada[1] + 4))
            elif jogada[0] == 2:
                posicoes.append(str(jogada[1] + 7))
        return posicoes

    def jogadasValidas(self, blackList=[]):
        '''Retorna todas as jogadas válidas possíveis no formato (linha,coluna) excluindo as que estão no parâmetro blackList'''
        tabuleiro = self.tabuleiro.criarTabuleiro()
        jogadas = []
        indiceL = 0
        for linha in tabuleiro:
            indiceC = 0
            for coluna in linha:
                if coluna == '':
                    if (indiceL, indiceC) not in blackList:
                        jogadas.append((indiceL, indiceC))
                indiceC += 1
            indiceL += 1
        return jogadas

    def jogar(self, jogada, simbolo='X'):
        """Faz a jogada e adiciona no grafo a aresta correspondente a esta jogada, somente se ainda não existir ligação entre elas"""
        linha = jogada[0]
        coluna = jogada[1]
        anterior = self.tabuleiro.tabuleiro
        i = linha * 3 + coluna
        self.ultimaJogada = (int(linha), int(coluna))
        self.tabuleiro.tabuleiro = self.tabuleiro.alterarTabuleiro(i, simbolo)
        if not self.arvore.existeLigacao(anterior, self.tabuleiro.tabuleiro):
            self.arvore.add(anterior, self.tabuleiro.tabuleiro, 0)

    def jogarAleatorio(self, blackList=[]):
        """Joga aleatoriamente, porém exclui as jogadas contidas na blacklist"""
        jogadas = self.jogadasValidas(blackList)
        pos = random.randint(0, len(jogadas) - 1)
        self.jogar(jogadas[pos])

    def fimDeJogo(self):
        '''Checa se a a partida encerrou com a ultima jogada. Este é um método mais eficiente do que o tabuleiroFinalizado()'''
        tabuleiro = self.tabuleiro.criarTabuleiro()
        linha = self.ultimaJogada[0]
        coluna = self.ultimaJogada[1]
        if tabuleiro[linha][0] == 'X' and tabuleiro[linha][1] == 'X' and tabuleiro[linha][2] == 'X':
            return True
        if tabuleiro[0][coluna] == 'X' and tabuleiro[1][coluna] == 'X' and tabuleiro[2][coluna] == 'X':
            return True
        if (tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X') or (
                tabuleiro[2][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[0][2] == 'X'):
            return True
        return False

    def tabuleiroFinalizado(self):
        """Checa se a partida encerrou em qualquer posicao do tabuleiro"""
        tabuleiro = self.tabuleiro.criarTabuleiro()
        for l in range(3):
            if tabuleiro[l][0] == 'X' and tabuleiro[l][1] == 'X' and tabuleiro[l][2] == 'X':
                return True
        for c in range(3):
            if tabuleiro[0][c] == 'X' and tabuleiro[1][c] == 'X' and tabuleiro[2][c] == 'X':
                return True
        if (tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X') or (
                tabuleiro[2][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[0][2] == 'X'):
            return True
        return False

    def buscarPosicao(self, proximo, anterior):
        '''Recebe dois estados do tabuleiro, retorna a linha e a coluna que difere estes tabuleiros, ou seja, a jogada seguinte'''
        i = 0
        while i < 9:
            if proximo[i] != anterior[i]:
                iLinha = i
                linha = 0
                while iLinha > 2:
                    linha += 1
                    iLinha -= 3
                coluna = iLinha
                return (linha, coluna)
            i += 1
        return None
