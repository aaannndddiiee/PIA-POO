import pygame
from sys import exit

global estado_juego, columnas, filas, minas, direccion

direccion = 'C:/Users/andre/OneDrive/Desktop/5to sem/POO/JUEGOPYTHON/'

def selec_dificultad(dificultad):
    if dificultad == 'facil':
        columnas = 8
        filas = 8
    if dificultad == 'media':
        colunmas = 16
        filas = 16

def tiempo():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)


bg_color_menu = '#F18D96'
bg_color_juego = '#6DADC6'
text_color = '#56536E'

pygame.init()
start_time = 0

pygame.display.set_caption('Buscaminas')

clock = pygame.time.Clock()
game_activo = True
estado_juego = 'menu'
screen = pygame.display.set_mode((300,300))
band_primero = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_activo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print()#si es el primer click cambiar la bandera a False

    if estado_juego == 'menu':
        titulo_surf = pygame.image.load(direccion + 'Menu/Buscaminas.png').convert_alpha()
        facil_surf = pygame.image.load(direccion + 'Menu/Facil.png').convert_alpha()
        facil_surf = pygame.transform.rotozoom(facil_surf,0.0,1.5)
        medio_surf = pygame.image.load(direccion + 'Menu/Medio.png').convert_alpha()
        medio_surf = pygame.transform.rotozoom(medio_surf, 0, 1.5)
        titulo_rect = titulo_surf.get_rect(center = (150,150))
        facil_rect = facil_surf.get_rect(midbottom = (75, 250))
        medio_rect = medio_surf.get_rect(midbottom = (225,250))
        screen.blit(titulo_surf,titulo_rect)
        screen.blit(facil_surf, facil_rect)
        screen.blit(medio_surf,medio_rect)
        band_primero = True
    if estado_juego == 'jugando':
        print()
    if estado_juego == 'perder':
        print()
    if estado_juego == 'ganar':
        print()

    clock.tick(60)
    pygame.display.update()


"""tablero = Tablero.Tablero(8, 8)
tablero.iniciarTablero()
tablero.iniciarMinas(10, 0, 0)
tablero.numerosMinas()
tablero.imprimir()"""
