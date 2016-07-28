//Game adapted from the game MASH#

alert ("Let's play MASH");

var myWives=["Justin Bieber.","Miley Cyrus.","Kim Kardasian."];
var wiveInput=prompt("Who do you want to marry?");
myWives.push(wiveInput+".");
var Wives=myWives[Math.floor(Math.random()*myWives.length)];

var myPets=["donkey.","cow.","rat."];
var petInput=prompt("What type of pet do you want?");
myPets.push(petInput+".");
var Pets=myPets[Math.floor(Math.random()*myPets.length)];

var myRec=["striper.","con-artist.","terrorist."];
var recInput=prompt("What do you want to be known as?");
myRec.push(recInput+".");
var Rec=myRec[Math.floor(Math.random()*myRec.length)];

var myCars=["Mercedes-Benz Maybach Exelero.","Lexus RX 350.", "Ford Escape."];
var carInput=prompt("What type of car do you want?");
myCars.push(carInput+".");
var Cars=myCars[Math.floor(Math.random()*myCars.length)];


alert ("You'll marry "+Wives);

alert ("Your pet will be a "+Pets);

alert ("You will be known as a "+Rec);

alert ("Your car will be a "+Cars);
