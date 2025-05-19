import Tablero

if __name__ == "__main__":
    tablero = Tablero.Tablero(8, 8)
    tablero.iniciarTablero()
    tablero.iniciarMinas(63, 0, 0)
    tablero.numerosMinas()
    tablero.imprimir()
