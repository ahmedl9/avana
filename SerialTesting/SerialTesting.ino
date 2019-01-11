#define BUTTON 12
#define JOYX A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.println("Hello, beginning program...");

  pinMode(BUTTON, INPUT_PULLUP); // Arduino automatically does pullup resistor for us
  pinMode(JOYX, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int reading = digitalRead(BUTTON);
  if (reading == 0) {
    Serial.println("-10");
  }
  int xRead = analogRead(JOYX); // Center at 517
  Serial.println(xRead);
  delay(150);

  
}
