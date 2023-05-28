#EJEMPLO DE UN MOVIMIENTO Y ROTACIÓN DE UNA NAVE
#CÓDIGO CONSEGUIDO DE UN VIDEO TUTORIAL

import pygame

pygame.init()
width=1280;height=720 #TAMAÑO VENTANA
red=(255,0,0);green=(0,255,0);blue=(0,0,255);white=(255,255,255);black=(0,0,0);yellow=(255,255,0);orange=(255,128,0)
window=pygame.display.set_mode((width,height))
#window=pygame.display.set_mode((width,height),pygame.FULLSCREEN)  #Con esto, se pone en pantalla completa la ventana
clock = pygame.time.Clock()
# Definicion de las variables(Datos)
x1=100;y1=100;x2=650;y2=500
x2v=0;y2v=0  #Velocidad

#DIBUJO DE NAVE HACIA ARRIBA
def naveUP(surface,x,y):
    pygame.draw.rect(window,red,(x2,y2,60,60))
    pygame.draw.rect(window,black,(x2,y2,15,30))
    pygame.draw.rect(window,black,(x2+45,y2,15,30))

#DIBUJO DE NAVE HACIA ABAJO
def naveDOWN(surface,x,y):
    pygame.draw.rect(window,blue,(x,y,60,60))
    pygame.draw.rect(window,black,(x,y+30,15,30))
    pygame.draw.rect(window,black,(x+45,y+30,15,30))

    # DIBUJO DE NAVE HACIA LA DERECHA
def naveRIGHT(surface,x,y):
    pygame.draw.rect(window,yellow,(x,y,60,60))
    pygame.draw.rect(window,black,(x+30,y,30,15))
    pygame.draw.rect(window,black,(x+30,y+45,30,15))

    # DIBUJO DE NAVE HACIA LA IZQUIERDA
def naveLEFT(surface,x,y):
    pygame.draw.rect(window,yellow,(x,y,60,60))
    pygame.draw.rect(window,black,(x,y,30,15))
    pygame.draw.rect(window,black,(x,y+45,30,15))
direction="LEFT"    #Dirección inicial de la nave, como aparece al iniciar este archivo
run=True
while run:
    clock.tick(60)# for all the window!
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_q:
                run=False
             if event.key==pygame.K_ESCAPE:
                run=False
             if event.key==pygame.K_RIGHT:
                direction="RIGHT"
                x2v=10
             if event.key==pygame.K_LEFT:
                direction="LEFT"
                x2v=-10
             if event.key==pygame.K_UP:
                direction="UP"
                y2v=-10
             if event.key==pygame.K_DOWN:
                direction="DOWN"
                y2v=10
        if event.type==pygame.KEYUP:
             if event.key==pygame.K_RIGHT:
                x2v=0
             if event.key==pygame.K_LEFT:
                x2v=-0
             if event.key==pygame.K_UP:
                y2v=-0
             if event.key==pygame.K_DOWN:
                y2v=0
   # Logica:
    x1+=5
    if x1>width: x1=-60
    x2+=x2v;y2+=y2v
    # Dibujos
    window.fill(black)#si se omite orange solo crece no se traslada
    pygame.draw.rect(window,orange,(x1,y1,60,60))
    if direction=="UP":
       naveUP(window,x2,y2)
    elif direction=="DOWN":
       naveDOWN(window,x2,y2)
    elif direction=="RIGHT":
       naveRIGHT(window,x2,y2)
    elif direction=="LEFT":
       naveLEFT(window,x2,y2)

    pygame.display.update()

pygame.quit()