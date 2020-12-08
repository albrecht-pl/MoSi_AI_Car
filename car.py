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
<<<<<<< Updated upstream
        print("NO")
=======


# Bewegung


def Bewegung (move, breake): #was für Variablen müssen hier rein ? x und y?
    car_speed = 0 # muss ich in dieser Funktion car_speed einen Wert zuordnen oder funktioniert sowas mit global Variablen nicht?

    running = True
    while running:
        for event in pygame.event.get():
            while event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    acceleration()
                if event.key == pygame.K_DOWN:
                    brake()
            if event.type == pygame.KEYUP:
                car_speed += 0

def acceleration():

    car_speed +=  0.1
    time.sleep(0.02)
    print("Beschleunigen")

def brake():
    car_speed -= - 0.1
    time.sleep(0.02)
    print("Bremsen")

def sail ():
    car_speed +=  0
    print("Geschwindigkeit halten")
