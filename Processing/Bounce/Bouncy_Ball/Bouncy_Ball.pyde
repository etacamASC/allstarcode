from time import *
from random import *

xCoordinate=237.5
yCoordinate=237.5
xSpeed = randint(1,2)
ySpeed = randint(1,2)
def setup():
    size(500,500)
    background(255)
    
def draw():
    global xCoordinate, yCoordinate, xSpeed, ySpeed
    noStroke()
    background(255)
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
        
    sleep(.01)