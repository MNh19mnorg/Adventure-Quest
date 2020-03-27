import pygame
import json
from player import Player
from tile import Tile
from enemy import Enemy
from random import randint

class Camera():
    def __init__(self, window, map_loader, player, screen_width, screen_height, size):
        self.window = window
        self.loader = map_loader
        self.player = player
        self.redraw_distance = 10
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.texture_width = screen_width / self.size
        self.texture_height = screen_height / self.size
        self.map_size = map_loader.map["size"]
        self.current_map = list()
        self.tiles = list()
        self.first_frame = True
        
        self.outside = False
        self.enemies = list()
        self.top = 0
        self.bottom = self.size
        self.left = 0
        self.right = self.size
    
    def section(self):
        Map = self.loader.map["map"]

         # Deletes the old map
        self.current_map = list()
        
        spawn_enemy = True
        for enemy in self.enemies:
            if enemy.tile_top == self.top and enemy.tile_left == self.left: 
                spawn_enemy = False
        if spawn_enemy and randint(1, 2) == 1:
            self.enemies.append(Enemy(self.window, self.player, (self.screen_width / 2, self.screen_height / 2), self.top, self.left, (self.texture_width, self.texture_width)))
        
        count_y = 0
        for index, y in enumerate(range(self.top, self.bottom)):
            vertical = Map[f"row: {y}"][self.left: self.right]            
            for i, x in enumerate(vertical):
                self.current_map.append((i * self.texture_width, count_y * self.texture_height, x))
            count_y += 1
        self.generate()
    
    def generate(self):
        self.tiles = list()
        for pos_x, pos_y, texture in self.current_map:
            new_tile = Tile(
                self.window, 
                self.load_texture(texture), 
                pos_x, pos_y, 
                self.texture_width, 
                self.texture_height)
            self.tiles.append(new_tile)
    
    # Load from textures.json
    def load_texture(self, value):
        with open("texture.json") as f:
            data = json.load(f)
            return str(f"Resources/{data[value]}")
        
    def draw(self, msTime):
        if self.first_frame:
            self.section()
            self.first_frame = False
        elif self.player_outside():
            self.section()    
           
        for tile in self.tiles:
            tile.draw()
        for enemy in self.enemies:
            if enemy.tile_top == self.top and enemy.tile_left == self.left:
                enemy.update(msTime)
                enemy.draw()
    
    def player_outside(self):
        x, y = pygame.display.get_surface().get_size()
        respawn_pos_x = x - self.redraw_distance
        respawn_pos_y = y - self.redraw_distance
        if self.player.pos_x > x - self.redraw_distance - 30 and self.right != self.map_size:
            self.player.pos_x = self.redraw_distance
            self.update_drawing(0, 0, 1, 1)
            return True
        elif self.player.pos_x < 0 + self.redraw_distance and self.left != 0:
            self.player.pos_x = respawn_pos_x - 50
            self.update_drawing(0, 0, -1, -1)
            return True
        elif self.player.pos_y > y - self.redraw_distance - 30 and self.bottom != self.map_size:
            self.player.pos_y = self.redraw_distance  + 30
            self.update_drawing(1, 1, 0, 0)
            return True
        elif self.player.pos_y < 0 + self.redraw_distance and self.top != 0:
            self.player.pos_y = respawn_pos_y - 50
            self.update_drawing(-1, -1, 0, 0)
            return True
    
    def update_drawing(self, top, bottom, left, right):
        if self.top + (top * self.size) >= 0:
            self.top += top * self.size
        else:
            self.top = 0
        if self.bottom + (bottom * self.size) <= self.map_size:
            self.bottom += bottom * self.size
        else:
            self.bottom = 0
        if self.left + (left * self.size) >= 0:
            self.left += left * self.size
        else:
            self.left = 0
        if self.right + (right * self.size) <= self.map_size:
            self.right += right * self.size
        else:
            self.right = 0