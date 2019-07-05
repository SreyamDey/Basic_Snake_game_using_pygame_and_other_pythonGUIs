import pygame
import time
import random
pygame.init()
color=(255,255,255)
screenh=800
screenv=600
red=(255,0,0,56)
black=(0,0,0)
green=(0,200,0,100)
blocksize=10
clock=pygame.time.Clock()
gamedisplay=pygame.display.set_mode((screenh,screenv))
pygame.display.set_caption('snake')
pygame.display.update()
gameexit=False
applex=0
appley=0
length=1
x_move=screenh/2
x_change=0
y_move=screenv/2
y_change=0
s=blocksize

snakelist=[]
x=blocksize
y=blocksize
uflag=0
dflag=0
rflag=0
lflag=0
font= pygame.font.SysFont(None,25)
loopcount=1
def messagetxt(msg,clr):
    screen_text=font.render(msg,True,clr)
    gamedisplay.blit(screen_text,[400,300])

applex=round(random.randrange(0,790)/10.0)*10.0
appley=round(random.randrange(0,590)/10.0)*10.0
pygame.draw.rect(gamedisplay,(255,0,0),[applex,appley,10,10])

def snakegenerate(a,snakelist):
     for elements in snakelist:
          pygame.draw.rect(gamedisplay,green,[elements[0],elements[1],blocksize,blocksize])
    

gamedisplay.fill(color)
while not gameexit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameexit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and rflag==0:
                x_change=-10
                y_change=0
               
                lflag=1
                uflag=0
                dflag=0
            elif event.key==pygame.K_RIGHT and lflag==0:
                x_change=10
                y_change=0
               
               
                rflag=1
                uflag=0
                dflag=0
            elif event.key==pygame.K_UP and dflag==0:
                y_change=-10
                x_change=0
               
               
                uflag=1
                rflag=0
                lflag=0
            elif event.key==pygame.K_DOWN and uflag==0:
                y_change=+10
                x_change=0
               
               
                dflag=1
                rflag=0
                lflag=0
    
    

    snakehead=[]
    x_move+=x_change
    y_move+=y_change
    snakehead.append(x_move)
    snakehead.append(y_move)
    for xy in snakelist[0:-1]:
        if(snakehead[0]==xy[0] and snakehead[1]==xy[1]):
            gameexit=True
    snakelist.append(snakehead)

    if(x_move>=800 or x_move<=0 or y_move>=600 or y_move<=0):
        gameexit=True
    if(len(snakelist)>length):
         del(snakelist[0])
    
    gamedisplay.fill(color)
    snakegenerate(blocksize,snakelist)
    pygame.draw.rect(gamedisplay,red,[applex,appley,blocksize,blocksize])
    
       
    pygame.display.update()
    

    if(x_move==applex and y_move==appley):
        print("yummm")
        length+=1
        applex=round(random.randrange(0,790)/10.0)*10.0
        appley=round(random.randrange(0,590)/10.0)*10.0
        

       
       
    clock.tick(15)
    
messagetxt("Game Over",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()

