import random
from pygame import *

class rockStage():
    def __init__(self):
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
        self.lives=3
    def draw(self,window):
        window.fill(self.light_blue)
        livesTextSurface=self.font.render(self.hpString+str(self.lives),True,self.textColour)
        livesTextRect=livesTextSurface.get_rect(center=(1150,20))
        window.blit(livesTextSurface,livesTextRect)
        if self.frames%120==0:
            self.generateRocks(window)
        
        for rock in self.rocks:
            draw.rect(window,"gray",Rect(rock[1],rock[0],32,32))
            rock[1]+=rock[3]*self.speed
            rock[0]+=rock[2]*self.speed
        self.frames+=1
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
