import pygame
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BRICK_WIDTH = 80
BRICK_HEIGHT = 20

class Brick:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dead = False

    def draw(self, surface):
        if not self.dead:
            pygame.draw.rect(surface, self.color, (self.x, self.y, BRICK_WIDTH, BRICK_HEIGHT))

    def die(self):
        self.dead = True

class Player:
    def __init__(self):
        self.x = (SCREEN_WIDTH // 2) - (BRICK_WIDTH // 2)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, SCREEN_HEIGHT - BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT))

    def move(self, dx):
        self.x += dx
        if self.x > SCREEN_WIDTH - BRICK_WIDTH:
            self.x = SCREEN_WIDTH - BRICK_WIDTH
        if self.x < 0:
            self.x = 0

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.vx = 0.0
        self.vy = 5.0

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', (self.x, self.y), 5)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def bounce(self):
        self.vx = -self.vx + random.randint(-2, 2)
        self.vy = -self.vy + random.randint(-2, 2)

    def collides_with_screen(self):
        return self.x > SCREEN_WIDTH or self.x < 0 or self.y < 0

    def collides_with_rect(self, x, y, width, height):
        return x <= self.x <= (x + width) and y <= self.y <= (y + height)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

player = Player()
bricks = []
colors = ['blue', 'red', 'white']

for x in range(0, SCREEN_WIDTH, BRICK_WIDTH):
    for y in range(0, SCREEN_HEIGHT // 3, BRICK_HEIGHT):
        bricks.append(Brick(x, y, colors[(x + y) % 3]))
ball = Ball()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move(10)
    if keys[pygame.K_LEFT]:
        player.move(-10)
    if ball.collides_with_screen():
        ball.bounce()
    for brick in bricks:
        if brick.dead:
            continue
        if ball.collides_with_rect(brick.x, brick.y, BRICK_WIDTH, BRICK_HEIGHT):
            brick.die()
            ball.bounce()
    if ball.collides_with_rect(player.x, SCREEN_HEIGHT - BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT):
        ball.bounce()
    if ball.y > SCREEN_HEIGHT:
        running = False

    screen.fill('black')
    player.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
