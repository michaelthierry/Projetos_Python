from tkinter import*

class Calculadora:
    def __init__(self, App):
        #Configurações da janela principal
        cor_frame = "#092909"
        App.title("Calculadora")
        App.geometry("240x320")
        App.config(bg=cor_frame)

        self.frame_tela(App)
        self.frame_botoes(App)
        

    def frame_tela(self,App):
        #Criando o frame para a tela e configurando
        cor_frame = "#2c332d"
        frame_tela = Frame(App, width=240, height=60, bg=cor_frame)
        frame_tela.grid(row=0, column=0)
        
    
    def frame_botoes(self, App):
        #Criando o frame dos botoes
        frame_botoes = Frame(App, width=240, height=260)
        frame_botoes.grid(row=1, column=0)
        #Criando botoes
        cor1 = "#0a6310"
        b1 = self.cria_botao(frame_botoes, "C", 16, 2, 0, 0, None)
        b2 = self.cria_botao(frame_botoes, "%", 8, 2, 120, 0, None)
        b3 = self.cria_botao(frame_botoes, "/", 8, 2, 180, 0, cor1)

        b4 = self.cria_botao(frame_botoes, "7", 8, 2, 0, 40, None)
        b5 = self.cria_botao(frame_botoes, "8", 8, 2, 60, 40, None)
        b6 = self.cria_botao(frame_botoes, "9", 8, 2, 120, 40, None)
        b7 = self.cria_botao(frame_botoes, "*", 8, 2, 180, 40, None)

        b8 = self.cria_botao(frame_botoes, "4", 8, 2, 0, 80, None)
        b9 = self.cria_botao(frame_botoes, "5", 8, 2, 60, 80, None)
        b10 = self.cria_botao(frame_botoes, "6", 8, 2, 120, 80, None)
        b11 = self.cria_botao(frame_botoes, "+", 8, 2, 180, 80, None)

        b12 = self.cria_botao(frame_botoes, "1", 8, 2, 0, 120, None)
        b13 = self.cria_botao(frame_botoes, "2", 8, 2, 60, 120, None)
        b14 = self.cria_botao(frame_botoes, "3", 8, 2, 120, 120, None)
        b15 = self.cria_botao(frame_botoes, "-", 8, 2, 180, 120, None)

        b16 = self.cria_botao(frame_botoes, "0", 16, 2, 0, 160, None)
        b18 = self.cria_botao(frame_botoes, ".", 8, 2, 120, 160, None)
        b19 = self.cria_botao(frame_botoes, "=", 8, 2, 180, 160, cor1)
               

    def cria_botao(self, frame_botoes, caracter, largura, altura, x, y, cor):
        botao = Button(frame_botoes, text=caracter, width=largura, height=altura, bg=cor, relief=RAISED, overrelief=RIDGE)
        botao.place(x=x, y=y)
