import pygame
import time

# PARAMS


# 第一次尝试
width = 1280
height = 720

# INIT

class Car:
    def __init__(self):
        self.image = pygame.image.load("Car_911.png")
        self.image = pygame.transform.scale(self.image, (103,51))
        self.image = pygame.transform.rotate(self.image, (-90))
        self.ps = self.image.get_rect()
        # Rotation

pygame.init()
pygame.display.set_caption("AI Car Race")
size = width, height
background = pygame.display.set_mode(size)
background.fill((255,255,255))
car = Car()
background.blit(car.image, car.ps)
pygame.display.flip()

time.sleep(5)

# MOVEMENT

for counter_move in range(1,50):
    car.ps = car.ps.move(0,2)
    print(car.ps)
    background.fill((255,255,255))
    background.blit(car.image, car.ps)
    pygame.display.flip()
    time.sleep(0.02)
