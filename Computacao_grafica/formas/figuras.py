"""
Programa simples para desenhar um quandaro em tela
"""
#Importando biliotecas
from OpenGL.GL import *
from OpenGL.GLUT import *

"""--------------------------------------------------
    Função responsavel por mostrar as figuras na tela
   -------------------------------------------------
"""
def display():
    
    glClear(GL_COLOR_BUFFER_BIT)#Limpando o buffer de cor
    glColor3f(1.0, 0.0, 0.0)#Definindo a cor para vermelho
    glBegin(GL_POLYGON)#Inicializando a macro de poligonos
    
    #Chamando a função da forma
    quadrado()
    
    #Terminar
    glEnd()
    glFlush()

def quadrado():
    #Definido os vertices da figura
    glVertex3f(0.00, 0.00, 0.00)
    glVertex3f(0.75, 0.00, 0.00)
    glVertex3f(0.75, 0.75, 0.00)
    glVertex3f(0.00, 0.75, 0.00)


#Inicializando
glutInit()
#Definido o modo do display
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
#Definindo o tamanho da janela e a posição dela
glutInitWindowSize(480, 480)
glutInitWindowPosition(100, 100)
#Criado a janela principal
janela = glutCreateWindow("Quadrado")
glClearColor(0.0, 0.0, 0.0, 0.0)
#Chamando a a função criada para apresentar sua saida na tela
glutDisplayFunc(display)
glutMainLoop()