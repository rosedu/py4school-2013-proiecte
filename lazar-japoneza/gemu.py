import pygame, sys
pygame.init()

class Word(object):
    def __init__(self, img, pos, name):
        self.img = img
        self.pos = pos
        self.name = name

    def is_clicked(self, pos):
        bounding_rect = self.img.get_bounding_rect()
        bounding_rect.x = self.pos[0]
        bounding_rect.y = self.pos[1]
        return bounding_rect.collidepoint(pos)


hana=Word(pygame.image.load("hana.bmp"),[50,258],"flower")
cat = Word(pygame.image.load("cat.bmp"), [50, 247], "neko")
choice=[cat,hana]

size= width, height= 700, 600
grey = 205, 205, 205
screen = pygame.display.set_mode(size)

words = []
images=[]
words.append(Word(pygame.image.load("neko.bmp"), [500, 75], "neko"))
words.append(Word(pygame.image.load("inu.bmp"), [500, 247], "inu"))
words.append(Word(pygame.image.load("tora.bmp"), [500, 418], "tora"))
images.append(Word(pygame.image.load("tree.bmp"), [500, 75], "tree"))
images.append(Word(pygame.image.load("fire.bmp"), [500, 418], "fire"))
images.append(Word(pygame.image.load("flower.bmp"), [500, 247], "flower"))

def ball():
    size = width, height = 600, 400
    speed = [1, 1]
    grey = 205, 205, 205

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("ball.bmp")
    ballrect = ball.get_rect()

    while 1:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

            ballrect = ballrect.move(speed)
            if ballrect.left < 0 or ballrect.right > width:
                    speed[0] = -speed[0]
            if ballrect.top < 0 or ballrect.bottom > height:
                    speed[1] = -speed[1]

            screen.fill(grey)
            screen.blit(ball, ballrect)
            pygame.display.flip()
    
choices = [cat, hana]


def game():
    level = 0
    while True:
        if level >= len(choices):
            print "Game finished"
            sys.exit()
        x = choices[level]
        for event in pygame.event.get():
                
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if x == cat:
                        for word in words:
                            if word.is_clicked(event.pos):
                                if word.name==x.name:
                                    
                                    level += 1
                    else:
                        for word in images:
                            if word.is_clicked(event.pos):
                                if word.name==x.name:
                                    ball()                
                                
                

        if x==cat:
            screen.fill(grey)
            for word in words:
                screen.blit(word.img, word.pos)
            screen.blit(x.img,x.pos)
            pygame.display.flip()
        else:
            screen.fill(grey)
            for word in images:
                screen.blit(word.img, word.pos)
            screen.blit(x.img,x.pos)
            pygame.display.flip()
            

game()

    

