#game

from pygame import*
from random import*
from math import*
from pprint import*

screen=display.set_mode((1280,720))

def clearGrid(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = 0
        
def drawGrid():
    for i in range(20):
        for j in range(10):
            if pressed[j][i] == 1 or temp[j][i] == 1:
                 draw.rect(screen,(255,255,255),Rect(400 + 35*j, 674 - 35*i, 35, 35), 0)    
            else:
                draw.rect(screen,(255,255,255),Rect(400 + 35*j, 674 - 35*i, 35, 35), 1)

def reset():
    draw.rect(screen,(0,0,0),Rect(0,0,1280,720),0)
    for i in range(20):
        for j in range(10):
            temp[j][i] = 0
    
##    locx+=1
##    locy+=1
##    
##    if locx == 10:
##        locx = 0
##        
##    if locy == 20:
##        locy = 0
##    if i == locy and j == locx:
##        draw.rect(screen,(255,255,255),Rect(400 + 35*j, 674 - 35*i, 35, 35), 0)
    
        
    
    
locx = 0
locy = 0

    
pressed = [[0]*20 for i in range(10)]
temp = [[0]*20 for i in range(10)]

running=True
while running:
    click = False #Keep track of everytime button is clicked or let go of.
    unclick = False
    
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
            
    mx,my = mouse.get_pos()  #Keep track of mouse pos
    mb = mouse.get_pressed() #Keep track of mouse clicks
    keys=key.get_pressed() #Keep track of keys pressed

    reset() 

    temp[locx][locy] = 1

    if keys[K_SPACE]:
        pressed[locx][locy] = 1
        locy+=1

    drawGrid()
    
    if locx>=0:
        locx+=1
        if locx == 10:
            locx = -1
    else:
        locx-=1
        if locx == -10:
            locx = 0
            
    time.wait(60)
    display.flip()
    
quit()
