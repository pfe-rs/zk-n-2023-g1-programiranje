import pygame
import sys
from copy import deepcopy

sirina_ekrana = 480
visina_ekrana = 480
velicina_celije=10
v=sirina_ekrana//velicina_celije
h=visina_ekrana//velicina_celije

sledeca_celija=[[]]
trenutna_celija=[[]]

broj_iteracija=0

for i  in range(v):
    sledeca_celija.append([])
    trenutna_celija.append([])
    for j in range(h):
        sledeca_celija[i].append(0)
        trenutna_celija[i].append(0)

def zivot_celije(trenutna_celija, x, y):
    broj_suseda=0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if trenutna_celija[j][i]:
                broj_suseda+=1
    if trenutna_celija[y][x]:
        broj_suseda-=1
        if broj_suseda==2 or broj_suseda==3:
            return 1
        return 0
    else:
       if broj_suseda == 3:
           return 1
       return 0
           
pygame.init()
screen = pygame.display.set_mode((sirina_ekrana, visina_ekrana))
clock = pygame.time.Clock()
running = True



          
pygame.init()
screen = pygame.display.set_mode((sirina_ekrana, visina_ekrana))
clock = pygame.time.Clock()
running=True

simulacija = False
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if simulacija==False:
        if event.type==pygame.MOUSEBUTTONDOWN:
            pritisnut_mis=pygame.mouse.get_pressed()
            if pritisnut_mis[0]:
                x,y=pygame.mouse.get_pos()
                i= x // velicina_celije
                j=y // velicina_celije
                trenutna_celija[j][i]=1
                pygame.draw.rect(screen, (178, 255, 102),(i, j, velicina_celije-2, velicina_celije-2 ))
        if keys[pygame.K_RETURN]:
            simulacija=True
            if keys[pygame.K_r]:
                simulacija=False
                broj_iteracija=0
                for i in range(v):
                    for j in range(h):
                        if trenutna_celija[i][j]==1:
                            trenutna_celija[i][j]=0
                        if sledeca_celija[i][j]==1:
                            sledeca_celija[i][j]=0
    screen.fill('black')
    for y in range(1, v-1):
        for x in range(1, h-1):
            if trenutna_celija[y][x]:
                pygame.draw.rect(screen, (178, 255, 102),(x*velicina_celije+2, y*velicina_celije+2, velicina_celije-2, velicina_celije-2 ))
            if simulacija:
                sledeca_celija[y][x]=zivot_celije(trenutna_celija, x, y)
    [pygame.draw.line(screen, pygame.Color('dimgray'),(x,0), (x, visina_ekrana)) for x in range(0, sirina_ekrana, velicina_celije)]
    [pygame.draw.line(screen, pygame.Color('dimgray'), (0,y), (sirina_ekrana, y)) for y in range(0,visina_ekrana, velicina_celije)]

    if keys[pygame.K_r]:
        simulacija=False
        broj_iteracija=0
        for i in range(v):
            for j in range(h):
                if trenutna_celija[i][j]==1:
                    trenutna_celija[i][j]=0
                if sledeca_celija[i][j]==1:
                    sledeca_celija[i][j]=0

    if(simulacija):
        broj_iteracija+=1
        trenutna_celija=deepcopy(sledeca_celija)

    font = pygame.font.SysFont("Arial", 32)
    dest=(10,25)
    text=font.render(str(broj_iteracija), 1, 'white')
    screen.blit(text, (0,0))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()

