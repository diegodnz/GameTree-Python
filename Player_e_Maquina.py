"""
Universidade Federal de Pernambuco - UFPE
Projeto IF969 - ALGORITMOS E ESTRUTURAS DE DADOS
Curso: Sistemas de Informação
Ultima modificação: 12/12/2019
Autor: Alisson Diego Diniz D. Da Fonseca (adddf@cin.ufpe.br)
"""


import random

class Maquina:
    def __init__(self, arvore, jogo):
        self.arvore = arvore
        self.jogo = jogo
        self.maquinaInicia = True  # Variável booleana usada para checagem de vitória da maquina, dependendo se ela iniciou ou não a partida

    def tentarOutrasJogadas(self, blackList, menoresAdjacentes, simbolo=False):
        """Verifica se há jogadas válidas para o jogo sem levar em conta as jogadas que estão na blackList.
        Caso não tenha possibilidades de jogada excluindo a blackList, é escolhida uma jogada dos menoresAdjacentes caso haja.
        O parâmetro simbolo tem valor diferente de False somente quando o jogo é o TicTacToe, pois cada jogador joga com seu simbolo."""
        if not simbolo:
            listaJogadas = self.jogo.jogadasValidas(blackList)
        else:
            listaJogadas = self.jogo.jogadasValidas(simbolo, blackList)
        if not menoresAdjacentes:
            if not simbolo:
                self.jogo.jogarAleatorio()
            else:
                self.jogo.jogarAleatorio(simbolo)
        elif listaJogadas:
            if not simbolo:
                self.jogo.jogarAleatorio(blackList)
            else:
                self.jogo.jogarAleatorio(simbolo, blackList)
        else:
            jogou = False
            random.shuffle(menoresAdjacentes)
            for elemento in menoresAdjacentes:
                if not jogou and elemento[0].valor != float('inf'):
                    jogada = elemento[2]
                    self.jogo.jogar(jogada)
                    jogou = True
            if not jogou:
                jogada = menoresAdjacentes[0][2]
                self.jogo.jogar(jogada)

    def procurarJogada(self):
        """A maquina procura a melhor jogada para o estado atual do tabuleiro"""
        encontrouJogo = False
        # No TicTacToe a máquina só pode jogar com seu simbolo correspondente
        if self.jogo.nomeJogo == 'TicTacToe':
            simbolo = 'X' if self.maquinaInicia else 'O'
        else:
            simbolo = False
        # Encontrar o vertice na arvore de jogo correspondente ao tabuleiro atual
        if self.jogo.tabuleiro.tabuleiro in self.arvore.mapVertices:
            encontrouJogo = True
            verticeTabuleiro = self.arvore.mapVertices[self.jogo.tabuleiro.tabuleiro]

        if not encontrouJogo:
            if not simbolo:
                self.jogo.jogarAleatorio()
            else:
                self.jogo.jogarAleatorio(simbolo)
        else:
            vez = 'Maquina'
            self.arvore.preBuscaProfundidade(verticeTabuleiro, vez, self.maquinaInicia)
            blackList = []  # blackList salva todas as jogadas adjacentes existentes ao tabuleiro atual, para poder não selecioná-las caso seja necessaria uma jogada aleatoria diferente destas
            temAdjacentes = False
            menoresAdjacentes = []
            for adjacente in self.arvore.dicVertices[verticeTabuleiro]:
                peso = self.arvore.dicVertices[verticeTabuleiro][adjacente]
                # Busca a posição que difere o tabuleiro adjacente do atual, ou seja, a jogada futura
                jogada = self.jogo.buscarPosicao(adjacente.info, self.jogo.tabuleiro.tabuleiro)
                if self.jogo.nomeJogo != 'TicTacToe' or (self.maquinaInicia and jogada[2] == 'X') or (not self.maquinaInicia and jogada[2] == 'O'):
                    # No TicTacToe, a máquina joga exclusivamente com 'X' ou com 'O'.
                    blackList.append(jogada)
                    if not adjacente.valor == float('inf'):  # Se um vértice tem valor float('inf'), ele representa uma derrota
                        temAdjacentes = True
                        if menoresAdjacentes == [] or (peso == menoresAdjacentes[0][1]):
                            menoresAdjacentes.append((adjacente, peso, jogada))
                        elif peso < menoresAdjacentes[0][1]:
                            menoresAdjacentes = [(adjacente, peso, jogada)]
            if temAdjacentes:
                valor = menoresAdjacentes[0][1]
                if len(menoresAdjacentes) == 1:  # Se o menoresAdjacentes tiver apenas um elemento, há apenas uma aresta mínima
                    jogada = menoresAdjacentes[0][2]
                    if valor <= 0:  # Valor menor ou igual a 0 significa que este caminho leva possivelmente a uma vitoria
                        self.jogo.jogar(jogada)
                    else:  # Se o valor for maior que 0, checa se outras jogadas podem ser feitas
                        self.tentarOutrasJogadas(blackList, menoresAdjacentes, simbolo)
                else:
                    if valor <= 0:  # Se o valor =< 0, entao os menores adjacentes sao bons
                        elemento = random.choice(menoresAdjacentes)
                        jogada = elemento[2]
                        self.jogo.jogar(jogada)
                    else:
                        self.tentarOutrasJogadas(blackList, menoresAdjacentes, simbolo)
            else:
                self.tentarOutrasJogadas(blackList, menoresAdjacentes, simbolo)

# Input para jogada do player
def jogadaDoUsuario(jogo, nomeJogo, jogadorInicia):
    """Pede ao usuário a posição em que ele deseja jogar e retorna ela no formato (linha,coluna)"""
    posicoesDisponiveis = jogo.posicoesDisponiveis()
    if jogo.tabuleiro.tabuleiro == '000000000':
        print(f'Tabuleiro:\n{jogo}')
    jogadaPosicao = input(
        "Digite em qual posição deseja jogar (posições disponíveis -> " + str(posicoesDisponiveis).replace('[',
                                                                                                           '').replace(
            ']', '') + ": ")
    while jogadaPosicao not in posicoesDisponiveis:
        jogadaPosicao = input("Por favor digite corretamente em qual posicao deseja jogar (Apenas os números " + str(
            posicoesDisponiveis).replace('[', '').replace(']', '') + "): ")
    # Transforma a entrada do usuário em índices de matriz
    linha = 0
    coluna = int(jogadaPosicao) - 1
    while coluna > 2:
        coluna -= 3
        linha += 1

    if nomeJogo == 'Misere':
        return (linha, coluna)  # No Misere, apenas o 'X' é jogado.
    elif nomeJogo == 'TicTacToe':
        return (linha, coluna, 'X' if jogadorInicia else 'O')  # No TicTacToe, o jogador não escolhe seu símbolo
    else:  # No Wild, cada jogador escolhe o simbolo que deseja jogar em cada rodada
        simbolosValidos = ['X', 'x', 'O', 'o', '0']
        simbolo = input("Digite o símbolo que deseja jogar ('x' ou 'o'): ")
        while simbolo not in simbolosValidos:
            simbolo = input("Por favor, digite somente 'x' ou 'o': ")
        simbolo = 'X' if simbolo == 'x' else simbolo
        simbolo = 'O' if simbolo in ['o', '0'] else simbolo
        return (linha, coluna, simbolo)
