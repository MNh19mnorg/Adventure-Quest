import pygame
from bullet import Bullet
from random import randint

class Enemy():
    def __init__(self, window, player, pos, tile_top, tile_left, size):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.middle_x = self.pos_x + (size[0] / 2)
        self.middle_y = self.pos_y + (size[1] / 2)
        self.tile_top = tile_top
        self.tile_left = tile_left
        self.width = size[0]
        self.height = size[1]
        self.range = 100
        self.speed = 0.5
        x, y = pygame.display.get_surface().get_size()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, x * 0.2, y * 0.2)
        self.window = window
        self.player = player
        self.area = pygame.Rect( 
                                self.middle_x - self.range, 
                                self.middle_y - self.range, 
                                self.range * 2, 
                                self.range * 2
                                )
        self.bullets = list()
        self.time = 0
        self.texture = pygame.image.load("Resources/WraithR.png")
        self.texture = pygame.transform.scale(self.texture, (int(self.width), int(self.height)))
    
    def within_range(self):
        if self.player.rect.colliderect(self.area):
            return True
        return False
    
    def move(self):
        if self.player.pos_x < self.pos_x:
            self.pos_x -= self.speed
        elif self.player.pos_x > self.pos_x:
            self.pos_x += self.speed
    
    def update(self, msTime):
        time = pygame.time.get_ticks() - self.time
        self.move()
        if self.within_range() and len(self.bullets) < 50 and time > 200:
            bullet = Bullet(self.window, self.player, self, self.middle_x, self.middle_y)
            bullet.fire(msTime)
            self.bullets.append(bullet)
            self.time = pygame.time.get_ticks()
    
    def draw(self):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.middle_x = self.pos_x + (self.width / 2)
        self.middle_y = self.pos_y + (self.height / 2)
        self.area = pygame.Rect( 
                        self.middle_x - self.range, 
                        self.middle_y - self.range, 
                        self.range * 2, 
                        self.range * 2
                        )
        # pygame.draw.rect(self.window, (255, 0, 0), self.area)
        # pygame.draw.rect(self.window, (0, 0, 0), self.rect)
        self.window.blit(self.texture, (self.pos_x, self.pos_y))
        for bullet in self.bullets:
            if bullet.active == False:
                self.bullets.remove(bullet)
            else:
                bullet.draw()