import pygame
import random
from gameState import gameState

from block import loadZone
from yapper import *
witchSprite = pygame.image.load("../Images/witch/witch.png")
sheepSprite =pygame.image.load("../Images/House/Sheep.png")

houseSprites = [pygame.image.load("../Images/House/House0.png"),pygame.image.load("../Images/House/House1.png"),pygame.image.load("../Images/House/House2.png"),pygame.image.load("../Images/House/House3.png"),pygame.image.load("../Images/House/House4.png")]
portalSprite = pygame.image.load("../Images/witch/portal.png")


class sheepStage:
    def __init__(self):
        self.inputCooldown = 30
        self.coolDown = False

        self.loadZones = []
        self.questionsAnswered = 0
        self.askedQuestions = []
        self.audio = yapper()
        self.yapTimer = 600
        self.spoutExpo = True
        self.font = pygame.font.Font(None, 25)
        self.textColour = (0,0,0)
        self.gameOn = True
        self.witchYap = ["AHAHAH, so you think you can get back your hard built foundations, if so then you must pass every witches greatest trial, solving my riddles 3"]
        self.questions =["What has to be broken before you can use it?",
                         "What goes up but never comes down?",
                         "I have branches, but no fruit, trunk or leaves. What am I?",
                         "What gets bigger when more is taken away?",
                         "What can’t be put in a saucepan?",
                         "What can you catch, but not throw?",
                         "What building has the most stories?",
                         "I am an odd number.Take away a letter and I become even.What number am",
                         "What is 3/7 chicken, 2/3 cat and 2/4 goat?"


                         ]
        self.options =[["Egg", "Piano", "Heart"],
                       ["Wall", "France", "Age"],
                       ["Boring Tree", "Bank", "Stick"],
                       ["Lottery", "Debt", "Hole"],
                       ["It's Lid", "Nuclear Waste", "Danny Devito"],
                       ["Short People", "A Cold", "Big Rock"],
                       ["Empire State Building", "Buckingham Palace", "A Library"],
                       ["Three", "Five", "Seven"],
                       ["Big Soup", "Chicago", "Lichtenstein"]
                        ]
        self.answers = [1,2,2,3,1,1,3,3,2]

        self.currentNumber = random.randint(0,8)
        self.askedQuestions.append(self.currentNumber)
        self.currentQuestion = self.questions[self.currentNumber]
        self.currentOptions = self.options[self.currentNumber]
        self.currentAnswer = self.answers[self.currentNumber]

        self.questionPic = self.font.render(self.currentQuestion, True,self.textColour)
        self.optionsPic = [self.font.render("1. " + self.currentOptions[0], True,self.textColour),
                           self.font.render("2. " + self.currentOptions[1], True,self.textColour),
                           self.font.render("3. " + self.currentOptions[2], True,self.textColour)]

    def update(self,win,player,currentGameState,bgImage):
        for zone in self.loadZones:
            if zone.check(player):
                gameState.state=zone.destination
                return
        if self.coolDown:
            self.inputCooldown -= 1
            if self.inputCooldown <= 0:
                self.coolDown = False
                self.inputCooldown = 16
        if self.spoutExpo:
            self.audio.startYapThread(self.witchYap[0])
            self.spoutExpo = False
        if self.yapTimer > 0:
            self.yapTimer -= 1

        if self.gameOn:
            player.canMove = False
            player.rect.center = (800,700)
        pressed_keys = pygame.key.get_pressed()
        if not self.coolDown:
            if pressed_keys[pygame.K_1]:
                if self.currentAnswer == 1:
                    self.audio.startYapThread("You Dare, well try this one then")
                    self.questionsAnswered += 1
                    if self.questionsAnswered >= 3:
                        self.endGame(currentGameState)
                        player.canMove = True
                else:
                    self.audio.startYapThread("Ha, cocky fool")
                self.reloadQuestions()
            elif pressed_keys[pygame.K_2]:
                if self.currentAnswer == 2:
                    self.audio.startYapThread("We have a smarty pants it seems, how about this then")
                    self.questionsAnswered += 1
                    if self.questionsAnswered >= 3:
                        self.endGame(currentGameState)
                        player.canMove = True
                else:
                    self.audio.startYapThread("Someone clearly overestimated themself")
                self.reloadQuestions()
            elif pressed_keys[pygame.K_3]:
                if self.currentAnswer == 3:
                    self.audio.startYapThread("Nerd")
                    self.questionsAnswered += 1
                    if self.questionsAnswered >= 3:
                        self.endGame(currentGameState)
                        player.canMove = True
                else:
                    self.audio.startYapThread("Nuh uh")
                self.reloadQuestions()




        self.draw(win,bgImage)
    def reloadQuestions(self):
        if len(self.askedQuestions) == len(self.questions):
            self.audio.startYapThread("suffer for eternity buffoon")
            self.currentQuestion = ""
            self.currentOptions = ["","",""]
            self.currentAnswer = 0
        else:
            self.coolDown = True
            self.currentNumber = random.randint(0, 8)
            while self.currentNumber in self.askedQuestions:
                self.currentNumber = random.randint(0, 8)
            self.askedQuestions.append(self.currentNumber)
            self.currentQuestion = self.questions[self.currentNumber]
            self.currentOptions = self.options[self.currentNumber]
            self.currentAnswer = self.answers[self.currentNumber]

            self.questionPic = self.font.render(self.currentQuestion, True, self.textColour)
            self.optionsPic = [self.font.render("1. " + self.currentOptions[0], True, self.textColour),
                           self.font.render("2. " + self.currentOptions[1], True, self.textColour),
                           self.font.render("3. " + self.currentOptions[2], True, self.textColour)]


    def endGame(self,currentGameState):
        self.gameOn = False
        currentGameState.states[0].houseCount += 1
        self.loadZones.append(loadZone(950,650,0,150,150,156,156))


    def draw(self,win,bgImage):
        win.fill((139,0,139))
        win.blit(sheepSprite,(100,600))
        win.blit(houseSprites[4],(100,40))
        win.blit(portalSprite, (900, 600))

        if self.gameOn:
            win.blit(witchSprite,(550,450))
            win.blit(self.questionPic,(700,50))
            for i, option in enumerate(self.optionsPic):
                win.blit(self.optionsPic[i],(700,100+i*100))
