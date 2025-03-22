import pygame.image

from src.block import fence, loadZone

stageSprite = pygame.image.load_extended("../Images/Stages/HomeStage.png")
houseSprites = [pygame.image.load("../Images/House/House0.png"),pygame.image.load("../Images/House/House1.png")]

class homeStage:
    def __init__(self,houseCount):
        self.loadZones = None
        self.houseCount = houseCount
        self.fences = [fence(0, 336,0), fence(32,336,1), fence(0, 432, 0), fence(32,432, 1),
                       fence(1184,336,0), fence(1152,336,2),fence(1184, 432, 0), fence(1152,432, 2),
                       fence(544,0,3),fence(544,32,5),fence(640,0,3),fence(640,32,5),
                       fence(544, 768, 3), fence(544, 736, 4), fence(640, 768, 3), fence(640, 736, 4),
                       ]
        if (houseCount ==0):
            self.loadZones = [loadZone(0,368, 1, 768, 384),loadZone(0,400, 1, 768, 384) ]
        if (houseCount ==2):
            self.loadZones = [loadZone(768,368, 3, 0, 384),loadZone(768,400, 3, 0, 384)]
        if houseCount ==3:
            self.loadZones = [loadZone(576,768, 4, 592, 1),loadZone(608,768, 4, 592, 1)]






    def draw(self, win):
        win.blit(stageSprite,(0,0))
        win.blit(houseSprites[self.houseCount], (340,280))
        for frame in self.fences:
            frame.draw(win)
