import pygame

#button class
class Botao():
	def __init__(self, x, y, image, scale=1):
		width = image.get_width()
		height = image.get_height()
		self.__image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.__imagehover = pygame.transform.scale(self.__image, (int(self.__image.get_width() * 1.05), int(self.__image.get_height() * 1.05)))
		self.__rect = self.__image.get_rect()
		self.__rect.topleft = (x, y)
		self.__clicked = False

	def draw(self, surface):
		#draw button on screen
		pos = pygame.mouse.get_pos()
		
		if self.__rect.collidepoint(pos):
			botao = self.__imagehover
		else:
			botao = self.__image
   
		surface.blit(botao, (self.__rect.x, self.__rect.y))
   
	def clicado(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.__rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.__clicked == False:
				self.__clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.__clicked = False

		return action
