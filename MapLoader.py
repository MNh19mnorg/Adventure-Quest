import pygame
import json

class Map_Loader():
    def __init__(self, file="map.json"):
        self.file = file
        self.map = list()
    
    def load(self):
        with open(self.file, encoding="utf-8") as f:
            self.map = json.load(f)        