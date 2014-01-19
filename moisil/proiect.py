import pygame
import sys
import random
import math
from pygame.locals import *
pygame.init()

MAXX=1024
MAXY=764-50
NMAX=100
class ELEMENT:
  Toate=[]
  enunt = ""
  def __init__(self,frm,txt,lista):
      self.forma=frm
      self.text=txt
      self.marime=[]
      for i in lista:
         self.marime.append(i)
      ok = False
      while not ok:
          self.x=random.randrange(marime[0],MAXX-marime[0])
          self.y=50+random.randrange(marime[0],MAXY-marime[0])
          ok = True
          for i in ELEMENT.Toate:
              if math.sqrt((self.x-i.x)**2+(self.y-i.y)**2) < self.marime[0]+i.marime[0]:
                  ok = False
  def desen(self):
        if self.forma==1:
           pygame.draw.rect(display,red,(self.x-self.marime[0],self.y-self.marime[0],2*self.marime[0],2*self.marime[0]))
        elif self.forma==2:
           pygame.draw.circle(display,blue,(self.x,self.y),self.marime[0])

forme=[]
f=open("test.txt","r")
ELEMENT.enunt=f.readline()[:-1]
n=int(f.readline())



for k in range(n):
  marime=[]
  txt=f.readline();
  txt=txt[:-1]
  linie=f.readline()
  inf=linie.split()

  unu=1
  for j in inf:
      if unu:
          frm=int(j)
          unu=0
      else:
          marime.append(int(j))
  
  a=ELEMENT(frm,txt,marime)
  ELEMENT.Toate.append(a)
  
  FORME = ELEMENT.Toate
#-------------------------------------------------------
#culori
white = (255,255,255)
pink = (255,200,255)
galben = (234,222,000)
black = (0,0,0)
red = (230,0,0)
red1 = (252,197,52)
red2 = (200,100,100)
red3 = (250,48,37)
red4 = (250,120,110)
blue = (2,26,240)
yellow = (241,253,23)
green = (30,223,39)
marimefont = 15
ceas = pygame.time.Clock

#lista culori
culori = [red1,red2,red3,red4]



display = pygame.display.set_mode((1024,768))
pygame.display.set_caption('Moisil Python Aplicatie')
#FONTURI
myfont = pygame.font.SysFont("Comic Sans MS", marimefont)
gameoverfont = pygame.font.SysFont("Comic Sans MS", 40)
enuntfont = pygame.font.SysFont("Comic Sans MS", 20)

patrate = []

patrate.append((150,100,"Patrat1"))
patrate.append((400,400,"Patrat2"))
gameovertext= gameoverfont.render("GAME OVER", 1, white)
enunttext= gameoverfont.render(ELEMENT.enunt, 1, white)




gameover=0






while True:
    
    for event in pygame.event.get():
        
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pmouse = pygame.mouse.get_pos()

        if len(FORME) <> 0:
            prima = FORME[0]
        if event.type == pygame.MOUSEBUTTONUP:
            
            if (prima.x+prima.marime[0]>pmouse[0]>prima.x-prima.marime[0]) and prima.y+prima.marime[0]>pmouse[1]>prima.y-prima.marime[0]:
                
                FORME.remove(prima)
            #else:
                #pygame.mixer.music.load('fire.wav') Daca exista driver de sunet!!!
                #pygame.mixer.music.play(0)
                
               
                
                    
    if len(FORME)==0:
        gameover = 1

        
           
            
            
            
    
                

            

   

  
    display.fill(black)
    
    pygame.time.delay(30)
    display.blit(enunttext, (100,10))
    for i in ELEMENT.Toate:
        #pygame.draw.rect(display,red4,(i[0],i[1],70,70))
        i.desen()
        display.blit( myfont.render(i.text, 1, white) , (i.x-marimefont/2, i.y-marimefont/2) )
    if gameover == 1:
         display.blit(gameovertext, (400,400 ))
         
    

        
    

    pygame.display.update()        
