"""
-----------------------------------------------

-----------------------------------------------
"""

class Unidade:
    def __init__(self, valor, simbolo):
        self.valor = valor
        self.simbolo = simbolo

    #geter e setter valor
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        if isinstance(valor, (int, float)):
            self._valor = valor
        else:
            print("Erro, não é um numero\n")
        

    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, simbolo):
        if isinstance(simbolo, str):
            self._simbolo = simbolo
        else:
            print("Erro, não é um caractere\n")

    def mostrar_unidade(self):
        print(f'{self._valor} {self.simbolo}\n')

u1 = Unidade(1 ,'m')

u1.mostrar_unidade()
u1.valor = 10
u1.simbolo = 'km'
u1.mostrar_unidade()
u1.valor = 'm'
u1.simbolo = 10
u1.mostrar_unidade()