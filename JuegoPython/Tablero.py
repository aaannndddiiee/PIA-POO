import Casilla
from random import randint as ran

class Tablero:
    def __init__(self, nFilas, nColumnas):
        self.nFilas = nFilas
        self.nColumnas = nColumnas
        self.casillas = []

    def iniciarTablero(self):
        self.casillas = [[Casilla.Casilla(i, j, False, i * self.nColumnas + j + 1, 0) for j in range(self.nColumnas)] for i in range(self.nFilas)]

    def iniciarMinas(self, nminas, x, y):
        self.casillas[x][y].setMinasAlrededor(0)
        pos_safe = []
        sumas = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,0], [0,1], [1,-1], [1,0], [1,1]]
        for i in range(9):
            if(x + sumas[i][0] >= 0 and x + sumas[i][0] < self.nFilas):
                if(y + sumas[i][1] >= 0 and y + sumas[i][1] < self.nFilas):
                    pos_safe.append(self.casillas[x + sumas[i][0]][y + sumas[i][1]].getPos())
        while(nminas > 0):
            posx = ran(0, self.nFilas - 1)
            posy = ran(0, self.nColumnas - 1)
            if(not (self.casillas[posx][posy].getPos() in pos_safe) and not self.casillas[posx][posy].isMina()):
                self.casillas[posx][posy].setMina(True)
                nminas -= 1
    
    def casillasAdyacentes(self, fila, columna):
        pos = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for i in range(8):
            if(fila + pos[i][0] >= 0 and fila + pos[i][0] < self.nFilas):
                if(columna + pos[i][1] >= 0 and columna + pos[i][1] < self.nFilas):
                    if(not (self.casillas[fila + pos[i][0]][columna + pos[i][1]].getMina())):
                        self.casillas[fila + pos[i][0]][columna + pos[i][1]].setMinasAlrededor(1)

    def numerosMinas(self):
        for i in range(self.nFilas):
            for j in range(self.nColumnas):
                if(self.casillas[i][j].isMina()):
                    self.casillasAdyacentes(i,j)
    
    def imprimir(self):
        print("\nTABLERO:")
        for fila in self.casillas:
            for casilla in fila:
                if casilla.mina:
                    print(" X ", end="")
                else:
                    print(f" {casilla.minasAlrededor} ", end="")
            print()  # salto de línea
