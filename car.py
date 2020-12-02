import pygame
import time

class Car:


    global x
    global y
    global rotation

    def __init__(self):
        self.image = pygame.image.load("Car_911.png")
        self.image = pygame.transform.scale(self.image, (103,51))
        self.image = pygame.transform.rotate(self.image, (-90))
        self.ps = self.image.get_rect()
        
        # Rotation


    def draw():
        print("NO")