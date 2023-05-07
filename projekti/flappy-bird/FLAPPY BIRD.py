import pygame
import random
pygame.init()

SCREEN_WIDTH=640
SCREEN_HEIGHT=480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running=True
pygame.display.set_caption('Flappy Bird')
class player:
 def __init__(self):
        self.x = (SCREEN_WIDTH // 2)

while running:
        def draw(self, surface):
                pygame.draw.circle(surface, (255, 255, 255), (self.x, SCREEN_HEIGHT, 30))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        running = False
        #screen.blit(,(0,0))


        screen.fill("lightblue")



                        
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
