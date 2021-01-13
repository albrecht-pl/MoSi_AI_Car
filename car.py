import pygame
import time
import os

class Car:


    def __init__(self):
        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        self.image = pygame.image.load(currentDirectory+"/Car_911.png")
        self.image = pygame.transform.scale(self.image, (103,51))
        self.image = pygame.transform.rotate(self.image, (-90))
        self.ps = self.image.get_rect()
        self.car_speed = 0
        self.x = 0
        self.y = 0
        self.rotation = 0
        
        # Rotation

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, (-1))


    def draw(self):
#<<<<<<< Updated upstream
        print("NO")
#=======

    def acceleration(self):

        self.car_speed +=  0.1
        time.sleep(0.02)
        print("Beschleunigen")

    def brake(self):
        self.car_speed -= 0.1
        time.sleep(0.02)
        print("Bremsen")

    def sail (self):
        self.car_speed +=  0
        print("Geschwindigkeit halten")


# Bewegung


def Bewegung(car1): #was für Variablen müssen hier rein ? x und y?
    car_speed = 0 # muss ich in dieser Funktion car_speed einen Wert zuordnen oder funktioniert sowas mit global Variablen nicht?


    running = True
    while running:
        for event in pygame.event.get():
            while event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    car1.acceleration()
                if event.key == pygame.K_DOWN:
                    car1.brake()
            if event.type == pygame.KEYUP:
                car1.sail()


if __name__ == '__main__':
    car1 = Car()
    Bewegung(car1)
