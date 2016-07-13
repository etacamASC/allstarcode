from Myro import *
init("sim")
penDown()
x=2
i=0
while x<3:
    while i<4:
       forward(1,x)
       turnBy(90)
       i=i+1
    x=x+2
while x<5:
    while i<8:
       forward(1,x)
       turnBy(90)
       i=i+1
    x=x+2