import pygame
import time

class Car:


	x = 0
	y = 0

	rotation = 0;

    def __init__(self):
        self.image = pygame.image.load("Car_911.png")
        self.image = pygame.transform.scale(self.image, (103,51))
        self.image = pygame.transform.rotate(self.image, (-90))
        self.ps = self.image.get_rect()
        
        # Rotation


    def draw():