import pygame

class Tile():
    def __init__(self, window, texture, pos_x, pos_y, width, height):
        self.window = window
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (int(width), int(height)))
        self.rect = self.texture.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self):
        self.window.blit(self.texture, (self.pos_x, self.pos_y))