import pygame.image
#0 Horizontal middle  #1 left endpoint #2 right endpoint #3 Verticle Middle #4 bottom endpoint # 5 top endpoint
fenceSprite = [pygame.image.load_extended("../Images/Fence/fence3.png"),pygame.image.load_extended("../Images/Fence/fence4.png"),
               pygame.transform.flip(pygame.image.load_extended("../Images/Fence/fence4.png"),True,False),
               pygame.transform.rotate(pygame.image.load_extended("../Images/Fence/fence3.png"),90),
               pygame.transform.rotate(pygame.image.load_extended("../Images/Fence/fence4.png"),90),
               pygame.transform.rotate(pygame.image.load_extended("../Images/Fence/fence4.png"),-90)
               ]
flowerSprite = pygame.image.load("../Images/Fence/flower.png")


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

class flowerPatch:
    def __init__(self,x,y, discovered):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x,self.y,48,48)
        self.discovered = discovered
    def draw(self,win):
        if self.discovered:
            win.blit(flowerSprite,(self.x,self.y))
        else:
            pygame.draw.rect(win, (0,255,0), self.hitbox, 1)
    def drawAnyway(self,win):
        win.blit(flowerSprite, (self.x, self.y))
class air:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 48, 48)
    def draw(self,win):
        pygame.draw.rect(win, (0,255,0), self.hitbox, 1)