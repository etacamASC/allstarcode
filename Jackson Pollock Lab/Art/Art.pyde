from random import *
xcoordinate=0
ycoordinate=0

def setup():
    size(500,500)
    background(255,255,255)

    
def draw():
    global xcoordinate
    global ycoordinate
    if mousePressed:
        noStroke()
        ellipse(mouseX,mouseY,50,50)
        fill(randint(0,255),randint(0,255),randint(0,255),randint(0,225))