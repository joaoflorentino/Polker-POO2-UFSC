#### 
# Programa Poker Disciplina POO II  - UFSC 2022-1
# Desenvolvedor - Luis Florentino  n- 17150281
####
''' Programa que simula um jogo de cartas Poer básico
que avalia o ganhador de uma distribuição de 05 cartas 
sem trocas de cartas
'''
## Este arquivo verifica qual jogador tem mlhor mão de Poker

# -*-*-*-*-*-*-*-*-*-* IMPORTs -**-*-*-*-

## Classes ##

class Vencedor:
    ''' Verifica melhor mão de Poker entre os 03 
    jogadores'''
    # Variavel global de ordenação 
    ordem = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'D':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    def __init__(self, mesa, jog1, jog2) -> None:
        self.jogadorMesa = mesa # Lista de cartas do jogador Mesa
        self.jogador1 = jog1         # Lista de cartas do jogador 1
        self.jogador2 = jog2         # Lista de cartas do jogador 2
    
    ## Organiza avaliação 
    def inicia(self):
        lista = []
        maos = {'M': self.jogadorMesa, 'J1' :self.jogador1, 'J2': self.jogador2 }
        for hand in maos:
            pontos = self.pontuacao(hand)
            lista.append(pontos)
        if lista[0] > lista[1] and lista[0] > lista[2]:
            texto = f'O Vencedor é a MESA. Com o Jogo {lista[0]} com a mão{self.jogadorMesa}'
            print(texto)
            return texto
        elif lista[1] > lista[0] and lista[1] > lista[2]:
            texto = f'O Vencedor é o JOGADOR 1. Com o Jogo {lista[0]} com a mão{self.jogadorMesa}'
            print(texto)
            return texto
        elif lista[2] > lista[0] and lista[2] > lista[1]:
                texto = f'O Vencedor é a JOGADOR 2. Com o Jogo {lista[0]} com a mão{self.jogadorMesa}'
                print(texto)
                return texto

    ## INICIO DAS REGRAS
    def straight_flush(self, mao):
        pass

    def quadra(self, mao):
        pass

    def full_house(self, mao):
        pass

    def flush(self, mao):
        pass

    def sequencia(self, mao):
        pass

    def trinca(self, mao):
        pass

    def dois_pares(self, mao):
        pass

    def par(self, mao):
        pass

 # PONTUACAO
    def pontuacao(self, mao):
        if self.straight_flush(mao):
            return 9
        if self.quadra(mao):
            return 8
        if self.full_house(mao):
            return 7
        if self.flush(mao):
            return 6
        if self.sequencia(mao):
            return 5
        if self.trinca(mao):
            return 4
        if self.dois_pares(mao):
            return 3
        if self.par(mao):
            return 2
        else:
            return 1
    

###############
##### MAIN #####
''' Para teste deste arquivo não roda quando 
chamado em outros arquivos'''
if __name__ == '__main__':
    pass