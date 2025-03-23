import random 
import pygame as pg
import sys
from os import path
from block import loadZone
from gameState import gameState
from sprites import *
from tilemap import *

class WoodStage:
    def __init__(self):
        pg.init()
        window = pg.display.set_mode((WIDTH, HEIGHT))
        
        self.clock = pg.time.Clock()
        self.load_data()
        self.mobs =[]
        self.new()
        self.wood = False
        self.loadZones=[loadZone(1196,0,0,596,384,20,800)]

        
    def load_data(self):
        self.mapno = random.randint(1, 5)
        self.map = Map("map{}.txt".format(self.mapno*2))
        self.background = pg.image.load('../Images/treeback.png') 
        

    def new(self):
        # initialize all variables and do all the setup for a new game
        
        self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'M':
                    self.mobs.append(Mob(self, col, row))
                if tile == 'W':
                    self.goal = Wood(self, col, row)
                if tile == 'E':
                    self.leave = Exit(self,col,row)
        self.camera = Camera(self.map.width, self.map.height)


    def quit(self):
        pg.quit()
        sys.exit()

    def update(self,window,player,currentGameState,bgImage):
        
           
        self.draw(window)
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        if self.wood and self.player.x == self.leave.x and self.player.y == self.leave.y:
            player.rect.center=(608,400)
            gameState.state = 0
            currentGameState.states[0].houseCount += 1
            return "Wood gotem"



    def draw(self,window):
        window.blit(self.background, (0, 0))
        #self.draw_grid()
        for sprite in self.all_sprites:
            #print(sprite,self.camera.apply(sprite))
            window.blit(sprite.image, self.camera.apply(sprite))
        

    def left(self):
        self.player.move(dx=-1)
        self.player.changeDirection(2)
        self.moveMobs()
    def right(self):
        
        self.player.move(dx=1)
        self.player.changeDirection(3)
        self.moveMobs()
    def up(self):
        
        self.player.move(dy=-1)
        self.player.changeDirection(1)
        self.moveMobs()
    def down(self):
        self.player.move(dy=1)
        self.player.changeDirection(0)
        self.moveMobs()

    def hit(self):
        self.player.hit()
        self.moveMobs()
    


                    
    def moveMobs(self):
        for mob in range(len(self.mobs)):
            self.mobs[mob].randMove()
                    




