import pygame
from pygame.locals import *
import sys
import Window
import Player
import Pipe

pygame.init()

class Main:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.wd = Window.Window()

        self.FPS = 30
        self.FramesPerSecond = pygame.time.Clock()

        self.p = Player.Player(self.wd)

        self.pipes = []

        

    def main(self):
        self.pipes.append(Pipe.Pipe(self.wd))
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
            if not self.p.dead:
                self.wd.window.fill(self.WHITE)
                

                if self.pipes[-1].downPipeX <= self.wd.width-400:
                    self.pipes.append(Pipe.Pipe(self.wd))

                if self.pipes[0].downPipeX < self.p.x: pipe = self.pipes[1]
                else: pipe = self.pipes[0]

                if self.p.x > pipe.downPipeX and self.p.x < pipe.downPipeX + pipe.width:
                    if self.p.y < pipe.upPipeY + pipe.heigth:
                        self.p.die()
                        continue
                    elif self.p.y+self.p.width > pipe.downPipeY:
                        self.p.die()
                        continue
                    else:
                        self.p.score += 1

                i = 0
                for pipe in self.pipes:
                    if pipe.isOutOfScreen():
                        self.pipes.pop(i)
                    else:
                        pipe.update()
                    i += 1

                self.p.update()
                self.wd.display_text(100, f"{self.p.score}", self.BLACK, self.wd.width/2, 100)
            
            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)


if __name__ == "__main__":
    Game = Main()
    Game.main()