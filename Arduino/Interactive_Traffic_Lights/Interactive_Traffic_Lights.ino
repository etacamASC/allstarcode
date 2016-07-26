// Project 4 - Interactive Traffic Lights

// assign the car lights
int carRed = 12;
int carYellow = 11;
int carGreen = 10;
// assign the pedestrian lights
int pedRed = 9;
int pedGreen = 8;
// button pin
int button = 2;
// time allowed to cross
int crossTime = 5000;

unsigned long changeTime; // time since button pressed

void setup() {
pinMode(carRed, OUTPUT);
pinMode(carYellow, OUTPUT);
pinMode(carGreen, OUTPUT);
pinMode(pedRed, OUTPUT);
pinMode(pedGreen, OUTPUT);
pinMode(button, INPUT);
// passing for cars
digitalWrite(carGreen, HIGH);
digitalWrite(pedRed, HIGH);
}

void loop() {
int state = digitalRead(button);
if (state == HIGH && (millis() - changeTime) > 5000) {
// Call the function to change the lights
changeLights();
  }
}

void changeLights() {
digitalWrite(carGreen, LOW); // green off
digitalWrite(carYellow, HIGH); // yellow on
delay(2000); // wait 2 seconds
digitalWrite(carYellow, LOW); // yellow off
digitalWrite(carRed, HIGH); // red on
delay(1000); // wait 1 second till its safe
digitalWrite(pedRed, LOW); // ped red off
digitalWrite(pedGreen, HIGH); // ped green on
delay(crossTime); // wait for preset time period
// flash the ped green
for (int x=0; x<10; x++) {
digitalWrite(pedGreen, HIGH);
delay(250);
digitalWrite(pedGreen, LOW);
delay(250);
}
// turn ped red on
digitalWrite(pedRed, HIGH);
delay(500);
digitalWrite(carYellow, HIGH); // yellow on
digitalWrite(carRed, LOW); // red off
delay(1000);
digitalWrite(carGreen, HIGH);
digitalWrite(carYellow, LOW); // yellow off
changeTime = millis();
}
