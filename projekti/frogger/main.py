import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CAR_WIDTH = 30
CAR_HEIGHT = 30
SZ_HEIGHT = 40
font = pygame.font.Font('Minecrafter.ttf',90)
font_s = pygame.font.Font('Minecrafter.ttf',20)
lives = 3
class Player:
     def __init__(self):
        
        self.x = SCREEN_WIDTH//2 -5
        self.y = SCREEN_HEIGHT-CAR_HEIGHT
     def draw(self, surface):
        pygame.draw.rect(surface, 'white', (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))
     def move(self,dx,dy):
         self.x+=dx  
         self.y+=dy  
         if self.x>SCREEN_WIDTH-CAR_WIDTH:
             self.x = SCREEN_WIDTH-CAR_WIDTH
         if self.x<0:
             self.x = 0
         if self.y > SCREEN_HEIGHT-CAR_HEIGHT:
            self.y = SCREEN_HEIGHT-CAR_HEIGHT
         if self.y < 0:
              self.y = 0
     def die(self):
          self.x = SCREEN_WIDTH//2 -5
          self.y = SCREEN_HEIGHT-CAR_HEIGHT
     def collides_with_car(self,x,y,width,height):
          return x <= self.x <= (x+width) and y <= self.y <= (y+height)
     
        

class Car:
    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.dead = False
    def move(self):
        self.x += self.vx
    def draw(self, surface):
        if not self.dead:
          pygame.draw.rect(surface, 'red', (self.x, self.y, CAR_WIDTH, CAR_HEIGHT))
    def die(self):
        self.dead = True  

class SafeZone:
     def __init__(self, y, color):
          self.x = 0
          self.y = y
          self.color = color
          y = SCREEN_HEIGHT - SZ_HEIGHT
     def draw(self, surface):
          pygame.draw.rect(surface, self.color , (self.x, self.y, SCREEN_WIDTH, SZ_HEIGHT))
class Row:
     def __init__(self,y,color):
          self.x = 0
          self.y = y
          self.color = color
     def draw(self, surface):
          self.rect_row = pygame.Rect(self.x, self.y-SZ_HEIGHT, SCREEN_WIDTH, SZ_HEIGHT)
          pygame.draw.rect(surface, self.color ,self.rect_row)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
player = Player()
safezone = SafeZone(SCREEN_HEIGHT-SZ_HEIGHT, 'green')
safezone2 = SafeZone(SCREEN_HEIGHT-SZ_HEIGHT - 240, 'green')
end = SafeZone(0, 'purple')
player = Player()
rows = []
cars = []
game_over = font.render("GAME OVER", True, 'white', 'black')
game_overRect = game_over.get_rect()
game_overRect.center = 320, 240
winText = font.render("YOU WON!", True, 'white', 'black')
winRect = winText.get_rect()
winRect.center = 320, 240
p_image = pygame.image.load('player.png').convert_alpha()

for y in range(0, SCREEN_HEIGHT, CAR_HEIGHT):
     rows.append(Row(y, 'grey'))
sz_rect = pygame.Rect(safezone2.x, safezone2.y, SCREEN_WIDTH, SZ_HEIGHT)
end_rect = pygame.Rect(end.x, end.y, SCREEN_WIDTH, SZ_HEIGHT)
counter = random.randint(20,60)
crko = False
while running:
        screen.fill('black')
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  running = False
        
        n = random.randint(2,(SCREEN_HEIGHT/CAR_HEIGHT)-2)
        p = random.uniform(0,1)
        k = random.randint(2,5)
        x = 0
        ##p_rect = pygame.Rect(player.x, player.y, CAR_WIDTH, CAR_HEIGHT)
        p_rect = p_image.get_rect(center = (player.x, player.y+10))
        counter -= 4
        if counter <= 0 :
             if(p >= 0.5):
               k = k*(-1)
               x = SCREEN_WIDTH
             cars.append(Car(x, SCREEN_HEIGHT-n*SZ_HEIGHT, k))
             counter = random.randint(60,240)
        
        for row in rows:
             row.draw(screen)
        safezone.draw(screen)
        safezone2.draw(screen)
        end.draw(screen)
        for car in cars:
             if car.dead:
                  continue
             if car.y == 0 or car.y == safezone2.y - SZ_HEIGHT or car.y == safezone2.y + SZ_HEIGHT or car.y == end.y+SZ_HEIGHT: 
                  car.y = car.y+5
             car.draw(screen)
             car.move()
          
             c_rect = pygame.Rect(car.x, car.y, CAR_WIDTH, CAR_HEIGHT)

             if pygame.Rect.colliderect(p_rect, c_rect) == True:
                  lives-=1
                  player.die()
             if pygame.Rect.colliderect(c_rect, sz_rect) or pygame.Rect.colliderect(c_rect, end_rect):
                  car.die()
             
        screen.blit(p_image, p_rect)
        if pygame.Rect.colliderect(p_rect, end_rect):
                  win = True
                  break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
             player.move(2,0)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
             player.move(-2,0)
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
             player.move(0,-2)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
             player.move(0,2)
        if lives == 0:
             crko = True
             break
        
        pygame.display.flip()
        clock.tick(60)

while crko == True:
     for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  pygame.quit()
     screen.fill('black')
     screen.blit(game_over, game_overRect)
     pygame.display.flip()
     clock.tick(60)
while win == True:
     for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  pygame.quit()
     screen.fill('black')
     screen.blit(winText, winRect)
     pygame.display.flip()
     clock.tick(60)     
pygame.quit()
