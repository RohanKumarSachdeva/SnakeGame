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
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for part in self.body:
            # Create a rectangle snake's body part surface
            x_pos = part.x * cell_size
            y_pos = part.y * cell_size
            snake_rect = pygame.Rect(x_pos, y_pos,
                                     cell_size, cell_size)
            # Draw the body part on above surface
            pygame.draw.rect(game_screen, (255, 0, 0), snake_rect)

    def move_snake(self):
        # Copy body parts from head to tail-1
        body_copy = self.body[:-1]
        # Create a new head that has moved in right direction
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy


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

    def respawn_fruit(self):
        self.x = random.randint(0, cell_count - 1)
        self.y = random.randint(0, cell_count - 1)
        self.pos = Vector2(self.x, self.y)


# Game logic class
class Main:
    def __init__(self):
        # Create snake and fruit class objects with main class object.
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.respawn_fruit()


main_game = Main()
# Creating own screen update event
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    # Start of every iteration we check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # On KEY DOWN event we change snake.direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)

    game_screen.fill((175, 215, 70))
    main_game.draw_elements()
    # Refreshing game surface
    pygame.display.update()
    # Restricting while loop to run 60 times per second
    clock.tick(60)
