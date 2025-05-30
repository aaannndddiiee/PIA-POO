class Casilla:
    def __init__(self, fila, columna, mina, pos, minasAlrededor):
        self.fila = fila
        self.columna = columna
        self.mina = mina
        self.pos = pos
        self.minasAlrededor = minasAlrededor
        self.visible = False
        self.bandera = False

    #Metodos para obtener si la casilla tiene mina, colocar mina, obtener, colocar posiciones; obtener, colocar numeros; 
    #saber si es visible, hacerla visible; colocar bandera, obtener bandera
    def isMina(self):
        return self.mina
    
    def setMina(self, mina):
        self.mina = mina
    
    def getMina(self):
        return self.mina

    def getPos(self):
        return self.pos
    
    def setPos(self, pos):
        self.pos = pos
    
    def getMinasAlrededor(self):
        return self.minasAlrededor
    
    def setMinasAlrededor(self, minasAlrededor):
        self.minasAlrededor += minasAlrededor
    
    def isVisible(self):
        return self.visible
    
    def setVisible(self, visible):
        self.visible = visible

    def isBandera(self):
        return self.bandera
    
    def setBandera(self, bandera):
        self.bandera = bandera
    
    def getBandera(self):
        return self.bandera
