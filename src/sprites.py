from random import randint
import pygame as pg
from constants import *
from Slayer import Player
from tilemap import Map
vec = pg.math.Vector2


class Wood(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = pg.image.load('../Images/log.png')
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Player(Player):
    def __init__(self, game, x, y):
        self.image_up = pg.image.load('../Images/Clunk/clunk-forward.png')
        self.image_down = pg.image.load('../Images/Clunk/clunk-backward.png')
        self.image_left = pg.image.load('../Images/Clunk/clunk-left.png')
        self.image_right = pg.image.load('../Images/Clunk/clunk-right.png')
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.image_up
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.groups = game.all_sprites
        self.dir = 0
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
    def hit(self):
        if self.dir == 0:
            target_x = self.x
            target_y = self.y + 1  
        elif self.dir == 1:
            target_x = self.x
            target_y = self.y - 1  
        elif self.dir == 2:
            target_x = self.x - 1 
            target_y = self.y
        elif self.dir == 3:
            target_x = self.x + 1  
            target_y = self.y

        for mob in self.game.mobs:
            if mob.x == target_x and mob.y == target_y:
                self.game.mobs.remove(mob)
                mob.kill() 
                
                if len(self.game.mobs) == 0:
                    
                    temp = [self.x, self.y]
                    imgtemp = self.image
                    
                    # Keep the player’s current position in temp
                    current_player_x, current_player_y = self.x, self.y
                    self.kill()
                    

                    self.game.map = Map("map1.txt")  # Swap maps when enemies are dead
                    self.game.new() 
                    
                    self.player = Player(self.game, current_player_x, current_player_y)  # Respawn player at the same position
                    self.player.image = imgtemp
                    self.game.all_sprites.add(self.player)  # Add the new player to the sprite group
        
        # Rebind the controls (if applicable)
                    self.game.player = self.player  # Make sure the game knows about the new player instance
                return  
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
    
    def changeDirection(self, dir):
        if dir == 0:
            self.image = self.image_up
            self.dir = 0
        elif dir == 1:
            self.image = self.image_down
            self.dir = 1
        elif dir == 2:
            self.image = self.image_left
            self.dir = 2
        elif dir == 3:
            self.image = self.image_right
            self.dir = 3
        self.image = pg.transform.scale(self.image, (70, 70))
        

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.image_up = pg.image.load('../Images/Ent/up.png')
        self.image_down = pg.image.load('../Images/Ent/down.png')
        self.image_left = pg.image.load('../Images/Ent/left.png')
        self.image_right = pg.image.load('../Images/Ent/right.png')
        self.groups = game.all_sprites, game.walls
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
            self.changeDir()
        else:
            self.randMove()
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def randMove(self):
        self.dir = randint(0,3)
        if self.dir == 0:
            self.move(1, 0)
        elif self.dir == 1:
            self.move(-1, 0)

        elif self.dir == 2:
            self.move(0, -1)

        elif self.dir == 3:
            self.move(0, 1)

    
    def changeDir(self):
        if self.dir == 0:
            self.image = self.image_right
        elif self.dir == 1:
            self.image = self.image_left

        elif self.dir == 2:
            self.image = self.image_up

        elif self.dir == 3:
            self.image = self.image_down

        self.image = pg.transform.scale(self.image, (70, 70))

     
class Exit(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = pg.transform.scale(pg.image.load('../Images/Tree.png'), (70, 70))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE