                if(Polja.Zauzeto_polje(x,y).boja==CRNI and KORAK%2==0):
                    print("ovde")
                    time.sleep(0.5)
                    moguce=Polja.legalan_potez(Polja.Zauzeto_polje(x,y))
                    n=len(moguce)
                    i=0
                    while(i<n):
                        sl_polja_na_tabli.append(circle(moguce[i][1],moguce[i][0]))
                        sl_polja_na_tabli[i].draw(screen)
                    br_klik=1#kaze da je vec jednom kliknuto
                    while(Trazi(moguce,klik2[0],klik2[1])==False):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_presses = pygame.mouse.get_pressed()
                            #print(event.button)
                            if(event.button==2):   
                                klik2=Uzmi_polje()
                                print('klik'+ str(klik2))
                    Polja.Zauzeto_polje(x,y).red=klik2[0]
                    Polja.Zauzeto_polje(x,y).kol=klik2[1]
                            #print ("x" + str(x))
                    Polja.pozicije[int(y)][int(x)]==0
                    if(Polja.pozicije[klik2[1]][klik2[0]].boja==BELI and Polja.pozicije[klik2[1][klik2[0]]].tip!=KRALJ):
                        Polja.pozicije[klik2[1][klik2[0]]].pojeden=True
                        Polja.pozicije[klik2[1]][klik2[0]]==Polja.Zauzeto_polje(klik2[1],klik2[0])