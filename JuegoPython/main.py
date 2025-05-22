import pygame
from sys import exit
from Tablero import Tablero as tab

direccion = 'C:/Users/andre/OneDrive/Desktop/5to sem/POO/JUEGOPYTHON/'

#donde tengo cuantas colunmas filas minas y el tamaño de la ventana
def selec_dificultad(dificultad):
    global ancho
    global alto
    global columnas
    global filas
    global minas
    if dificultad == 'facil':
        ancho = 295
        alto = 350
        columnas = 8
        filas = 8
        minas = 10
    if dificultad == 'media':
        ancho = 575
        alto = 620
        columnas = 16
        filas = 16
        minas = 40
    screen = pygame.display.set_mode((ancho,alto))
    screen.fill(bg_color_juego)

def ventana_default():
    #pantalla usada para el menu, ganar, perder
    screen = pygame.display.set_mode((300,300))

def tiempo():
    tiempo_surf = pygame.image.load(direccion + 'Jugando/tempo_azul.png')
    tiempo_surf = pygame.transform.rotozoom(tiempo_surf, 0, 1.2)
    tiempo_rect = tiempo_surf.get_rect(midbottom =(100, abs(20-alto)) )
    screen.blit(tiempo_surf,tiempo_rect)
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)


def revelar_casillas_ady(tab, x, y):
    #fuera de los limites
    if x < 0 or x >= filas or y < 0 or y >= columnas:
        return
    #para no revelar donde hay bandera o ya es visible
    if tab.casillas[x][y].getBandera():
        return
    if tab.casillas[x][y].isVisible():
        return
    
    #revelando la casilla
    tab.casillas[x][y].setVisible(True)
    minas_alrededor = tab.casillas[x][y].getMinasAlrededor()
    num_surf = pygame.image.load(direccion + f'Jugando/{minas_alrededor}.png')
    screen.blit(num_surf, (y * (celdas + sep) + 10, x * (celdas + sep) + 10))

    #continua revelando casillas hasta que llegue a donde hay adyacentes con minas
    #utilizando recursividad (waos)
    if minas_alrededor == 0:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i != 0 or j != 0:
                    revelar_casillas_ady(tab, x + i, y + j)


def explotar():
    print()

def flores():
    print()

#Colores 
bg_color_menu = '#F18D96'
bg_color_juego = '#6DADC6'
text_color = '#56536E'
detalles_blanco = '#E8DED4'
perder = '#168AB6'
ganar = '#E6AD37'

#Inciando la ventana y tiempo
pygame.init()
pygame.display.set_caption('Buscaminas')
screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()
start_time = 0

#Variables para el juego
estado_juego = 'menu'
primer_click = True
game_activo = False
tablero_inciado = False
banderas_correctas = []
banderas = 0
n_banderas = 0
fila = 0
col = 0
perder = False

#Tablero
tablero = tab

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                estado_juego = 'ganar'
                game_activo = False
                ventana_default()
            if event.key == pygame.K_p:
                estado_juego = 'perder'
                game_activo = False
                ventana_default()
        if game_activo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                x,y = pygame.mouse.get_pos() 
                col = (x - 10) // (celdas + sep)
                fila = (y - 10) // (celdas + sep)
                if mouse_presses:
                    if primer_click:
                        tab.iniciarMinas(tab, minas, fila, col)
                        tab.numerosMinas(tab)
                        tab.imprimir(tab)
                        primer_click = False
                        revelar_casillas_ady(tab,fila,col)
                    elif tab.casillas[fila][col].getMina():
                        perder = True
                    else:
                        revelar_casillas_ady(tab,fila,col)
                else: 
                    if tab.casillas[fila][col].getBandera():
                        tab.casillas[fila][col].setBandera(False)
                        if tab.casillas[fila][col].getMina():
                            banderas -= 1
                            banderas_correctas.pop()
                    else:
                        tab.casillas[fila][col].setBandera(True)
                        if tab.casillas[fila][col].getMina():
                            banderas_correctas.append(1)
                            banderas += 1
        if not game_activo and estado_juego == 'menu':
            if event.type == pygame.MOUSEBUTTONUP:
                if facil_rect.collidepoint(event.pos):
                    estado_juego = 'jugando'
                    celdas = 30
                    sep = 5
                    game_activo = True
                    tablero_inciado = False
                    primer_click = True
                    selec_dificultad('facil')
                if medio_rect.collidepoint(event.pos):
                    estado_juego = 'jugando'
                    celdas = 30
                    sep = 5
                    game_activo = True
                    tablero_inciado = False
                    primer_click = True
                    selec_dificultad('media')
        if not game_activo and estado_juego == 'perder':
            if event.type == pygame.MOUSEBUTTONUP:
                if remenu_rect.collidepoint(event.pos):
                    estado_juego = 'menu'
                    ventana_default()
        if not game_activo and estado_juego == 'ganar':
            if event.type == pygame.MOUSEBUTTONUP:
                if ganmenu_rect.collidepoint(event.pos):
                    estado_juego = 'menu'
                    ventana_default()
    if estado_juego == 'menu':
        titulo_surf = pygame.image.load(direccion + 'Menu/Buscaminas.png').convert_alpha()
        facil_surf = pygame.image.load(direccion + 'Menu/Facil.png').convert_alpha()
        facil_surf = pygame.transform.rotozoom(facil_surf,0,1.5)
        medio_surf = pygame.image.load(direccion + 'Menu/Medio.png').convert_alpha()
        medio_surf = pygame.transform.rotozoom(medio_surf, 0, 1.5)
        titulo_rect = titulo_surf.get_rect(center = (150,150))
        facil_rect = facil_surf.get_rect(midbottom = (75, 250))
        medio_rect = medio_surf.get_rect(midbottom = (225,250))
        screen.blit(titulo_surf,titulo_rect)
        screen.blit(facil_surf, facil_rect)
        screen.blit(medio_surf,medio_rect)
        primer_click = True
        banderas_correctas.clear()
        banderas = 0
        n_banderas = 0
        perder = False
    if estado_juego == 'perder':
        perder_surf = pygame.image.load(direccion+ 'Perder/perder_fondo.png').convert_alpha()
        perder_rect = perder_surf.get_rect(center = (150,150))
        calavera_surf = pygame.image.load(direccion + 'Perder/calavera.png').convert_alpha()
        calavera_surf = pygame.transform.rotozoom(calavera_surf,0,2.3)
        calavera_rect = calavera_surf.get_rect(center = (170,150))
        remenu_surf = pygame.image.load(direccion + 'Perder/menu.png').convert_alpha()
        remenu_surf = pygame.transform.rotozoom(remenu_surf,0,1.5)
        remenu_rect = remenu_surf.get_rect(center = (150, 250))
        screen.blit(perder_surf, perder_rect)
        screen.blit(calavera_surf, calavera_rect)
        screen.blit(remenu_surf, remenu_rect)
    if estado_juego == 'ganar':
        gantiempo_surf = pygame.image.load(direccion + 'Ganar/tiempo_ganar.png')
        ganmenu_surf = pygame.image.load(direccion + 'Ganar/menu_ganar.png')
        gantiempo_rect = gantiempo_surf.get_rect(midbottom = (75, 250))
        ganmenu_rect = ganmenu_surf.get_rect(midbottom = (225, 250))
        screen.blit(gantiempo_surf, gantiempo_rect)
        screen.blit(ganmenu_surf, ganmenu_rect)
    if game_activo:
        if estado_juego == 'jugando':
            tiempo()
        if not tablero_inciado:
            tab.setColumnas(tab,columnas)
            tab.setFilas(tab, filas)
            tab.iniciarTablero(tab)
            tab.imprimir(tab)
            tablero_inciado = True
            for i in range(filas):
                for j in range(columnas):
                    pygame.draw.rect(screen, detalles_blanco,pygame.Rect(j*(celdas + sep)+10, i*(celdas+sep)+10, 30, 30))
        else:
            if tab.casillas[fila][col].getMina():
                explotar()
                estado_juego = 'perder'
                game_activo = False
            if tab.casillas[fila][col].getBandera():
                print()
            if banderas < n_banderas:
                pygame.draw.rect(screen,detalles_blanco, pygame.Rect((col*(celdas + sep) + 10, fila*(celdas + sep) + 10), 30,30))
            n_banderas = banderas

    clock.tick(60)
    pygame.display.update()


"""tablero = Tablero.Tablero(8, 8)
tablero.iniciarTablero()
tablero.iniciarMinas(10, 0, 0)
tablero.numerosMinas()
tablero.imprimir()"""
