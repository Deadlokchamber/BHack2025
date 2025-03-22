import pygame
from src.yapper import yapper
pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

neuphonicGameMode=False
announcer =yapper()
#announcer.yap("Welcome to the game")
while True:
    
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...
    if not neuphonicGameMode:
        screen.fill("purple")  # Fill the display with a solid color
    if neuphonicGameMode:
        screen.fill("red")
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
