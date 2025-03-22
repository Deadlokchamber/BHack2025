import pygame
from Slayer import Player
from src.flowerStage import flowerStage
from src.homeStage import homeStage
from yapper import yapper
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


pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1216
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

clock = pygame.time.Clock()

# Variable to keep the main loop running
running = True
neuphonicGameMode=False
#announcer =speakOrSomething()
#announcer.yap("Welcome to the game")
# Main loop
stage = homeStage(1)
currentStage = 0
while running:

    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                print("Yeet")
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            print("Yeetos")
            running = False
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()


    all_sprites.update(pressed_keys, stage, currentStage)

    # Fill the screen with black

    if not neuphonicGameMode:
        screen.fill("purple")  # Fill the display with a solid color
    if neuphonicGameMode:
        screen.fill("red")

    # Draw the player on the screen
    stage.draw(screen)
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)

win = pygame.display.set_mode((1920,960))
