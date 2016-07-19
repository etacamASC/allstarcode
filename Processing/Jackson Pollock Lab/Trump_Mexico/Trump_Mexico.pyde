from random import *
xcoordinate=0
ycoordinate=0

def setup():
    size(500,500)
    background(255,255,255)
    global pic
    
def draw():
    global xcoordinate
    global ycoordinate
    if mousePressed:
        pic=loadImage("Trump.png")
        image(pic, mouseX, mouseY, 150, 150)