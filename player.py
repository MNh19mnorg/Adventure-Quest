import pygame

class Player():
    def __init__(self, window, map_size, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map_size = map_size
        self.map_pos_x = pos_x
        self.map_pos_y = pos_y
        x, y = pygame.display.get_surface().get_size()
        self.width = int(x * 0.03)
        self.height = int(y * 0.03)
        self.speed = 6
        self.health = 3
        self.dead = False
        self.window = window
        self.texture = pygame.image.load("Player/MS0.png")
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.left_texture = ["L0.png", "L1.png", "L2.png"]
        self.right_texture = ["D0.png", "D1.png", "D2.png"]
        self.down_texture = ["MS0.png", "MS1.png", "MS2.png"]
        self.up_texture = ["W0.png", "W1.png", "W2.png"]
        self.last_texture = "Player/MS0.png"
    
    def move(self, keys, time):    
        self.speed = time * 0.1
                    
        if keys[pygame.K_DOWN]:
            if not self.outside_window(0, self.rect.bottom + self.speed):
                self.pos_y += self.speed
                self.choose_texture(self.down_texture)
            if not self.outside_map(0, self.map_pos_y + self.speed):
                self.map_pos_y += self.speed       
        
        elif keys[pygame.K_UP]:
            if not self.outside_window(0, self.pos_y - self.speed):
                self.pos_y -= self.speed 
                self.choose_texture(self.up_texture)
            if not self.outside_map(0, self.map_pos_y - self.speed):
                self.map_pos_y -= self.speed       

        elif keys[pygame.K_RIGHT]:
            if not self.outside_window(self.rect.right + self.speed, 0):
                self.pos_x += self.speed 
                self.choose_texture(self.right_texture)
            if not self.outside_map(self.map_pos_x + self.speed, 0):
                self.map_pos_x += self.speed  
                
        elif keys[pygame.K_LEFT]:
            if not self.outside_window(self.pos_x - self.speed, 0):
                self.pos_x -= self.speed 
                self.choose_texture(self.left_texture)
            if not self.outside_map(self.map_pos_x - self.speed, 0):
                self.map_pos_x -= self.speed           

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.dead = True

    def choose_texture(self, textures):
        path = "Player/"
        if self.last_texture == textures[2]:
            self.texture = pygame.image.load(path + textures[1])
            self.last_texture = textures[1]
        else:
            self.texture = pygame.image.load(path + textures[2])
            self.last_texture = textures[2]
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))
                
    def outside_window(self, new_x, new_y):
        x, y = pygame.display.get_surface().get_size()
        if (new_x >= 0 and new_x <= x) and (new_y >= 0 and new_y <= y):
            return False
        return True
    
    def outside_map(self, new_x, new_y):
        size = self.map_size
        if (new_x >= 0 and new_x <= size) and (new_y >= 0 and new_y <= size):
            return False
        return True
    
    def draw(self):
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.window.blit(self.texture, (self.pos_x, self.pos_y))