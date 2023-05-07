import pygame
import random
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CIRCLE_WIDTH = 15
SQUARE_WIDTH = 29
TRIANGLE_WIDTH = 15
score = 0
bos_spawned  = False
speed_lvl = 1.5
highscore = 0
spawn_sec = 0.5
speedUp = 0
bos_active=  False
boss_seconds = 15
speed = 1
gameOver = False
spawn_speed = 2
class Player:
    def __init__(self):
        self.x = 20
        self.y = 380
        self.health = 100
        self.dead = False
    def draw(self,surface):
        pygame.draw.circle(surface,'#0D98BA',(self.x+45,self.y), 35)
        pygame.draw.rect(surface, '#0D98BA', (self.x+10, self.y,70,60))
        pygame.draw.circle(surface,'white',(self.x+45,self.y), 20)
        pygame.draw.circle(surface,'black',(self.x+45,self.y), 10)
        pygame.draw.rect(surface, '#0D98BA', (self.x+20, self.y+30,10,60))
        pygame.draw.rect(surface, '#0D98BA', (self.x+40, self.y+40,10,60))
        pygame.draw.rect(surface, '#0D98BA', (self.x+60, self.y+30,10,60))
        pygame.draw.rect(surface, '#0D98BA', (self.x-10, self.y+30,30,10))
        pygame.draw.rect(surface, '#0D98BA', (self.x+70, self.y+30,30,10))
    def dying(self ,damage):
        self.health -=damage
        if self.health < 0 or self.health == 0:
            self.dead = True
class Objects:
    def __init__(self, tip):
        randGuess = random.randint(1,3)
        self.x  = 620
        self.y = 405
        self.tip = tip
        self.dead = False
    def draw(self, surface):
        if self.tip == 'krug':
            pygame.draw.circle(screen, 'red', (self.x, self.y-2), CIRCLE_WIDTH)
        if self.tip == 'trougao':
            pygame.draw.polygon(screen, 'red',[(self.x -27,self.y+13), (self.x  - 10, self.y-15), (self.x + 7, self.y+13)])
        if self.tip == 'kvadrat':
            pygame.draw.rect(screen, 'red', (self.x-20, self.y-15, SQUARE_WIDTH,SQUARE_WIDTH))
    def move(self, vx):
        self.x -= vx
    def pos(self):
        return self.x

    def die(self):
        self.dead = True
    
    def type(self):
        return self.tip
        
class Boss:
    def __init__(self,speed):
        self.x  = 620
        self.y = 380
        self.dead = False
        self.speed = speed
        self.health  =100
    def draw(self,surface): 
        pygame.draw.circle(surface,'red',(self.x+45,self.y), 35)
        pygame.draw.rect(surface, 'red', (self.x+10, self.y,70,60))
        pygame.draw.circle(surface,'white',(self.x+45,self.y), 20)
        pygame.draw.circle(surface,'black',(self.x+45,self.y+5), 10)
        pygame.draw.rect(surface, 'red', (self.x+20, self.y+30,10,60))
        pygame.draw.rect(surface, 'red', (self.x+40, self.y+40,10,60))
        pygame.draw.rect(surface, 'red', (self.x+60, self.y+30,10,60))
        pygame.draw.rect(surface, 'red', (self.x-10, self.y+30,30,10))
        pygame.draw.rect(surface, 'red', (self.x+70, self.y+30,30,10))
        pygame.draw.circle(surface, 'red', (self.x+45, self.y-15),20)
    def attack(self):
        self.x += self.speed
    def die(self):
        self.dead = True
    def posX(self, player):
        if bos.x - player < 10:
         return True
    
class Ammo:
    def __init__(self, tip):
        self.x = 230
        self.y = 445
        self.tip = tip
        self.dead = False
    def attack(self,surface):
        if self.tip == 'krug':      
            pygame.draw.circle(screen, '#23395d', (self.x+15, self.y-41), CIRCLE_WIDTH)
        if self.tip == 'trougao':
            pygame.draw.polygon(screen, '#23395d',[(self.x ,self.y -27), (self.x + 17, self.y -55), (self.x + 34, self.y -27)])
        if self.tip == 'kvadrat':
            pygame.draw.rect(screen, '#23395d', (self.x, self.y - 55, SQUARE_WIDTH,SQUARE_WIDTH))
    def move(self,vx):
        self.x += vx
    def collide_w_object(self):
        pass
    def die(self):
        self.dead = True
    def pos(self):
        return self.x
    def type(self):
        return self.tip

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


#Text
font = pygame.font.Font('mine-sweeper.ttf', 28)
title = font.render('TRIGOCRASH', True, 'black', 'orange')
titleRect = title.get_rect()
titleRect.center = (SCREEN_WIDTH // 2, 20)
#score
scoreTxt = font.render(f'Score: {score}', True, 'black', 'orange')
scoreRect = scoreTxt.get_rect()
scoreRect.center = (SCREEN_WIDTH // 2, 60)
healthTxt = font.render(f'Health: ',True, 'black', 'orange')
healthRect = scoreTxt.get_rect()
healthRect.center = (110, 300) 
gameoverFont = pygame.font.Font('mine-sweeper.ttf', 18)
#gameover
gameover = gameoverFont.render('GAME OVER', True, 'white', 'black')
gameoverRect= gameover.get_rect()
gameoverRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 40)
quit = gameoverFont.render('Press q to quit or r to restart', True, 'white', 'black')
quitRect= quit.get_rect()
quitRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
#compare
def compare(one,two):
    if one < two and two - one < 30:
        return True
def compare_boss(one,two):
    if one < two and two - one < 30:
        return True
def game_over():
    return gameOver

shutdown = False
while not shutdown:
    ammos = []
    attackers = []
    start_ticks=pygame.time.get_ticks()
    prev_sec = 0
    key_sec = 0
    bos = Boss(-0.7)
    score = 0
    spawn_speed = 2
    player = Player()
    print(player.health)
    healthTxt = font.render(f'Health: {player.health}', True, 'black', 'orange')
    while running and not game_over():
        screen.fill('gray')
        pygame.draw.line(screen, 'black',(0, 380), (680, 380), 3)
        pygame.draw.line(screen, 'black',(0, 430), (680, 430), 3)
        pygame.draw.line(screen, 'black',(230, 430), (230, 380), 3)
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                shutdown = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if seconds - key_sec > spawn_sec:
                    if event.key == pygame.K_a:
                        ammos.append(Ammo('krug'))
                    if event.key == pygame.K_s:
                        ammos.append(Ammo('trougao'))
                    if event.key == pygame.K_d:
                            ammos.append(Ammo('kvadrat'))
                    key_sec = seconds
        pygame.draw.circle(screen, '#23395d', (140,405), CIRCLE_WIDTH)
        pygame.draw.polygon(screen, '#23395d',[(155,418), (172, 390), (189, 418)])
        pygame.draw.rect(screen, '#23395d', (195, 390, SQUARE_WIDTH,SQUARE_WIDTH))
        
        
        if bos_active and not bos.dead:
            bos.draw(screen)
            bos.attack()
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 
        if seconds - boss_seconds > 2 and not bos_spawned:
            bos.draw(screen)
            bos.attack()
            bos_active = True
            bos_spawned = True
            boss_seconds += 60
        if seconds - prev_sec >  spawn_speed and not bos_active:
            if speed > speed_lvl and spawn_speed > 0.5:
                spawn_speed -= 0.5
                speed_lvl  =speed
            if seconds - speedUp > 10:
                speed+=0.5
                speedUp = seconds
            if speed == 2:
                spawn_sec -= 0.2
            l = random.randint(1,3)
            if l == 1:
                attackers.append(Objects('krug'))
                
            if l == 2:
                attackers.append(Objects('trougao'))
                
            if l == 3:
                attackers.append(Objects('kvadrat'))
            prev_sec = seconds
        player.draw(screen)
        for ammo in ammos:
                if not ammo.dead:
                    ammo.attack(screen)
                    ammo.move(speed)
        if not bos_active:
            for attacker in attackers:
                if not attacker.dead:
                    attacker.draw(screen)
                    attacker.move(speed)
                if attacker.pos() < 250: 
                    attacker.die()
                    attackers.remove(attacker)
                    player.dying(10)
                    healthTxt = font.render(f'Health: {player.health}', True, 'black', 'orange')
                    if player.dead: 
                        gameOver = True
                        healthTxt = font.render(f'Health: {player.health}', True, 'black', 'orange')
                        screen.blit(healthTxt, healthRect)
            for ammo in ammos:
                if not ammo.dead:
                    ammo.attack(screen)
                    ammo.move(speed)
            for ammo in ammos:
                for attacker in attackers:
                    if compare(ammo.x,attacker.x) and ammo.tip == attacker.tip:
                        attacker.die()
                        ammo.die()
                        attackers.remove(attacker)
                        ammos.remove(ammo)
                        score += 1
                        if score > highscore:
                            highscore - score
                        scoreTxt = font.render(f'Score: {score}', True, 'black', 'orange')
                        screen.blit(scoreTxt, scoreRect)
                    elif compare(ammo.x, attacker.x) and not ammo.tip == attacker.tip:
                        ammo.die()
                        ammos.remove(ammo)
                        score -=1
                        scoreTxt = font.render(f'Score: {score}', True, 'black', 'orange')
                        screen.blit(scoreTxt, scoreRect)
        elif bos_active:
            for ammo in ammos:
                if compare_boss(ammo.x,bos.x):
                    score += 1
                    scoreTxt = font.render(f'Score: {score}', True, 'black', 'orange')
                    bos.health -= 10
                    if bos.health == 0:
                        bos.die()
                        bos_spawned = False
                        bos_active = False
                    ammos.remove(ammo)
            if bos.posX(200):
                player.dying(50)
                healthTxt = font.render(f'Health: {player.health}', True, 'black', 'orange')
                bos.die()
                bos_spawned = False
                bos_active = False
                if player.dead: 
                    gameOver = True
                    healthTxt = font.render(f'Health: {player.health}', True, 'black', 'orange')
                    screen.blit(healthTxt, healthRect)
        
        screen.blit(healthTxt, healthRect)            
        screen.blit(scoreTxt, scoreRect)
        screen.blit(title, titleRect)
        pygame.display.flip()
        clock.tick(60)
    while gameOver:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                shutdown = True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    gameOver = False
                    shutdown = True
                if event.key == pygame.K_r:
                    gameOver = False
        
        scoreTxt = font.render(f'Score: {score}', True, 'white', 'black')
        screen.blit(gameover,gameoverRect)      
        screen.blit(scoreTxt, scoreRect)
        screen.blit(quit,quitRect)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()
