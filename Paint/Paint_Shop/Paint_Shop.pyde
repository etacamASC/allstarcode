colorMode=1
def setup():
    size(500,500)
    background(255,255,255)
    fill(255,0,0)
    rect(0,0,250,55)
    fill(0,255,0)
    rect(250,0,250,55)

def draw():
    global colorMode
    noStroke()
    if mousePressed:
        if mouseY<55:
            if mouseX<250:
                colorMode=1
            if mouseX>250:
                colorMode=2
        elif mouseY>55:
            if colorMode==1:
                fill(255,0,0)
                ellipse(mouseX,mouseY,15,15)
            if colorMode==2:
                fill(0,255,0)
                ellipse(mouseX,mouseY,15,15)