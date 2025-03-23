import pygame

startButton = pygame.image.load_extended("../Images/menu/Start.png")
exitButton = pygame.image.load_extended("../Images/menu/Exit.png")
arrow = pygame.image.load_extended("../Images/menu/Arrow.png")

class menu:
    def __init__(self):
        self.currentState =0
        self.inputCooldown = 30
        self.coolDown = False

    def update(self,window,bgImage):
        if self.coolDown:
            self.inputCooldown -= 1
            if self.inputCooldown <= 0:
                self.coolDown = False
                self.inputCooldown = 16
        self.draw(window,bgImage)

    def swapState(self):
        if not self.coolDown:
            self.currentState = (self.currentState + 1) %2
            self.coolDown = True


    def draw(self,window,bgImage):
        window.fill((0,0,255))
        window.blit(startButton,(448,300))
        window.blit(exitButton,(480,500))
        window.blit(arrow,(350,300+200*self.currentState))
