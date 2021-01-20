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
        self.velocity = 0
        self.x = 10
        self.y = 51
        self.rotation = 0
        self.step = 0 # DEBUG
        
    # Rotation

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, (-1))


    def draw(self, pg, bg):
        bg.fill((255,255,255))
        bg.blit(self.image, self.ps)
        pg.display.flip()


    def acceleration(self):
        self.velocity += 0.01
        #print("Beschleunigen")

    def brake(self):
        self.velocity -= 0.01
#        print("Bremsen")

#"""    def sail (self):
#        self.velocity +=  0
#        print("Geschwindigkeit halten")
#@NotNecessary?
#"""
# Bewegung
#def KeyListiner()
    def keyListener(self):
        self.step += 1
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.step % 10 == 1:
                print("n1") #self.ps = self.ps.move(-1,0)
                
        if keys[pygame.K_RIGHT]:
            if self.step % 10 == 1:                       
                print("n")#self.ps = self.ps.move(1,0)

        if keys[pygame.K_UP]:
            if self.step % 10 == 1:     
                self.acceleration()
                
        if keys[pygame.K_DOWN]:
            if self.step % 10 == 1:     
                self.brake()
                
        print(self.velocity)

        """
        DUal Keying!
        for keys in pygame.key.get_pressed():
            #if event.type
            #if hasattr(event.key) == False:
            #    break
            print(keys)
            if keys == pygame.K_LEFT:
                print("LEFT" + str(self.step))
            #if event.key == pygame.K_RIGHT:
            #    print("RIGHT" + str(self.step))
            #if event.key == pygame.K_UP:
            #    self.acceleration()
            #if event.key == pygame.K_DOWN:
            #    self.brake()
            time.sleep(1)
            """

    #td: timedelta
    def move(self,td):        
        mv_x = self.velocity * td
        mv_y = 0
        self.ps.move_ip(mv_x, mv_y)

if __name__ == '__main__':
    print("Doesn't boot")
