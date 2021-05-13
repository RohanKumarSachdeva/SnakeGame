import pygame, sys

# Initializing pygame
pygame.init()
# Game surface
screen_width = 1280
screen_height = 900
game_screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    # Start of every iteration we check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # Draw all elements
    pygame.display.update()
