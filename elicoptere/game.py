import sys, pygame,random,time
from pygame.draw import rect
from pygame.locals import *
from functools import wraps

pygame.init()
circle = pygame.image.load("avion.png")
square = pygame.image.load("helicopter.png")

spritex=0
spritey=0
size = width, height = 800, 600
black = 99, 226, 242
blue = 0, 0, 255
x, y = 0, 0

harta =[1,1,2,2.1,3,4.1,5,6,7,8.1,9,10,11,12.1,13,14,15,16.1,17,18,19,19,20.1,20,20.1,19,19,18.1,17,16,15,14.1,13,12,11,10.1,9,8,7,6.1,5,4,3,2.1,2,1]
spatiu=[0]*50
h2 = spatiu + [1] + spatiu + [1]
harta2=[random.randint (0,500)*i for i in h2]

pos = 0.0
screen = pygame.display.set_mode(size)
circlerect = circle.get_rect()


while 1:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT: sys.exit()
      

        
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
     spritey -=3

    if keys_pressed[K_DOWN]:
     spritey +=3
       
    #ballrect = ballrect.move(speed)

    screen.fill(black)
    #screen.blit(circle, circlerect)

    bloc = 0
    for i in range(35):
        
        s = False
        if (harta2[int(pos + i) % len(harta2)]):
            dr = [i * 25,harta2[int(pos + i) % len(harta2)] , 25,bloc*5]
            screen.blit(square, (dr[0],dr[1]))
            r = square.get_bounding_rect()
            r.x = dr[0]
            r.y = dr[1]
            r_square = r
           # print r.x, r.y
            s = True
            
        if (height - bloc*5 <70):
            bloc = harta[int(pos + i) % len(harta)]
            dr = [i * 25, height - bloc*3+5,25, bloc*5]
            rect(screen, blue, dr)
        else:
            bloc = harta[int(pos + i) % len(harta)]
            dr = [i * 25, height - bloc*3-5,25, bloc*5]
            rect(screen, blue, dr)
        r = circle.get_bounding_rect()
        r.x = spritex
        r.y = spritey
        r_circle = r
      #  print r.x, r.y
        
     
        
        if s and r_circle.colliderect(r_square):
            square = pygame.image.load("explosion.png")
            start_time = time.time()
            elapsed_time = time.time() - start_time
            if(elapsed_time == 2):
                square = pygame.image.load("helicopter.png")
            
            
    screen.blit(circle, (spritex, spritey))
    pygame.display.flip()
    pos = pos + 0.15

