import pygame
import json

class Map_generator():
    def __init__(self, size):
        self.size = size
        self.tiles = dict()
        self.file = dict()
        self.file["size"] = (size)
        self.file["number of tiles"] = (size * size)
        
    def generate(self):
        for y in range(self.size):
            new_list = list()
            for x in range(self.size):
                new_list.append("g")
            self.tiles[f"row: {y}"] = new_list

    
    def save(self):
        self.file["map"] = self.tiles
        with open("map.json", "w", encoding="utf-8") as f:
            json.dump(self.file, f, indent=2)