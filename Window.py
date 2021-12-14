import pygame

class Window:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.width = 800
        self.heigth = 600

        self.window = pygame.display.set_mode((self.width, self.heigth))
        self.window.fill(self.WHITE)
        
    def display_text(self, size, text, color, x, y):
        font = pygame.font.Font("./assets/flappy-bird.ttf", size)
        textObj = font.render(text, True, color)
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.window.blit(textObj, textRect)