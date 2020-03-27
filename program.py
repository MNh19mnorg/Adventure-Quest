import pygame
import sys
from mapGenerator import Map_generator
from MapLoader import Map_Loader
from camera import Camera
from player import Player

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

pygame.init()

FPS = 120
clock = pygame.time.Clock()

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# generator = Map_generator(1000)
# generator.generate()
# generator.save()

font_arial = pygame.font.SysFont("Arial", 40)
gameover_label = font_arial.render("Game Over!", 1, (255,255,255))

Map = Map_Loader()
Map.load()
player = Player(surface, Map.map["size"] * 32, 100, 100, 40, 40)
camera = Camera(surface, Map, player, WINDOW_WIDTH, WINDOW_HEIGHT, 20)

while True:
    msTime = clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit() 
    player.move(keys, msTime)
    
    if player.dead:
        surface.blit(gameover_label, (100, 100))
    else:
        surface.fill((255, 255, 255))
        camera.draw(msTime)
        player.draw()
    pygame.display.update()