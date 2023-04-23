import pygame
import random
 
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
#screen dimen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
#snake speed
SPEED = 10
 
# snake pos
x = 250
y = 250
 
#move x, y
vx = SPEED
vy = 0
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 

pygame.display.set_caption('Snake Game')
 
# apple pos
apple_side = 20

apple_x = random.randint(0, SCREEN_WIDTH-apple_side)
apple_y = random.randint(0, SCREEN_HEIGHT-apple_side)
 
# snake length n tail pos
snake_side = 20

snake_length = 1
snake_tail = [(x, y)]
 
font = pygame.font.Font(None, 36)
 
# start score
score = 0
 
# game over screen
def game_over():
    over_font = pygame.font.Font(None, 38)
    over_text = over_font.render('Game Over. Your score is ' + str(score), True, WHITE)
    screen.blit(over_text, [SCREEN_WIDTH/2 - over_text.get_width()/2, SCREEN_HEIGHT/2 - over_text.get_height()/2])
    over_font = pygame.font.Font(None, 20)
    over_text = over_font.render('Press SPACE to continue, press any key to escape', True, WHITE)
    screen.blit(over_text, [SCREEN_WIDTH/2 - over_text.get_width()/2, SCREEN_HEIGHT/2 - over_text.get_height()/2 + 30])
    pygame.display.update()
    pygame.time.wait(2000)

# main loop
done = False
game_over_screen = False
clock = pygame.time.Clock()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over_screen:
                game_over_screen = False
                x = 250
                y = 250
                vx = SPEED
                vy = 0
                snake_length = 1
                snake_tail = [(x, y)]
                score = 0
                SPEED = 10
            elif game_over_screen:
                done = True

            elif event.key == pygame.K_LEFT:
                vx = -SPEED
                vy = 0
            elif event.key == pygame.K_RIGHT:
                vx = SPEED
                vy = 0
            elif event.key == pygame.K_UP:
                vx = 0
                vy = -SPEED
            elif event.key == pygame.K_DOWN:
                vx = 0
                vy = SPEED
 
    num_apples = 1
    # apple eating
    if x < apple_x + apple_side and x + snake_side > apple_x and y < apple_y + apple_side and y + snake_side > apple_y:
        apple_x = random.randint(0, SCREEN_WIDTH-apple_side)
        apple_y = random.randint(0, SCREEN_HEIGHT-apple_side)
        snake_length += 1
        score += 10
            #speed up the snake
        SPEED += 0.5
 
    # collision with edges
    if x < 0 or x + snake_side > SCREEN_WIDTH or y < 0 or y + snake_side > SCREEN_HEIGHT:
        game_over_screen = True
 
    # self- harm
    for tail in snake_tail[:-1]:
        if x == tail[0] and y == tail[1]:
            game_over_screen = True
 
    # tail keeps following
    snake_tail.insert(0, (x, y))
    if len(snake_tail) > snake_length:
        snake_tail.pop()
 
    # snake pos
    x += vx
    y += vy
 

    # screen filling
    screen.fill(BLACK)
 
    # Draw apple, snake, score
    pygame.draw.rect(screen, RED, [apple_x, apple_y, apple_side, apple_side])

    for tail in snake_tail:
        pygame.draw.rect(screen, GREEN, [tail[0], tail[1], snake_side, snake_side])
 
    text = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(text, [10, 10])

    if game_over_screen:
        game_over()

    pygame.display.update()
 
    clock.tick(15)
 
pygame.quit()
