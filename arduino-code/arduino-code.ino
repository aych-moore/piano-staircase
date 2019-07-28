String instrument = "piano";
byte note = random(8);

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  for(int i = 0; i < 20; i++){
    instrument = "piano";
    note = random(8);
    Serial.println(instrument + ',' + String(note));
    delay(500);
  }
  for(int i = 0; i < 20; i++){
    instrument = "drums";
    note = random(8);
    Serial.println(instrument + ',' + String(note));
    delay(500);
  }

}
