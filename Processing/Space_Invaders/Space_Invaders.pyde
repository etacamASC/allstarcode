
from time import *
from random import *

playerX=250
playerV=5
alienV =.1
y=0

#this is the state of movement True == right, False == left
alienMoveState = True
alienPos = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
            ] 
def myAliens(x,y):
    fill(0,255,0)
    rect(x,y,30,30)
def myPlayer():
    fill(255)
    triangle(playerX,450,playerX+30,450,playerX+15,425)
def setup():
    size(500,500)
    background(0)    
def draw():
    global alienPos, alienV, alienMoveState, playerX, playerY, y
    background(0)
    myPlayer()
    Lazer()#temp
    # if keyPressed and keyCode==LEFT and playerX>0:
    #     playerX -= playerV
    # if keyPressed and keyCode==RIGHT and playerX<width-30:
    #     playerX += playerV
    # if keyPressed and keyCode==UP:
    #     y -= 1
    #draw aliens block
    for row in range(len(alienPos)):
        for col in range(len(alienPos[row])):
            if alienPos[row][col] == 1:
                if ((row+1)*55 + alienV >= width-45):
                    alienMoveState = False
                if ((row+1)*55 + alienV <= 15):
                    alienMoveState = True
               #  elif ((row+1)*55 + alienV <= (55)):
                   #     alienV *= -1
                myAliens((row+1)*(55)+alienV,(col+1)*(55))
    MoveAlien(alienMoveState)
    #draw aliens block

def Lazer():
    global playerX, y
    fill(randint(0,255), randint(0,255), randint(0,255))
    ellipse(playerX + 15, 425+y, 5, 20)

def MoveAlien(leftOrRight):
    global alienV
    if leftOrRight == True:
        alienV +=.1
    if leftOrRight == False:
        alienV -=.1

def keyPressed():
    global playerX, playerV,y 
    if keyCode==LEFT and playerX>0:
        playerX -= playerV
    if keyCode==RIGHT and playerX<width-30:
        playerX += playerV
    if keyPressed and keyCode==UP:
        y -= 1