from tkinter import*
from tkinter import font

class Calculadora:
    
    def __init__(self, App):
        """
        Função construtrora da classe Calculadora, configura o frame principal e cria os frame
        de tela e os frame dos botoes 
        :Parametro App: raiz grafica do tipo Tk()
        """
        
        #Configurações da janela principal
        cor_frame = "#092909"

        App.title("Calculadora")
        App.geometry("240x320")
        App.config(bg=cor_frame)
        
        #Variavel de tela
        self.texto = StringVar()
        
        #Criando tela e botões da calculadora
        self.frame_tela(App)
        self.frame_botoes(App)
    
    def frame_tela(self,App):
        """
        Cria o frame da tela e o configura
        :Parametro App: raiz grafica do tipo Tk()
        """

        #Criando o frame da tela
        cor_frame = "#2c332d"

        #Configurando o frame
        frame_tela = Frame(App, 
                        width=240, 
                        height=60, 
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
             
    def frame_botoes(self, App):
        """
        Cria o frame dos botões, configura o frame e adiciona os botoes
        :Parametro App: raiz grafica do tipo Tk() 
        """
        #Criando o frame dos botoes e posicionando
        frame_botoes = Frame(App, 
                            width=240, 
                            height=260)
        frame_botoes.grid(row=1, column=0)
        
        #Cores da fonte
        cor_fundo = "#8800ff"
        cor_fonte = "#ffffff"
        cor_botao_limpar = "#5600a1"
        
        #Criando o botoes e definido as funções
        b1 = self.cria_botao(frame_botoes, "C", 16, 2, 0, 0, cor_botao_limpar, cor_fonte)
        b1["command"] = lambda: self.limpar_tela()

        b2 = self.cria_botao(frame_botoes, "%", 8, 2, 120, 0, None, None)
        b2["command"] = lambda: self.inserir("%")

        b3 = self.cria_botao(frame_botoes, "/", 8, 2, 180, 0, cor_fundo, cor_fonte)
        b3["command"] = lambda: self.inserir("/")

        b4 = self.cria_botao(frame_botoes, "7", 8, 2, 0, 40, None, None)
        b4["command"] = lambda: self.inserir("7")

        b5 = self.cria_botao(frame_botoes, "8", 8, 2, 60, 40, None, None)
        b5["command"] = lambda: self.inserir("8")

        b6 = self.cria_botao(frame_botoes, "9", 8, 2, 120, 40, None, None)
        b6["command"] = lambda: self.inserir("9")

        b7 = self.cria_botao(frame_botoes, "*", 8, 2, 180, 40, cor_fundo, cor_fonte)
        b7["command"] = lambda: self.inserir("*")

        b8 = self.cria_botao(frame_botoes, "4", 8, 2, 0, 80, None, None)
        b8["command"] = lambda: self.inserir("4")

        b9 = self.cria_botao(frame_botoes, "5", 8, 2, 60, 80, None, None)
        b9["command"] = lambda: self.inserir("5")

        b10 = self.cria_botao(frame_botoes, "6", 8, 2, 120, 80, None, None)
        b10["command"] = lambda: self.inserir("6")

        b11 = self.cria_botao(frame_botoes, "+", 8, 2, 180, 80, cor_fundo, cor_fonte)
        b11["command"] = lambda: self.inserir("+")

        b12 = self.cria_botao(frame_botoes, "1", 8, 2, 0, 120, None, None)
        b12["command"] = lambda: self.inserir("1")

        b13 = self.cria_botao(frame_botoes, "2", 8, 2, 60, 120, None, None)
        b13["command"] = lambda: self.inserir("2")

        b14 = self.cria_botao(frame_botoes, "3", 8, 2, 120, 120, None, None)
        b14["command"] = lambda: self.inserir("3")

        b15 = self.cria_botao(frame_botoes, "-", 8, 2, 180, 120, cor_fundo, cor_fonte)
        b15["command"] = lambda: self.inserir("-")

        b16 = self.cria_botao(frame_botoes, "0", 16, 2, 0, 160, None, None)
        b16["command"] = lambda: self.inserir("0")

        b18 = self.cria_botao(frame_botoes, ".", 8, 2, 120, 160, None, None)
        b18["command"] = lambda: self.inserir(".")

        b19 = self.cria_botao(frame_botoes, "=", 8, 2, 180, 160, cor_fundo, cor_fonte)
        b19["command"] = lambda: self.calcular()
               
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