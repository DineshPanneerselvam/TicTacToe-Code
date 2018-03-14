import pygame
import random
import os
import time

pygame.init()

display_width = 800
display_height = 600

userimg = pygame.image.load("user.png")
compimg = pygame.image.load("comp.png")
background = pygame.image.load("background.jpg")
dd = pygame.image.load("dd1.jpg")
bb = pygame.image.load("bb.jpg")

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('DANGER TIC TAC TOE')

a = [0,99,99,99,99,99,99,99,99,99,0,0]
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_blue = (0,0,64)

def initit():
    i = 1
    while i < 10:
        a[i] = 99
        i += 1

def head():
    font = pygame.font.SysFont('chillerregular',70)
    text = font.render('TIC TAC TOE',True,black)
    textrect = text.get_rect()
    textrect.center = (330,23)
    display.blit(text,textrect)

def intro():
    display.blit(bb,(0,0))
    display.blit(dd,(280,100))
    font = pygame.font.SysFont('chillerregular',70)
    textsur = font.render('DD SOLUTION',True,black)
    textrect = textsur.get_rect()
    textrect.center = ((display_width/2),(350))
    display.blit(textsur,textrect)
    pygame.display.update()
    time.sleep(3)

def font(x):
    font = pygame.font.SysFont('cosmicsansms',x)
    return font

def quits():
    intro()
    pygame.quit()
    quit()

def quitbutton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        
    if 650+150 > mouse[0] > 650 and 500+75 > mouse[1] > 500:
        pygame.draw.rect(display,blue,[650,500,100,50])
        if click[0] == 1:
            intro()
            pygame.quit()
            quit()
    else :
        pygame.draw.rect(display,light_blue,[650,500,100,50])        
    font = pygame.font.SysFont('chilleregular',25)
    textsuf = font.render('QUIT',True,white)
    textrect = textsuf.get_rect()
    textrect.center =((650+(100/2)),(500+(50/2)))
    display.blit(textsuf,textrect)
    pygame.display.update()

def userscore():
    font = pygame.font.SysFont('cosmicsansms',30)
    text = font.render('User : '+str((a[10])),True,black)
    display.blit(text,(700,25))

def compscore():
    font = pygame.font.SysFont('cosmicsansms',30)
    text = font.render('Comp : '+str((a[11])),True,black)
    display.blit(text,(700,45))

def text_object(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def gameover():
    font = pygame.font.SysFont('cosmicsansms',55)
    textsurface,textrect = text_object('DRAW!!!',font)
    textrect.center = ((325),75)
    display.blit(textsurface,textrect)
    pygame.display.update()
    time.sleep(2)

def win_message(text):
    font = pygame.font.SysFont('cosmicsansms',55)
    textsurface,textrect = text_object(text+' WIN!!!',font)
    textrect.center = (325,75)
    display.blit(textsurface,textrect)
    pygame.display.update()
    time.sleep(2)

def turn(x):
    font = pygame.font.SysFont('chillerregular',30)
    pixel = (580,325)
    if x == 1:
        text = font.render('COMPUTER TURN',True,black)
    elif x ==0:
        text = font.render('YOUR TURN',True,black)
    display.blit(text,pixel)
    pygame.display.update()


def checkwin():
    i=1
    while i<=7:
        if (a[i]+a[i+1]+a[i+2]) == 101:
            for j in range(i,(i+3)):
                if a[j] == 99:
                    return j;
        i += 3
    i=1
    while i<=3:
        if(a[i]+a[i+3]+a[i+6]) == 101:
            j=i
            k=i+6
            while j<=k:
                if a[j] == 99:
                    return j;
                j +=3
        i += 1
    if a[1]+a[5]+a[9] == 101:
        j=1
        while j <= 9:
            if a[j] == 99:
                return j;
            j += 4
    if a[3]+a[5]+a[7] == 101:
        j=3
        while j <= 7:
            if a[j] == 99:
                return j;
            j += 2
    return 0

def checkopp():
    i=1
    while i<=7:
        if (a[i]+a[i+1]+a[i+2]) == 99:
            for j in range(i,(i+3)):
                if a[j] == 99:
                    return j;
        i += 3
    i=1
    while i<=3:
        if(a[i]+a[i+3]+a[i+6]) == 99:
            j=i
            k=i+6
            while j<=k:
                if a[j] == 99:
                    return j;
                j +=3
        i += 1
    if a[1]+a[5]+a[9] == 99:
        j=1
        while j <= 9:
            if a[j] == 99:
                return j;
            j += 4
    if a[3]+a[5]+a[7] == 99:
        j=3
        while j <= 7:
            if a[j] == 99:
                return j;
            j += 2
    return 0

def present():
    for i in range(1,10):
        if a[i] == 99:
            return 1;
    return 0;

def win():
    i=1
    while i<=7:
        if (a[i]+a[i+1]+a[i+2]) == 0:
            return 0;
        i += 3
    i=1
    while i<=3:
        if(a[i]+a[i+3]+a[i+6]) == 0:
            return 0;
        i += 1
    if a[1]+a[5]+a[9] == 0:
        return 0;
    if a[3]+a[5]+a[7] == 0:
        return 0;
    i=1
    while i<=7:
        if (a[i]+a[i+1]+a[i+2]) == 3:
            return 1;
        i += 3
    i=1
    while i<=3:
        if(a[i]+a[i+3]+a[i+6]) == 3:
            return 1;
        i += 1
    if a[1]+a[5]+a[9] == 3:
        return 1;
    if a[3]+a[5]+a[7] == 3:
        return 1;
    return 5;

def available(x):
    if a[x] == 99:
        return 1
    return 0

userscr = 0
compscr = 0

def user():
    #os.system('cls')
    #sp.call('cls',shell=True)
    displays()
    x = win()
    if x == 1:
        win_message("COMPUTER IS ")
        a[11] += 1
        time.sleep(2)
        initit()
        gameloop()
    y = present()
    if y ==0:
        gameover()
        initit()
        gameloop()

    turn(0)
    pygame.display.update()
    while 1:
        quitbutton()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quits()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1:
            if 100 < mouse[0] < 250 :
                if 120 < mouse[1] < 270:
                    if available(1) == 1:
                        a[1] = 0
                        comp()
                if 170 < mouse[1] < 420 :
                    if available(4) == 1:
                        a[4] = 0
                        comp()
                if 420 < mouse[1] < 570:
                    if available(7) == 1:
                        a[7] = 0
                        comp()

            if 250 < mouse[0] < 400:
                if 120 < mouse[1] < 270:
                    if available(2):
                        a[2] = 0
                        comp()
                if 170 < mouse[1] < 420:
                    if available(5):
                        a[5] = 0
                        comp()
                if 420 < mouse[1] < 570:
                    if available(8):
                        a[8] = 0
                        comp()
            if 400 < mouse[0] < 550:
                if 120 < mouse[1] < 270:
                    if available(3):
                        a[3] = 0
                        comp()
                if 170 < mouse[1] < 420:
                    if available(6):
                        a[6] = 0
                        comp()
                if 420 < mouse[1] < 570:
                    if available(9):
                        a[9] = 0
                        comp()
def comp():
    #os.system('cls')
    #sp.call('cls',shell=True)
    displays()
    quitbutton()
    x = win()
    if x == 0:
        win_message("YOU ARE")
        a[10] += 1
        initit()
        gameloop()
    y = present()
    if y ==0:
        gameover()
        initit()
        gameloop()
    turn(1)
    pygame.display.update()
    time.sleep(1)
    x = checkwin()
    if x != 0:
        a[x] = 1
        user() 
    y = checkopp()
    if y != 0:
        a[y] = 1
        user()
    if a[5] == 99:
        a[5] = 1
        user()
    for i in range(1,20):
        x = random.randrange(1,10)
        if a[x] == 99:
            a[x] = 1
            user()
    i = 1
    while i<10:
        if a[i]==99:
            a[i] = 1
            user()
        i +=1




def displays():
    display.blit(background,(0,0))
    head()
    userscore()
    compscore()
    i=1
    pygame.draw.line(display,black,(100,120),(550,120),5)#top
    pygame.draw.line(display,black,(250,120),(250,570),5)#frst line right
    pygame.draw.line(display,black,(400,120),(400,570),5)#scnd line right
    pygame.draw.line(display,black,(100,120),(100,570),5)#zero line right
    pygame.draw.line(display,black,(550,120),(550,570),5)#Last line right
    pygame.draw.line(display,black,(100,270),(550,270),5)#frst line down
    pygame.draw.line(display,black,(100,420),(550,420),5)#scnd line down
    pygame.draw.line(display,black,(100,570),(550,570),5)#down
    if a[1] == 0:
        display.blit(userimg,(125,145))
    if a[2] == 0:
        display.blit(userimg,(275,145))
    if a[3] == 0:
        display.blit(userimg,(425,145))
    if a[4] == 0:
        display.blit(userimg,(125,295))
    if a[5] == 0:
        display.blit(userimg,(275,295))
    if a[6] == 0:
        display.blit(userimg,(425,295))
    if a[7] == 0:
        display.blit(userimg,(125,445))
    if a[8] == 0:
        display.blit(userimg,(275,445))
    if a[9] == 0:
        display.blit(userimg,(425,445))


    if a[1] == 1:
        display.blit(compimg,(125,145))
    if a[2] == 1:
        display.blit(compimg,(275,145))
    if a[3] == 1:
        display.blit(compimg,(425,145))
    if a[4] == 1:
        display.blit(compimg,(125,295))
    if a[5] == 1:
        display.blit(compimg,(275,295))
    if a[6] == 1:
        display.blit(compimg,(425,295))
    if a[7] == 1:
        display.blit(compimg,(125,445))
    if a[8] == 1:
        display.blit(compimg,(275,445))
    if a[9] == 1:
        display.blit(compimg,(425,445))
    pygame.display.update()
        

def gameloop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quits()
        displays()
        x = random.randrange(0,2)
        if x == 0:
            user()
        else :
            comp()

gameloop()
