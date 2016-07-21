from random import *
from time import *
myList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a=choice(myList)
e=0
x=0
y=randint(0,500)
def setup():
    size(500,500)
def draw():
    sleep(.01)
    global a,e,x,y
    background(0)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    textSize(32)
    text(a,x,y)
    fill(r,g,b)
    x=x+3
    if x>450:
        e=e+1
        x=0
        y=randint(0,500)
        a=choice(myList)
    if e==4:
        background(0)
        text("You Lose",180,250)
        if keyPressed:
            if key=="1":
                e=0
                background(0)
                x=0
                y=randint(0,500)
                a=choice(myList)
    if keyPressed:
        if key==a:
            background(255)
            x=0
            y=randint(0,500)
            a=choice(myList)
        elif e<4:
            e=e+1