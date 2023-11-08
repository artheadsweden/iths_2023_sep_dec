import pygame
from enum import Enum
import random
import numpy as np

# Constants
BLOCK_SIZE = 20
SPEED = 20

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
RED = (255, 0, 0)
GREEN1 = (0, 255, 0)
GREEN2 = (100, 255, 0)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class SnakeGame:
    def __init__(self, width=640, height=480, speed=SPEED):
        self.speed = speed
        pygame.init()
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont('arial', 25)

        # Init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.head = None
        self.body = None
        self.direction = None
        self.score = 0
        self.food = None
        self.frame_iteration = 0
        self.iterations_since_reward = 0
        self.reset()

    def reset(self):
        # Init game state
        self.direction = Direction.RIGHT
        self.head = Point(self.width/2, self.height/2)
        self.body = [self.head,
                     Point(self.head.x - BLOCK_SIZE, self.head.y),
                     Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.frame_iteration = 0
        self.iterations_since_reward = 0
        self._place_food()


    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.body:
            self._place_food()

    def _move(self):
        new_head = self.body.pop()
        if self.direction == Direction.RIGHT:
            new_head.x = self.head.x + BLOCK_SIZE
            new_head.y = self.head.y
        elif self.direction == Direction.LEFT:
            new_head.x = self.head.x - BLOCK_SIZE
            new_head.y = self.head.y
        elif self.direction == Direction.DOWN:
            new_head.y = self.head.y + BLOCK_SIZE
            new_head.x = self.head.x
        elif self.direction == Direction.UP:
            new_head.y = self.head.y - BLOCK_SIZE
            new_head.x = self.head.x

        self.body.insert(0, new_head)
        self.head = new_head

    def _extend_snake(self):
        new_tail = Point(0, 0)
        if self.direction == Direction.RIGHT:
            new_tail.x = self.body[-1].x - BLOCK_SIZE
            new_tail.y = self.body[-1].y
        elif self.direction == Direction.LEFT:
            new_tail.x = self.body[-1].x + BLOCK_SIZE
            new_tail.y = self.body[-1].y
        elif self.direction == Direction.DOWN:
            new_tail.y = self.body[-1].y - BLOCK_SIZE
            new_tail.x = self.body[-1].x
        elif self.direction == Direction.UP:
            new_tail.y = self.body[-1].y + BLOCK_SIZE
            new_tail.x = self.body[-1].x

        self.body.append(new_tail)

    def is_collision(self, point=None):
        if not point:
            point = self.head
        # Check if snake hits itself
        if point in self.body[1:]:
            return True

        # hits wall
        return point.x > self.width - BLOCK_SIZE or \
           point.x < 0 or \
           point.y > self.height - BLOCK_SIZE or \
           point.y < 0

    def _update_ui(self):
        self.display.fill(BLACK)

        pygame.draw.rect(self.display, GREEN1, pygame.Rect(self.head.x, self.head.y, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.display, GREEN2,
                         pygame.Rect(self.head.x + 4, self.head.y + 4, BLOCK_SIZE - 8, BLOCK_SIZE - 8))

        for body_part in self.body[1:]:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(body_part.x, body_part.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(body_part.x + 4, body_part.y + 4, BLOCK_SIZE - 8, BLOCK_SIZE - 8))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.display.blit(text, (0, 0))
        pygame.display.flip()

    def play_step_human(self):
        # 1. Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                if event.key == pygame.K_UP:
                    self.direction = Direction.UP
                if event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        # 2. Move
        self._move()

        # 3. Check if game is over
        if self.is_collision():
            return True

        # 4. Check if food is reached
        if self.head == self.food:
            self.score += 1
            self._place_food()
            # extend snake
            self._extend_snake()

        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(self.speed)

        # 6. Return game state
        return False

    def play_step_ai(self, action):
        self.iterations_since_reward += 1
        # 1. Collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Convert ai action to new direction

        #  [straight, right, left]
        #  [1, 0, 0]  -> Keep on going straight
        #  [0, 1, 0]  -> Turn right
        #  [0, 0, 1]  -> Turn left
        clockwise_dir = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        dir_idx = clockwise_dir.index(self.direction)

        if np.array_equal(action, [0, 1, 0]):  # Turn right
            dir_idx = (dir_idx + 1) % len(clockwise_dir)
        if np.array_equal(action, [0, 0, 1]):  # Turn left
            dir_idx = (dir_idx - 1) % len(clockwise_dir)
        self.direction = clockwise_dir[dir_idx]
        # 2. Move
        self._move()

        # 3. Check if game is over
        reward = 0
        if self.is_collision():
            return True, -10, self.score
        elif self.iterations_since_reward > 100 * len(self.body):
            return True, -5, self.score

        # 4. Check if food is reached
        if self.head == self.food:
            self.score += 1
            self.iterations_since_reward = 0
            self._place_food()
            # extend snake
            self._extend_snake()
            reward = 10
        # 5. Update UI and clock
        self._update_ui()
        self.clock.tick(self.speed)

        # 6. Return game state
        return False, reward, self.score


    @staticmethod
    def human_play():
        game = SnakeGame()
        # Game Loop
        while True:
            game_over = game.play_step_human()
            if game_over:
                break
        print('Final Score:', game.score)