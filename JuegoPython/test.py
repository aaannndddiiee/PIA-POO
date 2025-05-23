import unittest
from Tablero import Tablero as tab
from random import randint

class Tablerotest(unittest.TestCase):

    def setUp(self):
        tab.setColumnas(tab, 8)
        tab.setFilas(tab, 8)
        tab.iniciarTablero(tab)
    
    def test_noMinas(self):
        fila = randint(0,7)
        columna = randint(0,7)
        self.assertEqual(tab.casillas[fila][columna].isMina(),False,'Se estan generando minas')

    def test_pos1Safe(self):
        fila = randint(0,7)
        columna = randint(0,7)
        tab.iniciarMinas(tab,10,fila, columna)
        self.assertEqual(tab.casillas[fila][columna].isMina(), False, 'No deberia tener mina')

unittest.main()