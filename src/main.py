import pygame
from Slayer import Player
from flowerStage import flowerStage
from homeStage import homeStage
from gameState import gameState
from yapper import yapper
from rock import rockStage
from menu import menu
from pygame.locals import (

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
gs=gameState([homeStage(0),rockStage(),rockStage(),flowerStage(),rockStage()])
while running:

    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()



    if game:
        all_sprites.update(pressed_keys)

        # Fill the screen with black
        gs.drawState(screen,player,images)
        # if not neuphonicGameMode:
        #     screen.fill("purple")  # Fill the display with a solid color
        # if neuphonicGameMode:
        #     screen.fill("red")

        # Draw the player on the screen
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
