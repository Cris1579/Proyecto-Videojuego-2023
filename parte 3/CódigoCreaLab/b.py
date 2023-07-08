import pygame
import random


class Casilla:
	def __init__(self, game, x, y, TX, TY):
		self.game = game

		self.x = x
		self.y = y
		self.TX = TX
		self.TY = TY

		self.corners = [
	      (x * TX, y * TY),
	      (x * TX + TX, y * TY),
	      (x * TX + TX, y * TY + TY),
	      (x * TX, y * TY + TY),
	      (x * TX, y * TY )
	    ]

	# (Orden): Top, right, bottom, left
		self.walls = [True, True, True, True]
		self.visitada = False



	def render(self):
		if self.visitada:
			pintaVisitada = pygame.draw.rect(self.game.pantalla, self.game.verdeVISITADA,
				(self.x * self.TX, self.y * self.TY, self.TX, self.TY))

		for i in range(len(self.walls)):
			if self.walls[i]:
				self.dibujaLineaBorde(self.corners[i][0], self.corners[i][1],
					self.corners[i + 1][0], self.corners[i + 1][1])


	def check_vecinos(self):
		x = self.x
		y = self.y

		posVecinos = [
			(x, y - 1),
			(x + 1, y),
			(x, y + 1),
			(x - 1, y)
		]

		vecinos = []

		for i in range(len(posVecinos)):
			checkIndice = self.indice(posVecinos[i][0], posVecinos[i][1])

			if checkIndice != None:
				vecinoBajoCheckeo = self.game.casillas[checkIndice]

				if not vecinoBajoCheckeo.visitada:
					vecinos.append(vecinoBajoCheckeo)


		if len(vecinos) > 0:
			num_rnd = random.randrange(len(vecinos))
			return vecinos[num_rnd]

		return None


	def indice(self, x, y):
		if x < 0 or x > self.game.COLUMNAS - 1 or y < 0 or y > self.game.FILAS -1:
			return None

		return y * self.game.COLUMNAS + x


	def cursor(self):
		pintaCursor = pygame.draw.rect(self.game.pantalla,
			self.game.verdeCURSOR, (self.x * self.TX, self.y * self.TY, self.TX, self.TY))


	def dibujaLineaBorde(self, x1, y1, x2, y2):
		lineaBorde = pygame.draw.line(self.game.pantalla, self.game.paredCOLOR,
			(x1, y1), (x2, y2))
