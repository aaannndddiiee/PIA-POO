import Tablero as Tablero

import pygame
from sys import exit

class Tablero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

def tiempo():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    tiempo_surf = text_font.render()


bg_color = '#F18D96'

nivel = {10:[20,5,8],40:[10,2,16]}

pygame.init()
start_time = 0

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Buscaminas')
screen.fill(bg_color)
text_font = pygame.font.Font('font/Zain-Regulas.ttf.')

clock = pygame.time.Clock()
game_activo = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_activo:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = pygame.time.get_ticks()
    Tablero.iniciarCasillas()
    clock.tick(60)
    pygame.display.update()


"""tablero = Tablero.Tablero(8, 8)
tablero.iniciarTablero()
tablero.iniciarMinas(10, 0, 0)
tablero.numerosMinas()
tablero.imprimir()"""
