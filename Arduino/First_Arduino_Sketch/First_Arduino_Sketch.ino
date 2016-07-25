int LED = 9;
int LEDx = 12;
int fadeAmount = 5;
int brightness = 0;

void setup() {
pinMode(LED, OUTPUT); 
pinMode(LEDx, OUTPUT);
}


void loop() {
analogWrite(LED, brightness);
brightness = brightness + fadeAmount;
if (brightness <= 0 || brightness >= 225) {
  fadeAmount = -fadeAmount;
}
delay(40);
digitalWrite(LEDx, 1);
delay(40);
digitalWrite(LEDx, 0); 
delay(40);

}
