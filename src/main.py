import pygame
from Slayer import Player
from flowerStage import flowerStage
from woodStage import WoodStage
from homeStage import homeStage
from gameState import gameState
from yapper import yapper
from rock import rockStage
from fireStage import fireStage
from menu import menu
from sheepStage import *
from pygame.locals import (

    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
def sysQuit():
    pygame.quit()
    raise SystemExit

images=input("Do you want background images on?(y/n): ").lower()=='y'
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1216
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()
menu = menu()

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

clock = pygame.time.Clock()
rock = rockStage()
# Variable to keep the main loop running
running = True
neuphonicGameMode=False
#announcer =speakOrSomething()
#announcer.yap("Welcome to the game")
menuRun = True
game = False

# Main loop



gs=gameState([homeStage(0),rockStage(),WoodStage(),fireStage(),flowerStage(),sheepStage()])

while running:

    for event in pygame.event.get():
        # Check for KEYDOWN event
        
        if event.type == KEYDOWN:
            if gameState.state==2:
                if event.key == K_LEFT:
                    gs.states[2].left()
                if event.key == K_RIGHT:
                    gs.states[2].right()
                if event.key == K_UP:
                    gs.states[2].up()
                if event.key == K_DOWN:
                    gs.states[2].down()
                if event.key == K_SPACE:
                    gs.states[2].hit()
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        elif event.type ==pygame.MOUSEBUTTONDOWN and gameState.state==3:
            gs.states[3].mouseDown(pygame.mouse.get_pos(),screen)
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()




    if game:

        gs.drawState(screen,player,images)


        # Draw the player on the screen
        if gameState.state!=2:
            all_sprites.update(pressed_keys)
            all_sprites.draw(screen)
    if menuRun:
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_UP]:
            menu.swapState()
        if pressed_keys[pygame.K_RETURN]:
            if menu.currentState == 0:
                menuRun = False
                game = True
            else:
                running = False
        menu.update(screen,images)




    # Update the display
    pygame.display.flip()  # Refresh on-screen display

    clock.tick(60)


win = pygame.display.set_mode((1920,960))
