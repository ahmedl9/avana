#define BUTTON 12
#define JOYX A0
#define JOYY A1
#define LIGHT A2
#define TEMP A3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  //Serial.println("Hello, beginning program...");

  pinMode(BUTTON, INPUT_PULLUP); // Arduino automatically does pullup resistor for us
  pinMode(JOYX, INPUT);
  pinMode(JOYY, INPUT);
  pinMode(LIGHT, INPUT);
  pinMode(TEMP, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = digitalRead(BUTTON);
  // Serial.println(reading);
  if (reading == 0) {
    //Serial.print("button pressed: ");
    Serial.println("-10");
  }
  int xRead = analogRead(JOYX); // Center at 517
  int yRead = analogRead(JOYY); // Center at 516

  int lightRead = analogRead(LIGHT);
  //Serial.print("Light value: ");
  //Serial.println(lightRead);

  //Serial.print("X value: ");
  Serial.println(xRead);
  //Serial.print("Y value: ");
  //Serial.println(yRead);
  delay(100);

  
}
