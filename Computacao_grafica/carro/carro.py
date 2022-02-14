from ctypes import resize
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pywavefront
from pywavefront import visualization

#Variaveis Globias

T = 0
T2 = 0
T3 = 0
carro = pywavefront.Wavefront('carro.obj')
roda = pywavefront.Wavefront('roda.obj')

def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, w/h, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(7.0, 10.0, 15.0,
                0.0, 3.0, 0.0,
                0.0, 1.0, 0.0)

#Função de Rotação
def keys(key, x, y):
    global T
    global T2
    global T3

    if key == GLUT_KEY_LEFT:
        T -= 1
    elif key == GLUT_KEY_RIGHT:
        T += 1
    elif key == GLUT_KEY_UP:
        T2 -= 1
    elif key == GLUT_KEY_DOWN:
        T2 += 1
    elif key == GLUT_KEY_PAGE_UP:
        T3 -= 1
    elif key == GLUT_KEY_PAGE_DOWN:
        T3 += 1


def animacao(value):
    glutPostRedisplay()
    glutTimerFunc(30, animacao, 1)


#Funcção de Diplay
def display():
    global quadrica
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    #Açoes em todo o carro
    glPushMatrix()
    glTranslatef(T, T2, T3)

    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    visualization.draw(carro)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(1.2, 1.0, 3.0)
    visualization.draw(roda)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(-1.2, 1.0, 3.0)
    visualization.draw(roda)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(1.2, 1.0, -3.0)
    visualization.draw(roda)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(-1.2, 1.0, -3.0)
    visualization.draw(roda)
    glPopMatrix()

    glPopMatrix()
    
    #Grafico de Orientação:linhas
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(10.0, 0.0, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 10.0, 0.0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 10.0)
    glEnd()

    glutSwapBuffers()


#Função de inicialização e configuração da tela principal
def init():
    global quadrica

    glClearColor(0.3, 0.3, 0.3, 0.0)
    glShadeModel(GL_SMOOTH)#Define o sombreamento
    glClearColor(0.0, 0.1, 0.0, 0.5)
    glClearDepth(1.0)#Limpagem profunda
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, [2.0, 2.0, 1.0, 0.0])

    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


#Definindo a função principal
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(480, 480)
    glutInitWindowPosition(100, 100)
    
    #Crinado a janela
    janela = glutCreateWindow("Carro")
    
    #Chama a função para inicializar
    init()
    #Chamada a função de Callback do display
    glutDisplayFunc(display)
    #Chama a função de tempo 
    glutReshapeFunc(resize)
    glutTimerFunc(30, animacao, 1)
    #Chama uma função especial
    glutSpecialFunc(keys)
    #Looping
    glutMainLoop()

main()