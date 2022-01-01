from tkinter import*
from tkinter import font

class Calculadora:
    Flag = 0
    
    def __init__(self, App):
        """
        Função construtrora da classe Calculadora, configura o frame principal e cria os frame
        de tela e os frame dos botoes 
        :Parametro App: raiz grafica do tipo Tk()
        """
        
        #Configurações da janela principal
        cor_frame = "#092909"

        App.title("Calculadora")
        App.geometry("264x320")
        App.resizable(0,0)
        App.config(bg=cor_frame)
        
        #Variavel de tela
        self.texto = StringVar()
        
        #Criando tela e botões da calculadora
        self.frame_tela(App, 264)
        self.frame_botoes(App, 264)
    
    def frame_tela(self, App, largura):
        """
        Cria o frame da tela e o configura
        :Parametro App: raiz grafica do tipo Tk()
        """

        #Criando o frame da tela
        cor_frame = "#2c332d"

        #Configurando o frame
        frame_tela = Frame(App, 
                        width=largura, 
                        height=75, 
                        bg=cor_frame)
        frame_tela.grid(row=0, column=0)

        #Configurando e posicionando o label 
        label = Label(frame_tela, 
                    textvariable=self.texto, 
                    width=16, 
                    height=2, 
                    padx=7, 
                    relief=FLAT, 
                    anchor="e", 
                    justify=RIGHT, 
                    font=('Ivy 18'), 
                    bg=cor_frame, 
                    fg="#ffffff")
        label.place(x=0, y=0)
         
    def frame_botoes(self, App, largura):
        """
        Cria o frame dos botões, configura o frame e adiciona os botoes
        :Parametro App: raiz grafica do tipo Tk() 
        """
        #Criando o frame dos botoes e posicionando
        frame_botoes = Frame(App, 
                            width=largura, 
                            height=247)
        frame_botoes.grid(row=1, column=0)
        
        #Cores da fonte
        cor_fundo = "#8800ff"
        cor_fonte = "#ffffff"
        cor_botao_limpar = "#5600a1"
        
        #Criando o botoes e definido as funções
        botoa_limpa_tela = self.cria_botao(frame_botoes, "C", 18, 2, 0, 0, cor_botao_limpar, cor_fonte)
        botoa_limpa_tela["command"] = lambda: self.limpar_tela()

        botao_apagar = self.cria_botao(frame_botoes, "DEL", 18, 2, 132, 0, cor_fundo, cor_fonte)
        botao_apagar["command"] = lambda: self.apagar()

        

        botao_science =self.cria_botao(frame_botoes, "Science", 8, 2, 0, 41, cor_fundo, cor_fonte)
        botao_science["command"] = lambda: self.frame_cientifica(App)
    
        botao_abre_parenteses = self.cria_botao(frame_botoes, "(", 8, 2, 66, 41, cor_fundo, cor_fonte)
        botao_abre_parenteses["command"] = lambda: self.inserir("(")

        botao_fecha_parentese = self.cria_botao(frame_botoes, ")", 8, 2, 132, 41, cor_fundo, cor_fonte)
        botao_fecha_parentese["command"] = lambda: self.inserir(")")
        
        botao_modulo = self.cria_botao(frame_botoes, "%", 8, 2, 198, 41, cor_fundo, cor_fonte)
        botao_modulo["command"] = lambda: self.inserir("%")
        


        botao_sete = self.cria_botao(frame_botoes, "7", 8, 2, 0, 82, None, None)
        botao_sete["command"] = lambda: self.inserir("7")

        botao_oito = self.cria_botao(frame_botoes, "8", 8, 2, 66, 82, None, None)
        botao_oito["command"] = lambda: self.inserir("8")
        
        botao_nove = self.cria_botao(frame_botoes, "9", 8, 2, 132, 82, None, None)
        botao_nove["command"] = lambda: self.inserir("9")

        botao_divisao = self.cria_botao(frame_botoes, "/", 8, 2, 198, 82, cor_fundo, cor_fonte)
        botao_divisao["command"] = lambda: self.inserir("/")
               
       

        botao_quatro = self.cria_botao(frame_botoes, "4", 8, 2, 0, 123, None, None)
        botao_quatro["command"] = lambda: self.inserir("4")
        
        botao_cinco = self.cria_botao(frame_botoes, "5", 8, 2, 66, 123, None, None)
        botao_cinco["command"] = lambda: self.inserir("5")

        botao_seis = self.cria_botao(frame_botoes, "6", 8, 2, 132, 123, None, None)
        botao_seis["command"] = lambda: self.inserir("6")

        botao_multiplica = self.cria_botao(frame_botoes, "*", 8, 2, 198, 123, cor_fundo, cor_fonte)
        botao_multiplica["command"] = lambda: self.inserir("*")



        botao_um = self.cria_botao(frame_botoes, "1", 8, 2, 0, 164, None, None)
        botao_um["command"] = lambda: self.inserir("1")

        botao_dois = self.cria_botao(frame_botoes, "2", 8, 2, 66, 164, None, None)
        botao_dois["command"] = lambda: self.inserir("2")

        botao_tres = self.cria_botao(frame_botoes, "3", 8, 2, 132, 164, None, None)
        botao_tres["command"] = lambda: self.inserir("3")

        botao_soma = self.cria_botao(frame_botoes, "+", 8, 2, 198, 164, cor_fundo, cor_fonte)
        botao_soma["command"] = lambda: self.inserir("+")


        botao_zero = self.cria_botao(frame_botoes, "0", 8, 2, 0, 205, None, None)
        botao_zero["command"] = lambda: self.inserir("0")

        botao_ponto = self.cria_botao(frame_botoes, ".", 8, 2, 66, 205, None, None)
        botao_ponto["command"] = lambda: self.inserir(".")

        botao_igual = self.cria_botao(frame_botoes, "=", 8, 2, 132, 205, cor_fundo, cor_fonte)
        botao_igual["command"] = lambda: self.calcular()

        botao_subtracao = self.cria_botao(frame_botoes, "-", 8, 2, 198, 205, cor_fundo, cor_fonte)
        botao_subtracao["command"] = lambda: self.inserir("-")    
                     
    def cria_botao(self, frame_botoes, caracter, largura, altura, px, py, cor_fundo, cor_fonte):
        """Função cria os botoes, os configura e os retorna
        frame_botoes: onde será ecriado os botões
        caracter: titulo do botao
        largura: lagura do botao
        altura: altura do botão 
        px: posição x do botao 
        py: posição y do botao
        cor_fundo: cor de fundo do botão
        cor_fonte: cor da fonte do botão
        """
        botao = Button(frame_botoes, 
                        text=caracter, 
                        width=largura, 
                        height=altura, 
                        bg=cor_fundo, 
                        fg=cor_fonte, 
                        relief=RAISED, 
                        overrelief=RIDGE)
        botao.place(x=px, y=py)
        return botao

    def inserir(self, valor):
        """
        Função recebe o valor digitado e adiciona na variavel de texto do label
        valor: valor digitado pelo o usuário
        """
        buffer = self.texto.get()
        self.texto.set(buffer+valor)

    def calcular(self):
        """
        Função pega os valores de texto do label calcula e expressao 
        e altera os valores de texto do label 
        """
        valor = self.texto.get()
        resultado = eval(valor)
        self.texto.set(resultado)
    
    def limpar_tela(self):
        """
        Função apaga o texto do label
        """
        self.texto.set("")
    
    def apagar(self, ):
        texto = self.texto.get()
        texto = texto[:-1]
        self.texto.set(texto)

    def frame_cientifica(self, App):
        if self.Flag == 0:
            print("é Zero")
            App.geometry("400x320")
            self.frame_tela(App,400)
            self.frame_botoes(App,400)
            self.Flag = 1
        elif self.Flag == 1:
            print("é um")
            App.geometry("264x320")
            self.frame_tela(App,264)
            
            self.Flag = 0
