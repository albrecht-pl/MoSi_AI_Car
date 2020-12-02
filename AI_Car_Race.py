import pygame
import time
import car
# PARAMS


# 第一次尝试
width = 1280
height = 720



pygame.init()
pygame.display.set_caption("AI Car Race")
size = width, height
background = pygame.display.set_mode(size)
background.fill((255,255,255))
car = car.Car()
background.blit(car.image, car.ps)
pygame.display.flip()

#time.sleep(5)

# MOVEMENT

for counter_move in range(1,50):
    car.ps = car.ps.move(0,2)
    print(car.ps)
    background.fill((255,255,255))
    background.blit(car.image, car.ps)
    pygame.display.flip()
    time.sleep(0.02)
