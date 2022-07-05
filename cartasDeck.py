#### 
# Programa Deck de cartas Disciplina POO II  - UFSC 2022-1
# Desenvolvedor - Luis Florentino  n- 17150281
####
'''Desafio Deck de Cartas
Escreva um programa em python que embaralha e distribui um baralho de 
cartas para nove jogadores diferentes.Você pode usar quaisquer recursos 
python que tenha a disposição.'''

from random import  randint, random, shuffle

class Baralho():
    '''Esta classe Monta o baralho com 4 naipes de 13 cartas'''

    deck = ['AO', '2O', '3O', '4O','5O','6O','7O', '8O','9O','DO','JO', 'QO','KO',
                    'AP', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', 'DP', 'JP', 'QP', 'KP',
                    'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'DC', 'JC', 'QC', 'KC',
                    'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'DS', 'JS', 'QS', 'KS' ]
    ##  Naipes = O♦-> ouros;P ♣-> Paus; C ♥-> Copas; ->S ♠ Espadas
    def __init__(self) -> None:
        self.__bcompleto = Baralho.deck
    
    def embaralhar(self):
        shuffle(self.__bcompleto)
        brl = self.__bcompleto
        return  brl

#######################################

class Mostra:
    ''' Mostra como ficou o baralho apos o embaralhamento'''
    def __init__(self, embaralhado) -> None:
        self.kartas = embaralhado
        self.copiaLista(self.kartas)
    
    def copiaLista(self, lista):
        ''' Faz uma copia física da lista de cartas embaralhadas para 
        evitar o problema de esvaziamento da lista original 
        a copia some sem alterar a lisa original'''
        for i in  lista:
            self.kopia = lista[:]
    
    def mostraBaralho(self):
        '''Mostra o baralho embaralhado sem no entanto altera 
        lista de cartar otiginais'''
        copia = self.kopia
        k = len (copia)
        print(f'=-=-=-=-=  Baralho de {k} cartas-=-=-=-=-=-=-=-=-')
        kt = 52

        while kt > 0:
            for j in range(0,14):
                print(f'{copia[0]} ', end='')
                copia.pop(0)
                verifica = len(copia)
                if verifica == 0:
                    break
                j += 1
            print()
            kt = len(copia)
        print('##  Embaralhado ##') 

########################################

class Distribui():
    '''Classe que realiza a distribuição de 05 cartas para 3 jogadores'''
    def __init__(self, baralho) -> None:
        self.baralhoMisturado = baralho
        self.jogadores = {'Jog01':[], 'Jog02':[], 'Jog03':[]}
        ### Cria dicionário com os 03 jogadores 
    def entrega(self):
        '''Entrega as 5 cartas para os 3 jogadores
        na sequencia vemos quem vence '''
        kt = 5
        while kt > 0:
            for jog in self.jogadores.keys():
                j = self.jogadores.get(jog)
                ct = self.baralhoMisturado[0]
                j.append(ct)
                self.baralhoMisturado.pop(0)
                stp = len(self.baralhoMisturado)
                if stp == 0:
                    break
            kt -= 1
            #kt = len(self.baralhoMisturado)
        return (self.jogadores)

    def mostraMao(self, distribuido):
        '''Mostra como ficou a distribuição de cartas entre
        os 03 jogadores '''
        print()
        print(f'-=-=-=-=-=-=-=-=  DISTRIBUIDA ENTRE OS JOGADORES =-=-=-=-=-=-=-')
        for mao in distribuido.keys():
            dor = distribuido.get(mao)
            print(f'{mao} = {dor}')
#################################


###############
##### MAIN #####
 
if __name__ == '__main__':
    jogada01 = Baralho()                       ## Inicia o jogo criando um baralho novo 
    kt = jogada01.embaralhar()          ## Armazena lista com as cartas já embaralhadas
    kaza = Mostra(kt)                             ## Passa a lista de cartas para que possamos ver todo o baralho embaralhado
    kaza.mostraBaralho()                     ## Mostra como ficou o baralho 
    mao1 = Distribui(kt)                        ## Chama classe de distribuição de cartas
    resultado = mao1.entrega()        ## Aramazena o dicionario com a lista de jogadores e cartas distribuidas
    mao1.mostraMao(resultado)      ## Mostra resultado final


