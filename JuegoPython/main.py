import pygame
#https://www.pygame.org/docs/
from sys import exit
from Tablero import Tablero as tab
import time

#Direccion del proyecto
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

   #pantalla usada para el menu, ganar, perder

#Funcion para redimensionar la ventana para el menu, perder y ganar
def ventana_default():
    screen = pygame.display.set_mode((300,300))

#cronometro, se activa cuando se da el primer click
def tiempo():
    #Imagen de tiempo
    tiempo_surf = pygame.image.load(direccion + 'Jugando/tempo_azul.png')
    tiempo_surf = pygame.transform.rotozoom(tiempo_surf, 0, 1.2)
    tiempo_rect = tiempo_surf.get_rect(midbottom =(100, abs(20-alto)) )
    screen.blit(tiempo_surf,tiempo_rect)
    #Si aun no han clickeado en una casilla, se mantiene en cero
    if primer_click:
        current_time = 0
    else:
        #Comienza el conteo
        current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    #Imprimir en la ventana el tiempo
    tiem = text_font.render(f'{current_time}', False, detalles_blanco)
    pygame.draw.rect(screen, bg_color_juego, (150, abs(56 - alto), 50, 50))
    screen.blit(tiem, (155, abs(60 - alto )))
    return current_time

#revelar casillas adyacentes a la clickeada
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
    #asi solo revelara 0 y se detendra cuando encuentre numeros, por lo que no revelara minas
    if minas_alrededor == 0:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                #Evitando la casilla central
                if i != 0 or j != 0:
                    #Llamando la funcion de nuevo para la casilla adyacente
                    revelar_casillas_ady(tab, x + i, y + j)

#funcion para imprimir todas las minas (perder)
def explotar():
    #Imprimira en las casillas con minas, la imagen de una mina
    mina_surf = pygame.image.load(direccion + 'Perder/mina.png')
    for i in range(filas):
        for j in range(columnas):
            if tab.casillas[i][j].getMina():
                mina_rect = mina_surf.get_rect(topleft = (j*(celdas + sep)+10, i*(celdas+sep)+10))
                screen.blit(mina_surf, mina_rect)
    pygame.display.update()

#funcion para imprimir las flores(ganar)
def flores():
    #Imprimira en las casillas con minas, la imagen de una flor
    flor_surf = pygame.image.load(direccion + 'Ganar/flor_ganar.png')
    for i in range(filas):
        for j in range(columnas):
            if tab.casillas[i][j].getMina():
                flor_rect = flor_surf.get_rect(topleft = (j*(celdas + sep)+10, i*(celdas+sep)+10))
                screen.blit(flor_surf, flor_rect)
    pygame.display.update()

#Colores (ya que utilice Figma  y Pixilart para la mayoria de las cosas algunos colores no se usaran
#aun asi, me sirve para modificicaciones)
bg_color_menu = '#F18D96'
bg_color_juego = '#6DADC6'
detalles_oscuro = '#56536E'
detalles_blanco = '#E8DED4'
bg_color_perder = '#168AB6'
gb_color_ganar = '#E6AD37'

#Inciando la ventana y tiempo
pygame.init()
#Titlo de la ventana
pygame.display.set_caption('Buscaminas')
#inicializo la ventana para el menu
screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()
#Fuente utilizada para el reloj, en Figma utilice la fuente Micro5-Regular
text_font = pygame.font.Font(direccion + 'font/Tiny5-Regular.ttf', 40)

#Variables para el juego, banderas y contadores
estado_juego = 'menu'
primer_click = True
game_activo = False
tablero_inciado = False
#Crecera si se colocan banderas en donde hay minas, asi se que han ganado
banderas_correctas = []
#Banderas colocadas correctas o no
banderas = 0
#Utilizo este contador para dibujar las banderas si se agregaron o si se quitaron
n_banderas = 0
#Posicion de las casillas clickeadas
fila = 0
col = 0

#Tablero
tablero = tab

while True:
    for event in pygame.event.get():
        #Salir del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Atajos
        if event.type == pygame.KEYDOWN:
            #Para ganar
            if event.key == pygame.K_g:
                #Imprimo flores y muevo mi estado a 'ganar'
                estado_juego = 'ganar'
                game_activo = False
                flores()
                tiempo_ganar = tiempo()
                time.sleep(3)
                ventana_default()
            #Para perder
            if event.key == pygame.K_p:
                #imprimo bombas y muevo mi estado a 'perder'
                estado_juego = 'perder'
                game_activo = False
                explotar()
                time.sleep(3)
                ventana_default()
        if game_activo:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #click izquierdo o derecho
                mouse_presses = pygame.mouse.get_pressed()
                x,y = pygame.mouse.get_pos() 
                #indices para acceder a la matriz de casillas en mi Tablero
                col = (x - 10) // (celdas + sep)
                fila = (y - 10) // (celdas + sep)
                #Click izquierdo
                if mouse_presses[0]:
                    #Si es el primer click
                    if primer_click:
                        #Comienza mi reloj
                        start_time = pygame.time.get_ticks()
                        #las minas se generan despues del primer click
                        tab.iniciarMinas(tab, minas, fila, col)
                        tab.numerosMinas(tab)
                        #tab.imprimir(tab)
                        primer_click = False
                        #Revelar casillas adyacentes a mi primer click
                        revelar_casillas_ady(tab,fila,col)
                        #Click en una mina
                    #Si la casilla tiene mina, pierdo
                    elif tab.casillas[fila][col].getMina():
                        estado_juego = 'perder'
                        game_activo = False
                        explotar()
                        #Timepo para observar las posiciones de las minas
                        time.sleep(3)
                        ventana_default()
                    else:
                        #click en casilla cualquiera
                        revelar_casillas_ady(tab,fila,col)
                #Click derecho
                if mouse_presses[2] and not tab.casillas[fila][col].isVisible():
                    #click derecho = quitar / colocar bandera 
                    #Si la casilla ya tenia bandera la retiro
                    if tab.casillas[fila][col].getBandera():
                        tab.casillas[fila][col].setBandera(False)
                        #contador para quitar o agregar banderas(imagen)
                        banderas -= 1
                        if tab.casillas[fila][col].getMina():
                            #si en donde hay una mina se quita una bandera se resta de banderas correctas
                            banderas_correctas.pop()
                    else:
                        #Si la casilla no tenia bandera
                        tab.casillas[fila][col].setBandera(True)
                        banderas += 1
                        #Si la casilla tiene una mina
                        if tab.casillas[fila][col].getMina():
                            #si en donde hay una bandera hay mina se agrega a banderas correctas
                            banderas_correctas.append(1)
                #Ganar cuando todas las minas esten abanderadas
            if len(banderas_correctas) == minas and len(banderas_correctas) > 1:
                game_activo = False
                estado_juego = 'ganar'
                flores()
                #El tiempo que tomo ganar, se imprime en la pantalla de ganar
                tiempo_ganar = tiempo()
                #Tiempo para observar las flores
                time.sleep(3)
                ventana_default()
        if not game_activo and estado_juego == 'menu':
            if event.type == pygame.MOUSEBUTTONUP:
                #Seleccion de dificultad
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
            #Regresar a menu
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
        #Ventana del Menu, titulos, fondo, imagen y dificultades
        titulo_surf = pygame.image.load(direccion + 'Menu/Buscaminas.png').convert_alpha()
        facil_surf = pygame.image.load(direccion + 'Menu/Facil.png').convert_alpha()
        facil_surf = pygame.transform.rotozoom(facil_surf,0,1.5)
        medio_surf = pygame.image.load(direccion + 'Menu/Medio.png').convert_alpha()
        medio_surf = pygame.transform.rotozoom(medio_surf, 0, 1.5)
        flor_menu_surf = pygame.image.load(direccion + 'Menu/flor_inicio.png').convert_alpha()
        flor_menu_surf = pygame.transform.rotozoom(flor_menu_surf, 0, 1.5)
        titulo_rect = titulo_surf.get_rect(center = (150,150))
        facil_rect = facil_surf.get_rect(midbottom = (75, 250))
        medio_rect = medio_surf.get_rect(midbottom = (225,250))
        flor_menu_rect = flor_menu_surf.get_rect(center = (150,150))
        screen.blit(titulo_surf,titulo_rect)
        screen.blit(facil_surf, facil_rect)
        screen.blit(medio_surf,medio_rect)
        screen.blit(flor_menu_surf, flor_menu_rect)
        #Regresar contadores y banderas
        primer_click = True
        banderas_correctas.clear()
        banderas = 0
        n_banderas = 0
        perder = False
    if estado_juego == 'perder':
        #Ventana de perder titulo, imagen, menu
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
        #Ventana de ganar, titulo, imagen, menu y tiempo
        ganar_surf = pygame.image.load(direccion + 'Ganar/ganar_titulo.png')
        gantiempo_surf = pygame.image.load(direccion + 'Ganar/tiempo_ganar.png')
        ganmenu_surf = pygame.image.load(direccion + 'Ganar/menu_ganar.png')
        carita_surf = pygame.image.load(direccion + 'Ganar/cara_feliz.png')
        carita_surf = pygame.transform.rotozoom(carita_surf, 0, 2.1)
        tiempo_ganar_surf = text_font.render(f'{tiempo_ganar}', False, detalles_blanco)
        ganar_rect = ganar_surf.get_rect(center = (150,150))
        gantiempo_rect = gantiempo_surf.get_rect(midbottom = (75, 250))
        ganmenu_rect = ganmenu_surf.get_rect(midbottom = (225, 250))
        carita_rect = carita_surf.get_rect(center = (150,150))
        screen.blit(ganar_surf, ganar_rect)
        screen.blit(gantiempo_surf, gantiempo_rect)
        screen.blit(tiempo_ganar_surf, (80, 250))
        screen.blit(ganmenu_surf, ganmenu_rect)
        screen.blit(carita_surf, carita_rect)
    #Si estamos jugando
    if game_activo:
        if estado_juego == 'jugando':
            tiempo()
            if not tablero_inciado:
                #Iniciar la matriz en ceros
                tab.setColumnas(tab,columnas)
                tab.setFilas(tab, filas)
                tab.iniciarTablero(tab)
                #tab.imprimir(tab)
                tablero_inciado = True
                for i in range(filas):
                    for j in range(columnas):
                        #Dibujar las casillas
                        pygame.draw.rect(screen, detalles_blanco,pygame.Rect(j*(celdas + sep)+10, i*(celdas+sep)+10, 30, 30))
            else:
                #Si se ha colocado una bandera
                if tab.casillas[fila][col].getBandera():
                    bandera_surf = pygame.image.load(direccion + 'Jugando/bandera.png')
                    screen.blit(bandera_surf, (col * (celdas + sep) + 10, fila * (celdas + sep) + 10))
                #Si se ha quitado una bandera
                if banderas < n_banderas:
                    pygame.draw.rect(screen,detalles_blanco, pygame.Rect(col*(celdas + sep) + 10, fila*(celdas + sep) + 10, 30,30))
                n_banderas = banderas
    #Controlar los frames
    clock.tick(60)
    #Actualizaz la pantalla
    pygame.display.update()