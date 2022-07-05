 #******************************************
# Trabalho Deck de cartas - POO II  UFSC 2022-1
# Desenvolvedor  João Florentino
# numero 17150281
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from tkinter import *
import tkinter.font  as tkF
from PIL  import Image

# Importação para colocar os dados do deck de cartas na label
from  cartasDeck import *

## FONTES TTF

##  GUI  
class Telatk():
    def __init__(self) -> None:
        '''Classe que gera a GUI onde o usuário entra os dados do grafico
        visualisa o grafico e com botoes interage com o resultado'''
        ### CORES =====
        self.c1 = '#265207'  #Cor do fundo de tela geral
        self.c2 = '#4f8529' #Cor de fundo do  Frame
        self.c3 = '#0c4006' #Cor da borda do Frame
        self.c4 = '#f7f01b' #Cor Texto
        self.c5 = '#f5f5f2' #Cor Texto quase branca
        
        # Demais funcoes de tela
        self.janela = Tk()
        self.telaScreem()
        self.framesScreem()
        
        ## Conservação da Janela Tkinter
        self.janela.mainloop()
    
    def telaScreem (self):
        '''Função que define o formato geral da tela '''
        self.janela.title(' POLKER -  POO II - UFSC - 2022-1 ')
        self.janela.configure(bg=self.c1)
        self.janela.geometry('1200x600')
        self.janela.resizable(True, True)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
        self.janela.maxsize(width=700, height=900)  # Define o tamanho maximo da tela se acima for True
        self.janela.minsize(width= 300, height= 500) # Define o tamanho minimo da tela se acima for True
        self.fontSt1 = tkF.Font(family='figs/dc_s.ttf', size=15)
        self.embaralhado = StringVar()
        self.distribuido1 = StringVar()
        self.distribuido2 = StringVar()
        self.distribuido3 = StringVar()
       


    def importaTextos(self):

        ## Buscando o Texto do Programa Deckcartas
        j01 = Baralho()
        self.krt = j01.embaralhar()
        emb =  Mostra(self.krt)
        emb.mostraBaralho()
        texto = self.krt
        self.embaralhado.set(texto)
        
    
    def importaTextos02(self):
        mao = Distribui(self.krt)
        dictJogs = mao.entrega()
        mao.mostraMao(dictJogs)
        #Criando os labels
        j1 = dictJogs.get('Jog01')
        text01 = (f'Banca = {j1}')

        j2 = dictJogs.get('Jog02')
        text02 = (f'Jog02 = {j2}')

        j3 = dictJogs.get('Jog03')
        text03 = (f'Jog03 = {j3}')

       
        ## Artribui as caras distribuidas  ao varg  
        self.distribuido1.set(text01)
        self.distribuido2.set(text02)
        self.distribuido3.set(text03)
        


    def framesScreem (self):
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 1
        self.frame1 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.30)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 2
        self.frame2 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame2.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.32)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 3
        self.frame3 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame3.place(relx=0.01, rely=0.66, relwidth=0.98, relheight=0.33)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
       
       ## Lay-out ####
       # -=-=-=-=-=-=-=-=-=   FRAME  01 =-=-=-=-=-=-=-=-=-=
        lb01 = Label(self.frame1, text='POLKER - UFSC -  POO II ', font=('nimbus sans l', 14), bg=self.c2, fg=self.c4)
        lb01.place(relx=0.30, rely=0.05)

        lb02 = Label(self.frame1, text='Jogo de Polker com 52 cartas do baralho,  embaralhadas e distribuida para 3 Jogadores', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb02.place(relx=0.01, rely=0.20)

        lb03 = Label(self.frame1, text='As cartas são divididas nos seguintes nipes:', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb03.place(relx=0.01, rely=0.31)
        ##  Naipes = O-> ouros; P-> Paus; C-> Copas; S-> Espadas
        lb04 = Label(self.frame1, text=' O-> ouros', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb04.place(relx=0.01, rely=0.41)

        lb05 = Label(self.frame1, text=' P-> Paus', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb05.place(relx=0.01, rely=0.51)        

        lb06 = Label(self.frame1, text=' C-> Copas', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb06.place(relx=0.01, rely=0.61)

        lb07 = Label(self.frame1, text=' S-> Espadas', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb07.place(relx=0.01, rely=0.71)

        lb08 = Label(self.frame1, text='Seguidos dos numerais de 2 -> 10 ; J  Q  K  e  A', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
        lb08.place(relx=0.01, rely=0.81)
        ##  BOTOES -*-*-*-*-*-*-*--
        ## Botao Embaralha e inicia o Jogo
        self.cmd_Grafico = Button(self.frame1, text='   Embaralha  ',bd=3, bg='#f7ef59', command= self.importaTextos )
        self.cmd_Grafico.place(relx=0.75,rely=0.52)
        ## Botão chamar grafico interativo para salvar figura
        self.cmd_GraficoInterativo = Button(self.frame1, text='Distribui',bd=3, bg='#f0b207', command= self.importaTextos02)
        self.cmd_GraficoInterativo.place(relx=0.75,rely=0.75)

        # -=-=-=-=-=-=-=-=-=   FRAME  02 =-=-=-=-=-=-=-=-=-=
       
        lb10 = Label(self.frame2, text='Cartas dos três Jogadores', font=('nimbus sans l', 15), bg=self.c2, fg=self.c4)
        lb10.place(relx=0.24, rely=0.00)

        lb11 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido1, justify='left', wraplength= 400)
        lb11.place(relx=0.02, rely=0.14)

        lb12 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido2, justify='left', wraplength= 400)
        lb12.place(relx=0.02, rely=0.44)

        lb13 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido3, justify='left', wraplength= 400)
        lb13.place(relx=0.02, rely=0.74)

        # -=-=-=-=-=-=-=-=-=   FRAME  03 =-=-=-=-=-=-=-=-=-=

    ### ANTIGO FRAME 02(mostra o baralho-embaralhado) - APAGAR MAIS TARDE
    '''
    lb08 = Label(self.frame2, text='Baralho Embaralhado', font=('nimbus sans l', 15), bg=self.c2, fg=self.c4)
        lb08.place(relx=0.30, rely=0.02)

        lb09 = Label(self.frame2, font=('nimbus sans l', 13), bg=self.c2, fg=self.c4, textvariable= self.embaralhado, justify='left', wraplength= 400)
        lb09.place(relx=0.02, rely=0.25)

    '''
    ## =-=-=-=-=-=-=  Funcoes que geram e organizam imagem =-=-=-=-=-=-=
    def reduzImage(self, carta):
        '''Função que reduz resolucao de uma imagem 
        .png para colocar no Label TK'''
        self.card = carta ## Recebe a imagem da carta a ser reduzida
        iume = Image.open(f'imageCards/{self.card}.png') #Prepara arquivo pgn para resize
        wi = iume.width //  3# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  3 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        #res.save('graficos/new4.png') # Salva nova imagem no arquivo
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        gra04= PhotoImage(file= res) # gera arquivo no Photoimage
        #gra04= PhotoImage(file= 'imageCards/new4.png') # gera arquivo no Photoimage

        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=gra04) # chama imagem no canvas
        w.image = gra04 # gera o w imagem para inserção no Label
        return (gra04)

if __name__ == '__main__':

    tela1 = Telatk()