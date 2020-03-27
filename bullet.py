import pygame

class Bullet():
    def __init__(self, window, player, enemy, pos_x, pos_y):
        self.window = window
        self.player = player
        self.enemy = enemy
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 2
        self.speed_x = 0
        self.speed_y = 0
        self.width = 5
        self.height = 5
        self.rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        self.active = True
    
    def fire(self):
        play_middle_x = self.player.pos_x + (self.player.width / 2)
        play_middle_y = self.player.pos_y + (self.player.height / 2)
        dist_x = play_middle_x - self.pos_x
        dist_y = play_middle_y - self.pos_y
        self.speed_x = dist_x / self.player.pos_x * 3
        self.speed_y = dist_y / self.player.pos_y * 3

    
    def update(self):
        if not self.collision() and self.within_window():
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
        else:
            self.active = False
            self.speed = 0
    
    def collision(self):
        if self.player.rect.colliderect(self.rect):
            self.player.hit()
            return True
        return False
            
    def within_window(self):
        x, y = pygame.display.get_surface().get_size()
        if (self.pos_x > 0 and self.pos_x < x) and (self.pos_y > 0 and self.pos_y < y):
            return True
        return False
    
    def draw(self):
        self.update()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        if self.active:
          pygame.draw.rect(self.window, (255, 255, 255), self.rect)
