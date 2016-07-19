Color=raw_input("What color car do you want?")
Brand=raw_input("Toyota or Ford?")
Text=raw_input("What number do you want?")
Width=raw_input("What width is the car?")
Length=raw_input("How long do you want the car to be?")

size(500,500)

def makeCar(Color,Brand,Text,Width,Length):
    if Color==red:
        fill(255,0,0)
        rect(250,250,Width,Length)
    if Color==green:
        fill(0,255,0)
        rect(250,250,Width,Length)
    if Color==blue:
        fill(0,0,255)
        rect(250,250,Width,Length)
    else:
        fill(255,0,255)
        rect(250,250,Width,Length)
    if Brand==Toyota:
        pic=loadImage("Toyota.jpg")
        image(pic,250,250)
    if Brand==Ford:
        myPic=loadImage("Ford.jpg")
        image(myPic,250,250)
    textSize(32)
    text("Text",10,20)
    fill(0,102,153)   
        
makeCar(red, "Toyota", "ASC", 20, 30) 

        