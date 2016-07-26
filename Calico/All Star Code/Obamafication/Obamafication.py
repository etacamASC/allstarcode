#Code will change the pixels of an image to...#
#recreate a similar image from Obama's 2008...#
#presidential campaign#

from Myro import *
ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)
pic=makePicture(pickAFile())
for pixel in getPixels(pic):
    gray=getGray(pixel)
    if gray>180:
        setColor(pixel,ObamaYellow)
    elif gray>120:
        setColor(pixel,ObamaBlue)
    elif gray>60:
        setColor(pixel,ObamaRed)
    else:
        setColor(pixel,ObamaDarkBlue)
show(pic)