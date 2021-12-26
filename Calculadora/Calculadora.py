from tkinter import*
from tkinter import font

class Calculadora:
    def __init__(self, App):
        #Configurações da janela principal
        cor_frame = "#092909"
        App.title("Calculadora")
        App.geometry("240x320")
        App.config(bg=cor_frame)
        texto = StringVar()
        

        self.frame_tela(App, texto)
        self.frame_botoes(App)

    def frame_tela(self,App,texto):
        #Criando o frame para a tela e configurando
        cor_frame = "#2c332d"
        #texto = StringVar()
        frame_tela = Frame(App, width=240, height=60, bg=cor_frame)
        frame_tela.grid(row=0, column=0)
    
        label = Label(frame_tela, textvariable=texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor_frame, fg="#ffffff")
        label.place(x=0, y=0)
        #print(self.texto)
        
    def frame_botoes(self, App):
        #Criando o frame dos botoes
        frame_botoes = Frame(App, width=240, height=260)
        frame_botoes.grid(row=1, column=0)
        #Criando botoes
        fundo = "#0a6310"
        fonte = "#ffffff"
        

        b1 = self.cria_botao(frame_botoes, "C", 16, 2, 0, 0, None, None)
        b2 = self.cria_botao(frame_botoes, "%", 8, 2, 120, 0, None, None)
        b2.config(command=lambda: self.inserir())
        b3 = self.cria_botao(frame_botoes, "/", 8, 2, 180, 0, fundo, fonte)

        b4 = self.cria_botao(frame_botoes, "7", 8, 2, 0, 40, None, None)
        b5 = self.cria_botao(frame_botoes, "8", 8, 2, 60, 40, None, None)
        b6 = self.cria_botao(frame_botoes, "9", 8, 2, 120, 40, None, None)
        b7 = self.cria_botao(frame_botoes, "*", 8, 2, 180, 40, fundo, fonte)

        b8 = self.cria_botao(frame_botoes, "4", 8, 2, 0, 80, None, None)
        b9 = self.cria_botao(frame_botoes, "5", 8, 2, 60, 80, None, None)
        b10 = self.cria_botao(frame_botoes, "6", 8, 2, 120, 80, None, None)
        b11 = self.cria_botao(frame_botoes, "+", 8, 2, 180, 80, fundo, fonte)

        b12 = self.cria_botao(frame_botoes, "1", 8, 2, 0, 120, None, None)
        b13 = self.cria_botao(frame_botoes, "2", 8, 2, 60, 120, None, None)
        b14 = self.cria_botao(frame_botoes, "3", 8, 2, 120, 120, None, None)
        b15 = self.cria_botao(frame_botoes, "-", 8, 2, 180, 120, fundo, fonte)

        b16 = self.cria_botao(frame_botoes, "0", 16, 2, 0, 160, None, None)
        b18 = self.cria_botao(frame_botoes, ".", 8, 2, 120, 160, None, None)
        b19 = self.cria_botao(frame_botoes, "=", 8, 2, 180, 160, fundo, fonte)
               

    def cria_botao(self, frame_botoes, caracter, largura, altura, x, y, fundo, fonte):
        botao = Button(frame_botoes, text=caracter, width=largura, height=altura, bg=fundo, fg=fonte, relief=RAISED, overrelief=RIDGE)
        botao.place(x=x, y=y)
        return botao

    def inserir(self):
        #valor = 'a'
        #texto.set(valor)  
        #print(self.texto)  
        pass    