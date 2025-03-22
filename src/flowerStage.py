import random

from src.homeStage import stageSprite
from src.block import *

stageSprite = pygame.image.load_extended("../Images/Stages/flowerStage.png")


class flowerStage:
    def __init__(self):
        self.mazeTimer = 600
        self.squares = []
        self.patch = self.populatePatch()

        self.flowers = [flowerPatch(528,0,True),flowerPatch(528,48,True),flowerPatch(656,0,True),flowerPatch(656,48,True)
                       ,flowerPatch(704,48,True),flowerPatch(752,48,True),flowerPatch(800,48,True),flowerPatch(848,48,True)
                       ,flowerPatch(480,48,True),flowerPatch(432,48,True),flowerPatch(384,48,True),flowerPatch(336,48,True)]

        for i, y in enumerate(self.patch):
            for j, x in enumerate(y):
                if (x == 0):
                    self.flowers.append(flowerPatch(296+j*48,96+i*48,False))
                else:
                    self.squares.append(air(296+j*48,96+i*48))

    def populatePatch(self) :
        currentX = 6
        currentY = 0
        pathed = False
        patchBuild=[[0, 0 , 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                      ]
        while not pathed:
            #0 = Left 1 = Down 2 = Right
            direction = random.randint(0,6)
            if currentY == 0 :
                if (direction == 0 or direction == 1 or direction == 5) and currentX-1 > 1 and patchBuild[currentY][currentX-1] == 0:
                    currentX -= 1
                    patchBuild[currentY][currentX] = 1
                elif direction == 2:
                    currentY += 1
                    patchBuild[currentY][currentX] = 1
                elif (direction == 4 or direction == 3) and currentX+1 < 12 and patchBuild[currentY][currentX+1] == 0:
                    currentX += 1
                    patchBuild[currentY][currentX] = 1
            else:
                if (direction == 0 or direction == 1) and currentX-1 > 1 and patchBuild[currentY][currentX-1] == 0 and patchBuild[currentY-1][currentX-1] == 0:
                    currentX -= 1
                    patchBuild[currentY][currentX] = 1
                elif direction == 2:
                    currentY += 1
                    patchBuild[currentY][currentX] = 1
                elif (direction == 4 or direction == 3 or direction == 6)and currentX+1 < 12 and patchBuild[currentY][currentX+1] == 0 and patchBuild[currentY-1][currentX+1] == 0:
                    currentX += 1
                    patchBuild[currentY][currentX] = 1
            if currentY == 10:
                pathed = True
        return patchBuild

    def update(self, player,win):
        player.moveSpeed=3
        if (self.mazeTimer>0):
            player.canMove=False
            self.mazeTimer -= 1;
        else:
            player.canMove=True
        self.draw(win)


    def draw(self, win):
        win.blit(stageSprite,(0,0))
        if (self.mazeTimer > 0):
            for flower in self.flowers:
                flower.drawAnyway(win)
        else:
            for flower in self.flowers:
                flower.draw(win)
        for frame in self.squares:
            frame.draw(win)




