import pygame


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

STEP = 10


pygame.init()

display = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

x = 100
y = 100
x_step = -STEP
y_step = STEP

# Game Loop
while True:
    # 1. Collect user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_step = -STEP
            if event.key == pygame.K_RIGHT:
                x_step = STEP
            if event.key == pygame.K_UP:
                y_step = -STEP
            if event.key == pygame.K_DOWN:
                y_step = STEP

    # 2. Move
    x += x_step
    y += y_step

    # 3. Update UI
    # Erase
    display.fill(BLACK)

    pygame.draw.rect(display, RED, pygame.Rect(x, y, 10, 10))

    pygame.display.flip()

    # 4. Control game time
    clock.tick(24)

pygame.quit()