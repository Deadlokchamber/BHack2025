import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clunk = pygame.image.load_extended("Images/Clunk/clunk-forward.png")

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
win = pygame.display.set_mode((1920,960))

while True:
    print("running")