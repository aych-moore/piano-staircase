// pins numbers
const byte backButton = 11;
const byte forwardButton = 12;
const byte trigPins[8] = {A0,A1,A2,A3,A4,A5,A6,A7};
const byte echoPins[8] = {3,4,5,6,7,8,9,10};

int mode = 0;
const byte maxModes = 3;

// defines variables
long duration;

//distances to be sent to pi
int distances[8] = {0,0,0,0,0,0,0,0};

void setup() {
  
  // define pin modes
  pinMode(backButton,INPUT_PULLUP);
  pinMode(forwardButton,INPUT_PULLUP);
  for(byte i = 0; i < 8; i++){
    pinMode(echoPins[i], INPUT); // Sets the echoPin as an Input
    pinMode(trigPins[i], OUTPUT); // Sets the trigPin as an Output
  }
  
  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  /*
  for(byte j = 0; j < 2; j++){
    for(byte i = 0; i < 8; i += 2){
      digitalWrite(trigPins[i+j], LOW); // Clears the trigPin
      delayMicroseconds(2);
      
      digitalWrite(trigPins[i+j], HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
      delayMicroseconds(10);
      digitalWrite(trigPins[i+j], LOW);
      
      distances[i+j] = pulseIn(echoPins[i], HIGH, 10000UL)*0.034/2; // Reads the echoPin, returns the sound wave travel time in microseconds then converts to distance
    }
  }
*/
  for(byte i = 0; i < 8; i++){
    digitalWrite(trigPins[i], LOW); // Clears the trigPin
    delayMicroseconds(5);
    
    digitalWrite(trigPins[i], HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
    delayMicroseconds(10);
    digitalWrite(trigPins[i], LOW);
    
    distances[i] = pulseIn(echoPins[i], HIGH, 10000UL)*0.034/2; // Reads the echoPin, returns the sound wave travel time in microseconds then converts to distance
  }

  /*
  for(byte j = 0; j < 2; j++){
    for(byte i = 0; i < 8; i += 2){
      digitalWrite(trigPins[i+j], LOW); // Clears the trigPin
    }
    delayMicroseconds(2);
  
    for(byte i = 0; i < 8; i += 2){
      digitalWrite(trigPins[i+j], HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
    }
    delayMicroseconds(10);
    for(byte i = 0; i < 8; i += 2){
      digitalWrite(trigPins[i+j], LOW);
    }
  
    for(byte i = 0; i < 8; i += 2){
      distances[i+j] = pulseIn(echoPins[i], HIGH, 10000UL)*0.034/2; // Reads the echoPin, returns the sound wave travel time in microseconds then converts to distance
    }
  }
  */

  if(digitalRead(forwardButton) == 0){ //forward pressed
    mode += 1;
    if(mode > maxModes-1){
      mode = 0;
    }
    delay(500);
  }
  if(digitalRead(backButton) == 0){ //forward pressed
    mode -= 1;
    if(mode < 0){
      mode = maxModes-1;
    }
    delay(500);
  }
  



  /* OUTPUT FORMAT:
   *     mode,distance,distance,distance,distance,distance,distance,distance
   *  eg 1,14,0,167,23,0,0,0,99
   *  mode: int 0, room for expansion eg 0-10 modes
   *  distance: int
   */


  Serial.print(String(mode));
  for(byte i = 0; i < 8; i++){
    Serial.print(",       ");
    Serial.print(distances[i]);
    
  }
  Serial.println();
}
