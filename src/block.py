import pygame.image

fenceSprite = [pygame.image.load_extended("../Images/Fence/fence3.png"),pygame.image.load_extended("../Images/Fence/fence4.png")]

class fence:
    def __init__(self,x,y,sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.hitbox = pygame.Rect(self.x,self.y,32,32)

    def draw(self,win):
        win.blit(fenceSprite[self.sprite],(self.x,self.y))


class loadZone:
    def __init__(self,x,y,destination,destinationX,destinationY):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x,self.y,32,32)
        self.destination = destination
        self.destinationX = destinationX
        self.destinationY = destinationY
