#Alex Popovic
#main.py
#main file for markos gay ass game.

from pygame import*
from random import*
from math import*
from pprint import*

screen=display.set_mode((1280,720))

mainpic=image.load("background.jpg")
resetPic=image.load("reset.png")
resetClickedPic=image.load("resetClicked.png")
purchasePic=image.load("purchase.png")
purchaseClickedPic=image.load("purchaseClicked.png")

def clearGrid(lst): #makes whatever grid u pass all zeroes
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = 0
        
def drawGrid(): #drawing of grid happens here, draws main,temp and hover all based on values inside
    for i in range(len(seats[0])):
        for j in range(len(seats)):
            if seats[j][i] == 1: #selected seats
                 draw.rect(screen,(57,226,113),Rect(215 + 34*j, 34*i, 34, 34), 0)
            elif temp[j][i] == 1: #temp selected seats
                draw.rect(screen,(20,184,255),Rect(215 + 34*j, 34*i, 34, 34), 0)
            elif hover[j][i] == 1: #hovering seats
                draw.rect(screen,(125,125,125),Rect(215 + 34*j, 34*i, 34, 34),0)
            
            draw.rect(screen,(0,0,0),Rect(215 + 34*j, 34*i, 34, 34), 1)

def reset(): #resets everything temp
    global tempTotal,tempNum
    tempTotal = 0
    tempNum = 0
    clearGrid(temp)


def selectSeat(): #selects a seat temporarily, changes temp list plus temp values to make it all work
    global tempTotal,tempNum
    for i in range(len(seats[0])):
        for j in range(len(seats)):
            if 215 + 34*j <= mx <= 215 + 34*(j+1) and 34*i <= my <= 34*(i+1):
                if seats[j][i] != 1:
                    if temp[j][i] == 1:
                        temp[j][i] = 0
                        tempTotal-= costs[i]
                        tempNum-=1
                    elif temp[j][i] == 0:
                        temp[j][i] = 1
                        tempTotal+= costs[i]
                        tempNum+=1

def hoverSeat(): #hover a seat, changes value in hover list so draw makes it gray.
    for i in range(len(seats[0])):
        for j in range(len(seats)):
            if 215 + 34*j <= mx < 215 + 34*(j+1) and 34*i <= my < 34*(i+1):
                hover[j][i] = 1

def drawButtons(): #draws the reset and buy buttons
    for button in buttons:
        draw.rect(screen,(125,125,125),button,0)
        
def buySeats(): #resets temp after putting all of temp in the real list, transfers temp purch to real purch.
    global total,tempTotal,num,tempNum
    total+= tempTotal
    num+= tempNum
    for i in range(len(seats[0])):
        for j in range(len(seats)):
            if temp[j][i] == 1:
                seats[j][i] = 1
    reset()

def clearScreen(): #resets the hover, cleans the screen
    draw.rect(screen,(0,0,0),Rect(0,0,1280,720),0)
    clearGrid(hover)
    
    


resetRect = Rect(1080,510,185,90)
buyRect = Rect(1080,610,185,90)
buttons = [resetRect,buyRect]
    
seats  = [[0]*20 for i in range(25)]
temp   = [[0]*20 for i in range(25)]
hover  = [[0]*20 for i in range(25)]

costs = [12]*5 +[8.50]*6 + [6.25]*9
total = 0
tempTotal = 0
num =0
tempNum = 0

font.init()     #Start the font
comicFont = font.SysFont("ComicSansMS",20)
comicFontSmall = font.SysFont("ComicSansMS",18)


running=True
while running:
    click = False               #Keep track of everytime button is clicked or let go of.
    unclick = False

    clearScreen()
    screen.blit(mainpic,(0,0))
    screen.blit(resetPic,(1080,510))
    screen.blit(purchasePic,(1080,610))

    totalText = comicFont.render("Total",True,(0,0,0))
    selectedText = comicFont.render("Selected",True,(0,0,0))
    moneyText = comicFont.render("$",True,(0,0,0))
    numberText = comicFont.render("#",True,(0,0,0))
    totalMoney = comicFontSmall.render(str(total),True,(0,0,0))
    totalNumero = comicFontSmall.render(str(num),True,(0,0,0))
    tempMoney = comicFontSmall.render(str(tempTotal),True,(0,0,0))
    tempNumero = comicFontSmall.render(str(tempNum),True,(0,0,0))
    
    screen.blit(totalText,(1192,80))
    screen.blit(selectedText,(1085,80))
    screen.blit(moneyText,(1070,160))
    screen.blit(numberText,(1070,120))
    screen.blit(totalMoney,(1200,160))
    screen.blit(totalNumero,(1200,120))
    screen.blit(tempMoney,(1125,160))
    screen.blit(tempNumero,(1125,120))

    for evnt in event.get():
        if evnt.type==QUIT:
            running=False

        if evnt.type == MOUSEBUTTONDOWN :
            if evnt.button==1:
                click=True
        if evnt.type == MOUSEBUTTONUP :
            unclick=True
            
        event.get()
            
    mx,my = mouse.get_pos()     #Keep track of mouse pos
    mb = mouse.get_pressed()    #Keep track of mouse clicks
    keys=key.get_pressed()      #Keep track of keys pressed

    if click: #should add undo plus add text
        selectSeat()

    if buyRect.collidepoint(mx,my):
        screen.blit(purchaseClickedPic,(1080,610))
        if click:
            buySeats()

    if resetRect.collidepoint(mx,my):
        screen.blit(resetClickedPic,(1080,510))
        if click:
            reset()
                    
    hoverSeat()    
    drawGrid()
            
    time.wait(0)
    display.flip()
    
quit()
