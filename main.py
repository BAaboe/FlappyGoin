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

        self.p = Player.Player(self.wd)

        self.pipes = []

        self.lastPipeIndex = 0
        self.passedPipe = False


        

    def main(self):
        self.pipes.append(Pipe.Pipe(self.wd))
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if keys[K_ESCAPE]:
                        pygame.quit()
                        quit()
            if not self.p.dead:
                self.wd.window.fill(self.wd.WHITE)
                

                if self.pipes[-1].downPipeX <= self.wd.width-400:
                    self.pipes.append(Pipe.Pipe(self.wd))

                if self.pipes[0].downPipeX < self.p.x: pipe = self.pipes[1]
                else: pipe = self.pipes[0]

                if self.p.x + self.p.heigth > pipe.downPipeX and self.p.x < pipe.downPipeX + pipe.width:
                    if self.p.y < pipe.upPipeY + pipe.heigth:
                        self.p.die()
                        continue
                    elif self.p.y+self.p.width > pipe.downPipeY:
                        self.p.die()
                        continue
                    else:
                        if not self.passedPipe:
                            self.lastPipeIndex = self.pipes.index(pipe)
                            self.p.score += 1
                            self.passedPipe = True

                if self.pipes[self.lastPipeIndex].downPipeX + self.pipes[self.lastPipeIndex].width < self.p.x:
                    self.passedPipe = False

                i = 0
                for pipe in self.pipes:
                    if pipe.isOutOfScreen():
                        self.pipes.pop(i)
                    else:
                        pipe.update()
                    i += 1

                self.p.update()
                self.wd.display_text(100, f"{self.p.score}", self.wd.BLACK, self.wd.width/2, 100)
            
            else:
                if keys[K_SPACE]:
                    self.pipes.clear()
                    self.pipes.append(Pipe.Pipe(self.wd))
                    self.p.dead = False

            pygame.display.update()
            self.FramesPerSecond.tick(self.FPS)


if __name__ == "__main__":
    Game = Main()
    Game.main()