// Project 3 - Traffic Lights

int ledDelay = 10000; // delay in between changes
int redPin = 10;
int yellowPin = 9;
int greenPin = 8;

void setup() {
pinMode(redPin, OUTPUT);
pinMode(yellowPin, OUTPUT);
pinMode(greenPin, OUTPUT);
}

void loop() {
// turn the red light on
digitalWrite(redPin, HIGH);
delay(ledDelay);
// turn the yellow light on
digitalWrite(yellowPin, HIGH);
delay(2000);
// turn the green light on
digitalWrite(greenPin, HIGH);
// turn the red light off
digitalWrite(redPin, LOW);
// turn the yellow light off
digitalWrite(yellowPin, LOW);
delay(ledDelay);
// turn the yellow light on
digitalWrite(yellowPin, HIGH);
// turn the green light off
digitalWrite(greenPin, LOW);
delay(2000);
// turn the yellow light off
digitalWrite(yellowPin, LOW);
}
