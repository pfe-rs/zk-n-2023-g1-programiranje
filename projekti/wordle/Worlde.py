import pygame as pg
import random
import time
import io as os

n=random.randint(1, 14850)
print(n)
green=(124,252,0)
f=open('worldebaza.txt','r')
lines=f.readlines()





print(lines[n-1])









SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BRICK_WIDTH = 80
BRICK_HEIGHT = 80




pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen = pg.display.set_mode((640, 480))
screen.fill((220,242,157))
font = pg.font.Font(None, 32)
input_box = pg.Rect(220, 448, 140, 32)
slova_box1=pg.Rect(170,80,60,60)
slova_box2=pg.Rect(230,80,60,60)
slova_box3=pg.Rect(290,80,60,60)
slova_box4=pg.Rect(350,80,60,60)
slova_box5=pg.Rect(410,80,60,60)
color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('orange')
color = color_inactive
active = False
text = ''
done = False
clock = pg.time.Clock()
uspeo=1
i=0
da=0
pobeda=0

Font = pg.font.Font(None, 50)
pg.draw.rect(screen,"white",slova_box1,2)
pg.draw.rect(screen,"white",slova_box2,2)
pg.draw.rect(screen,"white",slova_box3,2)
pg.draw.rect(screen,"white",slova_box4,2)
pg.draw.rect(screen,"white",slova_box5,2)



while not done:
       
        yes = font.render("GUEES THE WORD", True, "White")
        screen.blit(yes, (220,40))
        yes = font.render("WORDLE", True, "White")
        screen.blit(yes, (270,20))
        
        pg.draw.rect(screen,"white",slova_box1,2)
        pg.draw.rect(screen,"white",slova_box2,2)
        pg.draw.rect(screen,"white",slova_box3,2)
        pg.draw.rect(screen,"white",slova_box4,2)
        pg.draw.rect(screen,"white",slova_box5,2)

        slova_box1=pg.Rect(170,80+da*60,60,60)
        slova_box2=pg.Rect(230,80+da*60,60,60)
        slova_box3=pg.Rect(290,80+da*60,60,60)
        slova_box4=pg.Rect(350,80+da*60,60,60)
        slova_box5=pg.Rect(410,80+da*60,60,60)
        
        if(da==6):
          
          done=True
          
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                
                if input_box.collidepoint(event.pos):
                    
                    active = not active
                else:
                    active = False
                
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        pobeda=0
                        
                        if lines[n-1][0]==text[0]:
                                pg.draw.rect(screen,green,slova_box1)
                                pg.draw.rect(screen,"white",slova_box1,2)
                                slova = Font.render(text[0], True, "White")
                                screen.blit(slova, (190,90+da*60))
                                pobeda+=1
                                #print("da")
                        else:
                                if lines[n-1][0]==text[0]:
                                    pg.draw.rect(screen,"orange",slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))
                                                            
                                elif lines[n-1][1]==text[0]:
                                    pg.draw.rect(screen,"orange",slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))
                               
                                elif lines[n-1][2]==text[0]:
                                    pg.draw.rect(screen,"orange",slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))
                                
                                elif lines[n-1][3]==text[0]:
                                    pg.draw.rect(screen,"orange",slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))
                                
                                elif lines[n-1][4]==text[0]:
                                    pg.draw.rect(screen,"orange",slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))
                                else:
                                    pg.draw.rect(screen,'red',slova_box1)
                                    pg.draw.rect(screen,"white",slova_box1,2)
                                    slova = Font.render(text[0], True, "White")
                                    screen.blit(slova, (190,90+da*60))

                        
                                                     
                        if lines[n-1][1]==text[1]:
                                pg.draw.rect(screen,green,slova_box2)
                                pg.draw.rect(screen,"white",slova_box2,2)
                                slova = Font.render(text[1], True, "White")
                                screen.blit(slova, (250,90+da*60))
                                pobeda+=1
                        
                        else:
                                if lines[n-1][0]==text[1]:
                                    pg.draw.rect(screen,"orange",slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                                                            
                                elif lines[n-1][1]==text[1]:
                                    pg.draw.rect(screen,"orange",slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                               
                                elif lines[n-1][2]==text[1]:
                                    pg.draw.rect(screen,"orange",slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                                
                                elif lines[n-1][3]==text[1]:
                                    pg.draw.rect(screen,"orange",slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                                
                                elif lines[n-1][4]==text[1]:
                                    pg.draw.rect(screen,"orange",slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                                else:
                                    pg.draw.rect(screen,'red',slova_box2)
                                    pg.draw.rect(screen,"white",slova_box2,2)
                                    slova = Font.render(text[1], True, "White")
                                    screen.blit(slova, (250,90+da*60))
                        if lines[n-1][2]==text[2]:
                                pg.draw.rect(screen,green,slova_box3)
                                pg.draw.rect(screen,"white",slova_box3,2)
                                slova = Font.render(text[2], True, "White")
                                screen.blit(slova, (310,90+da*60))
                                pobeda+=1
                        else:
                                if lines[n-1][0]==text[2]:
                                    pg.draw.rect(screen,"orange",slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                                                            
                                elif lines[n-1][1]==text[2]:
                                    pg.draw.rect(screen,"orange",slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                               
                                elif lines[n-1][2]==text[2]:
                                    pg.draw.rect(screen,"orange",slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                                
                                elif lines[n-1][3]==text[2]:
                                    pg.draw.rect(screen,"orange",slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                                
                                elif lines[n-1][4]==text[2]:
                                    pg.draw.rect(screen,"orange",slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                                else:
                                    pg.draw.rect(screen,'red',slova_box3)
                                    pg.draw.rect(screen,"white",slova_box3,2)
                                    slova = Font.render(text[2], True, "White")
                                    screen.blit(slova, (310,90+da*60))
                        if lines[n-1][3]==text[3]:
                                pg.draw.rect(screen,green,slova_box4)
                                pg.draw.rect(screen,"white",slova_box4,2)
                                slova = Font.render(text[3], True, "White")
                                screen.blit(slova, (370,90+da*60))
                                pobeda+=1
                        else:
                                if lines[n-1][0]==text[3]:
                                    pg.draw.rect(screen,"orange",slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                                                            
                                elif lines[n-1][1]==text[3]:
                                    pg.draw.rect(screen,"orange",slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                               
                                elif lines[n-1][2]==text[3]:
                                    pg.draw.rect(screen,"orange",slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                                
                                elif lines[n-1][3]==text[3]:
                                    pg.draw.rect(screen,"orange",slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                                
                                elif lines[n-1][4]==text[3]:
                                    pg.draw.rect(screen,"orange",slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                                else:
                                    pg.draw.rect(screen,'red',slova_box4)
                                    pg.draw.rect(screen,"white",slova_box4,2)
                                    slova = Font.render(text[3], True, "White")
                                    screen.blit(slova, (370,90+da*60))
                        if lines[n-1][4]==text[4]:
                                pg.draw.rect(screen,green,slova_box5)
                                pg.draw.rect(screen,"white",slova_box5,2)
                                slova = Font.render(text[4], True, "White")
                                screen.blit(slova, (430,90+da*60))
                                pobeda+=1
                        else:
                                if lines[n-1][0]==text[4]:
                                    pg.draw.rect(screen,"orange",slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                                                            
                                elif lines[n-1][1]==text[4]:
                                    pg.draw.rect(screen,"orange",slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                               
                                elif lines[n-1][2]==text[4]:
                                    pg.draw.rect(screen,"orange",slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                                    
                                
                                elif lines[n-1][3]==text[4]:
                                    pg.draw.rect(screen,"orange",slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                                
                                elif lines[n-1][4]==text[4]:
                                    pg.draw.rect(screen,"orange",slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                                else:
                                    pg.draw.rect(screen,'red',slova_box5)
                                    pg.draw.rect(screen,"white",slova_box5,2)
                                    slova = Font.render(text[4], True, "White")
                                    screen.blit(slova, (430,90+da*60))
                        da+=1
                        
                        pg.display.flip()
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

     
        if(pobeda==5):
                
                            
                yes = font.render("WOOOOOOOO", True, "White")
                screen.blit(yes, (10,200))
                
                done=True
        if(da==6 and pobeda!=5):
            yes = font.render("The word was", True, "White")
            screen.blit(yes, (10,200))
            yes = font.render(lines[n-1].strip(), True, "White")
            screen.blit(yes, (10,220))
        pg.draw.rect(screen, color, input_box,)
        pg.draw.rect(screen, "black", input_box,4)
        txt_surface = font.render(text, True, "white")
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        
        
        
        
        
        
        pg.display.flip()
        if(pobeda==5):
            time.sleep(5)
        if(da==6):
            time.sleep(2)
        clock.tick(60)
        
        
                    
            
            




pg.quit()
