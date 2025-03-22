import pygame.image

from src.block import fence

stageSprite = pygame.image.load_extended("../Images/Stages/HomeStage.png")

class homeStage:
    def __init__(self,houseCount):
        self.houseCount = houseCount
        self.fences = [fence(0, 336,0), fence(32,336,1), fence(0, 432, 0), fence(32,432, 1),
                       fence(1184,336,0), fence(1152,336,2),fence(1184, 432, 0), fence(1152,432, 2),
                       fence(544,0,3),fence(544,32,5),fence(640,0,3),fence(640,32,5),
                       fence(544, 768, 3), fence(544, 736, 4), fence(640, 768, 3), fence(640, 736, 4),
                       ]

    def draw(self, win):
        win.blit(stageSprite,(0,0))
        for frame in self.fences:
            frame.draw(win)
