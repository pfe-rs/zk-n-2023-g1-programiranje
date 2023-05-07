import pygame
import random
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BRICK_WIDTH = 26
BRICK_HEIGHT = 26
SWIDTH=20
SHEIGHT=5
b=0
pygame.font.init()
pygame.font.get_fonts()
myfont = pygame.font.SysFont("monospace", 30)
# e=pygame.image.load("space-invaders-icon-33.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Shield:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dead = False

    def draw(self, surface):
        if not self.dead:
            pygame.draw.rect(surface, self.color, (self.x, self.y, SWIDTH, SHEIGHT))\
            
    def die(self):
        self.dead = True


class Enemy:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = 0.6
        self.vy = 0.0
        self.color = color
        self.dead = False
        

    def draw(self, surface):
        if not self.dead:
            pygame.draw.rect(surface, self.color, (self.x, self.y, BRICK_WIDTH, BRICK_HEIGHT))\
            #screen.blit(e,(self.x, self.y))
    
    def collides_with_wall(self, s_width, width):
        return (self.x + s_width > width or self.x < 0) and not(self.dead)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
    
    def die(self):
        self.dead = True

    def shoote(self):
        return self.x, self.y
    
    def movey (self):
        self.y += 15

    def minusx (self):
        self.vx = -self.vx

class Player:
    def __init__(self):
        self.x = (SCREEN_WIDTH // 2) - (BRICK_WIDTH // 2)
        self.y = SCREEN_HEIGHT - BRICK_HEIGHT
        self.dead = False
        self.lives = 3

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, SCREEN_HEIGHT - BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT))

    def move(self, dx):
        self.x += dx
        if self.x > SCREEN_WIDTH - BRICK_WIDTH:
            self.x = SCREEN_WIDTH - BRICK_WIDTH
        if self.x < 0:
            self.x = 0

    def die(self):
        self.dead = True
    
    def shoot(self):
        return self.x, self.y

class Bullet:
    def __init__(self, x, y, color):
        self.x = x + BRICK_WIDTH//2
        self.y = y
        self.color = color
        self.vx = 0.0
        self.vy = -5.0
        self.dead = False

    def draw(self, surface):
        if not self.dead:
            pygame.draw.circle(surface, (255,255,255), (self.x, self.y), 3)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def collides_with_enemy_dissapear(self, x, y, width, height):
        return x <= self.x <= (x + width) and y <= self.y <= (y + height)
    
    def die(self):
        self.dead = True

    def collides_with_shield(self, x, y, width):
        return x <= self.x <= (x + width) and y <= self.y <= (y + SHEIGHT)
   
class Bullete:
    def __init__(self, x, y, color):
        self.x = x + BRICK_WIDTH//2
        self.y = y + BRICK_HEIGHT//2
        self.vx = 0.0
        self.vy = 5.0
        self.dead = False
        self.color = color

    def draw(self, surface):
        if not(bullete.dead):
            pygame.draw.circle(surface, (255,255,255), (self.x, self.y), 3)

    def update(self):
        self.x += self.vx
        self.y += self.vy
    
    def collides_with_player_dissapear(self, x, y, width, height):
        return x <= self.x <= (x + width) and y <= self.y <= (y + height)
    
    def die(self):
        self.dead = True

    def collides_with_shield(self, x, y, width):
        return x <= self.x <= (x + width) and y <= self.y <= (y + SHEIGHT)
    

pygame.init()

clock = pygame.time.Clock()
running = True

player = Player()
enemies = []
color = 'white'
bullets = []
bulletse = []
t1 = 20
shieldi = []

for x in range(80, SCREEN_WIDTH - 80, BRICK_WIDTH + 40):
    for y in range(10, SCREEN_HEIGHT // 3, BRICK_HEIGHT + 20):
        enemies.append(Enemy(x, y, color))

for x in range(180, SCREEN_WIDTH - 180, SWIDTH):
    shieldi.append(Shield(x, 410, color))


t=random.randint(60,180)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and t1<0:
                x, y = player.shoot()   
                bullets.append(Bullet(x, y, color))
                t1 = 20

    t1 -= 1

    for enemy in enemies:
        if enemy.dead:
            enemies.remove(enemy)
    
    s=False
    
    t-=1

    if 0>t:
        i=random.randint(0,len(enemies)-1)
        enemy1 = enemies[i]
        x, y = enemy1.shoote()   
        bulletse.append(Bullete(x, y, color))
        t=random.randint(60,120)

    k=False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move(4)
    if keys[pygame.K_LEFT]:
        player.move(-4)

    for bullet in bullets:
        bullet.update()
    for bullete in bulletse:
        bullete.update()
    for enemy in enemies:
        enemy.update()

    for enemy in enemies:
        if enemy.collides_with_wall(BRICK_WIDTH, SCREEN_WIDTH):
            s=True
    if s==True:
        for enemy in enemies:
            enemy.minusx()
            enemy.movey()

    for bullet in bullets:
        if bullet.dead:
            continue
    
    for enemy in enemies:
        if enemy.dead:
            enemies.remove(enemy)
        for bullet in bullets:
            if not bullet.dead:
                if bullet.collides_with_enemy_dissapear(enemy.x, enemy.y, BRICK_WIDTH, BRICK_HEIGHT):
                    enemy.die()
                    bullet.die()
                    b+=10

    
    for bullete in bulletse:
        if not bullete.dead:
            if bullete.collides_with_player_dissapear(player.x, player.y, BRICK_WIDTH, BRICK_HEIGHT) and not(shield.dead):
                player.lives -= 1
                bullete.die()
                player.x=SCREEN_WIDTH//2
            for shield in shieldi:
                if bullete.collides_with_shield(shield.x, shield.y, SWIDTH) and not(shield.dead):
                    bullete.die()
                    shield.die()

    for bullet in bullets:
        for shield in shieldi:
                if bullet.collides_with_shield(shield.x, shield.y, SWIDTH) and not(shield.dead):
                    bullet.die()
                    shield.die()
    
                
    if player.lives==0:
        k=True

    screen.fill('black')

    for enemy in enemies:
        if enemy.y > SCREEN_HEIGHT - BRICK_HEIGHT - BRICK_HEIGHT:
            myfont = pygame.font.SysFont("monospace", 40)
            label3 = myfont.render("Game Over", 1, (255,100,100))
            screen.blit(label3, (150, 100))
            pygame.time.wait(500)
            for enemy in enemies:
                enemy.die() 
            break
    
    if k:
        myfont = pygame.font.SysFont("monospace", 40)
        label1 = myfont.render("Game Over", 1, (255,100,100))
        screen.blit(label1, (150, 100))
        pygame.time.wait(500)
        for enemy in enemies:
            enemy.die()
        


    if b==320 and not(player.dead):
        myfont = pygame.font.SysFont("monospace", 40)
        label2 = myfont.render("Victory", 1, (255,100,100))
        screen.blit(label2, (150, 100))
        pygame.time.wait(500)

    label = myfont.render(str(b)+"/320", 1, (255,255,255))
    screen.blit(label, (100, 370))
    labell = myfont.render(str(player.lives)+"/3 lives", 1, (255,255,255))
    screen.blit(labell, (100, 320))
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)
    for bullete in bulletse:
        bullete.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for shield in shieldi:
        shield.draw(screen)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
  