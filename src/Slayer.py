import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
class Player(pygame.sprite.Sprite):
    def __init__(self, sw, sh):
        super(Player, self).__init__()
        self.canMove = True
        self.image_up = pygame.image.load('../Images/Clunk/clunk-forward.png')
        self.image_down = pygame.image.load('../Images/Clunk/clunk-backward.png')
        self.image_left = pygame.image.load('../Images/Clunk/clunk-left.png')
        self.image_right = pygame.image.load('../Images/Clunk/clunk-right.png')
        self.image = self.image_down
        self.sw = sw
        self.sh = sh

        



        self.rect = self.image.get_rect()
        self.rect.center = (self.sw // 2, self.sh // 2)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys, stage, stageNumber):
        if self.canMove:
            if pressed_keys[K_UP]:
               self.rect.move_ip(0, -5)
               self.image = self.image_down
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                self.image = self.image_up
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.image = self.image_left
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.image = self.image_right
            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > self.sw:
                self.rect.right = self.sw
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.sh:
                self.rect.bottom = self.sh

        if (stageNumber == 5):
            self.flowerCollide(stage.flowers)

    def flowerCollide(self,flowers):
        for flower in flowers:
            if flower.hitbox.colliderect(self.rect):
                flower.discovered = True
                self.rect.center=(608,0)
