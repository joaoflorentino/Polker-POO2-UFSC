 #******************************************
# Trabalho Jogo de Poker - POO II  UFSC 2022-1
# Desenvolvedor  João Florentino
# numero 17150281
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from tkinter import *
import tkinter.font  as tkF
from PIL  import Image, ImageTk

# Meus Imports
from  cartasDeck import *
import ganhador 

## FONTES TTF

##  GUI  
class Telatk():
    def __init__(self) -> None:
        '''Classe que gera a GUI onde o usuário para 
        intergir com o jogo
        '''
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
        self.janela.title(' POKER -  POO II - UFSC - 2022-1 ')
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
        text02 = (f'Jog01 = {j2}')
        j3 = dictJogs.get('Jog03')
        text03 = (f'Jog02 = {j3}')
        ## Artribui as caras distribuidas  ao varg  
        self.distribuido1.set(text01)
        self.distribuido2.set(text02)
        self.distribuido3.set(text03)

        ## Separa listas 
        self.listaMesa = j1
        self.listaJog1 = j2
        self.listaJog2 = j3
        ## Mostra as mãos no frame 02

        # -=-=-=-=-=-=-=-=-=   FRAME  02 =-=-=-=-=-=-=-=-=-=
        # -*-*-*-*-*-*-*-* BANCA -*-*-*-*-*-*-*-*-*
        # Distribuição de cartas da mesa da Jogada
        lb11 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido1, justify='left', wraplength= 400)
        lb11.place(relx=0.02, rely=0.11)
        ## Cartas do baralho jogador MESA
        w = Canvas(self.janela) # Gera imagem no canvas para inserção no frame
        #carta 01
        c0 = j1[0]
        ima1 = self.reduzImage(c0)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima1) # chama imagem no canvas
        w.image1 = ima1 # gera o w imagem para inserção no Label
        lbc1 = Label(self.frame2, image=w.image1)
        lbc1.place(relx=0.02, rely=0.21 )
        #carta 02,
        c1 = j1[1]
        ima2 = self.reduzImage(c1)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima2) # chama imagem no canvas
        w.image2 = ima2 # gera o w imagem para inserção no Label
        lbc2 = Label(self.frame2, image=w.image2)
        lbc2.place(relx=0.10, rely=0.21 )
        #carta 03
        c2 = j1[2]
        ima3 = self.reduzImage(c2)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima3) # chama imagem no canvas
        w.image3 = ima3 # gera o w imagem para inserção no Label
        lbc3 = Label(self.frame2, image=w.image3)
        lbc3.place(relx=0.18, rely=0.21 )
        #carta 04
        c3 = j1[3]
        ima4 = self.reduzImage(c3)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima4) # chama imagem no canvas
        w.image4 = ima4 # gera o w imagem para inserção no Label
        lbc4 = Label(self.frame2, image=w.image4)
        lbc4.place(relx=0.26, rely=0.21 )
        #carta 05
        c4 = j1[4]
        ima5 = self.reduzImage(c4)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima5) # chama imagem no canvas
        w.image5 = ima5 # gera o w imagem para inserção no Label
        lbc5 = Label(self.frame2, image=w.image5)
        lbc5.place(relx=0.34, rely=0.21 )

        # -*-*-*-*-*-*-*-* JAGADOR 1 -*-*-*-*-*-*-*-*-*

        lb12 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido2, justify='left', wraplength= 400)
        lb12.place(relx=0.02, rely=0.48)

        #carta 01
        d0 = j2[0]
        ima6 = self.reduzImage(d0)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima6) # chama imagem no canvas
        w.image6 = ima6 # gera o w imagem para inserção no Label
        lbcJog1 = Label(self.frame2, image= w.image6)
        lbcJog1.place(relx=0.02, rely=0.57 )
        #carta 02
        d1 = j2[1]
        ima7 = self.reduzImage(d1)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima7) # chama imagem no canvas
        w.image7 = ima7 # gera o w imagem para inserção no Label
        lbcJog2 = Label(self.frame2, image=w.image7)
        lbcJog2.place(relx=0.10, rely=0.57 )
        #carta 03
        d2 = j2[2]
        ima8 = self.reduzImage(d2)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima8) # chama imagem no canvas
        w.image8 = ima8 # gera o w imagem para inserção no Label
        lbcJog3 = Label(self.frame2, image= w.image8)
        lbcJog3.place(relx=0.18, rely=0.57 )
        #carta 04
        d3 = j2[3]
        ima9 = self.reduzImage(d3)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima9) # chama imagem no canvas
        w.image9 = ima9 # gera o w imagem para inserção no Label
        lbcJog4 = Label(self.frame2, image= w.image9)
        lbcJog4.place(relx=0.26, rely=0.57 )
        #carta 05
        d4 = j2[4]
        ima10 = self.reduzImage(d4)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima10) # chama imagem no canvas
        w.image10 = ima10 # gera o w imagem para inserção no Label
        lbcJog5 = Label(self.frame2, image= w.image10)
        lbcJog5.place(relx=0.34, rely=0.57 )

        # -*-*-*-*-*-*-*-* JAGADOR 2 -*-*-*-*-*-*-*-*-*
        lb13 = Label(self.frame2, font=('nimbus sans l', 9), bg=self.c2, fg=self.c4, textvariable= self.distribuido3, justify='left', wraplength= 400)
        lb13.place(relx=0.52, rely=0.11)

        #carta 01
        t0 = j3[0]
        ima11 = self.reduzImage(t0)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima11) # chama imagem no canvas
        w.image11 = ima11 # gera o w imagem para inserção no Label
        lbcJogb1 = Label(self.frame2, image= w.image11)
        lbcJogb1.place(relx=0.52, rely=0.21 )
        #carta 02
        t1 = j3[1]
        ima12 = self.reduzImage(t1)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima12) # chama imagem no canvas
        w.image12 = ima12 # gera o w imagem para inserção no Label
        lbcJogb2 = Label(self.frame2, image= w.image12)
        lbcJogb2.place(relx=0.60, rely=0.21 )
        #carta 03
        t2 = j3[2]
        ima13 = self.reduzImage(t2)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima13) # chama imagem no canvas
        w.image13 = ima13 # gera o w imagem para inserção no Label
        lbcJogb3 = Label(self.frame2, image= w.image13)
        lbcJogb3.place(relx=0.68, rely=0.21 )
        #carta 04
        t3 = j3[3]
        ima14 = self.reduzImage(t3)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima14) # chama imagem no canvas
        w.image14 = ima14 # gera o w imagem para inserção no Label
        lbcJogb4 = Label(self.frame2, image= w.image14)
        lbcJogb4.place(relx=0.76, rely=0.21 )
        #carta 05
        t4 = j3[4]
        ima15 = self.reduzImage(t4)
        ## Passar para o label onde a carta aparecerá 
        w.create_image(0,0, image=ima15) # chama imagem no canvas
        w.image15 = ima15 # gera o w imagem para inserção no Label
        lbcJogb5 = Label(self.frame2, image= w.image15)
        lbcJogb5.place(relx=0.84, rely=0.21 )
    
    def avalia(self):
        '''Função que traz do arquivo ganhador o 
        resultado do jovo e apresenta na tel do Tkinter'''
        jogo = ganhador.Vencedor(self.listaMesa, self.listaJog1, self.listaJog2)
        resultado = jogo.inicia()
        print()
        print(resultado)


    def framesScreem (self):
        '''Função que define o tamanho e a posição dos frames'''
        # FRAME 1
        self.frame1 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.30)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 2
        self.frame2 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame2.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.50)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 3
        self.frame3 = Frame(self.janela, bd=4 ,bg=self.c2, highlightbackground=self.c3, highlightthickness=3)
        self.frame3.place(relx=0.01, rely=0.84, relwidth=0.98, relheight=0.15)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
       
       ## Lay-out ####
       # -=-=-=-=-=-=-=-=-=   FRAME  01 =-=-=-=-=-=-=-=-=-=
        lb01 = Label(self.frame1, text='POKER - UFSC -  POO II ', font=('nimbus sans l', 14), bg=self.c2, fg=self.c4)
        lb01.place(relx=0.30, rely=0.05)

        lb02 = Label(self.frame1, text='Jogo de Poker com 52 cartas do baralho,  embaralhadas e distribuida para 3 Jogadores', font=('nimbus sans l', 10), bg=self.c2, fg=self.c5)
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

        # -=-=-=-=-=-=-=-=-=   FRAME  02 Titulo =-=-=-=-=-=-=-=-=-=
        lb10 = Label(self.frame2, text='Cartas dos três Jogadores', font=('nimbus sans l', 15), bg=self.c2, fg=self.c4)
        lb10.place(relx=0.24, rely=0.00)

        # -=-=-=-=-=-=-=-=-=   FRAME  03 =-=-=-=-=-=-=-=-=-=
        ## Botao Ver Vencedor que utiliza o arquivo ganhador classe vencedor
        self.resultado = Button(self.frame3, text='  VENCEDOR  ',bd=3, bg='#f7ef59', command= self.avalia )
        self.resultado.place(relx=0.01,rely=0.01)
        ## Exibe o Resultado do jogo 
        
    
    ## =-=-=-=-=-=-=  Funcoes que geram e organizam imagem =-=-=-=-=-=-=
    def reduzImage(self, carta):
        '''Função que reduz resolucao de uma imagem 
        .png para colocar no Label TK'''
        self.card = carta ## Recebe a imagem da carta a ser reduzida
        arq = str(self.card + '.png') ## Gera o nome do arquivo da carta 
        iume = Image.open(f'imageCards/{arq}') #Prepara arquivo pgn para resize
        wi = iume.width //  13# Reduz imagem em 3 vezes(Somente numeros inteiros)
        h = iume.height //  11 # Reduz imagem em 3 vezes(Somente numeros inteiros)
        res = iume.resize((wi,h)) #Chama a função de redimensionamento
        #res.save('graficos/new4.png') # Salva nova imagem no arquivo
        iume = ImageTk.PhotoImage(res)  ## Carrega novamente a imagem reduzida no arquivo
        return (iume)

        
###############
##### MAIN #####
''' Para teste deste arquivo não roda quando 
chamado em outros arquivos'''


if __name__ == '__main__':

    tela1 = Telatk()