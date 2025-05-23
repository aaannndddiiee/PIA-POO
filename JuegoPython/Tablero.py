import Casilla
from random import randint as ran

class Tablero:
    def __init__(self):
        self.casillas = []

    def setColumnas(self,columnas):
        self.nColumnas = columnas
    
    def setFilas(self, filas):
        self.nFilas = filas

    #Incia la matriz
    def iniciarTablero(self):
        self.casillas = [[Casilla.Casilla(i, j, False, i * self.nColumnas + j + 1, 0) for j in range(self.nColumnas)] for i in range(self.nFilas)]

    #Coloca las mina de manera aleatoria en el tablero, evitando, la primera casilla clickeada y sus adyacentes
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
                self.casillas[posx][posy].setMinasAlrededor(10)
                nminas -= 1
    
    #Coloca numeros en todas las casillas adyacentes a una mina
    def casillasAdyacentes(self, fila, columna):
        pos = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for i in range(8):
            if(fila + pos[i][0] >= 0 and fila + pos[i][0] < self.nFilas):
                if(columna + pos[i][1] >= 0 and columna + pos[i][1] < self.nFilas):
                    if(not (self.casillas[fila + pos[i][0]][columna + pos[i][1]].getMina())):
                        self.casillas[fila + pos[i][0]][columna + pos[i][1]].setMinasAlrededor(1)
    
    #Recorre las casillas hasta que una tenga mina
    def numerosMinas(self):
        for i in range(self.nFilas):
            for j in range(self.nColumnas):
                if(self.casillas[i][j].isMina()):
                    self.casillasAdyacentes(self,i,j)
    
    #Imprime el tablero, con numeros y x en donde hay minas
    def imprimir(self):
        print("\nTABLERO:")
        for fila in self.casillas:
            for casilla in fila:
                if casilla.mina:
                    print(" X ", end="")
                else:
                    print(f" {casilla.minasAlrededor} ", end="")
            print() 
