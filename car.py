import pygame
import time
import os

class Car:


    global x
    global y
    global rotation

    def __init__(self):
        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        self.image = pygame.image.load(currentDirectory+"/Car_911.png")
        self.image = pygame.transform.scale(self.image, (103,51))
        self.image = pygame.transform.rotate(self.image, (-90))
        self.ps = self.image.get_rect()
        
        # Rotation

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, (-1))


    def draw():
        print("NO")