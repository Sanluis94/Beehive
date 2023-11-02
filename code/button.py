import pygame

class Button:
    def __init__(self,screen,x,y,image,single_click):

        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.single_click = single_click

    def draw(self):
        self.action = False
        self.pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.pos) and self.clicked == False:
            if pygame.mouse.get_pressed()[0] == 1:
                self.action = True
                if self.single_click:
                    self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.screen.blit(self.image,self.rect)

        return self.action