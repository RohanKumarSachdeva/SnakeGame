import pygame
import sys

# Initializing pygame
pygame.init()
# Game display surface
screen_width = 1280
screen_height = 900
game_screen = pygame.display.set_mode((screen_width, screen_height))
# To restrict programs frame rate
clock = pygame.time.Clock()
while True:
    # Start of every iteration we check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Refreshing game surface
    pygame.display.update()
    # Restricting while loop to run 60 times per second
    clock.tick(60)
