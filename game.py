import pygame
from pygame.math import Vector2
import sys
import random

pygame.init()
# Game display surface
cell_size = 40
cell_count = 20
game_screen = pygame.display.set_mode((cell_size * cell_count,
                                       cell_size * cell_count))
pygame.display.set_caption('Snake Game')
# To restrict program's frame rate
clock = pygame.time.Clock()


# Snake Class
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]

    def draw_snake(self):
        for part in self.body:
            # Create a rectangle snake's body part surface
            x_pos = part.x * cell_size
            y_pos = part.y * cell_size
            snake_rect = pygame.Rect(x_pos, y_pos,
                                     cell_size, cell_size)
            # Draw the body part on above surface
            pygame.draw.rect(game_screen, (255, 0, 0), snake_rect)


# Fruit Class
class Fruit:
    def __init__(self):
        # X and Y position of Fruit
        self.x = random.randint(0, cell_count - 1)
        self.y = random.randint(0, cell_count - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        # Create a rectangle surface using x,y coordinate, width and height.
        fruit_rect = pygame.Rect(self.pos.x * cell_size,
                                 self.pos.y * cell_size,
                                 cell_size, cell_size)
        # Draw the above fruit surface on game_screen
        pygame.draw.rect(game_screen, (0, 100, 0), fruit_rect)


# Instantiating Fruit object
fruit = Fruit()
# Instantiating Snake object
snake = Snake()

while True:
    # Start of every iteration we check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_screen.fill((175, 215, 70))
    fruit.draw_fruit()
    snake.draw_snake()
    # Refreshing game surface
    pygame.display.update()
    # Restricting while loop to run 60 times per second
    clock.tick(60)
