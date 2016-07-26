#Game adapted from the game MASH#

from random import *

print ("Let's play MASH")

myWives=["Justin Bieber","Miley Cyrus","Kim Kardasian"]
myWives.append(raw_input("Who do you want to marry?"))


myPets=["Donkey","Cow","Rat"]
myPets.append(raw_input("What type of pet do you want?"))

myRec=["Striper","Con-artist","Terrorist"]
myRec.append(raw_input("What do you want to be known as?"))

myCars=["Mercedes-Benz Maybach Exelero","Lexus RX 350", "Ford Escape"]
myCars.append(raw_input("What type of car do you want?"))

print ("You'll marry...")
print (choice(myWives))

print ("Your pet will be a...")
print (choice(myPets))

print ("You will be known as a...")
print (choice(myRec))

print ("Your car will be a...")
print (choice(myCars))