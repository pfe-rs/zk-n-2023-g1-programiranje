import pygame
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_WIDTH = 30
BLOCK_HEIGHT = 30
PLAYFIELD_WIDTH=10
PLAYFIELD_HEIGHT=20
colors=["black","white","yellow","cyan"]
O_SHAPE_MATRIX=[[2,2],[2,2]]
I_SHAPE_MATRIX1=[[3],[3],[3],[3]]
I_SHAPE_MATRIX0=[[3,3,3,3]]
cntDrop=0
cntMoveLR=0
gameover=False
score=0
shapes=[0,1]
currentShape=-1
cntChangePosition=0
fallSpeed=60
cntChangeSpeed=0


PLAYFIELD_MATRIX=[[0 for _ in range(PLAYFIELD_WIDTH+2)] for _ in range(PLAYFIELD_HEIGHT+2)]
for i in range(0,12):
    PLAYFIELD_MATRIX[21][i]=1
for i in range(0,22):
    PLAYFIELD_MATRIX[i][0]=1
    PLAYFIELD_MATRIX[i][11]=1

def playfieldDraw(surface):
    for i in range(1,21):
        for j in range(1,11):
            pygame.draw.rect(surface, colors[PLAYFIELD_MATRIX[i][j]],((j-1)*30,(i-1)*30,30,30))

def playfieldDeleteRow(row):
    i=row-1
    while(i>-1):
        for j in range(12):
            PLAYFIELD_MATRIX[i+1][j]=PLAYFIELD_MATRIX[i][j]
        i-=1

def playfieldCheck():
    for i in range(1,21):
        check=True
        for j in range(1,11):
            if(PLAYFIELD_MATRIX[i][j]==0):
                check=False
                break
        if(check):
            playfieldDeleteRow(i)


class O_SHAPE:
    def __init__(self,x,y,col,row):
        self.shape=O_SHAPE_MATRIX
        self.x=x
        self.y=y
        self.row=row
        self.col=col
        self.active=False
        self.color="yellow"
    def draw(self,surface):
        pygame.draw.rect(surface, self.color,(self.x,self.y,60,60))
    def drop(self):
        self.y+=30
        self.row+=1
    def moveLR(self,x):
        self.x+=x

class I_SHAPE:
    def __init__(self,x,y,col,row):
        self.shape=I_SHAPE_MATRIX0
        self.x=x
        self.y=y
        self.row=row
        self.col=col
        self.active=False
        self.color="cyan"
        self.state=0
    def draw0(self,surface):
        pygame.draw.rect(surface, self.color,(self.x,self.y,120,30))
    def draw1(self,surface):
        pygame.draw.rect(surface, self.color,(self.x,self.y,30,120))
    def drop(self):
        self.y+=30
        self.row+=1
    def moveLR(self,x):
        self.x+=x

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
o1=O_SHAPE(120,-60,5,-1)
i1=I_SHAPE(90,-30,4,0)
myfont = pygame.font.SysFont("monospace",45)
myfont2=pygame.font.SysFont("monospace",30)
currentShape=-1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if(currentShape==-1):
       currentShape=random.randint(0,1)
    print (fallSpeed)
    if(gameover==0):
        if(currentShape==0):
            if(o1.active==False):
                o1.x=120
                o1.y=-60
                o1.col=5
                o1.row=-1
                o1.active=True
                cntDrop=0
                cntMoveLR=0
                cntChangePosition=0
    
            cntDrop+=1
            if(PLAYFIELD_MATRIX[o1.row+2][o1.col] or PLAYFIELD_MATRIX[o1.row+2][o1.col+1]):
                o1.active=False
                currentShape=-1
                score+=100
                cntChangeSpeed+=1
                for i in range(o1.row,o1.row+2):
                    for j in range(o1.col, o1.col+2):
                        PLAYFIELD_MATRIX[i][j]=2
                for j in range(1,11):
                    if PLAYFIELD_MATRIX[0][j]:
                        gameover=True
                        score-=100
                        break

            if(cntDrop==fallSpeed and o1.active):
                o1.drop()
                cntDrop=0
            cntMoveLR+=1
            if(cntMoveLR>=8 and o1.active):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] and (not(PLAYFIELD_MATRIX[o1.row][o1.col+2] or PLAYFIELD_MATRIX[o1.row+1][o1.col+2])):
                    o1.moveLR(30)
                    o1.col+=1
                    cntMoveLR=0
                if keys[pygame.K_LEFT] and (not(PLAYFIELD_MATRIX[o1.row][o1.col-1] or PLAYFIELD_MATRIX[o1.row+1][o1.col-1])):
                    o1.moveLR(-30)
                    o1.col-=1
                    cntMoveLR=0
        if(currentShape==1):
            if(i1.active==False):
                i1.shape=I_SHAPE_MATRIX0
                i1.x=90
                i1.y=-30
                i1.col=4
                i1.row=0
                i1.active=True
                cntDrop=0
                cntMoveLR=0
                i1.state=0
                cntChangePosition=0
            if(PLAYFIELD_MATRIX[i1.row+1][i1.col] or PLAYFIELD_MATRIX[i1.row+1][i1.col+1] or PLAYFIELD_MATRIX[i1.row+1][i1.col+2] or PLAYFIELD_MATRIX[i1.row+1][i1.col+3])and i1.state==0 and i1.active==1:
                i1.active=False
                currentShape=-1
                cntChangeSpeed+=1
                score+=100
                for j in range(i1.col, i1.col+4):
                    PLAYFIELD_MATRIX[i1.row][j]=3
                for j in range(1,11):
                    if PLAYFIELD_MATRIX[0][j]:
                        gameover=True
                        score-=100
                        break
            if(i1.state==1 and PLAYFIELD_MATRIX[i1.row+4][i1.col] and i1.active==1):
                i1.active=False
                currentShape=-1
                score+=100
                cntChangeSpeed+=1
                for i in range(i1.row, i1.row+4):
                    PLAYFIELD_MATRIX[i][i1.col]=3
                for j in range(1,11):
                    if PLAYFIELD_MATRIX[0][j]:
                        gameover=True
                        score-=100
                        break
            cntDrop+=1
           
            if(cntDrop==fallSpeed and i1.active):
                i1.drop()
                cntDrop=0
            cntMoveLR+=1
            if(cntMoveLR>=8 and i1.active and i1.state==0):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]and (not (PLAYFIELD_MATRIX[i1.row][i1.col+4])):
                    i1.moveLR(30)
                    i1.col+=1
                    cntMoveLR=0
                if keys[pygame.K_LEFT] and (not(PLAYFIELD_MATRIX[i1.row][i1.col-1])):
                    i1.moveLR(-30)
                    i1.col-=1
                    cntMoveLR=0
            if(cntMoveLR>=8 and i1.active and i1.state==1):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]and (not (PLAYFIELD_MATRIX[i1.row][i1.col+1] or PLAYFIELD_MATRIX[i1.row+1][i1.col+1] or PLAYFIELD_MATRIX[i1.row+2][i1.col+1] or PLAYFIELD_MATRIX[i1.row+3][i1.col+1])):
                    i1.moveLR(30)
                    i1.col+=1
                    cntMoveLR=0
                if keys[pygame.K_LEFT] and (not(PLAYFIELD_MATRIX[i1.row][i1.col-1] or PLAYFIELD_MATRIX[i1.row+1][i1.col-1] or PLAYFIELD_MATRIX[i1.row+2][i1.col-1] or PLAYFIELD_MATRIX[i1.row+3][i1.col-1])):
                    i1.moveLR(-30)
                    i1.col-=1
                    cntMoveLR=0
            cntChangePosition+=1
            if(cntChangePosition>=16 and i1.active and i1.state==0 and((PLAYFIELD_MATRIX[i1.row-1][i1.col+1]==0 and PLAYFIELD_MATRIX[i1.row+1][i1.col+1]==0 and PLAYFIELD_MATRIX[i1.row+2][i1.col+1]==0) or i1.row==0)):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    i1.shape=I_SHAPE_MATRIX1                    
                    i1.x+=30
                    i1.y-=30
                    i1.row-=1
                    i1.col+=1
                    i1.state=1
                    cntChangePosition=0
            if cntChangePosition>=16 and i1.active and i1.state and (PLAYFIELD_MATRIX[i1.row+1][i1.col-1]==0 and PLAYFIELD_MATRIX[i1.row+1][i1.col+1]==0 and PLAYFIELD_MATRIX[i1.row+1][i1.col+2]==0):
                keys=pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    i1.shape=I_SHAPE_MATRIX0                   
                    i1.x-=30
                    i1.y+=30
                    i1.row+=1
                    i1.col-=1
                    i1.state=0
                    cntChangePosition=0

    if(cntChangeSpeed==5):
        cntChangeSpeed=0
        fallSpeed-=5
    playfieldCheck()
    if(gameover==False):
        playfieldDraw(screen)
        if(currentShape==0):
            o1.draw(screen)
        if(currentShape==1 and i1.state==0):
            i1.draw0(screen)
        if(currentShape==1 and i1.state==1):
            i1.draw1(screen)
    else:
        screen.fill("black")
        label=myfont.render("Game Over",1,(255,255,255))
        screen.blit(label,(30,200))
        label=myfont2.render("Score: "+str(score),1,(255,255,255))
        screen.blit(label,(35,250))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()