from pytmx.util_pygame import load_pygame
import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surface, grupo):
        super().__init__(grupo)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()
screen = pygame.display.set_mode((20*64, 12*64))
tmxdata = load_pygame('fases/fase0/setup/fase0.tmx')
sprite_group = pygame.sprite.Group()

for layer in tmxdata.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
            Tile((x*64, y*64), surf, sprite_group)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    sprite_group.draw(screen)
    pygame.display.update()