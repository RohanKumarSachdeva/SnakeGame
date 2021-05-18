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
apple = pygame.image.load("Graphics/apple-image.png").convert_alpha()


# Snake Class
class Snake:
    def __init__(self):
        self.head = None
        self.tail = None
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

    def update_head_graphics(self):
        relative_position = self.body[1] - self.body[0]
        if relative_position == Vector2(1, 0):
            self.head = self.head_left
        elif relative_position == Vector2(-1, 0):
            self.head = self.head_right
        elif relative_position == Vector2(0, 1):
            self.head = self.head_up
        elif relative_position == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        relative_position = self.body[-2] - self.body[-1]
        if relative_position == Vector2(1, 0):
            self.tail = self.tail_left
        elif relative_position == Vector2(-1, 0):
            self.tail = self.tail_right
        elif relative_position == Vector2(0, 1):
            self.tail = self.tail_up
        elif relative_position == Vector2(0, -1):
            self.tail = self.tail_down

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        # Using enumerate to get the index and element from array
        for index, part in enumerate(self.body):
            # Create a rectangle snake's body part surface
            x_pos = part.x * cell_size
            y_pos = part.y * cell_size
            snake_rect = pygame.Rect(x_pos, y_pos,
                                     cell_size, cell_size)
            # Find which direction the snake is heading
            if index == 0:
                game_screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                game_screen.blit(self.tail, snake_rect)
            else:
                relative_prev_part = self.body[index + 1] - part
                relative_next_part = self.body[index - 1] - part
                if relative_prev_part.x == relative_next_part.x:
                    game_screen.blit(self.body_vertical, snake_rect)
                elif relative_prev_part.y == relative_next_part.y:
                    game_screen.blit(self.body_horizontal, snake_rect)
                else:
                    if (relative_prev_part.x == -1 and relative_next_part.y == -1) or \
                            (relative_prev_part.y == -1 and relative_next_part.x == -1):
                        game_screen.blit(self.body_tl, snake_rect)
                    elif (relative_prev_part.x == -1 and relative_next_part.y == 1) or \
                            (relative_prev_part.y == 1 and relative_next_part.x == -1):
                        game_screen.blit(self.body_bl, snake_rect)
                    elif (relative_prev_part.x == 1 and relative_next_part.y == -1) or \
                            (relative_prev_part.y == -1 and relative_next_part.x == 1):
                        game_screen.blit(self.body_tr, snake_rect)
                    elif (relative_prev_part.x == 1 and relative_next_part.y == 1) or \
                            (relative_prev_part.y == 1 and relative_next_part.x == 1):
                        game_screen.blit(self.body_br, snake_rect)

    def move_snake(self):
        # Copy body parts from head to tail-1
        body_copy = self.body[:-1]
        # Create a new head that has moved in right direction
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def increase_snake(self):
        body_copy = self.body[:]
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
        game_screen.blit(apple, fruit_rect)
        # pygame.draw.rect(game_screen, (0, 100, 0), fruit_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.respawn_fruit()
            self.snake.increase_snake()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_count or \
                not 0 <= self.snake.body[0].y < cell_count:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    # noinspection PyMethodMayBeStatic
    # this because the method does not use self in its body and hence does
    # not actually change the class instance. Hence the method could be static,
    # i.e. callable without passing a class instance
    def game_over(self):
        pygame.quit()
        sys.exit()

    # noinspection PyMethodMayBeStatic
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_count):
            if row % 2 == 0:
                for column in range(cell_count):
                    if column % 2 == 0:
                        grass_rect = pygame.Rect(column * cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(game_screen, grass_color, grass_rect)
            else:
                for column in range(cell_count):
                    if column % 2 != 0:
                        grass_rect = pygame.Rect(column * cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(game_screen, grass_color, grass_rect)


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
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    game_screen.fill((175, 215, 70))
    main_game.draw_elements()
    # Refreshing game surface
    pygame.display.update()
    # Restricting while loop to run 60 times per second
    clock.tick(60)
