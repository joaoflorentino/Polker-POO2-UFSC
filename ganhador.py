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
import cartasDeck

## Classes ##

class vencedor:
    ''' Verifica melhor mão de Poker'''
    def __init__(self, mesa, jog1, jog2) -> None:
        self.jogadorMesa = mesa # Lista de cartas do jogador Mesa
        self.jogador1 = jog1         # Lista de cartas do jogador 1
        self.jogador2 = jog2         # Lista de cartas do jogador 2
        



###############
##### MAIN #####
''' Para teste deste arquivo não roda quando 
chamado em outros arquivos'''
if __name__ == '__main__':
    pass