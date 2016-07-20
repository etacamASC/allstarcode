from random import *
p=0
xList=[0,100,200,300,400]
yList=[0,100,200,300,400]
def setup():
    global pic, sX, sY, p, xList, yList
    size(500,500)
    pic=loadImage("Ship.png")
    fill(255,0,255)
    x=0
    y=0
    z=0
    i=0
    eList=[100,200,300,400,500]
    while p<1:
        sX=choice(xList)
        sY=choice(yList)
        image(pic,sX,sY,100,100)
        p=p+1
    while i<5:
        while z<5:
            rect(x,y,100,100)
            x=x+100
            z=z+1
        y=y+100
        x=0
        z=0
        i=i+1
def draw():
    global pic, sX, sY, p, xList, yList
    
def mouseClicked():
    global sX,sY, e, pic, xList, yList
    if mouseX>sX and mouseX<sX+100 and mouseY>sY and mouseY<sY+100:
        background(0,255,255)
        textSize(64)
        text("You Win", 125, 200)
        fill(0, 102, 153)
        image(pic,150,250,200,200)