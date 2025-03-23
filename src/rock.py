import random
from pygame import *
import math
from block import *
from gameState import gameState
from yapper import yapper
class rockStage():
    def __init__(self):
        self.reset()
    def reset(self):
        self.rockWavePresent=False
        self.rockWaveCount=0
        self.rockWaveDirection=-1
        self.rocks=[]
        self.frames=0
        self.speed=4
        self.light_blue=(106,157,183)
        self.font=font.Font(None,40)
        self.textColour=(0,0,0)
        self.hpString="Lives: "
        self.timeString="Time remaining: "
        self.timeRemaining=66
        self.lives=3
        self.invincibilityFrames=60
        self.gracePeriod=6
        self.lastCollision=-(self.invincibilityFrames+1)
        self.golemStates=[image.load('../Images/Golem/golem1.png'),image.load('../Images/Golem/golem2.png'),image.load('../Images/Golem/golem3.png'),image.load('../Images/Golem/golem4.png'),image.load('../Images/Golem/golem5.png'),image.load('../Images/Golem/golem6.png')]
        self.rockImage=image.load('../Images/rockStage/rock.png')
        self.rockLump=image.load('../Images/rockStage/rockLump.png')
        self.bg = image.load('../Images/rockStage/rockStage.png')
        self.collectedRock=False
        
        self.loadZones=[loadZone(1196,0,0,596,384,20,800)]
    def update(self,window,player,currentGameState,bgImage):
        
        playerRect=player.rect
        if bgImage:
            window.blit(self.bg,(0,0))
        else:
            window.fill("blue")


        index=min(5,self.timeRemaining//10)
        if index>=0:
            golemImage=self.golemStates[5-index]
            golemRect=golemImage.get_rect()
            golemRect.topleft = (400,200)
            window.blit(golemImage,golemRect)
        if self.timeRemaining<0 and (not self.collectedRock):
            lumpRect=self.rockLump.get_rect()
            lumpRect.topleft = (400,200)    
            window.blit(self.rockLump,lumpRect)
            lumpCollisionRect=(492,342,200,100)
            if playerRect.colliderect(lumpCollisionRect):
                self.collectedRock=True
                currentGameState.states[0].houseCount += 1

        if self.collectedRock:
            for load in self.loadZones:
                if load.check(player):
                    gameState.state=load.destination
                    return "Win"
        
        if self.frames%120==0 and self.frames>=60*self.gracePeriod and self.timeRemaining>=0:
            self.generateRocks(window)
        if self.frames%60==0:
            self.timeRemaining-=1
            if(self.timeRemaining==-1):
                self.rocks=[]
                player.rect.center=(40,400)
        for rock in self.rocks[:]:
            rockRect=Rect(rock[0],rock[1],32,32)
            rockCollisionRect=Rect(rock[1]+2,rock[0]+2,28,28)
            rockRect=self.rockImage.get_rect()
            rockRect.topleft = (rock[1],rock[0])
            window.blit(self.rockImage,rockRect)
            if playerRect.colliderect(rockCollisionRect) and self.frames>self.lastCollision+self.invincibilityFrames:
                self.lives-=1
                if self.lives<=0:
                    gameState.state=0
                    player.rect.center=(100,384)
                    self.reset()
                    return "Lose"
                self.lastCollision=self.frames
                self.rocks.remove(rock)
            
            rock[1]+=rock[3]*self.speed
            rock[0]+=rock[2]*self.speed
        

        

        livesTextSurface=self.font.render(self.hpString+str(self.lives),True,self.textColour)
        livesTextRect=livesTextSurface.get_rect(center=(1150,20))
        window.blit(livesTextSurface,livesTextRect)

        if self.timeRemaining>=0:
            timeTextSurface=self.font.render(self.timeString+str(self.timeRemaining),True,self.textColour)
            timeTextRect=timeTextSurface.get_rect(center=(140,20))
            window.blit(timeTextSurface,timeTextRect)

        if self.frames==1:
            dwayne=yapper()
            dwayne.startYapThread("I am Dwayne the rock johnson... Tremble before me and behold my immense power!!! Mwaahahahahahahahaahahahhahahahahhahahahhaha")
        
        self.frames+=1
        return 0
    def generateRocks(self,window):
        # notPresent=random.randint(0,24)
        # for i in range(25):
        #     if i!=notPresent:
        #         print("B")
        #         self.rocks.append([32*i,0])
        # self.rockWavePresent=True
        maxH=window.get_height()-34
        maxW=window.get_width()-34
        for i in range(20):
            dir=random.randint(1,4)
            if dir==1:
                y=random.randint(0,maxH)
                self.rocks.append([y,0,0,1])
            elif dir==2:
                y=random.randint(0,maxH)
                self.rocks.append([y,maxW,0,-1])
            elif dir==3:
                x=random.randint(0,maxW)
                self.rocks.append([0,x,1,0])
            elif dir==4:
                x=random.randint(0,maxW)
                self.rocks.append([maxH,x,-1,0])
        self.rockWavePresent=True
