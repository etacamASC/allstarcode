def setup():
    size(500,500)
    background(255,255,255)
    pic=loadImage("Trump.png")
    image(pic,0,0,250,100)
    myPic=loadImage("Kim.jpg")
    image(myPic,250,0,250,100)

def draw():
    global pic
    global myPic
    noStroke()
    if mousePressed:
        if mouseY<100:
            if mouseX<250:
                pic=loadImage("Trump.png")
            if mouseX>250:
                myPic=loadImage("Kim.jpg")
        elif mouseY>100:
            pic=loadImage("Trump.png")
            myPic=loadImage("Kim.jpg")
            if pic:
                image(pic,mouseX,mouseY,125,50)
            if myPic:
                image(myPic,mouseX,mouseY,125,50)