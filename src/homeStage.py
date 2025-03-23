import pygame.image

from block import fence, loadZone
from gameState import gameState
from yapper import yapper

stageSprite = pygame.image.load_extended("../Images/Stages/HomeStage.png")
houseSprites = [pygame.image.load("../Images/House/House0.png"),pygame.image.load("../Images/House/House1.png"),pygame.image.load("../Images/House/House2.png"),pygame.image.load("../Images/House/House3.png"),pygame.image.load("../Images/House/House4.png")]
sheepSprite =pygame.image.load("../Images/House/Sheep.png")
witchSprite = pygame.image.load("../Images/witch/witch.png")
portalSprite = pygame.image.load("../Images/witch/portal.png")

class homeStage:
    def __init__(self,houseCount):
        self.loadZones = []
        self.witchCutscene = False
        self.witchCutsceneTimer = 300
        self.storyCount = 0
        self.houseCount = houseCount
        self.fences = [fence(0, 336,0), fence(32,336,1), fence(0, 432, 0), fence(32,432, 1),
                       fence(1184,336,0), fence(1152,336,2),fence(1184, 432, 0), fence(1152,432, 2),
                       fence(544,0,3),fence(544,32,5),fence(640,0,3),fence(640,32,5),
                       fence(544, 768, 3), fence(544, 736, 4), fence(640, 768, 3), fence(640, 736, 4),
                       ]



    def update(self,win,player,currentGameState,bgImage):
        if self.houseCount ==0:
            self.loadZones = [loadZone(0,368, 1, 768, 384),loadZone(0,400, 1, 768, 384) ]
        elif self.houseCount ==1:
            self.loadZones = [loadZone(576,0, 2, 768, 384),loadZone(608,0, 2, 768, 384) ]
        elif self.houseCount ==2:
            self.loadZones = [loadZone(768,368, 3, 0, 384),loadZone(768,400, 3, 0, 384)]
        elif self.houseCount ==3:
            self.loadZones = [loadZone(576,768, 4, 592, 80),loadZone(608,768, 4, 592, 80)]
        if self.houseCount==5:
            self.loadZones = []
        for zone in self.loadZones:
            if zone.check(player):
                gameState.state=zone.destination
                self.loadZones = []
                return
        if self.storyCount == self.houseCount:

            talkTHing = yapper()
            if self.storyCount == 0:
                talkTHing.startYapThread("Aah hello welcome young one, there seams to be the perfect hole here to build a house, how about we start with some foundations, go west and get some stone")
            elif self.storyCount == 1:
                talkTHing.startYapThread("This foundation is looking nice, how about going north to try and find some timber for the walls")
            elif self.storyCount == 2:
                talkTHing.startYapThread("Wow the walls are looking nice but the house seams a bit cold, why not go east to grab some fire to carry back, whats that look for yes thats how fire works here")
            elif self.storyCount == 3:
                talkTHing.startYapThread("Wow very functional but how about going south to find some flowers to pretty up this place")
            elif self.storyCount == 4:
                talkTHing.startYapThread("Mwahahaha thanks for the house bozo see you")
                self.witchCutscene = True
                player.canMove = False
            self.storyCount += 1

        if self.witchCutscene == True:
            self.witchCutsceneTimer -= 1
            if self.witchCutsceneTimer == 0:
                self.witchCutscene = False
                player.canMove = True
                self.loadZones.append(loadZone(150,150, 5, 200, 200, 156,156))




        self.draw(win,bgImage)


    def draw(self, win,bgImage):
        if bgImage:
            win.blit(stageSprite,(0,0))
        else:
            win.fill("green")
        if self.houseCount == 5:
            win.blit(houseSprites[4], (340, 180))
            win.blit(sheepSprite, (800, 20))
        elif self.houseCount == 4:
            if self.witchCutscene == True:
                win.blit(houseSprites[4], (340, 180))
                win.blit(witchSprite, (300, 100))
            else:
                win.blit(houseSprites[0], (340, 280))
                win.blit(portalSprite, (100, 100))
        elif self.houseCount > 1:
            win.blit(houseSprites[self.houseCount], (340, 180))
        else:
            win.blit(houseSprites[self.houseCount], (340, 280))
        for frame in self.fences:
            frame.draw(win)
        for zone in self.loadZones:
            pygame.draw.rect(win,"red",zone.hitbox)
        if self.houseCount <4:
            win.blit(witchSprite,(300,100))


