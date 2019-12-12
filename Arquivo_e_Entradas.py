from GameTree import *
import os

def carregarArquivo(nome, nomeJogo):
    """Carrega o arquivo e retorna a arvore de jogo correspondente aos dados do arquivo"""
    arvoreDeJogo = GameTree(nomeJogo)
    # Caso o arquivo não exista, ele é criado
    try:
        grafo = open(nome, 'r')
    except Exception:
        grafo = open(nome, 'w')
        grafo.close()
        grafo = open(nome, 'r')
    # Adiciona os vértices e arestas do arquivo na árvore de jogo
    for l in grafo.readlines():
        linha = l.split(';')
        vertice = linha.pop(0)
        # Tirar o \n do ultimo elemento
        if len(linha) > 0:
            novoElemento = ''
            for caractere in linha[len(linha) - 1]:
                if caractere != '\n':
                    novoElemento += caractere
            linha[len(linha) - 1] = novoElemento
        else:
            # Caso o vértice seja o único elemento da linha, retira o \n dele mesmo
            novoElemento = ''
            for caractere in vertice:
                if caractere != '\n':
                    novoElemento += caractere
            vertice = novoElemento
        arvoreDeJogo.addAdjacents(vertice, linha, 0)
    return arvoreDeJogo


def salvarArvoreNoArquivo(arvoreDeJogo, nomeJogo):
    """Salva a arvore de jogo no arquivo. O arquivo segue o padrão a cada linha: vertice;adj1;adj2... (Caso não tenha adjacentes apenas o vertice ocupa a linha)"""
    if nomeJogo == 'Wild':
        arquivo = open('game-treeWild.txt', 'w')
    elif nomeJogo == 'Misere':
        arquivo = open('game-treeMisere.txt', 'w')
    else:
        arquivo = open('game-treeTicTacToe.txt', 'w')
    for vertice in arvoreDeJogo.dicVertices:
        adjacentsString = ''
        for adjacente in arvoreDeJogo.dicVertices[vertice]:
            adjacentsString += ';' + adjacente.info
        arquivo.write(
            vertice.info + adjacentsString + '\n')  # O calculo do peso das arestas e feito dinâmicamente a cada jogada, logo não é necessário salvar no arquivo
    arquivo.close()


def entradas(primeiraEscolha, limparTerminal):
    """Pede as entradas do usuário para iniciar o jogo.
    Retorna: se o usuário inicia a partida caso ele jogue, o nome do jogo, o nome do arquivo txt que será salva a arvore,
    o modo de jogo escolhido pelo usuário e a quantidade de jogos caso ele escolha um modo que tenha bots."""
    os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
    if primeiraEscolha:
        printDescricoes()
    print('Lista de modos de jogo:\n1 -> Tic-Tac-Toe tradicional\n2 -> Wild Tic-Tac-Toe\n3 -> Misere')
    # Selecionar modo de jogo
    nomeJogo = input('\nDigite a seguir o número correspondente ao jogo que deseja jogar: ')  # 1 -> Tic-Tac-Toe   2 -> Wild   3 -> Misere
    while nomeJogo not in ['1', '2', '3']:
        nomeJogo = input('Por favor, digite apenas 1, 2 ou 3: ')
    if nomeJogo == '1':
        nomeJogo = 'TicTacToe'
        nomeArquivo = 'game-treeTicTacToe.txt'
    elif nomeJogo == '2':
        nomeJogo = 'Wild'
        nomeArquivo = 'game-treeWild.txt'
    else:
        nomeJogo = 'Misere'
        nomeArquivo = 'game-treeMisere.txt'
    os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
    modoJogo = input('\nModos de jogo: '
                     '\n1 -> Jogador vs Máquina (Jogador inicia jogando)'
                     '\n2 -> Máquina vs Jogador (Máquina inicia jogando)'
                     '\n3 -> Máquina vs Bot aleatório'
                     '\n4 -> Bot aleatório vs Bot aleatório'
                     '\n5 -> Gerar árvore com todas as possibilidades'
                     '\n\nOBS: Em qualquer modo de jogo, as jogadas não conhecidas anteriormente são salvas na árvore.'
                     '\n     No final da execução, toda a árvore é salva no arquivo.\n'
                     '\nDigite o número correspondente ao modo de jogo: ')
    while modoJogo not in ['1', '2', '3', '4', '5']:
        modoJogo = input('Digite apenas as opções 1, 2, 3, 4 ou 5: ')
    jogadorInicia = False
    jogosModoBot = 0
    if modoJogo == '1':
        modoJogo = 'PxM'
        jogadorInicia = True
    elif modoJogo == '2':
        modoJogo = 'MxP'
    elif modoJogo == '3':
        modoJogo = 'MxB'
        jogosModoBot = int(input('Digite a quantidade de jogos: '))
    elif modoJogo == '4':
        modoJogo = 'BxB'
        jogosModoBot = int(input('Digite a quantidade de jogos: '))
    else:
        if nomeJogo == 'Misere':
            print('Tempo Estimado: 0.4s')
        elif nomeJogo == 'TicTacToe':
            print('Tempo Estimado: 11s')
        else:
            print('Tempo Estimado: 30min \nNeste modo há muitas possibilidades de jogada. Você pode construir a árvore no modo aleatório bot vs bot, porém sem garantia de que ela estará completa com todas as possibilidades')
    return jogadorInicia, nomeJogo, nomeArquivo, modoJogo, jogosModoBot


def printDescricoes():
    """Printa as descrições dos modos de jogo"""
    print('\nSeja Bem-vindo!!. Para jogar, você deve selecionar um dos três modos descritos a seguir:')
    descricaoTicTacToe = '->  Tic-Tac-Toe' + '\nDescrição e regras: É o modo de jogo tradicional, mais conhecido como jogo da velha. Cada jogador joga com seu símbolo ("X" ou "O"). \nO jogador que finalizar o tabuleiro com seu símbolo, vence a partida.'
    print('\n', descricaoTicTacToe)
    descricaoWild = '->  Wild Tic-Tac-Toe' + '\nDescrição e regras: É semelhante ao tic-tac-toe tradicional. Ambos os jogadores podem escolher jogar com o símbolo "X" ou "O" a cada jogada. \nO jogador que finalizar o tabuleiro com qualquer símbolo, vence a partida.'
    print('\n', descricaoWild)
    descricaoMisere = '->  Miserè' + '\nDescrição e regras: É um variante do jogo tic-tac-toe. Cada jogador joga com o mesmo símbolo "X". \nQuem completar 3 símbolos seguidos horizontalmente, verticalmente ou na diagonal do tabuleiro, PERDE!!.'
    print('\n',descricaoMisere,'\n\n')
