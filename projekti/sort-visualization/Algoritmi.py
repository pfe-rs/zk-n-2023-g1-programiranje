import pygame, sys, random, time, os

os.environ['SDL_VIDEO_WINDOW_POS'] = "640,250"
os.environ['SDL_VIDEO_CENTERED'] = '0'


SIRINA = 840
VISINA = 580
STUBOVI = (233, 0, 100)
POZADINA = (6, 0, 71)

counter = 0
j = 0
sorting_start = False
bubble = False
insertion = False
reset = False
alg = "Odaberite algoritam za sortiranje (b / i)."


display_surface = pygame.display.set_mode((SIRINA//2, 10))


n = 4 
w = int(SIRINA/n)

h_arr = []
states = []

num = random.randint(2, 5)

win = pygame.display.set_mode((SIRINA, VISINA))
pygame.display.set_caption('Vizualizacija algoritama za sortiranje')
clock = pygame.time.Clock()

pygame.init()

#Generisanje niza stubova
def create_h_arr(w):
    h_arr = []
    states = []
    for i in range(w):
        h_arr.append(random.randint(100, 400))
        states.append(1)
    return h_arr, states
def create_h_arr(w):
    h_arr = []
    states = []
    for i in range(w):
        h_arr.append(random.randint(100, 400))
        states.append(1)
    return h_arr, states

#Poziv funkcije za inicijalizaciju niza stubova
h_arr, states = create_h_arr(w)


while True:
    win.fill(POZADINA)
    keys = pygame.key.get_pressed()

    #Insertion/Umetanje
    if insertion and sorting_start and counter < len(h_arr):
        key = h_arr[counter]
        j = counter - 1
        while j >= 0 and key < h_arr[j]:
            h_arr[j+1] = h_arr[j]
            j -= 1
        h_arr[j+1] = key
        counter += 1
        alg = "Pritisnite r za reset niza."
    
    #Bubble/Mehurasto
    elif bubble and sorting_start and counter < len(h_arr):
        if counter < len(h_arr):
            #Unutrasnja petlja
            for j in range(len(h_arr) - 1 - counter):
                if h_arr[j] > h_arr[j+1]:
                    states[j] = 0
                    states[j+1] = 0
                    temp = h_arr[j]
                    h_arr[j] = h_arr[j+1]
                    h_arr[j+1] = temp
                else:
                    states[j] = 1
                    states[j+1] = 1
        counter += 1
        if len(h_arr) - counter >= 0:
            states[len(h_arr) - counter] = 2
        alg = "Pritisnite r za reset niza."

    #Iscrtavanje stubova
    for i in range (len(h_arr)):
        pygame.draw.rect(win, STUBOVI, (i*n, VISINA - h_arr[i], n, h_arr[i]))

    #Eventi na pritisak dugmeta 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sorting_start = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            bubble = True
            insertion = False
            alg = "Bubble algoritam aktivan. Pritisnite SPACE za pocetak."
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
            insertion = True
            bubble = False
            alg = "Insertion algoritam aktivan. Pritisnite SPACE za pocetak."
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            h_arr.clear()
            counter = 0
            states = 0
            h_arr, states = create_h_arr(w)
            sorting_start = False
            alg = "Niz stubova resetovan. Odaberite algoritam za sortiranje."
    
    #Render teksta
    font = pygame.font.Font('RobotoSlab-Black.ttf', 22)
    dest = (10, 25)
    text = font.render(alg, 1, STUBOVI)
    display_surface.blit(text, dest)

    clock.tick(60)
    pygame.display.flip()
