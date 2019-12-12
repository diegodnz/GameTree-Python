from Misere import *
from Wild import *
from Arquivo_e_Entradas import *
from Player_e_Maquina import *
import os
import time


def inicioJogo(nomeJogo, arvore):
    """Retorna a classe do jogo. Serve tanto para criar pela primeira vez, quanto para reiniciar o jogo caso o
    usuário queira jogar novamente """
    if nomeJogo == 'Misere':
        return Misere(arvore)
    elif nomeJogo == 'Wild':
        return Wild(arvore)
    else:
        return TicTacToe(arvore)


def ganhador(jogo, nomeJogo, vez, jogadorInicia):
    """Printa o ganhador da partida dependendo dos parâmetros recebidos"""
    if nomeJogo == 'TicTacToe':
        ganhador = jogo.tabuleiroFinalizado()
        if (ganhador == 'X' and jogadorInicia) or (ganhador == 'O' and not jogadorInicia):
            print('Parabéns, você venceu!!')
        elif (ganhador == 'O' and jogadorInicia) or (ganhador == 'X' and not jogadorInicia):
            print('Você perdeu :(')
        else:
            print('Empate!!')
    elif nomeJogo == 'Misere':
        print('Parabéns, você venceu!!') if vez == 'Jogador' else print('Você perdeu :(')
    else:
        if not jogo.tabuleiroFinalizado():
            print('Empate!!')
        else:
            print("Parabéns, você venceu!!") if vez == 'Maquina' else print('Você perdeu :(')

def jogando(jogadorInicia, jogo, modoJogo, nomeJogo, maquina=None, limparTerminal=False):
    """Nesta função a partida está em andamento,
    Retorna o jogador que faria a próxima jogada para a checagem de vitória ou derrota"""
    if modoJogo in ['MxB', 'BxB']:
        jogadores = ['Maquina', 'bot'] if maquina else ['bot1', 'bot2']
    else:
        jogadores = ['Jogador', 'Maquina'] if jogadorInicia else ['Maquina', 'Jogador']
    vez = jogadores[0]
    while not jogo.fimDeJogo() and jogo.jogadasValidas() != []:
        if vez == 'Jogador':
            jogada = jogadaDoUsuario(jogo, nomeJogo, jogadorInicia)
            jogo.jogar(jogada)
            os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
            print(jogo)
        elif vez == 'Maquina':
            maquina.procurarJogada()
            os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
            print(jogo)
        elif maquina and vez == 'bot':
            if nomeJogo == 'TicTacToe':
                jogo.jogarAleatorio('O')
            else:
                jogo.jogarAleatorio()
            os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
            print(jogo)
        elif vez == 'bot1':
            if nomeJogo == 'TicTacToe':
                jogo.jogarAleatorio('X')
            else:
                jogo.jogarAleatorio()
        else:  # bot2
            if nomeJogo == 'TicTacToe':
                jogo.jogarAleatorio('O')
            else:
                jogo.jogarAleatorio()
        vez = jogadores[1] if vez == jogadores[0] else jogadores[0]
    return vez

def gerarArvore(arvore, jogo, simbolo=None):
    """Executa todas as possibilidades possíveis no jogo, adicionando cada aresta de jogada na árvore de jogo"""
    tabuleiro = jogo.tabuleiro.tabuleiro
    if not jogo.tabuleiroFinalizado():
        salvaTabuleiro = tabuleiro
        if jogo.nomeJogo == 'TicTacToe':
            jogadasValidas = jogo.jogadasValidas(simbolo)
        else:
            jogadasValidas = jogo.jogadasValidas()
        for jogada in jogadasValidas:
            jogo.jogar(jogada)
            if simbolo is None:
                gerarArvore(arvore, jogo, None)
            else:
                s = 'O' if simbolo == 'X' else 'X'
                gerarArvore(arvore, jogo, s)
            jogo.tabuleiro.tabuleiro = salvaTabuleiro

def rodandoNoTerminal():
    limparTerminal = input('\nVocê está executando diretamente pelo terminal? ')
    if limparTerminal.lower() in ['s', 'sim', 'y', 'yes']:
        return True
    else:
        return False

def main():
    """Inicialização do jogo com base nas variáveis recebidas pela função entradas()"""
    limparTerminal = rodandoNoTerminal()
    primeiraEscolha = True
    sair = False
    while not sair:
        # Inputs do usuário
        jogadorInicia, nomeJogo, nomeArquivo, modoJogo, jogosModoBot = entradas(primeiraEscolha, limparTerminal)
        # Carrega os dados do txt para uma arvore de jogo
        arvoreDeJogo = carregarArquivo(nomeArquivo, nomeJogo)
        verticesArvore = len(arvoreDeJogo.dicVertices)
        arestasArvore = arvoreDeJogo.qntArestas
        # Inicialização do jogo
        jogo = inicioJogo(nomeJogo, arvoreDeJogo)
        if primeiraEscolha and modoJogo in ['PxM', 'MxP']:
            jogo.tutorial()
            input('Insira qualquer tecla para iniciar o jogo...')
        primeiraEscolha = False

        if modoJogo in ['PxM', 'MxP']:
            # Jogo com player
            jogarNovamente = True
            while jogarNovamente:
                os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
                maquina = Maquina(arvoreDeJogo, jogo)
                maquina.maquinaInicia = False if jogadorInicia else True
                vez = jogando(jogadorInicia, jogo, modoJogo, nomeJogo, maquina, limparTerminal)
                ganhador(jogo, nomeJogo, vez, jogadorInicia)
                # Input caso o player deseje jogar novamente
                jogarNovamente = False
                jogar = input("Deseja jogar novamente? [s/n]: ")
                if jogar.lower() in ['sim', 's', 'y', 'yes']:
                    jogarNovamente = True
                jogo = inicioJogo(nomeJogo, arvoreDeJogo)
        elif modoJogo in ['MxB', 'BxB']:
            # Jogo sem player
            estatisticas = {'Maquina': 0, 'bot': 0, 'Empates': 0}
            maquinaJoga = True if modoJogo == 'MxB' else False
            if not maquinaJoga:
                print('Bots estão jogando aleatoriamente...')
            for i in range(jogosModoBot):
                maquina = Maquina(arvoreDeJogo, jogo) if maquinaJoga else False
                vez = jogando(jogadorInicia, jogo, modoJogo, nomeJogo, maquina, limparTerminal)
                if maquinaJoga:
                    if nomeJogo == 'Misere':
                        estatisticas[vez] += 1
                        print(f'{vez} ganhou esta partida!!')
                    elif nomeJogo == 'Wild':
                        if not jogo.jogadasValidas():
                            estatisticas['Empates'] += 1
                            print('\nEmpate\n')
                        elif vez == 'Maquina':
                            estatisticas['bot'] += 1
                            print('Bot ganhou esta partida!!')
                        else:
                            estatisticas['Maquina'] += 1
                            print('Maquina ganhou esta partida!!')
                    else:  # nomeJogo == TicTacToe
                        ganhou = jogo.tabuleiroFinalizado()
                        if ganhou == 'X':
                            estatisticas['Maquina'] += 1
                            print('Maquina ganhou esta partida!!')
                        elif ganhou == 'O':
                            estatisticas['bot'] += 1
                            print('Bot ganhou esta partida!!')
                        else:
                            estatisticas['Empates'] += 1
                            print('\nEmpate\n')
                jogo = inicioJogo(nomeJogo, arvoreDeJogo)
            if maquinaJoga:
                print('\nEstatísticas:')
                print('Vitorias da maquina: ' + str(estatisticas['Maquina']))
                print('Vitorias do bot: ' + str(estatisticas['bot']))
                if nomeJogo != 'Misere':
                    print('Empates: ' + str(estatisticas['Empates']))
            else:
                print(f'Foram jogados {jogosModoBot} jogos aleatoriamente e os movimentos não conhecidos anteriormente foram adicionados na árvore de jogo')
                verticesArvoreFinal = len(arvoreDeJogo.dicVertices)
                arestasArvoreFinal = arvoreDeJogo.qntArestas
                print(f'A árvore ganhou {verticesArvoreFinal-verticesArvore} novos vértices e {arestasArvoreFinal - arestasArvore} novas arestas!!\nTotal: {verticesArvoreFinal} vértices e {arestasArvoreFinal} arestas')
        else:
            start = time.time()
            if nomeJogo == 'TicTacToe':
                gerarArvore(arvoreDeJogo, jogo, 'X')
            else:
                gerarArvore(arvoreDeJogo, jogo)
            tempoTotal = time.time()-start
            verticesArvoreFinal = len(arvoreDeJogo.dicVertices)
            arestasArvoreFinal = arvoreDeJogo.qntArestas
            print(f'Tempo decorrido: {round(tempoTotal, 2)}s\nA árvore ganhou {verticesArvoreFinal-verticesArvore} novos vértices e {arestasArvoreFinal - arestasArvore} novas arestas!!\nTotal: {verticesArvoreFinal} vértices e {arestasArvoreFinal} arestas')
        selecionarJogo = input('Deseja escolher outro jogo? [s/n]: ')
        if selecionarJogo.lower() in ['n', 'nao', 'não', 'no']:
            sair = True
        os.system('cls' if os.name == 'nt' else 'clear') if limparTerminal else None
        salvarArvoreNoArquivo(arvoreDeJogo, nomeJogo)


main()
