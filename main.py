import random
import pygame as pg
import copy
clock = pg.time.Clock()
pozadina = (64, 64, 64)
boje = {0:(74, 74, 74),2:(255,224,153),4:(255,158,102),8:(255, 100, 71),16:(246, 189, 0),32:(100,60,10),64:(200,0,0),128:(111,53,70),256:(50,200,200),512:(125,75,199),1024:(144,10,40),2048:(255,255,180)}
tabla = []
prtabla = []
pomerajdesno = []
pomerajdole = []
VelicinaTable = 4 #moze da se menja velicina table, sada je 4x4
(sirinapolja,visinapolja)=(60,60) #mogu da se menjaju dimenzije polja
margina = 10 #moze da se menja sirina margine
def prvaigra():
    global dimenzijeprozora
    global tabla
    global prozor
    global prtabla
    for i in range(VelicinaTable):
        tabla.append([])
        pomerajdesno.append([])
        pomerajdole.append([])
        for j in range(VelicinaTable):
            tabla[i].append(0)
            pomerajdesno[i].append(0)
            pomerajdole[i].append(0)
    dimenzijeprozora = [sirinapolja * VelicinaTable + margina * (VelicinaTable + 1),
                        visinapolja * VelicinaTable + margina * (VelicinaTable + 1)]
    prozor = pg.display.set_mode(dimenzijeprozora)
    slpolje()
    slpolje()
    prtabla = copy.deepcopy(tabla)
    CrtajTablu(tabla,pomerajdesno,pomerajdole)
pg.init()
prozor = pg.display.set_mode([280,320])
pg.display.set_caption("2048")
prozor.fill(pozadina)
font = pg.font.SysFont('boulder', 40)
tekst = font.render("Choose a board:", True, (255, 255, 255))
prozor.blit(tekst, (30, 20))
pg.draw.rect(prozor,(255,158,102),[20, 60, 110, 110])
pg.draw.rect(prozor,(255,158,102),[150, 60, 110, 110])
pg.draw.rect(prozor,(255,158,102),[20, 190, 110, 110])
pg.draw.rect(prozor,(255,158,102),[150, 190, 110, 110])
font = pg.font.SysFont('boulder', 40)
tekst = font.render("3x3", True, (255, 255, 255))
prozor.blit(tekst, (50, 100))
tekst = font.render("4x4", True, (255, 255, 255))
prozor.blit(tekst, (180, 100))
tekst = font.render("5x5", True, (255, 255, 255))
prozor.blit(tekst, (50, 230))
tekst = font.render("6x6", True, (255, 255, 255))
prozor.blit(tekst, (180, 230))
pg.display.update()
sledecepolje = [2,2,2,4] #posto u igrici mogu da se pojave i dvojke i cetvorke, ali redje cetvorke?
def slpolje():
    global tabla
    a=random.randint(0,VelicinaTable-1)
    b=random.randint(0,VelicinaTable-1)
    while tabla[a][b]!=0:
        a = random.randint(0, VelicinaTable-1)
        b = random.randint(0, VelicinaTable-1)
    tabla[a][b] = sledecepolje[random.randint(0,3)]
def stanjeigre():
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            if tabla[i][j]==2048:
                return 0 #poooobeedaa
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            if tabla[i][j]==0:
                return 1 #moze daljeee
    for i in range (VelicinaTable):
        for j in range(VelicinaTable-1):
            if tabla[i][j]==tabla[i][j+1]:
                return 1 #mozeeee
    for i in range(VelicinaTable-1):
        for j in range(VelicinaTable):
            if tabla[i][j]==tabla[i+1][j]:
                return 1 #opet mozee
    return 2 #porazz :'(
def prevrnimatricu(tabla): #transpozicija matrice
    rez = [[tabla[j][i] for j in range(len(tabla))] for i in range(len(tabla[0]))]
    return rez
def pomnozimatricu(tabla,n):
    rez = []
    for i in range(VelicinaTable):
        rez.append([])
        for j in range(VelicinaTable):
            rez[i].append(0)
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            rez[i][j]=n*tabla[i][j]
    return rez
def SpojiRedDesno1(red,pomerajreda):
    prethodnired = copy.deepcopy(red)
    for j in range (VelicinaTable-1): #maks broj pomeranja nadam se
        for i in range(VelicinaTable - 1):
            if red[i+1] == 0:
                red[i+1] = red[i]
                red[i] = 0
    a=0
    b=0
    while True:
        if a == VelicinaTable or b == VelicinaTable:
            break
        while prethodnired[a] == 0 and a<VelicinaTable-1:
            a+=1
        while red[b] == 0 and b<VelicinaTable-1:
            b+=1
        if a<VelicinaTable:
            pomerajreda[a] = b-a
        a+=1
        b+=1
    return red,pomerajreda
def SpojiRedDesno2(red,pomerajreda):
    for i in range(VelicinaTable - 1,0,-1):
            if red[i] == red[i - 1]:
                red[i] += red[i]
                red[i-1] = 0
                pomerajreda[i-1]+=1
    return red,pomerajreda
def SpojiRedLevo1(red,pomerajreda):
    red.reverse()
    pomerajreda.reverse()
    (red,pomerajreda)= SpojiRedDesno1(red,pomerajreda)
    red.reverse()
    pomerajreda.reverse()
    for i in range (VelicinaTable):
        pomerajreda[i] = -1*pomerajreda[i]
    return red,pomerajreda
def SpojiRedLevo2(red,pomerajreda):
    red.reverse()
    pomerajreda.reverse()
    (red, pomerajreda) = SpojiRedDesno2(red, pomerajreda)
    red.reverse()
    pomerajreda.reverse()
    for i in range (VelicinaTable):
        pomerajreda[i] = -1*pomerajreda[i]
    return red, pomerajreda
brzina = 3
def PotezDesno():
    global tabla
    global pomerajdesno
    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedDesno1(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(prtabla, matrica,pomerajdole)
    pomocnatabla = copy.deepcopy(tabla)
    for i in range (VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdesno[i][j]=0

    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedDesno2(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(pomocnatabla, matrica,pomerajdole)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range (VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdesno[i][j]=0

    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedDesno1(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(pomocnatabla, matrica,pomerajdole)
def PotezLevo():
    global tabla
    global pomerajdesno
    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedLevo1(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(prtabla, matrica,pomerajdole)
    pomocnatabla = copy.deepcopy(tabla)
    for i in range (VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdesno[i][j]=0

    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedLevo2(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(pomocnatabla, matrica,pomerajdole)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range (VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdesno[i][j]=0

    for i in range(VelicinaTable):
        (tabla[i],pomerajdesno[i]) = SpojiRedLevo1(tabla[i],pomerajdesno[i])
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdesno,i)
        CrtajTablu(pomocnatabla, matrica,pomerajdole)
def PotezGore():
    global tabla
    global pomerajdole
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i],pomerajdole[i]) = SpojiRedLevo1(tabla[i],pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range (0,sirinapolja,brzina):
        matrica = pomnozimatricu(pomerajdole,i)
        CrtajTablu(prtabla, pomerajdesno,matrica)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdole[i][j]=0

    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i],pomerajdole[i]) = SpojiRedLevo2(tabla[i],pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdole,i)
        CrtajTablu(pomocnatabla, pomerajdesno,matrica)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdole[i][j] = 0

    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i],pomerajdole[i]) = SpojiRedLevo1(tabla[i],pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range (0,sirinapolja,brzina*2):
        matrica = pomnozimatricu(pomerajdole,i)
        CrtajTablu(pomocnatabla, pomerajdesno,matrica)
def PotezDole():
    global tabla
    global pomerajdole
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i], pomerajdole[i]) = SpojiRedDesno1(tabla[i], pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(0, sirinapolja, brzina):
        matrica = pomnozimatricu(pomerajdole, i)
        CrtajTablu(prtabla, pomerajdesno, matrica)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdole[i][j] = 0

    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i], pomerajdole[i]) = SpojiRedDesno2(tabla[i], pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(0, sirinapolja, brzina * 2):
        matrica = pomnozimatricu(pomerajdole, i)
        CrtajTablu(pomocnatabla, pomerajdesno, matrica)

    pomocnatabla = copy.deepcopy(tabla)
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            pomerajdole[i][j] = 0

    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(VelicinaTable):
        (tabla[i], pomerajdole[i]) = SpojiRedDesno1(tabla[i], pomerajdole[i])
    tabla = prevrnimatricu(tabla)
    pomerajdole = prevrnimatricu(pomerajdole)
    for i in range(0, sirinapolja, brzina * 2):
        matrica = pomnozimatricu(pomerajdole, i)
        CrtajTablu(pomocnatabla, pomerajdesno, matrica)
def crtajbroj(broj, x, y):
    font = pg.font.SysFont('boulder', 35)
    tekst = font.render(str(broj), True, (255, 255, 255))
    (xbroja, ybroja) = (14, 20)
    y-=ybroja//2
    if broj<10:
        x-=xbroja//2
    elif broj<100:
        x-=xbroja
    elif broj<1000:
        x-=xbroja//2*3
    else:
        x-=2*xbroja
    prozor.blit(tekst, (x,y))
def CrtajTablu(tabla, pomerajdesno,pomerajdole):
    prozor.fill(pozadina)# brisanje prethodne table
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            boja = boje.get(0, [])
            pg.draw.rect(prozor, boja, [(margina + sirinapolja) * j + margina ,
                                        (margina + visinapolja) * i + margina , sirinapolja,
                                        visinapolja])
    for i in range(VelicinaTable):
        for j in range(VelicinaTable):
            boja = boje.get(tabla[i][j], [])
            if tabla[i][j]!=0:
                pg.draw.rect(prozor, boja, [(margina + sirinapolja) * j + margina + pomerajdesno[i][j],
                                            (margina + visinapolja) * i + margina + pomerajdole[i][j], sirinapolja,
                                            visinapolja])
                crtajbroj(tabla[i][j],(margina + sirinapolja) * j + margina+sirinapolja//2+pomerajdesno[i][j], (margina + visinapolja) * i+margina+visinapolja//2+pomerajdole[i][j])
    pg.display.flip()
izgubio_si = False
pobedio_si = False
font = pg.font.SysFont('boulder', 20)
tekst2 = font.render("press SPACE to play again", True, (255, 255, 255))
done = False
while not done:
    if izgubio_si:
        font = pg.font.SysFont('boulder', 50)
        tekst = font.render("GAME OVER", True, (255, 255, 255))
        prozor.fill(pozadina)
        prozor.blit(tekst, ((VelicinaTable - 4) * ((sirinapolja + margina) // 2)+40, dimenzijeprozora[1] // 2 - 25))
        prozor.blit(tekst2, ((VelicinaTable - 4) * ((sirinapolja + margina) // 2) + 60, dimenzijeprozora[1] // 2 + 20))
        pg.display.update()
    elif pobedio_si:
        font = pg.font.SysFont('boulder', 60)
        tekst = font.render("YOU WIN", True, (255, 255, 255))
        prozor.fill(pozadina)
        prozor.blit(tekst, ((VelicinaTable - 4) * ((sirinapolja + margina) // 2)+50, dimenzijeprozora[1] // 2 - 25))
        prozor.blit(tekst2, ((VelicinaTable - 4) * ((sirinapolja + margina) // 2) + 60, dimenzijeprozora[1] // 2 + 20))
        pg.display.update()
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            done = True
        elif dogadjaj.type == pg.MOUSEBUTTONDOWN:
            (mis_x,mis_y) = pg.mouse.get_pos()
            if mis_x>=140 and mis_y>=180:
                VelicinaTable = 6
            elif mis_x>=140 and mis_y<180:
                VelicinaTable = 4
            elif mis_x<140 and mis_y<180:
                VelicinaTable = 3
            else: VelicinaTable = 5
            prvaigra()
        elif dogadjaj.type == pg.KEYDOWN:
            mogucpotez = True
            if dogadjaj.key == pg.K_SPACE:
                pobedio_si = False
                izgubio_si = False
                for i in range(VelicinaTable):
                    for j in range(VelicinaTable):
                        tabla[i][j] = 0
                        pomerajdesno[i][j]=0
                        pomerajdole[i][j]=0
                slpolje()
                slpolje()
                CrtajTablu(tabla,pomerajdesno,pomerajdole)

            else:
                if dogadjaj.key == pg.K_LEFT:
                    PotezLevo()
                elif dogadjaj.key == pg.K_RIGHT:
                    PotezDesno()
                elif dogadjaj.key == pg.K_DOWN:
                    PotezDole()
                elif dogadjaj.key == pg.K_UP:
                    PotezGore()
                else:
                    mogucpotez = False
                if prtabla == tabla:
                    mogucpotez = False
                if mogucpotez:
                    slpolje()
                    for i in range(VelicinaTable):
                        for j in range(VelicinaTable):
                            pomerajdole[i][j] = 0
                            pomerajdesno[i][j] = 0
                    CrtajTablu(tabla,pomerajdesno,pomerajdole)
                    prtabla = copy.deepcopy(tabla)
                if stanjeigre() == 2:
                    izgubio_si = True
                elif stanjeigre() == 0:
                    pobedio_si = True
    clock.tick(60)
pg.quit()