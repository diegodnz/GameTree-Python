class Tabuleiro:
    def __init__(self, jogo):
        self.tabuleiro = '000000000'
        self.jogo = jogo

    def criarTabuleiro(self, stringTabuleiro=None):
        """A partir de uma string que representa o tabuleiro com 0,1 ou 2, retorna uma matriz que representa o tabuleiro com linhas e colunas"""
        if stringTabuleiro == None:
            stringTabuleiro = self.tabuleiro
        tabuleiro = [['', '', ''], ['', '', ''], ['', '', '']]
        for char in range(len(stringTabuleiro)):
            if stringTabuleiro[char] != '0':
                i = char
                l = 0
                while i > 2:
                    l += 1
                    i -= 3
                if stringTabuleiro[char] == '1':
                    tabuleiro[l][i] = "X"
                elif stringTabuleiro[char] == '2':
                    tabuleiro[l][i] = "O"

        return tabuleiro

    def alterarTabuleiro(self, i, simbolo):
        """Dado um indice i e um simbolo, retona o tabuleiro com a posição i marcada com o simbolo (representa uma jogada)"""
        string = ''
        iTabuleiro = 0
        for char in self.tabuleiro:
            if iTabuleiro != i:
                string += char
            elif simbolo == "O":
                string += '2'
            elif simbolo == 'X':
                string += '1'
            else:
                string += '0'
            iTabuleiro += 1

        return string
