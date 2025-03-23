import math
from pprint import pprint
from Slayer import Player
from yapper import yapper
import random
import pygame
from gameState import gameState
class fireStage():
    def  __init__(self):
        self.announcer=yapper()
        self.frames=0
        self.delay=1
        self.maxAttempts=5
        self.totalTargets=3
        self.previousYapState=True
        self.lastYapFrame=0
        self.targetNum=1
        self.attempts=0
        self.targetX=-1
        self.targetY=-1
        self.lastAnnounced=0
        self.targetRadius=30
        self.canShoot=False
        self.finished=False
        
    def update(self,window,player,bgImage):
        window.fill("black")
        if self.canShoot:
            pygame.draw.circle(window,"red",(self.targetX,self.targetY),self.targetRadius)
        
        if self.announcer.yapping:
            self.lastYapFrame=self.frames
        if self.announcer.yapping==False and self.finished:
            gameState.state=0
            return "Win"
        self.previousYapState=self.announcer.yapping
        if self.frames==0:
            
            self.announcer.startYapThread("Welcome to the fire challenge... Please place your mouse in the centre of the screen then close your eyes... A fire has caused smoke to block your vision... Your task is to hit"+str(self.totalTargets)+"targets with your eyes closed.. you will have" +str(self.maxAttempts)+ "attempts to hit each target and before each attempt you will be told the bearing and distance of the target from the centre of the screen as well as the bearing and distance of your last shot... Good luck!")
        if self.lastAnnounced<self.targetNum and self.frames>self.lastYapFrame+self.delay*60:
            self.generateTarget(window)
            print(self.targetX,self.targetY)
            
            
            self.lastAnnounced+=1
        if self.lastAnnounced==self.targetNum and self.announcer.yapping==False and (not self.canShoot):
            self.canShoot=True
            print("CAN SHOOT")
        
      
        # if self.frames==self.initialDelay*60:
        #     self.announcer.startYapThread("Heyyy we finna yap at the same time right now homie?")
        self.frames+=1
    def generateTarget(self,window):
        maxY=window.get_height()
        maxX=window.get_width()
        self.targetX=random.randint(0,maxX)
        self.targetY=random.randint(0,maxY)
        distTarget=int(round(self.getDist(self.targetX,self.targetY,window.get_width()/2,window.get_height()/2)))
        bearingTarget=int(round(self.getBearing(self.targetX,self.targetY,window.get_width()/2,window.get_height()/2)))
        self.announcer.startYapThread("Target number "+str(self.targetNum)+"has a bearing of... "+str(bearingTarget)+"... and a distance of... "+str(distTarget)) 
    def getBearing(self,x1,y1,x2,y2):
        bearing=math.degrees(math.atan2(y2-y1,x2-x1))
        bearing-=90
        if bearing<0:
            bearing+=360
        return bearing
    def getDist(self,x1,y1,x2,y2):
        return math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)
    def isHit(self,x,y):
        hSquared=abs(self.targetX-x)**2+abs(self.targetY-y)**2
        if self.targetRadius**2>=hSquared:
            return True
        return False
    def mouseDown(self,pos,screen):
        if self.canShoot:
            self.fire(pos,screen)
    def fire(self,pos,screen):
        self.canShoot=False
        self.attempts+=1
        shotX=pos[0]
        shotY=pos[1]
        hit =self.isHit(shotX,shotY)
        if hit:
            print("HIT")
            self.attempts=0
            self.targetNum+=1
            if self.targetNum>self.totalTargets:
                self.announcer.startYapThread("Congratulations on hitting all"+str(self.totalTargets)+"targets and claiming fire for your house")
                
                self.finished=True
            else:
                self.announcer.startYapThread("You hit target number... "+str(self.targetNum-1))            
                
        else:
            print("MISS")
            distTarget=int(round(self.getDist(self.targetX,self.targetY,screen.get_width()/2,screen.get_height()/2)))
            bearingTarget=int(round(self.getBearing(self.targetX,self.targetY,screen.get_width()/2,screen.get_height()/2)))
            distShot=int(round(self.getDist(shotX,shotY,screen.get_width()/2,screen.get_height()/2)))
            bearingShot=int(round(self.getBearing(shotX,shotY,screen.get_width()/2,screen.get_height()/2)))
            print(distShot,bearingShot)
            if self.attempts==self.maxAttempts:
                self.announcer.startYapThread("You lose")
                gameState.state=0
                return "Lose"
            
            self.announcer.startYapThread("You missed the target...The target has a bearing of... "+str(bearingTarget)+"... and a distance of... "+str(distTarget)+"... Youre shot had a bearing of... "+str(bearingShot)+"... and a distance of... "+str(distShot)) 
