import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
g = 0.3
r = 30

class Kokos:
    def __init__(self):
        self.x = 60
        self.y = 420
        self.vx = 0
        self.vy = 0
    def crtaj(self, surface):
        pygame.draw.circle(surface, (80,40,15), (self.x, self.y), r)
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), 26)
        pygame.draw.circle(surface, (190, 190, 190), (self.x, self.y), 20)
    def gravitacija(self):
        self.vy += g
    def odskakuje(self):
        self.vy *= -0.7
    def odbijanje(self):
        self.vx *= -0.7
    def mrdaj(self):
        self.x += self.vx
        self.y += self.vy

class Prase:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ded = False
        self.r = 30
        self.color = (140, 255, 140)
    def crtaj(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.r)
    def umri(self):
        self.ded = True
        
plejer = Kokos()
prasici = []

nx = SCREEN_WIDTH // (4 * (r + 5))
ny = SCREEN_HEIGHT // (2 * (r + 5))

for i in range(0, nx - 1):
    for j in range(0, ny - 1):
        prasici.append(Prase(SCREEN_WIDTH + r + 5 + i * 2 * (r + 5), r + 5 + i * 2 * (r + 5)))


x1 = -1
y1 = -1
x2 = -1
y2 = -1

while running:
    screen.fill((200, 200, 240))
    plejer.crtaj(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            poz1 = pygame.mouse.get_pos()
            if abs(poz1[0] - plejer.x <= r) and abs(poz1[1] - plejer.y <= r):
                x1 = poz1[0]
                y1 = poz1[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if x1 != -1 and y1 != -1:
                pos2 = pygame.mouse.get_pos()
                x2 = pos2[0]
                y2 = pos2[1]
                plejer.vx = (x1 - x2) * 0.3
                plejer.vy = (y1 - y2) * 0.3
                x1 = -1
                y1 = -1

    plejer.mrdaj()
    plejer.gravitacija()
    if((plejer.x >= SCREEN_WIDTH - r and plejer.vx > 0) or (plejer.x <= r and plejer.vx < 0)):
        plejer.odbijanje()
    if((plejer.y >= SCREEN_HEIGHT - r and plejer.vy > 0) or (plejer.y <= r and plejer.vy < 0)):
        plejer.odskakuje()
    
    for prase in prasici:
        prase.crtaj(screen)

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()