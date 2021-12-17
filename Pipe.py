import Window
import pygame
from pygame.locals import*

import random

class Pipe:
    def __init__(self, wd: Window.Window()):
        self.wd = wd

        self.width = 100
        self.heigth = 600

        self.pipeDistance = 200

        self.ySpawnRange = (self.heigth/10*2, self.heigth/10*9)

        self.downPipeX = self.wd.width
        self.downPipeY = random.randint(self.ySpawnRange[0], self.ySpawnRange[1])

        self.upPipeX = self.downPipeX
        self.upPipeY = self.downPipeY - self.pipeDistance - self.heigth

        self.image = pygame.image.load("./assets/pipe.png")
        self.downPipe = pygame.transform.scale(self.image, (self.width, self.heigth))
        self.upPipe = pygame.transform.rotate(self.downPipe, 180)

        self.speed = 5


    def move(self):
        self.upPipeX -= self.speed
        self.downPipeX -= self.speed
    
    def update(self):
        self.move()

        self.draw()

    def draw(self):
        self.wd.window.blit(self.upPipe, (self.upPipeX, self.upPipeY))
        self.wd.window.blit(self.downPipe, (self.downPipeX, self.downPipeY))
    
    def isOutOfScreen(self):
        return self.downPipeX <= 0 - self.width


    

        