import pygame
import math
import random
pygame.init()

sw=800
sh=650
pygame.init()

pozadina=pygame.image.load("pozadina.jpg")
Raketa=pygame.image.load("Raketa1.png")
asteroid1=pygame.image.load("Stone1.png")
asteroid2=pygame.image.load("Stone2.png")
asteroid3=pygame.image.load("Stone3.png")
asteroid4=pygame.image.load("Stone4.png")
asteroid5=pygame.image.load("Stone5.png")
asteroid6=pygame.image.load("Stone6.png")

pygame.display.set_caption("Asteroidi")
win=pygame.display.set_mode((sw,sh))

clock=pygame.time.Clock()

kraj=False  
zivoti=3   
poeni=0  

class Player(object):
    
    def __init__(self):
        self.img=Raketa
        self.w=self.img.get_width()
        self.h=self.img.get_height()
        self.x=sw//2
        self.y=sh//2
        self.angle=0
        self.rotiraj()

    def rotiraj(self):

        self.rotatedSurf=pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect=self.rotatedSurf.get_rect()
        self.rotatedRect.center=(self.x, self.y)

        self.cosine=math.cos(math.radians(self.angle+90))
        self.sine=math.sin(math.radians(self.angle+90))
        self.head=(self.x, self.y)

    def crtaj(self,win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    def Levo(self):
        self.angle+=5
        self.rotiraj()


    def Desno(self):
        self.angle-=5
        self.rotiraj()

    def Napred(self):
        self.x+=self.cosine*6
        self.y-=self.sine*6
        self.rotiraj()

    def Nazad(self):
        self.x-=self.cosine*6
        self.y+=self.sine*6
        self.rotiraj()

    def osveziLokaciju(self):
        if self.x>sw+self.w:
            self.x=0
        elif self.x<0-self.w:
            self.x=sw
        if self.y<-self.h:
            self.y=sh
        elif self.y>sh+self.h:
            self.y=0

#klasa municije
class Municija(object):
    def __init__(self):
        self.x, self.y = igrac.head
    
        self.w=4
        self.h=4
        self.xv=igrac.cosine*10
        self.yv=igrac.sine*10

    def move(self):
        self.x+=self.xv
        self.y-=self.yv

    def crtaj(self, win):
        pygame.draw.rect(win, (255,255,255), (self.x, self.y, self.w, self.h))

    def checkOffScreen(self):
        if self.x<-igrac.w or self.x>sw or self.y>sh or self.y<-igrac.h:
            return True

class Asteroid(object):
    def __init__(self, rang):
        self.rang=rang
        if self.rang==1:
            self.img=asteroid1
        elif self.rang==2:
            self.img=asteroid2
        elif self.rang==3:
            self.img=asteroid3
        elif self.rang==4:
            self.img=asteroid4
        elif self.rang==5:
            self.img=asteroid5
        elif self.rang==6:
            self.img=asteroid6
        
        self.w=self.img.get_width()
        self.h=self.img.get_height()
        
        gore_dole=(random.randrange(0,sw-self.w), random.choice([-1*self.h-5, sh+5]))
        levo_desno=(random.choice([-1*self.w-5,sw+5]), random.randrange(0, sh-self.h))
        self.x, self.y = random.choice([gore_dole, levo_desno])
        
        if self.x<sw//2:
            self.xdir=1
        else:
            self.xdir=-1
        if self.y<sh//2:
            self.ydir=1
        else:
            self.ydir=-1
        
        self.xv=self.xdir*random.randrange(1,3)
        self.yv=self.ydir*random.randrange(1,3)

    def crtaj(self, win):
        win.blit(self.img, (self.x, self.y))
        
# osvežavanje ekrana
def osveziEkran():

    win.blit(pozadina, (0,0))
    font=pygame.font.SysFont("arial",30)
    font1=pygame.font.SysFont("arial",50)
    zivotiTekst=font.render("Životi: " + str(zivoti), True, (255,255,255))
    poeniTekst=font.render("Poeni: " + str(poeni), True, (255,255,255))
    IgrajPonovoTekst=font1.render("Pritisni SPACE da bi ponovo igrao:", True, (255,255,0))
    
    igrac.crtaj(win)
    for a in asteroidi:
        a.crtaj(win)
    for b in igracMunicija:
        b.crtaj(win)

    if kraj:
        win.blit(IgrajPonovoTekst, (sw//2-IgrajPonovoTekst.get_width()//2, sh//2-IgrajPonovoTekst.get_height()//2))
    win.blit(zivotiTekst, (25,25))
    win.blit(poeniTekst, (sw-poeniTekst.get_width()-25,25))

    pygame.display.update()

igrac=Player()
igracMunicija=[] 
asteroidi=[] 
count=0
   
run=True

while run:
    clock.tick(60)
    count+=1
    if not kraj:
        if count%50==0:
            rang=random.choice([1,1,1,1,1,1,2,2,2,3,3,3,4,4,5,5,6])
            asteroidi.append(Asteroid(rang))
            
        igrac.osveziLokaciju()
        
        for b in igracMunicija:
            b.move()
            if b.checkOffScreen():
                igracMunicija.pop(igracMunicija.index(b))

        for a in asteroidi:
            a.x+=a.xv
            a.y+=a.yv
            if (igrac.x>=a.x and igrac.x<=a.x+a.w) or (igrac.x+igrac.w>=a.x and igrac.x+igrac.w<=a.x+a.w):
                    if (igrac.y>=a.y and igrac.y<=a.y+a.h) or (igrac.y+igrac.h>=a.y and igrac.y+igrac.h<=a.y+a.h):
                        zivoti-=1
                        asteroidi.pop(asteroidi.index(a))
                        break 
            for b in igracMunicija:
                if (b.x>=a.x and b.x<=a.x+a.w) or (b.x+b.w>=a.x and b.x+b.w<=a.x+a.w):
                    if (b.y>=a.y and b.y<=a.y+a.h) or (b.y+b.h>=a.y and b.y+b.h<=a.y+a.h):
                        if a.rang==6:
                            poeni+=10
                            for i in range(4):
                                novi_asteroid=Asteroid(1)
                                novi_asteroid.x=a.x
                                novi_asteroid.y=a.y
                                asteroidi.append(novi_asteroid)
    
                        elif a.rang==4 or a.rang==5:
                            poeni+=20
                            for i in range(2):
                                novi_asteroid=Asteroid(1)
                                novi_asteroid.x=a.x
                                novi_asteroid.y=a.y
                                asteroidi.append(novi_asteroid)
                    
                        elif a.rang==3 or a.rang==2:
                            poeni+=30
                    
                        elif a.rang==1:
                            poeni+=50
                        
                        asteroidi.pop(asteroidi.index(a))
                        igracMunicija.pop(igracMunicija.index(b))

        if zivoti<=0:
            kraj=True

        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            igrac.Levo()
        if keys[pygame.K_RIGHT]:
            igrac.Desno()
        if keys[pygame.K_UP]:
            igrac.Napred()
        if keys[pygame.K_DOWN]:
            igrac.Nazad()  
        osveziEkran()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if not kraj:
                    igracMunicija.append(Municija())
                else:
                    kraj=False
                    zivoti=3
                    poeni=0
                    asteroidi.clear()
                    igracMunicija.clear()
            
#kraj igrice
pygame.quit()
