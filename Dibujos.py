# Utilizar la Data inicial para funcionamiento de este archivo
# Aquí hay unos cuantos ejemplos de como implementar dibujos en la ventana

#Definiendo colores en formato RGB (Buscar más colores si es necesario)
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,255,0)
ROJO = (255,0,0)
AZUL =  (0,0,255)

# Color de fondo
# screen.fill(BLANCO)

###------ Zona de dibujo(Figuras básicas)

# Dibujar una linea
# pygame.draw.line(screen,VERDE,[0,100],[100,100],15) # [Pos inicial],[Pos final],Grosor

# Dibujar un Rectangulo
# pygame.draw.rect(screen,NEGRO, (100,100,80,80)) # (Pos X, Pos Y, Ancho, Alto)

# Dibujar un círculo
# pygame.draw.circle(screen,ROJO,(200,200),20) # (Centro), radio)

###------- Zona de dibujo

###------- Loops para dibujos
# for x in range(100, 700, 100):
#    pygame.draw.rect(screen, AZUL, (x, 230, 50, 50))

# Para actualizar la pantalla
# pygame.display.flip()