import pygame

class Botao():
	def __init__(self, x, y, image, scale=1):
		# gera imagem do botão
		width = image.get_width()
		height = image.get_height()
		self.__image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) # escala a imagem
  
		# gera imagem do botão quando o mouse passa por cima
		self.__imagehover = pygame.transform.scale(self.__image, (int(self.__image.get_width() * 1.05), int(self.__image.get_height() * 1.05)))
		self.__rect = self.__image.get_rect()
		self.__rect.midtop = (x, y) # o botao eh posicionado no meio
		self.__clicked = False

	def draw(self, surface):
		pos = pygame.mouse.get_pos()
		
		if self.__rect.collidepoint(pos):
			botao = self.__imagehover
		else:
			botao = self.__image
   
		surface.blit(botao, (self.__rect.x, self.__rect.y))
   
	def clicado(self):
		action = False
		pos = pygame.mouse.get_pos()

		# se colidiu com o botão
		if self.__rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1: # se o botão foi ativado enquanto colidia
				self.__clicked = True
    
		if self.__clicked and pygame.mouse.get_pressed()[0] == 0: # se o botão foi desativado enquanto colidia
				self.__clicked = False
				action = True


		return action
