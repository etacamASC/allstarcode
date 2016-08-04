confirm("Hello, my name is Erik Tacam.");
var input = prompt("What's your name?");
alert ("Hi " + input + "!");

$.post("https://maker.ifttt.com/trigger/Visitor:/with/key/bIP_dzQAxmUS1ms8zyYW1y",{
	"value1":input
});
