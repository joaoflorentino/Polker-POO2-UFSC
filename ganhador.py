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

from collections import defaultdict


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
        '''Cria lista com pontuação de cada jogador'''
        lista = []
        maos = {'M': self.jogadorMesa, 'J1' :self.jogador1, 'J2': self.jogador2 }
        ## Jogos possiveis de vitoria organizados em um dicionario
        jogosPoker = {9:'straight_flush', 8:'quadra', 7:'full_house', 6:'flush', 5:'sequencia', 4:'trinca', 3:'dois_pares', 2:'par', 1:'Maior Carta'}

        for hand in maos.values():
            pontos = self.pontuacao(hand)
            lista.append(pontos)
        if lista[0] > lista[1] and lista[0] > lista[2]:
            texto = f'O Vencedor é a MESA. Com o Jogo   {jogosPoker[lista[0]]}   com a mão  {self.jogadorMesa}'
            print(texto)
            return texto
        elif lista[1] > lista[0] and lista[1] > lista[2]:
            texto = f'O Vencedor é o JOGADOR 1. Com o Jogo   {jogosPoker[lista[1]]}   com a mão  {self.jogador1}'
            print(texto)
            return texto
        elif lista[2] > lista[0] and lista[2] > lista[1]:
            texto = f'O Vencedor é a JOGADOR 2. Com o Jogo   {jogosPoker[lista[2]]}   com a mão  {self.jogador2}'
            print(texto)
            return texto
        elif lista[0] == lista[1] and lista[0]== list[2]:
            print(lista)
            texto = f'Tres Jogos  de mão {jogosPoker[lista[0]]}  EMPATADOS'
            print(texto)
            return texto
        elif lista[0] == lista[1]:
            texto = f'Dois Jogos  de mão {jogosPoker[lista[0]]}  EMPATADOS'
            print(texto)
            return texto
        elif  lista[0] == lista[2]:
            texto = f'Dois Jogos  de mão {jogosPoker[lista[0]]}  EMPATADOS'
            print(texto)
            return texto
        elif lista [1] == lista[2]:
            texto = f'Dois Jogos  de mão {jogosPoker[lista[0]]}  EMPATADOS'
            print(texto)
            return texto
        

    ## INICIO DAS REGRAS
    def straight_flush(self, mao):
        '''Funcao que checa a ocorrencia de Straight-Flush'''
        if self.flush(mao) and self.sequencia(mao):
            return True
        else:
            return False

    def quadra(self, mao):
        '''Fucao que separa ocorrencia de quadra'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        if sorted (contaValor.values()) == [1,4]:
            return True
        else:
            return False

    def full_house(self, mao):
        '''Fucao que separa ocorrencia de Full_House'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        if sorted (contaValor.values()) == [2,3]:
            return True
        else:
            return False

    def flush(self, mao):
        '''Fucao que separa ocorrencia de flush mesmos naipes sem ordem'''
        naipes = [i[1] for i in mao]
        if len(set(naipes)) == 1:
            return True
        else:
            return False

    def sequencia(self, mao):
        '''Fucao que separa ocorrencia de sequencia sem mesmos naipes'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        ordemValor = [Vencedor.ordem[i] for i in valores]
        faixa = max(ordemValor) - min(ordemValor)
        if len(set(contaValor.values())) == 1 and (faixa == 4):
            return True
        else:
            if set(valores) == set(['A', '2', '3','4','5']):
                return True
            else:
                return False

    def trinca(self, mao):
        '''Fucao que separa ocorrencia de trinca'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        if set(contaValor.values()) == set([3,1]):
            return True
        else:
            return False

    def dois_pares(self, mao):
        '''Fucao que separa ocorrencia de Dois_Pares'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        if sorted (contaValor.values()) == [1,2,2]:
            return True
        else:
            return False

    def par(self, mao):
        '''Fucao que separa ocorrencia de Par'''
        valores = [i[0] for i in mao]
        contaValor = defaultdict(lambda:0)
        for v in valores:
            contaValor[v] += 1
        if 2 in contaValor.values():
            return True
        else:
            return False

 # PONTUACAO
    def pontuacao(self, mao):
        '''Executa as pontuações e retorna o valor de cada jogada'''
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
    mesa = ['DO', 'JS', '8C', '5O', 'JP']
    jog1 = ['9S', 'AS', '4S', '3S', 'DS']
    jog2 = ['KO', 'KC', 'DP', 'AO', 'KS']
    rodada = Vencedor(mesa, jog1, jog2)
    rodada.inicia()
