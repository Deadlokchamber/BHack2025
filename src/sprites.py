import pygame as pg
from constants import *
from Slayer import Player
vec = pg.math.Vector2




class Player(Player):
    def __init__(self, game, x, y):
        self.image_up = pg.image.load('../Images/Clunk/clunk-forward.png')
        self.image_down = pg.image.load('../Images/Clunk/clunk-backward.png')
        self.image_left = pg.image.load('../Images/Clunk/clunk-left.png')
        self.image_right = pg.image.load('../Images/Clunk/clunk-right.png')
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.image_up
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
    
    def changeDirection(self, dir):
        if dir == 0:
            self.image = self.image_up
        elif dir == 1:
            self.image = self.image_down
        elif dir == 2:
            self.image = self.image_left
        elif dir == 3:
            self.image = self.image_right
        self.image = pg.transform.scale(self.image, (70, 70))
        

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE