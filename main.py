import pygame
from pygame.locals import *
import sys
import Window
import Player
import Pipe

pygame.init()


class Main:
    def __init__(self):
        self.wd = Window.Window()

        self.FPS = 30
        self.FramesPerSecond = pygame.time.Clock()

        self.themeSong = pygame.mixer.Sound("./assets/Theme.wav")
        self.startSound = pygame.mixer.Sound("./assets/start.wav")
        self.dieSound = pygame.mixer.Sound("./assets/die.wav")
        self.dingSound = pygame.mixer.Sound("./assets/ding.wav")
        self.flappSound = pygame.mixer.Sound("./assets/flapp.wav")

        self.p = Player.Player(self.wd, self)

        self.pipes = []
        self.breakLoop = False

        

    def start(self, first):
        if first:
            pygame.mixer.Sound.play(self.themeSong)
        self.wd.window.fill(self.wd.WHITE)
        self.wd.draw_bg()
        self.wd.display_text(100, "Flappy Goin", self.wd.BLACK, self.wd.width/2, 100)
        self.wd.display_text(50, "Press Space to start", self.wd.BLACK, self.wd.width/2, 400)
        self.p.draw()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[K_ESCAPE]:
                        pygame.quit()
                        quit()
                    elif keys[K_SPACE]:
                        pygame.mixer.stop()
                        pygame.mixer.Sound.play(self.startSound)
                        self.main()
            self.wd.window.fill(self.wd.WHITE)
            self.wd.update_bg()
            self.wd.display_text(100, "Flappy Goin", self.wd.BLACK, self.wd.width/2, 100)
            self.wd.display_text(50, "Press Space to start", self.wd.BLACK, self.wd.width/2, 400)
            self.p.draw()
            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)

    def main(self):
        self.pipes.append(Pipe.Pipe(self.wd))
        while not self.breakLoop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[K_ESCAPE]:
                        pygame.quit()
                        quit()
                    elif keys[K_SPACE] and self.p.dead:
                        pygame.mixer.Sound.play(self.startSound)
                        pygame.mixer.Sound.play(self.startSound)
                        main = Main()
                        main.start(False)
            if not self.p.dead: 

                self.wd.window.fill(self.wd.WHITE)
                self.wd.update_bg()
                

                if self.pipes[-1].downPipeX <= self.wd.width - 400:
                    self.pipes.append(Pipe.Pipe(self.wd))

                i = 0
                for pipe in self.pipes:
                    if pipe.isOutOfScreen():
                        self.pipes.pop(i)
                    else:
                        pipe.update()
                        i += 1
                
                self.p.update(self)
                self.wd.display_text(100, f"{self.p.score}", self.wd.BLACK, self.wd.width/2, 100)
                
                if self.p.y + self.p.heigth + self.p.width > self.wd.heigth:
                    self.p.die()

                for closePipe in self.pipes:
                    if pygame.Rect.colliderect(self.p.rect, closePipe.upRect): self.p.die(); continue
                    if not closePipe.upRect.bottom < 2:
                        if pygame.Rect.colliderect(self.p.rect, closePipe.downRect): self.p.die(); continue

                    if self.p.x+self.p.heigth == closePipe.downPipeX + (closePipe.width/2):
                        self.p.score += 1
                        pygame.mixer.Sound.play(self.dingSound)

                

            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)


if __name__ == "__main__":
    Game = Main()
    Game.start(True)