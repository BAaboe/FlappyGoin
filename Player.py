import pygame
from pygame.locals import *
import Window

class Player(pygame.sprite.Sprite):
    def __init__(self, wd: Window.Window()):
        super().__init__()
        self.wd = wd

        self.width = 50
        self.heigth = 100
        self.x = self.wd.width/4
        self.y = self.wd.heigth/2

        self.speed = 0
        self.speedMult = 1.5
        
        self.image = pygame.image.load("./assets/goin1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.heigth))
        self.image = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

        self.flap = 0

        self.score = 0

        #self.curentRoation = 0

        #self.image = pygame.transform.rotate(self.image, 360-self.curentRoation+90+180)
        #self.curentRoation = 90
        #self.maxRotation = 120
        #self.minRotation = 60

        self.dead = False


    def move(self):
        self.y -= self.speed
        self.rect.move_ip(0, -self.speed)


    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_SPACE]:
            if self.rect.top <= 10:
                self.flap -= 1
            else:
                self.flap = 10
        else:
            self.flap -= 1
        
        self.speed = self.flap*self.speedMult
        if self.rect.y + self.width > self.wd.heigth:
            if pressed_keys[K_SPACE]:
                self.move()
        else:
            self.move()
        
        self.draw()
        
        #TODO fix it self.animate()

    def draw(self):
        self.wd.window.blit(self.image, self.rect)

    #TODO finish this

    def animate(self):
        if self.flap + 10 <= 0:
            degree = self.maxRotation
        elif self.flap + 10 >= 10:
            degree = self.minRotation
        else:
            degree = self.maxRotation-self.minRotation/20 * (self.flap+10)
        self.rotate(degree)

    def rotate(self, degree):
        self.image = pygame.transform.rotate(self.image, 360-self.curentRoation+degree)
        self.curentRoation = degree
    
    def die(self):
        self.wd.display_text(200, "Game Over", self.wd.BLACK, self.wd.width/2, self.wd.heigth/2)
        self.wd.display_text(100, f"{self.score}", self.wd.BLACK, self.wd.width/2, self.wd.heigth/3*2)
        self.dead =True

        
