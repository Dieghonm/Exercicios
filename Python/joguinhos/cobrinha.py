import pygame
import random
import sys

# Definições de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definições do jogo
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
CELL_SIZE = 20
FPS = 10

class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = (head[0], head[1] - CELL_SIZE)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + CELL_SIZE)
        elif self.direction == "LEFT":
            new_head = (head[0] - CELL_SIZE, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + CELL_SIZE, head[1])

        self.body.insert(0, new_head)

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def grow(self):
        self.body.append(self.body[-1])

class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE * CELL_SIZE,
                         random.randint(0, SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE * CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        screen.fill(BLACK)
        snake.move()

        # Verifica se a cobra comeu a comida
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()

        # Verifica se a cobra bateu na parede ou em si mesma
        if (snake.body[0][0] < 0 or snake.body[0][0] >= SCREEN_WIDTH
                or snake.body[0][1] < 0 or snake.body[0][1] >= SCREEN_HEIGHT
                or snake.body[0] in snake.body[1:]):
            running = False

        snake.draw(screen)
        food.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
