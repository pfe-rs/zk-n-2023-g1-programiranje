import pygame
import random
import numpy
from pynput import keyboard, mouse
import time



pygame.init()

running = True



#changables
width = 10
height = 10
bombCount = 10

#constants
tileSize = 64
screenWidht = tileSize * width + tileSize
screenHeight = tileSize * height + tileSize//2 + 3*tileSize

#colors
colorTile = (65, 70, 75)
colorTileLight = (125, 130, 135)
colorTileDark = (45, 50, 55)
colorBack = colorTile


color1 = (0, 0, 255)
color2 = (0, 155, 0)
color3 = (255, 0, 0)
color4 = (0, 0, 100)
color5 = (130, 0, 0)
color6 = (0, 192, 150)
color7 = (0, 0, 0)
color8 = (140, 140, 140)

colors = [(255, 255, 255), color1, color2, color3, color4, color5, color6, color7, color8]


bombs = numpy.zeros((bombCount, 2))
matrixPerm = numpy.zeros((height + 2, width + 2))
matrix = numpy.zeros((height, width))

screen = pygame.display.set_mode((screenWidht, screenHeight))
pygame.display.set_caption('MineSweeper')
print(pygame.font.get_fonts())
fontMS = pygame.font.SysFont('minesweeperregular', tileSize//2)
falgPicUnscaled = pygame.image.load('FlagMS.png')
flagPic = pygame.transform.scale(falgPicUnscaled, (tileSize//2, tileSize//2))
bombPicUnscaled = pygame.image.load('BombMS.png')
bombPic = pygame.transform.scale(bombPicUnscaled, (tileSize//2, tileSize//2))
clock = pygame.time.Clock







class Tile:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.vis = True
        self.flaged = False

    def Draw(self):
        pygame.draw.rect(screen, colorTileDark, [(self.x, self.y), (tileSize, tileSize)])
        pygame.draw.polygon(screen, colorTileLight, [(self.x, self.y), (self.x + tileSize, self.y), (self.x, self.y + tileSize)])
        pygame.draw.rect(screen, colorTile, [(self.x + tileSize // 8, self.y + tileSize//8), (tileSize - 2 * tileSize / 8 + tileSize / 64, tileSize - 2 * tileSize / 8 + tileSize/64)])
        if self.flaged:
            screen.blit(flagPic, (self.x + tileSize//4, self.y + tileSize //4))



#gen bombs
counter = 0
while counter < bombCount:
    x = random.randrange(1, width + 1)
    y = random.randrange(1, height + 1)
    if matrixPerm[y][x] == 0:
        matrixPerm[y][x] = -1
        bombs[counter][0] = x
        bombs[counter][1] = y
        counter += 1


#gen numbers (matrixPerm)
for i in range(0, bombCount, 1):
    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            if matrixPerm[int(bombs[i][1] + b)][int(bombs[i][0] + a)] > -1:
                matrixPerm[int(bombs[i][1] + b)][int(bombs[i][0] + a)] += 1

#reformat matrix
for j in range(0, height, 1):
    for i in range(0, width, 1):
        matrix[j][i] = matrixPerm[j+1][i+1]

print(matrix)





#gen tiles
tiles = []
for j in range(0, height):
    for i in range(0, width):
        x = i * tileSize + tileSize//2
        y = j * tileSize + 3*tileSize
        tiles.append(Tile(x, y, matrix[j, i]))






#write custom methods inside
class Mtdh:
    @staticmethod
    def uncover(x, y):
        for a in range(-1, 2, 1):
            for b in range(-1, 2, 1):
                try:
                    if (-1 < x + a < width and -1 < y + b < height) and (tiles[(y + b) * width + x + a].vis):

                        tiles[(y + b) * width + x + a].vis = False
                        print(x + a, y + b)
                        if matrix[y + b][x + a] == 0:
                            Mtdh.uncover(x + a, y + b)


                except Exception as e:
                    print(e)

    @staticmethod
    def visible(x, y):
        tiles[y * width + x].vis = False

    @staticmethod
    def win():
        print("win")
        fontMSBig = pygame.font.Font('mine-sweeper.ttf', screenWidht // 2)
        winText = fontMSBig.render("GG EZ", True, 'black')
        winTextRect = winText.get_rect()
        winTextRect.center = (screenWidht // 2, screenHeight // 2)
        screen.blit(winText, winTextRect)
        pygame.display.flip()

    @staticmethod
    def lose():
        print("lose")
        fontMSBig = pygame.font.SysFont('minesweeperregular', screenWidht // 10)
        gameOverText = fontMSBig.render('GAME OVER', True, 'black')
        gameOverTextRect = gameOverText.get_rect()
        gameOverTextRect.center = (screenWidht // 2, screenHeight // 2)
        screen.blit(gameOverText, gameOverTextRect)
        pygame.display.flip()




lose = False
win = False

startTime = pygame.time.get_ticks()

#UPDATE
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posM = pygame.mouse.get_pos()
            x = (posM[0] - tileSize // 2) // tileSize
            y = (posM[1] - 3*tileSize) // tileSize

            if pygame.mouse.get_pressed()[0] == 1:

                if(tileSize // 2 <= posM[0] <= tileSize * width + tileSize // 2) and (3*tileSize <= posM[1] <= tileSize * height + 3*tileSize):

                    tiles[y * width + x].vis = False
                    print(x, y)
                    if matrix[y][x] == 0:
                        Mtdh.uncover(x, y)
                    elif matrix[y][x] == -1:
                        lose = True
                        running = False
                        break


            if pygame.mouse.get_pressed()[2] == 1:
                if (tileSize // 2 <= posM[0] <= tileSize * width + tileSize // 2) and (3*tileSize <= posM[1] <= tileSize * height + 3*tileSize):
                    tiles[y * width + x].flaged = not tiles[y * width + x].flaged



    allUncovered = True
    for j in range(0, height):
        for i in range(0, width):
            if tiles[j*width + i].vis and not matrix[j][i] == -1:
                allUncovered = False
                break

    if allUncovered:
        win = True
        running = False


    currentTime = pygame.time.get_ticks()



    screen.fill(colorBack);

    pygame.draw.rect(screen, colorTileLight, (tileSize//2, tileSize//2, screenWidht - tileSize, 2 * tileSize))
    pygame.draw.polygon(screen, colorTileDark, [(tileSize // 2, tileSize // 2),
                                         (tileSize//2, tileSize * 5 // 2),
                                         (tileSize//2 + tileSize//8, tileSize * 5 // 2 - tileSize // 8),
                                         (screenWidht - tileSize // 2 - tileSize // 8, tileSize // 2 + tileSize // 8),
                                         (screenWidht - tileSize // 2, tileSize // 2)])
    pygame.draw.rect(screen, colorTile, (tileSize // 2 + tileSize//8, tileSize // 2 + tileSize // 8, screenWidht - tileSize - tileSize // 4, 2 * tileSize - tileSize // 4))

    timeText = fontMS.render(str((currentTime - startTime % 1000) // 1000), True, 'red')
    timeTextRect = timeText.get_rect()
    timeTextRect.center = (screenWidht // 2, 3*tileSize//2)
    screen.blit(timeText, timeTextRect)


    for i in range(0, height + 1):
        xOS = tileSize//2
        yOS = 3*tileSize
        pygame.draw.line(screen, colorTileDark, (xOS - 1, yOS + i * tileSize - 1), (xOS + width * tileSize - 1, yOS + i * tileSize - 1), 2)
    for i in range(0, width + 1):
        xOS = tileSize // 2
        yOS = 3*tileSize
        pygame.draw.line(screen, colorTileDark, (xOS + i * tileSize - 1, yOS - 1), (xOS + i * tileSize - 1, yOS + height * tileSize - 1), 2)

    for j in range(0, height):
        for i in range(0, width):
            if matrix[j][i] == 0:
                pass
            elif not matrix[j][i] == -1:
                text = fontMS.render(str(matrix[j][i])[0], True, colors[int(matrix[j][i])])
                textRect = text.get_rect()
                textRect.center = (tileSize // 2 + i * tileSize + tileSize // 2, 3*tileSize + j * tileSize + tileSize // 2)
                screen.blit(text, textRect)
            else:
                screen.blit(bombPic, (i * tileSize + tileSize//2 + tileSize//4,j * tileSize + 3*tileSize + tileSize//4 ))





    for tile in tiles:
        if tile.vis:
            tile.Draw()








    pygame.display.flip()

    if win:
        Mtdh.win()
    if lose:
        Mtdh.lose()









while(1):
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



