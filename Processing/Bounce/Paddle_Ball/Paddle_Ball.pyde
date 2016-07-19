from time import *
from random import *

xCoordinate=237.5
yCoordinate=237.5
xSpeed = randint(1,5)
ySpeed = randint(1,5)
def setup():
    size(500,500)
    background(0,255,0)
    
def draw():
    global xCoordinate, yCoordinate, xSpeed, ySpeed
    noStroke()
    background(0,255,0)
    fill(0,0,255)
    rect(mouseX,425,50,10)
    fill(255,0,0)
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
        
    sleep(.01)