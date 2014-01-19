import requests
import random
from lxml.html.soupparser import fromstring
import pygame
from pygame import *

def inlocuire(sir, dr):
    caractere = list(sir)
    for c in dr.keys():
        for i in range(len(caractere)):
            if ord(caractere[i]) == ord(c):
                caractere[i] = dr[c]
    return "".join(caractere)

def nivel(niv, dicti):

    listkey = dicti.keys()

    if niv==1:
        while True:
            l = random.choice(listkey)
            if l<=7:
                break
        x = random.randint(0,len(dicti[l]))
    elif niv==2:
        while True:
            l = random.choice(listkey)
            if l<13 and l>=8 :
                break
        x = random.randint(0,len(dicti[l]))
    else:
        while True:
            l = random.choice(listkey)
            if l>12:
                break
        x = random.randint(0,len(dicti[l]))
    return dicti[l][x]

def meniu():
    print "Bine ati venit!\n "
    print " Alegeti varianta de joc\n"
    print "Tastati : \n"
    print "1  Pentru alegerea nivelului de dificultate dorit \n"
    print "2  Pentru trecerea de la nivelul minim la nivelul maxim\n"
    start_joc()
    #...TBC (in caz ca mai vrea sa joace!)
def trat(key, cuvint, cuvint_initial):
    
    print key in cuvint
    val = False
    for i in range(len(cuvint)):
        if key == cuvint[i]:
            cuvint_initial[i] = str(key)
            val = True
    return (cuvint_initial, val)

def start_joc(cuvintul):
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 35)
    DISPLAYSURF=pygame.display.set_mode((700, 500))
    cuv_init = []
    for i in range(len(cuvintul)):
        cuv_init.append("*")
    OK=8
    finish=0
    while OK and not finish:
        pygame.display.flip()
        YELLOW = (255,255, 0)
        RED = (205, 51,51)
        BLUE = (0,0,205)
        GREEN = (0,205, 0)
        pygame.draw.rect(DISPLAYSURF, YELLOW, DISPLAYSURF.get_rect())
        latime=700/len(cuvintul)
        for i in range(len(cuvintul)):
            pygame.draw.rect(DISPLAYSURF, RED, (i*latime, 300, latime-10, 100), 5)
            lit = cuv_init[i]
            label = myfont.render(lit, 1, BLUE)
            DISPLAYSURF.blit(label, ((i)*700/len(cuvintul), 350))
    #pygame.font.Font.render(cuvintul[0], 100, (255, 255, 255)) afiseaza prima litera TBW
        pygame.display.flip()
        for ev in event.get():
            if ev.type == KEYDOWN:
                if K_a <= ev.key <= K_z:
                    x = trat(chr(ev.key), cuvintul, cuv_init)
                    cuv_init = x[0]
                    if not x[1]:
                        OK=OK-1
                    else:
                        finish = 1
                        for i in range(len(cuvintul)):
                            if cuv_init[i] == "*":
                                finish = 0
                elif ev.key == K_ESCAPE:
                    pygame.quit()
                    return
    if finish == 1:
        print "FELICITARI!"
        pygame.draw.rect(DISPLAYSURF, BLUE, DISPLAYSURF.get_rect())
        label = myfont.render("FELICITARI!!! AI TERMINAT JOCUL!", 1, YELLOW)
        DISPLAYSURF.blit(label, (0, 350))
        pygame.display.flip()
        pygame.time.delay(5000)
    else:
        pygame.draw.rect(DISPLAYSURF, GREEN, DISPLAYSURF.get_rect())
        label = myfont.render("ai pierdut!", 1, YELLOW)
        DISPLAYSURF.blit(label, (0, 350))
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.draw.rect(DISPLAYSURF, GREEN, DISPLAYSURF.get_rect())
        label = myfont.render("cuvintul era " + cuvintul, 1, YELLOW)
        DISPLAYSURF.blit(label, (0, 350))
        pygame.display.flip()
        pygame.time.delay(5000)
    pygame.quit()

url = 'http://dexonline.ro/cuvinte-aleatoare'
source = requests.get(url) #preia sursa
x = fromstring(source.content)
container = x.get_element_by_id("contentProper")
children = container.getchildren()
children = children[1:]
cuvinte = []
tr = {u"\u0103":"a",u"\u0219":"s", u"\u021b":"t", u"\xee":"i", u"\xe2":"a" }
for a in children:
    cuvinte.append(inlocuire(a.text, tr))
cuv = {}
for c in cuvinte:
    l = len(c)
    if l in cuv:
        cuv[l].append(c)
    else:
        cuv[l] = [c]
#pt a primi cuvintul, apeleaza nivel (nivelul_dorit, dictionar), returneaza un cuvint aleator!
        
start_joc(nivel(1, cuv))
