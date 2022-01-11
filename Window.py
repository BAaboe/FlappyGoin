import pygame

class Window:
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)

        self.width = 800
        self.heigth = 600

        self.window = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption("Flappy Goin")
        Icon = pygame.image.load("./assets/icon.png")
        pygame.display.set_icon(Icon)
        self.window.fill(self.WHITE)

        self.bg_image = pygame.image.load("./assets/bg.png")

        self.bgWidth = self.bg_image.get_size()[0]
        self.bgHeigth = 600

        self.bg_image = pygame.transform.scale(self.bg_image, (self.bgWidth, self.bgHeigth))

        self.bgX = 0
        self.bgY = 0

        self.bg_speed = 1

        
    def display_text(self, size, text, color, x, y):
        font = pygame.font.Font("./assets/flappy-bird.ttf", size)
        textObj = font.render(text, True, color)
        textRect = textObj.get_rect()
        textRect.center = (x, y)
        self.window.blit(textObj, textRect)

    def draw_bg(self):
        self.window.blit(self.bg_image, (self.bgX, self.bgY))
    
    def update_bg(self):
        if self.bgX+self.bgWidth == self.width:
            self.bgX = 0
        else:
            self.bgX -= self.bg_speed
        self.draw_bg()