import pygame
import sys

pygame.init()
# Game display surface
screen_width = 1280
screen_height = 900
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
# To restrict program's frame rate
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill((0, 0, 255))

while True:
    # Start of every iteration we check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_screen.fill((175, 215, 70))
    game_screen.blit(test_surface, (200, 250))
    # Refreshing game surface
    pygame.display.update()
    # Restricting while loop to run 60 times per second
    clock.tick(60)
