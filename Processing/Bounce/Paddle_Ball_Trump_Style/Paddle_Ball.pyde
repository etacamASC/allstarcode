from time import *
from random import *

xCoordinate=237.5
yCoordinate=237.5
xSpeed = randint(1,10)
ySpeed = randint(1,10)
def setup():
    size(500,500)
    pic = loadImage("Trump.png")
    background(0)
    image(pic,0,0,500,500)
    
def draw():
    global xCoordinate, yCoordinate, xSpeed, ySpeed, pic
    noStroke()
    pic = loadImage("Trump.png")
    background(0)
    image (pic,0,0,500,500)
    fill(255,0,0)
    rect(mouseX,425,50,10)
    fill(0)
    ellipse(xCoordinate,yCoordinate,25,25)
    
    xCoordinate += xSpeed
    yCoordinate += ySpeed
    
    if xCoordinate > 487.5:
        xSpeed = -1 * xSpeed
    if xCoordinate < -.1:
        xSpeed = -1 * xSpeed
    if yCoordinate > 487.5:
        ySpeed = -1 * ySpeed
    if yCoordinate < -.1:
        ySpeed = -1 * ySpeed 
    if yCoordinate > 412.5 and xCoordinate > mouseX and xCoordinate < mouseX + 25:
        ySpeed = -1 * ySpeed
        xSpeed = -1 * xSpeed
        
    sleep(0)