import pygame
import random
import math
from pygame import mixer


#Importa todos los metodos de la libreria
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))


#Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono=pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("espacio.png")

#agregar musica de fondo
mixer.music.load('darth_vader.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1) #-1 para que se repita cada vez que se termine

#Variables del Jugador
img_jugador = pygame.image.load("nave-espacial.png")
jugador_x=368 #aparece en la mitad
jugador_y=500 #aparece abajo
jugador_x_cambio=0


#Variables del enemigo
img_enemigo = []
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio= []
enemigo_y_cambio= []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("astronave.png"))
    enemigo_x.append(random.randint(0,736)) #aparece en la mitad
    enemigo_y.append(random.randint(50,200)) #aparece abajo
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(40)

#Variables de la bala del jugador
img_bala = pygame.image.load("bala.png")
bala_x=0 #aparece en la mitad
bala_y=500 #aparece abajo
bala_x_cambio= 0
bala_y_cambio= 3
bala_visible=False 

#puntaje
puntaje=0 
fuente=pygame.font.Font('freesansbold.ttf', 32)
texto_x= 10
texto_y = 10


#texto final del juego
fuente_final=pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final=fuente_final.render("JUEGO TERMINADO", True,(255,255,255))
    pantalla.blit(mi_fuente_final, (80,200))
    


#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto,(x,y))

#Funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y)) #blit arroja la imagen en la pantalla


#Funcion del enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y)) #blit arroja la imagen en la pantalla

#funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x+16, y+10))
    

#funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia=math.sqrt(math.pow(x_1-x_2, 2)+math.pow(y_2-y_1, 2))
    if distancia<27:
        return True
    else:
        return False


#loop del juego
se_ejecuta=True
while se_ejecuta:
    
    #Imagen de fondo
    #pantalla.fill((205, 144, 228))
    pantalla.blit(fondo,(0,0))
    
    
    #Iterar eventos
    for evento in pygame.event.get():
        
        #Evento cerrar
        if evento.type == pygame.QUIT: #QUIT es cuando se da en la X
            se_ejecuta = False
        
        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala=mixer.Sound('disparo_laser.mp3')
                sonido_bala.play()
                if bala_visible==False:
                    bala_x=jugador_x
                    disparar_bala(bala_x, bala_y)
            
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio=0
    
    #Modificar posición del jugador
    jugador_x += jugador_x_cambio
    
    #Mantener dentro de bordes al jugador
    if jugador_x<=0:
        jugador_x=0
    elif jugador_x >=736:
        jugador_x=736
        
    #Modificar posición del enemigo
    for e in range(cantidad_enemigos):
        
        #fin del juego
        if enemigo_y[e]>500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break
        
        
        enemigo_x[e] += enemigo_x_cambio[e]
    
    #Mantener dentro de bordes al enemigo
        if enemigo_x[e]<=0:
            enemigo_x_cambio[e]=0.2
            enemigo_y[e] +=enemigo_y_cambio[e]
        elif enemigo_x[e] >=736:
            enemigo_x_cambio[e]=-0.2
            enemigo_y[e] +=enemigo_y_cambio[e]
            
            
        #colision
        colision=hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            sonido_colision=mixer.Sound('colision.mp3')
            sonido_colision.play()
            bala_y=500
            bala_visible= False
            puntaje +=1
            #print(puntaje)
            #si lo impacta debe aparecer en otro lugar
            enemigo_x[e]=random.randint(0,736) #aparece en la mitad
            enemigo_y[e]=random.randint(50,200) #aparece abajo
            
        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    #Movimiento bala
    if bala_y <= -64:# La bala tiene 64 bits, cuando ya desaparezca de la vista en la posición 0 en Y
        bala_y=500
        bala_visible=False
        
    if bala_visible == True:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio
        
    
    jugador(jugador_x, jugador_y) #posiciona el personaje en la pantalla
    
    mostrar_puntaje(texto_x, texto_y)
    
    #Actualizar pantalla
    pygame.display.update() #Actualiza el color de la pantalla