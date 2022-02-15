import pygame
from pygame.locals import *
import Window


class Player(pygame.sprite.Sprite):
    def __init__(self, wd: Window.Window(), main):
        super().__init__()
        self.wd = wd

        self.width = 50
        self.heigth = 100

        self.x = self.wd.width/4
        self.y = self.wd.heigth/2-(self.heigth/2)

        self.speed = 0
        self.speedMult = 2
        
        self.flipImg = pygame.image.load("./assets/goin1.png")
        #self.flipImg = pygame.transform.rotate(self.flipImg, 270)
        self.flipImg = pygame.transform.scale(self.flipImg, (self.width, self.heigth))

        self.image = self.flipImg

        self.rect = self.flipImg.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.flap = 0
        self.lastFlap = 0

        self.score = 0

        self.rotation = 270

        self.dead = False

        self.main = main

        self.counter = 0


    def move(self):
        self.y -= self.speed
        self.rect.y = self.y
        self.rect.x = self.x


    def update(self, main):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_SPACE]:
            if self.rect.top <= 5:
                self.flap -= 1
            else:
                self.flap = 5
        else:
            self.flap -= 1
        
        self.speed = self.flap*self.speedMult
        
        self.move()
        
        self.draw()

        if self.flap == 5 and self.lastFlap != 5:
            pygame.mixer.Sound.play(self.main.flappSound)

        self.lastFlap = self.flap


    def draw(self):
        self.wd.window.blit(self.image, (self.x, self.y))

    
    
    def die(self):
        #TODO: mario sound pipes
        pygame.mixer.Sound.play(self.main.dieSound)
        

        self.dead = True
        self.flap = 10
        self.speedMult = 1
        FramesPerSecond = pygame.time.Clock()
        while True:
            self.wd.window.fill(self.wd.WHITE)
            self.wd.draw_bg()
            
            
            
            self.flap -= 1
            self.speed = self.flap*self.speedMult
            self.move()
            if self.y+self.heigth > self.wd.heigth:
                self.draw()
                break
            self.draw()

            for pipe in self.main.pipes:
                pipe.draw()

            pygame.display.update()
            FramesPerSecond.tick(self.main.FPS)

        for pipe in self.main.pipes:
                pipe.draw()
        pygame.display.update()
        pygame.mixer.Sound.play(self.main.themeSong)

        self.wd.display_text(200, "Game Over", self.wd.BLACK, self.wd.width/2, self.wd.heigth/2)
        self.wd.display_text(100, f"{self.score}", self.wd.BLACK, self.wd.width/2, self.wd.heigth/3*2)

        


        
