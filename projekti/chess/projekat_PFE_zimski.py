import pygame
import numpy as np
import time
# 
SCREEN_WIDTH=650
SCREEN_HEIGHT=650
SCREEN_DIM=650#dimenzije ekrana
DIM_TABLE=8#br polja u tabli
DIM_POLJA=SCREEN_DIM/8
FPS=60
#boje
TAMNO_BRAON=(92, 64, 51)
SVETLO_BRAON=(204, 153, 102)
PINK=(199,21,133)
#figure
PIJUN='pijun'
TOP='top'
LOVAC='lovac'
KONJ='konj'
KRALJICA='kraljica'
KRALJ='kralj'
BELI='beli'
CRNI='crni'
#class sl polje
class circle:#ova klasa je prakticno beskorisna tj sluzi da bi oznacila legalna polja
    def __init__(self,red,kol):    
        self.red=red
        self.kol=kol
    def draw(self,surface):
        pygame.draw.circle(surface, PINK, (DIM_POLJA*self.kol-DIM_POLJA//2, DIM_POLJA*self.red-DIM_POLJA//2), DIM_POLJA//3)
        print('kolona')
        print(self.kol)
        print('red')
        print(self.red)

class polje:
    def __init__(self):
        self.mat=False
        self.sahmat=False
        self.pozicije=[]
#        self.polje = [
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0]
#]

        self.figure=np.zeros((64, 1))

        #self.figure=[]#zauzeto[figura],[]........]
        self.selected_piece=None
        #self.beli=self.crni=16
#    def __str__(self):
#        ret_str = "["
#        for i in self.pozicije:
#            ret_str += "["
#            for j in i:
#                ret_str += str(j) + " "
#            ret_str += "]\n"
#        ret_str += "]"

#        return ret_str

    def draw(self,surface):
        for i in range(DIM_TABLE):
            for j in range(i%2,DIM_TABLE,2):
                pygame.draw.rect(surface,SVETLO_BRAON, (i*DIM_POLJA, j*DIM_POLJA, DIM_POLJA, DIM_POLJA))
#    def legalan_potez(self,red,kol,sl_red,sl_kolona,tip,boja):
    def legalan_potez(self,figura):
            moguce=[]
            if(figura.tip==PIJUN):
                if(figura.boja==BELI and figura.kol!=0):
                    if(figura.red==6):
                        moguce.append([figura.red,figura.kol-1])
                        moguce.append([figura.red,figura.kol-2])
                        print("iz funkcije aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                        print(moguce)
                    else:
                        moguce.append([figura.red,figura.kol-1])
                        print("iz funkcije bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                        print(moguce)
                if(figura.boja==CRNI and figura.kol!=7):
                    if(figura.kol==1):
                        moguce.append([figura.kol+1,figura.red])
                        moguce.append([figura.kol+2,figura.red])
                    moguce.append([figura.kol+1,figura.red])
                        
            if(figura.tip==TOP):
                i=1
                while(figura.red<7):
                    moguce.append([figura.kol,figura.red+i])
                    i=i+1
                i=1
                while(figura.red>0):
                    moguce.append([figura.kol,figura.red-i])
                    i=i+1
                i=1
                while(figura.kol<7):
                    moguce.append([figura.kol-i,figura.red])
                    i=i+1
                i=1
                while(figura.kol>0):
                    moguce.append([figura.kol-i,figura.red])
                    i=i+1

            if(figura.tip==LOVAC):
                i=1
                while(figura.red<7 and figura.kol<7):
                    moguce.append([figura.kol+i,figura.red+i])
                    i=i+1
                i=1
                while(figura.red>0 and figura.red>0):
                    moguce.append([figura.kol,-i,figura.red-i])
                    i=i+1
                i=1
                while(figura.kol<7 and figura.red>0):
                    moguce.append([figura.kol-i,figura.red+1])
                    i=i+1
                i=1
                while(figura.kol>0 and figura.red<7):
                    moguce.append([figura.kol+i,figura.red-i])
                    i=i+1
                
            if(figura.tip==KONJ):
                if(figura.red+2<7 and figura.kol+1<7):
                    moguce.append([figura.red+2,figura.kol+1])
                if(figura.red+2<7 and figura.kol-1>0):
                    moguce.append([figura.red+2,figura.kol-1])
                if(figura.red-2>0 and figura.kol+1<7):
                    moguce.append([figura.red-2,figura.kol+1])
                if(figura.red-2>0 and figura.kol-1>0):
                    moguce.append([figura.red-2,figura.kol-1])

                if(figura.kol+2<7 and figura.red+1<7):
                    moguce.append([figura.kol+2,figura.red+1])
                if(figura.kol+2<7 and figura.red-1>0):
                    moguce.append([figura.kol+2,figura.red-1])
                if(figura.kol-2>0 and figura.red+1<7):
                    moguce.append([figura.kol-2,figura.red+1])
                if(figura.kol-2>0 and figura.red-1>0):
                    moguce.append([figura.kol-2,figura.red-1])
            if(figura.tip==KRALJICA):
                i=1
                while(figura.red<7):
                    moguce.append([figura.kol,figura.red+i])
                    i=i+1
                i=1
                while(figura.red>0):
                    moguce.append([figura.kol,figura.red-i])
                    i=i+1
                i=1
                while(figura.kol<7):
                    moguce.append([figura.kol-i,figura.red])
                    i=i+1
                i=1
                while(figura.kol>0):
                    moguce.append([figura.kol-i,figura.red])
                    i=i+1
                i=1
                while(figura.red<7 and figura.kol<7):
                    moguce.append([figura.kol+i,figura.red+i])
                    i=i+1
                i=1
                while(figura.red>0 and figura.red>0):
                    moguce.append([figura.kol,-i,figura.red-i])
                    i=i+1
                i=1
                while(figura.kol<7 and figura.red>0):
                    moguce.append([figura.kol-i,figura.red+1])
                    i=i+1
                i=1
                while(figura.kol>0 and figura.red<7):
                    moguce.append([figura.kol+i,figura.red-i])
                    i=i+1
            if(figura.tip==KRALJ):
                moguce.append([figura.kol+1,figura.red])
                moguce.append([figura.kol+1,figura.red+1])
                moguce.append([figura.kol,figura.red+1])
                moguce.append([figura.kol-1,figura.red])
                moguce.append([figura.kol-1,figura.red-1])
                moguce.append([figura.kol,figura.red-1])
                moguce.append([figura.kol+1,figura.red-1])
                moguce.append([figura.kol-1,figura.red+1])
            return moguce
    def Zauzeto_polje(self,kol,red):
        kol=int(kol)
        red=int(red)
        if(self.pozicije[red][kol]!=0):
            return self.pozicije[red][kol]
        else:
            return None
    def izabrano_polje(self,x,y):
        return DIM_TABLE//x,DIM_TABLE//y
    


class figura:
    def __init__(self,red, kol, image, pojeden,tip,boja):
        self.red=red
        self.kol=kol        
        self.x=DIM_POLJA*self.kol+DIM_POLJA//2
        self.y=DIM_POLJA*self.red+DIM_POLJA//2
        #width = image.get_width()
        #height = image.get_height()
        self.image = pygame.transform.scale(image, (DIM_POLJA, DIM_POLJA))
        #self.rect = self.image.get_rect()
        #self.rect.topleft = (self.x, self.y)
        self.tip=tip
        self.boja=boja
        self.pojeden = pojeden

    def __str__(self):
        return str(self.boja) +" " +self.tip

    def draw (self,surface):
        if(self.pojeden==False):
            if(self.pojeden==False):
                surface.blit(self.image,(self.red*DIM_POLJA,self.kol*DIM_POLJA))
    def pozicija(self):
        self.x=DIM_POLJA*self.kol+DIM_POLJA//2
        self.y=DIM_POLJA*self.red+DIM_POLJA//2
    def pomeri_se(self,red,kol):
        self.red=red
        self.kol=kol
    def pojeden(self):
        self.pojeden=True
def Uzmi_polje():   
        klik=pygame.mouse.get_pos()
        #print(klik[0]//DIM_POLJA+1,klik[1]//DIM_POLJA+1)
        time.sleep(0.4)
        return klik[0]//DIM_POLJA,klik[1]//DIM_POLJA
def Taster_pritisnut():
    	if pygame.mouse.get_pressed()[0] == 0:
            return False
def Trazi(moguce,red,kol):
    n=len(moguce)
    i=0
    while(i<n):
        if(moguce[i][0]==kol and moguce[i][1]==red):
            return i
        i=i+1
    return False

        
pygame.init()
KORAK=1
AKT_FIG=8*4
click_count=0
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
#ucitavam slike
b_Kraljica=pygame.image.load('bela kraljica.png').convert_alpha()
b_Konj=pygame.image.load('beli konj.png').convert_alpha()
b_Kralj=pygame.image.load('beli kralj.png').convert_alpha()
b_Lovac=pygame.image.load('beli lovac.png').convert_alpha()
b_Pijun=pygame.image.load('beli pijun.png').convert_alpha()
b_Top=pygame.image.load('beli top.png').convert_alpha()

c_Kraljica=pygame.image.load('crna kraljica.png').convert_alpha()
c_Konj=pygame.image.load('crni konj.png').convert_alpha()
c_Kralj=pygame.image.load('crni kralj.png').convert_alpha()
c_Lovac=pygame.image.load('crni lovac.png').convert_alpha()
c_Pijun=pygame.image.load('crni pijun.png').convert_alpha()
c_Top=pygame.image.load('crni top.png').convert_alpha()

Polja=polje()    
Pijun_b=[]
Konj_b=[]
Lovac_b=[]
Top_b=[]
Top_c=[]
Lovac_c=[]
Konj_c=[]
Pijun_c=[]
sl_polja_na_tabli=[]



pozicije = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

Kraljica_b=figura(3,7,b_Kraljica,False,KRALJICA,BELI)
Kraljica_c=figura(3,0,c_Kraljica,False,KRALJICA,CRNI)
Kralj_b=figura(4,7,b_Kralj,False,KRALJ,BELI)
Kralj_c=figura(4,0,c_Kralj,False,KRALJ,CRNI)
pozicije[Kraljica_b.kol][Kraljica_b.red]=Kraljica_b
pozicije[Kralj_b.kol][Kralj_b.red]=Kralj_b
pozicije[Kraljica_c.kol][Kraljica_c.red]=Kraljica_c
pozicije[Kralj_c.kol][Kralj_c.red]=Kralj_c


for i in range(8):
    Pijun_b.append(figura(i,6,b_Pijun,False,PIJUN,BELI) )
    pozicije[Pijun_b[i].kol][Pijun_b[i].red]=Pijun_b[i]
    Pijun_c.append(figura(i,1,c_Pijun,False,PIJUN,CRNI) )
    pozicije[Pijun_c[i].kol][Pijun_c[i].red]=Pijun_c[i]


Konj_b.append(figura(1,7,b_Konj,False,KONJ,BELI) )
pozicije[Konj_b[0].kol][Konj_b[0].red]=Konj_b[0]
print(Konj_b[0].kol)
print(Konj_b[0].red)
#print(pozicije[1][7])
#Polja.polje[Konj_b[0].red,Konj_b[0].kol]=Konj_b
Konj_b.append(figura(6,7,b_Konj,False,KONJ,BELI) )
pozicije[Konj_b[1].kol][Konj_b[1].red]=Konj_b[1]
#Polja.polje[Konj_b[0].red,Konj_b[0].kol]=Konj_b

Top_b.append(figura(0,7,b_Top,False,TOP,BELI) )
pozicije[Top_b[0].kol][Top_b[0].red]=Top_b[0]
Top_b.append(figura(7,7,b_Top,False,TOP,BELI) )
pozicije[Top_b[1].kol][Top_b[1].red]=Top_b[1]

Lovac_b.append(figura(2,7,b_Lovac,False,LOVAC,BELI) )
pozicije[Lovac_b[0].kol][Lovac_b[0].red]=Lovac_b[0]
Lovac_b.append(figura(5,7,b_Lovac,False,LOVAC,BELI) )
pozicije[Lovac_b[0].kol][Lovac_b[1].red]=Lovac_b[0]

Konj_c.append(figura(1,0,c_Konj,False,KONJ,CRNI) )
Konj_c.append(figura(6,0,c_Konj,False,KONJ,CRNI) )
pozicije[Konj_c[0].kol][Konj_c[0].red]=Konj_c[0]
pozicije[Konj_c[1].kol][Konj_c[1].red]=Konj_c[1]

Top_c.append(figura(0,0,c_Top,False,TOP,CRNI) )
Top_c.append(figura(7,0,c_Top,False,TOP,CRNI) )
pozicije[Top_c[0].kol][Top_c[0].red]=Top_c[0]
pozicije[Top_c[1].kol][Top_c[1].red]=Top_c[1]

Lovac_c.append(figura(2,0,c_Lovac,False,LOVAC,CRNI) )
Lovac_c.append(figura(5,0,c_Lovac,False,LOVAC,CRNI) )
pozicije[Lovac_c[0].kol][Lovac_c[0].red]=Lovac_c[0]
pozicije[Lovac_c[1].kol][Lovac_c[1].red]=Lovac_c[1]
#deklarisanje polja i figura

Polja.pozicije=pozicije
#Pijun=figura(100,100,b_Pijun,False,'pijun') 
running=True
clock = pygame.time.Clock()
pygame.display.set_caption("Šah")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type==pygame.MOUSEBUTTONDOWN:
         #   pass
    klik2=[-1,-1]
    #crtanje polja i figura
    screen.fill(TAMNO_BRAON)
    Polja.draw(screen)
    for pijun in Pijun_b:
        pijun.draw(screen)
    for pijun in Pijun_c:
        pijun.draw(screen)
    for konj in Konj_b:
        konj.draw(screen)   
    for konj in Konj_c:
        konj.draw(screen)
    for lovac in Lovac_b:
        lovac.draw(screen)
    for lovac in Lovac_c:
        lovac.draw(screen)
    for top in Top_b:
        top.draw(screen)
    for top in Top_c:
        top.draw(screen)
    Kralj_b.draw(screen)
    Kralj_c.draw(screen)
    Kraljica_b.draw(screen)
    Kraljica_c.draw(screen)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_presses = pygame.mouse.get_pressed()
        #print(event.button)
        if(event.button==1):
            #print(Polja)
            klik=Uzmi_polje()
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print(klik[0],klik[1])

            #pygame.event.clear()
            if(Polja.Zauzeto_polje(klik[0],klik[1])!=None):
                print("evo")
                
        if(click_count==0):
            if(Polja.Zauzeto_polje(klik[0],klik[1]).boja==BELI and KORAK%2==1):
                click_count=1
                print(Polja.Zauzeto_polje(klik[0],klik[1]).boja + Polja.Zauzeto_polje(klik[0],klik[1]).tip)
                time.sleep(0.5)
                moguce=Polja.legalan_potez(Polja.Zauzeto_polje(klik[0],klik[1]))
                n=len(moguce)
                y=klik[0]
                x=klik[1]
                i=0
                print(moguce)
                while(i<n):
                    sl_polja_na_tabli.append(circle(moguce[i][0],moguce[i][1]))
                    print("iksic"+str(moguce[i][0]))
                    sl_polja_na_tabli[i].draw(screen)
                    i=i+1
        if(click_count==1):
            if(Trazi(moguce,klik[1],klik[0])==True):#####
                click_count=0
                print('klik'+ str(klik))
                Polja.Zauzeto_polje(x,y).red=klik[0]
                Polja.Zauzeto_polje(x,y).kol=klik[1]
                            #print ("x" + str(x))
                Polja.pozicije[int(y)][int(x)]==0
                if(Polja.pozicije[int(klik[1])][int(klik[0])].boja==CRNI and Polja.pozicije[int(klik[1])][int(klik[0])].tip!=KRALJ):
                    Polja.pozicije[klik[1][klik[0]]].pojeden=True
                    Polja.pozicije[klik[1]][klik[0]]==Polja.Zauzeto_polje(klik[1],klik[0])
            else:
                print("preskok")    
                #okolina_kralja=Polja.legalan_potez(Kralj_b)
                #k=len(okolina_kralja)
                #if(Trazi(Polja.legalan_potez(Polja.Zauzeto_polje(klik2[1],klik2[0])),Kralj_b.kol,Kralj_b.red)):
                #   Polja.mat=True
                #kad je crni na redu

                    
                    #mat i sah mat


                

                    
                        

    #kada se mis pritisne trazi taj red i kolonu da vidi da li je popunjeno i ako nije sta se nalazi tu
    pygame.event.clear()
    pygame.display.flip()
    KORAK=KORAK+1
    clock.tick(FPS)
pygame.quit()


