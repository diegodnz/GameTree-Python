# GameTree-Python
## Descrição
Projeto da cadeira IF969 - ALGORITMOS E ESTRUTURAS DE DADOS (CIn - UFPE).
Analisa cada possibilidade de jogada em uma árvore de jogo para a escolha do melhor movimento possível. 
Possui 3 variantes do TicTacToe: Tradicional, Wild e Misere
## Modos de Jogo
- TicTacToe tradicional
    - O primeiro jogador joga com o símbolo 'X'.
    - O segundo jogador joga com o símbolo 'O'.
    - O jogador que completar o tabuleiro 3x3 na vertical, horizontal ou diagonal com o seu símbolo, vence a partida.
    - Neste modo, caso ambos os jogadores joguem suas melhores jogadas, irá ocorrer um empate.
- Wild
    - Os jogadores escolhem o símbolo que desejam jogar em qualquer rodada.
    - O jogador que completar o tabuleiro 3x3 na vertical, horizontal ou diagonal com qualquer símbolo, vence a partida.
    - Neste modo, quem joga primeiro irá ganhar se fizer suas melhores jogadas possíveis.
- Misere
    - Ambos os jogadores jogam apenas com o símbolo 'X'.
    - O jogador que completar o tabuleiro 3x3 na vertical, horizontal ou diagonal, PERDE a partida.
    - Neste modo, quem joga primeiro irá ganhar se fizer suas melhores jogadas possíveis.
## Funcionalidades
- Jogador vs Máquina (Jogador inicia a partida)
- Máquina vs Jogador (Máquina inicia a partida)
- Máquina vs Random  (Testa a máquina contra jogadas randomizadas)
- Random vs Random   (São jogados n jogos randomizados. Este modo serve para a geração da árvore de jogo)
- Criação da árvore  (Simula todas as possibilidades de jogada e salva na árvore. Ao final da execução salva a árvore no arquivo)




